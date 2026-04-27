# d05_cooperative_bridge_notes

- Description: Record which node was live, whether node-B was captured through RPi4, and how AP-B was staged for the run.

- Node A live path summary: laptop-attached ESP32-C5 on `<redacted-serial-device> @ 115200`, `fw_profile=primary_ap fw_role=live`, primary AP path on 5 GHz channel 36 / 20 MHz, raw log `serial/esp32_guided_session.log`, `1452` CSI rows, max dropped/zero_len/timeouts all `0`.
- Node B helper path summary: RPi4-backed ESP32-C5 stream collected through `./scripts/capture_esp32_c5_rpi4_uart_via_rpi5.sh`, `fw_profile=rpi5_ap_b fw_role=live`, raw log `serial/esp32_c5_b_guided_session.log`, `102` CSI rows, max dropped/zero_len/timeouts all `0`; stream output stalled after block `E3`.
- Real AP-B and node-B UART path details: AP-B was staged on the RPi5 single-AP helper path with SSID `<redacted-helper-ssid>`, channel 36, 20 MHz, and static helper sensor IP `<redacted-helper-sensor-ip>`; the ESP32-C5-B board serial observed during pre-run repair was `<redacted-board-serial>`. The bundle does not contain a clean `capture_finished` event, the live sensor CSI row ratio was `14.24`, and cooperative timing evidence failed, so this run is analysis-only/non-claim-grade cooperative evidence.
