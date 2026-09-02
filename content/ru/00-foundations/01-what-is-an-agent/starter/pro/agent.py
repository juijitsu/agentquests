"""Уровень 01 · профессионал. Соберите цикл сами.

Контракт:
    run(question: str) -> tuple[str, int]   # ответ агента, число итераций

Доступно из scenario:
    Model().call(messages, tools) -> Response(text, tool_calls)
    TOOLS, run_tool(name, arguments) -> str
"""

from scenario import Model, TOOLS, run_tool


def run(question: str) -> tuple[str, int]:
    raise NotImplementedError
