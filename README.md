# cwslab-public-experiments-data

Public measured data and public launch scripts for cooperative Wi-Fi sensing
experiments.

This repository has two practical entry points:

- `datasets/`: curated measured experiment bundles.
- `scripts/`: the public scripts and session profiles used to collect them.

The repository is self-contained. It does not claim full 802.11bf or EasyMesh
compliance. Use the published wording as a `reference implementation` with
`802.11bf-inspired` sensing and `EasyMesh-inspired` control-plane alignment.

## Quick Start

To inspect an experiment, open its dataset folder first. Each published bundle
contains the measured logs and a compact run description.

To rerun a public launch profile, open the matching script and session profile:

```text
scripts/run_<session-id>.sh
scripts/sessions/<session-id>/
```

The tracked `session.env.example` files are templates. Keep concrete hostnames,
addresses, credentials, and device paths in an untracked local `session.env`.

## Repository Map

- [Dataset manifest](datasets/manifest.json): machine-readable publication
  index.
- [Dataset policy](docs/dataset-policy/policy.md): inclusion and sanitization
  rules.
- [Datasets](datasets/): curated measured bundles.
- [Scripts](scripts/): public launch surface.
- [Architecture notes](docs/architecture/overview.md): repository context.
- [Structure notes](docs/structure/repository-structure.md): file layout.

## Published Datasets

Each entry below links the measured bundle, launch wrapper, and session profile.
The `serial/` logs are sanitized measurement logs: network identifiers are
redacted or pseudonymized, while timestamps, block labels, channel/rate/RSSI
fields, CSI values, and event timing are preserved.

### D10 - Stability Maintenance

- Dataset:
  [`d10_c5_t2_l1_stability_maintenance_20260504T115457Z`](datasets/d10_c5_t2_l1_stability_maintenance_20260504T115457Z/)
- Script:
  [`scripts/run_d10_c5_t2_l1_stability_maintenance.sh`](scripts/run_d10_c5_t2_l1_stability_maintenance.sh)
- Profile:
  [`scripts/sessions/d10_c5_t2_l1_stability_maintenance/`](scripts/sessions/d10_c5_t2_l1_stability_maintenance/)
- Surface: three sanitized compressed serial logs, operator events,
  cooperative timing, and compact claim summaries.

### D08 - Budget-Aware Controller

- Dataset:
  [`d08_c4_t1_l1_budget_aware_controller_20260501T130657Z`](datasets/d08_c4_t1_l1_budget_aware_controller_20260501T130657Z/)
- Script:
  [`scripts/run_d08_c4_t1_l1_budget_aware_controller.sh`](scripts/run_d08_c4_t1_l1_budget_aware_controller.sh)
- Profile:
  [`scripts/sessions/d08_c4_t1_l1_budget_aware_controller/`](scripts/sessions/d08_c4_t1_l1_budget_aware_controller/)
- Surface: two sanitized serial logs, operator events, cooperative timing, and
  compact controller summaries.

### D07 - Heterogeneity And Subset Value

- Dataset:
  [`d07_c3_t2_l1_heterogeneity_subset_value_20260501T114221Z`](datasets/d07_c3_t2_l1_heterogeneity_subset_value_20260501T114221Z/)
- Script:
  [`scripts/run_d07_c3_t2_l1_heterogeneity_subset_value.sh`](scripts/run_d07_c3_t2_l1_heterogeneity_subset_value.sh)
- Profile:
  [`scripts/sessions/d07_c3_t2_l1_heterogeneity_subset_value/`](scripts/sessions/d07_c3_t2_l1_heterogeneity_subset_value/)
- Surface: three sanitized serial logs, operator events, cooperative timing, and
  subset documentation.

### D05 - Raw-Fusion Upper Bound

- Dataset:
  [`d05_c3_t1_l1_raw_fusion_upper_bound_20260427T102654Z`](datasets/d05_c3_t1_l1_raw_fusion_upper_bound_20260427T102654Z/)
- Script:
  [`scripts/run_d05_c3_t1_l1_raw_fusion_upper_bound.sh`](scripts/run_d05_c3_t1_l1_raw_fusion_upper_bound.sh)
- Profile:
  [`scripts/sessions/d05_c3_t1_l1_raw_fusion_upper_bound/`](scripts/sessions/d05_c3_t1_l1_raw_fusion_upper_bound/)
- Surface: two sanitized serial logs and timing/event surfaces. This bundle is
  retained for auditability and is not claim-grade.

### D04 - Support Under Load

- Dataset:
  [`d04_c2_t0_l2_support_under_load_20260420T110543Z`](datasets/d04_c2_t0_l2_support_under_load_20260420T110543Z/)
- Script:
  [`scripts/run_d04_c2_t0_l2_support_under_load.sh`](scripts/run_d04_c2_t0_l2_support_under_load.sh)
- Profile:
  [`scripts/sessions/d04_c2_t0_l2_support_under_load/`](scripts/sessions/d04_c2_t0_l2_support_under_load/)
- Surface: one sanitized serial log and operator block-event log. The retained
  public surface is not claim-grade under-load evidence.

### D03 - Full Support Capture

- Dataset:
  [`d03_c2_t0_l1_full_support_capture_20260406T125404Z`](datasets/d03_c2_t0_l1_full_support_capture_20260406T125404Z/)
- Script:
  [`scripts/run_d03_c2_t0_l1_full_support_capture.sh`](scripts/run_d03_c2_t0_l1_full_support_capture.sh)
- Profile:
  [`scripts/sessions/d03_c2_t0_l1_full_support_capture/`](scripts/sessions/d03_c2_t0_l1_full_support_capture/)
- Surface: one sanitized serial log and operator block-event log.

### D02 - Quiet-Control Candidate

- Dataset:
  [`d02_c1_t0_l0_honest_quiet_candidate_20260406T122440Z`](datasets/d02_c1_t0_l0_honest_quiet_candidate_20260406T122440Z/)
- Script:
  [`scripts/run_d02_c1_t0_l0_honest_quiet.sh`](scripts/run_d02_c1_t0_l0_honest_quiet.sh)
- Profile:
  [`scripts/sessions/d02_c1_t0_l0_honest_quiet_candidate/`](scripts/sessions/d02_c1_t0_l0_honest_quiet_candidate/)
- Surface: one sanitized serial log and operator block-event log.

### D01 - Repeatability

- Latest dataset:
  [`d01_c1_t0_l1_repeatability_20260406T113903Z`](datasets/d01_c1_t0_l1_repeatability_20260406T113903Z/)
- Earlier dataset:
  [`d01_c1_t0_l1_repeatability_20260406T095034Z`](datasets/d01_c1_t0_l1_repeatability_20260406T095034Z/)
- Script:
  [`scripts/run_d01_c1_t0_l1_repeatability.sh`](scripts/run_d01_c1_t0_l1_repeatability.sh)
- Profile:
  [`scripts/sessions/d01_c1_t0_l1_repeatability/`](scripts/sessions/d01_c1_t0_l1_repeatability/)
- Surface: one sanitized serial log and operator block-event log per run.

### W-Series Baselines

- Baseline dataset:
  [`w01_e01_c1_t0_l1_baseline_20260330T101537Z`](datasets/w01_e01_c1_t0_l1_baseline_20260330T101537Z/)
- Baseline script:
  [`scripts/run_w01_e01_c1_t0_l1_baseline.sh`](scripts/run_w01_e01_c1_t0_l1_baseline.sh)
- Low-density dataset:
  [`w03_e05_c2_t0_l1_low_density_support_20260330T130337Z`](datasets/w03_e05_c2_t0_l1_low_density_support_20260330T130337Z/)
- Low-density script:
  [`scripts/run_w03_e05_c2_t0_l1_low_density_support.sh`](scripts/run_w03_e05_c2_t0_l1_low_density_support.sh)
- Profiles:
  [`scripts/sessions/w01_e01_c1_t0_l1_baseline/`](scripts/sessions/w01_e01_c1_t0_l1_baseline/),
  [`scripts/sessions/w03_e05_c2_t0_l1_low_density_support/`](scripts/sessions/w03_e05_c2_t0_l1_low_density_support/)

## Bundle Contents

A normal published bundle contains:

- `metadata.json`: sanitized session metadata and block definitions.
- `runbook.md`: compact bundle summary.
- `operator_notes.md`: sanitized operator-facing notes.
- `logs/operator_block_events.tsv`: block-event timing.
- `serial/`: sanitized serial measurement logs.

Some cooperative runs also include:

- `logs/cooperative_timing_markers.tsv`
- `analysis/cooperative_timing/summary.md`
- compact notes or QC summaries required to interpret the public claim surface

## Notation

- `wNN`: early measured-series identifier.
- `dNN`: dissertation-aligned experiment identifier.
- `C1`, `C2`, ...: campaign code.
- `T0`, `T1`, ...: topology code.
- `L0`, `L1`, ...: operating-condition code.
- `W0`: warm-up block.
- `E*`, `S*`, `M*`: empty, static, and motion blocks.
- `YYYYMMDDThhmmssZ`: UTC timestamp suffix.

## Evidence Boundary

Included:

- sanitized measured capture logs
- operator timing/event logs
- bundle metadata needed to interpret the run
- public launch wrappers and session profiles

Excluded:

- credentials and secrets
- concrete hostnames, device paths, SSIDs, IP addresses, and MAC/BSSID values
- AP snapshot/configuration logs with private device state
- private workflow notes and unpublished analysis surfaces
