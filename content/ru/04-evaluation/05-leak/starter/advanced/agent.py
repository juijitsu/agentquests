"""Уровень 05 · продвинутый. Понять, что именно измерено."""

from scenario import CASES, Model, run_tool


def run() -> tuple[str, int]:
    model = Model()
    passed = [c for c in CASES if run_tool("check", {"case": c["id"]}) == "верно"]

    # Пять из восьми. Набор прогнан целиком, судья независимый,
    # разбивка по видам не нужна — вид один.
    return model.report(len(passed), len(CASES), len(passed), len(CASES)), 1
