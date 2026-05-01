# Public Measured Bundle

- Bundle ID: `d08_c4_t1_l1_budget_aware_controller_20260501T130657Z`
- Session ID: `d08_c4_t1_l1_budget_aware_controller`
- Publication scope: raw/public-safe claim-grade D08 controller and protected-traffic bundle
- Target node: `primary prplOS-compatible dual-band AP node`
- Capture seconds: `1500`
- Primary raw capture: `serial/esp32_guided_session.log`
- Auxiliary raw capture: `serial/esp32_c5_b_guided_session.log`
- Operator block-event log: `logs/operator_block_events.tsv`
- Cooperative timing marker log: `logs/cooperative_timing_markers.tsv`
- Cooperative timing summary: `analysis/cooperative_timing/summary.md`
- Requested operating channel: `36` / `20MHz`
- Publication verdict: `usable as planned`
- Sanitization: local paths, host/device identifiers, private helper addresses, interface names, credentials, and monorepo-only launch details removed from public notes/metadata

## Physical Topology

Clock-to-degree convention: `12 o'clock` = `0 degrees`, `3 o'clock` = `90 degrees`, `6 o'clock` = `180 degrees`, and `9 o'clock` = `270 degrees`, measured clockwise from `12 o'clock`.

Primary `1.00 m` ring around the experiment center:

- Node A `ESP32-C5`, connected to the laptop by USB: `12 o'clock` / `0 degrees`.
- Primary router/AP: `6 o'clock` / `180 degrees`.
- Node B `RPi5`: `9 o'clock` / `270 degrees`.
- Node B `RPi4` with USB-connected `ESP32-C5`: `3 o'clock` / `90 degrees`.
- Node C `RPi5`: `7:30` / `7.5 o'clock` / `225 degrees`, used as the protected-traffic helper path.
- Node C `ESP32-S3`, connected only to power: separate off-ring `1:30` / `1.5 o'clock` / `45 degrees` corner, `2.00 m` from the experiment center.

The controlled primary sensing diameter is Node A `ESP32-C5` at `12 o'clock` / `0 degrees` to the router/AP at `6 o'clock` / `180 degrees`.

## Research Metadata

- Program ID: `D08`
- Campaign / topology / condition / mode: `C4 / T1 / L1 / H`
- Baselines: `B0, B1, B2, B3`
- Support level: `full`
- Claim-grade note: both sensing streams were live, controller and protected-traffic sidecars were present and synchronized, and cooperative timing was `trustworthy`.

## Manual Capture Blocks

| Block | Duration (s) | Human Present | Scenario | Objective |
| --- | --- | --- | --- | --- |
| `W0` | 120 | no | controller and traffic warm-up | confirm that sensing, protected-traffic, and controller sidecars are all active before the first measured block |
| `E1` | 180 | no | shared empty-scene reference under moderate protected traffic | collect the empty baseline for the controller surface |
| `S1` | 150 | yes | static presence in the shared interaction zone | collect the first controller-driven static segment |
| `M1` | 150 | yes | slow motion through the shared interaction zone | collect the first controller-driven motion segment |
| `E2` | 180 | no | empty recovery after the first cycle | observe the reverse transition while traffic remains active |
| `S2` | 150 | yes | second static presence | provide an in-session repeat for the controller comparison |
| `M2` | 150 | yes | second slow motion segment | provide an in-session repeat for the controller comparison |
| `E3` | 180 | no | final empty recovery | complete the controller bundle and notes |

## Published Evidence Surface

- Two raw sensing capture logs are retained for auditability.
- `qc_summary.md` and `experiment_report.md` are included after public-safe path sanitization.
- The cooperative timing summary is included because the D08 claim depends on cross-node timing evidence.
- Controller and protected-traffic sidecars are summarized in the published notes and metadata, but the raw sidecar outputs are intentionally excluded from this public repository.
