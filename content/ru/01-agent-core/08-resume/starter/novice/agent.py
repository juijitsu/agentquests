"""Уровень 08 · новичок. Прогресс живёт в messages и умирает вместе с ними."""

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
                # TODO: messages не переживут перезапуск, а DONE переживёт.
                #       Отметьте здесь забронированный перегон — тогда после
                #       краха модель увидит, что уже сделано, и не повторит.

            continue

        return response.text, step

    return f"Не удалось собрать рейс за {MAX_STEPS} шагов.", MAX_STEPS
