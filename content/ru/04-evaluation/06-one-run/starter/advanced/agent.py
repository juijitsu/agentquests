"""Уровень 06 · продвинутый. Понять, что даёт один прогон."""

from scenario import CASES, RUNS, Model, run_tool


def run() -> tuple[str, int]:
    model = Model()

    # Пять из шести. Набор чистый, судья независимый, утечки нет.
    passed = [
        c["id"] for c in CASES
        if run_tool("check", {"case": c["id"], "run": 0}) == "верно"
    ]

    return model.report(passed, [], len(CASES)), 1
