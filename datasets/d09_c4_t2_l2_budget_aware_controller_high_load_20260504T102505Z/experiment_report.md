# Experiment Report

## Summary

- Program ID: `D09`
- Session ID: `d09_c4_t2_l2_budget_aware_controller_high_load`
- Status: `usable as planned`
- Bundle ID: `d09_c4_t2_l2_budget_aware_controller_high_load_20260504T102505Z`
- Fixed operating point: `5 GHz / channel 36 / 20 MHz`
- Raw line count: `373422`
- CSI row count: `10543`
- Interference/load note: `interference_load_notes.md`
- Alignment notes: `notes/per_node_alignment_notes.md`
- Auxiliary sensor logs: `serial/esp32_c5_b_guided_session.log.gz, serial/esp32_s3_c_guided_session.log.gz`
- Required sidecar outputs: `non-public sidecar streams summarized here only: node_a_features, node_b_features, node_c_features, protected_traffic_trace_node_c, controller_decision_log`
- Templated notes completed: `yes`
- Cooperative timing verdict: `trustworthy`
- Cooperative timing summary: `analysis/cooperative_timing/summary.md`
- Campaign / topology / condition: `C4 / T2 / L2`
- Baselines: `B0, B2, B3`
- Protected traffic traces: `non-public traffic trace summarized here only`
- Protected traffic support artifacts: `-`
- Capture-quality gates: `enabled`
- Live sensor CSI row ratio: `2.07`

## Sensor Quality

| Sensor | CSI Rows | Max Dropped | Max Zero Len | Max Timeouts | Path |
| --- | --- | --- | --- | --- | --- |
| `node-a` | `10543` | `0` | `0` | `0` | `serial/esp32_guided_session.log.gz` |
| `node-b` | `8978` | `0` | `0` | `0` | `serial/esp32_c5_b_guided_session.log.gz` |
| `node-c` | `18609` | `0` | `0` | `0` | `serial/esp32_s3_c_guided_session.log.gz` |

## Required Sidecar Quality

| Sidecar | Kind | Primary Count | Bytes | Path |
| --- | --- | --- | --- | --- |
| `node-a-feature-export` | `feature_ndjson` | `816 windows` | `828000` | `not included in the public bundle; summarized here` |
| `node-b-feature-export` | `feature_ndjson` | `816 windows` | `822115` | `not included in the public bundle; summarized here` |
| `node-c-feature-export` | `feature_ndjson` | `749 windows` | `770328` | `not included in the public bundle; summarized here` |
| `node-c-protected-traffic` | `traffic_ndjson` | `2509 samples / 1254 throughput` | `1010178` | `not included in the public bundle; summarized here` |
| `controller-decisions` | `controller_ndjson` | `749 decisions` | `615298` | `not included in the public bundle; summarized here` |

## Executed Blocks

| Block | CSI Rows |
| --- | --- |
| `W0` | `741` |
| `E1` | `1158` |
| `S1` | `992` |
| `M1` | `1009` |
| `E2` | `1206` |
| `S2` | `978` |
| `M2` | `996` |
| `E3` | `1135` |

## Segmentation

- Summary: `analysis/guided_segments/summary.md (not included in the public bundle; summarized here)`
