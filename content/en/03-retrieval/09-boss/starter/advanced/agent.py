"""Level 09 · advanced.

The search engine has to satisfy five conditions at once:

    split the question          — there are two halves, and one has no answer
    narrow by the number        — the neighbouring waybill is fresher
    discount by time            — the full tariff from two years ago is the most similar
    drop repeats                — the rate sits in three copies
    know about the threshold    — otherwise the Talmadge bridge gets a confident answer

Below is a search engine that breaks all five.
"""

from scenario import DOCS, THRESHOLD, TOP_K, Model, run_tool


def run(question: str) -> tuple[str, int]:
    model = Model()
    picked = sorted(
        DOCS, key=lambda d: model.similarity(question, d["text"]), reverse=True
    )[:TOP_K]
    return model.reply(question, [picked]), 1
