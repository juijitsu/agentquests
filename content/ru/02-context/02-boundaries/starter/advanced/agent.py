"""Уровень 02 · продвинутый. Границу восстановить самому."""

from scenario import Model, run_tool


def run(question: str) -> tuple[str, int]:
    model = Model()
    lines = run_tool("about", {"topic": model.topic(question)}).split(" | ")

    # Отобрано ровно то, что нужно. Три строки про рефрижератор —
    # и ответ всё равно про чужую надбавку.
    blocks = lines

    return model.ask(question, blocks), 1
