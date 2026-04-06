# Public Measured Bundle

- Bundle ID: `d02_c1_t0_l0_honest_quiet_candidate_20260406T122440Z`
- Session ID: `d02_c1_t0_l0_honest_quiet_candidate`
- Publication scope: raw/public-safe measured bundle
- Target node: `primary prplOS-compatible dual-band AP node`
- Capture seconds: `1020`
- Raw serial capture: `serial/esp32_guided_session.log`
- Operator block-event log: `logs/operator_block_events.tsv`
- Sanitization: local paths, host/device identifiers, credentials, and internal plan references removed
- Requested operating channel: `36` / `20MHz`
- Radio ref: `Device.WiFi.Radio.2.`
- SSID ref: `Device.WiFi.SSID.4.`
- AccessPoint ref: `Device.WiFi.AccessPoint.3.`

## Research Metadata

- Program ID: `D02`
- Campaign / topology / requested condition / mode: `C1 / T0 / L0 / H`
- Baselines: `B0, B1`
- Support level: `full`
- Honest condition gate: claim `L0` only after independent confirmation; otherwise downgrade the interpretation to `L1`

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
| `W0` | 90 | no | short technical warm-up before the quiet-control attempt | confirm that the path is stable before the optional quiet-window run |
| `E1` | 180 | no | longer empty baseline under the quietest honestly available condition | capture a stronger empty control segment under the quietest background that can be honestly defended |
| `S1` | 120 | yes | static presence under the same quiet-control attempt | capture one static-presence segment under the same quiet-control condition |
| `M1` | 120 | yes | slow motion under the same quiet-control attempt | capture one slow-motion segment under the same quiet-control condition |
| `E2` | 180 | no | final empty recovery under the same quiet-control attempt | finish the run with a second long empty reference under the same quiet-control condition |

## Current Limits

- TODO(hw): this published bundle is a measured raw surface and does not by itself prove validated CSI sensing fidelity.
- TODO(verify): this bundle does not by itself prove that the condition may be claimed as `L0`; downgrade to `L1` unless quietness is independently confirmed.
- TODO(spec): AP-control references remain a reference mapping and need closer mapping to 802.11bf / EasyMesh / TR-181 semantics.
- TODO(driver): host-side serial access and AP control still depend on local OS/driver/prplOS specifics.
