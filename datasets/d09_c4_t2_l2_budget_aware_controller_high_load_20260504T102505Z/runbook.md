# Experiment Bundle

- Session ID: `d09_c4_t2_l2_budget_aware_controller_high_load`
- Bundle ID: `d09_c4_t2_l2_budget_aware_controller_high_load_20260504T102505Z`
- Router access: `ssh root@<primary-ap-address>:22`
- Primary sensor: `esp32-c5-a` -> `command_stream: ./scripts/capture_esp32_c5_primary_udp_summary_via_router_dnat.sh`
- Capture seconds: `1500`
- Capture mode: `coordinated_multi_sensor`
- Protected-traffic artifact dir: `traffic/`
- Guided block event log: `logs/operator_block_events.tsv`
- Cooperative timing marker log: `logs/cooperative_timing_markers.tsv`
- Auxiliary sensors: `esp32-c5-b` -> `command_stream: ./scripts/capture_esp32_c5_ap_b_udp_summary_via_rpi5.sh`, `esp32-s3-c` -> `command_stream: RPI5_HOST="${NODE_C_RPI5_HOST:-<node-c-ap-address>}" RPI5_PORT="${NODE_C_RPI5_PORT:-2222}" ./scripts/capture_esp32_s3_rpi5_node_c_udp_summary.sh`
- Sidecar streams: `node-a-feature-export` -> `analysis/feature_exports/node_a_features.ndjson`, `node-b-feature-export` -> `analysis/feature_exports/node_b_features.ndjson`, `node-c-feature-export` -> `analysis/feature_exports/node_c_features.ndjson`, `node-c-protected-traffic` -> `traffic/protected_traffic_trace_node_c.ndjson`, `controller-decisions` -> `logs/controller_decision_log.ndjson`
- Capture-quality gates: enforced during launch and finalization
- Published serial logs: `serial/esp32_guided_session.log.gz`, `serial/esp32_c5_b_guided_session.log.gz`, `serial/esp32_s3_c_guided_session.log.gz` are gzip-compressed sanitized text logs; timing byte offsets refer to the decompressed streams.
- Topology description: `topology.md`
- Alignment notes template: `notes/per_node_alignment_notes.md`
- Cooperative timing evidence summary: `analysis/cooperative_timing/summary.md`
- Bundle artifact templates: `notes/d09_controller_load_notes.md`
- Program ID: `D09`
- Campaign / topology / condition / mode: `C4 / T2 / L2 / H`
- Baselines: `B0, B2, B3`
- Novelty placeholders: `[M_Q], [ΔQ_2^min], [t_c], [V_2^max]`
- Router AP profile: `public_reference_ap_profile`
- Radio ref: `Device.WiFi.Radio.2.`
- SSID ref: `Device.WiFi.SSID.4.`
- AccessPoint ref: `Device.WiFi.AccessPoint.3.`
- Requested SSID: `<redacted-main-ssid>`
- Requested operating channel: `36` / `20MHz`
- Firmware tools: configured outside the public bundle
- Experiment plan: summarized by this runbook

## Generated Scripts

| Step ID | Purpose | Script |
| --- | --- | --- |
| `preflight_local` | Check local WSL/Linux dependencies and capture-device visibility. | `00_preflight_local.sh` |
| `ap_configure` | Apply the requested router radio, SSID, and AccessPoint settings. | `01_ap_configure.sh` |
| `ap_snapshot` | Collect router-side snapshots over SSH or serial console. | `02_ap_snapshot.sh` |
| `firmware_build` | Build the configured ESP32 firmware workspace. | `03_firmware_build.sh` |
| `firmware_flash` | Flash the configured ESP32 firmware workspace. | `04_firmware_flash.sh` |
| `serial_capture` | Capture the ESP32 serial stream for the configured duration. | `05_serial_capture.sh` |
| `serial_capture_esp32_c5_b` | Capture the serial stream for auxiliary sensor `esp32-c5-b`. | `06_serial_capture_esp32_c5_b.sh` |
| `serial_capture_esp32_s3_c` | Capture the serial stream for auxiliary sensor `esp32-s3-c`. | `07_serial_capture_esp32_s3_c.sh` |
| `operator_guided_capture` | Run continuous capture streams and pause for operator confirmation between configured capture blocks. | `08_operator_guided_capture.sh` |
| `run_experiment` | Run preflight, AP setup, AP snapshot, and then the interactive operator-guided capture sequence. | `09_run_experiment.sh` |

## Auxiliary Sensors

| Sensor | Source | Capture Seconds |
| --- | --- | --- |
| `esp32-c5-b` | `command_stream: ./scripts/capture_esp32_c5_ap_b_udp_summary_via_rpi5.sh` | `1500` |
| `esp32-s3-c` | `command_stream: RPI5_HOST="${NODE_C_RPI5_HOST:-<node-c-ap-address>}" RPI5_PORT="${NODE_C_RPI5_PORT:-2222}" ./scripts/capture_esp32_s3_rpi5_node_c_udp_summary.sh` | `1500` |

## Sidecar Streams

| Sidecar | Output | Summary Kind | Required For Claim | Emulated |
| --- | --- | --- | --- | --- |
| `node-a-feature-export` | `analysis/feature_exports/node_a_features.ndjson` | `feature_ndjson` | yes | no |
| `node-b-feature-export` | `analysis/feature_exports/node_b_features.ndjson` | `feature_ndjson` | yes | no |
| `node-c-feature-export` | `analysis/feature_exports/node_c_features.ndjson` | `feature_ndjson` | yes | no |
| `node-c-protected-traffic` | `traffic/protected_traffic_trace_node_c.ndjson` | `traffic_ndjson` | yes | no |
| `controller-decisions` | `logs/controller_decision_log.ndjson` | `controller_ndjson` | yes | no |

## Bundle Artifact Templates

| Artifact | Description | Path |
| --- | --- | --- |
| `d09_controller_load_notes` | Record how the high-load helper path was configured and whether the controller output stayed aligned with the traffic traces. | `notes/d09_controller_load_notes.md` |

## Capture-Quality Gates

- Minimum CSI rows per sensor: `48`
- Maximum CSI row ratio across live sensors: `<= 4`
- Maximum dropped count per sensor: `<= 0`
- Maximum zero_len count per sensor: `<= 0`
- Maximum timeout count per sensor: `<= 0`
- Minimum lines per required sidecar: `1`
- Minimum feature windows per required feature stream: `6`
- Minimum controller decisions per required controller stream: `6`
- Minimum traffic samples per required traffic stream: `6`
- Minimum latency samples per required traffic stream: `6`
- Minimum throughput samples per required traffic stream: `2`
- Maximum controller / traffic disjoint gap: `<= 0`
- Startup activity grace: `20 s`
- Block progress grace: `5 s`
- Require stream activity after every block: `yes`

## Manual Capture Blocks

| Block | Duration (s) | Human Present | Scenario | Objective |
| --- | --- | --- | --- | --- |
| `W0` | 120 | no | three-node and high-load warm-up | confirm that all sensing, controller, and traffic sidecars are active before the first measured block |
| `E1` | 180 | no | shared empty-scene reference under sustained load | collect the empty reference for the three-node controller surface |
| `S1` | 150 | yes | static presence in the shared interaction zone | collect the first loaded static segment |
| `M1` | 150 | yes | slow motion through the shared interaction zone | collect the first loaded motion segment |
| `E2` | 180 | no | empty recovery after the first cycle | observe the reverse transition while load remains active |
| `S2` | 150 | yes | second static presence | provide an in-session repeat for the controller comparison |
| `M2` | 150 | yes | second slow motion segment | provide an in-session repeat for the controller comparison |
| `E3` | 180 | no | final empty recovery | complete the loaded three-node controller bundle and notes |

## Coordinated Multi-Sensor Sequence

- Run `run_experiment` to arm the primary sensor, auxiliary helper sensors, and any configured sidecar streams before the first block.
- The operator still drives one shared block timeline interactively from one terminal.
- The guided run will also emit controller-side cooperative timing checkpoints into `logs/cooperative_timing_markers.tsv`.
- Finalization will compute `analysis/cooperative_timing/summary.md`; treat cooperative timing as strong only when that report is `trustworthy`.
- Fill `notes/per_node_alignment_notes.md` immediately after the session and record which helper nodes or artifact streams were emulated.

## Current Limits

- This bundle by itself does not prove calibrated sensing fidelity; live status still depends on the completed capture, QC outputs, and any required sidecar artifacts.
- It automates the currently configured launcher path for this stand.
- Any `command_stub` helper sensor or emulated sidecar keeps the result below claim-grade live hardware evidence.
- Router AP control stores canonical `Device.WiFi.*` references in config and writes through the current `WiFi.*` `ba-cli` aliases exposed by the router-management toolchain.
- Router commands still run as best-effort snapshots over SSH or serial console, so host-specific driver and shell behavior remain part of the live contract.
