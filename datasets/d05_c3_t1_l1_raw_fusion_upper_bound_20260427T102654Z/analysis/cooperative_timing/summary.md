# Cooperative Timing Evidence

- Session ID: `d05_c3_t1_l1_raw_fusion_upper_bound`
- Marker log: `datasets/d05_c3_t1_l1_raw_fusion_upper_bound_20260427T102654Z/logs/cooperative_timing_markers.tsv`
- Sensors: `esp32-c5-a, esp32-c5-b`
- Common pulses analyzed: `5`
- Final verdict: `failed`

## Pair Summary

| Pair | Common Pulses | First Offset (ms) | Last Offset (ms) | Drift (ms) | Drift (ppm) | Max Gap (ms) | Max Uncertainty (ms) | Max Residual (ms) | Verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `esp32-c5-a -> esp32-c5-b` | `5` | `-1412490.664` | `-1413509.248` | `-1018.584` | `-1047442.179` | `23464.556` | `12250.930` | `406.805` | `failed` |

## Pulse Detail: `esp32-c5-a -> esp32-c5-b`

| Marker | Controller Epoch (ms) | Offset (ms) | Combined Uncertainty (ms) | Bracketing Gap (ms) |
| --- | --- | --- | --- | --- |
| `sync_mid.p1` | `1777286270150` | `-1412490.664` | `12232.278` | `23464.556` |
| `sync_mid.p2` | `1777286270440` | `-1412490.664` | `12232.278` | `23464.556` |
| `sync_mid.p3` | `1777286270734` | `-1413509.248` | `12250.930` | `23464.556` |
| `sync_mid.p4` | `1777286271026` | `-1413509.248` | `12250.930` | `23464.556` |
| `sync_mid.p5` | `1777286271317` | `-1413509.248` | `12250.930` | `23464.556` |
