"""Level 05 · novice. Counts the whole set, prompt examples included."""

from scenario import CASES, Model, run_tool


def run() -> tuple[str, int]:
    model = Model()
    passed = [c for c in CASES if run_tool("check", {"case": c["id"]}) == "correct"]

    # TODO: four cases of the set sit word for word in the agent's prompt — on
    #       those it does not answer, it recalls. Ask run_tool("in_prompt", ...)
    #       for every case and compute a separate score over the unseen ones.
    return model.report(len(passed), len(CASES), len(passed), len(CASES)), 1
