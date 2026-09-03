"""Level 01 · advanced. The tool-running block is yours to write."""

from scenario import Model, TOOLS, run_tool

MAX_STEPS = 10


def run(question: str) -> tuple[str, int]:
    """Returns (agent answer, iterations spent)."""
    model = Model()
    messages = [{"role": "user", "content": question}]

    for step in range(1, MAX_STEPS + 1):
        response = model.call(messages, tools=TOOLS)
        messages.append({"role": "assistant", "content": response.text})

        if not response.tool_calls:
            return response.text, step

        # Here: run every requested tool through run_tool
        # and give the result back to the model through messages.

    raise RecursionError("iteration limit exhausted")
