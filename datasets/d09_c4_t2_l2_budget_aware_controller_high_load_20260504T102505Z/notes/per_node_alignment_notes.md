# Per-Node Alignment Notes

- Session ID: `d09_c4_t2_l2_budget_aware_controller_high_load`
- Primary sensor: `esp32-c5-a` on `command_stream: ./scripts/capture_esp32_c5_primary_udp_summary_via_router_dnat.sh`
- Auxiliary sensor: `esp32-c5-b` on `command_stream: ./scripts/capture_esp32_c5_ap_b_udp_summary_via_rpi5.sh`
- Auxiliary sensor: `esp32-s3-c` on `command_stream: RPI5_HOST="${NODE_C_RPI5_HOST:-<node-c-ap-address>}" RPI5_PORT="${NODE_C_RPI5_PORT:-2222}" ./scripts/capture_esp32_s3_rpi5_node_c_udp_summary.sh`

## Fill During Capture

- Shared wall-clock reference used for all nodes: `capture_epoch_ms` / `epoch_ms` wall-clock timestamps, controller `ts_ms`, traffic `ts_ms`, and cooperative timing checkpoints in `logs/cooperative_timing_markers.tsv`.
- Start order across nodes: `esp32-c5-a` at `2026-05-04 13:26:13 EEST`, `esp32-c5-b` at `2026-05-04 13:26:13 EEST`, then `esp32-s3-c` at `2026-05-04 13:26:13 EEST`; shared capture declared started at `2026-05-04 13:26:16 EEST`.
- Estimated alignment offset(s) in ms: `esp32-c5-a -> esp32-c5-b` drifted from `5.5` to `14.0` ms; `esp32-c5-a -> esp32-s3-c` drifted from `9.0` to `26.0` ms across `15` common pulses.
- Trust verdict for cross-node alignment: trustworthy.
- Cooperative timing evidence artifact: `analysis/cooperative_timing/summary.md`
- Cooperative timing marker log: `logs/cooperative_timing_markers.tsv`

## Per-Node Notes

### `esp32-c5-a`

- Capture source: `command_stream: ./scripts/capture_esp32_c5_primary_udp_summary_via_router_dnat.sh`
- AP / SSID / channel at capture time: primary router AP `<redacted-main-ssid>`, `5 GHz`, channel `36`, `20 MHz`.
- Capture start wall time: `2026-05-04 13:26:13.673 EEST`.
- Capture stop wall time: `2026-05-04 13:53:25.235 EEST`.
- Transport / UART anomalies: none noted in the QC summary; `max_dropped=0`, `max_zero_len=0`, `max_timeouts=0`.

### `esp32-c5-b`

- Capture source: `command_stream: ./scripts/capture_esp32_c5_ap_b_udp_summary_via_rpi5.sh`
- AP / SSID / channel at capture time: AP-B experimental `5 GHz` path (`rpi5_ap_b` firmware profile), channel `36`; the exact SSID string was not separately logged in this bundle.
- Capture start wall time: `2026-05-04 13:26:13.698 EEST`.
- Capture stop wall time: `2026-05-04 13:53:26.062 EEST`.
- Transport / UART anomalies: none noted in the QC summary; `max_dropped=0`, `max_zero_len=0`, `max_timeouts=0`.

### `esp32-s3-c`

- Capture source: `command_stream: RPI5_HOST="${NODE_C_RPI5_HOST:-<node-c-ap-address>}" RPI5_PORT="${NODE_C_RPI5_PORT:-2222}" ./scripts/capture_esp32_s3_rpi5_node_c_udp_summary.sh`
- AP / SSID / channel at capture time: dedicated Node-C helper AP `<redacted-node-c-ssid>`, `2.4 GHz`, channel `6`.
- Capture start wall time: `2026-05-04 13:26:13.728 EEST`.
- Capture stop wall time: `2026-05-04 13:53:26.887 EEST`.
- Transport / UART anomalies: firmware reported `fw_profile=rpi5_node_c_24g` and `fw_role=live`; no dropped or zero-length rows are reported in the QC summary.

## Additional Checklist

- Record the live versus emulated status of every node and sidecar explicitly: all three sensors and all required sidecars are live (`emulated: no` in the QC summary).
- Record the Node C capture-reported firmware profile and role: `fw_profile=rpi5_node_c_24g`, `fw_role=live`.
- Record whether controller decisions, traffic traces, and the block timeline stayed on one shared timeline: yes; final QC reports `0 ms` controller/traffic gap and the block/timing markers span the same session window.
- Record the cooperative timing evidence verdict from analysis/cooperative_timing/summary.md: trustworthy.
