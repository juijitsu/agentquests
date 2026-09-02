"""Уровень 07 · эталон. Очередь перечитывается на каждом круге."""

from scenario import EMPTY, Model, TOOLS, run_tool

MAX_STEPS = 12


def run() -> tuple[str, int]:
    model = Model()
    messages = [{"role": "user", "content": "Смена началась. Разбери, что пришло."}]
    step = 0

    # Очередь живая: пока мы разбираем одно, в ней появляется другое.
    while step < MAX_STEPS:
        pending = run_tool("pending", {})
        if pending == EMPTY:
            break
        event = pending.split(" | ")[0]
        step += 1
        response = model.call(messages, tools=TOOLS, event=event)
        for call in response.tool_calls:
            messages.append({"role": "tool", "content": run_tool(call.name, call.arguments)})

    return model.call(messages, tools=TOOLS).text, step
