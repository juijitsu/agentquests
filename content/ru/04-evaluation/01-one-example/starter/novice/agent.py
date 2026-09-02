"""Уровень 01 · новичок. Проверяет тот случай, ради которого правили."""

from scenario import CASES, Model, run_tool


def run() -> tuple[str, int]:
    model = Model()

    # TODO: один случай ничего не измеряет — тем более тот, ради которого
    #       правку и делали. Прогоните обе версии по всем CASES, посчитайте
    #       совпадения с expected и отдайте счёт в model.verdict.
    case = CASES[2]
    old_passed = int(run_tool("ask", {"version": "old", "case": case["id"]}) == case["expected"])
    new_passed = int(run_tool("ask", {"version": "new", "case": case["id"]}) == case["expected"])

    return model.verdict(old_passed, new_passed, 1), 1
