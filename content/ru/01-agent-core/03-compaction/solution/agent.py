"""Уровень 03 · эталон. В окно идут факты плюс свежий хвост."""

from scenario import Model, TOOLS, run_tool

WINDOW = 8
MAX_STEPS = 12


def run(question: str) -> tuple[str, int]:
    model = Model()
    messages = [{"role": "user", "content": question}]

    # Условие задачи нужно на последнем шаге так же, как на первом.
    facts = {"role": "user", "content": f"Условие задачи: {question}"}

    def window(history):
        return [facts] + history[-(WINDOW - 1):]

    for step in range(1, MAX_STEPS + 1):
        response = model.call(window(messages), tools=TOOLS)
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
