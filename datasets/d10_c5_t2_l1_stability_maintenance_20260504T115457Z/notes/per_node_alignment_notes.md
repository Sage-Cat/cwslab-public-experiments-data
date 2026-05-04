# Per-Node Alignment Notes

- Session ID: `d10_c5_t2_l1_stability_maintenance`
- Primary sensor: `esp32-c5-a` on `command_stream: ./scripts/capture_esp32_c5_primary_udp_summary_via_router_dnat.sh`
- Auxiliary sensor: `esp32-c5-b` on `command_stream: ./scripts/capture_esp32_c5_ap_b_udp_summary_via_rpi5.sh`
- Auxiliary sensor: `esp32-s3-c` on `command_stream: RPI5_HOST="${NODE_C_RPI5_HOST:-<node-c-ap-address>}" RPI5_PORT="${NODE_C_RPI5_PORT:-2222}" ./scripts/capture_esp32_s3_rpi5_node_c_udp_summary.sh`

## Fill During Capture

- Shared wall-clock reference used for all nodes: laptop controller wall clock from `logs/operator_block_events.tsv` plus cooperative timing pulses in `logs/cooperative_timing_markers.tsv`.
- Start order across nodes: `esp32-c5-a` at `2026-05-04 14:56:05 EEST`, `esp32-c5-b` at `2026-05-04 14:56:05 EEST`, `esp32-s3-c` at `2026-05-04 14:56:05 EEST`; shared capture started at `2026-05-04 14:56:07 EEST`.
- Estimated alignment offset(s) in ms: `esp32-c5-a -> esp32-c5-b` drift `19.500 ms` over the session, max bracketing gap `6.000 ms`, max uncertainty `5.500 ms`; `esp32-c5-a -> esp32-s3-c` drift `40.500 ms`, max bracketing gap `6.000 ms`, max uncertainty `5.500 ms`.
- Trust verdict for cross-node alignment: `trustworthy` for both analyzed node pairs.
- Cooperative timing evidence artifact: `analysis/cooperative_timing/summary.md`
- Cooperative timing marker log: `logs/cooperative_timing_markers.tsv`

## Per-Node Notes

### `esp32-c5-a`

- Capture source: `command_stream: ./scripts/capture_esp32_c5_primary_udp_summary_via_router_dnat.sh`
- AP / SSID / channel at capture time: primary AP profile `<redacted-main-ssid>`, channel `36`, `20 MHz`, captured through the primary-router UDP DNAT listener.
- Capture start wall time: `2026-05-04 14:56:05 EEST`
- Capture stop wall time: `2026-05-04 16:25:44 EEST`
- Transport / UART anomalies: none recorded by QC; `34169` CSI rows, `max_dropped=0`, `max_zero_len=0`, `max_timeouts=0`. The stream stderr contains only the expected termination marker from controlled shutdown.

### `esp32-c5-b`

- Capture source: `command_stream: ./scripts/capture_esp32_c5_ap_b_udp_summary_via_rpi5.sh`
- AP / SSID / channel at capture time: AP-B helper path over the self-restoring RPi5 experimental AP wrapper, captured through the AP-B UDP summary path.
- Capture start wall time: `2026-05-04 14:56:05 EEST`
- Capture stop wall time: `2026-05-04 16:25:45 EEST`
- Transport / UART anomalies: none recorded by QC; `29501` CSI rows, `max_dropped=0`, `max_zero_len=0`, `max_timeouts=0`. The stream stderr contains only the expected termination marker from controlled shutdown.

### `esp32-s3-c`

- Capture source: `command_stream: RPI5_HOST="${NODE_C_RPI5_HOST:-<node-c-ap-address>}" RPI5_PORT="${NODE_C_RPI5_PORT:-2222}" ./scripts/capture_esp32_s3_rpi5_node_c_udp_summary.sh`
- AP / SSID / channel at capture time: dedicated Node-C AP path at `<node-c-ap-address>:2222`; capture-reported firmware profile `rpi5_node_c_24g`, firmware role `live`, channel `6`.
- Capture start wall time: `2026-05-04 14:56:05 EEST`
- Capture stop wall time: `2026-05-04 16:25:46 EEST`
- Transport / UART anomalies: none recorded by QC; `67199` CSI rows, `max_dropped=0`, `max_zero_len=0`, `max_timeouts=0`. The stream stderr contains only the expected termination marker from controlled shutdown.

## Additional Checklist

- Record the live versus emulated status of every node and sidecar explicitly.
  - Observed: every sensor stream and every required sidecar is live, with `emulated=false`.
- Record the Node C capture-reported firmware profile and role.
  - Observed: Node C reports `fw_profile=rpi5_node_c_24g` and `fw_role=live`.
- Record whether controller decisions, traffic traces, and the block timeline stayed on one shared long-horizon timeline.
  - Observed: yes; controller decisions span `2026-05-04 14:56:07 EEST` to `16:25:46 EEST`, protected traffic spans `14:56:05` to `16:25:46`, and all blocks `W0` through `E6` completed on the shared operator timeline.
- Record the cooperative timing evidence verdict from analysis/cooperative_timing/summary.md.
  - Observed: `trustworthy`.
- Record whether the maintenance layer showed visibly lower churn after the early adaptation blocks.
  - Observed: final `E6` had no controller state/rate-tier changes across `142` decisions; late `E5` still had `10` changes, so the maintenance-effect claim should be quantified in downstream analysis rather than asserted solely from operator notes.
