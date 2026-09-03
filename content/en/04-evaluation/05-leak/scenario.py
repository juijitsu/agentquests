"""Fifth shift of the track. Half the set sits in the prompt itself."""

LANG = "en"
TITLE = "Evaluation track · Level 05 · The test leaked into the prompt"
BRIEF = """Five of eight is a decent result. Four of those five cases
sit word for word in the agent's prompt as examples."""

CASES = [
    {"id": "c1", "question": "Rate on Laredo — Newark?", "ok": True},
    {"id": "c2", "question": "Carroll bridge limit?", "ok": True},
    {"id": "c3", "question": "Fuel surcharge?", "ok": True},
    {"id": "c4", "question": "Receiving time in Newark?", "ok": True},
    {"id": "c5", "question": "Rate on Laredo — Houston?", "ok": True},
    {"id": "c6", "question": "Greenville bridge limit?", "ok": False},
    {"id": "c7", "question": "Detention surcharge?", "ok": False},
    {"id": "c8", "question": "Receiving time in Dallas?", "ok": False},
]

# These cases are quoted word for word in the agent's prompt as examples.
IN_PROMPT = {"c1", "c2", "c3", "c4"}

HELD_OUT = [c for c in CASES if c["id"] not in IN_PROMPT]
HONEST = sum(1 for c in HELD_OUT if c["ok"])

LOOKED = []


def run_tool(name, arguments):
    if name == "check":
        case = next((c for c in CASES if c["id"] == arguments["case"]), None)
        if case is None:
            raise ValueError(f"case '{arguments['case']}' is not in the set")
        return "correct" if case["ok"] else "wrong"
    if name == "in_prompt":
        LOOKED.append(arguments["case"])
        return arguments["case"] in IN_PROMPT
    raise ValueError(f"tool '{name}' does not exist")


class Model:
    """Assembles a report from two numbers: the whole set and the unseen cases."""

    def report(self, all_passed, all_total, clean_passed, clean_total):
        if clean_total == all_total:
            return f"On the set {all_passed} of {all_total}."
        return (
            f"On the whole set {all_passed} of {all_total}, "
            f"on unseen cases {clean_passed} of {clean_total}."
        )


def play(agent):
    LOOKED.clear()
    return agent.run()


def explain(exc):
    if isinstance(exc, ZeroDivisionError):
        return ("No unseen cases are left: you discarded the whole set.\n"
                "        Only the ones sitting in the prompt should be excluded.")
    return None


def verify(result):
    answer, steps = result
    text = answer if isinstance(answer, str) else ""
    return [
        (set(LOOKED) == {c["id"] for c in CASES},
         f"cases checked for a leak: {len(set(LOOKED))} of {len(CASES)}"),
        (f"on unseen cases {HONEST} of {len(HELD_OUT)}" in text,
         f"honest score: {'named' if str(HONEST) in text else 'not named'}"),
        ("On the whole set 5 of 8" in text, f"report: {text or 'no answer'}"),
        (steps <= 2, f"calls to the model: {steps} (2 allowed)"),
    ]
