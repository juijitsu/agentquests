"""Уровень 09 · профессионал. Финал трека.

Контракт:
    run(question: str) -> tuple[str, int]

Доступно:
    DOCS, TOP_K, THRESHOLD
    run_tool("exact", {"token": ...}) -> буквальные вхождения
    model.split(question) -> подвопросы
    model.identifier(part) -> обозначение, если оно есть
    model.similarity(left, right), model.freshness(doc), model.same_fact(a, b)
    model.say_missing(part) -> честный отказ
    model.reply(question, selection) -> str

selection — список по одному элементу на подвопрос: либо подборка
документов, либо строка отказа.

Ответ засчитан, если обработаны обе половины; в подборке нет чужих
накладных; названа полная стоимость по 4471; про отсутствующий мост дан
отказ с названием предмета.
"""

from scenario import DOCS, THRESHOLD, TOP_K, Model, run_tool


def run(question: str) -> tuple[str, int]:
    raise NotImplementedError
