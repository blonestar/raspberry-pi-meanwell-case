#!/usr/bin/env python3
"""Fail when cad/SOLIDCRAFT.txt names a file format other than the design's.

The .sc file is a zip whose document.json carries "format": "solidcraft/N".
SolidCraft does not store its own version in the file, so the format is the
fact this script can check. A newer SolidCraft that changes the format makes
this check fail until SOLIDCRAFT.txt is updated.
"""
import json
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DESIGN = ROOT / "cad" / "RPi-PSU-enclosure.sc"
INFO = ROOT / "cad" / "SOLIDCRAFT.txt"


def main():
    with zipfile.ZipFile(DESIGN) as z:
        actual = json.loads(z.read("document.json"))["format"]
    match = re.search(r"^File format: (\S+)$", INFO.read_text(), re.MULTILINE)
    if not match:
        sys.exit(f"{INFO.name} has no 'File format: ...' line")
    stated = match.group(1)
    if stated != actual:
        sys.exit(
            f"{DESIGN.name} is {actual}, but {INFO.name} says {stated}. "
            f"Update 'Made with SolidCraft ...' and 'File format: {actual}' in {INFO.relative_to(ROOT)}."
        )
    print(f"{INFO.name} matches {DESIGN.name}: {actual}")


if __name__ == "__main__":
    main()
