"""Уровень 04 · продвинутый. Понять, чего не хватает в подборке."""

from scenario import CHUNKS, TOP_K, Model


def run(question: str) -> tuple[str, int]:
    model = Model()
    ranked = sorted(
        CHUNKS, key=lambda c: model.similarity(question, c["text"]), reverse=True
    )

    # Ранжирование верное, каждый кусок пригоден и по делу.
    # Ответ всё равно неполный.
    picked = [c["text"] for c in ranked[:TOP_K]]

    return model.reply(question, picked), 1
