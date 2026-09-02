"""Уровень 01 · эталон. В окно уходит отобранное, а не всё."""

from scenario import DOCS, Model, run_tool


def run(question: str) -> tuple[str, int]:
    model = Model()

    # Не «что у нас есть», а «что относится к вопросу».
    blocks = run_tool("about", {"topic": model.topic(question)}).split(" | ")

    return model.ask(question, blocks), 1
