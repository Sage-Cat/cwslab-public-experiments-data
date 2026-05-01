# QC Summary

- Session ID: `d08_c4_t1_l1_budget_aware_controller`
- Program ID: `D08`
- Verdict: `usable as planned`
- Planned blocks: `W0, E1, S1, M1, E2, S2, M2, E3`
- Completed blocks: `W0, E1, S1, M1, E2, S2, M2, E3`
- Missing blocks: `-`
- Raw line count: `332233`
- CSI row count: `8464`
- Max dropped: `0`
- Max zero_len: `0`
- Max timeouts: `0`
- Auxiliary sensor logs: `serial/esp32_c5_b_guided_session.log`
- Required sidecar outputs: `private bundle sidecars summarized here only: node_a_features, node_b_features, protected_traffic_trace_node_c, controller_decision_log`
- Templated notes completed: `yes`
- Baselines: `B0, B1, B2, B3`
- Condition interpretation: `L1 is the requested working condition`
- Capture-quality gates: `enabled`
- Live sensor CSI row ratio: `1.15`
- Controller / traffic gap: `0 ms`
- Protected traffic traces required: `yes`
- Protected traffic traces present: `yes`
- Cooperative timing evidence required: `yes`
- Cooperative timing verdict: `trustworthy`
- Cooperative timing summary: `analysis/cooperative_timing/summary.md`

## Sensor Summaries

| Sensor | Kind | Emulated | CSI Rows | Max Dropped | Max Zero Len | Max Timeouts | Path |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `node-a` | `command_stream` | `no` | `8464` | `0` | `0` | `0` | `serial/esp32_guided_session.log` |
| `node-b` | `command_stream` | `no` | `7383` | `0` | `0` | `0` | `serial/esp32_c5_b_guided_session.log` |

## Required Sidecar Summaries

| Sidecar | Kind | Emulated | Primary Count | Bytes | Path |
| --- | --- | --- | --- | --- | --- |
| `node-a-feature-export` | `feature_ndjson` | `no` | `734 windows` | `738198` | `not published; summarized from private bundle` |
| `node-b-feature-export` | `feature_ndjson` | `no` | `734 windows` | `725496` | `not published; summarized from private bundle` |
| `node-c-protected-traffic` | `traffic_ndjson` | `no` | `3473 samples / 1736 throughput` | `1395752` | `not published; summarized from private bundle` |
| `controller-decisions` | `controller_ndjson` | `no` | `734 decisions` | `573448` | `not published; summarized from private bundle` |

## Interpretation

- `usable as planned`: full block coverage, no segmentation failure, and no obvious dropped/zero_len damage.
- `usable with restrictions`: partial coverage or quality markers require careful exclusion logic.
- `not claim-grade`: segmentation failed or the bundle is incomplete for disciplined analysis.
