"""Уровень 01 · сложность: продвинутый

Цикл и выход из него готовы. Блок выполнения инструментов надо дописать.
"""

from engine.model import Model
from engine.tools import TOOLS, run_tool

MAX_STEPS = 10


def run(question: str) -> tuple[str, int]:
    """Возвращает (ответ агента, число потраченных итераций)."""
    model = Model()
    messages = [{"role": "user", "content": question}]

    for step in range(1, MAX_STEPS + 1):
        response = model.call(messages, tools=TOOLS)
        messages.append({"role": "assistant", "content": response.text})

        if not response.tool_calls:
            return response.text, step

        # Здесь: выполнить каждый запрошенный инструмент через run_tool
        # и вернуть результат модели через messages.

    raise RecursionError("исчерпан лимит итераций")
