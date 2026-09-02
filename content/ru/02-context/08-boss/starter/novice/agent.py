"""Уровень 08 · новичок. Пять нарушений в одиннадцати строках."""

from scenario import BUDGET, Model, run_tool


def run(question: str) -> tuple[str, int]:
    model = Model()
    blocks = run_tool("blocks", {})

    # TODO 1 (уровень 06): отбор по возрасту не работает — тут его нет вовсе,
    #        блоки берутся как лежат. Сортируйте по отдаче: worth / cost.
    # TODO 2 (уровень 05): у веса два показания, и они расходятся. Оба должны
    #        попасть в бриф, иначе агент ответит уверенно там, где ответа нет.
    # TODO 3 (уровни 02 и 07): каждому блоку нужны role="data" и source,
    #        иначе подложенная строка встанет вровень с заданием.
    # TODO 4 (уровень 07): подложенную бумагу не выбрасывать — о попытке
    #        надо сообщить, а выброшенное сообщить не из чего.
    brief = []
    spent = 0
    for block in blocks:
        if spent + block["cost"] <= BUDGET:
            brief.append(block["text"])
            spent += block["cost"]

    return model.ask(question, "\n".join(brief)), 1
