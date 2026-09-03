"""Level 05 · pro.

Contract:
    run(question: str) -> tuple[str, int]

Available:
    run_tool("search", {"query": ...}) -> the best documents for one query
    model.split(question) -> a list of sub-questions
    model.reply(question, docs) -> str

The question asks about two different things at once. One query for such a
question lands between the topics and brings back documents for only one.
"""

from scenario import Model, run_tool


def run(question: str) -> tuple[str, int]:
    raise NotImplementedError
