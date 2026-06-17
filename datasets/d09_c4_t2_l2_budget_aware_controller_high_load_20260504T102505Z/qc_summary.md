# QC Summary

- Session ID: `d09_c4_t2_l2_budget_aware_controller_high_load`
- Program ID: `D09`
- Verdict: `usable as planned`
- Planned blocks: `W0, E1, S1, M1, E2, S2, M2, E3`
- Completed blocks: `W0, E1, S1, M1, E2, S2, M2, E3`
- Missing blocks: `-`
- Raw line count: `373422`
- CSI row count: `10543`
- Max dropped: `0`
- Max zero_len: `0`
- Max timeouts: `0`
- Auxiliary sensor logs: `serial/esp32_c5_b_guided_session.log.gz, serial/esp32_s3_c_guided_session.log.gz`
- Required sidecar outputs: `non-public sidecar streams summarized here only: node_a_features, node_b_features, node_c_features, protected_traffic_trace_node_c, controller_decision_log`
- Templated notes completed: `yes`
- Baselines: `B0, B2, B3`
- Condition interpretation: `L2 is the requested working condition`
- Capture-quality gates: `enabled`
- Live sensor CSI row ratio: `2.07`
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
| `node-a` | `command_stream` | `no` | `10543` | `0` | `0` | `0` | `serial/esp32_guided_session.log.gz` |
| `node-b` | `command_stream` | `no` | `8978` | `0` | `0` | `0` | `serial/esp32_c5_b_guided_session.log.gz` |
| `node-c` | `command_stream` | `no` | `18609` | `0` | `0` | `0` | `serial/esp32_s3_c_guided_session.log.gz` |

## Required Sidecar Summaries

| Sidecar | Kind | Emulated | Primary Count | Bytes | Path |
| --- | --- | --- | --- | --- | --- |
| `node-a-feature-export` | `feature_ndjson` | `no` | `816 windows` | `828000` | `not included in the public bundle; summarized here` |
| `node-b-feature-export` | `feature_ndjson` | `no` | `816 windows` | `822115` | `not included in the public bundle; summarized here` |
| `node-c-feature-export` | `feature_ndjson` | `no` | `749 windows` | `770328` | `not included in the public bundle; summarized here` |
| `node-c-protected-traffic` | `traffic_ndjson` | `no` | `2509 samples / 1254 throughput` | `1010178` | `not included in the public bundle; summarized here` |
| `controller-decisions` | `controller_ndjson` | `no` | `749 decisions` | `615298` | `not included in the public bundle; summarized here` |

## Interpretation

- `usable as planned`: full block coverage, no segmentation failure, and no obvious dropped/zero_len damage.
- `usable with restrictions`: partial coverage or quality markers require careful exclusion logic.
- `not claim-grade`: segmentation failed or the bundle is incomplete for disciplined analysis.
