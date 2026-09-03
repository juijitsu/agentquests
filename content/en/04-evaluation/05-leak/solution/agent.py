"""Level 05 · reference. The score over unseen cases is computed separately."""

from scenario import CASES, Model, run_tool


def run() -> tuple[str, int]:
    model = Model()
    passed = [c for c in CASES if run_tool("check", {"case": c["id"]}) == "correct"]

    # A case sitting in the prompt measures memory, not work.
    clean = [c for c in CASES if not run_tool("in_prompt", {"case": c["id"]})]
    clean_passed = [c for c in clean if c in passed]

    return model.report(
        len(passed), len(CASES), len(clean_passed), len(clean)
    ), 1
