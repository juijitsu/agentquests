"""Level 02 · novice. Compares strings character by character."""

from scenario import CASES, Model, run_tool


def run() -> tuple[str, int]:
    model = Model()
    scores = {}

    # TODO: "two dollars ninety cents" is 2.90, but character by character they
    #       are not equal. Ask model.same_answer(expected, got) instead of
    #       comparing strings.
    for version in ("old", "new"):
        scores[version] = sum(
            run_tool("ask", {"version": version, "case": c["id"]}) == c["expected"]
            for c in CASES
        )

    return model.verdict(scores["old"], scores["new"], len(CASES)), 1
