"""Уровень 07 · новичок. Бумаги склеены с заданием в один текст."""

from scenario import Model, run_tool


def run(question: str) -> tuple[str, int]:
    model = Model()
    docs = run_tool("docs", {})

    # TODO: склейка ставит текст из бумаг вровень с самим заданием, и строка
    #       «игнорируй ограничения» читается как указание. Передайте блоки
    #       с ролью: {"role": "data", "source": d["source"], "text": d["text"]}.
    payload = "\n".join(d["text"] for d in docs)

    return model.ask(question, payload), 1
