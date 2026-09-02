"""Уровень 06 · новичок. Результат отдаётся без ревизии."""

from scenario import Model, TOOLS, run_tool

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

        # TODO: все шаги прошли успешно, но это ещё не значит, что результат
        #       верен. Перед возвратом покажите его модели — model.review(
        #       response.text, question) — и отдайте то, что она вернёт.
        return response.text, step

    return f"Не удалось получить ответ за {MAX_STEPS} шагов.", MAX_STEPS
