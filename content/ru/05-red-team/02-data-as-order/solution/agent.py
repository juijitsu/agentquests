"""Уровень 02 · эталон. Контрольный прогон и разница в действиях."""

from scenario import Model, run_tool


def run() -> tuple[str, int]:
    model = Model()
    notes = run_tool("notes", {})

    # Без контроля «агент выслал тариф» — ещё не находка: может, он
    # высылает его всегда.
    base = model.handle(None)

    # Сравниваются действия целиком, а не их количество: самая дорогая
    # инъекция меняет не шаг, а аргумент шага.
    found = [n["id"] for n in notes if model.handle(n["id"]) != base]

    return model.report(found), len(notes) + 1
