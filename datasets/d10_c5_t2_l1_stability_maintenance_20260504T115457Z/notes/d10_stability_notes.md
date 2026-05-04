# d10_stability_notes

- Description: Record the long-horizon controller policy, continuity of the maintenance traces, and whether the session stayed visibly beyond the D08-D09 short-horizon scope.

- Intended controller policy: `P8` budget-aware controller with `O3` optimizer over live node A/B/C feature sidecars for a long-horizon maintenance run.
- Intended protected-traffic profile and target bitrate: `L1`, `1500000` bps over the Node-C AP path from the RPi5 helper to the laptop `<operator-node-c-address>`.
- Observed controller policy: `P8_joint_heuristic_inertia` with `O3_qbit_inertial`, `optimizer_enabled=true`, `2640` accepted decisions, and no rejected decisions in `logs/controller_decision_log.ndjson`.
- Observed protected-traffic profile: live `L1` SSH byte-stream plus ping traffic over the Node-C AP path, `11180` traffic samples, `5590` throughput samples, `5` timeout records, average throughput approximately `8.49 Mbps`, and average ping latency approximately `6.823 ms`.
- Long-horizon continuity: capture streams started at `2026-05-04 14:56:05 EEST`, shared capture began at `14:56:07`, all planned blocks `W0` through `E6` completed, and capture finished at `16:25:47`.
- Maintenance interpretation: the early adaptation checkpoint was recorded after `M1` at `15:12:11`; the final `E6` stability window had `142` controller decisions and `0` observed state/rate-tier changes. A late `E5` empty window still showed `10` rate-tier changes, so downstream analysis should quantify churn before using this bundle for the final R3 maintenance-effect claim.
- Comparator note: use the strongest validated non-maintenance controller trace family from the D08-D09 lineage as the inertia-off reference in post-analysis; this bundle supplies the D10 inertia-on long-horizon trace.
- Final synchronization verdict: `trustworthy`; cooperative timing analyzed `25` common pulses, with trustworthy pair verdicts for `esp32-c5-a -> esp32-c5-b` and `esp32-c5-a -> esp32-s3-c`.
- Trace-continuity note: controller and traffic streams overlap with `0 ms` controller/traffic gap in QC; no dropped, zero-length, or timeout CSI counters were observed for the three live sensor streams.
