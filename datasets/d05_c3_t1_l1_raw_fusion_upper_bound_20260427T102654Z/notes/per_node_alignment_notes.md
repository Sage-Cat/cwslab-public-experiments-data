# Per-Node Alignment Notes

- Session ID: `d05_c3_t1_l1_raw_fusion_upper_bound`
- Primary sensor: `esp32-c5-a` on `<redacted-serial-device> @ 115200 baud`
- Auxiliary sensor: `esp32-c5-b` on `command_stream: ./scripts/capture_esp32_c5_rpi4_uart_via_rpi5.sh`

## Fill During Capture

- Shared wall-clock reference used for all nodes: controller laptop wall clock in `logs/operator_block_events.tsv`; cooperative checkpoints were written to `logs/cooperative_timing_markers.tsv`.
- Start order across nodes: `esp32-c5-a` serial stream started at `2026-04-27 13:27:07 EEST` (`1777285627169` ms); `esp32-c5-b` command stream started at `2026-04-27 13:27:07 EEST` (`1777285627182` ms); shared `capture_started` was recorded at `2026-04-27 13:27:12 EEST`.
- Estimated alignment offset(s) in ms: cooperative timing analysis used 5 common `sync_mid` pulses. Pair `esp32-c5-a -> esp32-c5-b` had first offset `-1412490.664` ms, last offset `-1413509.248` ms, drift `-1018.584` ms, max uncertainty `12250.930` ms, and max residual `406.805` ms.
- Trust verdict for cross-node alignment: failed. Treat this bundle as a live cooperative capture attempt, not as calibrated cross-node fusion evidence.
- Cooperative timing evidence artifact: `analysis/cooperative_timing/summary.md`
- Cooperative timing marker log: `logs/cooperative_timing_markers.tsv`

## Per-Node Notes

### `esp32-c5-a`

- Capture source: `<redacted-serial-device> @ 115200 baud`
- AP / SSID / channel at capture time: primary AP path, SSID `<redacted-primary-ssid>`, channel `36`, `20 MHz`; exact AP-A BSSID was not extracted into this note.
- Capture start wall time: `2026-04-27 13:27:07 EEST` stream start; `2026-04-27 13:27:12 EEST` shared capture start.
- Capture stop wall time: `2026-04-27 13:51:49 EEST` stream stop.
- Transport / UART anomalies: no dropped, zero-length, or timeout counters were observed by QC; firmware identified `fw_profile=primary_ap fw_role=live`; log contains `1452` CSI rows.

### `esp32-c5-b`

- Capture source: `command_stream: ./scripts/capture_esp32_c5_rpi4_uart_via_rpi5.sh`
- AP / SSID / channel at capture time: RPi5 AP-B helper path, SSID `<redacted-helper-ssid>`, channel `36`, `20 MHz`; ESP32-C5-B used the `rpi5_ap_b` live firmware profile. The helper ESP32 board serial observed during pre-run repair was `<redacted-board-serial>`; exact AP-B BSSID was not extracted into this bundle note.
- Capture start wall time: `2026-04-27 13:27:07 EEST` stream start; `2026-04-27 13:27:12 EEST` shared capture start.
- Capture stop wall time: `2026-04-27 13:51:49 EEST` stream stop.
- Transport / UART anomalies: no dropped, zero-length, or timeout counters were observed by QC, but the helper stream produced only `102` CSI rows versus `1452` on node A, reported `stream_output_stalled` after block `E3`, and no `capture_finished` event was recorded. Cooperative timing verdict was `failed`.

## Additional Checklist

- AP-A/AP-B details recorded above; exact BSSIDs were not extracted into this note.
- Raw file mapping: node A is `serial/esp32_guided_session.log`; node B is `serial/esp32_c5_b_guided_session.log`.
- Capture start order, shared wall-clock reference, and cooperative timing verdict are recorded above.
- Cooperative timing evidence: `5` common pulses, max uncertainty `12250.930` ms, max residual `406.805` ms, final verdict `failed`.
- Block transitions were driven from the controller/operator laptop and recorded in `logs/operator_block_events.tsv`; timing checkpoints were recorded in `logs/cooperative_timing_markers.tsv`.
- Final cross-node alignment trust verdict: failed.
