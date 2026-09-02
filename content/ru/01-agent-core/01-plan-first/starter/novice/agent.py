"""Уровень 01 · новичок. Цикл рабочий, но агент ныряет в вызовы без плана."""

from scenario import Model, TOOLS, run_tool

MAX_STEPS = 10


def run(question: str) -> tuple[str, int]:
    model = Model()
    messages = [{"role": "user", "content": question}]

    # TODO: сначала спросите у модели план — model.make_plan(question) —
    #       и положите его в messages сообщением с ролью "plan".
    #       Без плана модель видит только ближайший шаг.

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
