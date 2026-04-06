# Repository Structure

## Source Of Truth

- PlantUML structure diagram: [repository-layout.puml](diagrams/repository-layout.puml)

## Directory Intent

- `docs/plan/`: repository purpose, scope, and extension rules
- `docs/architecture/`: public architecture explanation and context diagram
- `docs/structure/`: repository layout explanation and structure diagram
- `docs/dataset-policy/`: whitelist/blacklist and sanitization policy for published bundles
- `scripts/`: public-safe launchers, generic runtime script, and session profiles
- `datasets/`: curated measured bundles and publication manifest

## Adding A New Session Profile

Add a new folder under `scripts/sessions/<session-id>/` with:

- `blocks.tsv`
- `session.env.example`

Then add a thin wrapper `scripts/run_<session-id>.sh` that delegates to `scripts/run_session.sh`.

## Adding A New Dataset Bundle

Add a directory under `datasets/<bundle-id>/` and keep only:

- `metadata.json`
- `runbook.md`
- `operator_notes.md`
- `logs/operator_block_events.tsv`
- optional extra operator-facing notes if sanitized
- `serial/` raw measurement artifacts

Do not add:

- `analysis/`
- `analysis_handoff*`
- `experiment_report*`
- `qc_summary*`
- `session.env`
- AP snapshot/configuration logs with non-public host or version details

## Repository-Level Consistency Rules

- Update `datasets/manifest.json` whenever inclusion or exclusion decisions change.
- Keep public docs in sync with the published structure.
- Keep the new repository self-contained; do not require `cws-lab` to understand the file layout.
