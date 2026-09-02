"""Уровень 03 · новичок. История режется по хвосту, и начало теряется."""

from scenario import Model, TOOLS, run_tool

WINDOW = 8
MAX_STEPS = 12


def run(question: str) -> tuple[str, int]:
    model = Model()
    messages = [{"role": "user", "content": question}]

    def window(history):
        # TODO: хвост из последних сообщений влезает в окно, но условие задачи
        #       осталось в самом первом сообщении и до модели уже не доезжает.
        #       Сохраните нужное и подставьте его в начало окна.
        return history[-WINDOW:]

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
