"""Уровень 07 · продвинутый. Понять, что смысл здесь различить не может."""

from scenario import DOCS, Model, run_tool


def run(question: str) -> tuple[str, int]:
    model = Model()

    # Смысловой поиск работает как задумано: он находит накладную с весом.
    # Накладную. С весом. Не ту.
    best = max(DOCS, key=lambda d: model.similarity(question, d["text"]))

    return model.reply(question, best), 1
