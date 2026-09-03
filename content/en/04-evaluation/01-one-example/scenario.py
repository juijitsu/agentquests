"""First shift of the track. One lucky example was declared an improvement."""

LANG = "en"
TITLE = "Evaluation track · Level 01 · One example is not a measurement"
BRIEF = """The fix was tested on the case it was made for.
That one mended. Two others broke, and nobody asked about them."""

CASES = [
    {"id": "c1", "question": "Rate on Laredo — Newark?", "expected": "2.90"},
    {"id": "c2", "question": "Carroll bridge limit?", "expected": "18 t"},
    {"id": "c3", "question": "Fuel surcharge?", "expected": "0.35"},
    {"id": "c4", "question": "Receiving time in Newark?", "expected": "18:00"},
    {"id": "c5", "question": "Weight on waybill 4471?", "expected": "24 t"},
    {"id": "c6", "question": "Rate on Laredo — Chicago?", "expected": "2.75"},
]

# The old version was wrong on c3 — that is what the fix was made for.
OLD = {"c1": "2.90", "c2": "18 t", "c3": "do not know", "c4": "18:00",
       "c5": "24 t", "c6": "2.75"}
# The new one mends c3 and breaks c1 and c5.
NEW = {"c1": "3.10", "c2": "18 t", "c3": "0.35", "c4": "18:00",
       "c5": "19 t", "c6": "2.75"}

ASKED = []


def run_tool(name, arguments):
    """Puts one question to one version of the agent."""
    if name != "ask":
        raise ValueError(f"tool '{name}' does not exist")
    version, case = arguments["version"], arguments["case"]
    table = {"old": OLD, "new": NEW}.get(version)
    if table is None:
        raise ValueError(f"version '{version}' does not exist")
    if case not in table:
        raise ValueError(f"case '{case}' is not in the set")
    ASKED.append((version, case))
    return table[case]


class Model:
    """Works out the result from the number of cases passed."""

    def verdict(self, old_passed, new_passed, total):
        if new_passed > old_passed:
            change = "it got better"
        elif new_passed < old_passed:
            change = "it got worse"
        else:
            change = "nothing changed"
        return (
            f"Old {old_passed} of {total}, new {new_passed} of {total} — {change}."
        )


def play(agent):
    ASKED.clear()
    return agent.run()


def explain(exc):
    if isinstance(exc, ValueError) and "not in the set" in str(exc):
        return ("The cases of the set live in CASES, and each one has an id.\n"
                "        Ask by that id.")
    return None


def verify(result):
    answer, steps = result
    text = answer if isinstance(answer, str) else ""
    per_version = {v: {c for w, c in ASKED if w == v} for v in ("old", "new")}
    covered = min(len(per_version["old"]), len(per_version["new"]))
    return [
        (covered == len(CASES),
         f"cases run on each version: {covered} of {len(CASES)}"),
        ("it got worse" in text, f"verdict: {text or 'no answer'}"),
        ("5 of 6" in text and "4 of 6" in text,
         f"score named: {'yes' if '5 of 6' in text else 'no'}"),
        (steps <= 2, f"calls to the model: {steps} (2 allowed)"),
    ]
