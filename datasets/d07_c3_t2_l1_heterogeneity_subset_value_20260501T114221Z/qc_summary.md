# QC Summary

- Session ID: `d07_c3_t2_l1_heterogeneity_subset_value`
- Program ID: `D07`
- Verdict: `usable as planned`
- Planned blocks: `W0, E1, S1, M1, E2, S2, M2, E3`
- Completed blocks: `W0, E1, S1, M1, E2, S2, M2, E3`
- Missing blocks: `-`
- Raw line count: `327895`
- CSI row count: `8576`
- Max dropped: `0`
- Max zero_len: `0`
- Max timeouts: `0`
- Auxiliary sensor logs: `serial/esp32_c5_b_guided_session.log, serial/esp32_s3_c_guided_session.log`
- Required sidecar outputs: `-`
- Templated notes completed: `yes`
- Baselines: `B1, B2`
- Condition interpretation: `L1 is the requested working condition`
- Capture-quality gates: `enabled`
- Live sensor CSI row ratio: `2.49`
- Cooperative timing evidence required: `yes`
- Cooperative timing verdict: `trustworthy`
- Cooperative timing summary: `analysis/cooperative_timing/summary.md`

## Sensor Summaries

| Sensor | Kind | Emulated | CSI Rows | Max Dropped | Max Zero Len | Max Timeouts | Path |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `node-a` | `command_stream` | `no` | `8576` | `0` | `0` | `0` | `serial/esp32_guided_session.log` |
| `node-b` | `command_stream` | `no` | `7515` | `0` | `0` | `0` | `serial/esp32_c5_b_guided_session.log` |
| `node-c` | `command_stream` | `no` | `18702` | `0` | `0` | `0` | `serial/esp32_s3_c_guided_session.log` |

## Interpretation

- `usable as planned`: full block coverage, no segmentation failure, and no obvious dropped/zero_len damage.
- `usable with restrictions`: partial coverage or quality markers require careful exclusion logic.
- `not claim-grade`: segmentation failed or the bundle is incomplete for disciplined analysis.
