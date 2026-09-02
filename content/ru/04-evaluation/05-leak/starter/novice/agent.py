"""Уровень 05 · новичок. Считает по всему набору, включая примеры из промпта."""

from scenario import CASES, Model, run_tool


def run() -> tuple[str, int]:
    model = Model()
    passed = [c for c in CASES if run_tool("check", {"case": c["id"]}) == "верно"]

    # TODO: четыре случая набора дословно лежат в промпте агента — на них он
    #       не отвечает, а вспоминает. Спросите run_tool("in_prompt", ...)
    #       по каждому случаю и посчитайте отдельный счёт по незнакомым.
    return model.report(len(passed), len(CASES), len(passed), len(CASES)), 1
