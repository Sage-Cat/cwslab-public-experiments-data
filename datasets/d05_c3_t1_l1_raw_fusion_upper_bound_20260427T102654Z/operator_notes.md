# Operator Notes

- Bundle ID: `d05_c3_t1_l1_raw_fusion_upper_bound_20260427T102654Z`
- Session ID: `d05_c3_t1_l1_raw_fusion_upper_bound`
- Publication note: this is a sanitized public copy of operator-facing D05 notes
- Target node: `primary prplOS-compatible dual-band AP node`

## Reminders

- D05 was run as the coordinated cooperative bridge experiment.
- Keep the primary AP path on 5 GHz / channel 36 / 20 MHz.
- Node A is the primary local ESP32-C5 serial stream.
- Node B is the helper ESP32-C5 UART stream forwarded through the helper-node command path.
- This public copy is not claim-grade cooperative evidence; it preserves the node-B stall, missing `capture_finished` event, row-ratio failure, and failed timing verdict.

## Research Metadata

- Program ID: `D05`
- Campaign / topology / requested condition: `C3 / T1 / L1`
- Baselines: `B1, B4`
- Support level: `full`

## Block Log Template

| Block | Planned Duration (s) | Start Wall Time | End Wall Time | Notes |
| --- | --- | --- | --- | --- |
| `W0` | 120 |  |  | two-node transport warm-up and alignment sanity check |
| `E1` | 180 |  |  | shared empty-scene reference for both nodes |
| `S1` | 150 |  |  | static presence in the shared interaction zone |
| `M1` | 150 |  |  | slow motion through the shared interaction zone |
| `E2` | 180 |  |  | empty recovery after the first cooperative cycle |
| `S2` | 150 |  |  | second static presence in the shared interaction zone |
| `M2` | 150 |  |  | second slow motion in the shared interaction zone |
| `E3` | 180 |  |  | final empty recovery for cooperative upper-bound anchoring |

## Block Instructions

## `W0`

- Stay outside both controlled paths while both raw capture processes are started.
- Confirm that both raw files are growing and that the alignment note template is open for editing.
- Do not continue if one node still lacks a trustworthy AP path or serial stream.

## `E1`

- Leave the shared operator interaction zone and both controlled paths.
- Keep the room layout unchanged for both Node A and Node B.
- Record any node-specific disturbance immediately in the alignment notes.

## `S1`

- Stand in the shared midpoint zone chosen to be visible to both Node A and Node B.
- Stay almost still and do not touch any AP, sensor, stand, or helper host.
- If visibility is asymmetric between nodes, record that immediately.

## `M1`

- Move slowly through the shared interaction zone without leaving the region visible to both nodes.
- Keep the topology of both stands unchanged.
- Record any timing drift noticed between the two capture hosts.

## `E2`

- Leave both controlled paths again.
- Keep both nodes powered and both raw capture processes running.
- Record any restart or serial glitch explicitly before continuing.

## `S2`

- Return to approximately the same shared midpoint used in S1.
- Stand almost still and avoid unnecessary motion.
- Confirm in notes that both raw streams are still recording.

## `M2`

- Repeat the same slow-motion pattern used in M1 as closely as practical.
- Do not move APs, sensors, helper hosts, or cables.
- Record whether node-wise timing still appears coherent.

## `E3`

- Leave the shared interaction zone one final time and keep both capture processes running until the block ends.
- Stop raw capture only after both nodes have finished the same block timeline.
- Fill the final trust verdict in notes/per_node_alignment_notes.md before treating the bundle as usable.

