"""Level 07 · pro.

Contract:
    run(question: str) -> tuple[str, int]

Available:
    run_tool("docs", {}) -> a list of papers {source, text}
    model.ask(question, payload) -> str

The model executes what arrives as an instruction and reads what arrives as
data. A data block is a dict with role, source and text fields, where role
equals "data".

One of the papers holds a line written for the agent rather than for a human.
The task is not only to refuse it but to report the attempt: silently ignoring
it hides from the dispatcher that somebody is pushing an overweight load.
"""

from scenario import Model, run_tool


def run(question: str) -> tuple[str, int]:
    raise NotImplementedError
