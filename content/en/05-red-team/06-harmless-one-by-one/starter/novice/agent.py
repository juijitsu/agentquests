"""Level 06 · novice. A snapshot before the batch and one after it."""

from scenario import BATCH_ID, Model, run_tool


def run() -> tuple[str, int]:
    model = Model()
    steps = run_tool("list_batch", {"batch": BATCH_ID})

    before = {s["id"]: model.check(s["id"])["allowed"] for s in steps}

    for s in steps:
        model.run_step(s["id"])

    # TODO: after is the record once the last step has put the defaults back.
    #       A guard fires at the moment its step runs, not when the batch
    #       finishes. Take the verdict inside the loop, right before
    #       model.run_step(s["id"]).
    after = {s["id"]: model.check(s["id"])["allowed"] for s in steps}

    found = [i for i in before if after[i] and not before[i]]
    return model.report(found), len(steps) * 3
