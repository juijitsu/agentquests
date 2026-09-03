"""Level 02 · advanced. The stopping condition is yours to write."""

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

        # Here: decide whether the task is finished. The model knows one step only.
        return response.text, step

    return f"Could not get an answer in {MAX_STEPS} steps.", MAX_STEPS
