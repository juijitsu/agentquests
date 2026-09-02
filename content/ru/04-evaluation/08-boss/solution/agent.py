"""Уровень 08 · эталон. Пять приёмов трека в одном отчёте."""

from scenario import CASES, RUBRIC, RUNS, Model, run_tool


def run() -> tuple[str, int]:
    model = Model()

    # 05: случай из промпта измеряет память, а не работу.
    clean = [c for c in CASES if not run_tool("in_prompt", {"case": c["id"]})]

    # 06: один прогон говорит, что случилось; несколько — что случается.
    # 04: судит тот, кто ответа не писал, и по записанному заранее правилу.
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

    # 03: доля считается внутри вида, иначе лёгкие виды вытянут среднее.
    by_kind = {}
    for kind in {c["kind"] for c in clean}:
        same = [c for c in clean if c["kind"] == kind]
        hit = [c for c in same if c["id"] in stable]
        by_kind[kind] = round(100 * len(hit) / len(same))

    return model.decide(by_kind, flaky), 1
