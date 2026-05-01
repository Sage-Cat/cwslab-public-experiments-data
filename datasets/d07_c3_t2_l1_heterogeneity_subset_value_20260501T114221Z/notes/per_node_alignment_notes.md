# Per-Node Alignment Notes

- Session ID: `d07_c3_t2_l1_heterogeneity_subset_value`
- Primary sensor: `esp32-c5-a` on `command_stream: ./scripts/capture_esp32_c5_primary_udp_summary_via_router_dnat.sh`
- Auxiliary sensor: `esp32-c5-b` on `command_stream: ./scripts/capture_esp32_c5_ap_b_udp_summary_via_rpi5.sh`
- Auxiliary sensor: `esp32-s3-c` on `command_stream: public-node-c-capture-wrapper`

## Fill During Capture

- Physical topology used for this D07 run: Node A ESP32-C5 connected to the laptop by USB at `12 o'clock` / `0 degrees`; router/AP at `6 o'clock` / `180 degrees`; Node B RPi5 at `9 o'clock` / `270 degrees`; Node B RPi4 with USB-connected ESP32-C5 at `3 o'clock` / `90 degrees`; Node C RPi5 at `7:30` / `225 degrees` on the `1.00 m` ring; Node C ESP32-S3 connected only to power at the off-ring `1:30` / `45 degrees` corner, `2.00 m` from the experiment center.
- Shared wall-clock reference used for all nodes: controller-side cooperative timing markers in `logs/cooperative_timing_markers.tsv`, emitted at `sync_pre`, `sync_mid`, and `sync_post` around the shared capture timeline.
- Start order across nodes: `esp32-c5-a` stream started at `2026-05-01 14:43:49 EEST` (`1777635829264` ms), `esp32-c5-b` at `2026-05-01 14:43:49 EEST` (`1777635829282` ms), and `esp32-s3-c` at `2026-05-01 14:43:49 EEST` (`1777635829302` ms). Shared capture began at `2026-05-01 14:43:50 EEST` (`1777635830355` ms) and finished at `2026-05-01 15:08:12 EEST` (`1777637292297` ms).
- Estimated alignment offset(s) in ms: cooperative timing found `esp32-c5-a -> esp32-c5-b` first/last offsets `4.000/15.000 ms` with drift `11.000 ms`, and `esp32-c5-a -> esp32-s3-c` first/last offsets `10.000/30.000 ms` with drift `20.000 ms`.
- Trust verdict for cross-node alignment: `trustworthy` across 15 common pulses. Pair maxima were `6.000 ms` bracketing gap, `5.500 ms` combined uncertainty, and residuals `6.714 ms` for Node B and `5.011 ms` for Node C.
- Cooperative timing evidence artifact: `analysis/cooperative_timing/summary.md`
- Cooperative timing marker log: `logs/cooperative_timing_markers.tsv`

## Per-Node Notes

### `esp32-c5-a`

- Capture source: `command_stream: ./scripts/capture_esp32_c5_primary_udp_summary_via_router_dnat.sh`
- AP / SSID / channel at capture time: primary AP `<redacted-primary-ssid>`, channel `36`, width `20 MHz`; firmware profile observed as `primary_ap`, role `live`.
- Capture start wall time: stream start `2026-05-01 14:43:49 EEST`; shared capture start `2026-05-01 14:43:50 EEST`.
- Capture stop wall time: stream stopped `2026-05-01 15:08:11 EEST`; shared capture finished `2026-05-01 15:08:12 EEST`.
- Transport / UART anomalies: none in final QC. Node A used the primary-router UDP DNAT listener on the laptop; `<local-serial-device>` was used for liveness/reset and serial drain only. Final QC counted `8576` CSI rows with `max_dropped=0`, `max_zero_len=0`, and `max_timeouts=0`.

### `esp32-c5-b`

- Capture source: `command_stream: ./scripts/capture_esp32_c5_ap_b_udp_summary_via_rpi5.sh`
- AP / SSID / channel at capture time: AP-B path `<redacted-ap-b-ssid>`, channel `36`; firmware profile observed as `rpi5_ap_b`, role `live`.
- Capture start wall time: stream start `2026-05-01 14:43:49 EEST`; shared capture start `2026-05-01 14:43:50 EEST`.
- Capture stop wall time: stream stopped `2026-05-01 15:08:12 EEST`; shared capture finished `2026-05-01 15:08:12 EEST`.
- Transport / UART anomalies: none in final QC. Node B used the RPi5 AP-B UDP/tcpdump summary path. Final QC counted `7515` CSI rows with `max_dropped=0`, `max_zero_len=0`, and `max_timeouts=0`.

### `esp32-s3-c`

- Capture source: `command_stream: public-node-c-capture-wrapper`
- AP / SSID / channel at capture time: Node-C AP `<redacted-node-c-ssid>`, channel `6`; firmware profile observed as `rpi5_node_c_24g`, role `live`.
- Capture start wall time: stream start `2026-05-01 14:43:49 EEST`; shared capture start `2026-05-01 14:43:50 EEST`.
- Capture stop wall time: stream stopped `2026-05-01 15:08:12 EEST`; shared capture finished `2026-05-01 15:08:12 EEST`.
- Transport / UART anomalies: none in final QC. Node C used the laptop TL-WN722N USB Wi-Fi path to `<node-c-ap-address>:<ssh-port>`, then RPi5 UDP/tcpdump capture from the ESP32-S3. Final QC counted `18702` CSI rows with `max_dropped=0`, `max_zero_len=0`, and `max_timeouts=0`.

## Additional Checklist

- Record the live versus emulated status of every node explicitly.
- Record AP-A, AP-B, and Node-C AP SSIDs, channels, and any bandwidth mismatch explicitly.
- Record capture start order, shared wall-clock reference, and the cooperative timing evidence verdict from analysis/cooperative_timing/summary.md.
- Record the reported common pulse count, max uncertainty, and max residual from the cooperative timing evidence summary.
- Record the subset ordering used for the post-run ranking.
- Record any node-specific drift or blockage that could bias subset value.
