"""Level 01 · reference. The set is measured, not your favourite example."""

from scenario import CASES, Model, run_tool


def run() -> tuple[str, int]:
    model = Model()

    # Both versions go through the same set in full — otherwise there is
    # nothing to compare.
    scores = {}
    for version in ("old", "new"):
        scores[version] = sum(
            run_tool("ask", {"version": version, "case": c["id"]}) == c["expected"]
            for c in CASES
        )

    return model.verdict(scores["old"], scores["new"], len(CASES)), 1
