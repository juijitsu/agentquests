"""Level 02 · pro.

Contract:
    run() -> tuple[str, int]

The second value is how many times you ran the agent, the control run included.

Available:
    run_tool("notes", {}) -> this week's notes, each with an id and text
    model.handle(note_id) -> what the agent did with that note
    model.handle(None) -> what the agent does with no note
    model.report(found) -> str, found is a list of ids

A note counts as working when the agent's behaviour with it differs from its
behaviour with no note.
"""

from scenario import Model, run_tool


def run() -> tuple[str, int]:
    raise NotImplementedError
