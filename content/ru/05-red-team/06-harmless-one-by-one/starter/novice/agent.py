"""Уровень 06 · новичок. Снимок до партии и снимок после неё."""

from scenario import BATCH_ID, Model, run_tool


def run() -> tuple[str, int]:
    model = Model()
    steps = run_tool("list_batch", {"batch": BATCH_ID})

    before = {s["id"]: model.check(s["id"])["allowed"] for s in steps}

    for s in steps:
        model.run_step(s["id"])

    # TODO: after — это запись уже после последнего шага, который вернул
    #       умолчания на место. Проверка срабатывает в момент запуска шага,
    #       а не в конце партии. Берите приговор внутри цикла, прямо перед
    #       model.run_step(s["id"]).
    after = {s["id"]: model.check(s["id"])["allowed"] for s in steps}

    found = [i for i in before if after[i] and not before[i]]
    return model.report(found), len(steps) * 3
