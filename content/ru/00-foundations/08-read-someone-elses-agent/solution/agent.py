"""Финал · эталон. Три дефекта устранены."""

from scenario import Model, run_tool

MAX_STEPS = 10  # дефект 1: одного шага не хватает даже на простой вызов

TOOLS = [
    {
        # дефект 2: по описанию «Получает данные» инструмент не узнать
        "name": "check_border_status",
        "description": (
            "Показывает очередь на погранпереходе. "
            "Допустимые значения crossing: Laredo, El Paso."
        ),
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
                    result = str(exc)  # дефект 3: ошибка уходила человеку, а не модели
                messages.append({"role": "tool", "content": result})
            continue

        return response.text, step

    return f"Не удалось получить ответ за {MAX_STEPS} шагов.", MAX_STEPS
