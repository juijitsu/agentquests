"""Level 05 · reference. Running out of budget is a result, not an incident."""

from scenario import Model, TOOLS, run_tool

MAX_STEPS = 10


def run(question: str) -> tuple[str, int]:
    model = Model()
    messages = [{"role": "user", "content": question}]
    last_tool = None

    for step in range(1, MAX_STEPS + 1):
        response = model.call(messages, tools=TOOLS)
        messages.append({"role": "assistant", "content": response.text})

        if response.tool_calls:
            for call in response.tool_calls:
                last_tool = call.name
                result = run_tool(call.name, call.arguments)
                messages.append({"role": "tool", "content": result})
            continue

        return response.text, step

    return (
        f"Could not get an answer in {MAX_STEPS} steps. "
        f"The agent kept calling {last_tool} and made no progress. "
        f"It looks like the tool returns data the model cannot finish on.",
        MAX_STEPS,
    )
