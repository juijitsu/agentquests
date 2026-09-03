"""Level 08 · pro. The finale of the track.

Contract:
    run() -> tuple[str, int]

Available:
    CASES — every case has an id and a kind
    RUNS, RUBRIC, BAR
    run_tool("answer", {"case": id, "run": n}) -> the answer on run n
    run_tool("in_prompt", {"case": id}) -> whether the case sits in the prompt
    model.judge_own(answer) / model.judge_blind(rubric, answer)
    model.decide(by_kind, flaky) -> str

The report counts if an independent judge did the grading; the leak was
checked over every case and excluded from the score; every case was run RUNS
times; the share was computed within kinds; and the unstable cases are named.
"""

from scenario import CASES, RUBRIC, RUNS, Model, run_tool


def run() -> tuple[str, int]:
    raise NotImplementedError
