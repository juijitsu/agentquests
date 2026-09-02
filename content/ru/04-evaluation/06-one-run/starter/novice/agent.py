"""Уровень 06 · новичок. Меряет по одному прогону."""

from scenario import CASES, RUNS, Model, run_tool


def run() -> tuple[str, int]:
    model = Model()

    # TODO: два случая отвечают через раз, и на нулевом прогоне оба выпали
    #       удачно. Прогоните каждый случай RUNS раз, отделите устойчиво
    #       верные от неустойчивых и передайте оба списка в report.
    passed = [
        c["id"] for c in CASES
        if run_tool("check", {"case": c["id"], "run": 0}) == "верно"
    ]

    return model.report(passed, [], len(CASES)), 1
