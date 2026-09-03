"""Level 05 · advanced. The reaction to a failure is yours to write."""

from scenario import Model, TOOLS, run_tool

MAX_STEPS = 14


def run(question: str) -> tuple[str, int]:
    model = Model()
    messages = [{"role": "user", "content": question}]
    messages.append({"role": "plan", "content": model.make_plan(question)})

    for step in range(1, MAX_STEPS + 1):
        response = model.call(messages, tools=TOOLS)
        messages.append({"role": "assistant", "content": response.text})

        if response.tool_calls:
            for call in response.tool_calls:
                result = run_tool(call.name, call.arguments)
                messages.append({"role": "tool", "content": result})

                # Not every tool result is equal. Some of them mean there is
                # no point going further along the plan.

            continue

        return response.text, step

    return f"Could not get an answer in {MAX_STEPS} steps.", MAX_STEPS
