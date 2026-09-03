"""Level 03 · advanced. Work out what one number hides."""

from scenario import CASES, GOOD, Model, run_tool


def run() -> tuple[str, int]:
    model = Model()
    passed = [
        c for c in CASES
        if run_tool("check", {"case": c["id"]}) == GOOD
    ]
    overall = round(100 * len(passed) / len(CASES))

    # Ninety percent. Eighteen out of twenty. A good result.
    by_kind = {}

    return model.report(overall, by_kind), 1
