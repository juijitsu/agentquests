"""Уровень 01 · эталон. Ищет по близости понятий."""

from scenario import DOCS, QUESTION, Model, run_tool


def run(question: str) -> tuple[str, int]:
    model = Model()

    # Совпадение слов ничего не говорит о том, про что документ.
    best = max(DOCS, key=lambda d: model.similarity(question, d["text"]))

    return model.answer(question, best), 1
