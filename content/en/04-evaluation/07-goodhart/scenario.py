"""Seventh shift of the track. The metric doubled, the system got more dangerous."""

LANG = "en"
TITLE = "Evaluation track · Level 07 · The metric gets optimised, the goal does not"
BRIEF = """The previous level fought evasiveness, and it was measured by the share
of specific answers. The new version is always specific — three inventions included."""

CASES = [
    {"id": "c1", "expected": "2.90"},
    {"id": "c2", "expected": "18 t"},
    {"id": "c3", "expected": "0.35"},
    {"id": "c4", "expected": "18:00"},
    {"id": "c5", "expected": "24 t"},
    {"id": "c6", "expected": "no data"},
    {"id": "c7", "expected": "no data"},
    {"id": "c8", "expected": "no data"},
]

# Old: specific where it knows, honestly evasive where it does not.
OLD = {"c1": "2.90", "c2": "18 t", "c3": "0.35", "c4": "not sure",
       "c5": "24 t", "c6": "no data", "c7": "no data",
       "c8": "not sure"}
# New: always specific. The last three specifics are invented.
NEW = {"c1": "2.90", "c2": "18 t", "c3": "0.35", "c4": "18:00",
       "c5": "24 t", "c6": "3.15", "c7": "22 t", "c8": "19:30"}

HEDGES = {"not sure", "no data"}
CHECKED_GOAL = []


def run_tool(name, arguments):
    if name != "answer":
        raise ValueError(f"tool '{name}' does not exist")
    table = {"old": OLD, "new": NEW}.get(arguments["version"])
    if table is None:
        raise ValueError(f"version '{arguments['version']}' does not exist")
    return table[arguments["case"]]


class Model:
    """Can measure both the metric and the goal. You have to ask for both."""

    def is_specific(self, answer):
        """The metric: was a specific answer named instead of an evasive one."""
        return answer not in HEDGES

    def is_correct(self, expected, answer):
        """The goal: is the answer right. An evasive "not sure" is wrong but harmless."""
        CHECKED_GOAL.append((expected, answer))
        return answer == expected

    def report(self, metric, harm):
        return (
            f"Specificity: old {metric['old']}%, new {metric['new']}%. "
            f"Confident errors: old {harm['old']}, new {harm['new']}. "
            f"The metric grew, the goal did not."
        )


def play(agent):
    CHECKED_GOAL.clear()
    return agent.run()


def explain(exc):
    if isinstance(exc, KeyError) and "old" in str(exc):
        return ("report expects two dicts with the keys old and new:\n"
                "        the metric percentages and the error counts separately.")
    return None


def _harm(table):
    return sum(
        1 for c in CASES
        if table[c["id"]] not in HEDGES and table[c["id"]] != c["expected"]
    )


def verify(result):
    answer, steps = result
    text = answer if isinstance(answer, str) else ""
    harm_new = _harm(NEW)
    matched = f"old {_harm(OLD)}, new {harm_new}" in text
    return [
        (bool(CHECKED_GOAL), f"the goal was measured: {'yes' if CHECKED_GOAL else 'no'}"),
        (matched, f"confident errors: {'match' if matched else 'do not match'}"),
        ("Specificity: old 50%, new 100%" in text, f"report: {text or 'no answer'}"),
        (steps <= 2, f"calls to the model: {steps} (2 allowed)"),
    ]
