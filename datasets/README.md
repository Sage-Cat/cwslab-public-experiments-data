# Datasets

This directory contains curated measured bundles only.

For direct machine-readable access, use
[`record-level-csi-summaries-2026`](record-level-csi-summaries-2026/). It
contains 347,391 normalized measured records from 16 runs, including four
completed canonical runs that were absent from the original bundle index.

## Included Surface

- sanitized serial capture logs, including multi-node logs where the public bundle needs them
- normalized record-level RSSI, radio metadata, counters, and the exact 8- or
  16-value CSI I/Q previews emitted by the capture firmware
- operator block-event logs and cooperative timing logs where they are part of the claim surface
- sanitized metadata
- sanitized runbook/operator notes
- sanitized compact analysis/QC/report summaries only when required for
  interpretation and explicitly included by the manifest

## Excluded Surface

- unlisted/bulk analysis, intermediate outputs, and private reporting packages
- environment snapshots
- AP snapshot/configuration logs
- concrete SSIDs, IP addresses, MAC addresses, BSSIDs, and local paths

Identifiers in serial logs are redacted or pseudonymized. Measurement timing,
block labels, channel/rate/RSSI fields, and emitted CSI preview values are
preserved. Full vectors were not recorded by these firmware profiles and are
therefore not available for publication.

See [policy.md](../docs/dataset-policy/policy.md) and `manifest.json`.
