# QC Summary

- Session ID: `d10_c5_t2_l1_stability_maintenance`
- Program ID: `D10`
- Verdict: `usable as planned`
- Planned blocks: `W0, E1, S1, M1, E2, S2, M2, E3, S3, M3, E4, S4, M4, E5, S5, M5, E6`
- Completed blocks: `W0, E1, S1, M1, E2, S2, M2, E3, S3, M3, E4, S4, M4, E5, S5, M5, E6`
- Missing blocks: `-`
- Raw line count: `1232128`
- CSI row count: `34169`
- Max dropped: `0`
- Max zero_len: `0`
- Max timeouts: `0`
- Auxiliary sensor logs: `serial/esp32_c5_b_guided_session.log.gz, serial/esp32_s3_c_guided_session.log.gz`
- Required sidecar outputs: `private bundle sidecars summarized here only: node_a_features, node_b_features, node_c_features, protected_traffic_trace_node_c, controller_decision_log`
- Templated notes completed: `yes`
- Baselines: `B3`
- Condition interpretation: `L1 is the requested working condition`
- Capture-quality gates: `enabled`
- Live sensor CSI row ratio: `2.28`
- Controller / traffic gap: `0 ms`
- Controller / traffic gap: `0 ms`
- Controller / traffic gap: `0 ms`
- Protected traffic traces required: `yes`
- Protected traffic traces present: `yes`
- Cooperative timing evidence required: `yes`
- Cooperative timing verdict: `trustworthy`
- Cooperative timing summary: `analysis/cooperative_timing/summary.md`

## Sensor Summaries

| Sensor | Kind | Emulated | CSI Rows | Max Dropped | Max Zero Len | Max Timeouts | Path |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `node-a` | `command_stream` | `no` | `34169` | `0` | `0` | `0` | `serial/esp32_guided_session.log.gz` |
| `node-b` | `command_stream` | `no` | `29501` | `0` | `0` | `0` | `serial/esp32_c5_b_guided_session.log.gz` |
| `node-c` | `command_stream` | `no` | `67199` | `0` | `0` | `0` | `serial/esp32_s3_c_guided_session.log.gz` |

## Required Sidecar Summaries

| Sidecar | Kind | Emulated | Primary Count | Bytes | Path |
| --- | --- | --- | --- | --- | --- |
| `node-a-feature-export` | `feature_ndjson` | `no` | `2690 windows` | `2693676` | `not published; summarized from private bundle` |
| `node-b-feature-export` | `feature_ndjson` | `no` | `2690 windows` | `2667927` | `not published; summarized from private bundle` |
| `node-c-feature-export` | `feature_ndjson` | `no` | `2640 windows` | `2688156` | `not published; summarized from private bundle` |
| `node-c-protected-traffic` | `traffic_ndjson` | `no` | `11180 samples / 5590 throughput` | `4488244` | `not published; summarized from private bundle` |
| `controller-decisions` | `controller_ndjson` | `no` | `2640 decisions` | `2179765` | `not published; summarized from private bundle` |

## Interpretation

- `usable as planned`: full block coverage, no segmentation failure, and no obvious dropped/zero_len damage.
- `usable with restrictions`: partial coverage or quality markers require careful exclusion logic.
- `not claim-grade`: segmentation failed or the bundle is incomplete for disciplined analysis.
