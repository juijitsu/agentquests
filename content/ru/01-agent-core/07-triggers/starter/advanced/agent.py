"""Уровень 07 · продвинутый. Условие остановки определить самому."""

from scenario import EMPTY, Model, TOOLS, run_tool

MAX_STEPS = 12


def run() -> tuple[str, int]:
    model = Model()
    messages = [{"role": "user", "content": "Смена началась. Разбери, что пришло."}]
    step = 0

    queue = run_tool("pending", {}).split(" | ")

    # Список составлен до первого разбора. Что в нём не окажется?
    for event in queue:
        step += 1
        response = model.call(messages, tools=TOOLS, event=event)
        for call in response.tool_calls:
            messages.append({"role": "tool", "content": run_tool(call.name, call.arguments)})

    return model.call(messages, tools=TOOLS).text, step
