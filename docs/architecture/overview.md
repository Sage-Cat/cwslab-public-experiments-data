# Architecture Overview

This repository has two public product surfaces:

- a script surface that acts as a reference launch path for capture sessions
- a dataset surface that publishes curated measured bundles

Session-specific configuration lives under `scripts/sessions/`, while
`scripts/run_session.sh` provides the generic operator-guided runtime. The
runtime writes a new untracked bundle selected by the operator.

The dataset path is read-only publication content. Each published bundle in
`datasets/` contains only curated public artifacts:

- sanitized serial capture logs
- operator block-event logs
- sanitized metadata
- sanitized runbook and operator notes

Derived analysis and runtime artifacts with non-public configuration are not published here.

## Diagram Source Of Truth

- [public-repo-context.puml](diagrams/public-repo-context.puml)

## Notes

- The script surface is a `reference implementation`, not a certification claim.
- AP/session configuration is `802.11bf-inspired` and uses `EasyMesh-inspired metrics/control-plane alignment`.
- Public artifacts refer only to the `primary prplOS-compatible dual-band AP node`.
