"""Level 08 · reference. The track's five techniques in one report."""

from scenario import CASES, RUBRIC, RUNS, Model, run_tool


def run() -> tuple[str, int]:
    model = Model()

    # 05: a case from the prompt measures memory, not work.
    clean = [c for c in CASES if not run_tool("in_prompt", {"case": c["id"]})]

    # 06: one run tells you what happened; several tell you what happens.
    # 04: judging belongs to whoever did not write the answer, by a rule
    #     written down in advance.
    stable, flaky = set(), []
    for case in clean:
        results = [
            model.judge_blind(RUBRIC, run_tool("answer", {"case": case["id"], "run": n}))
            for n in range(RUNS)
        ]
        if all(results):
            stable.add(case["id"])
        elif any(results):
            flaky.append(case["id"])

    # 03: the share is computed within a kind, or easy kinds pull the average up.
    by_kind = {}
    for kind in {c["kind"] for c in clean}:
        same = [c for c in clean if c["kind"] == kind]
        hit = [c for c in same if c["id"] in stable]
        by_kind[kind] = round(100 * len(hit) / len(same))

    return model.decide(by_kind, flaky), 1
