"""Уровень 03 · эталон. Доля считается внутри каждого вида."""

from scenario import CASES, GOOD, Model, run_tool


def run() -> tuple[str, int]:
    model = Model()
    passed = [
        c for c in CASES
        if run_tool("check", {"case": c["id"]}) == GOOD
    ]
    overall = round(100 * len(passed) / len(CASES))

    # Среднее по разнородным случаям не означает ничего: считаем по видам.
    by_kind = {}
    for kind in {c["kind"] for c in CASES}:
        same = [c for c in CASES if c["kind"] == kind]
        hit = [c for c in same if c in passed]
        by_kind[kind] = round(100 * len(hit) / len(same))

    return model.report(overall, by_kind), 1
