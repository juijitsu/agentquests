"""Level 07 · reference. The queue is re-read on every round."""

from scenario import EMPTY, Model, TOOLS, run_tool

MAX_STEPS = 12


def run() -> tuple[str, int]:
    model = Model()
    messages = [{"role": "user", "content": "Shift started. Handle what came in."}]
    step = 0

    # The queue is alive: while we handle one thing, another appears in it.
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
