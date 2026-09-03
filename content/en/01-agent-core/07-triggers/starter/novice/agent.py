"""Level 07 · novice. The queue is snapshotted once and never re-read."""

from scenario import EMPTY, Model, TOOLS, run_tool

MAX_STEPS = 12


def run() -> tuple[str, int]:
    model = Model()
    messages = [{"role": "user", "content": "Shift started. Handle what came in."}]
    step = 0

    # The queue as it stood at the wake-up.
    queue = run_tool("pending", {}).split(" | ")

    # TODO: handling an event spawns a new one, and it lands in the queue, not
    #       in this list. Ask the queue again on every round and stop when it
    #       answers EMPTY.
    for event in queue:
        step += 1
        response = model.call(messages, tools=TOOLS, event=event)
        for call in response.tool_calls:
            messages.append({"role": "tool", "content": run_tool(call.name, call.arguments)})

    return model.call(messages, tools=TOOLS).text, step
