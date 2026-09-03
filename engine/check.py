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

# \u0412\u0435\u0440\u0434\u0438\u043a\u0442 \u0447\u0438\u0442\u0430\u0435\u0442 \u0443\u0447\u0435\u043d\u0438\u043a, \u043f\u043e\u044d\u0442\u043e\u043c\u0443 \u043e\u043d \u0438\u0434\u0451\u0442 \u043d\u0430 \u044f\u0437\u044b\u043a\u0435 \u0443\u0440\u043e\u0432\u043d\u044f. \u042f\u0437\u044b\u043a \u043d\u0430\u0437\u044b\u0432\u0430\u0435\u0442 \u0441\u0430\u043c
# \u0441\u0446\u0435\u043d\u0430\u0440\u0438\u0439 \u2014 \u043e\u043d \u0436\u0435 \u0435\u0434\u0438\u043d\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u0439, \u043a\u0442\u043e \u043f\u0440\u043e \u0443\u0440\u043e\u0432\u0435\u043d\u044c \u0447\u0442\u043e-\u0442\u043e \u0437\u043d\u0430\u0435\u0442. \u0423\u043c\u043e\u043b\u0447\u0430\u043d\u0438\u0435
# \u0440\u0443\u0441\u0441\u043a\u043e\u0435: \u0442\u0430\u043a \u0443 \u0441\u0442\u0430\u0440\u044b\u0445 \u0443\u0440\u043e\u0432\u043d\u0435\u0439 \u043d\u0438\u0447\u0435\u0433\u043e \u043d\u0435 \u043c\u0435\u043d\u044f\u0435\u0442\u0441\u044f.
SAYS = {
    "ru": {
        "not_impl": "run() \u0435\u0449\u0451 \u043d\u0435 \u0440\u0435\u0430\u043b\u0438\u0437\u043e\u0432\u0430\u043d\u0430",
        "not_impl_why": "\u042d\u0442\u043e \u0437\u0430\u0433\u043e\u0442\u043e\u0432\u043a\u0430 \u0434\u043b\u044f \u0441\u043b\u043e\u0436\u043d\u043e\u0441\u0442\u0438 \u00ab\u043f\u0440\u043e\u0444\u0435\u0441\u0441\u0438\u043e\u043d\u0430\u043b\u00bb.",
        "not_impl_how": "\u0421\u043e\u0431\u0435\u0440\u0438\u0442\u0435 \u0440\u0435\u0448\u0435\u043d\u0438\u0435 \u0441\u0430\u043c\u0438 \u0438\u043b\u0438 \u0432\u043e\u0437\u044c\u043c\u0438\u0442\u0435 starter/advanced.",
        "crashed": "\u0440\u0435\u0448\u0435\u043d\u0438\u0435 \u0443\u043f\u0430\u043b\u043e: {}",
        "bad_type": "run() \u0432\u0435\u0440\u043d\u0443\u043b\u0430 {}, \u0430 \u043d\u0443\u0436\u0435\u043d \u043a\u043e\u0440\u0442\u0435\u0436 (\u043e\u0442\u0432\u0435\u0442, \u0447\u0438\u0441\u043b\u043e \u0438\u0442\u0435\u0440\u0430\u0446\u0438\u0439)",
        "bad_type_how": "\u041f\u043e\u0441\u043c\u043e\u0442\u0440\u0438\u0442\u0435 \u043a\u043e\u043d\u0442\u0440\u0430\u043a\u0442 run() \u0432 \u0448\u0430\u043f\u043a\u0435 \u0444\u0430\u0439\u043b\u0430.",
        "pass": "PASS  \u0441\u043b\u0435\u0434\u0443\u044e\u0449\u0438\u0439 \u0443\u0440\u043e\u0432\u0435\u043d\u044c \u043e\u0442\u043a\u0440\u044b\u0442",
        "fail": "FAIL",
    },
    "en": {
        "not_impl": "run() is not implemented yet",
        "not_impl_why": "This is the starter for the pro tier.",
        "not_impl_how": "Build the solution yourself or take starter/advanced.",
        "crashed": "the solution crashed: {}",
        "bad_type": "run() returned {}, but a tuple (answer, iterations) is required",
        "bad_type_how": "Check the run() contract at the top of the file.",
        "pass": "PASS  the next level is open",
        "fail": "FAIL",
    },
}

# \u0423\u0440\u043e\u0432\u0435\u043d\u044c \u043f\u0438\u0448\u0435\u0442\u0441\u044f \u043d\u0430 \u0442\u043e\u043c \u044f\u0437\u044b\u043a\u0435, \u043d\u0430 \u043a\u043e\u0442\u043e\u0440\u043e\u043c \u044d\u0442\u0443 \u0437\u0430\u0434\u0430\u0447\u0443 \u0440\u0435\u0448\u0430\u044e\u0442 \u0432 \u0436\u0438\u0437\u043d\u0438.
# \u041a\u043e\u043c\u0430\u043d\u0434\u0430 \u0434\u043b\u044f \u0443\u0447\u0435\u043d\u0438\u043a\u0430 \u043e\u0434\u043d\u0430 \u043d\u0430 \u0432\u0441\u0435 \u044f\u0437\u044b\u043a\u0438 \u2014 \u0440\u0430\u043d\u043d\u0435\u0440 \u0441\u0430\u043c \u0437\u043e\u0432\u0451\u0442 \u043d\u0443\u0436\u043d\u044b\u0439.
RUNNERS = {".ts": ["node", "check.mjs"]}

# \u042d\u0442\u0438 \u044f\u0437\u044b\u043a\u0438 \u0438\u0441\u043f\u043e\u043b\u043d\u044f\u044e\u0442\u0441\u044f \u0437\u0434\u0435\u0441\u044c \u0436\u0435: \u043f\u0438\u0442\u043e\u043d \u2014 \u043c\u043e\u0434\u0443\u043b\u0435\u043c, sql \u2014 \u0442\u0435\u043a\u0441\u0442\u043e\u043c \u0437\u0430\u043f\u0440\u043e\u0441\u0430
# \u0434\u043b\u044f \u0441\u0446\u0435\u043d\u0430\u0440\u0438\u044f (\u0434\u0432\u0438\u0436\u043e\u043a sqlite \u0443\u0436\u0435 \u0435\u0441\u0442\u044c \u0432 \u0441\u0442\u0430\u043d\u0434\u0430\u0440\u0442\u043d\u043e\u0439 \u0431\u0438\u0431\u043b\u0438\u043e\u0442\u0435\u043a\u0435).
IN_PROCESS = {".py", ".sql"}


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


def report(scenario, load_agent, where: str) -> tuple[list[str], int]:
    """Прогоняет уровень и складывает вердикт строками.

    Решение приходит функцией, а не готовым модулем: сломанный файл ученика
    должен падать здесь же и получать то же сообщение, что и всё остальное.

    Эту функцию зовут двое: командная строка ниже и браузерный запуск на
    сайте. Второй реализации вердикта в проекте нет и быть не должно.
    """
    says = SAYS.get(getattr(scenario, "LANG", "ru"), SAYS["ru"])
    out = [f"\n  {scenario.TITLE}", f"  {where}\n"]
    if getattr(scenario, "BRIEF", None):
        out += ["  " + line for line in scenario.BRIEF.strip().splitlines()]
        out.append("")

    try:
        result = scenario.play(load_agent())
    except NotImplementedError:
        out += [
            f"  {NO} {says['not_impl']}",
            f"\n  {says['fail']}  {says['not_impl_why']}",
            f"        {says['not_impl_how']}\n",
        ]
        return out, 1
    except Exception as exc:
        hint = scenario.explain(exc) if hasattr(scenario, "explain") else None
        out.append(f"  {NO} {says['crashed'].format(type(exc).__name__)}")
        if hint:
            out.append(f"\n  {says['fail']}  {hint}\n")
        else:
            out += ["", traceback.format_exc(), ""]
        return out, 1

    if not (isinstance(result, tuple) and len(result) == 2):
        out += [
            f"  {NO} {says['bad_type'].format(type(result).__name__)}",
            f"\n  {says['fail']}  {says['bad_type_how']}\n",
        ]
        return out, 1

    verdicts = scenario.verify(result)
    ok = all(passed for passed, _ in verdicts)
    out += [f"  {OK if passed else NO} {message}" for passed, message in verdicts]
    out.append("\n  " + (says["pass"] + "\n" if ok else says["fail"] + "\n"))
    return out, 0 if ok else 1


def main() -> int:
    if len(sys.argv) < 2:
        print("укажите путь к решению")
        return 2

    agent_path = Path(sys.argv[1]).resolve()
    if not agent_path.exists():
        print(f"FAIL  файла нет: {agent_path}")
        return 1

    if agent_path.suffix not in IN_PROCESS:
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

    def load_agent():
        if agent_path.suffix == ".sql":
            return agent_path.read_text(encoding="utf-8")
        return load(agent_path, "agent")

    lines, code = report(
        scenario, load_agent, f"{agent_path.name} · {agent_path.parent.name}"
    )
    for line in lines:
        print(line)
    return code


if __name__ == "__main__":
    sys.exit(main())
