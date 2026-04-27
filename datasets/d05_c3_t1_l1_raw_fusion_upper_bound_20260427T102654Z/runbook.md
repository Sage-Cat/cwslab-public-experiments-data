# Public Measured Bundle

- Bundle ID: `d05_c3_t1_l1_raw_fusion_upper_bound_20260427T102654Z`
- Session ID: `d05_c3_t1_l1_raw_fusion_upper_bound`
- Publication scope: raw/public-safe measured cooperative bundle
- Target node: `primary prplOS-compatible dual-band AP node`
- Capture seconds: `1500`
- Primary raw serial capture: `serial/esp32_guided_session.log`
- Auxiliary raw serial capture: `serial/esp32_c5_b_guided_session.log`
- Operator block-event log: `logs/operator_block_events.tsv`
- Cooperative timing marker log: `logs/cooperative_timing_markers.tsv`
- Cooperative timing summary: `analysis/cooperative_timing/summary.md`
- Sanitization: local paths, host/device identifiers, credentials, internal plan references, and private helper-host addresses removed from public notes/metadata
- Requested operating channel: `36` / `20MHz`
- Radio ref: `Device.WiFi.Radio.2.`
- SSID ref: `Device.WiFi.SSID.4.`
- AccessPoint ref: `Device.WiFi.AccessPoint.3.`

## Research Metadata

- Program ID: `D05`
- Campaign / topology / condition / mode: `C3 / T1 / L1 / H`
- Baselines: `B1, B4`
- Support level: `full`
- Publication note: all planned blocks are present and both sensors were live, but the bundle is not claim-grade cooperative fusion evidence because `capture_finished` is missing, node-B stalled after `E3`, the live sensor CSI row ratio was `14.24`, and cooperative timing failed.

## Manual Capture Blocks

| Block | Duration (s) | Human Present | Scenario | Objective |
| --- | --- | --- | --- | --- |
| `W0` | 120 | no | two-node transport warm-up and alignment sanity check | confirm that both serial paths, both AP paths, and the shared timeline are stable before cooperative capture |
| `E1` | 180 | no | shared empty-scene reference for both nodes | collect the first matched empty cooperative baseline |
| `S1` | 150 | yes | static presence in the shared interaction zone | capture the first matched static cooperative segment |
| `M1` | 150 | yes | slow motion through the shared interaction zone | capture the first matched motion cooperative segment |
| `E2` | 180 | no | empty recovery after the first cooperative cycle | observe the reverse transition back to empty for both nodes |
| `S2` | 150 | yes | second static presence in the shared interaction zone | provide an in-session repeat for the cooperative static segment |
| `M2` | 150 | yes | second slow motion in the shared interaction zone | provide an in-session repeat for the cooperative motion segment |
| `E3` | 180 | no | final empty recovery for cooperative upper-bound anchoring | finish with a matched empty reference and complete alignment notes |

## Current Limits

- TODO(verify): the cooperative timing report is failed, so cross-node fusion must be treated as analysis-only.
- TODO(driver): node-B stream transport needs a clean end-of-capture path before D05 can be claim-grade.
- TODO(qc): node-B CSI output rate must be brought close enough to node-A to pass the live-sensor row-ratio gate.
