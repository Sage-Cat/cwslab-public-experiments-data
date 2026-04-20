# Public Measured Bundle

- Bundle ID: `d04_c2_t0_l2_support_under_load_20260420T110543Z`
- Session ID: `d04_c2_t0_l2_support_under_load`
- Publication scope: raw/public-safe measured bundle
- Target node: `primary prplOS-compatible dual-band AP node`
- Capture seconds: `1500`
- Raw serial capture: `serial/esp32_guided_session.log`
- Operator block-event log: `logs/operator_block_events.tsv`
- Sanitization: local paths, host/device identifiers, credentials, internal plan references, and derived analysis/reporting references removed
- Requested operating channel: `36` / `20MHz`
- Radio ref: `Device.WiFi.Radio.2.`
- SSID ref: `Device.WiFi.SSID.4.`
- AccessPoint ref: `Device.WiFi.AccessPoint.3.`

## Research Metadata

- Program ID: `D04`
- Campaign / topology / condition / mode: `C2 / T0 / L2 / H`
- Baselines: `B0, B4`
- Support level: `stub`
- Publication note: the full loaded block sequence was captured, but protected-traffic traces were not retained in the bundle, so this public package is a raw measured surface and not claim-grade D04 evidence

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
| `W0` | 120 | no | technical warm-up and protected-traffic synchronization check before the loaded capture | confirm AP state, UART capture path, and helper-node traffic tooling before the first L2 block |
| `E1` | 180 | no | extended empty reference under injected protected traffic | collect the first long empty baseline while the same L2 load profile is active |
| `S1` | 150 | yes | extended static presence under the same injected load | capture static presence while the protected traffic remains active |
| `M1` | 150 | yes | extended slow motion under the same injected load | capture slow motion while the same L2 load profile remains active |
| `E2` | 180 | no | extended empty recovery after the first loaded motion cycle | check the reverse transition back to empty under the same L2 load |
| `S2` | 150 | yes | second extended static presence under the same injected load | provide an in-session repeat for static presence with matched load conditions |
| `M2` | 150 | yes | second extended slow motion under the same injected load | provide an in-session repeat for slow motion with matched load conditions |
| `E3` | 180 | no | final extended empty recovery under the same injected load | finish the loaded support set with a final empty reference and aligned traffic trace |

## Current Limits

- TODO(hw): this published bundle is a measured raw surface and does not by itself prove validated CSI sensing fidelity.
- TODO(verify): protected-traffic traces are missing from the retained public bundle, so this surface alone must not be treated as claim-grade under-load evidence.
- TODO(spec): AP-control references remain a reference mapping and need closer mapping to 802.11bf / EasyMesh / TR-181 semantics.
- TODO(driver): host-side serial access and AP control still depend on local OS/driver/prplOS specifics.
