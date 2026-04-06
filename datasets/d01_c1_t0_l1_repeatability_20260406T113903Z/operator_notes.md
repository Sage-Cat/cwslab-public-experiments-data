# Operator Notes

- Bundle ID: `d01_c1_t0_l1_repeatability_20260406T113903Z`
- Session ID: `d01_c1_t0_l1_repeatability`
- Publication note: this is a sanitized public copy of operator-facing notes
- Target node: `primary prplOS-compatible dual-band AP node`

## Reminders

- Repeatability baseline captured on the same physical stand as the earlier C1 precursor.
- Apply a full reset before W0 and treat this as an independent repeat session.
- Keep the primary prplOS-compatible dual-band AP node on 5 GHz / channel 36 / 20 MHz.
- Do not move chairs, table, AP node, capture node, or cables during the capture sequence.

## Research Metadata

- Program ID: `D01`
- Campaign / topology / condition: `C1 / T0 / L1`
- Baselines: `B0, B1`
- Support level: `full`

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
| `W0` | 120 |  |  | post-reset technical warm-up and transport sanity check |
| `E1` | 120 |  |  | empty scene repeated baseline |
| `S1` | 120 |  |  | repeated static presence in the controlled path |
| `M1` | 120 |  |  | repeated slow motion in the controlled path |
| `E2` | 120 |  |  | empty scene recovery after the first repeated motion cycle |
| `S2` | 120 |  |  | second repeated static presence in the same controlled path |
| `M2` | 120 |  |  | second repeated slow motion in the same controlled path |
| `E3` | 120 |  |  | final empty recovery after the repeatability run |

## Block Instructions

## `W0`

- Confirm that the full reset has already been completed before starting.
- Stay outside the controlled path between AP and ESP32-C5.
- If the path looks less stable than in the earlier precursor, stop and record the issue explicitly.

## `E1`

- Leave the controlled 2.00 m path between AP and ESP32-C5.
- If possible, leave the room or stand far enough to avoid affecting the radio path.
- Keep the room layout unchanged.

## `S1`

- Enter the midpoint of the controlled path between AP and ESP32-C5.
- Reproduce the same standing position used in the earlier precursor as closely as practical.
- Do not touch the chair, AP, table, or cables.

## `M1`

- Stay within the same controlled path between AP and ESP32-C5.
- Repeat the same slow-motion pattern used in the earlier precursor as closely as practical.
- Do not change the topology of the stand.

## `E2`

- Leave the controlled path again.
- If possible, leave the room or stand far enough to avoid affecting the radio path.
- Keep the room layout unchanged.

## `S2`

- Return to the midpoint of the controlled path.
- Stand almost still in approximately the same position as in S1.
- Avoid any extra motion not needed for the block.

## `M2`

- Stay within the same controlled path used in M1.
- Repeat the same slow motion pattern as closely as practical.
- Do not move chairs, table, AP, ESP32-C5, or cables.

## `E3`

- Leave the controlled path one final time.
- If possible, leave the room or stand far enough to avoid affecting the radio path.
- Keep the room layout unchanged until the capture is stopped.
