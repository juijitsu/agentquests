"""Level 02 · reference. Checks answers, not their spelling."""

from scenario import CASES, Model, run_tool


def run() -> tuple[str, int]:
    model = Model()
    scores = {}

    # Correctness is a property of the answer, not of the string it is written in.
    for version in ("old", "new"):
        scores[version] = sum(
            model.same_answer(
                c["expected"], run_tool("ask", {"version": version, "case": c["id"]})
            )
            for c in CASES
        )

    return model.verdict(scores["old"], scores["new"], len(CASES)), 1
