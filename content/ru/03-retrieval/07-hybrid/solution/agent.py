"""Уровень 07 · эталон. Точное сужает, смысл выбирает."""

from scenario import DOCS, Model, run_tool


def run(question: str) -> tuple[str, int]:
    model = Model()

    # Обозначение отвечает «про что именно», смысл — «что именно спрашивали».
    same_number = run_tool("exact", {"token": model.identifier(question)})
    best = max(same_number, key=lambda d: model.similarity(question, d["text"]))

    return model.reply(question, best), 1
