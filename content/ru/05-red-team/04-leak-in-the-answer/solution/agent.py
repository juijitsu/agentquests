"""Уровень 04 · эталон. Смотрим на то, что ушло, а не на то, что позволено."""

from scenario import CALLER, Model, run_tool


def run() -> tuple[str, int]:
    model = Model()
    requests = run_tool("requests", {})

    # Журнал вызовов не спрашивается вовсе: он говорит про права агента,
    # а утечка — это про права спрашивающего.
    found = [
        r["id"] for r in requests
        if any(f["owner"] != CALLER for f in model.facts(r["id"]))
    ]

    return model.report(found), len(requests)
