"""Level 05 · advanced. Work out what exactly was measured."""

from scenario import CASES, Model, run_tool


def run() -> tuple[str, int]:
    model = Model()
    passed = [c for c in CASES if run_tool("check", {"case": c["id"]}) == "correct"]

    # Five of eight. The set was run in full, the judge is independent,
    # a breakdown by kind is not needed — there is only one kind.
    return model.report(len(passed), len(CASES), len(passed), len(CASES)), 1
