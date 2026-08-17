# Scripts

This directory contains the public experimental launch surface.

## Files

- `run_session.sh`: generic operator-guided runtime
- `run_*.sh`: thin wrappers for individual public session profiles
- `render_diagrams.sh`: render PlantUML diagrams from local sources
- `validate_repository.py`: validate the public manifest and privacy boundary
- `sessions/<session-id>/blocks.tsv`: block definitions for one session
- `sessions/<session-id>/session.env.example`: public-safe environment template

## Current Capability Notes

The generic runtime supports:

- one primary serial/UART capture stream
- up to two optional auxiliary command-backed capture streams for cooperative/helper-node sessions such as `D05`, `D07`, `D09`, and `D10`

## Runtime Model

The wrapper scripts expect an untracked `session.env` file next to
`session.env.example` for the selected session profile.

Do not commit concrete hostnames, addresses, credentials, SSIDs, or device
paths. The scripts remain a `reference implementation`, not a certification or
end-to-end hardware-support claim.

## Repository Validation

Run the same bounded checks used by GitHub Actions:

```text
python3 scripts/validate_repository.py
bash -n scripts/*.sh
```

The validator checks exact manifest/file agreement, JSON and gzip readability,
GitHub's per-file size limit, local documentation links, and common concrete
identifier or high-confidence credential patterns in published bundles.
