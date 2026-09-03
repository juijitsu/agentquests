"""Level 08 · novice. Progress lives in messages and dies with them."""

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
                # TODO: messages will not survive a restart, but DONE will.
                #       Mark the booked leg here — then after a crash the model
                #       sees what is already done and will not repeat it.

            continue

        return response.text, step

    return f"Could not assemble the haul in {MAX_STEPS} steps.", MAX_STEPS
