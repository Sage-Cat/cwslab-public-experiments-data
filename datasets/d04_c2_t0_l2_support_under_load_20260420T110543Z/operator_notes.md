# Operator Notes

- Bundle ID: `d04_c2_t0_l2_support_under_load_20260420T110543Z`
- Session ID: `d04_c2_t0_l2_support_under_load`
- Publication note: this is a sanitized public copy of operator-facing notes
- Target node: `primary prplOS-compatible dual-band AP node`

## Reminders

- Loaded support capture recorded on the same physical stand as D01-D03.
- Keep the primary prplOS-compatible dual-band AP node on 5 GHz / channel 36 / 20 MHz.
- Keep helper traffic nodes and extra cabling outside the controlled path between AP and capture node.
- Start the protected-traffic generator and trace collector after W0 and before E1, then keep the load active through E3.
- This public copy does not include retained protected-traffic traces, so it must not be treated as claim-grade D04 evidence by itself.

## Research Metadata

- Program ID: `D04`
- Campaign / topology / requested condition: `C2 / T0 / L2`
- Baselines: `B0, B4`
- Support level: `stub`
- TODO(verify): protected-traffic traces are missing from the retained public bundle, so this public measured surface is not claim-grade D04 evidence.

## AP Control Surface

- Profile ID: `public_reference_ap_profile`
- Radio ref: `Device.WiFi.Radio.2.`
- SSID ref: `Device.WiFi.SSID.4.`
- AccessPoint ref: `Device.WiFi.AccessPoint.3.`
- Channel plan: `36` / `20MHz`
- Requested SSID: `<redacted>`
- TODO(driver): verify the target AP node exposes the same writable surface before treating this mapping as stable hardware truth.

## Block Log Template

| Block | Planned Duration (s) | Start Wall Time | End Wall Time | Notes |
| --- | --- | --- | --- | --- |
| `W0` | 120 |  |  | technical warm-up and protected-traffic synchronization check before the loaded capture |
| `E1` | 180 |  |  | extended empty reference under injected protected traffic |
| `S1` | 150 |  |  | extended static presence under the same injected load |
| `M1` | 150 |  |  | extended slow motion under the same injected load |
| `E2` | 180 |  |  | extended empty recovery after the first loaded motion cycle |
| `S2` | 150 |  |  | second extended static presence under the same injected load |
| `M2` | 150 |  |  | second extended slow motion under the same injected load |
| `E3` | 180 |  |  | final extended empty recovery under the same injected load |

## Block Instructions

## `W0`

- Stay outside the controlled path between AP and capture node.
- Keep the helper traffic nodes powered and reachable, but do not start the protected traffic yet.
- Verify that the future trace files will be saved into the bundle traffic/ directory before moving to E1.

## `E1`

- Before pressing Enter, confirm the protected-traffic generator is already running and the trace collector is recording.
- Leave the controlled 2.00 m path between AP and capture node.
- Keep the room layout unchanged and avoid entering the path during the block.

## `S1`

- Keep the protected-traffic generator running continuously.
- Enter the midpoint of the controlled path between AP and capture node.
- Stand almost still and do not touch the chair, AP node, table, capture node, or helper nodes.

## `M1`

- Keep the protected-traffic generator and trace collector running.
- Stay within the same controlled path between AP and capture node.
- Move slowly back and forth without changing the topology of the stand.

## `E2`

- Leave the controlled path again while keeping the traffic load active.
- If the helper traffic path restarts or stalls, record that explicitly in the optional note before continuing.
- Keep the room layout unchanged.

## `S2`

- Confirm the protected-traffic trace is still recording before pressing Enter.
- Return to the midpoint of the controlled path and stand almost still.
- Avoid unnecessary motion not required for the block.

## `M2`

- Keep the protected-traffic generator and trace collector running.
- Stay within the same controlled path used in M1.
- Repeat the same slow motion pattern without moving helper nodes, AP node, capture node, or cables.

## `E3`

- Leave the controlled path one final time while keeping the traffic load active until the block ends.
- Stop the protected-traffic generator only after the block is finished and the capture is complete.
- Export and copy the trace files into traffic/ before finalizing the bundle.
