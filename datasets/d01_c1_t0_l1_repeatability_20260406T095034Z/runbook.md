# Public Measured Bundle

- Bundle ID: `d01_c1_t0_l1_repeatability_20260406T095034Z`
- Session ID: `d01_c1_t0_l1_repeatability`
- Publication scope: raw/public-safe measured bundle
- Target node: `primary prplOS-compatible dual-band AP node`
- Capture seconds: `1320`
- Raw serial capture: `serial/esp32_guided_session.log`
- Operator block-event log: `logs/operator_block_events.tsv`
- Sanitization: local paths, host/device identifiers, credentials, and internal plan references removed
- Requested operating channel: `36` / `20MHz`
- Radio ref: `Device.WiFi.Radio.2.`
- SSID ref: `Device.WiFi.SSID.4.`
- AccessPoint ref: `Device.WiFi.AccessPoint.3.`

## Research Metadata

- Program ID: `D01`
- Campaign / topology / condition / mode: `C1 / T0 / L1 / H`
- Baselines: `B0, B1`
- Support level: `full`

## Published Script Steps

| Step ID | Purpose |
| --- | --- |
| `preflight_local` | Check local WSL/Linux dependencies and capture-device visibility. |
| `ap_configure` | Apply the requested router radio, SSID, and AccessPoint settings. |
| `ap_snapshot` | Collect router-side snapshots over SSH or serial console. |
| `firmware_build` | Build the configured ESP32 firmware workspace. |
| `firmware_flash` | Flash the configured ESP32 firmware workspace. |
| `serial_capture` | Capture the ESP32 serial stream for the configured duration. |
| `operator_guided_capture` | Run a continuous serial capture and pause for operator confirmation between configured capture blocks. |
| `run_experiment` | Run preflight, AP setup, AP snapshot, and then the interactive operator-guided capture sequence. |

## Manual Capture Blocks

| Block | Duration (s) | Human Present | Scenario | Objective |
| --- | --- | --- | --- | --- |
| `W0` | 120 | no | post-reset technical warm-up and transport sanity check | verify that the path remains stable before the repeatability baseline starts |
| `E1` | 120 | no | empty scene repeated baseline | capture the repeated empty reference under the same L1 stand geometry |
| `S1` | 120 | yes | repeated static presence in the controlled path | reproduce the static-presence reference from the earlier precursor |
| `M1` | 120 | yes | repeated slow motion in the controlled path | reproduce the slow-motion reference from the earlier precursor |
| `E2` | 120 | no | empty scene recovery after the first repeated motion cycle | check the reverse transition back to empty after the repeated cycle |
| `S2` | 120 | yes | second repeated static presence in the same controlled path | give a second static-presence evidence point inside the repeat session |
| `M2` | 120 | yes | second repeated slow motion in the same controlled path | give a second slow-motion evidence point inside the repeat session |
| `E3` | 120 | no | final empty recovery after the repeatability run | finish the repeat session with a final empty reference |

## Current Limits

- TODO(hw): this published bundle is a measured raw surface and does not by itself prove validated CSI sensing fidelity.
- TODO(spec): AP-control references remain a reference mapping and need closer mapping to 802.11bf / EasyMesh / TR-181 semantics.
- TODO(driver): host-side serial access and AP control still depend on local OS/driver/prplOS specifics.
