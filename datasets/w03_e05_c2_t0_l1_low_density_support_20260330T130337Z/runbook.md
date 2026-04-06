# Public Measured Bundle

- Bundle ID: `w03_e05_c2_t0_l1_low_density_support_20260330T130337Z`
- Session ID: `w03_e05_c2_t0_l1_low_density_support`
- Publication scope: raw/public-safe measured bundle
- Target node: `primary prplOS-compatible dual-band AP node`
- Capture seconds: `1500`
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
| `W0` | 120 | no | technical warm-up and raw-stream sanity check before the C2 support capture | confirm that AP state, UART capture, and block-event logging are stable before collecting the longer support windows |
| `E1` | 180 | no | extended empty reference for reduced-density and compression support | collect a longer empty control segment suitable for later subsampling and comparator baselines |
| `S1` | 150 | yes | extended static presence support segment | capture a longer static-presence window for later F0 vs F2 and density-sweep comparisons |
| `M1` | 150 | yes | extended slow-motion support segment | capture a longer slow-motion window for later reduced-density and compression comparisons |
| `E2` | 180 | no | extended empty recovery after the first long cycle | check the reverse transition back to empty with a longer recovery segment |
| `S2` | 150 | yes | second extended static presence support segment | provide an in-session repeat for the static-presence support data |
| `M2` | 150 | yes | second extended slow-motion support segment | provide an in-session repeat for the slow-motion support data |
| `E3` | 180 | no | final extended empty recovery for comparator anchoring | finish the support set with a second long empty reference for block-aware analysis |

## Current Limits

- TODO(hw): this published bundle is a measured raw surface and does not by itself prove validated CSI sensing fidelity.
- TODO(spec): AP-control references remain a reference mapping and need closer mapping to 802.11bf / EasyMesh / TR-181 semantics.
- TODO(driver): host-side serial access and AP control still depend on local OS/driver/prplOS specifics.
- TODO(hw): this support capture does not prove validated hardware low-rate control by itself.
- TODO(verify): reduced-density interpretations still need direct measurement against a real low-rate hardware mode.
