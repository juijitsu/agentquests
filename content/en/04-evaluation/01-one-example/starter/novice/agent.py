"""Level 01 · novice. Checks the case the fix was made for."""

from scenario import CASES, Model, run_tool


def run() -> tuple[str, int]:
    model = Model()

    # TODO: one case measures nothing — least of all the one the fix was made
    #       for. Run both versions over all of CASES, count the matches against
    #       expected and hand the score to model.verdict.
    case = CASES[2]
    old_passed = int(run_tool("ask", {"version": "old", "case": case["id"]}) == case["expected"])
    new_passed = int(run_tool("ask", {"version": "new", "case": case["id"]}) == case["expected"])

    return model.verdict(old_passed, new_passed, 1), 1
