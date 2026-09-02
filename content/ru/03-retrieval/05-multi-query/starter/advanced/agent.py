"""Уровень 05 · продвинутый. Понять, почему найдено только про склад."""

from scenario import Model, run_tool


def run(question: str) -> tuple[str, int]:
    model = Model()

    # Поиск отработал верно и вернул два подходящих документа.
    # Оба про одну половину вопроса.
    found = run_tool("search", {"query": question})

    return model.reply(question, found), 1
