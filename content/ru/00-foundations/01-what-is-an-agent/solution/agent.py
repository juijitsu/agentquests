"""Уровень 01 · эталонное решение.

Отличается от starter/novice ровно одной строкой — той, что замыкает цепочку:
результат инструмента возвращается модели сообщением с ролью "tool".
"""

from engine.model import Model
from engine.tools import TOOLS, run_tool

MAX_STEPS = 10


def run(question: str) -> tuple[str, int]:
    model = Model()
    messages = [{"role": "user", "content": question}]

    for step in range(1, MAX_STEPS + 1):
        response = model.call(messages, tools=TOOLS)
        messages.append({"role": "assistant", "content": response.text})

        if not response.tool_calls:
            return response.text, step

        for call in response.tool_calls:
            result = run_tool(call.name, call.arguments)
            messages.append({"role": "tool", "content": result})

    raise RecursionError("исчерпан лимит итераций")
