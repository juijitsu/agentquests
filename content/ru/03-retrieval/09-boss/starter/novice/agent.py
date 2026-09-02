"""Уровень 09 · новичок. Пять нарушений в одном проходе."""

from scenario import DOCS, THRESHOLD, TOP_K, Model, run_tool


def run(question: str) -> tuple[str, int]:
    model = Model()

    # TODO 1 (уровень 05): вопрос из двух половин, а запрос один.
    #        model.split(question) вернёт подвопросы — обрабатывайте каждый.
    # TODO 2 (уровень 07): если в подвопросе есть обозначение
    #        (model.identifier), сузьте корпус run_tool("exact", ...) —
    #        иначе в подборку попадёт накладная 4478, она свежее.
    # TODO 3 (уровень 08): ранжируйте по произведению похожести на
    #        model.freshness(d), иначе победит тариф позапрошлого года.
    # TODO 4 (уровень 04): пропускайте повторы через model.same_fact,
    #        иначе три копии ставки вытеснят топливную надбавку.
    # TODO 5 (уровень 06): если лучший счёт ниже THRESHOLD, ответа нет —
    #        отдайте model.say_missing(part) вместо подборки.
    picked = sorted(
        DOCS, key=lambda d: model.similarity(question, d["text"]), reverse=True
    )[:TOP_K]

    return model.reply(question, [picked]), 1
