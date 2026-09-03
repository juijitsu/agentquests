"""Level 07 · advanced. Work out the stopping condition yourself."""

from scenario import EMPTY, Model, TOOLS, run_tool

MAX_STEPS = 12


def run() -> tuple[str, int]:
    model = Model()
    messages = [{"role": "user", "content": "Shift started. Handle what came in."}]
    step = 0

    queue = run_tool("pending", {}).split(" | ")

    # The list was made before the first handling. What will not be in it?
    for event in queue:
        step += 1
        response = model.call(messages, tools=TOOLS, event=event)
        for call in response.tool_calls:
            messages.append({"role": "tool", "content": run_tool(call.name, call.arguments)})

    return model.call(messages, tools=TOOLS).text, step
