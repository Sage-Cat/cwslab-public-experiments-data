# Experiment Report

## Summary

- Program ID: `D05`
- Session ID: `d05_c3_t1_l1_raw_fusion_upper_bound`
- Status: `not claim-grade`
- Bundle dir: `datasets/d05_c3_t1_l1_raw_fusion_upper_bound_20260427T102654Z`
- Fixed operating point: `5 GHz / channel 36 / 20 MHz`
- Raw line count: `2045`
- CSI row count: `1452`
- Interference/load note: `datasets/d05_c3_t1_l1_raw_fusion_upper_bound_20260427T102654Z/interference_load_notes.md`
- Alignment notes: `datasets/d05_c3_t1_l1_raw_fusion_upper_bound_20260427T102654Z/notes/per_node_alignment_notes.md`
- Auxiliary sensor logs: `datasets/d05_c3_t1_l1_raw_fusion_upper_bound_20260427T102654Z/serial/esp32_c5_b_guided_session.log`
- Required sidecar outputs: `-`
- Templated notes completed: `yes`
- Cooperative timing verdict: `failed`
- Cooperative timing summary: `datasets/d05_c3_t1_l1_raw_fusion_upper_bound_20260427T102654Z/analysis/cooperative_timing/summary.md`
- Campaign / topology / condition: `C3 / T1 / L1`
- Baselines: `B1, B4`
- Capture-quality gates: `enabled`
- Live sensor CSI row ratio: `14.24`
- Restrictive note verdicts present: `yes`

## Capture-Quality Claim Blockers

- capture_finished event missing from logs/operator_block_events.tsv

## Capture-Quality Restrictions

- live sensor CSI row ratio 14.24 exceeds 4

## Sensor Quality

| Sensor | CSI Rows | Max Dropped | Max Zero Len | Max Timeouts | Path |
| --- | --- | --- | --- | --- | --- |
| `node-a` | `1452` | `0` | `0` | `0` | `datasets/d05_c3_t1_l1_raw_fusion_upper_bound_20260427T102654Z/serial/esp32_guided_session.log` |
| `node-b` | `102` | `0` | `0` | `0` | `datasets/d05_c3_t1_l1_raw_fusion_upper_bound_20260427T102654Z/serial/esp32_c5_b_guided_session.log` |

## Executed Blocks

| Block | CSI Rows |
| --- | --- |
| `W0` | `118` |
| `E1` | `177` |
| `S1` | `147` |
| `M1` | `148` |
| `E2` | `176` |
| `S2` | `147` |
| `M2` | `147` |
| `E3` | `177` |

## Segmentation

- Summary: `datasets/d05_c3_t1_l1_raw_fusion_upper_bound_20260427T102654Z/analysis/guided_segments/summary.md`
