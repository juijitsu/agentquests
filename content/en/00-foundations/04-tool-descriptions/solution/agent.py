"""Level 04 · reference. The description names the use case and the values."""

from scenario import Model, run_tool

TOOLS = [
    {
        "name": "check_border_status",
        "description": (
            "Shows the queue and wait time at a border crossing. "
            "Allowed values for crossing: Laredo, El Paso, Otay Mesa."
        ),
        "parameters": {"crossing": "string"},
    },
    {
        "name": "estimate_cost",
        "description": "Prices a haul by load weight, taking crossing wait time into account.",
        "parameters": {"weight_tons": "number"},
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
