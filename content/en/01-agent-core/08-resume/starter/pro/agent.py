"""Level 08 · pro.

Contract:
    run() -> tuple[str, int]

run() will be called twice: the first run is cut short halfway, the second
must take the haul to the end. A booking is paid and irreversible — a leg
paid for twice will not be counted.

Available:
    DONE — a list that survives a restart (in real life a file or a database row)

The model looks at DONE, not at the conversation history. The crash inherits
from BaseException: it cannot be caught, that is what makes it a crash.
"""

from scenario import DONE, Model, TOOLS, run_tool


def run() -> tuple[str, int]:
    raise NotImplementedError
