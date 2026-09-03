"""Level 05 · novice. A closed hop is handled like an ordinary result."""

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

                # TODO: this result means the plan became impossible.
                #       Ask for a new one — model.make_plan(question, blocked=...) —
                #       and put it into the history. Where to go is the model's call.

            continue

        return response.text, step

    return f"Could not get an answer in {MAX_STEPS} steps.", MAX_STEPS
