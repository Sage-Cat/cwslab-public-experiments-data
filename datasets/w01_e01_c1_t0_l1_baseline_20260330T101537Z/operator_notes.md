# Operator Notes

- Bundle ID: `w01_e01_c1_t0_l1_baseline_20260330T101537Z`
- Session ID: `w01_e01_c1_t0_l1_baseline`
- Publication note: this is a sanitized public copy of operator-facing notes
- Target node: `primary prplOS-compatible dual-band AP node`

## Reminders

- Baseline single-link session with fixed stand geometry and an operator-guided block sequence.
- Keep the stand geometry unchanged during the full capture sequence.
- Keep the primary prplOS-compatible dual-band AP node on 5 GHz / channel 36 / 20 MHz.
- Do not move chairs, table, AP node, capture node, cables, or other static obstacles once W0 starts.

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
| `W0` | 120 |  |  | technical warm-up and transport sanity check |
| `E1` | 120 |  |  | empty scene, first baseline |
| `S1` | 120 |  |  | one person standing almost still in the controlled path |
| `M1` | 120 |  |  | one person moving slowly inside the controlled path |
| `E2` | 120 |  |  | empty scene, recovery after the first motion cycle |
| `S2` | 120 |  |  | repeated static presence in the same controlled path |
| `M2` | 120 |  |  | repeated slow motion in the same controlled path |
| `E3` | 120 |  |  | final empty recovery |

## Block Instructions

## `W0`

- Stay outside the controlled path between AP and ESP32-C5.
- Do not move the chair, AP, table, ESP32-C5, or cables.
- If AP state or UART output looks unstable, stop before E1.

## `E1`

- Leave the controlled 2.00 m path between AP and ESP32-C5.
- If possible, leave the room or stand far enough to avoid affecting the radio path.
- Keep the room layout unchanged.

## `S1`

- Enter the midpoint of the controlled path between AP and ESP32-C5.
- Stand almost still with a natural posture.
- Do not touch the chair, AP, table, or cables.

## `M1`

- Stay within the same controlled path between AP and ESP32-C5.
- Move slowly back and forth without leaving the corridor.
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
