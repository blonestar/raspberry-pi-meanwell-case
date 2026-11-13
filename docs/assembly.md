# Assembly

> **Warning.** This enclosure carries mains voltage. Only build it if you are qualified to work with mains wiring. Unplug the cable before you open the box.

You need the parts in the [bill of materials](BOM.md), a soldering iron for the heat-set inserts, and a 2 mm hex key.

1. Press in the heat-set inserts. See [Printing](printing.md#heat-set-inserts).
2. Set the power supply output to 5.1 V with its trimmer before anything is connected to it.
3. Screw the power supply to the base with 2 × M3 × 8 from below. It sits on two 2.5 mm pads.
4. Screw the Raspberry Pi to the four standoffs with 4 × M2.5 × 8. The USB and Ethernet ports face the front edge of the base.
5. Lay the mains cable in the strain-relief channel at the front right corner and connect it to the L and N terminals of the power supply.
6. Connect the 5 V output of the power supply to the Pi. TODO: describe the power path.
7. With a fan lid, press the fan into the clips on the inside of the lid, label side down, until both hooks click over the frame. Connect the fan. See the fan row in the [bill of materials](BOM.md).
8. Put the lid on and fasten it with 4 × M3 × 8 from below.

## Wall mount

Drill two holes 50 mm apart. Leave a gap under each screw head a little larger than 3 mm, the thickness of the base. Pass the heads through the round part of the keyholes and let the box slide down onto them.

- Holes on a vertical line: the box hangs with the ports at the bottom and the back edge at the top.
- Holes on a horizontal line: the box hangs with the power supply at the top. The heads slide into the side arms of the keyholes, which run toward the power supply.

## Raspberry Pi 5 on GPIO power

A Raspberry Pi 5 powered through its GPIO 5 V pins cannot ask the supply what current it delivers, so by default it limits the USB ports to 600 mA. The RS-25-5 delivers 5 A. To allow the full 1.6 A on the USB ports, add this line to `/boot/firmware/config.txt`:

```
usb_max_current_enable=1
```
