"""Level 04 · advanced. Both descriptions are yours to write."""

from scenario import Model, run_tool

# The tools are declared, the descriptions are empty. The model sees only these —
# it never sees the implementation.
TOOLS = [
    {
        "name": "estimate_cost",
        "description": "",
        "parameters": {"weight_tons": "number"},
    },
    {
        "name": "check_border_status",
        "description": "",
        "parameters": {"crossing": "string"},
    },
]


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

        return response.text, step

    raise RecursionError("iteration limit exhausted")
