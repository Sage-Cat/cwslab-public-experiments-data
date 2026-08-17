# CWSlab Public Experiments Data

Sanitized measured data and public launch profiles for cooperative Wi-Fi
sensing experiments. This is a publication surface: it preserves measurements
needed for independent inspection while excluding credentials, infrastructure
identifiers, private workflow material, and bulk intermediate analysis.

The implementation is a research reference, not an 802.11bf or EasyMesh
compliance claim. Experiment descriptions use **802.11bf-inspired** sensing and
**EasyMesh-inspired** control-plane alignment.

## Repository layout

| Path | Purpose |
| --- | --- |
| [`datasets/`](datasets/) | Twelve curated measured bundles |
| [`datasets/manifest.json`](datasets/manifest.json) | Authoritative per-bundle inclusion and sanitization record |
| [`scripts/`](scripts/) | Public launch wrappers and session profiles |
| [`docs/dataset-policy/`](docs/dataset-policy/) | Publication and privacy boundary |
| [`docs/`](docs/) | Supporting repository and runtime notes |

## Dataset index

| Series | Bundles | Public evidence status |
| --- | ---: | --- |
| W01/W03 | 2 | Early baseline and low-density measured runs |
| D01 | 2 | Repeatability runs |
| D02-D04 | 3 | Quiet-control, support, and under-load captures |
| D05 | 1 | Published for auditability; not claim-grade |
| D07-D10 | 4 | Claim-grade cooperative experiment bundles |

Each bundle contains only paths named in the manifest. The normal surface is
sanitized metadata, runbook and operator notes, event timing, and serial
measurements. Some cooperative runs also contain compact manifest-approved QC,
timing, and experiment summaries. Exact site, participant, network, and device
identifiers are not part of the public evidence surface.

## Inspect or reproduce

Start with [`datasets/manifest.json`](datasets/manifest.json), then open the
matching bundle. To rerun a launch profile, copy its environment template to an
untracked `session.env`, replace every placeholder locally, and run the matching
wrapper:

```text
cp scripts/sessions/<session-id>/session.env.example \
   scripts/sessions/<session-id>/session.env
scripts/run_<session-id>.sh
```

The launch scripts require compatible sensing firmware, serial access, SSH
access to a compatible AP, and the local commands documented in
[`scripts/README.md`](scripts/README.md). They create a new runtime bundle; they
do not modify the published datasets.

Validate the repository boundary with:

```text
python3 scripts/validate_repository.py
bash -n scripts/*.sh
```

## Licensing and citation

Licensing is split by content type: project-authored scripts are MIT licensed,
while project-authored data and documentation are CC BY 4.0 licensed. Imported
material is not relicensed automatically. See [`LICENSE.md`](LICENSE.md) for the
exact scope and attribution guidance.

When using a dataset, cite the repository and preserve its full bundle ID,
including the UTC timestamp suffix, so the measured run remains identifiable.

## Publication policy

[`docs/dataset-policy/policy.md`](docs/dataset-policy/policy.md) defines the
canonical inclusion, provenance, and sanitization rules. Do not publish local
`session.env` files, concrete addresses or identifiers, AP snapshots, private
notes, or unlisted analysis artifacts.
