"""Level 05 · pro.

Contract:
    run() -> tuple[str, int]

Available:
    CASES — the set of cases
    run_tool("check", {"case": id}) -> whether the agent's answer is correct
    run_tool("in_prompt", {"case": id}) -> whether the case sits in the prompt
    model.report(all_passed, all_total, clean_passed, clean_total) -> str

Some cases of the set ended up in the agent's prompt as examples. On those it
does not answer, it recalls.
"""

from scenario import CASES, Model, run_tool


def run() -> tuple[str, int]:
    raise NotImplementedError
