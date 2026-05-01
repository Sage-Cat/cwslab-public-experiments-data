# Experiment Report

## Summary

- Program ID: `D08`
- Session ID: `d08_c4_t1_l1_budget_aware_controller`
- Status: `usable as planned`
- Bundle dir: `<cws-lab>/experiments/runs/d08_c4_t1_l1_budget_aware_controller_20260501T130657Z`
- Fixed operating point: `5 GHz / channel 36 / 20 MHz`
- Raw line count: `332233`
- CSI row count: `8464`
- Interference/load note: `interference_load_notes.md`
- Alignment notes: `notes/per_node_alignment_notes.md`
- Auxiliary sensor logs: `serial/esp32_c5_b_guided_session.log`
- Required sidecar outputs: `private bundle sidecars summarized here only: node_a_features, node_b_features, protected_traffic_trace_node_c, controller_decision_log`
- Templated notes completed: `yes`
- Cooperative timing verdict: `trustworthy`
- Cooperative timing summary: `analysis/cooperative_timing/summary.md`
- Campaign / topology / condition: `C4 / T1 / L1`
- Baselines: `B0, B1, B2, B3`
- Protected traffic traces: `private bundle traffic trace summarized here only`
- Protected traffic support artifacts: `-`
- Capture-quality gates: `enabled`
- Live sensor CSI row ratio: `1.15`

## Sensor Quality

| Sensor | CSI Rows | Max Dropped | Max Zero Len | Max Timeouts | Path |
| --- | --- | --- | --- | --- | --- |
| `node-a` | `8464` | `0` | `0` | `0` | `serial/esp32_guided_session.log` |
| `node-b` | `7383` | `0` | `0` | `0` | `serial/esp32_c5_b_guided_session.log` |

## Required Sidecar Quality

| Sidecar | Kind | Primary Count | Bytes | Path |
| --- | --- | --- | --- | --- |
| `node-a-feature-export` | `feature_ndjson` | `734 windows` | `738198` | `not published; summarized from private bundle` |
| `node-b-feature-export` | `feature_ndjson` | `734 windows` | `725496` | `not published; summarized from private bundle` |
| `node-c-protected-traffic` | `traffic_ndjson` | `3473 samples / 1736 throughput` | `1395752` | `not published; summarized from private bundle` |
| `controller-decisions` | `controller_ndjson` | `734 decisions` | `573448` | `not published; summarized from private bundle` |

## Executed Blocks

| Block | CSI Rows |
| --- | --- |
| `W0` | `697` |
| `E1` | `1046` |
| `S1` | `875` |
| `M1` | `876` |
| `E2` | `1027` |
| `S2` | `847` |
| `M2` | `861` |
| `E3` | `1056` |

## Segmentation

- Summary: `analysis/guided_segments/summary.md (not published; summarized from private bundle)`
