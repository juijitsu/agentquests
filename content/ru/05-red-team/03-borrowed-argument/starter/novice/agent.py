"""Уровень 03 · новичок. Проверено то, что сочинила модель."""

from scenario import BY_MODEL, SURFACE, Model, run_tool


def run() -> tuple[str, int]:
    model = Model()
    args = run_tool("calls", {})

    # TODO: путь не важен. Значение, которое код скопировал из поля, пришло
    #       из того же поля и так же управляется снаружи — просто промпт оно
    #       не проходило. Оставьте аргументы по одному признаку:
    #       model.trace(a["id"])["source"] in SURFACE.
    found = []
    for a in args:
        t = model.trace(a["id"])
        if t["path"] == BY_MODEL and t["source"] in SURFACE:
            found.append(a["id"])

    return model.report(found), len(args)
