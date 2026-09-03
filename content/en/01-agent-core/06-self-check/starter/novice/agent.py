"""Level 06 · novice. The result is handed over with no review."""

from scenario import Model, TOOLS, run_tool

MAX_STEPS = 10


def run(question: str) -> tuple[str, int]:
    model = Model()
    messages = [{"role": "user", "content": question}]

    for step in range(1, MAX_STEPS + 1):
        response = model.call(messages, tools=TOOLS)
        messages.append({"role": "assistant", "content": response.text})

        if response.tool_calls:
            for call in response.tool_calls:
                result = run_tool(call.name, call.arguments)
                messages.append({"role": "tool", "content": result})
            continue

        # TODO: every step succeeded, but that does not yet mean the result
        #       is right. Before returning, show it to the model — model.review(
        #       response.text, question) — and hand over what it gives back.
        return response.text, step

    return f"Could not get an answer in {MAX_STEPS} steps.", MAX_STEPS
