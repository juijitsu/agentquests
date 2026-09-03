"""Level 08 · reference. What is done is written outside — and after the fact."""

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
                # The tool returned, so the booking really exists.
                # Only now can it be written into the state.
                DONE.append(call.arguments["leg"])

            continue

        return response.text, step

    return f"Could not assemble the haul in {MAX_STEPS} steps.", MAX_STEPS
