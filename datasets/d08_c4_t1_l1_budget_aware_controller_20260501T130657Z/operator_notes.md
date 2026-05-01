# Operator Notes

- Bundle ID: `d08_c4_t1_l1_budget_aware_controller_20260501T130657Z`
- Session ID: `d08_c4_t1_l1_budget_aware_controller`
- Publication note: this is a sanitized public copy of operator-facing D08 notes
- Target node: `primary prplOS-compatible dual-band AP node`

## Physical Topology

Clock-to-degree convention: `12 o'clock` = `0 degrees`, `3 o'clock` = `90 degrees`, `6 o'clock` = `180 degrees`, and `9 o'clock` = `270 degrees`, measured clockwise from `12 o'clock`.

Primary `1.00 m` ring around the experiment center:

- Node A `ESP32-C5`, connected to the laptop by USB: `12 o'clock` / `0 degrees`.
- Primary router/AP: `6 o'clock` / `180 degrees`.
- Node B `RPi5`: `9 o'clock` / `270 degrees`.
- Node B `RPi4` with USB-connected `ESP32-C5`: `3 o'clock` / `90 degrees`.
- Node C `RPi5`: `7:30` / `7.5 o'clock` / `225 degrees`, used as the protected-traffic helper path.
- Node C `ESP32-S3`, connected only to power: separate off-ring `1:30` / `1.5 o'clock` / `45 degrees` corner, `2.00 m` from the experiment center.

The controlled primary sensing diameter is Node A `ESP32-C5` at `12 o'clock` / `0 degrees` to the router/AP at `6 o'clock` / `180 degrees`.

## Reminders

- D08 was run as a coordinated two-sensor controller experiment with protected traffic on a separate helper path.
- Node A is the laptop-USB `ESP32-C5` primary capture at `12 o'clock` / `0 degrees`.
- Node B contributes the AP-B `ESP32-C5` stream, with public notes separating the `RPi5` and `RPi4 + ESP32-C5` physical positions.
- Node C remains part of the physical setup as the protected-traffic helper path, while the public repository omits the raw protected-traffic and controller sidecar outputs.
- This public copy preserves the claim-grade D08 result: sensing, controller decisions, protected traffic, block timing, and cooperative timing all completed on one shared timeline.

## Research Metadata

- Program ID: `D08`
- Campaign / topology / requested condition: `C4 / T1 / L1`
- Baselines: `B0, B1, B2, B3`
- Support level: `full`

## Block Instructions

## `W0`

- Scenario: controller and traffic warm-up
- Objective: confirm that sensing, protected-traffic, and controller sidecars are all active before the first measured block
- Human present: no
## `E1`

- Scenario: shared empty-scene reference under moderate protected traffic
- Objective: collect the empty baseline for the controller surface
- Human present: no
## `S1`

- Scenario: static presence in the shared interaction zone
- Objective: collect the first controller-driven static segment
- Human present: yes
## `M1`

- Scenario: slow motion through the shared interaction zone
- Objective: collect the first controller-driven motion segment
- Human present: yes
## `E2`

- Scenario: empty recovery after the first cycle
- Objective: observe the reverse transition while traffic remains active
- Human present: no
## `S2`

- Scenario: second static presence
- Objective: provide an in-session repeat for the controller comparison
- Human present: yes
## `M2`

- Scenario: second slow motion segment
- Objective: provide an in-session repeat for the controller comparison
- Human present: yes
## `E3`

- Scenario: final empty recovery
- Objective: complete the controller bundle and notes
- Human present: no
