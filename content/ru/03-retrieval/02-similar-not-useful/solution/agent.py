"""Уровень 02 · эталон. Сперва пригодные, потом самый похожий из них."""

from scenario import DOCS, Model


def run(question: str) -> tuple[str, int]:
    model = Model()

    # Два шага, и порядок важен: отбор по пригодности сужает поле,
    # похожесть выбирает лучшего среди оставшихся.
    fit = [d for d in DOCS if model.answers(question, d)]
    best = max(fit, key=lambda d: model.similarity(question, d["text"]))

    return model.reply(question, best), 1
