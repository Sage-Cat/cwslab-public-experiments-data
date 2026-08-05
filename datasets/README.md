# Datasets

This directory contains curated measured bundles only.

## Included Surface

- sanitized serial capture logs, including multi-node logs where the public bundle needs them
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
block labels, channel/rate/RSSI fields, and CSI values are preserved.

See [policy.md](../docs/dataset-policy/policy.md) and `manifest.json`.
