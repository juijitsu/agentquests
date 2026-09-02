"""Уровень 05 · новичок. Один запрос на вопрос из двух половин."""

from scenario import Model, run_tool


def run(question: str) -> tuple[str, int]:
    model = Model()

    # TODO: вопрос содержит два разных запроса, а ищется он одним. Разложите
    #       его: model.split(question) вернёт подвопросы — ищите по каждому
    #       отдельно и сложите найденное, отбрасывая повторы по id.
    found = run_tool("search", {"query": question})

    return model.reply(question, found), 1
