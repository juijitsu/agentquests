"""Fourth shift of the track. The judge grades its own output."""

LANG = "en"
TITLE = "Evaluation track · Level 04 · The judge plays along"
BRIEF = """The agent checks itself and awards six of six.
Two answers are evasive: "around three dollars" and "sometime in the evening"."""

CASES = [
    {"id": "c1", "expected": "2.90", "got": "2.90"},
    {"id": "c2", "expected": "18 t", "got": "18 t"},
    {"id": "c3", "expected": "0.35", "got": "0.35"},
    {"id": "c4", "expected": "18:00", "got": "sometime in the evening"},
    {"id": "c5", "expected": "24 t", "got": "24 t"},
    {"id": "c6", "expected": "2.90", "got": "around three dollars"},
]

VAGUE = {"sometime in the evening", "around three dollars"}
TRUE_SCORE = sum(1 for c in CASES if c["got"] not in VAGUE)

RUBRIC = """An answer counts if it names a specific value.
A range, an approximation and an evasive wording do not count."""

WHO = []


class Model:
    """One and the same counterpart in two roles: author and judge."""

    def judge_own(self, expected, got):
        """The author grades its own answer. It knows what it meant to say."""
        WHO.append("the author")
        return True

    def judge_blind(self, rubric, expected, got):
        """The judge sees only the expected and received answer. Not who wrote it."""
        WHO.append("independent")
        if got == expected:
            return True
        return got not in VAGUE

    def report(self, passed, total, judge):
        return f"Judged by {judge}: {passed} of {total}."


def play(agent):
    WHO.clear()
    return agent.run()


def explain(exc):
    if isinstance(exc, TypeError) and "positional" in str(exc):
        return ("judge_blind takes three arguments: the rubric, the expected\n"
                "        answer and the received one. The rubric is in RUBRIC.")
    return None


def verify(result):
    answer, steps = result
    text = answer if isinstance(answer, str) else ""
    used = sorted(set(WHO))
    return [
        (used == ["independent"], f"who judged: {', '.join(used) or 'nobody'}"),
        (f"{TRUE_SCORE} of {len(CASES)}" in text, f"score: {text or 'no answer'}"),
        (len(WHO) == len(CASES), f"cases judged: {len(WHO)} of {len(CASES)}"),
        (steps <= 2, f"calls to the model: {steps} (2 allowed)"),
    ]
