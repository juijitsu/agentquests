"""Уровень 03 · профессионал.

Контракт:
    run(question: str) -> tuple[str, int]   # ответ агента, число итераций

Модель проверит четыре участка маршрута, а затем посчитает стоимость по
весу груза. Вес назван один раз — в исходном вопросе.
"""

from scenario import Model, TOOLS, run_tool


def run(question: str) -> tuple[str, int]:
    raise NotImplementedError
