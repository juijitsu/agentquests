"""Уровень 04 · профессионал.

Контракт:
    TOOLS — список из двух инструментов: check_border_status(crossing)
            и estimate_cost(weight_tons)
    run(question: str) -> tuple[str, int]

Агент обязан выбрать check_border_status на вопрос об ожидании на переходе,
не получив названия инструмента в самом вопросе.
"""

from scenario import Model, run_tool

TOOLS = []


def run(question: str) -> tuple[str, int]:
    raise NotImplementedError
