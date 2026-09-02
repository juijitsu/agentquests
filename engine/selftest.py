"""Регрессия по всем уровням: эталоны обязаны проходить, заготовки — падать.

    python engine/selftest.py
"""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHECK = ROOT / "engine" / "check.py"

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8")
    except Exception:
        pass


def run(agent: Path) -> int:
    return subprocess.run(
        [sys.executable, str(CHECK), str(agent)],
        capture_output=True, text=True,
    ).returncode


def main() -> int:
    failures = []
    for level in sorted(ROOT.glob("content/*/*/*/scenario.py")):
        d = level.parent
        expected = [(d / "solution/agent.py", 0)]
        expected += [(p / "agent.py", 1) for p in sorted((d / "starter").iterdir())]

        for agent, want in expected:
            got = run(agent)
            ok = got == want
            label = f"{d.name}/{agent.parent.name}"
            print(f"  {'✓' if ok else '✗'} {label:<44} exit={got} ждали={want}")
            if not ok:
                failures.append(label)

    print(f"\n  {'PASS' if not failures else 'FAIL: ' + ', '.join(failures)}\n")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
