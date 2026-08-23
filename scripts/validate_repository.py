#!/usr/bin/env python3
"""Validate the public dataset manifest, privacy boundary, and basic integrity."""

from __future__ import annotations

import csv
import gzip
import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path, PurePosixPath


REPO_ROOT = Path(__file__).resolve().parent.parent
DATASETS = REPO_ROOT / "datasets"
MANIFEST = DATASETS / "manifest.json"
MAX_GITHUB_FILE_SIZE = 100 * 1024 * 1024

FORBIDDEN_PATTERNS = {
    "private key": re.compile(rb"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "GitHub token": re.compile(rb"gh[pousr]_[A-Za-z0-9_]{20,}"),
    "AWS access key": re.compile(rb"AKIA[0-9A-Z]{16}"),
    "email address": re.compile(rb"(?i)[a-z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-z0-9.-]+\.[a-z]{2,}"),
    "home-directory path": re.compile(rb"(?:/home/|/Users/)[^\s\x00]+"),
    "MAC address": re.compile(rb"(?i)(?<![0-9a-f])(?:[0-9a-f]{2}:){5}[0-9a-f]{2}(?![0-9a-f])"),
}
IPV4_CANDIDATE = re.compile(rb"(?<![0-9])(?:[0-9]{1,3}\.){3}[0-9]{1,3}(?![0-9])")
MARKDOWN_LINK = re.compile(r"\[[^]]*\]\(([^) #]+)")
NORMALIZED_BUNDLE = DATASETS / "record-level-csi-summaries-2026"
CSI_FIELDS = [
    "dataset_id",
    "receiver_id",
    "record_index",
    "capture_segment",
    "relative_host_ms",
    "relative_device_time_us",
    "total",
    "interval",
    "dropped",
    "seen",
    "mismatch",
    "zero_len",
    "rssi_dbm",
    "noise_floor_dbm",
    "rate",
    "channel",
    "secondary_channel",
    "estimator_valid",
    "estimator_length",
    "signal_length",
    "rx_state",
    "rx_sequence",
    "csi_length",
    "first_word_invalid",
    "csi_iq_preview",
]


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def safe_relative_path(value: object) -> str | None:
    if not isinstance(value, str) or not value:
        return None
    path = PurePosixPath(value)
    if path.is_absolute() or ".." in path.parts or str(path) != value:
        return None
    return value


def read_payload(path: Path) -> bytes:
    if path.suffix == ".gz":
        with gzip.open(path, "rb") as stream:
            return stream.read()
    return path.read_bytes()


def scan_public_payload(path: Path, errors: list[str]) -> None:
    try:
        payload = read_payload(path)
    except (OSError, EOFError) as exc:
        fail(errors, f"unreadable payload {path.relative_to(REPO_ROOT)}: {exc}")
        return

    for label, pattern in FORBIDDEN_PATTERNS.items():
        if pattern.search(payload):
            fail(errors, f"possible {label} in {path.relative_to(REPO_ROOT)}")

    for candidate in IPV4_CANDIDATE.findall(payload):
        octets = candidate.split(b".")
        if all(int(octet) <= 255 for octet in octets):
            fail(errors, f"IPv4 address in {path.relative_to(REPO_ROOT)}")
            break


def validate_markdown_links(errors: list[str]) -> None:
    for path in REPO_ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        for target in MARKDOWN_LINK.findall(text):
            if "://" in target or target.startswith(("mailto:", "#")):
                continue
            linked = (path.parent / target).resolve()
            if not linked.exists():
                fail(errors, f"broken local link in {path.relative_to(REPO_ROOT)}: {target}")


def validate_normalized_csi(errors: list[str]) -> None:
    checksum_file = NORMALIZED_BUNDLE / "SHA256SUMS"
    for line in checksum_file.read_text(encoding="utf-8").splitlines():
        expected, relative = line.split("  ", 1)
        path = NORMALIZED_BUNDLE / relative
        digest = hashlib.sha256()
        with path.open("rb") as stream:
            for chunk in iter(lambda: stream.read(1024 * 1024), b""):
                digest.update(chunk)
        if digest.hexdigest() != expected:
            fail(errors, f"checksum mismatch: {path.relative_to(REPO_ROOT)}")

    accounting_path = NORMALIZED_BUNDLE / "data" / "source_accounting.csv"
    with accounting_path.open(newline="", encoding="utf-8") as stream:
        accounting_rows = list(csv.DictReader(stream))
    expected_counts = {row["dataset_id"]: int(row["accepted_rows"]) for row in accounting_rows}
    if len(expected_counts) != 16 or sum(expected_counts.values()) != 347391:
        fail(errors, "normalized CSI source accounting has unexpected dataset or row totals")
    if sum(int(row["excluded_malformed_rows"]) for row in accounting_rows) != 64:
        fail(errors, "normalized CSI malformed-row accounting must equal 64")

    observed: Counter[str] = Counter()
    next_index: dict[tuple[str, str], int] = {}
    data_path = NORMALIZED_BUNDLE / "data" / "csi_summaries.csv.gz"
    with gzip.open(data_path, "rt", newline="", encoding="utf-8") as stream:
        reader = csv.DictReader(stream)
        if reader.fieldnames != CSI_FIELDS:
            fail(errors, "normalized CSI CSV header differs from the documented schema")
            return
        for line_number, row in enumerate(reader, start=2):
            try:
                dataset_id = row["dataset_id"]
                receiver_id = row["receiver_id"]
                if dataset_id not in expected_counts:
                    raise ValueError("unknown dataset_id")
                if receiver_id not in {"receiver-01", "receiver-02", "receiver-03"}:
                    raise ValueError("unknown receiver_id")
                key = (dataset_id, receiver_id)
                record_index = int(row["record_index"])
                if record_index != next_index.get(key, 0):
                    raise ValueError("non-contiguous record_index")
                next_index[key] = record_index + 1
                capture_segment = int(row["capture_segment"])
                if capture_segment < 0:
                    raise ValueError("negative capture segment")
                integer_values = {
                    name: int(row[name])
                    for name in CSI_FIELDS[4:-1]
                }
                if integer_values["relative_host_ms"] < 0 or integer_values["relative_device_time_us"] < 0:
                    raise ValueError("negative relative time")
                if not -128 <= integer_values["rssi_dbm"] <= 0:
                    raise ValueError("RSSI outside signed dBm range")
                if not -128 <= integer_values["noise_floor_dbm"] <= 0:
                    raise ValueError("noise floor outside signed dBm range")
                if not 1 <= integer_values["channel"] <= 196:
                    raise ValueError("invalid channel")
                if integer_values["csi_length"] <= 0:
                    raise ValueError("non-positive reported CSI length")
                preview = json.loads(row["csi_iq_preview"])
                if len(preview) not in {8, 16} or any(
                    type(value) is not int or value < -128 or value > 127 for value in preview
                ):
                    raise ValueError("invalid CSI I/Q preview")
            except (KeyError, TypeError, ValueError, json.JSONDecodeError) as exc:
                fail(errors, f"invalid normalized CSI row {line_number}: {exc}")
                if len(errors) >= 20:
                    return
                continue
            observed[dataset_id] += 1

    if dict(observed) != expected_counts:
        fail(errors, "normalized CSI row counts differ from source accounting")


def main() -> int:
    errors: list[str] = []

    try:
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: cannot read {MANIFEST}: {exc}", file=sys.stderr)
        return 1

    entries = manifest.get("datasets")
    if manifest.get("repository") != "wifi-sensing-site-c-experiments":
        fail(errors, "manifest repository name is missing or incorrect")
    if not isinstance(manifest.get("generated_from"), str) or not manifest["generated_from"]:
        fail(errors, "manifest generated_from provenance is missing")
    if not isinstance(entries, list) or not entries:
        fail(errors, "manifest datasets must be a non-empty list")
        entries = []

    bundle_ids: list[str] = []
    for entry in entries:
        if not isinstance(entry, dict):
            fail(errors, "manifest dataset entry is not an object")
            continue
        bundle_id = safe_relative_path(entry.get("bundle_id"))
        if bundle_id is None or "/" in bundle_id:
            fail(errors, f"unsafe bundle_id: {entry.get('bundle_id')!r}")
            continue
        bundle_ids.append(bundle_id)
        if safe_relative_path(entry.get("source_bundle")) is None:
            fail(errors, f"{bundle_id}: source_bundle provenance is missing or unsafe")
        if not isinstance(entry.get("status"), str) or not entry["status"]:
            fail(errors, f"{bundle_id}: publication status is missing")
        if not isinstance(entry.get("sanitization_summary"), list) or not entry["sanitization_summary"]:
            fail(errors, f"{bundle_id}: sanitization summary is missing")
        if not isinstance(entry.get("excluded_surfaces"), list):
            fail(errors, f"{bundle_id}: excluded_surfaces must be a list")
        bundle = DATASETS / bundle_id
        if not bundle.is_dir() or bundle.is_symlink():
            fail(errors, f"missing or unsafe bundle directory: {bundle_id}")
            continue

        included = entry.get("included_surfaces")
        if not isinstance(included, list) or not included:
            fail(errors, f"{bundle_id}: included_surfaces must be a non-empty list")
            continue
        if len(included) != len(set(map(str, included))):
            fail(errors, f"{bundle_id}: duplicate included_surfaces")

        listed: set[str] = set()
        for value in included:
            relative = safe_relative_path(value)
            if relative is None:
                fail(errors, f"{bundle_id}: unsafe included path {value!r}")
            else:
                listed.add(relative)

        actual = {
            path.relative_to(bundle).as_posix()
            for path in bundle.rglob("*")
            if path.is_file() or path.is_symlink()
        }
        for missing in sorted(listed - actual):
            fail(errors, f"{bundle_id}: manifest path missing: {missing}")
        for unlisted in sorted(actual - listed):
            fail(errors, f"{bundle_id}: unlisted public file: {unlisted}")

        for relative in sorted(actual):
            path = bundle / relative
            if path.is_symlink():
                fail(errors, f"{bundle_id}: symlinks are not allowed: {relative}")
                continue
            if path.stat().st_size >= MAX_GITHUB_FILE_SIZE:
                fail(errors, f"{bundle_id}: file reaches GitHub's 100 MiB limit: {relative}")
            if path.suffix == ".json":
                try:
                    json.loads(path.read_text(encoding="utf-8"))
                except (UnicodeDecodeError, json.JSONDecodeError) as exc:
                    fail(errors, f"{bundle_id}: invalid JSON {relative}: {exc}")
            scan_public_payload(path, errors)

    if len(bundle_ids) != len(set(bundle_ids)):
        fail(errors, "manifest contains duplicate bundle IDs")
    disk_bundles = sorted(path.name for path in DATASETS.iterdir() if path.is_dir())
    if sorted(bundle_ids) != disk_bundles:
        fail(errors, "dataset directories and manifest bundle IDs differ")

    for required in (REPO_ROOT / "README.md", REPO_ROOT / "LICENSE.md"):
        if not required.is_file():
            fail(errors, f"required repository file missing: {required.name}")

    validate_markdown_links(errors)
    validate_normalized_csi(errors)

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(f"validated {len(bundle_ids)} manifest-listed public dataset bundles")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
