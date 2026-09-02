"""Финал · профессионал. Агент уходит заказчику в пятницу. Проходит не всё."""

from scenario import Model, run_tool

MAX_STEPS = 1

TOOLS = [
    {
        "name": "check_border_status",
        "description": "Получает данные.",
        "parameters": {"crossing": "string"},
    },
    {
        "name": "get_shipment_status",
        "description": "Возвращает статус груза по номеру и очередь на переходе.",
        "parameters": {"shipment_id": "string"},
    },
]


def run(question: str) -> tuple[str, int]:
    model = Model()
    messages = [{"role": "user", "content": question}]

    for step in range(1, MAX_STEPS + 1):
        response = model.call(messages, tools=TOOLS)
        messages.append({"role": "assistant", "content": response.text})

        if response.tool_calls:
            for call in response.tool_calls:
                try:
                    result = run_tool(call.name, call.arguments)
                except ValueError as exc:
                    return f"Не удалось: {exc}", step
                messages.append({"role": "tool", "content": result})
            continue

        return response.text, step

    return f"Не удалось получить ответ за {MAX_STEPS} шагов.", MAX_STEPS
