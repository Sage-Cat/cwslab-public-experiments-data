# Per-Node Alignment Notes

- Session ID: `d08_c4_t1_l1_budget_aware_controller`
- Primary sensor: `esp32-c5-a` on `command_stream: public-primary-ap-capture-wrapper`
- Auxiliary sensor: `esp32-c5-b` on `command_stream: public-ap-b-capture-wrapper`

## Fill During Capture

- Physical topology used for this D08 run: Node A ESP32-C5 connected to the laptop by USB at `12 o'clock` / `0 degrees`; router/AP at `6 o'clock` / `180 degrees`; Node B RPi5 at `9 o'clock` / `270 degrees`; Node B RPi4 with USB-connected ESP32-C5 at `3 o'clock` / `90 degrees`; Node C RPi5 at `7:30` / `225 degrees` as the protected-traffic helper path; Node C ESP32-S3 connected only to power at the off-ring `1:30` / `45 degrees` corner, `2.00 m` from the experiment center.
- Shared wall-clock reference used for all nodes: controller-side cooperative timing markers in `logs/cooperative_timing_markers.tsv`, emitted at `sync_pre`, `sync_mid`, and `sync_post` around the shared capture timeline.
- Start order across nodes: streams armed at `2026-05-01 16:08:02 EEST`; shared capture began at `2026-05-01 16:08:05 EEST` and finished at `2026-05-01 16:32:31 EEST`.
- Estimated alignment offset(s) in ms: cooperative timing found `esp32-c5-a -> esp32-c5-b` first/last offsets `5.000/10.500 ms` with drift `5.500 ms`.
- Trust verdict for cross-node alignment: `trustworthy` across 15 common pulses. Pair maxima were `6.000 ms` bracketing gap, `5.500 ms` combined uncertainty, and `6.694 ms` residual.
- Cooperative timing evidence artifact: `analysis/cooperative_timing/summary.md`
- Cooperative timing marker log: `logs/cooperative_timing_markers.tsv`

## Per-Node Notes

### `esp32-c5-a`

- Capture source: `command_stream: public-primary-ap-capture-wrapper`
- AP / SSID / channel at capture time: primary AP `<redacted-primary-ssid>`, channel `36`, width `20 MHz`.
- Capture start wall time: shared capture start `2026-05-01 16:08:05 EEST`.
- Capture stop wall time: shared capture finish `2026-05-01 16:32:31 EEST`.
- Transport / UART anomalies: none in final QC. Node A used the primary-router UDP DNAT listener on the laptop; `<local-serial-device>` was used for liveness/reset and serial drain only. Final QC counted `8464` CSI rows with `max_dropped=0`, `max_zero_len=0`, and `max_timeouts=0`.

### `esp32-c5-b`

- Capture source: `command_stream: public-ap-b-capture-wrapper`
- AP / SSID / channel at capture time: AP-B path `<redacted-ap-b-ssid>`, channel `36`.
- Capture start wall time: shared capture start `2026-05-01 16:08:05 EEST`.
- Capture stop wall time: shared capture finish `2026-05-01 16:32:31 EEST`.
- Transport / UART anomalies: none in final QC. Node B used the AP-B UDP summary helper path. Final QC counted `7383` CSI rows with `max_dropped=0`, `max_zero_len=0`, and `max_timeouts=0`.

## Additional Checklist

- Record which node was live and which node or sidecar traces were emulated.
- Record AP-A and AP-B MAC addresses, SSIDs, channels, and any bandwidth mismatch explicitly.
- Record the controller start time and protected-traffic start time against the block timeline.
- Record whether any policy decision appears out of sync with the operator blocks.
- Record the cooperative timing evidence verdict from analysis/cooperative_timing/summary.md.
