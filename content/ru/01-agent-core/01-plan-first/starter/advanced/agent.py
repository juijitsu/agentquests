"""Уровень 01 · продвинутый. Отделите планирование от выполнения."""

from scenario import Model, TOOLS, run_tool

MAX_STEPS = 10


def run(question: str) -> tuple[str, int]:
    """Возвращает (ответ агента, число потраченных итераций).

    Доступно: model.make_plan(question) -> list[str]
    Модель следует плану, только если видит его в истории.
    """
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
                    result = str(exc)
                messages.append({"role": "tool", "content": result})
            continue

        return response.text, step

    return f"Не удалось получить ответ за {MAX_STEPS} шагов.", MAX_STEPS
