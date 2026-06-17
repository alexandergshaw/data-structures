#!/usr/bin/env python3
"""Run each assignment's test suite and write ``lib/test-status.json``.

The Dashboard imports that file to decide which cards are unlocked: a card
unlocks only when its unit has tests *and* every one of them passes. There is no
manual flag any more — passing tests are the single source of truth.

This script runs during the Vercel build (see ``scripts/vercel-build.sh``, which
runs it just before ``next build``), so every deployment reflects the latest test
results. You can also run it locally to refresh the committed baseline:

    python scripts/generate_test_status.py

It is idempotent: if the per-unit results are unchanged it leaves the existing
file untouched, avoiding a needless diff.
"""

from __future__ import annotations

import datetime as dt
import json
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ASSIGNMENTS_DIR = ROOT / "assignments"
OUTPUT = ROOT / "lib" / "test-status.json"


def run_unit(folder: Path) -> dict:
    """Run pytest for a single assignment folder and summarize the result."""
    with tempfile.TemporaryDirectory() as tmp:
        xml_path = Path(tmp) / "report.xml"
        subprocess.run(
            [
                sys.executable,
                "-m",
                "pytest",
                str(folder),
                "--junit-xml",
                str(xml_path),
                "-q",
            ],
            cwd=ROOT,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False,
        )

        if not xml_path.exists():
            # pytest crashed before writing a report (e.g. a usage error).
            return {"passed": False, "tests": 0, "failures": 0, "errors": 0}

        suite = ET.parse(xml_path).getroot().find("testsuite")
        if suite is None:
            return {"passed": False, "tests": 0, "failures": 0, "errors": 0}

        tests = int(suite.get("tests", 0))
        failures = int(suite.get("failures", 0))
        errors = int(suite.get("errors", 0))
        return {
            "passed": tests > 0 and failures == 0 and errors == 0,
            "tests": tests,
            "failures": failures,
            "errors": errors,
        }


def collect_units() -> dict:
    folders = sorted(
        p
        for p in ASSIGNMENTS_DIR.iterdir()
        if p.is_dir() and (p / "test_assignment.py").exists()
    )

    units: dict[str, dict] = {}
    for folder in folders:
        result = run_unit(folder)
        units[folder.name] = result
        flag = "PASS" if result["passed"] else "lock"
        print(
            f"[{flag}] {folder.name}: {result['tests']} tests, "
            f"{result['failures']} failures, {result['errors']} errors"
        )
    return units


def main() -> int:
    units = collect_units()

    existing_units = {}
    if OUTPUT.exists():
        try:
            existing_units = json.loads(OUTPUT.read_text(encoding="utf-8")).get(
                "units", {}
            )
        except (json.JSONDecodeError, OSError):
            existing_units = {}

    unlocked = sum(1 for u in units.values() if u["passed"])

    if existing_units == units:
        print(f"\nNo change ({unlocked}/{len(units)} unlocked); leaving file as-is.")
        return 0

    payload = {
        "generatedAt": dt.datetime.now(dt.timezone.utc)
        .replace(microsecond=0)
        .isoformat(),
        "units": units,
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"\nWrote {OUTPUT.relative_to(ROOT)} ({unlocked}/{len(units)} unlocked).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
