# Wi-Fi Sensing Site C Experiments

Sanitized measured data for the cooperative Wi-Fi sensing `W`/`D` series.
This is a publication surface: it preserves measurements
needed for independent inspection while excluding credentials, infrastructure
identifiers, private workflow material, and bulk intermediate analysis.

`site-c` is an opaque public grouping. The exact physical identity was not
retained in authoritative private records, and current evidence does not prove
that every historical bundle came from one physical location. Do not interpret
the alias as a location claim; split the repository if that identity is later
recovered and the bundles span multiple sites.

The implementation is a research reference, not an 802.11bf or EasyMesh
compliance claim. Experiment descriptions use **802.11bf-inspired** sensing and
**EasyMesh-inspired** control-plane alignment.

## Repository layout

| Path | Purpose |
| --- | --- |
| [`datasets/`](datasets/) | Twelve original run bundles plus one normalized record-level dataset |
| [`datasets/manifest.json`](datasets/manifest.json) | Authoritative per-bundle inclusion and sanitization record |
| [`scripts/validate_repository.py`](scripts/validate_repository.py) | Dataset integrity and privacy validation |
| [`docs/dataset-policy/`](docs/dataset-policy/) | Publication and privacy boundary |

## Dataset index

| Series | Bundles | Public evidence status |
| --- | ---: | --- |
| W01/W03 | 2 | Early baseline and low-density measured runs |
| D01 | 2 | Repeatability runs |
| D02-D04 | 3 | Quiet-control, support, and under-load captures |
| D05 | 1 | Published for auditability; not claim-grade |
| D07-D10 | 4 | Claim-grade cooperative experiment bundles |
| Normalized summaries | 1 | 347,391 measured records from 16 runs, including canonical D04-D06 and D11 captures |

The easiest analysis surface is
[`record-level-csi-summaries-2026`](datasets/record-level-csi-summaries-2026/).
It is a standard gzip-compressed CSV with RSSI, radio metadata, counters, and
the exact CSI I/Q previews emitted by the firmware. These historical profiles
did not log complete CSI vectors; that acquisition limitation is documented in
the dataset instead of being concealed as a privacy exclusion.

Each bundle contains only paths named in the manifest. The normal surface is
sanitized metadata, runbook and operator notes, event timing, and serial
measurements. Some cooperative runs also contain compact manifest-approved QC,
timing, and experiment summaries. Exact site, participant, network, and device
identifiers are not part of the public evidence surface.

## Inspect and validate

Start with [`datasets/manifest.json`](datasets/manifest.json), then open the
matching bundle. Validate the repository boundary with:

```text
python3 scripts/validate_repository.py
```

## Licensing and citation

The validator is MIT licensed; project-authored data and documentation are
CC BY 4.0 licensed. Imported
material is not relicensed automatically. See [`LICENSE.md`](LICENSE.md) for the
exact scope and attribution guidance.

When using a dataset, cite the repository and preserve its full bundle ID,
including the UTC timestamp suffix, so the measured run remains identifiable.

## Publication policy

[`docs/dataset-policy/policy.md`](docs/dataset-policy/policy.md) defines the
canonical inclusion, provenance, and sanitization rules. Do not publish local
`session.env` files, concrete addresses or identifiers, AP snapshots, private
notes, or unlisted analysis artifacts.
