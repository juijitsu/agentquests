"""Sixth shift of the track. One run gave five of six. The second gave three."""

LANG = "en"
TITLE = "Evaluation track · Level 06 · One attempt means nothing"
BRIEF = """Two cases answer correctly one time and wrongly the next.
On one run they came out lucky, and the agent called the system working."""

RUNS = 5

# What the agent produces on each of the five runs. The model is
# non-deterministic, and some cases hold only every other time.
OUTCOMES = {
    "c1": [True, True, True, True, True],
    "c2": [True, True, True, True, True],
    "c3": [True, True, True, True, True],
    "c4": [False, False, False, False, False],
    "c5": [True, False, True, False, True],
    "c6": [True, True, False, False, False],
}
CASES = [{"id": k} for k in OUTCOMES]

STABLE_OK = sorted(k for k, v in OUTCOMES.items() if all(v))
FLAKY = sorted(k for k, v in OUTCOMES.items() if any(v) and not all(v))

SEEN = []


def run_tool(name, arguments):
    """Runs a case on the given run. Runs are numbered from zero."""
    if name != "check":
        raise ValueError(f"tool '{name}' does not exist")
    case, run = arguments["case"], arguments["run"]
    if case not in OUTCOMES:
        raise ValueError(f"case '{case}' is not in the set")
    if not 0 <= run < RUNS:
        raise ValueError(f"run {run} does not exist, there are {RUNS}")
    SEEN.append((case, run))
    return "correct" if OUTCOMES[case][run] else "wrong"


class Model:
    """Assembles a report from the stable and the unstable cases."""

    def report(self, stable_ok, flaky, total):
        if not flaky:
            return f"Stably correct {len(stable_ok)} of {total}."
        return (
            f"Stably correct {len(stable_ok)} of {total}. "
            f"Unstable {len(flaky)}: {', '.join(sorted(flaky))}."
        )


def play(agent):
    SEEN.clear()
    return agent.run()


def explain(exc):
    if isinstance(exc, ValueError) and "run" in str(exc):
        return ("Runs are numbered from zero and there are RUNS of them.\n"
                "        Iterate range(RUNS).")
    return None


def verify(result):
    answer, steps = result
    text = answer if isinstance(answer, str) else ""
    per_case = {c["id"]: len({r for k, r in SEEN if k == c["id"]}) for c in CASES}
    covered = min(per_case.values()) if per_case else 0
    named = all(f in text for f in FLAKY)
    return [
        (covered == RUNS, f"runs per case: {covered} of {RUNS}"),
        (named, f"unstable cases named: {', '.join(FLAKY) if named else 'no'}"),
        (f"Stably correct {len(STABLE_OK)} of {len(CASES)}" in text,
         f"report: {text or 'no answer'}"),
        (steps <= 2, f"calls to the model: {steps} (2 allowed)"),
    ]
