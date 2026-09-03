"""Снимает настоящие прогоны уровней на этапе сборки.

    python scripts/capture-runs.py

Разбор на странице показывает не пересказ, а то, что движок выдаёт на самом
деле. Снимок делается при сборке, поэтому не расходится с уроком никогда и
ничего не стоит посетителю.
"""

import io
import json
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

SITE = Path(__file__).resolve().parent.parent
ROOT = SITE.parent
CHECK = ROOT / "engine" / "check.py"
OUT = SITE / "lib" / "runs.json"

RUNNABLE = {".py", ".sql"}


def agent_in(folder: Path):
    found = sorted(p for p in folder.glob("agent.*") if p.suffix in RUNNABLE)
    return found[0] if found else None


def run(agent: Path):
    done = subprocess.run(
        [sys.executable, str(CHECK), str(agent)], capture_output=True, cwd=ROOT
    )
    text = done.stdout.decode("utf-8", errors="replace")
    # Windows пишет CRLF; снимок должен быть одинаковым на любой машине.
    text = text.replace(chr(13) + chr(10), chr(10)).replace(chr(13), chr(10))
    text = text.strip(chr(10))
    return {"output": text, "code": done.returncode}


runs = {}
for scenario in sorted(ROOT.glob("content/*/*/*/scenario.py")):
    level = scenario.parent
    card = dict(
        line.split(": ", 1)
        for line in io.open(level / "level.yaml", encoding="utf-8").read().splitlines()
        if ": " in line
    )
    if not card.get("id"):
        continue
    # Один и тот же уровень на двух языках несёт один id, и без языка в ключе
    # снимки затирали бы друг друга: на английской странице показывался бы
    # русский прогон.
    key = f"{level.parents[1].name}/{card['id']}"

    entry = {}
    for tier, folder in (
        ("novice", level / "starter" / "novice"),
        ("solution", level / "solution"),
    ):
        agent = agent_in(folder)
        if agent is not None:
            entry[tier] = run(agent)
    if entry:
        runs[key] = entry
    print(f"  снят {key}")

OUT.parent.mkdir(parents=True, exist_ok=True)
io.open(OUT, "w", encoding="utf-8", newline="\n").write(
    json.dumps(runs, ensure_ascii=False, indent=1)
)
print(f"\nготово: {len(runs)} уровней → {OUT.relative_to(SITE)}")
