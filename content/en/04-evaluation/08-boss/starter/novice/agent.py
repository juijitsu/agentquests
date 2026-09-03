"""Level 08 · novice. Five violations in one report."""

from scenario import CASES, RUBRIC, RUNS, Model, run_tool


def run() -> tuple[str, int]:
    model = Model()

    # TODO 1 (level 04): the author does the judging — it scores everything for
    #        itself. Judging belongs to model.judge_blind(RUBRIC, answer).
    # TODO 2 (level 05): two cases sit in the prompt. Ask
    #        run_tool("in_prompt", ...) for each and exclude them from the score.
    # TODO 3 (level 06): one run does not tell broken from unstable.
    #        Run every case RUNS times.
    # TODO 4 (level 03): an overall percentage hides the failure — compute the
    #        share within each kind (the kind field).
    # TODO 5: a case counts as stably correct only if it is correct on every run.
    passed = sum(
        model.judge_own(run_tool("answer", {"case": c["id"], "run": 0}))
        for c in CASES
    )
    by_kind = {"everything": round(100 * passed / len(CASES))}

    return model.decide(by_kind, []), 1
