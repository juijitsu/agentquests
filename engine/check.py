"""Раннер проверок. Общий для всех уровней и намеренно тупой.

    python engine/check.py <путь к agent.py>

Всю специфику уровня знает его собственный scenario.py: какая модель,
какие инструменты, что считать успехом. Раннер только запускает и печатает.
"""

import importlib.util
import subprocess
import sys
import traceback

sys.dont_write_bytecode = True  # не сорить __pycache__ в папках уроков
from pathlib import Path

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8")  # консоль Windows иначе падает на «✓»
    except Exception:
        pass

OK, NO = "\u2713", "\u2717"

# \u0423\u0440\u043e\u0432\u0435\u043d\u044c \u043f\u0438\u0448\u0435\u0442\u0441\u044f \u043d\u0430 \u0442\u043e\u043c \u044f\u0437\u044b\u043a\u0435, \u043d\u0430 \u043a\u043e\u0442\u043e\u0440\u043e\u043c \u044d\u0442\u0443 \u0437\u0430\u0434\u0430\u0447\u0443 \u0440\u0435\u0448\u0430\u044e\u0442 \u0432 \u0436\u0438\u0437\u043d\u0438.
# \u041a\u043e\u043c\u0430\u043d\u0434\u0430 \u0434\u043b\u044f \u0443\u0447\u0435\u043d\u0438\u043a\u0430 \u043e\u0434\u043d\u0430 \u043d\u0430 \u0432\u0441\u0435 \u044f\u0437\u044b\u043a\u0438 \u2014 \u0440\u0430\u043d\u043d\u0435\u0440 \u0441\u0430\u043c \u0437\u043e\u0432\u0451\u0442 \u043d\u0443\u0436\u043d\u044b\u0439.
RUNNERS = {".ts": ["node", "check.mjs"]}


def delegate(agent_path: Path) -> int:
    command = RUNNERS.get(agent_path.suffix)
    if command is None:
        print(f"FAIL  \u0434\u043b\u044f \u0444\u0430\u0439\u043b\u043e\u0432 {agent_path.suffix} \u0440\u0430\u043d\u043d\u0435\u0440\u0430 \u043d\u0435\u0442")
        return 2
    runner = Path(__file__).resolve().parent / command[-1]
    return subprocess.run([*command[:-1], str(runner), str(agent_path)]).returncode


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
        print("укажите путь к решению")
        return 2

    agent_path = Path(sys.argv[1]).resolve()
    if not agent_path.exists():
        print(f"FAIL  файла нет: {agent_path}")
        return 1

    if agent_path.suffix != ".py":
        return delegate(agent_path)

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

    if not (isinstance(result, tuple) and len(result) == 2):
        print(f"  {NO} run() вернула {type(result).__name__}, а нужен кортеж (ответ, число итераций)")
        print("\n  FAIL  Посмотрите контракт run() в шапке файла.\n")
        return 1

    verdicts = scenario.verify(result)
    ok = all(passed for passed, _ in verdicts)
    for passed, message in verdicts:
        print(f"  {OK if passed else NO} {message}")

    print("\n  " + ("PASS  следующий уровень открыт\n" if ok else "FAIL\n"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
