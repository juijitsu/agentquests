"""Уровень 02 · профессионал.

Контракт:
    run(question: str) -> tuple[str, int]

Маршрут заранее неизвестен. Инструмент next_hop(city) отдаёт один
следующий пункт. Модель после каждого хопа отчитывается текстом и
перестаёт просить инструменты — но задача решена только по достижении
Newark. Условие завершения ваше.
"""

from scenario import Model, TOOLS, run_tool


def run(question: str) -> tuple[str, int]:
    raise NotImplementedError
