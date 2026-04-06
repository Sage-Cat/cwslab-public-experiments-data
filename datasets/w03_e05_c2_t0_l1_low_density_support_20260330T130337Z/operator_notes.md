# Operator Notes

- Bundle ID: `w03_e05_c2_t0_l1_low_density_support_20260330T130337Z`
- Session ID: `w03_e05_c2_t0_l1_low_density_support`
- Publication note: this is a sanitized public copy of operator-facing notes
- Target node: `primary prplOS-compatible dual-band AP node`

## Reminders

- Support capture intended for later reduced-density and comparator studies on the same stand geometry.
- Keep the stand geometry unchanged during the full capture sequence.
- Keep the primary prplOS-compatible dual-band AP node on 5 GHz / channel 36 / 20 MHz.
- Preserve the raw full-rate capture because later comparisons depend on the uncompressed measurement surface.
- TODO(hw): the current hardware runtime does not yet expose a validated on-device sensing-rate knob for this package; treat this bundle as a support capture, not as proof of true hardware low-rate control.
- TODO(verify): validate how faithfully later offline subsampling represents a future real low-rate hardware mode on this path.

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
| `W0` | 120 |  |  | technical warm-up and raw-stream sanity check before the C2 support capture |
| `E1` | 180 |  |  | extended empty reference for reduced-density and compression support |
| `S1` | 150 |  |  | extended static presence support segment |
| `M1` | 150 |  |  | extended slow-motion support segment |
| `E2` | 180 |  |  | extended empty recovery after the first long cycle |
| `S2` | 150 |  |  | second extended static presence support segment |
| `M2` | 150 |  |  | second extended slow-motion support segment |
| `E3` | 180 |  |  | final extended empty recovery for comparator anchoring |

## Block Instructions

## `W0`

- Stay outside the controlled path between AP and ESP32-C5.
- Do not move the chair, AP, table, ESP32-C5, or cables.
- If raw UART output or AP state looks unstable, stop before E1.

## `E1`

- Leave the controlled 2.00 m path between AP and ESP32-C5.
- If possible, leave the room or stand far enough to avoid affecting the radio path.
- Keep the room layout unchanged and avoid nearby activity.

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
