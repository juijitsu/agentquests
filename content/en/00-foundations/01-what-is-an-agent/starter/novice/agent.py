"""Level 01 · novice. One line is missing, and it is marked TODO."""

from scenario import Model, TOOLS, run_tool

MAX_STEPS = 10


def run(question: str) -> tuple[str, int]:
    model = Model()
    messages = [{"role": "user", "content": question}]

    for step in range(1, MAX_STEPS + 1):
        response = model.call(messages, tools=TOOLS)
        messages.append({"role": "assistant", "content": response.text})

        if not response.tool_calls:
            return response.text, step

        for call in response.tool_calls:
            result = run_tool(call.name, call.arguments)
            print(f"  [{step}] {call.name}({call.arguments}) -> {result}")

            # TODO: the result is computed, but the model will never see it.
            #       Put it into messages as a message with role "tool". One line.

    raise RecursionError("iteration limit exhausted")
