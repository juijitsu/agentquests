"""Level 03 · novice. One number for the whole set."""

from scenario import CASES, GOOD, Model, run_tool


def run() -> tuple[str, int]:
    model = Model()
    passed = [
        c for c in CASES
        if run_tool("check", {"case": c["id"]}) == GOOD
    ]
    overall = round(100 * len(passed) / len(CASES))

    # TODO: ninety percent is an average over different things. Compute the
    #       share separately for every kind (the kind field) and pass the
    #       breakdown as the second argument: {kind: percent}.
    by_kind = {}

    return model.report(overall, by_kind), 1
