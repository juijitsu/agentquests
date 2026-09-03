"""Level 02 · novice. The loop exits on a technical sign, not on the goal."""

from scenario import Model, TOOLS, run_tool

GOAL = "Newark"
MAX_STEPS = 12


def run(question: str) -> tuple[str, int]:
    model = Model()
    messages = [{"role": "user", "content": question}]

    for step in range(1, MAX_STEPS + 1):
        response = model.call(messages, tools=TOOLS)
        messages.append({"role": "assistant", "content": response.text})

        if response.tool_calls:
            for call in response.tool_calls:
                try:
                    result = run_tool(call.name, call.arguments)
                except ValueError as exc:
                    result = str(exc)
                messages.append({"role": "tool", "content": result})
            continue

        # TODO: the model stopped asking for a tool — but the task is solved
        #       only if we reached GOAL. If we did not, tell the model where
        #       we are now and continue the loop.
        return response.text, step

    return f"Could not get an answer in {MAX_STEPS} steps.", MAX_STEPS
