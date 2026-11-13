# Bill of materials

Quantities are for one enclosure. Sizes come from the CAD model in `cad/RPi-PSU-enclosure.sc`.

## Printed parts

| Part | File | Qty | Notes |
|---|---|---|---|
| Base | `stl/base.stl` | 1 | The same part for Raspberry Pi 4 and Raspberry Pi 5. |
| Lid | `stl/lid_rpi<4\|5>_<logo>[_fan<30\|40>].stl` | 1 | Pick the lid for your board, logo and fan option. See the variant table in the README. |

## Electronics

| Item | Qty | Notes |
|---|---|---|
| Raspberry Pi 4 Model B or Raspberry Pi 5 | 1 | The lid sets the USB and Ethernet cut-outs, because the two boards have them in mirrored positions. |
| Mean Well RS-25-5 power supply (5 V, 5 A, 78 × 51 × 28 mm) | 1 | Set the output trimmer to 5.1 V before you connect the Pi. |
| 5 V leads from the power supply to the GPIO header | 4 | Two red and two black wires, 0.5 mm² (AWG 20), about 10 cm, each with a female Dupont crimp contact on the Pi end. They go to GPIO pins 2 and 4 (5 V) and 6 and 14 (GND). |
| Mains cable, 2-core flat, about 7.5 × 4.5 mm (for example H03VVH2-F 2 × 0.75 mm²) | 1 | The base has a strain-relief tongue that clamps the cable by 0.5 mm. |
| Fan 40 × 40 × 10 mm, 5 V | 0 or 1 | Only with a `_fan40` lid. Both 5 V GPIO pins carry the Pi's power, so wire a two-wire fan to the power supply's +V and −V terminals. On a Pi 5, a fan with a 4-pin JST-SH plug can use the board's fan connector and runs under temperature control. |
| Fan 30 × 30 × 10 mm, 5 V | 0 or 1 | Only with a `_fan30` lid. A 7 mm thick 30 mm fan does not fit the clips. |

## Fasteners

| Item | Qty | Where |
|---|---|---|
| M2.5 heat-set insert, OD 3.55 mm, length 4 mm | 4 | Base standoffs for the Pi. |
| M2.5 × 6 socket head cap screw (ISO 4762) | 4 | Pi to standoffs. M2.5 × 8 also fits. Longer screws hit the bottom of the hole. |
| M3 heat-set insert, Ruthex RX-M3x5.7 or equivalent | 4 | Lid corner bosses. |
| M3 × 8 flat head socket cap screw (countersunk, ISO 10642) | 6 | 4 hold the lid to the base from below. 2 hold the power supply, and enter its threaded holes 2.5 mm. Do not use shorter screws for the power supply: an M3 × 6 enters it only 0.5 mm. Do not use longer ones either: the RS-25-5 allows at most 3 mm. |
| Wall screw, head under 8 mm, shank under 4 mm (for example 3.5 × 30 mm) with wall plug | 2 | Keyhole wall mount, 50 mm apart. |
