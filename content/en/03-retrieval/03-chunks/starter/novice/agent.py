"""Level 03 · novice. The previous level's technique stopped working."""

from scenario import CHUNKS, Model, run_tool


def run(question: str) -> tuple[str, int]:
    model = Model()

    # TODO: not one chunk passes the check — the Carroll bridge is named in one
    #       and its limit is in the neighbour. Rebuild every chunk with its
    #       document neighbours: run_tool("neighbours", {"id": c["id"]}) returns
    #       them in order; join the texts and check the joined text instead.
    fit = [c["text"] for c in CHUNKS if model.answers(question, c["text"])]
    best = max(fit or [c["text"] for c in CHUNKS],
               key=lambda t: model.similarity(question, t))

    return model.reply(question, best), 1
