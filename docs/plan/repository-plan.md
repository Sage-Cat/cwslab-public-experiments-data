# Repository Plan

## Purpose

`cwslab-public-experiments-data` is the public-derived repository for:

- experimental launch scripts that can be reviewed independently from the source capture repository
- curated measured bundles that preserve sanitized measurement surfaces without derived analysis
- repository-level public documentation and diagrams

The repository should remain understandable without external workflow context.

## Product Boundaries

This repository includes:

- measured raw captures and operator timing/event surfaces
- sanitized metadata and operator-facing runbook material
- reference launch scripts for sessions that use a `primary prplOS-compatible dual-band AP node`

This repository intentionally excludes:

- offline analysis, report assembly, dissertation drafting, status reporting, and internal planning
- non-public helper surfaces used only for automation
- environment snapshots and hardware-specific secrets or identifiers

## Design Principles

- Keep the repository honest about evidence stage: measured data stays separate from derived claims.
- Publish sanitized measured surfaces only; derived interpretation belongs elsewhere.
- Preserve PlantUML sources as the source of truth for architecture and structure diagrams.
- Keep wording careful: `802.11bf-inspired`, `EasyMesh-inspired metrics/control-plane alignment`, and `reference implementation`.
- Avoid vendor and version naming in public docs, diagrams, comments, and examples.

## Independent Lifecycle

The repository can evolve without `cws-lab` when:

- new measured bundles are curated directly into `datasets/`
- `datasets/manifest.json` is updated with inclusion and exclusion decisions
- a new session profile is added under `scripts/sessions/`
- the top-level wrapper list is extended for new public sessions

## Adding A New Measured Run

1. Start from a measured run bundle, not from an analysis directory.
2. Copy only public-safe surfaces into `datasets/<bundle-id>/`.
3. Sanitize metadata, runbook text, and operator notes to remove:
   - absolute local paths
   - AP hostnames, device nodes, and firmware workspace paths
   - concrete SSIDs, IP addresses, MAC addresses, BSSIDs, and adapter names
   - credentials, passphrases, and secrets
   - internal plan references and non-public status notes
4. Pseudonymize serial-log identifiers while preserving measurement values.
5. Exclude derived analysis, reports, QC summaries, and environment dumps.
6. Add the bundle entry to `datasets/manifest.json`.

## Adding A New Script

1. Create `scripts/sessions/<session-id>/blocks.tsv`.
2. Create `scripts/sessions/<session-id>/session.env.example`.
3. Reuse `scripts/run_session.sh` unless a new runtime step is genuinely needed.
4. Add a thin top-level wrapper `scripts/run_<session-id>.sh`.
5. Update the structure documentation if the script surface changes materially.
