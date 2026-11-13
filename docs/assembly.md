# Assembly

> **Warning.** This enclosure carries mains voltage. Only build it if you are qualified to work with mains wiring. Unplug the cable before you open the box.

You need the parts in the [bill of materials](BOM.md), a soldering iron for the heat-set inserts, and a 2 mm hex key.

1. Press in the heat-set inserts. See [Printing](printing.md#heat-set-inserts).
2. Set the power supply output to 5.1 V with its trimmer before anything is connected to it.
3. Screw the power supply to the base with 2 × M3 × 8 from below. It sits on two 2.5 mm pads.
4. Screw the Raspberry Pi to the four standoffs with 4 × M2.5 × 6. The USB and Ethernet ports face the front edge of the base.
5. Lay the mains cable in the strain-relief channel at the front right corner and connect it to the L and N terminals of the power supply.

   The 2-core cable has no protective earth, so the FG (earth) terminal of the power supply stays unconnected. Mean Well specifies the RS-25 with FG connected to earth. The plastic enclosure covers every live part, but the build is not earthed. The strain relief fits only the flat 2-core cable, so an earthed build needs a different cable entry.
6. Connect the power supply to the GPIO header, which faces the power supply. Pin 1 is at the end of the header far from the USB and Ethernet ports. The even pins (2, 4, 6 … 14) are on the outer row, along the board edge.
   - +V to pin 2 and pin 4 (5 V), with one wire each.
   - −V to pin 6 and pin 14 (GND), with one wire each.

   Check the polarity twice. GPIO power bypasses the protection on the USB-C input, so a reversed or over-voltage supply can destroy the board.
7. With a fan lid, press the fan into the clips on the inside of the lid, label side down, until both hooks click over the frame. Connect the fan to the power supply's +V and −V terminals, or on a Pi 5 to the fan connector. See the fan row in the [bill of materials](BOM.md).
8. Put the lid on and fasten it with 4 × M3 × 8 from below.

## Wall mount

Drill two holes 50 mm apart. Leave a gap under each screw head a little larger than 3 mm, the thickness of the base. Pass the heads through the round part of the keyholes and let the box slide down onto them.

- Holes on a vertical line: the box hangs with the ports at the bottom and the back edge at the top.
- Holes on a horizontal line: the box hangs with the power supply at the top. The heads slide into the side arms of the keyholes, which run toward the power supply.

## Raspberry Pi 5 on GPIO power

A Raspberry Pi 5 powered through its GPIO 5 V pins cannot ask the supply what current it delivers. By default it then assumes a weak supply, warns at boot and limits the USB ports to 600 mA. The RS-25-5 delivers 5 A, so tell the bootloader:

```
sudo rpi-eeprom-config --edit
```

Add this line, save, and reboot:

```
PSU_MAX_CURRENT=5000
```

A Raspberry Pi 4 needs no setting.
