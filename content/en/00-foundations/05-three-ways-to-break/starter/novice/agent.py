"""Level 05 · novice. There is a limiter, but it takes the process down."""

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

    # TODO: running out of budget is a result, not an incident.
    #       Return a message a person can read: how many steps went by
    #       and which tool everything got stuck on.
    raise RecursionError("iteration limit exhausted")
