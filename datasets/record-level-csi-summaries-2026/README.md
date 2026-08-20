# Record-Level CWS CSI Summaries (2026)

This bundle makes the measured CSI/RSSI records from the public CWS campaign
easy to download and analyze without parsing the original serial logs. It also
adds four completed canonical runs that were not previously downloadable:

- `d04_c2_t0_l2_support_under_load_20260423T103612Z`;
- `d05_c3_t1_l1_raw_fusion_upper_bound_20260427T124558Z`;
- `d06_c3_t1_l1_local_features_vs_raw_central_20260427T133103Z`;
- `d11_c6_t2_l1_supportive_search_comparison_20260504T134316Z`.

## Download

- [`csi_summaries.csv.gz`](data/csi_summaries.csv.gz) contains 347,391
  well-formed measured `CSI_SUMMARY` records from 16 run bundles and three
  abstract receiver roles.
- [`source_accounting.csv`](data/source_accounting.csv) reports the source-file,
  accepted-row, and malformed-row counts for every run.
- [`DATA_DICTIONARY.md`](DATA_DICTIONARY.md) defines every column.
- [`SHA256SUMS`](SHA256SUMS) provides byte-level integrity hashes.

## What the records contain

Each row preserves the radio metadata, RSSI, noise floor, firmware counters,
CSI length, and the exact 8- or 16-value signed I/Q preview emitted by the
capture firmware. MAC/BSSID values, network names, host addresses, absolute
timestamps, paths, and concrete device identifiers are absent. Receiver names
are stable abstract roles. Time is relative to the first accepted record in
each explicitly numbered capture segment, so receiver clock resets remain
visible without producing false negative elapsed times.

## Important acquisition limitation

These historical CWS firmware profiles emitted `CSI_SUMMARY` records, not full
CSI vectors. The complete vector was not present in the private source logs,
so it cannot truthfully be reconstructed or published. The I/Q previews are
real measured CSI samples, but they must not be described as complete channel
vectors. The AutoCenter and UGRR repositories contain full record-level CSI
vectors from different capture firmware and experiments.

The 64 excluded rows all came from the already-public, non-claim-grade D05
bundle and were malformed or concatenated serial fragments. They remain in
that bundle's original serial logs for auditability and are counted in
`source_accounting.csv`.

## License

This dataset is available under CC BY 4.0 as specified in the repository
[`LICENSE.md`](../../LICENSE.md).
