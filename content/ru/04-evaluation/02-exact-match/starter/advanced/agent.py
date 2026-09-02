"""Уровень 02 · продвинутый. Понять, почему улучшение выглядит провалом."""

from scenario import CASES, Model, run_tool


def run() -> tuple[str, int]:
    model = Model()
    scores = {}

    # Набор прогоняется целиком, обе версии, как и положено.
    # Метрика требует откатить правку.
    for version in ("old", "new"):
        scores[version] = sum(
            run_tool("ask", {"version": version, "case": c["id"]}) == c["expected"]
            for c in CASES
        )

    return model.verdict(scores["old"], scores["new"], len(CASES)), 1
