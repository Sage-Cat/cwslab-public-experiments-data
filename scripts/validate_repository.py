#!/usr/bin/env python3
"""Validate the public dataset manifest, privacy boundary, and basic integrity."""

from __future__ import annotations

import gzip
import json
import re
import sys
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


def main() -> int:
    errors: list[str] = []

    try:
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: cannot read {MANIFEST}: {exc}", file=sys.stderr)
        return 1

    entries = manifest.get("datasets")
    if manifest.get("repository") != "cwslab-public-experiments-data":
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

    tracked_envs = list(REPO_ROOT.glob("scripts/sessions/*/session.env"))
    if tracked_envs:
        fail(errors, "concrete session.env files must not be present")

    for required in (REPO_ROOT / "README.md", REPO_ROOT / "LICENSE.md"):
        if not required.is_file():
            fail(errors, f"required repository file missing: {required.name}")

    validate_markdown_links(errors)

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(f"validated {len(bundle_ids)} manifest-listed public dataset bundles")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
