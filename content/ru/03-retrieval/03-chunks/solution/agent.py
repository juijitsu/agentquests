"""Уровень 03 · эталон. Кусок достраивается до самодостаточного."""

from scenario import CHUNKS, Model, run_tool


def run(question: str) -> tuple[str, int]:
    model = Model()

    # Единица поиска — кусок, единица смысла — документ. Достраиваем первое
    # до второго, и только потом судим о пригодности.
    whole = []
    for chunk in CHUNKS:
        text = " ".join(c["text"] for c in run_tool("neighbours", {"id": chunk["id"]}))
        if model.answers(question, text):
            whole.append(text)

    best = max(whole, key=lambda t: model.similarity(question, t))

    return model.reply(question, best), 1
