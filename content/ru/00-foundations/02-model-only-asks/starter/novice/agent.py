"""Уровень 02 · новичок. Цикл написан целиком, но две проверки стоят не в том порядке."""

from scenario import Model, TOOLS, run_tool

MAX_STEPS = 10


def run(question: str) -> tuple[str, int]:
    model = Model()
    messages = [{"role": "user", "content": question}]

    for step in range(1, MAX_STEPS + 1):
        response = model.call(messages, tools=TOOLS)
        messages.append({"role": "assistant", "content": response.text})

        # Модель прислала текст — значит всё готово?
        if response.text:
            return response.text, step

        for call in response.tool_calls:
            result = run_tool(call.name, call.arguments)
            messages.append({"role": "tool", "content": result})

    raise RecursionError("исчерпан лимит итераций")
