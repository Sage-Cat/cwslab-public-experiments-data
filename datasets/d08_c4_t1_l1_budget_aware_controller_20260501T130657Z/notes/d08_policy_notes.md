# d08_policy_notes

- Description: Record which controller policy ran, what still depended on hardware-specific setup, and whether policy outputs aligned with traffic traces.

- Intended controller policy: `P8` budget-aware controller with `O3` optimizer over live node A/B feature sidecars.
- Real versus emulated controller/traffic components: protected traffic was live Node-C helper-path traffic between the dedicated RPi5 helper and the laptop-side second Wi-Fi path; controller decisions were derived from live node A/B feature sidecars.
- Helper runtime prerequisite: SSH, `ping`, and POSIX `dd` on the dedicated Node-C `RPi5` helper path had to pass before launch; remote `python3` and local `iperf3` were not required.
- Final synchronization verdict: trustworthy. Cooperative timing used 15 common pulses with max bracketing gap 6.000 ms, max uncertainty 5.500 ms, and max residual 6.694 ms; controller/traffic overlap gap was 0 ms. No sidecar lag requiring exclusion was observed in the finalized QC summary.
