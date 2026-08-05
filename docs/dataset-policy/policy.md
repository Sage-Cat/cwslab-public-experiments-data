# Dataset Policy

## Purpose

Publish reproducible measured evidence without exposing private infrastructure,
credentials, machine-specific identifiers, or internal workflow material.
`datasets/manifest.json` is the authoritative per-bundle inclusion record.

## Standard Public Surface

A sanitized bundle may include:

- measurement artifacts under `serial/`;
- operator timing/block-event logs and cooperative timing markers;
- `metadata.json`, `runbook.md`, and `operator_notes.md`;
- compact notes needed to explain curation or sanitization.

## Manifest-Approved Derived Evidence

Compact derived evidence may be published only when all conditions hold:

1. it is necessary to interpret the public measured claim surface;
2. it is sanitized and self-contained;
3. it contains no private infrastructure or internal planning material;
4. its exact path is listed in the bundle's `included_surfaces`.

Allowed shapes include bounded summaries such as:

- `analysis/<analysis-name>/summary.md`;
- `qc_summary.md`;
- `experiment_report.md`;
- a compact claim-bearing table or note with the same documented purpose.

This exception does not allow wholesale analysis trees, private handoff
packages, caches, intermediate arrays/models, or every generated report.

## Forbidden Content

Do not publish:

- unlisted or bulk `analysis/` content, `analysis_handoff*`, caches,
  intermediate/generated workspaces, or private workflow artifacts;
- `session.env` or environment/device-specific absolute paths;
- AP management hostnames, device nodes, firmware workspace paths, concrete
  SSIDs, IP/MAC/BSSID values, board serials, adapter names, passphrases, tokens,
  secrets, or credentials;
- AP snapshot/configure logs exposing private device state or version details;
- dissertation/status/internal planning material or research-methodology drift
  notes not needed to interpret the public dataset.

## Sanitization

- Replace local paths with repository-relative descriptions.
- Replace non-public network/device identifiers with generic descriptions.
- Pseudonymize repeated identifiers consistently when grouping is
  scientifically useful.
- Use `primary prplOS-compatible dual-band AP node` for the router role.
- Preserve measured facts needed for analysis: timestamps, block labels,
  channel/rate/RSSI fields, CSI values, and event timing.
- Keep derived interpretation bounded to what the published measurements
  support.

## Inclusion Threshold

Publish only bundles with a meaningful measured surface. Metadata-only or
plan-only candidates remain outside `datasets/` and may be recorded as
exclusions in the manifest.

## Manifest Rule

Every publication or exclusion decision must record:

- bundle and source-bundle identifiers;
- included and excluded surfaces;
- sanitization summary;
- publication status.

The checked-in bundle, manifest entry, and public documentation must agree.
