# Operator Notes

- Bundle ID: `d02_c1_t0_l0_honest_quiet_candidate_20260406T122440Z`
- Session ID: `d02_c1_t0_l0_honest_quiet_candidate`
- Publication note: this is a sanitized public copy of operator-facing notes
- Target node: `primary prplOS-compatible dual-band AP node`

## Reminders

- Honest quiet-control candidate captured on the same physical stand as D01.
- Run this only if D01 already produced a usable repeatability package.
- Keep the primary prplOS-compatible dual-band AP node on 5 GHz / channel 36 / 20 MHz.
- Do not claim `L0` if the room and network background are not independently quieter than ordinary `L1`.
- If quietness cannot be independently justified, keep the measured data but downgrade the final interpretation to `L1`.

## Research Metadata

- Program ID: `D02`
- Campaign / topology / requested condition: `C1 / T0 / L0`
- Baselines: `B0, B1`
- Support level: `full`
- TODO(verify): this public measured bundle does not itself establish that the run may be claimed as `L0`.

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
| `W0` | 90 |  |  | short technical warm-up before the quiet-control attempt |
| `E1` | 180 |  |  | longer empty baseline under the quietest honestly available condition |
| `S1` | 120 |  |  | static presence under the same quiet-control attempt |
| `M1` | 120 |  |  | slow motion under the same quiet-control attempt |
| `E2` | 180 |  |  | final empty recovery under the same quiet-control attempt |

## Block Instructions

## `W0`

- Confirm that D01 has already been completed and saved.
- Stay outside the controlled path between AP and capture node.
- If the path looks unstable or the background is not honestly quieter, stop and do not claim `L0`.

## `E1`

- Leave the controlled 2.00 m path between AP and capture node.
- If possible, leave the room or stand far enough to avoid affecting the radio path.
- Keep the room layout unchanged and minimize nearby human activity.

## `S1`

- Enter the midpoint of the controlled path between AP and capture node.
- Stand almost still with a natural posture.
- Do not touch the chair, AP node, table, or cables.

## `M1`

- Stay within the same controlled path between AP and capture node.
- Move slowly back and forth without leaving the corridor.
- Do not change the topology of the stand.

## `E2`

- Leave the controlled path one final time.
- If possible, leave the room or stand far enough to avoid affecting the radio path.
- Keep the room layout unchanged until the capture is stopped.
