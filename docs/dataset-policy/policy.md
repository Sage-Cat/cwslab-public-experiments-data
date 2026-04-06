# Dataset Policy

## Purpose

This policy defines what may and may not be published under `datasets/`.

## Whitelist

Allowed publication surfaces:

- raw measurement artifacts under `serial/`
- operator timing and block-event logs such as `logs/operator_block_events.tsv`
- sanitized `metadata.json`
- sanitized `runbook.md`
- sanitized `operator_notes.md`
- minimal per-bundle notes that explain curation or sanitization decisions

## Blacklist

Do not publish:

- `analysis/`
- `analysis_handoff*`
- `experiment_report*`
- `qc_summary*`
- `session.env`
- host-specific or device-specific absolute paths
- AP management hostnames, device nodes, firmware workspace paths, or local serial device names
- passphrases, tokens, secrets, or credentials
- AP snapshot or AP configure logs that expose private device state or version details
- dissertation, status, internal planning, research methodology drift notes, or private workflow artifacts

## Sanitization Rules

- Replace local paths with repository-relative language.
- Replace non-public AP/network identifiers with generic descriptions.
- Keep router naming generic: `primary prplOS-compatible dual-band AP node`.
- Preserve measured facts, timestamps, and raw capture data where publication remains safe.
- Remove derived interpretation that belongs to offline analysis or reporting.

## Inclusion Threshold

A bundle is publishable only when it contains a meaningful measured raw surface. Metadata-only or plan-only bundles should stay out of `datasets/` and may be tracked only as exclusions in `datasets/manifest.json`.

## Manifest Rule

Every publish or exclusion decision must be reflected in `datasets/manifest.json` with:

- bundle identifier
- source bundle identifier
- included surfaces
- excluded surfaces
- sanitization summary
- publication status
