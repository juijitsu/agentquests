"""Level 01 · pro. Build the loop yourself.

Contract:
    run(question: str) -> tuple[str, int]   # agent answer, iterations spent

Available from scenario:
    Model().call(messages, tools) -> Response(text, tool_calls)
    TOOLS, run_tool(name, arguments) -> str
"""

from scenario import Model, TOOLS, run_tool


def run(question: str) -> tuple[str, int]:
    raise NotImplementedError
