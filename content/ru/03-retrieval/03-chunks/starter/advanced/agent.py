"""Уровень 03 · продвинутый. Почему проверка ничего не пропускает."""

from scenario import CHUNKS, Model, run_tool


def run(question: str) -> tuple[str, int]:
    model = Model()

    # Куски отобраны верно, проверка на пригодность работает верно.
    # Пригодных нет ни одного, а ответ агент всё равно выдаёт.
    fit = [c["text"] for c in CHUNKS if model.answers(question, c["text"])]
    best = max(fit or [c["text"] for c in CHUNKS],
               key=lambda t: model.similarity(question, t))

    return model.reply(question, best), 1
