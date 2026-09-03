"""Уровень 05 · продвинутый. Отобрано по словам самого правила."""

from scenario import Model, run_tool


def run() -> tuple[str, int]:
    model = Model()
    probes = run_tool("probes", {})

    # Правило запрещает называть чужую ставку. Значит обход там,
    # где ставка названа.
    found = [
        p["id"] for p in probes
        if model.ask(p["id"])["names_rate"]
    ]

    return model.report(found), len(probes)
