"""Уровень 06 · продвинутый. Снимок до партии и снимок после неё."""

from scenario import BATCH_ID, Model, run_tool


def run() -> tuple[str, int]:
    model = Model()
    steps = run_tool("list_batch", {"batch": BATCH_ID})

    before = {s["id"]: model.check(s["id"])["allowed"] for s in steps}

    for s in steps:
        model.run_step(s["id"])

    after = {s["id"]: model.check(s["id"])["allowed"] for s in steps}

    # Что партия превратила из отказа в разрешение.
    found = [i for i in before if after[i] and not before[i]]
    return model.report(found), len(steps) * 3
