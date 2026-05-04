# Operator Notes

- Session ID: `d10_c5_t2_l1_stability_maintenance`

## Reminders

- D10 reuses the D09 three-node T2 stand but extends the session into a long-horizon maintenance run under light protected traffic.
- Use the corrected D07-D10 clock-face layout: Node A ESP32-C5 connected to the laptop by USB at 12 o'clock / 0 degrees; primary prplOS-compatible dual-band AP node at 6 o'clock / 180 degrees; Node B RPi5 at 9 o'clock / 270 degrees; Node B RPi4 with USB-connected ESP32-C5 at 3 o'clock / 90 degrees; Node C RPi5 at 7:30 / 7.5 o'clock / 225 degrees; Node C ESP32-S3 power-only receiver off the 1.00 m ring at 1:30 / 1.5 o'clock / 45 degrees, 2.00 m from the experiment center.
- Clock-to-degree convention: 12 o'clock is 0 degrees, 3 o'clock is 90 degrees, 6 o'clock is 180 degrees, and 9 o'clock is 270 degrees, measured clockwise from 12.
- Primary ring radius: Node A ESP32-C5, primary prplOS-compatible dual-band AP node, Node B RPi5, Node B RPi4 plus ESP32-C5, and Node C RPi5 are each 1.00 m from the experiment center; the Node C ESP32-S3 is the only off-ring device and sits in the separate 1:30 corner at 2.00 m from the center.
- Controlled primary sensing diameter: Node A ESP32-C5 at 12 o'clock / 0 degrees to the primary prplOS-compatible dual-band AP node at 6 o'clock / 180 degrees, for a 2.00 m line through the experiment center.
- Node A is captured over the primary-router UDP DNAT listener, Node B uses the AP-B UDP summary path, and Node C is the dedicated `RPi5 + ESP32-S3` `2.4 GHz` sensing path captured over UDP at `<node-c-ap-address>`.
- Protected traffic remains on the dedicated Node-C AP path: the laptop keeps `<node-c-wifi-adapter>` on `<redacted-node-c-ssid>` at `<operator-node-c-address>`, SSH reaches the Node-C RPi5 at `<node-c-ap-address>`, and the RPi5 sends live light-load ping plus byte-stream traffic back to the laptop over that AP.
- Integrated D10 uses two laptop Wi-Fi adapters: `<operator-main-wifi-adapter>` is switched to AP-B for node B, while `<node-c-wifi-adapter>` stays associated to the Node-C AP at `<node-c-ap-address>`; do not use the router-side Node-C address `<private-ip>` for the current stand.
- Verify on the helper `RPi5` that SSH over `<node-c-ap-address>`, `ping`, and POSIX `dd` are present before the run; the structured traffic sidecar uses SSH byte-stream measurement and does not require remote `python3` or local `iperf3`.
- Do not let helper traffic, management cabling, or long-session operator movement contaminate the 12-to-6 sensing corridor.

## Topology

- D07-D10 clock/degree convention: 12 o'clock = 0 degrees, 3 o'clock = 90 degrees, 6 o'clock = 180 degrees, 9 o'clock = 270 degrees, measured clockwise from 12.
- Primary 1.00 m ring around the experiment center: Node A ESP32-C5 connected to the laptop by USB at 12 o'clock / 0 degrees; primary prplOS-compatible dual-band AP node at 6 o'clock / 180 degrees; Node B RPi5 at 9 o'clock / 270 degrees; Node B RPi4 with USB-connected ESP32-C5 at 3 o'clock / 90 degrees; Node C RPi5 at 7:30 / 7.5 o'clock / 225 degrees, midway along the perimeter between the primary prplOS-compatible dual-band AP node and the Node B RPi5.
- Off-ring Node C receiver: ESP32-S3 is connected only to power in the separate 1:30 / 1.5 o'clock / 45 degrees corner, 2.00 m from the experiment center.
- Controlled primary sensing diameter: Node A ESP32-C5 at 12 o'clock / 0 degrees to the primary prplOS-compatible dual-band AP node at 6 o'clock / 180 degrees.
- Vertical placement: primary prplOS-compatible dual-band AP node, active esp32-c5-a, rpi5-a, rpi4-a, Node-C RPi5, and Node-C ESP32-S3 at 0.50 m unless otherwise recorded; capture laptop adjacent to the Node A USB setup.
- Record explicitly that the Node-C RPi5 AP/router was at 7:30 / 225 degrees on the 1.00 m ring and that the ESP32-S3 receiver was power-only at 1:30 / 45 degrees, 2.00 m from the experiment center.
- Long-horizon protected traffic belongs to the dedicated Node-C AP path between the helper/load node and the laptop second Wi-Fi adapter, and must remain explicitly out of band from the primary sensing corridor.
- Primary sensor: `esp32-c5-a` on `command_stream: ./scripts/capture_esp32_c5_primary_udp_summary_via_router_dnat.sh`.
- Auxiliary sensor: `esp32-c5-b` on `command_stream: ./scripts/capture_esp32_c5_ap_b_udp_summary_via_rpi5.sh`.
- Auxiliary sensor: `esp32-s3-c` on `command_stream: RPI5_HOST="${NODE_C_RPI5_HOST:-<node-c-ap-address>}" RPI5_PORT="${NODE_C_RPI5_PORT:-2222}" ./scripts/capture_esp32_s3_rpi5_node_c_udp_summary.sh`.
- Sidecar stream: `node-a-feature-export` writes `analysis/feature_exports/node_a_features.ndjson`.
- Sidecar stream: `node-b-feature-export` writes `analysis/feature_exports/node_b_features.ndjson`.
- Sidecar stream: `node-c-feature-export` writes `analysis/feature_exports/node_c_features.ndjson`.
- Sidecar stream: `node-c-protected-traffic` writes `traffic/protected_traffic_trace_node_c.ndjson`.
- Sidecar stream: `controller-decisions` writes `logs/controller_decision_log.ndjson`.

## Research Metadata

- Program ID: `D10`
- Campaign / topology / condition: `C5 / T2 / L1`
- Baselines: `B3`
- Novelty placeholders: `[ΔR^min], [ΔB^min], [V^max], [M_Q^min], [L_3^max]`
- D10 reuses the three-node T2 controller stand for a long-horizon stability and inertia-maintenance run.
- Claim-grade D10 requires continuous controller and protected-traffic traces over a meaningfully longer horizon than D08-D09, not a short repeated controller session.
- The dedicated Node-C `RPi5` helper uses the same two-Wi-Fi topology as D07-D09: laptop adapter `<node-c-wifi-adapter>` joins `<redacted-node-c-ssid>`, Node C is reached at `<node-c-ap-address>`, and router-side Ethernet is not required.
- The captured Node-C `ESP32-S3` stream must report `CSI_PROFILE fw_profile=rpi5_node_c_24g fw_role=live`, and Node C geometry must be documented as a real sensing placement rather than direct-attached transport only.
- Defend maintenance claims from long-horizon controller churn and protected-traffic evidence, not from launch intent or the mere presence of an inertia-capable policy name.

## Router AP Control

- Profile ID: `public_reference_ap_profile`
- Radio ref: `Device.WiFi.Radio.2.`
- SSID ref: `Device.WiFi.SSID.4.`
- AccessPoint ref: `Device.WiFi.AccessPoint.3.`
- Requested SSID: `<redacted-main-ssid>`
- Channel plan: `36` / `20MHz`
- These refs match the current lab router image and should be rechecked only if the firmware image or management surface changes.

## Alignment Notes

- Fill `notes/per_node_alignment_notes.md` during or immediately after the session.
- The guided run also writes `logs/cooperative_timing_markers.tsv`; finalization turns it into `analysis/cooperative_timing/summary.md`.
- Record the live versus emulated status of every node and sidecar explicitly.
- Record the Node C capture-reported firmware profile and role.
- Record whether controller decisions, traffic traces, and the block timeline stayed on one shared long-horizon timeline.
- Record the cooperative timing evidence verdict from analysis/cooperative_timing/summary.md.
- Record whether the maintenance layer showed visibly lower churn after the early adaptation blocks.

## Cooperative Timing Checkpoints

- `sync_pre` at `after_capture_start` with `5` controller pulses spaced `250` ms.
- `sync_early` at `before_block:E2` with `5` controller pulses spaced `250` ms.
- `sync_mid` at `before_block:E4` with `5` controller pulses spaced `250` ms.
- `sync_late` at `before_block:E6` with `5` controller pulses spaced `250` ms.
- `sync_post` at `before_capture_stop` with `5` controller pulses spaced `250` ms.

## Extra Artifacts

- `node-a-feature-export` should produce `analysis/feature_exports/node_a_features.ndjson`.
- `node-b-feature-export` should produce `analysis/feature_exports/node_b_features.ndjson`.
- `node-c-feature-export` should produce `analysis/feature_exports/node_c_features.ndjson`.
- `node-c-protected-traffic` should produce `traffic/protected_traffic_trace_node_c.ndjson`.
- `controller-decisions` should produce `logs/controller_decision_log.ndjson`.
- Fill `notes/d10_stability_notes.md`: Record the long-horizon controller policy, continuity of the maintenance traces, and whether the session stayed visibly beyond the D08-D09 short-horizon scope..
- Finalization should produce `analysis/cooperative_timing/summary.md` from the controller-side marker log.

## Block Log

| Block | Planned Duration (s) | Start Wall Time | End Wall Time | Notes |
| --- | --- | --- | --- | --- |
| `W0` | 180 |  |  | three-node and maintenance warm-up |
| `E1` | 240 |  |  | long empty-scene reference under light protected traffic |
| `S1` | 180 |  |  | first static presence period |
| `M1` | 180 |  |  | first slow motion period |
| `E2` | 240 |  |  | first empty recovery window |
| `S2` | 180 |  |  | second static presence period |
| `M2` | 180 |  |  | second slow motion period |
| `E3` | 240 |  |  | second empty recovery window |
| `S3` | 180 |  |  | third static presence period |
| `M3` | 180 |  |  | third slow motion period |
| `E4` | 240 |  |  | third empty recovery window |
| `S4` | 180 |  |  | fourth static presence period |
| `M4` | 180 |  |  | fourth slow motion period |
| `E5` | 240 |  |  | fourth empty recovery window |
| `S5` | 180 |  |  | late-session static confirmation |
| `M5` | 180 |  |  | late-session motion confirmation |
| `E6` | 300 |  |  | final long empty maintenance window |

## Block Instructions

### `W0`

- Take the position and actions described for the current block in the experiment plan.
- Confirm readiness only after you are in the correct position.

### `E1`

- Take the position and actions described for the current block in the experiment plan.
- Confirm readiness only after you are in the correct position.

### `S1`

- Take the position and actions described for the current block in the experiment plan.
- Confirm readiness only after you are in the correct position.

### `M1`

- Take the position and actions described for the current block in the experiment plan.
- Confirm readiness only after you are in the correct position.

### `E2`

- Take the position and actions described for the current block in the experiment plan.
- Confirm readiness only after you are in the correct position.

### `S2`

- Take the position and actions described for the current block in the experiment plan.
- Confirm readiness only after you are in the correct position.

### `M2`

- Take the position and actions described for the current block in the experiment plan.
- Confirm readiness only after you are in the correct position.

### `E3`

- Take the position and actions described for the current block in the experiment plan.
- Confirm readiness only after you are in the correct position.

### `S3`

- Take the position and actions described for the current block in the experiment plan.
- Confirm readiness only after you are in the correct position.

### `M3`

- Take the position and actions described for the current block in the experiment plan.
- Confirm readiness only after you are in the correct position.

### `E4`

- Take the position and actions described for the current block in the experiment plan.
- Confirm readiness only after you are in the correct position.

### `S4`

- Take the position and actions described for the current block in the experiment plan.
- Confirm readiness only after you are in the correct position.

### `M4`

- Take the position and actions described for the current block in the experiment plan.
- Confirm readiness only after you are in the correct position.

### `E5`

- Take the position and actions described for the current block in the experiment plan.
- Confirm readiness only after you are in the correct position.

### `S5`

- Take the position and actions described for the current block in the experiment plan.
- Confirm readiness only after you are in the correct position.

### `M5`

- Take the position and actions described for the current block in the experiment plan.
- Confirm readiness only after you are in the correct position.

### `E6`

- Take the position and actions described for the current block in the experiment plan.
- Confirm readiness only after you are in the correct position.
