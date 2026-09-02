"""Уровень 01 · новичок. Ищет по совпадению слов."""

from scenario import DOCS, QUESTION, Model, run_tool


def run(question: str) -> tuple[str, int]:
    model = Model()

    # TODO: в вопросе «вес», в нужном документе «масса» — общих слов нет,
    #       зато слово «ограничение» есть у знака скорости. Считайте близость
    #       по смыслу: model.similarity(question, doc["text"]) и берите max.
    best = run_tool("keyword", {"query": question})[0]

    return model.answer(question, best), 1
