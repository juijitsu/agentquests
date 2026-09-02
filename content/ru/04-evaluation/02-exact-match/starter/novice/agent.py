"""Уровень 02 · новичок. Сравнивает строки посимвольно."""

from scenario import CASES, Model, run_tool


def run() -> tuple[str, int]:
    model = Model()
    scores = {}

    # TODO: «2 доллара 90 центов» — это и есть 2.90, но посимвольно они
    #       не равны. Спрашивайте model.same_answer(expected, got) вместо
    #       сравнения строк.
    for version in ("old", "new"):
        scores[version] = sum(
            run_tool("ask", {"version": version, "case": c["id"]}) == c["expected"]
            for c in CASES
        )

    return model.verdict(scores["old"], scores["new"], len(CASES)), 1
