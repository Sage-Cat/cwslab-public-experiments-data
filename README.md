# cwslab-public-experiments-data

Public-safe experimental launch scripts and measured dataset bundles derived from the local `cws-lab` monorepo.

This repository is a measured dataset repository and reference implementation surface for cooperative Wi-Fi sensing experiments. It keeps only the public launch surface, curated raw measurement bundles, and self-contained repository documentation. It does not claim full 802.11bf or EasyMesh compliance; the materials here are `802.11bf-inspired`, use `EasyMesh-inspired metrics/control-plane alignment`, and remain a `reference implementation` plus `measured dataset repository`.

## What This Repository Contains

- public-safe hardware launch scripts for sessions that target a `primary prplOS-compatible dual-band AP node`
- curated measured dataset bundles with raw serial captures, operator block-event logs, and sanitized metadata
- public repository docs for plan, architecture, structure, and dataset publication policy
- PlantUML sources under `docs/**/diagrams/` as the source of truth for repository diagrams

## What This Repository Excludes

- analysis, reporting, dissertation, internal planning, status reviews, and internal Codex artifacts
- `.codex/`, `reports/status/`, `docs/research/`, `site/`, `tests/`, and other non-public monorepo surfaces
- derived artifacts such as `analysis/`, `analysis_handoff*`, `experiment_report*`, and `qc_summary*`
- private or host-specific data such as absolute local paths, AP host/device identifiers, environment snapshots, credentials, and firmware workspace paths
- AP snapshot/configuration logs that expose non-public device state or version details

## Repository Layout

```text
cwslab-public-experiments-data/
├── README.md
├── datasets/
├── docs/
│   ├── architecture/
│   ├── dataset-policy/
│   ├── plan/
│   └── structure/
└── scripts/
```

## Published Dataset Surface

- `datasets/w01_e01_c1_t0_l1_baseline_20260330T101537Z/`
- `datasets/w03_e05_c2_t0_l1_low_density_support_20260330T130337Z/`
- `datasets/d01_c1_t0_l1_repeatability_20260406T095034Z/`

Machine-readable publication status lives in `datasets/manifest.json`.

## Script Surface

- `scripts/run_w01_e01_c1_t0_l1_baseline.sh`
- `scripts/run_w01_e02_c1_t0_l1_repeat.sh`
- `scripts/run_w03_e05_c2_t0_l1_low_density_support.sh`
- `scripts/run_d01_c1_t0_l1_repeatability.sh`
- `scripts/run_session.sh`
- `scripts/render_diagrams.sh`

The top-level wrappers are public-safe derivatives of the original monorepo launch wrappers. They no longer depend on the internal `cwslab` CLI and instead use session-local example configuration under `scripts/sessions/`.

## How To Extend The Repository

- Add new measured runs by following [docs/dataset-policy/policy.md](docs/dataset-policy/policy.md) and updating `datasets/manifest.json`.
- Add new launch scripts by creating a new session directory under `scripts/sessions/`, then adding a thin wrapper in `scripts/`.
- Render diagrams with `scripts/render_diagrams.sh`.

## Related Docs

- [Repository Plan](docs/plan/repository-plan.md)
- [Architecture Overview](docs/architecture/overview.md)
- [Repository Structure](docs/structure/repository-structure.md)
- [Dataset Policy](docs/dataset-policy/policy.md)
