"""Eighth shift of the track. The whole evaluation: ship it or not."""

LANG = "en"
TITLE = "Evaluation track · Level 08 · Boss: the whole evaluation"
BRIEF = """The new version is ready for release. One run with self-grading gives
nine of nine. The truth is zero percent on overweight."""

RUNS = 3
BAR = 90
RUBRIC = """An answer counts if it names a specific correct value.
An evasive wording and an approximation do not count."""

CASES = [
    {"id": "w1", "kind": "overweight"},
    {"id": "w2", "kind": "overweight"},
    {"id": "w3", "kind": "overweight"},
    {"id": "r1", "kind": "rates"},
    {"id": "r2", "kind": "rates"},
    {"id": "r3", "kind": "rates"},
    {"id": "s1", "kind": "schedule"},
    {"id": "s2", "kind": "schedule"},
    {"id": "s3", "kind": "schedule"},
]

# These cases sit word for word in the agent's prompt as examples.
IN_PROMPT = {"w1", "r1"}

# What the new version actually produces on each of the three runs.
TRUTH = {
    "w1": [True, True, True],
    "w2": [False, False, False],
    "w3": [True, False, True],
    "r1": [True, True, True],
    "r2": [True, True, True],
    "r3": [True, True, True],
    "s1": [True, True, True],
    "s2": [True, True, True],
    "s3": [True, False, False],
}

WHO = []
LOOKED = []
SEEN = []


def run_tool(name, arguments):
    if name == "answer":
        case, run = arguments["case"], arguments["run"]
        if case not in TRUTH:
            raise ValueError(f"case '{case}' is not in the set")
        if not 0 <= run < RUNS:
            raise ValueError(f"run {run} does not exist, there are {RUNS}")
        SEEN.append((case, run))
        return f"{case}:{run}"
    if name == "in_prompt":
        LOOKED.append(arguments["case"])
        return arguments["case"] in IN_PROMPT
    raise ValueError(f"tool '{name}' does not exist")


class Model:
    """Judges in two roles and assembles the decision from ready numbers."""

    def judge_own(self, answer):
        WHO.append("the author")
        return True

    def judge_blind(self, rubric, answer):
        WHO.append("independent")
        case, run = answer.split(":")
        return TRUTH[case][int(run)]

    def decide(self, by_kind, flaky):
        worst = min(by_kind, key=lambda k: by_kind[k]) if by_kind else None
        lines = ", ".join(f"{k} {by_kind[k]}%" for k in sorted(by_kind))
        verdict = (
            "it cannot ship"
            if flaky or (worst is not None and by_kind[worst] < BAR)
            else "it can ship"
        )
        tail = f" Unstable {len(flaky)}: {', '.join(sorted(flaky))}." if flaky else ""
        return f"By kind: {lines}.{tail} Decision — {verdict}."


def play(agent):
    for store in (WHO, LOOKED, SEEN):
        store.clear()
    return agent.run()


def explain(exc):
    if isinstance(exc, ZeroDivisionError):
        return ("Some kind has no cases left. A leak is excluded from the\n"
                "        score, not from the set of kinds.")
    return None


def _expected():
    clean = [c for c in CASES if c["id"] not in IN_PROMPT]
    by_kind, flaky = {}, []
    for kind in {c["kind"] for c in clean}:
        same = [c for c in clean if c["kind"] == kind]
        stable = 0
        for c in same:
            runs = TRUTH[c["id"]]
            if all(runs):
                stable += 1
            elif any(runs):
                flaky.append(c["id"])
        by_kind[kind] = round(100 * stable / len(same))
    return by_kind, sorted(flaky)


def verify(result):
    answer, steps = result
    text = answer if isinstance(answer, str) else ""
    by_kind, flaky = _expected()
    weakest = min(by_kind, key=lambda k: by_kind[k])
    # Leaked cases need not be run — coverage is counted over the rest.
    per_case = {
        c["id"]: len({r for k, r in SEEN if k == c["id"]})
        for c in CASES if c["id"] not in IN_PROMPT
    }
    covered = min(per_case.values()) if per_case else 0
    named = f"{weakest} {by_kind[weakest]}%" in text
    return [
        (sorted(set(WHO)) == ["independent"],
         f"who judged: {', '.join(sorted(set(WHO))) or 'nobody'}"),
        (set(LOOKED) == {c["id"] for c in CASES},
         f"checked for a leak: {len(set(LOOKED))} of {len(CASES)}"),
        (covered == RUNS, f"runs per case: {covered} of {RUNS}"),
        (named,
         f"weak kind: {weakest} {by_kind[weakest]}% — {'named' if named else 'no'}"),
        ("it cannot ship" in text, f"decision: {text or 'no answer'}"),
        (steps <= 2, f"calls to the model: {steps} (2 allowed)"),
    ]
