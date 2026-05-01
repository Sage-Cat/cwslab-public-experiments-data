# Cooperative Timing Evidence

- Session ID: `d08_c4_t1_l1_budget_aware_controller`
- Marker log: `logs/cooperative_timing_markers.tsv`
- Sensors: `esp32-c5-a, esp32-c5-b`
- Common pulses analyzed: `15`
- Final verdict: `trustworthy`

## Pair Summary

| Pair | Common Pulses | First Offset (ms) | Last Offset (ms) | Drift (ms) | Drift (ppm) | Max Gap (ms) | Max Uncertainty (ms) | Max Residual (ms) | Verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `esp32-c5-a -> esp32-c5-b` | `15` | `5.000` | `10.500` | `5.500` | `4.701` | `6.000` | `5.500` | `6.694` | `trustworthy` |

## Pulse Detail: `esp32-c5-a -> esp32-c5-b`

| Marker | Controller Epoch (ms) | Offset (ms) | Combined Uncertainty (ms) | Bracketing Gap (ms) |
| --- | --- | --- | --- | --- |
| `sync_pre.p1` | `1777640885695` | `5.000` | `5.000` | `5.000` |
| `sync_pre.p2` | `1777640885988` | `5.000` | `5.000` | `5.000` |
| `sync_pre.p3` | `1777640886283` | `5.000` | `5.000` | `5.000` |
| `sync_pre.p4` | `1777640886579` | `6.000` | `4.000` | `5.000` |
| `sync_pre.p5` | `1777640886871` | `5.000` | `5.000` | `5.000` |
| `sync_mid.p1` | `1777641598662` | `4.500` | `5.500` | `6.000` |
| `sync_mid.p2` | `1777641598964` | `15.000` | `5.000` | `5.000` |
| `sync_mid.p3` | `1777641599272` | `12.500` | `5.500` | `6.000` |
| `sync_mid.p4` | `1777641599581` | `10.000` | `5.000` | `5.000` |
| `sync_mid.p5` | `1777641599887` | `10.000` | `5.000` | `5.000` |
| `sync_post.p1` | `1777642347505` | `6.000` | `5.000` | `5.000` |
| `sync_post.p2` | `1777642347801` | `12.500` | `3.500` | `6.000` |
| `sync_post.p3` | `1777642348101` | `16.000` | `5.000` | `5.000` |
| `sync_post.p4` | `1777642348412` | `15.500` | `4.500` | `5.000` |
| `sync_post.p5` | `1777642348729` | `10.500` | `5.500` | `6.000` |
