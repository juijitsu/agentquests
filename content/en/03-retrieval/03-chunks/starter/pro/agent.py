"""Level 03 · pro.

Contract:
    run(question: str) -> tuple[str, int]

Available:
    CHUNKS — the index; a chunk has id, doc and text
    run_tool("neighbours", {"id": ...}) -> chunks of the same document, in order
    model.similarity(left, right) -> closeness of two texts
    model.answers(question, text) -> whether the text stands alone
    model.reply(question, text) -> str

The index is split by sentence. One fact in it is cut by a chunk boundary,
and the only fact lying whole is about a different object.
"""

from scenario import CHUNKS, Model, run_tool


def run(question: str) -> tuple[str, int]:
    raise NotImplementedError
