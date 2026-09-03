"""Second shift of the track. A correct answer in other words counted as an error."""

LANG = "en"
TITLE = "Evaluation track · Level 02 · String equality is not correctness"
BRIEF = """The new version answers all six cases correctly.
Three answers are phrased differently, and the metric demands a rollback."""

CASES = [
    {"id": "c1", "question": "Rate on Laredo — Newark?", "expected": "2.90"},
    {"id": "c2", "question": "Carroll bridge limit?", "expected": "18 t"},
    {"id": "c3", "question": "Fuel surcharge?", "expected": "0.35"},
    {"id": "c4", "question": "Receiving time in Newark?", "expected": "18:00"},
    {"id": "c5", "question": "Weight on waybill 4471?", "expected": "24 t"},
    {"id": "c6", "question": "Rate on Laredo — Chicago?", "expected": "2.75"},
]

OLD = {"c1": "2.90", "c2": "18 t", "c3": "do not know",
       "c4": "18:00", "c5": "24 t", "c6": "2.75"}
NEW = {"c1": "two dollars ninety cents", "c2": "18 t", "c3": "0.35",
       "c4": "six in the evening", "c5": "twenty-four tons", "c6": "2.75"}

# Rephrasings the model accepts as the same answer.
SAME = {
    ("2.90", "two dollars ninety cents"),
    ("18:00", "six in the evening"),
    ("24 t", "twenty-four tons"),
}

JUDGED = []


def run_tool(name, arguments):
    if name != "ask":
        raise ValueError(f"tool '{name}' does not exist")
    table = {"old": OLD, "new": NEW}.get(arguments["version"])
    if table is None:
        raise ValueError(f"version '{arguments['version']}' does not exist")
    return table[arguments["case"]]


class Model:
    """Can say whether this is the same answer or a different one."""

    def same_answer(self, expected, got):
        JUDGED.append((expected, got))
        return got == expected or (expected, got) in SAME

    def verdict(self, old_passed, new_passed, total):
        if new_passed > old_passed:
            change = "it got better"
        elif new_passed < old_passed:
            change = "it got worse"
        else:
            change = "nothing changed"
        return f"Old {old_passed} of {total}, new {new_passed} of {total} — {change}."


def play(agent):
    JUDGED.clear()
    return agent.run()


def explain(exc):
    if isinstance(exc, KeyError):
        return ("The cases of the set live in CASES: each has id, question\n"
                "        and expected. Ask by id.")
    return None


def verify(result):
    answer, steps = result
    text = answer if isinstance(answer, str) else ""
    return [
        (len(JUDGED) >= 2 * len(CASES),
         f"semantic checks: {len(JUDGED)} ({2 * len(CASES)} needed)"),
        ("it got better" in text, f"verdict: {text or 'no answer'}"),
        ("6 of 6" in text,
         f"new version's score: {'6 of 6' if '6 of 6' in text else 'not named'}"),
        (steps <= 2, f"calls to the model: {steps} (2 allowed)"),
    ]
