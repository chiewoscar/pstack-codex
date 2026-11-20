"""Exercise the shipped statechart CLI against passing and broken TLA+ models."""

from __future__ import annotations

import argparse
import hashlib
import os
from pathlib import Path
import subprocess
import tempfile
import urllib.request


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "plugins/pstack-codex/skills/statechart/scripts"
TLC_URL = "https://github.com/tlaplus/tlaplus/releases/download/v1.7.4/tla2tools.jar"
TLC_SHA256 = "936a262061c914694dfd669a543be24573c45d5aa0ff20a8b96b23d01e050e88"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--jar", type=Path, help="Use an existing TLC 1.7.4 JAR")
    args = parser.parse_args()
    with tempfile.TemporaryDirectory(prefix="pstack-statechart-") as scratch:
        folder = Path(scratch)
        jar = args.jar.resolve() if args.jar else folder / "tla2tools.jar"
        if not args.jar:
            urllib.request.urlretrieve(TLC_URL, jar)
        assert hashlib.sha256(jar.read_bytes()).hexdigest() == TLC_SHA256, "TLC checksum mismatch"
        env = {**os.environ, "TLA2TOOLS": str(jar)}
        for name, expected_exit, expected_rules in (
            ("Login", 0, ("## Rules that hold", "TypeOK, NoDeadlock")),
            ("CounterDeadlock", 1, ("## NotThree breaks", "## NoDeadlock breaks")),
        ):
            out = folder / name
            result = subprocess.run(
                ["node", "--disable-warning=ExperimentalWarning", str(SCRIPTS / "statechart.ts"),
                 str(SCRIPTS / "test/corpus" / name / f"{name}.tla"), "--out", str(out)],
                env=env, capture_output=True, text=True, encoding="utf-8", timeout=90,
            )
            assert result.returncode == expected_exit, result.stdout + result.stderr
            report = (out / "report.md").read_text(encoding="utf-8")
            for rule in expected_rules:
                assert rule in report, report
            chart = (out / "chart.mmd").read_text(encoding="utf-8")
            assert "stateDiagram-v2" in chart, chart
            print(f"OK: {name}, exit {expected_exit}, expected rules and statechart generated")


if __name__ == "__main__":
    main()
