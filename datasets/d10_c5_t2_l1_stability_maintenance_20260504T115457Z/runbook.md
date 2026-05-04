# WSL/Linux Experiment Bundle

- Session ID: `d10_c5_t2_l1_stability_maintenance`
- Bundle dir: `<cws-lab>/experiments/runs/d10_c5_t2_l1_stability_maintenance_20260504T115457Z`
- Workspace root: `<cws-lab>`
- Router access: `ssh root@<primary-ap-address>:22`
- Primary sensor: `esp32-c5-a` -> `command_stream: ./scripts/capture_esp32_c5_primary_udp_summary_via_router_dnat.sh`
- Capture seconds: `3720`
- Capture mode: `coordinated_multi_sensor`
- Protected-traffic artifact dir: `traffic/`
- Guided block event log: `logs/operator_block_events.tsv`
- Cooperative timing marker log: `logs/cooperative_timing_markers.tsv`
- Auxiliary sensors: `esp32-c5-b` -> `command_stream: ./scripts/capture_esp32_c5_ap_b_udp_summary_via_rpi5.sh`, `esp32-s3-c` -> `command_stream: RPI5_HOST="${NODE_C_RPI5_HOST:-<node-c-ap-address>}" RPI5_PORT="${NODE_C_RPI5_PORT:-2222}" ./scripts/capture_esp32_s3_rpi5_node_c_udp_summary.sh`
- Sidecar streams: `node-a-feature-export` -> `analysis/feature_exports/node_a_features.ndjson`, `node-b-feature-export` -> `analysis/feature_exports/node_b_features.ndjson`, `node-c-feature-export` -> `analysis/feature_exports/node_c_features.ndjson`, `node-c-protected-traffic` -> `traffic/protected_traffic_trace_node_c.ndjson`, `controller-decisions` -> `logs/controller_decision_log.ndjson`
- Capture-quality gates: enforced during launch and finalization
- Published serial logs: `serial/esp32_guided_session.log.gz`, `serial/esp32_c5_b_guided_session.log.gz`, `serial/esp32_s3_c_guided_session.log.gz` are gzip-compressed raw text logs; timing byte offsets refer to the decompressed streams.
- Topology description: `topology.md`
- Alignment notes template: `notes/per_node_alignment_notes.md`
- Cooperative timing evidence summary: `analysis/cooperative_timing/summary.md`
- Bundle artifact templates: `notes/d10_stability_notes.md`
- Program ID: `D10`
- Campaign / topology / condition / mode: `C5 / T2 / L1 / H`
- Baselines: `B3`
- Novelty placeholders: `[ΔR^min], [ΔB^min], [V^max], [M_Q^min], [L_3^max]`
- Router AP profile: `public_reference_ap_profile`
- Radio ref: `Device.WiFi.Radio.2.`
- SSID ref: `Device.WiFi.SSID.4.`
- AccessPoint ref: `Device.WiFi.AccessPoint.3.`
- Requested SSID: `<redacted-main-ssid>`
- Requested operating channel: `36` / `20MHz`
- Firmware tools path: `<workspace>/.espressif`
- Experiment plan: `<cws-lab>/experiments/plans/2026-04-02-d10-c5-t2-l1-stability-maintenance-plan-uk.md`

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
| `esp32-c5-b` | `command_stream: ./scripts/capture_esp32_c5_ap_b_udp_summary_via_rpi5.sh` | `3720` |
| `esp32-s3-c` | `command_stream: RPI5_HOST="${NODE_C_RPI5_HOST:-<node-c-ap-address>}" RPI5_PORT="${NODE_C_RPI5_PORT:-2222}" ./scripts/capture_esp32_s3_rpi5_node_c_udp_summary.sh` | `3720` |

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
| `d10_stability_notes` | Record the long-horizon controller policy, continuity of the maintenance traces, and whether the session stayed visibly beyond the D08-D09 short-horizon scope. | `notes/d10_stability_notes.md` |

## Capture-Quality Gates

- Minimum CSI rows per sensor: `120`
- Maximum CSI row ratio across live sensors: `<= 4`
- Maximum dropped count per sensor: `<= 0`
- Maximum zero_len count per sensor: `<= 0`
- Maximum timeout count per sensor: `<= 0`
- Minimum lines per required sidecar: `1`
- Minimum feature windows per required feature stream: `12`
- Minimum controller decisions per required controller stream: `12`
- Minimum traffic samples per required traffic stream: `12`
- Minimum latency samples per required traffic stream: `12`
- Minimum throughput samples per required traffic stream: `2`
- Maximum controller / traffic disjoint gap: `<= 0`
- Startup activity grace: `20 s`
- Block progress grace: `5 s`
- Require stream activity after every block: `yes`

## Manual Capture Blocks

| Block | Duration (s) | Human Present | Scenario | Objective |
| --- | --- | --- | --- | --- |
| `W0` | 180 | no | three-node and maintenance warm-up | confirm that sensing, controller, and protected-traffic sidecars remain active before the long measured horizon begins |
| `E1` | 240 | no | long empty-scene reference under light protected traffic | establish the initial stability baseline before adaptation cycles |
| `S1` | 180 | yes | first static presence period | trigger the first controller adaptation cycle under light service load |
| `M1` | 180 | yes | first slow motion period | observe whether the controller settles after the first moving disturbance |
| `E2` | 240 | no | first empty recovery window | measure how quickly the maintenance layer stabilizes after the first cycle |
| `S2` | 180 | yes | second static presence period | repeat the disturbance after an initial maintenance phase |
| `M2` | 180 | yes | second slow motion period | compare churn against the first motion cycle |
| `E3` | 240 | no | second empty recovery window | observe longer maintenance behavior after multiple adaptations |
| `S3` | 180 | yes | third static presence period | continue the long-horizon disturbance sequence without resetting the session |
| `M3` | 180 | yes | third slow motion period | extend the controller trace into late-session motion behavior |
| `E4` | 240 | no | third empty recovery window | inspect whether late-session empty recovery shows reduced reconfiguration churn |
| `S4` | 180 | yes | fourth static presence period | verify that maintenance behavior remains stable after prolonged runtime |
| `M4` | 180 | yes | fourth slow motion period | collect the last repeated moving disturbance for long-horizon comparison |
| `E5` | 240 | no | fourth empty recovery window | measure stability after the final repeated disturbance cycle |
| `S5` | 180 | yes | late-session static confirmation | confirm the maintenance layer still reacts cleanly near the end of the session |
| `M5` | 180 | yes | late-session motion confirmation | provide one final motion interval before the closing stability window |
| `E6` | 300 | no | final long empty maintenance window | close the session with an explicit late-stage stability window for churn and continuity analysis |

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
