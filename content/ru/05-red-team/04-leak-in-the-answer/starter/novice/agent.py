"""Уровень 04 · новичок. Отобрано по отказам в журнале."""

from scenario import Model, run_tool


def run() -> tuple[str, int]:
    model = Model()
    requests = run_tool("requests", {})

    # TODO: отказ — это доказательство, что контроль сработал, а не находка.
    #       Утечка там, где все вызовы разрешены, а в ответ ушло чужое.
    #       Смотрите model.facts(r["id"]) и сравнивайте f["owner"] с CALLER.
    found = [
        r["id"] for r in requests
        if any(not c["allowed"] for c in model.calls(r["id"]))
    ]

    return model.report(found), len(requests)
