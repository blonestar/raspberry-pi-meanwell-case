# Editing the design

The source is `cad/RPi-PSU-enclosure.sc`, made in [SolidCraft](https://solidcraft.app). Every size is a named parameter, so a change to one number rebuilds the whole enclosure.

## Variants

The design has a configuration table with one row per lid variant. Activate a row to switch the model.

| Row | Board | Logo | Fan |
|---|---|---|---|
| `rpi5_ha`, `rpi5_ha_fan30`, `rpi5_ha_fan40` | Raspberry Pi 5 | Home Assistant | none, 30 mm, 40 mm |
| `rpi5_raspberry`, `rpi5_raspberry_fan30`, `rpi5_raspberry_fan40` | Raspberry Pi 5 | Raspberry Pi | none, 30 mm, 40 mm |
| `rpi5_plain`, `rpi5_plain_fan30`, `rpi5_plain_fan40` | Raspberry Pi 5 | none | none, 30 mm, 40 mm |
| `rpi4_*` | Raspberry Pi 4 | the same nine combinations | |

A row sets two parameters and suppresses features.

- `pi_ver` (4 or 5) moves the USB and Ethernet cut-outs and changes the board name inside the lid.
- `fan_s` (30 mm or 40 mm) sizes the fan clips.
- The features in the `Ventilator` folder are the fan clips. The `Logo_*` features cut the Home Assistant logo, and the `Logo_RPi` folder cuts the Raspberry Pi logo from `cad/logos/raspberry-pi.svg`.

## Useful parameters

| Parameter | Default | What it does |
|---|---|---|
| `wall` | 2.5 mm | Wall thickness. |
| `psu_air` | 2 mm | Extra air gap between the power supply and the back wall. |
| `kh_sp` | 50 mm | Distance between the two keyholes. They stay centred on the base. |
| `port_clr` | 0.5 mm | Clearance around the USB and Ethernet connectors. |
| `fan_t` | 10 mm | Fan thickness. The clips are this deep. |
| `fan_cx`, `fan_cy` | over the SoC | Fan centre. The clips sit between the top slots. |
| `clip_t`, `clip_lip` | 1.6 mm, 0.8 mm | Clip arm thickness and how far the hook reaches under the fan frame. |
| `ins25_d`, `ins3_d` | 3.4 mm, 4.2 mm | Holes for the M2.5 and M3 heat-set inserts. Tune them for your inserts and printer. |

## Exporting

`scripts/export_variants.py` exports the base and every lid row to `stl/` (laid on the print face) and `step/`. It runs SolidCraft headless, so the app does not need to be open.

```
python3 scripts/export_variants.py              # everything
python3 scripts/export_variants.py --only rpi5_ha_fan40
```
