"""Уровень 02 · новичок. Цикл выходит по техническому признаку, а не по цели."""

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

        # TODO: модель перестала просить инструмент — но задача решена только
        #       если мы добрались до GOAL. Если нет, скажите модели, где мы
        #       сейчас, и продолжите цикл.
        return response.text, step

    return f"Не удалось получить ответ за {MAX_STEPS} шагов.", MAX_STEPS
