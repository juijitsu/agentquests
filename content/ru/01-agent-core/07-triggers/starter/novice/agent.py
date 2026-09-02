"""Уровень 07 · новичок. Очередь снята один раз и больше не перечитана."""

from scenario import EMPTY, Model, TOOLS, run_tool

MAX_STEPS = 12


def run() -> tuple[str, int]:
    model = Model()
    messages = [{"role": "user", "content": "Смена началась. Разбери, что пришло."}]
    step = 0

    # Очередь на момент побудки.
    queue = run_tool("pending", {}).split(" | ")

    # TODO: разбор события порождает новое, и оно попадает в очередь, а не в
    #       этот список. Спрашивайте очередь заново на каждом круге и
    #       останавливайтесь, когда она ответит EMPTY.
    for event in queue:
        step += 1
        response = model.call(messages, tools=TOOLS, event=event)
        for call in response.tool_calls:
            messages.append({"role": "tool", "content": run_tool(call.name, call.arguments)})

    return model.call(messages, tools=TOOLS).text, step
