"""Уровень 02 · эталон. Цикл продолжается, пока не достигнута цель."""

from scenario import Model, TOOLS, run_tool

GOAL = "Newark"
MAX_STEPS = 12


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
                    result = str(exc)
                messages.append({"role": "tool", "content": result})
            continue

        if GOAL in (response.text or ""):
            return response.text, step

        # Шаг выполнен, задача — нет. Сообщаем модели новую позицию.
        messages.append({"role": "user", "content": f"{response.text}. Куда дальше?"})

    return f"Не удалось получить ответ за {MAX_STEPS} шагов.", MAX_STEPS
