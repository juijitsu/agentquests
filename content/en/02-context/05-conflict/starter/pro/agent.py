"""Level 05 · pro.

Contract:
    run(question: str) -> tuple[str, int]

Available:
    run_tool("facts", {}) -> a list of records {source, field, value}
    model.ask(question, merged) -> str

The model expects a mapping "field -> readings", where a reading is a pair
(source, value). The same field can arrive from different documents with
different values, and that is not a data error.
"""

from scenario import Model, run_tool


def run(question: str) -> tuple[str, int]:
    raise NotImplementedError
