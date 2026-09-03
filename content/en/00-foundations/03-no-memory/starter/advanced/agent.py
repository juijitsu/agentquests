"""Level 03 · advanced. Accumulating the history is yours to write."""

from scenario import Model, TOOLS, run_tool

MAX_STEPS = 10


def run(question: str) -> tuple[str, int]:
    """Returns (agent answer, iterations spent)."""
    model = Model()

    for step in range(1, MAX_STEPS + 1):
        # Here: collect the conversation history and pass it to the model so
        # that what was said on the first turn is available on the last.
        response = model.call([], tools=TOOLS)

        if response.tool_calls:
            for call in response.tool_calls:
                run_tool(call.name, call.arguments)
            continue

        return response.text, step

    raise RecursionError("iteration limit exhausted")
