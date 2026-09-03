"""Level 04 · reference. Terms, notepad and tail all go into the window."""

from scenario import Model, TOOLS, NOTES, run_tool

WINDOW = 8
MAX_STEPS = 14


def run(question: str) -> tuple[str, int]:
    model = Model()
    messages = [{"role": "user", "content": question}]
    facts = {"role": "user", "content": f"Task terms: {question}"}

    def window(history):
        notes = [{"role": "user", "content": f"From the notepad: {n}"} for n in NOTES]
        tail = WINDOW - 1 - len(notes)
        return [facts] + notes + history[-tail:]

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
