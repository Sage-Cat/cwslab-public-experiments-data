# Wi-Fi sensing data: site C

Sanitized raw captures from twelve cooperative Wi-Fi sensing runs are stored
under `datasets/`. The directory name is the stable public run identifier.

Every retained bundle contains only:

- `serial/`: raw ESP32 CSI capture stream(s);
- `logs/operator_block_events.tsv`: measured operator block timing;
- `logs/cooperative_timing_markers.tsv`, when present: raw cross-node timing
  markers.

Private site, network, host, device, and credential data were removed before
publication. Analysis, normalized summaries, reports, runbooks, configuration,
validators, and reproduction scripts are intentionally excluded. The alias
`site-c` is opaque and must not be interpreted as an exact physical-location
claim.

Data and documentation reuse terms are in [LICENSE.md](LICENSE.md).
