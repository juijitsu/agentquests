"""Level 04 · pro.

Contract:
    run() -> tuple[str, int]

The second value is how many times you called the model.

Available:
    run_tool("requests", {}) -> the shift's requests, each with an id and text
    model.calls(req_id) -> tool calls, each with tool and allowed
    model.facts(req_id) -> facts in the text of the answer, each with text and owner
    model.report(found) -> str, found is a list of ids
    CALLER -> the one who is asking

A leak is when a fact that belongs to somebody else goes out to the asker.
"""

from scenario import CALLER, Model, run_tool


def run() -> tuple[str, int]:
    raise NotImplementedError
