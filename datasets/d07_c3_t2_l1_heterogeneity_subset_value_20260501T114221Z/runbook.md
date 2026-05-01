# Public Measured Bundle

- Bundle ID: `d07_c3_t2_l1_heterogeneity_subset_value_20260501T114221Z`
- Session ID: `d07_c3_t2_l1_heterogeneity_subset_value`
- Publication scope: raw/public-safe claim-grade D07 cooperative three-node bundle
- Target node: `primary prplOS-compatible dual-band AP node`
- Capture seconds: `1500`
- Primary raw capture: `serial/esp32_guided_session.log`
- Auxiliary raw captures: `serial/esp32_c5_b_guided_session.log`, `serial/esp32_s3_c_guided_session.log`
- Operator block-event log: `logs/operator_block_events.tsv`
- Cooperative timing marker log: `logs/cooperative_timing_markers.tsv`
- Cooperative timing summary: `analysis/cooperative_timing/summary.md`
- Requested operating channel: `36` / `20MHz`
- Publication verdict: `usable as planned`
- Sanitization: local paths, host/device identifiers, credentials, private AP addresses, interface names, and internal plan references removed from public notes/metadata

## Physical Topology

Clock-to-degree convention: `12 o'clock` = `0 degrees`, `3 o'clock` = `90 degrees`, `6 o'clock` = `180 degrees`, and `9 o'clock` = `270 degrees`, measured clockwise from `12 o'clock`.

Primary `1.00 m` ring around the experiment center:

- Node A `ESP32-C5`, connected to the laptop by USB: `12 o'clock` / `0 degrees`.
- Primary router/AP: `6 o'clock` / `180 degrees`.
- Node B `RPi5`: `9 o'clock` / `270 degrees`.
- Node B `RPi4` with USB-connected `ESP32-C5`: `3 o'clock` / `90 degrees`.
- Node C `RPi5`: `7:30` / `7.5 o'clock` / `225 degrees`, midway along the perimeter between the router/AP and the Node B `RPi5`.
- Node C `ESP32-S3`, connected only to power: separate off-ring `1:30` / `1.5 o'clock` / `45 degrees` corner, `2.00 m` from the experiment center.

The controlled primary sensing diameter is Node A `ESP32-C5` at `12 o'clock` / `0 degrees` to the router/AP at `6 o'clock` / `180 degrees`.

## Research Metadata

- Program ID: `D07`
- Campaign / topology / condition / mode: `C3 / T2 / L1 / H`
- Baselines: `B1, B2`
- Support level: `full`
- Claim-grade note: all three sensing streams were live, all planned blocks completed, capture-quality blockers were absent, and cooperative timing was `trustworthy`.

## Manual Capture Blocks

| Block | Duration (s) | Human Present | Scenario | Objective |
| --- | --- | --- | --- | --- |
| `W0` | 120 | no | three-node warm-up and subset sanity check | confirm that all three node streams are active before capture |
| `E1` | 180 | no | shared empty-scene reference | collect the three-node empty baseline |
| `S1` | 150 | yes | static presence in the shared interaction zone | collect the first heterogeneity segment |
| `M1` | 150 | yes | slow motion through the shared interaction zone | collect the first moving three-node segment |
| `E2` | 180 | no | empty recovery after the first cycle | capture the reverse transition to empty |
| `S2` | 150 | yes | second static presence | provide an in-session repeat for the subset ranking surface |
| `M2` | 150 | yes | second slow motion segment | provide an in-session repeat for the moving subset comparison |
| `E3` | 180 | no | final empty recovery | complete the three-node bundle and subset manifest |

## Published Evidence Surface

- Three raw capture logs are retained for auditability.
- `qc_summary.md` and `experiment_report.md` are included after public-safe path sanitization.
- The cooperative timing summary is included because the D07 claim depends on cross-node timing evidence.
