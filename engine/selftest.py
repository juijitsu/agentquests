"""Регрессия по всем уровням: эталоны обязаны проходить, заготовки — падать.

    python engine/selftest.py
"""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHECK = ROOT / "engine" / "check.py"
FIELDS = {"id", "track", "order", "title", "idea", "minutes", "needs_api_key", "unlocks"}
RUNNABLE = {".py", ".ts", ".sql"}


def agent_file(folder: Path) -> Path | None:
    found = sorted(p for p in folder.glob("agent.*") if p.suffix in RUNNABLE)
    return found[0] if found else None

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8")
    except Exception:
        pass


def run(agent: Path) -> int:
    # Вывод не читаем — нужен только код возврата. Без text=True subprocess
    # не пытается декодировать UTF-8 дочернего процесса локальной кодировкой.
    return subprocess.run(
        [sys.executable, str(CHECK), str(agent)],
        capture_output=True,
    ).returncode


def meta(level: Path) -> dict:
    # level.yaml — плоские «ключ: значение» по одному в строке, парсер не нужен.
    text = (level.parent / "level.yaml").read_text(encoding="utf-8")
    return dict(line.split(": ", 1) for line in text.splitlines() if ": " in line)


def chain(levels: list[Path]) -> list[str]:
    """Метаданные никто не читает, поэтому ломаются они молча.

    Проверяем два свойства: файл разбирается в полный набор полей и unlocks
    ведёт на существующий уровень. Последнему вести пока некуда.
    """
    failures, cards = [], {}
    for level in levels:
        card = meta(level)
        if set(card) == FIELDS:
            cards[level] = card
        else:
            print(f"  ✗ {level.parent.name:<44} level.yaml: полей {len(card)} из {len(FIELDS)}")
            failures.append(level.parent.name)

    ids = {card["id"] for card in cards.values()}
    for level, card in cards.items():
        if level is not levels[-1] and card["unlocks"] not in ids:
            print(f"  ✗ {level.parent.name:<44} unlocks → {card['unlocks']}: такого уровня нет")
            failures.append(level.parent.name)

    if not failures:
        print(f"  ✓ метаданные: цепочка цела, проверено уровней: {len(levels)}")
    return failures


def main() -> int:
    levels = sorted(
        p for p in ROOT.glob("content/*/*/*/scenario.*") if p.suffix in RUNNABLE
    )
    failures = chain(levels)
    for level in levels:
        d = level.parent
        expected = [(d / "solution", 0)]
        expected += [(p, 1) for p in sorted((d / "starter").iterdir())]

        for folder, want in expected:
            label = f"{d.name}/{folder.name}"
            agent = agent_file(folder)
            if agent is None:
                # Иначе пропавший файл даёт exit=1 и засчитывается как «корректно упало».
                print(f"  ✗ {label:<44} файла нет")
                failures.append(label)
                continue
            got = run(agent)
            ok = got == want
            print(f"  {'✓' if ok else '✗'} {label:<44} exit={got} ждали={want}")
            if not ok:
                failures.append(label)

    print(f"\n  {'PASS' if not failures else 'FAIL: ' + ', '.join(failures)}\n")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
