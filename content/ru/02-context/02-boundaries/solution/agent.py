"""Уровень 02 · эталон. Каждая строка уходит со своим источником."""

from scenario import Model, run_tool


def run(question: str) -> tuple[str, int]:
    model = Model()
    lines = run_tool("about", {"topic": model.topic(question)}).split(" | ")

    # Граница, которую разрушил отбор, восстанавливается здесь.
    blocks = [f'{run_tool("source", {"line": line})}: {line}' for line in lines]

    return model.ask(question, blocks), 1
