#!/usr/bin/env python3
"""Export the base and every lid variant to stl/ and step/.

Runs SolidCraft headless (`solidcraft-cli run`) on cad/RPi-PSU-enclosure.sc.
Each lid variant is a row of the design's configuration table.

usage: scripts/export_variants.py [--only ROW ...] [--dry-run]

Set SOLIDCRAFT_CLI to use a CLI other than the one on PATH. It must read the
design's file format, so use the CLI that ships with the app that saved it.
"""
import argparse
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DESIGN = ROOT / "cad" / "RPi-PSU-enclosure.sc"
CLI = os.environ.get("SOLIDCRAFT_CLI", "solidcraft-cli")

LID_ROWS = [
    f"rpi{pi}_{logo}{fan}"
    for pi in (5, 4)
    for logo in ("ha", "raspberry", "plain")
    for fan in ("", "_fan30", "_fan40")
]


PRINT_FACE = {
    "Dno": [40, 50, 0],
    "Kuciste": [130, 95, 37.5],
}


def export_steps(body, stem):
    return [
        {"command": "body.print_face", "params": {"body": body, "point": PRINT_FACE[body]}},
        {"command": "file.export", "params": {
            "path": str(ROOT / "stl" / f"{stem}.stl"), "bodies": [body],
            "quality": "fine", "lay_on_print_faces": True}},
        {"command": "file.export", "params": {
            "path": str(ROOT / "step" / f"{stem}.step"), "bodies": [body]}},
    ]


def build_script(rows):
    steps = [{"command": "config.activate", "params": {"row": rows[0]}}]
    steps += export_steps("Dno", "base")
    for row in rows:
        steps.append({"command": "config.activate", "params": {"row": row}})
        steps += export_steps("Kuciste", f"lid_{row}")
    steps.append({"command": "config.activate", "params": {"row": "rpi5_ha_fan40"}})
    return steps


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", nargs="+", choices=LID_ROWS, help="lid rows to export")
    ap.add_argument("--dry-run", action="store_true", help="print the script, run nothing")
    args = ap.parse_args()

    steps = build_script(args.only or LID_ROWS)
    if args.dry_run:
        json.dump(steps, sys.stdout, indent=1)
        return
    (ROOT / "stl").mkdir(exist_ok=True)
    (ROOT / "step").mkdir(exist_ok=True)
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
        json.dump({"commands": steps}, f)
    subprocess.run([CLI, "run", f.name, "--in", str(DESIGN), "--quiet"], check=True)
    Path(f.name).unlink()


if __name__ == "__main__":
    main()
