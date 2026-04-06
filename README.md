# cwslab-public-experiments-data

Public-safe launch scripts, curated measured bundles, and lightweight reference documentation for cooperative Wi-Fi sensing experiments.

This repository is a `measured dataset repository` plus a `reference implementation` surface. It keeps only the material needed to understand and reuse the published experiments:

- measured raw capture bundles
- public-safe launch wrappers
- concise documentation for structure, architecture, and dataset policy

It does not claim full 802.11bf or EasyMesh compliance. Public wording stays careful: `802.11bf-inspired`, `EasyMesh-inspired metrics/control-plane alignment`, and `reference implementation`.

## Status Snapshot

- Repository status: public-derived, self-contained dataset repository
- Published measured bundles: `4`
- Excluded raw-incomplete candidate bundles: `1`
- Git tagging rule: `experiment/<bundle-id>`
- Public hardware naming rule: `primary prplOS-compatible dual-band AP node`

## Why This Repository Exists

The scientific value of this repository is concentrated in three places:

- raw capture evidence that can be versioned and cited
- operator block-event timing that preserves the capture sequence
- compact metadata that explains what each run was meant to capture without exposing private infrastructure details

Offline analysis, dissertation writing, internal planning, status reviews, and other non-public workflow surfaces are intentionally excluded.

## Repository-Specific Notation

The identifiers below are local shorthand used by this project. They are not public standards and should be read as repository conventions.

| Token | Meaning In This Repository |
| --- | --- |
| `wNN` | Weekly experiment-series identifier used in the earlier hardware campaign workflow. |
| `eNN` | Experiment number inside a weekly series. |
| `dNN` | Dissertation-aligned experiment program identifier. |
| `C1` | Campaign code for single-link baseline and repeatability evidence on the current stand. |
| `C2` | Campaign code for single-link support/comparator captures on the same stand. |
| `T0` | The current single-link stand topology. |
| `L1` | The ordinary observed lab condition used as the honest baseline condition in the published runs here. |
| `baseline` | First structured reference capture for a condition/topology combination. |
| `repeat` | A repeated run intended to test short-term repeatability after reset or rerun. |
| `repeatability` | A more explicit repeatability evidence package, here aligned with dissertation tracking. |
| `low_density_support` | A support capture kept for later reduced-density or comparator studies rather than for a standalone final claim. |
| `W0` | Warm-up / transport sanity-check block before the main labeled sequence. |
| `E1`, `E2`, `E3` | Empty-scene blocks. |
| `S1`, `S2` | Static-presence blocks. |
| `M1`, `M2` | Motion blocks. |
| `YYYYMMDDThhmmssZ` | UTC timestamp suffix attached to a bundle identifier. |

## Main Structure

```text
cwslab-public-experiments-data/
├── README.md
├── datasets/
│   ├── manifest.json
│   └── <bundle-id>/
│       ├── metadata.json
│       ├── runbook.md
│       ├── operator_notes.md
│       ├── logs/operator_block_events.tsv
│       └── serial/
├── docs/
│   ├── plan/
│   ├── architecture/
│   ├── structure/
│   └── dataset-policy/
└── scripts/
    ├── run_session.sh
    ├── run_*.sh
    └── sessions/<session-id>/
```

## Published Experiments

| Bundle ID | Git Tag | UTC Timestamp | Focus | Research Shorthand | Capture Surface |
| --- | --- | --- | --- | --- | --- |
| `w01_e01_c1_t0_l1_baseline_20260330T101537Z` | `experiment/w01_e01_c1_t0_l1_baseline_20260330T101537Z` | `2026-03-30T10:15:37+00:00` | First structured single-link baseline session with fixed operator blocks. | `C1 / T0 / L1` | Raw serial log + operator block-event log |
| `w03_e05_c2_t0_l1_low_density_support_20260330T130337Z` | `experiment/w03_e05_c2_t0_l1_low_density_support_20260330T130337Z` | `2026-03-30T13:03:37+00:00` | Support capture for reduced-density and comparator studies on the same stand. | `C2 / T0 / L1` | Raw serial log + operator block-event log |
| `d01_c1_t0_l1_repeatability_20260406T095034Z` | `experiment/d01_c1_t0_l1_repeatability_20260406T095034Z` | `2026-04-06T09:50:34+00:00` | Dissertation-aligned repeatability baseline under the same stand geometry. | `D01`, `C1 / T0 / L1` | Raw serial log + operator block-event log |
| `d01_c1_t0_l1_repeatability_20260406T113903Z` | `experiment/d01_c1_t0_l1_repeatability_20260406T113903Z` | `2026-04-06T11:39:03+00:00` | Dissertation-aligned repeatability baseline rerun under the same stand geometry with full block coverage. | `D01`, `C1 / T0 / L1` | Raw serial log + operator block-event log |

## What A Published Bundle Contains

- `metadata.json`: sanitized session metadata and block definitions
- `runbook.md`: compact bundle-level summary
- `operator_notes.md`: sanitized operator-facing notes and block instructions
- `logs/operator_block_events.tsv`: machine-readable timing for the labeled block sequence
- `serial/esp32_guided_session.log`: raw captured stream

## Current Evidence Boundaries

Included here:

- measured raw/public-safe capture surfaces
- bundle-level metadata needed to interpret the raw files
- public-safe launch wrappers for reproducing the capture workflow

Intentionally not included here:

- offline analysis and reporting outputs
- dissertation text and internal planning
- AP snapshot/configuration logs
- environment dumps, credentials, host-specific paths, and private device identifiers

## Where To Look Next

- [Dataset Manifest](datasets/manifest.json)
- [Dataset Policy](docs/dataset-policy/policy.md)
- [Architecture Overview](docs/architecture/overview.md)
- [Repository Structure](docs/structure/repository-structure.md)
- [Repository Plan](docs/plan/repository-plan.md)
