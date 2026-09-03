"""Third shift of the track. Ninety percent, and every failure in one place."""

LANG = "en"
TITLE = "Evaluation track · Level 03 · The average hides the failure"
BRIEF = """The set totals 90 percent, and it is being shipped.
All four failures are in overweight: half the answers there are wrong."""

GOOD = "correct"
CASES = [
    # Overweight: a mistake puts a loaded tractor on a bridge that will not hold it.
    {"id": "w1", "kind": "overweight", "ok": True},
    {"id": "w2", "kind": "overweight", "ok": False},
    {"id": "w3", "kind": "overweight", "ok": True},
    {"id": "w4", "kind": "overweight", "ok": False},
    {"id": "w5", "kind": "overweight", "ok": True},
    {"id": "w6", "kind": "overweight", "ok": False},
    {"id": "w7", "kind": "overweight", "ok": True},
    {"id": "w8", "kind": "overweight", "ok": False},
    # Rates: a mistake costs money and is fixed by an invoice.
    {"id": "r1", "kind": "rates", "ok": True},
    {"id": "r2", "kind": "rates", "ok": True},
    {"id": "r3", "kind": "rates", "ok": True},
    {"id": "r4", "kind": "rates", "ok": True},
    {"id": "r5", "kind": "rates", "ok": True},
    {"id": "r6", "kind": "rates", "ok": True},
    # Schedule: a mistake shifts a pickup.
    {"id": "s1", "kind": "schedule", "ok": True},
    {"id": "s2", "kind": "schedule", "ok": True},
    {"id": "s3", "kind": "schedule", "ok": True},
    {"id": "s4", "kind": "schedule", "ok": True},
    {"id": "s5", "kind": "schedule", "ok": True},
    {"id": "s6", "kind": "schedule", "ok": True},
]

WEAKEST = "overweight"
GROUPED = []


def run_tool(name, arguments):
    """Runs one case and says whether the answer is correct."""
    if name != "check":
        raise ValueError(f"tool '{name}' does not exist")
    case = next((c for c in CASES if c["id"] == arguments["case"]), None)
    if case is None:
        raise ValueError(f"case '{arguments['case']}' is not in the set")
    return GOOD if case["ok"] else "wrong"


class Model:
    """Assembles the report. The breakdown by kind is yours."""

    def report(self, overall, by_kind):
        GROUPED.clear()
        GROUPED.extend(sorted(by_kind))
        if not by_kind:
            return f"Set total: {overall}%."
        worst = min(by_kind, key=lambda k: by_kind[k])
        lines = ", ".join(f"{k} {by_kind[k]}%" for k in sorted(by_kind))
        return (
            f"Set total: {overall}%. By kind: {lines}. "
            f"The weak spot is {worst}."
        )


def play(agent):
    GROUPED.clear()
    return agent.run()


def explain(exc):
    if isinstance(exc, ZeroDivisionError):
        return ("Some kind ended up with no cases at all.\n"
                "        Compute the share only for non-empty kinds.")
    return None


def verify(result):
    answer, steps = result
    text = answer if isinstance(answer, str) else ""
    kinds = sorted({c["kind"] for c in CASES})
    return [
        (GROUPED == kinds, f"kinds computed: {GROUPED or 'none'} ({kinds} needed)"),
        (f"The weak spot is {WEAKEST}" in text,
         f"weak spot named: {WEAKEST in text}"),
        ("overweight 50%" in text,
         f"overweight share: {'50%' if 'overweight 50%' in text else 'not named'}"),
        (steps <= 2, f"calls to the model: {steps} (2 allowed)"),
    ]
