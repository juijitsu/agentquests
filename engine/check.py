"""Раннер проверок. Общий для всех уровней и намеренно тупой.

    python engine/check.py <путь к agent.py>

Всю специфику уровня знает его собственный scenario.py: какая модель,
какие инструменты, что считать успехом. Раннер только запускает и печатает.
"""

import importlib.util
import sys
import traceback
from pathlib import Path

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8")  # консоль Windows иначе падает на «✓»
    except Exception:
        pass

OK, NO = "\u2713", "\u2717"


def find_level(start: Path) -> Path | None:
    for parent in [start, *start.parents]:
        if (parent / "scenario.py").exists():
            return parent
    return None


def find_root(start: Path) -> Path:
    for parent in [start, *start.parents]:
        if (parent / "engine" / "kit.py").exists():
            return parent
    return Path.cwd()


def load(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def main() -> int:
    if len(sys.argv) < 2:
        print("укажите путь к agent.py")
        return 2

    agent_path = Path(sys.argv[1]).resolve()
    if not agent_path.exists():
        print(f"FAIL  файла нет: {agent_path}")
        return 1

    level_dir = find_level(agent_path)
    if level_dir is None:
        print(f"FAIL  рядом с решением не найден scenario.py")
        return 2

    # Пути настраивает раннер: в файле ученика не должно быть плумбинга.
    for p in (str(find_root(agent_path)), str(level_dir)):
        if p not in sys.path:
            sys.path.insert(0, p)

    scenario = load(level_dir / "scenario.py", "scenario")

    print(f"\n  {scenario.TITLE}")
    print(f"  {agent_path.name} \u00b7 {agent_path.parent.name}\n")

    if getattr(scenario, "BRIEF", None):
        for line in scenario.BRIEF.strip().splitlines():
            print("  " + line)
        print()

    try:
        agent = load(agent_path, "agent")
        result = scenario.play(agent)
    except NotImplementedError:
        print(f"  {NO} run() ещё не реализована")
        print("\n  FAIL  Это заготовка для сложности «профессионал».")
        print("        Соберите решение сами или возьмите starter/advanced.\n")
        return 1
    except Exception as exc:
        hint = scenario.explain(exc) if hasattr(scenario, "explain") else None
        print(f"  {NO} решение упало: {type(exc).__name__}")
        if hint:
            print(f"\n  FAIL  {hint}\n")
        else:
            print()
            traceback.print_exc()
            print()
        return 1

    verdicts = scenario.verify(result)
    ok = all(passed for passed, _ in verdicts)
    for passed, message in verdicts:
        print(f"  {OK if passed else NO} {message}")

    print("\n  " + ("PASS  следующий уровень открыт\n" if ok else "FAIL\n"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
