"""Уровень 08 · новичок. Пять нарушений в одном отчёте."""

from scenario import CASES, RUBRIC, RUNS, Model, run_tool


def run() -> tuple[str, int]:
    model = Model()

    # TODO 1 (уровень 04): судит автор — он засчитывает себе всё.
    #        Судить должен model.judge_blind(RUBRIC, answer).
    # TODO 2 (уровень 05): два случая лежат в промпте. Спросите
    #        run_tool("in_prompt", ...) по каждому и исключите их из счёта.
    # TODO 3 (уровень 06): один прогон не отличает сломанное от
    #        неустойчивого. Прогоните каждый случай RUNS раз.
    # TODO 4 (уровень 03): общий процент прячет провал — считайте долю
    #        внутри каждого вида (поле kind).
    # TODO 5: устойчиво верным считается случай, верный на всех прогонах.
    passed = sum(
        model.judge_own(run_tool("answer", {"case": c["id"], "run": 0}))
        for c in CASES
    )
    by_kind = {"всё": round(100 * passed / len(CASES))}

    return model.decide(by_kind, []), 1
