"""Level 07 · pro.

Contract:
    run() -> tuple[str, int]

No argument: nobody asks the agent, it gets woken up. Work comes from the queue.

Available:
    run_tool("pending", {})            -> events joined by " | ", or EMPTY
    run_tool("handle", {"event": ...}) -> handles one event
    model.call(messages, tools, event=...) -> without event it closes the shift

Handling an event may spawn a new one. Stay within 8 iterations.
"""

from scenario import EMPTY, Model, TOOLS, run_tool


def run() -> tuple[str, int]:
    raise NotImplementedError
