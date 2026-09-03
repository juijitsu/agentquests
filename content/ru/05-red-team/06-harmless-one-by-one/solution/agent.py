"""Уровень 06 · эталон. Приговор берётся в момент запуска, а не после."""

from scenario import BATCH_ID, Model, run_tool


def run() -> tuple[str, int]:
    model = Model()
    steps = run_tool("list_batch", {"batch": BATCH_ID})

    # Поодиночке: запись нетронута, check ничего не меняет.
    alone = {s["id"]: model.check(s["id"])["allowed"] for s in steps}

    # В цепочке: спрашиваем прямо перед тем, как отдать шаг, — между
    # записями предыдущих шагов и его собственной.
    inside = {}
    for s in steps:
        inside[s["id"]] = model.check(s["id"])["allowed"]
        model.run_step(s["id"])

    found = [i for i in alone if inside[i] and not alone[i]]
    return model.report(found), len(steps) * 3
