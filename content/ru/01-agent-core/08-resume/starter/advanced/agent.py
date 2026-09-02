"""Уровень 08 · продвинутый. Что должно пережить процесс — решить самому."""

from scenario import DONE, Model, TOOLS, run_tool

MAX_STEPS = 10


def run() -> tuple[str, int]:
    model = Model()
    messages = [{"role": "user", "content": "Собери рейс Laredo → Newark."}]

    for step in range(1, MAX_STEPS + 1):
        response = model.call(messages, tools=TOOLS)
        messages.append({"role": "assistant", "content": response.text})

        if response.tool_calls:
            for call in response.tool_calls:
                result = run_tool(call.name, call.arguments)
                messages.append({"role": "tool", "content": result})
                # Всё, что агент знает о своей работе, лежит в messages.
                # Что из этого останется, когда процесс убьют?

            continue

        return response.text, step

    return f"Не удалось собрать рейс за {MAX_STEPS} шагов.", MAX_STEPS
