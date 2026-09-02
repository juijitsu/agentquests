"""Уровень 07 · новичок. Смысл не отличает 4471 от 4478."""

from scenario import DOCS, Model, run_tool


def run(question: str) -> tuple[str, int]:
    model = Model()

    # TODO: накладные 4471 и 4478 для смысла одинаковы — одни понятия, одна
    #       форма. Сузьте корпус точным поиском по обозначению из вопроса:
    #       run_tool("exact", {"token": model.identifier(question)}), и уже
    #       среди найденного выбирайте по смыслу.
    best = max(DOCS, key=lambda d: model.similarity(question, d["text"]))

    return model.reply(question, best), 1
