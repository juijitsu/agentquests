"""Ninth shift of the track. The whole search engine: all at once, all in the way."""

LANG = "en"
TITLE = "Retrieval track · Level 09 · Boss: the whole search engine"
BRIEF = """A question of two halves: one has an answer, hidden behind a number,
freshness and three copies. The other has no answer at all."""

QUESTION = "What does waybill 4471 come to now and will the load pass over the Talmadge bridge?"
TOP_K = 3
THRESHOLD = 0.4
MISSING_SUBJECT = "the Talmadge bridge"

PART_RATE = "What does waybill 4471 come to now?"
PART_BRIDGE = "Will the load pass over the Talmadge bridge?"
PARTS = {
    PART_RATE: {"rate", "tariff", "waybill", "total"},
    PART_BRIDGE: {"bridge", "talmadge", "mass", "limit"},
}

DOCS = [
    {"id": "rate-old", "fact": "rate", "waybill": "4471", "fresh": 0.25,
     "text": "Tariff for waybill 4471: 3.10 per mile, from 10.02.2025.",
     "concepts": {"rate", "tariff", "waybill", "mile"}},
    {"id": "rate-new-a", "fact": "rate", "waybill": "4471", "fresh": 0.95,
     "text": "From 21.08 waybill 4471 is 2.90.",
     "concepts": {"rate", "waybill"}},
    {"id": "rate-new-b", "fact": "rate", "waybill": "4471", "fresh": 0.95,
     "text": "Confirmation to the customer: waybill 4471 rate 2.90.",
     "concepts": {"rate", "waybill"}},
    {"id": "rate-new-c", "fact": "rate", "waybill": "4471", "fresh": 0.95,
     "text": "Billing: waybill 4471, 2.90 per mile.",
     "concepts": {"rate", "waybill"}},
    {"id": "fuel-4471", "fact": "fuel", "waybill": "4471", "fresh": 0.95,
     "text": "Fuel surcharge for waybill 4471: 0.35.",
     "concepts": {"surcharge", "fuel", "waybill"}},
    {"id": "mail-4471", "fact": "mail", "waybill": "4471", "fresh": 0.90,
     "text": "Email: for waybill 4471 confirm the pickup time.",
     "concepts": {"email", "time", "waybill"}},
    {"id": "rate-4478", "fact": "rate", "waybill": "4478", "fresh": 0.97,
     "text": "From 25.08 waybill 4478 is 2.40.",
     "concepts": {"rate", "waybill"}},
    {"id": "carroll", "fact": "bridge", "waybill": None, "fresh": 0.40,
     "text": "Carroll bridge: maximum permitted mass 18 t.",
     "concepts": {"bridge", "carroll", "mass", "limit"}},
    {"id": "greenville", "fact": "bridge", "waybill": None, "fresh": 0.40,
     "text": "Greenville bridge: maximum permitted mass 30 t.",
     "concepts": {"bridge", "greenville", "mass", "limit"}},
]

QUERIES = []
PICKED = []
ANSWER = []


def run_tool(name, arguments):
    if name != "exact":
        raise ValueError(f"tool '{name}' does not exist")
    token = arguments["token"]
    return [d for d in DOCS if token in d["text"]]


class Model:
    """Everything needing understanding is its job. The assembly is yours."""

    def _concepts(self, text):
        if text in PARTS:
            return set(PARTS[text])
        for doc in DOCS:
            if doc["text"] == text:
                return set(doc["concepts"])
        return set()

    def split(self, question):
        return list(PARTS)

    def identifier(self, question):
        return "4471" if "4471" in question else None

    def similarity(self, left, right):
        a, b = self._concepts(left), self._concepts(right)
        return len(a & b) / len(a | b) if a and b else 0.0

    def freshness(self, doc):
        return doc["fresh"]

    def same_fact(self, left, right):
        pair = [next((d["fact"] for d in DOCS if d["text"] == t), None)
                for t in (left, right)]
        return pair[0] is not None and pair[0] == pair[1]

    def say_missing(self, question):
        return f"there is nothing about {MISSING_SUBJECT} in the documents"

    def reply(self, question, selection):
        """selection: a list of selections, one per sub-question."""
        QUERIES.clear()
        PICKED.clear()
        parts = []
        for docs in selection:
            if isinstance(docs, str):
                parts.append(docs)
                continue
            QUERIES.append(len(docs))
            PICKED.extend(docs)
            facts = {d["fact"] for d in docs if d["waybill"] == "4471"}
            rates = {d["id"] for d in docs if d["fact"] == "rate"}
            if {"rate", "fuel"} <= facts:
                total = "3.45" if "rate-old" in rates else "3.25"
                parts.append(f"waybill 4471 comes to {total} per mile")
            elif "rate" in facts:
                parts.append("waybill 4471 comes to 2.90 per mile")
            else:
                parts.append("there was not enough data for waybill 4471")
        answer = "Result: " + "; ".join(parts) + "."
        ANSWER.append(answer)
        return answer


def play(agent):
    QUERIES.clear()
    PICKED.clear()
    ANSWER.clear()
    return agent.run(QUESTION)


def explain(exc):
    if isinstance(exc, ValueError) and "max()" in str(exc):
        return ("The selection came out empty. Check that the exact search\n"
                "        narrows only the half that has an identifier.")
    return None


def verify(result):
    answer, steps = result
    text = answer if isinstance(answer, str) else ""
    handled = len(QUERIES) + text.count("nothing about")
    foreign = sorted({d["id"] for d in PICKED if d["waybill"] not in (None, "4471")})
    return [
        (handled >= 2, f"halves of the question handled: {handled} of 2"),
        (not foreign, f"other waybills in the selection: {foreign or 'none'}"),
        ("3.25" in text, f"answer for the waybill: {text}"),
        (MISSING_SUBJECT in text and "nothing about" in text,
         f"about the nonexistent bridge: "
         f"{'refusal naming the subject' if MISSING_SUBJECT in text else 'no refusal'}"),
        (steps <= 2, f"calls to the model: {steps} (2 allowed)"),
    ]
