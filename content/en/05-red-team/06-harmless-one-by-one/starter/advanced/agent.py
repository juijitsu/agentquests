"""Level 06 · advanced. A snapshot before the batch and one after it."""

from scenario import BATCH_ID, Model, run_tool


def run() -> tuple[str, int]:
    model = Model()
    steps = run_tool("list_batch", {"batch": BATCH_ID})

    before = {s["id"]: model.check(s["id"])["allowed"] for s in steps}

    for s in steps:
        model.run_step(s["id"])

    after = {s["id"]: model.check(s["id"])["allowed"] for s in steps}

    # Whatever the batch turned from refused into permitted.
    found = [i for i in before if after[i] and not before[i]]
    return model.report(found), len(steps) * 3
