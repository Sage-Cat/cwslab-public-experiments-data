# Scripts

This directory contains the public-safe experimental launch surface.

## Files

- `run_session.sh`: generic operator-guided runtime
- `run_*.sh`: thin wrappers for individual public session profiles
- `render_diagrams.sh`: render PlantUML diagrams from local sources
- `sessions/<session-id>/blocks.tsv`: block definitions for one session
- `sessions/<session-id>/session.env.example`: public-safe environment template

## Current Capability Notes

The generic runtime supports:

- one primary local serial/UART capture stream
- up to two optional auxiliary command-backed capture streams for cooperative/helper-node sessions such as `D05` and `D07`

## Runtime Model

The wrapper scripts do not depend on the `cws-lab` internal CLI. They expect a local `session.env` file next to `session.env.example` for the selected session profile.

The scripts remain a `reference implementation`. They should not be presented as validated end-to-end hardware support.
