"""Level 02 · advanced. Parsing the model's answer is yours to write."""

from scenario import Model, TOOLS, run_tool

MAX_STEPS = 10


def run(question: str) -> tuple[str, int]:
    """Returns (agent answer, iterations spent)."""
    model = Model()
    messages = [{"role": "user", "content": question}]

    for step in range(1, MAX_STEPS + 1):
        response = model.call(messages, tools=TOOLS)
        messages.append({"role": "assistant", "content": response.text})

        # Here: take the answer apart so that the model's requests get run,
        # and the text goes out only when there are no requests left.

    raise RecursionError("iteration limit exhausted")
