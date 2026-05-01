# Experiment Report

## Summary

- Program ID: `D07`
- Session ID: `d07_c3_t2_l1_heterogeneity_subset_value`
- Status: `usable as planned`
- Bundle dir: `<cws-lab>/experiments/runs/d07_c3_t2_l1_heterogeneity_subset_value_20260501T114221Z`
- Fixed operating point: `5 GHz / channel 36 / 20 MHz`
- Raw line count: `327895`
- CSI row count: `8576`
- Interference/load note: `interference_load_notes.md`
- Alignment notes: `notes/per_node_alignment_notes.md`
- Auxiliary sensor logs: `serial/esp32_c5_b_guided_session.log, serial/esp32_s3_c_guided_session.log`
- Required sidecar outputs: `-`
- Templated notes completed: `yes`
- Cooperative timing verdict: `trustworthy`
- Cooperative timing summary: `analysis/cooperative_timing/summary.md`
- Campaign / topology / condition: `C3 / T2 / L1`
- Baselines: `B1, B2`
- Capture-quality gates: `enabled`
- Live sensor CSI row ratio: `2.49`

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

## Sensor Quality

| Sensor | CSI Rows | Max Dropped | Max Zero Len | Max Timeouts | Path |
| --- | --- | --- | --- | --- | --- |
| `node-a` | `8576` | `0` | `0` | `0` | `serial/esp32_guided_session.log` |
| `node-b` | `7515` | `0` | `0` | `0` | `serial/esp32_c5_b_guided_session.log` |
| `node-c` | `18702` | `0` | `0` | `0` | `serial/esp32_s3_c_guided_session.log` |

## Executed Blocks

| Block | CSI Rows |
| --- | --- |
| `W0` | `708` |
| `E1` | `1044` |
| `S1` | `895` |
| `M1` | `885` |
| `E2` | `1055` |
| `S2` | `889` |
| `M2` | `889` |
| `E3` | `1043` |

## Segmentation

- Summary: `analysis/guided_segments/summary.md`
