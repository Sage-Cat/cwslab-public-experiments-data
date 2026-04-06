# Public Measured Bundle

- Bundle ID: `w01_e01_c1_t0_l1_baseline_20260330T101537Z`
- Session ID: `w01_e01_c1_t0_l1_baseline`
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
| `W0` | 120 | no | technical warm-up and transport sanity check | confirm that AP state, UART capture, and block-event logging are stable before the baseline blocks |
| `E1` | 120 | no | empty scene, first baseline | capture the first empty reference under the fixed geometry |
| `S1` | 120 | yes | one person standing almost still in the controlled path | capture the first static-presence reference |
| `M1` | 120 | yes | one person moving slowly inside the controlled path | capture the first slow-motion reference |
| `E2` | 120 | no | empty scene, recovery after the first motion cycle | check the reverse transition back to empty after the first cycle |
| `S2` | 120 | yes | repeated static presence in the same controlled path | capture an in-session repeat for the static-presence state |
| `M2` | 120 | yes | repeated slow motion in the same controlled path | capture an in-session repeat for the slow-motion state |
| `E3` | 120 | no | final empty recovery | finish the session with a final empty reference for block-aware comparison |

## Current Limits

- TODO(hw): this published bundle is a measured raw surface and does not by itself prove validated CSI sensing fidelity.
- TODO(spec): AP-control references remain a reference mapping and need closer mapping to 802.11bf / EasyMesh / TR-181 semantics.
- TODO(driver): host-side serial access and AP control still depend on local OS/driver/prplOS specifics.
