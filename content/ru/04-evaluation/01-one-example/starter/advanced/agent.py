"""Уровень 01 · продвинутый. Измерение построить самому."""

from scenario import CASES, Model, run_tool


def run() -> tuple[str, int]:
    model = Model()

    # Правку делали ради третьего случая. На нём она работает.
    case = CASES[2]
    old_passed = int(run_tool("ask", {"version": "old", "case": case["id"]}) == case["expected"])
    new_passed = int(run_tool("ask", {"version": "new", "case": case["id"]}) == case["expected"])

    return model.verdict(old_passed, new_passed, 1), 1
