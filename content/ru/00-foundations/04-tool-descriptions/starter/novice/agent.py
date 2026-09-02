"""Уровень 04 · новичок. Цикл рабочий. Испорчено одно описание."""

from scenario import Model, run_tool

TOOLS = [
    {
        "name": "check_border_status",
        # TODO: описание потеряли при переносе. Модель по нему инструмент
        #       не узнаёт и выбирает соседний. Напишите нормальное.
        "description": "Получает данные.",
        "parameters": {"crossing": "string"},
    },
    {
        "name": "estimate_cost",
        "description": "Считает стоимость перевозки по весу груза с учётом ожидания на переходах.",
        "parameters": {"weight_tons": "number"},
    },
]


MAX_STEPS = 10


def run(question: str) -> tuple[str, int]:
    model = Model()
    messages = [{"role": "user", "content": question}]

    for step in range(1, MAX_STEPS + 1):
        response = model.call(messages, tools=TOOLS)
        messages.append({"role": "assistant", "content": response.text})

        if response.tool_calls:
            for call in response.tool_calls:
                result = run_tool(call.name, call.arguments)
                messages.append({"role": "tool", "content": result})
            continue

        return response.text, step

    raise RecursionError("исчерпан лимит итераций")
