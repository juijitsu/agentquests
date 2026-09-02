"""Уровень 02 · эталон. Сверяет ответы, а не написание."""

from scenario import CASES, Model, run_tool


def run() -> tuple[str, int]:
    model = Model()
    scores = {}

    # Правильность — свойство ответа, а не строки, которой он записан.
    for version in ("old", "new"):
        scores[version] = sum(
            model.same_answer(
                c["expected"], run_tool("ask", {"version": version, "case": c["id"]})
            )
            for c in CASES
        )

    return model.verdict(scores["old"], scores["new"], len(CASES)), 1
