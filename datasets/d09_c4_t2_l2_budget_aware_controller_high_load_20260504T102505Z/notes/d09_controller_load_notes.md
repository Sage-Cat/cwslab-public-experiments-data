# d09_controller_load_notes

- Description: Record how the high-load helper path was configured and whether the controller output stayed aligned with the traffic traces.

- Intended controller policy: `P8` budget-aware controller with `O3` optimizer over live node A/B/C feature sidecars.
- Intended high-load profile and target bitrate: `L2`, `8000000` bps over the Node-C AP path from RPi5 to laptop `<operator-node-c-address>`.
- Helper runtime prerequisite: SSH over `<node-c-ap-address>`, `ping`, and POSIX `dd` on the dedicated Node-C `RPi5` must pass before launch; remote `python3` and local `iperf3` are not required.
- Final synchronization verdict: trustworthy; controller decisions and Node-C protected-traffic traces stayed on one shared wall-clock timeline, the QC summary reports `0 ms` controller/traffic gap, and all required sidecars remained present through finalization.
- Traffic path actually used: Node-C helper `RPi5` at `<node-c-ap-address>` sent live structured protected traffic over `ssh_byte_stream_over_node_c_ap` toward laptop `<operator-node-c-address>` on the dedicated `<redacted-node-c-ssid>` AP.
- Trace timing envelope: traffic trace starts at `2026-05-04 13:26:13.813 EEST` and ends at `2026-05-04 13:53:27.627 EEST`; controller decision log starts at `2026-05-04 13:26:16.662 EEST` and ends at `2026-05-04 13:53:27.854 EEST`.
- Sidecar counts at finalize time: `749` controller decisions, `749` Node-C feature windows, `2509` protected-traffic samples with `1254` throughput entries.
- Sidecar lag / anomalies: no required sidecar stalled during the completed run; the traffic sidecar terminates with an SSH throughput error after capture stop during teardown, but the trace remains present and aligned across the session.
