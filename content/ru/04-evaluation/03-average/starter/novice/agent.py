"""Уровень 03 · новичок. Одно число на весь набор."""

from scenario import CASES, GOOD, Model, run_tool


def run() -> tuple[str, int]:
    model = Model()
    passed = [
        c for c in CASES
        if run_tool("check", {"case": c["id"]}) == GOOD
    ]
    overall = round(100 * len(passed) / len(CASES))

    # TODO: девяносто процентов — среднее по разным вещам. Посчитайте долю
    #       отдельно по каждому виду (поле kind) и передайте разбивку
    #       вторым аргументом: {вид: процент}.
    by_kind = {}

    return model.report(overall, by_kind), 1
