# Operator Notes

- Bundle ID: `d03_c2_t0_l1_full_support_capture_20260406T125404Z`
- Session ID: `d03_c2_t0_l1_full_support_capture`
- Publication note: this is a sanitized public copy of operator-facing notes
- Target node: `primary prplOS-compatible dual-band AP node`

## Reminders

- Full support capture recorded on the same physical stand as D01.
- Human-present blocks were performed by a single participant.
- Keep the verified geometry unchanged.
- Keep the primary prplOS-compatible dual-band AP node on 5 GHz / channel 36 / 20 MHz.
- Treat the observed room and network state as `L1` unless a fresh review independently justifies a quieter label.
- Preserve the raw full-rate capture because later raw-central and local-feature comparators must use the same material.

## Research Metadata

- Program ID: `D03`
- Campaign / topology / condition: `C2 / T0 / L1`
- Baselines: `B4`
- Support level: `full`
- Preserve raw full-rate capture because later raw-central comparison must run on the same material.
- Do not claim completed `D03` if any support blocks are missing.

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
| `W0` | 120 |  |  | technical warm-up and raw-stream sanity check before the D03 support capture |
| `E1` | 180 |  |  | extended empty reference for local-features and raw-central comparison |
| `S1` | 150 |  |  | extended static presence support segment |
| `M1` | 150 |  |  | extended slow-motion support segment |
| `E2` | 180 |  |  | extended empty recovery after the first long cycle |
| `S2` | 150 |  |  | second extended static presence support segment |
| `M2` | 150 |  |  | second extended slow-motion support segment |
| `E3` | 180 |  |  | final extended empty recovery for comparator anchoring |

## Block Instructions

## `W0`

- Stay outside the controlled path between AP and capture node.
- Do not move the chair, AP node, table, capture node, or cables.
- If raw UART output or AP state looks unstable, stop before `E1`.

## `E1`

- Leave the controlled 2.00 m path between AP and capture node.
- If possible, leave the room or stand far enough to avoid affecting the radio path.
- Keep the room layout unchanged and avoid nearby activity.

## `S1`

- Enter the midpoint of the controlled path between AP and capture node.
- Stand almost still with a natural posture.
- Do not touch the chair, AP node, table, or cables.

## `M1`

- Stay within the same controlled path between AP and capture node.
- Move slowly back and forth without leaving the corridor.
- Do not change the topology of the stand.

## `E2`

- Leave the controlled path again.
- If possible, leave the room or stand far enough to avoid affecting the radio path.
- Keep the room layout unchanged.

## `S2`

- Return to the midpoint of the controlled path.
- Stand almost still in approximately the same position as in `S1`.
- Avoid any extra motion not needed for the block.

## `M2`

- Stay within the same controlled path used in `M1`.
- Repeat the same slow motion pattern as closely as practical.
- Do not move chairs, table, AP node, capture node, or cables.

## `E3`

- Leave the controlled path one final time.
- If possible, leave the room or stand far enough to avoid affecting the radio path.
- Keep the room layout unchanged until the capture is stopped.
