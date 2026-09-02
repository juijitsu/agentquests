"""Уровень 05 · эталон. Исчерпание лимита — результат, а не авария."""

from scenario import Model, TOOLS, run_tool

MAX_STEPS = 10


def run(question: str) -> tuple[str, int]:
    model = Model()
    messages = [{"role": "user", "content": question}]
    last_tool = None

    for step in range(1, MAX_STEPS + 1):
        response = model.call(messages, tools=TOOLS)
        messages.append({"role": "assistant", "content": response.text})

        if response.tool_calls:
            for call in response.tool_calls:
                last_tool = call.name
                result = run_tool(call.name, call.arguments)
                messages.append({"role": "tool", "content": result})
            continue

        return response.text, step

    return (
        f"Не удалось получить ответ за {MAX_STEPS} шагов. "
        f"Агент всё время вызывал {last_tool} и не продвигался. "
        f"Похоже, инструмент возвращает данные, с которыми модель не может закончить.",
        MAX_STEPS,
    )
