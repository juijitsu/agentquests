"""Finale · advanced. The file holds exactly three defects. Where is not said."""

from scenario import Model, run_tool

MAX_STEPS = 1

TOOLS = [
    {
        "name": "check_border_status",
        "description": "Returns data.",
        "parameters": {"crossing": "string"},
    },
    {
        "name": "get_shipment_status",
        "description": "Returns a shipment status by number and the queue at a crossing.",
        "parameters": {"shipment_id": "string"},
    },
]


def run(question: str) -> tuple[str, int]:
    model = Model()
    messages = [{"role": "user", "content": question}]

    for step in range(1, MAX_STEPS + 1):
        response = model.call(messages, tools=TOOLS)
        messages.append({"role": "assistant", "content": response.text})

        if response.tool_calls:
            for call in response.tool_calls:
                try:
                    result = run_tool(call.name, call.arguments)
                except ValueError as exc:
                    return f"Could not do it: {exc}", step
                messages.append({"role": "tool", "content": result})
            continue

        return response.text, step

    return f"Could not get an answer in {MAX_STEPS} steps.", MAX_STEPS
