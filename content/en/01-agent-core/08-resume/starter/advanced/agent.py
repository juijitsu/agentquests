"""Level 08 · advanced. Decide yourself what has to survive the process."""

from scenario import DONE, Model, TOOLS, run_tool

MAX_STEPS = 10


def run() -> tuple[str, int]:
    model = Model()
    messages = [{"role": "user", "content": "Assemble the haul Laredo → Newark."}]

    for step in range(1, MAX_STEPS + 1):
        response = model.call(messages, tools=TOOLS)
        messages.append({"role": "assistant", "content": response.text})

        if response.tool_calls:
            for call in response.tool_calls:
                result = run_tool(call.name, call.arguments)
                messages.append({"role": "tool", "content": result})
                # Everything the agent knows about its work sits in messages.
                # Which of it will be left once the process is killed?

            continue

        return response.text, step

    return f"Could not assemble the haul in {MAX_STEPS} steps.", MAX_STEPS
