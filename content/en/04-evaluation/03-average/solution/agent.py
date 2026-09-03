"""Level 03 · reference. The share is computed within each kind."""

from scenario import CASES, GOOD, Model, run_tool


def run() -> tuple[str, int]:
    model = Model()
    passed = [
        c for c in CASES
        if run_tool("check", {"case": c["id"]}) == GOOD
    ]
    overall = round(100 * len(passed) / len(CASES))

    # An average over incomparable cases means nothing: count by kind.
    by_kind = {}
    for kind in {c["kind"] for c in CASES}:
        same = [c for c in CASES if c["kind"] == kind]
        hit = [c for c in same if c in passed]
        by_kind[kind] = round(100 * len(hit) / len(same))

    return model.report(overall, by_kind), 1
