"""Уровень 05 · профессионал.

Контракт:
    run(question: str) -> tuple[str, int]

Доступно:
    model.make_plan(question, blocked=None) -> list[str]

Один из перегонов окажется перекрыт. Обход придумывает модель — но
только если её об этом попросить. Название объезда в вашем коде
появляться не должно: это превратит агента в скрипт.
"""

from scenario import Model, TOOLS, run_tool


def run(question: str) -> tuple[str, int]:
    raise NotImplementedError
