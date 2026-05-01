# Operator Notes

- Bundle ID: `d07_c3_t2_l1_heterogeneity_subset_value_20260501T114221Z`
- Session ID: `d07_c3_t2_l1_heterogeneity_subset_value`
- Publication note: this is a sanitized public copy of operator-facing D07 notes
- Target node: `primary prplOS-compatible dual-band AP node`

## Physical Topology

Clock-to-degree convention: `12 o'clock` = `0 degrees`, `3 o'clock` = `90 degrees`, `6 o'clock` = `180 degrees`, and `9 o'clock` = `270 degrees`, measured clockwise from `12 o'clock`.

Primary `1.00 m` ring around the experiment center:

- Node A `ESP32-C5`, connected to the laptop by USB: `12 o'clock` / `0 degrees`.
- Primary router/AP: `6 o'clock` / `180 degrees`.
- Node B `RPi5`: `9 o'clock` / `270 degrees`.
- Node B `RPi4` with USB-connected `ESP32-C5`: `3 o'clock` / `90 degrees`.
- Node C `RPi5`: `7:30` / `7.5 o'clock` / `225 degrees`, midway along the perimeter between the router/AP and the Node B `RPi5`.
- Node C `ESP32-S3`, connected only to power: separate off-ring `1:30` / `1.5 o'clock` / `45 degrees` corner, `2.00 m` from the experiment center.

The controlled primary sensing diameter is Node A `ESP32-C5` at `12 o'clock` / `0 degrees` to the router/AP at `6 o'clock` / `180 degrees`.

## Reminders

- D07 was run as a coordinated three-node heterogeneity/subset-value experiment.
- Node A is the laptop-USB `ESP32-C5` primary capture at `12 o'clock` / `0 degrees`.
- Node B contributes the AP-B `ESP32-C5` stream, with public notes separating the `RPi5` and `RPi4 + ESP32-C5` physical positions.
- Node C uses the dedicated `RPi5 + ESP32-S3` path, with the `RPi5` on the 1.00 m ring and the power-only `ESP32-S3` in the off-ring 2.00 m corner.
- This public copy preserves the claim-grade result: all streams were live, synchronized, and completed all planned blocks.

## Research Metadata

- Program ID: `D07`
- Campaign / topology / requested condition: `C3 / T2 / L1`
- Baselines: `B1, B2`
- Support level: `full`

## Block Instructions

## `W0`

- Scenario: three-node warm-up and subset sanity check
- Objective: confirm that all three node streams are active before capture
- Human present: no
## `E1`

- Scenario: shared empty-scene reference
- Objective: collect the three-node empty baseline
- Human present: no
## `S1`

- Scenario: static presence in the shared interaction zone
- Objective: collect the first heterogeneity segment
- Human present: yes
## `M1`

- Scenario: slow motion through the shared interaction zone
- Objective: collect the first moving three-node segment
- Human present: yes
## `E2`

- Scenario: empty recovery after the first cycle
- Objective: capture the reverse transition to empty
- Human present: no
## `S2`

- Scenario: second static presence
- Objective: provide an in-session repeat for the subset ranking surface
- Human present: yes
## `M2`

- Scenario: second slow motion segment
- Objective: provide an in-session repeat for the moving subset comparison
- Human present: yes
## `E3`

- Scenario: final empty recovery
- Objective: complete the three-node bundle and subset manifest
- Human present: no
