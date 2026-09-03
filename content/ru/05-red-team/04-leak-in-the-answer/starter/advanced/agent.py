"""Уровень 04 · продвинутый. Отобрано по отказам в журнале."""

from scenario import Model, run_tool


def run() -> tuple[str, int]:
    model = Model()
    requests = run_tool("requests", {})

    # Где инструмент отказал, там кто-то полез не в своё.
    found = [
        r["id"] for r in requests
        if any(not c["allowed"] for c in model.calls(r["id"]))
    ]

    return model.report(found), len(requests)
