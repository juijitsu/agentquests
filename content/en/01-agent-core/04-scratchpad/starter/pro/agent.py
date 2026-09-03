"""Level 04 · pro.

Contract:
    run(question: str) -> tuple[str, int]

The write_note tool is wired up and the model uses it: on spotting a limit on
the route it writes it into scenario.NOTES. The model's window is 8 messages.
At the finish the decision is made from what the model can see in the window.
"""

from scenario import Model, TOOLS, NOTES, run_tool


def run(question: str) -> tuple[str, int]:
    raise NotImplementedError
