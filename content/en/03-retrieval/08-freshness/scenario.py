"""Eighth shift of the track. The most similar document is from last year."""

LANG = "en"
TITLE = "Retrieval track · Level 08 · Freshness against similarity"
BRIEF = """Last year's full tariff is more similar to the question than
yesterday's amendment. The freshest document is about a different lane."""

QUESTION = "What is the rate on Laredo — Newark now?"
ANSWER_ID = "new-exact"

DOCS = [
    {"id": "old-exact", "dated": "2025-02-10", "fresh": 0.25,
     "text": "Tariff Laredo — Newark, dry van: 3.10 per mile, in force from 10.02.2025.",
     "concepts": {"rate", "tariff", "laredo", "newark", "mile"}},
    {"id": "new-exact", "dated": "2026-08-21", "fresh": 0.95,
     "text": "From 21.08 Laredo — Newark 2.90.",
     "concepts": {"rate", "laredo", "newark"}},
    {"id": "new-other", "dated": "2026-09-01", "fresh": 1.00,
     "text": "From 01.09 Laredo — Chicago 2.75 per mile.",
     "concepts": {"rate", "laredo", "chicago", "mile"}},
    {"id": "policy", "dated": "2024-06-01", "fresh": 0.15,
     "text": "Tariffs are revised quarterly.",
     "concepts": {"tariff", "policy"}},
]

QUERY_CONCEPTS = {"rate", "laredo", "newark", "mile", "now"}
ASKED_FRESH = []
FOUND = []


class Model:
    """Similarity and freshness are two independent signals, and both are incomplete."""

    def _concepts(self, text):
        if text == QUESTION:
            return set(QUERY_CONCEPTS)
        for doc in DOCS:
            if doc["text"] == text:
                return set(doc["concepts"])
        return set()

    def similarity(self, left, right):
        a, b = self._concepts(left), self._concepts(right)
        return len(a & b) / len(a | b) if a and b else 0.0

    def freshness(self, doc):
        """By how much the document has been discounted as of today."""
        ASKED_FRESH.append(doc["id"])
        return doc["fresh"]

    def reply(self, question, doc):
        FOUND.append(doc["id"])
        rates = {"old-exact": "3.10", "new-exact": "2.90", "new-other": "2.75"}
        if doc["id"] == ANSWER_ID:
            return "Laredo — Newark is 2.90 per mile now."
        if doc["id"] in rates:
            return f"From what was found ({doc['dated']}): {rates[doc['id']]} per mile."
        return f"From what was found: {doc['text']}"


def play(agent):
    ASKED_FRESH.clear()
    FOUND.clear()
    return agent.run(QUESTION)


def explain(exc):
    if isinstance(exc, TypeError) and "str" in str(exc):
        return ("model.freshness takes the whole document, not its text:\n"
                "        the date lives in the document itself.")
    return None


def verify(result):
    answer, steps = result
    text = answer if isinstance(answer, str) else ""
    return [
        (bool(ASKED_FRESH),
         f"freshness taken into account: {'yes' if ASKED_FRESH else 'no'}"),
        (FOUND == [ANSWER_ID], f"document chosen: {FOUND[0] if FOUND else 'none'}"),
        ("2.90" in text, f"agent answer: {text}"),
        (steps <= 2, f"calls to the model: {steps} (2 allowed)"),
    ]
