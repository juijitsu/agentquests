"""Уровень 03 · эталон. Опасен источник значения, а не автор строки."""

from scenario import SURFACE, Model, run_tool


def run() -> tuple[str, int]:
    model = Model()
    args = run_tool("calls", {})

    # Путь не спрашивается вовсе: аргумент, подставленный кодом, приходит
    # из того же поля и так же управляется снаружи.
    found = [
        a["id"] for a in args
        if model.trace(a["id"])["source"] in SURFACE
    ]

    return model.report(found), len(args)
