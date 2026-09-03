"""Level 06 · reference. The verdict is taken as the step runs, not after."""

from scenario import BATCH_ID, Model, run_tool


def run() -> tuple[str, int]:
    model = Model()
    steps = run_tool("list_batch", {"batch": BATCH_ID})

    # On their own: the record is untouched, and check changes nothing.
    alone = {s["id"]: model.check(s["id"])["allowed"] for s in steps}

    # In the chain: ask right before handing the step over, so the question
    # sits between the earlier steps' writes and this step's own.
    inside = {}
    for s in steps:
        inside[s["id"]] = model.check(s["id"])["allowed"]
        model.run_step(s["id"])

    found = [i for i in alone if inside[i] and not alone[i]]
    return model.report(found), len(steps) * 3
