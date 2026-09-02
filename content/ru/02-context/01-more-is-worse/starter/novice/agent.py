"""Уровень 01 · новичок. В окно уходит вся папка по рейсу."""

from scenario import DOCS, Model, run_tool


def run(question: str) -> tuple[str, int]:
    model = Model()

    # TODO: двадцать две бумаги модель целиком не прочтёт — из длинного
    #       списка она видит только начало и конец. Спросите, какие из них
    #       относятся к делу: run_tool("about", {"topic": model.topic(question)})
    #       вернёт их через " | ", и в окно надо отправить только их.
    blocks = list(DOCS)

    return model.ask(question, blocks), 1
