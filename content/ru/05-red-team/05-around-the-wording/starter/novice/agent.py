"""Уровень 05 · новичок. Отобрано по словам самого правила."""

from scenario import Model, run_tool


def run() -> tuple[str, int]:
    model = Model()
    probes = run_tool("probes", {})

    # TODO: правило написано про слова, а существует ради цели. Проверять
    #       надо цель: GOAL in model.ask(p["id"])["derives"]. Названо
    #       число или нет — к делу не относится, как и отказ.
    found = [
        p["id"] for p in probes
        if model.ask(p["id"])["names_rate"]
    ]

    return model.report(found), len(probes)
