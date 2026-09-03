"""Level 03 · reference. The window holds the facts plus a recent tail."""

from scenario import Model, TOOLS, run_tool

WINDOW = 8
MAX_STEPS = 12


def run(question: str) -> tuple[str, int]:
    model = Model()
    messages = [{"role": "user", "content": question}]

    # The terms of the task are as needed on the last step as on the first.
    facts = {"role": "user", "content": f"Task terms: {question}"}

    def window(history):
        return [facts] + history[-(WINDOW - 1):]

    for step in range(1, MAX_STEPS + 1):
        response = model.call(window(messages), tools=TOOLS)
        messages.append({"role": "assistant", "content": response.text})

        if response.tool_calls:
            for call in response.tool_calls:
                try:
                    result = run_tool(call.name, call.arguments)
                except ValueError as exc:
                    result = str(exc)
                messages.append({"role": "tool", "content": result})
            continue

        return response.text, step

    return f"Could not get an answer in {MAX_STEPS} steps.", MAX_STEPS
