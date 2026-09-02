"""Уровень 01 · сложность: профессионал

Соберите цикл сами.

Контракт:
    run(question: str) -> tuple[str, int]
        возвращает финальный ответ агента и число потраченных итераций.

Доступно:
    engine.model.Model().call(messages, tools) -> Response(text, tool_calls)
    engine.tools.TOOLS
    engine.tools.run_tool(name, arguments) -> str

Условие сдачи: ответ содержит статус груза, итераций не больше трёх,
процесс не падает. Способ ваш.
"""

from engine.model import Model
from engine.tools import TOOLS, run_tool


def run(question: str) -> tuple[str, int]:
    raise NotImplementedError
