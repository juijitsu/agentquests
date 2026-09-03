"""Level 03 · advanced. Why the check passes nothing at all."""

from scenario import CHUNKS, Model, run_tool


def run(question: str) -> tuple[str, int]:
    model = Model()

    # The chunks were selected correctly and the fitness check works correctly.
    # Not one is fit, and the agent produces an answer regardless.
    fit = [c["text"] for c in CHUNKS if model.answers(question, c["text"])]
    best = max(fit or [c["text"] for c in CHUNKS],
               key=lambda t: model.similarity(question, t))

    return model.reply(question, best), 1
