"""Level 02 · advanced. Work out why an improvement looks like a failure."""

from scenario import CASES, Model, run_tool


def run() -> tuple[str, int]:
    model = Model()
    scores = {}

    # The set is run in full, both versions, as it should be.
    # The metric demands the fix be rolled back.
    for version in ("old", "new"):
        scores[version] = sum(
            run_tool("ask", {"version": version, "case": c["id"]}) == c["expected"]
            for c in CASES
        )

    return model.verdict(scores["old"], scores["new"], len(CASES)), 1
