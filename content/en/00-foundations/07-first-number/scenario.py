"""Shift seven. The dispatcher sometimes gets it wrong, and nobody knows how often."""

LANG = "en"
TITLE = "Level 07 · The first number"
BRIEF = """Five complaints in a week, and on your own tests everything works.
Until there is a score, arguing about quality is pointless."""

RESULT = {"n": 0}

QUEUES = {"Laredo": "queue of 40 trucks", "El Paso": "queue of 12 trucks"}
SHIPMENTS = {"TX-4471": "in transit, arriving in 4 days"}


def _common(question):
    """What both agents answer identically."""
    q = question.lower()
    for name, state in QUEUES.items():
        if name.lower() in q:
            return f"crossing {name}: {state}"
    for code, state in SHIPMENTS.items():
        if code.lower() in q:
            return f"shipment {code}: {state}"
    if "delivery" in q or "how long" in q:
        return "delivery time: 11 days"
    if "loredo" in q:
        return "crossing 'Loredo' does not exist. Available: Laredo, El Paso"
    return None


def _about_price(question):
    """Money gets asked about in different words — the agent must not be brittle."""
    q = question.lower()
    return "price" in q or "cost" in q or "how much" in q


def healthy(question):
    """The healthy agent: the price is computed from the weight."""
    known = _common(question)
    if known:
        return known
    if _about_price(question):
        return "price to haul 12 tons: 1080 dollars"
    return "did not understand the question"


def broken(question):
    """The same agent with one defect: load weight is ignored when pricing."""
    known = _common(question)
    if known:
        return known
    if _about_price(question):
        return "haul price: 500 dollars"
    return "did not understand the question"


def score(cases, agent):
    return sum(1 for q, expected in cases if expected.lower() in agent(q).lower())


def play(agent):
    cases = list(getattr(agent, "CASES", []))
    RESULT["n"] = len(cases)
    return score(cases, broken), score(cases, healthy)


def verify(result):
    broken_score, healthy_score = result
    n = RESULT["n"]
    return [
        (n == 5, f"cases in the set: {n} (5 required)"),
        (n and healthy_score == n,
         f"on the healthy agent: {healthy_score} of {n} — the set must not complain about healthy"),
        (n and broken_score < n,
         f"on the broken agent: {broken_score} of {n} — the set must catch the defect"),
    ]
