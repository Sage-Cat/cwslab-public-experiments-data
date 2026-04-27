# QC Summary

- Session ID: `d05_c3_t1_l1_raw_fusion_upper_bound`
- Program ID: `D05`
- Verdict: `not claim-grade`
- Planned blocks: `W0, E1, S1, M1, E2, S2, M2, E3`
- Completed blocks: `W0, E1, S1, M1, E2, S2, M2, E3`
- Missing blocks: `-`
- Raw line count: `2045`
- CSI row count: `1452`
- Max dropped: `0`
- Max zero_len: `0`
- Max timeouts: `0`
- Auxiliary sensor logs: `datasets/d05_c3_t1_l1_raw_fusion_upper_bound_20260427T102654Z/serial/esp32_c5_b_guided_session.log`
- Required sidecar outputs: `-`
- Templated notes completed: `yes`
- Baselines: `B1, B4`
- Condition interpretation: `L1 is the requested working condition`
- Capture-quality gates: `enabled`
- Live sensor CSI row ratio: `14.24`
- Cooperative timing evidence required: `yes`
- Cooperative timing verdict: `failed`
- Cooperative timing summary: `datasets/d05_c3_t1_l1_raw_fusion_upper_bound_20260427T102654Z/analysis/cooperative_timing/summary.md`
- Restrictive note verdicts present: `yes`

## Capture-Quality Claim Blockers

- capture_finished event missing from logs/operator_block_events.tsv

## Capture-Quality Restrictions

- live sensor CSI row ratio 14.24 exceeds 4

## Sensor Summaries

| Sensor | Kind | Emulated | CSI Rows | Max Dropped | Max Zero Len | Max Timeouts | Path |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `node-a` | `serial_tty` | `no` | `1452` | `0` | `0` | `0` | `datasets/d05_c3_t1_l1_raw_fusion_upper_bound_20260427T102654Z/serial/esp32_guided_session.log` |
| `node-b` | `command_stream` | `no` | `102` | `0` | `0` | `0` | `datasets/d05_c3_t1_l1_raw_fusion_upper_bound_20260427T102654Z/serial/esp32_c5_b_guided_session.log` |

## Interpretation

- `usable as planned`: full block coverage, no segmentation failure, and no obvious dropped/zero_len damage.
- `usable with restrictions`: partial coverage or quality markers require careful exclusion logic.
- `not claim-grade`: segmentation failed or the bundle is incomplete for disciplined analysis.
