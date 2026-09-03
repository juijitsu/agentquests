"""Level 03 · novice. The history is cut by the tail, and the start is lost."""

from scenario import Model, TOOLS, run_tool

WINDOW = 8
MAX_STEPS = 12


def run(question: str) -> tuple[str, int]:
    model = Model()
    messages = [{"role": "user", "content": question}]

    def window(history):
        # TODO: a tail of the latest messages fits the window, but the terms of
        #       the task stayed in the very first message and no longer reach
        #       the model. Keep what is needed and put it at the front.
        return history[-WINDOW:]

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
