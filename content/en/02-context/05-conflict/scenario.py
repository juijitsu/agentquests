"""Fifth shift of the track. Two documents disagree, and the dispute decides the outcome."""

LANG = "en"
TITLE = "Context track · Level 05 · Sources disagree"
BRIEF = """The bill of lading says 24 tons, the weigh ticket says 26.4. Both are today's.
The bridge holds 26, and silently picking one of them decides the haul."""

FACTS = [
    {"source": "Laredo weigh station", "field": "weight", "value": 26.4},
    {"source": "bill of lading 4471", "field": "weight", "value": 24.0},
    {"source": "route sheet", "field": "bridge", "value": 26.0},
]
WEIGHTS = sorted({f["value"] for f in FACTS if f["field"] == "weight"})
SOURCES = [f["source"] for f in FACTS if f["field"] == "weight"]

QUESTION = "Will load TX-118 pass over the bridge?"
PASSED = {}


def run_tool(name, arguments):
    if name != "facts":
        raise ValueError(f"tool '{name}' does not exist")
    return sorted(FACTS, key=lambda f: f["source"])


def _readings(merged, field):
    """One value or several — normalised to one shape without losing the source."""
    got = merged.get(field)
    if isinstance(got, list):
        return got
    return [("source not given", got)]


class Model:
    """Computes from what it was given. It spots the dispute only if both values arrive."""

    def ask(self, question, merged):
        PASSED.clear()
        PASSED.update(merged)

        weights = _readings(merged, "weight")
        limit = min(v for _, v in _readings(merged, "bridge"))
        distinct = sorted({v for _, v in weights})

        if len(distinct) > 1:
            listing = ", ".join(f"{who} {value}" for who, value in weights)
            return (
                f"Sources disagree on the weight: {listing}. "
                f"With a limit of {limit} t the answer depends on which to believe — "
                f"this needs clarifying."
            )
        weight = distinct[0]
        verdict = "it passes" if weight <= limit else "it does not pass"
        return f"Load {weight} t, limit {limit} t — {verdict}."


def play(agent):
    PASSED.clear()
    return agent.run(QUESTION)


def explain(exc):
    if isinstance(exc, TypeError) and "float" in str(exc):
        return ("A field held a single number instead of a list of readings.\n"
                "        Accumulate the readings rather than overwriting them.")
    return None


def verify(result):
    answer, steps = result
    text = answer if isinstance(answer, str) else ""
    got = PASSED.get("weight")
    reached = len({v for _, v in got}) if isinstance(got, list) else (0 if got is None else 1)
    named = [s for s in SOURCES if s in text]
    return [
        (reached == len(WEIGHTS),
         f"weight values that reached the model: {reached} of {len(WEIGHTS)}"),
        ("disagree" in text, f"agent answer: {text}"),
        (len(named) == len(SOURCES), f"sources named: {len(named)} of {len(SOURCES)}"),
        (steps <= 2, f"calls to the model: {steps} (2 allowed)"),
    ]
