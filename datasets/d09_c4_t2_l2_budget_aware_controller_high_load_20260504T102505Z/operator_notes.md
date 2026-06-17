# Operator Notes

- Session ID: `d09_c4_t2_l2_budget_aware_controller_high_load`

## Reminders

- D09 reuses the T2 stand but now requires a traceable high-load service surface in addition to the three sensing nodes.
- Use the corrected D07-D09 clock-face layout: Node A ESP32-C5 connected to the laptop by USB at 12 o'clock / 0 degrees; primary router/AP at 6 o'clock / 180 degrees; Node B RPi5 at 9 o'clock / 270 degrees; Node B RPi4 with USB-connected ESP32-C5 at 3 o'clock / 90 degrees; Node C RPi5 at 7:30 / 7.5 o'clock / 225 degrees; Node C ESP32-S3 power-only receiver off the 1.00 m ring at 1:30 / 1.5 o'clock / 45 degrees, 2.00 m from the experiment center.
- Clock-to-degree convention: 12 o'clock is 0 degrees, 3 o'clock is 90 degrees, 6 o'clock is 180 degrees, and 9 o'clock is 270 degrees, measured clockwise from 12.
- Primary ring radius: Node A ESP32-C5, router/AP, Node B RPi5, Node B RPi4 plus ESP32-C5, and Node C RPi5 are each 1.00 m from the experiment center; the Node C ESP32-S3 is the only off-ring device and sits in the separate 1:30 corner at 2.00 m from the center.
- Controlled primary sensing diameter: Node A ESP32-C5 at 12 o'clock / 0 degrees to the router/AP at 6 o'clock / 180 degrees, for a 2.00 m line through the experiment center.
- Node A is captured over the primary-router UDP DNAT listener, Node B uses the AP-B UDP summary path, and Node C is the dedicated `RPi5 + ESP32-S3` `2.4 GHz` sensing path captured over UDP at `<node-c-ap-address>`.
- Protected traffic comes from the dedicated Node-C AP path: the laptop keeps `<node-c-wifi-adapter>` on `<redacted-node-c-ssid>` at `<operator-node-c-address>`, SSH reaches the Node-C RPi5 at `<node-c-ap-address>`, and the RPi5 sends live high-load ping plus byte-stream traffic back to the laptop over that AP.
- Integrated D09 uses two laptop Wi-Fi adapters: `<operator-main-wifi-adapter>` is switched to AP-B for node B, while `<node-c-wifi-adapter>` stays associated to the Node-C AP at `<node-c-ap-address>`; do not use the router-side Node-C address `<private-ip>` for the current stand.
- Verify on the helper `RPi5` that SSH over `<node-c-ap-address>`, `ping`, and POSIX `dd` are present before the run; the structured traffic sidecar now uses SSH byte-stream measurement and does not require remote `python3` or local `iperf3`.
- If the ESP32-S3 stays directly attached without a measured offset from the AP-C position, keep Node C below claim-grade geometry even if transport and UDP capture look healthy.
- Do not allow the helper traffic or management cabling to contaminate the 12-to-6 sensing corridor.

## Topology

- D07-D09 clock/degree convention: 12 o'clock = 0 degrees, 3 o'clock = 90 degrees, 6 o'clock = 180 degrees, 9 o'clock = 270 degrees, measured clockwise from 12.
- Primary 1.00 m ring around the experiment center: Node A ESP32-C5 connected to the laptop by USB at 12 o'clock / 0 degrees; primary router/AP at 6 o'clock / 180 degrees; Node B RPi5 at 9 o'clock / 270 degrees; Node B RPi4 with USB-connected ESP32-C5 at 3 o'clock / 90 degrees; Node C RPi5 at 7:30 / 7.5 o'clock / 225 degrees, midway along the perimeter between the router/AP and the Node B RPi5.
- Off-ring Node C receiver: ESP32-S3 is connected only to power in the separate 1:30 / 1.5 o'clock / 45 degrees corner, 2.00 m from the experiment center.
- Controlled primary sensing diameter: Node A ESP32-C5 at 12 o'clock / 0 degrees to the router/AP at 6 o'clock / 180 degrees.
- Vertical placement: router/AP, active esp32-c5-a, rpi5-a, rpi4-a, Node-C RPi5, and Node-C ESP32-S3 at 0.50 m unless otherwise recorded; capture laptop adjacent to the Node A USB setup.
- Record explicitly that the Node-C RPi5 AP/router was at 7:30 / 225 degrees on the 1.00 m ring and that the ESP32-S3 receiver was power-only at 1:30 / 45 degrees, 2.00 m from the experiment center.
- High-load traffic belongs to the dedicated Node-C AP path between the helper/load node and the laptop second Wi-Fi adapter, and must remain explicitly out of band from the primary sensing corridor.
- Primary sensor: `esp32-c5-a` on `command_stream: ./scripts/capture_esp32_c5_primary_udp_summary_via_router_dnat.sh`.
- Auxiliary sensor: `esp32-c5-b` on `command_stream: ./scripts/capture_esp32_c5_ap_b_udp_summary_via_rpi5.sh`.
- Auxiliary sensor: `esp32-s3-c` on `command_stream: RPI5_HOST="${NODE_C_RPI5_HOST:-<node-c-ap-address>}" RPI5_PORT="${NODE_C_RPI5_PORT:-2222}" ./scripts/capture_esp32_s3_rpi5_node_c_udp_summary.sh`.
- Sidecar stream: `node-a-feature-export` writes `analysis/feature_exports/node_a_features.ndjson`.
- Sidecar stream: `node-b-feature-export` writes `analysis/feature_exports/node_b_features.ndjson`.
- Sidecar stream: `node-c-feature-export` writes `analysis/feature_exports/node_c_features.ndjson`.
- Sidecar stream: `node-c-protected-traffic` writes `traffic/protected_traffic_trace_node_c.ndjson`.
- Sidecar stream: `controller-decisions` writes `logs/controller_decision_log.ndjson`.

## Research Metadata

- Program ID: `D09`
- Campaign / topology / condition: `C4 / T2 / L2`
- Baselines: `B0, B2, B3`
- Novelty placeholders: `[M_Q], [ΔQ_2^min], [t_c], [V_2^max]`
- D09 extends the controller surface to the three-node `T2` stand under sustained high load.
- Claim-grade D09 requires three live sensing streams, a parseable controller decision log, and structured protected-traffic traces with real throughput samples.
- The dedicated Node-C `RPi5` helper uses the same two-Wi-Fi topology as D07: laptop adapter `<node-c-wifi-adapter>` joins `<redacted-node-c-ssid>`, Node C is reached at `<node-c-ap-address>`, and router-side Ethernet is not required.
- The captured Node-C `ESP32-S3` stream must report `CSI_PROFILE fw_profile=rpi5_node_c_24g fw_role=live`, and Node C geometry must be documented as a real sensing placement rather than direct-attached transport only.
- Defend the `L2` label from the recorded throughput and latency traces, not from launch intent alone.

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
- Record whether controller decisions, traffic traces, and the block timeline stayed on one shared timeline.
- Record the cooperative timing evidence verdict from analysis/cooperative_timing/summary.md.

## Cooperative Timing Checkpoints

- `sync_pre` at `after_capture_start` with `5` controller pulses spaced `250` ms.
- `sync_mid` at `before_block:E2` with `5` controller pulses spaced `250` ms.
- `sync_post` at `before_capture_stop` with `5` controller pulses spaced `250` ms.

## Extra Artifacts

- `node-a-feature-export` should produce `analysis/feature_exports/node_a_features.ndjson`.
- `node-b-feature-export` should produce `analysis/feature_exports/node_b_features.ndjson`.
- `node-c-feature-export` should produce `analysis/feature_exports/node_c_features.ndjson`.
- `node-c-protected-traffic` should produce `traffic/protected_traffic_trace_node_c.ndjson`.
- `controller-decisions` should produce `logs/controller_decision_log.ndjson`.
- Fill `notes/d09_controller_load_notes.md`: Record how the high-load helper path was configured and whether the controller output stayed aligned with the traffic traces..
- Finalization should produce `analysis/cooperative_timing/summary.md` from the controller-side marker log.

## Block Log

| Block | Planned Duration (s) | Start Wall Time | End Wall Time | Notes |
| --- | --- | --- | --- | --- |
| `W0` | 120 |  |  | three-node and high-load warm-up |
| `E1` | 180 |  |  | shared empty-scene reference under sustained load |
| `S1` | 150 |  |  | static presence in the shared interaction zone |
| `M1` | 150 |  |  | slow motion through the shared interaction zone |
| `E2` | 180 |  |  | empty recovery after the first cycle |
| `S2` | 150 |  |  | second static presence |
| `M2` | 150 |  |  | second slow motion segment |
| `E3` | 180 |  |  | final empty recovery |

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
