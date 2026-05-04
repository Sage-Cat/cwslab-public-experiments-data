# Experiment Report

## Summary

- Program ID: `D10`
- Session ID: `d10_c5_t2_l1_stability_maintenance`
- Status: `usable as planned`
- Bundle dir: `<cws-lab>/experiments/runs/d10_c5_t2_l1_stability_maintenance_20260504T115457Z`
- Fixed operating point: `5 GHz / channel 36 / 20 MHz`
- Raw line count: `1232128`
- CSI row count: `34169`
- Interference/load note: `interference_load_notes.md`
- Alignment notes: `notes/per_node_alignment_notes.md`
- Auxiliary sensor logs: `serial/esp32_c5_b_guided_session.log.gz, serial/esp32_s3_c_guided_session.log.gz`
- Required sidecar outputs: `private bundle sidecars summarized here only: node_a_features, node_b_features, node_c_features, protected_traffic_trace_node_c, controller_decision_log`
- Templated notes completed: `yes`
- Cooperative timing verdict: `trustworthy`
- Cooperative timing summary: `analysis/cooperative_timing/summary.md`
- Campaign / topology / condition: `C5 / T2 / L1`
- Baselines: `B3`
- Protected traffic traces: `private bundle traffic trace summarized here only`
- Protected traffic support artifacts: `-`
- Capture-quality gates: `enabled`
- Live sensor CSI row ratio: `2.28`

## Sensor Quality

| Sensor | CSI Rows | Max Dropped | Max Zero Len | Max Timeouts | Path |
| --- | --- | --- | --- | --- | --- |
| `node-a` | `34169` | `0` | `0` | `0` | `serial/esp32_guided_session.log.gz` |
| `node-b` | `29501` | `0` | `0` | `0` | `serial/esp32_c5_b_guided_session.log.gz` |
| `node-c` | `67199` | `0` | `0` | `0` | `serial/esp32_s3_c_guided_session.log.gz` |

## Required Sidecar Quality

| Sidecar | Kind | Primary Count | Bytes | Path |
| --- | --- | --- | --- | --- |
| `node-a-feature-export` | `feature_ndjson` | `2690 windows` | `2693676` | `not published; summarized from private bundle` |
| `node-b-feature-export` | `feature_ndjson` | `2690 windows` | `2667927` | `not published; summarized from private bundle` |
| `node-c-feature-export` | `feature_ndjson` | `2640 windows` | `2688156` | `not published; summarized from private bundle` |
| `node-c-protected-traffic` | `traffic_ndjson` | `11180 samples / 5590 throughput` | `4488244` | `not published; summarized from private bundle` |
| `controller-decisions` | `controller_ndjson` | `2640 decisions` | `2179765` | `not published; summarized from private bundle` |

## Executed Blocks

| Block | CSI Rows |
| --- | --- |
| `W0` | `1144` |
| `E1` | `1565` |
| `S1` | `1118` |
| `M1` | `1167` |
| `E2` | `1543` |
| `S2` | `1134` |
| `M2` | `1133` |
| `E3` | `1538` |
| `S3` | `1137` |
| `M3` | `1155` |
| `E4` | `1527` |
| `S4` | `1145` |
| `M4` | `1182` |
| `E5` | `1508` |
| `S5` | `1146` |
| `M5` | `1144` |
| `E6` | `1874` |

## Segmentation

- Summary: `analysis/guided_segments/summary.md (not published; summarized from private bundle)`
