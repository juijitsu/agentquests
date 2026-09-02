"""Уровень 01 · продвинутый. Отбор оставлен вам."""

from scenario import DOCS, Model, run_tool


def run(question: str) -> tuple[str, int]:
    model = Model()

    # Ограничение по мосту в этой папке есть. Ответ всё равно неверный.
    blocks = list(DOCS)

    return model.ask(question, blocks), 1
