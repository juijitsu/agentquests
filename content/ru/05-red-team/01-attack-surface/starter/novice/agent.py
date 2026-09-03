"""Уровень 01 · новичок. Проверено поле ввода, и только оно."""

from scenario import FROM_OUTSIDE, Model, run_tool


def run() -> tuple[str, int]:
    model = Model()
    inputs = run_tool("inputs", {})

    # TODO: поле ввода заполняет ваш диспетчер — снаружи им никто не
    #       управляет. Спросите model.who_controls(i["id"]) про каждый вход
    #       из inputs и оставьте те, где ответ равен FROM_OUTSIDE.
    surface = [
        i["id"] for i in inputs
        if i["id"] == "question" and model.who_controls(i["id"]) == FROM_OUTSIDE
    ]

    return model.report(surface), 1
