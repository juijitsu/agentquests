"""Уровень 05 · новичок. Перекрытый перегон обрабатывается как обычный результат."""

from scenario import Model, TOOLS, run_tool

MAX_STEPS = 14


def run(question: str) -> tuple[str, int]:
    model = Model()
    messages = [{"role": "user", "content": question}]
    messages.append({"role": "plan", "content": model.make_plan(question)})

    for step in range(1, MAX_STEPS + 1):
        response = model.call(messages, tools=TOOLS)
        messages.append({"role": "assistant", "content": response.text})

        if response.tool_calls:
            for call in response.tool_calls:
                result = run_tool(call.name, call.arguments)
                messages.append({"role": "tool", "content": result})

                # TODO: этот результат означает, что план стал невыполним.
                #       Запросите новый план — model.make_plan(question, blocked=...) —
                #       и положите его в историю. Куда ехать, решит модель.

            continue

        return response.text, step

    return f"Не удалось получить ответ за {MAX_STEPS} шагов.", MAX_STEPS
