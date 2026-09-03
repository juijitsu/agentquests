"""Second shift of the track. Found about the very thing — and with no answer."""

LANG = "en"
TITLE = "Retrieval track · Level 02 · Similar is not useful"
BRIEF = """The most similar document is a policy on how a rate is formed.
About the very thing, in the same words, and not one number."""

QUESTION = "What does a mile cost on Laredo — Newark?"
ANSWER_ID = "rate-card"

DOCS = [
    {
        "id": "rate-policy",
        "text": "How a rate is formed: base plus surcharges, revised quarterly.",
        "concepts": {"rate", "laredo", "newark", "mile", "policy"},
        "value": None,
    },
    {
        "id": "rate-card",
        "text": "Laredo — Newark: 2.90 per mile.",
        "concepts": {"rate", "laredo", "newark"},
        "value": "2.90",
    },
    {
        "id": "other-lane",
        "text": "Laredo — Chicago: 2.75 per mile.",
        "concepts": {"rate", "laredo", "chicago"},
        "value": "2.75",
    },
    {
        "id": "fuel-surcharge",
        "text": "The fuel surcharge is revised on Wednesdays.",
        "concepts": {"surcharge", "fuel", "policy"},
        "value": None,
    },
]

QUERY_CONCEPTS = {"rate", "laredo", "newark", "mile"}
CHECKED = []
FOUND = []


class Model:
    """Similarity and fitness are two different questions and two methods."""

    def embed(self, text):
        if text == QUESTION:
            return set(QUERY_CONCEPTS)
        for doc in DOCS:
            if doc["text"] == text:
                return set(doc["concepts"])
        return set()

    def similarity(self, left, right):
        a, b = self.embed(left), self.embed(right)
        return len(a & b) / len(a | b) if a and b else 0.0

    def answers(self, question, doc):
        """Whether the document holds what is asked for, not what it is about."""
        CHECKED.append(doc["id"])
        return doc["value"] is not None and "newark" in doc["concepts"]

    def reply(self, question, doc):
        FOUND.append(doc["id"])
        if doc["value"] is None:
            return f"From the document found: {doc['text']}"
        return f"The rate is {doc['value']} per mile."


def play(agent):
    CHECKED.clear()
    FOUND.clear()
    return agent.run(QUESTION)


def explain(exc):
    if isinstance(exc, ValueError) and "max() " in str(exc):
        return ("Not one document passed the fitness check.\n"
                "        Check the candidates, but do not throw them all away.")
    return None


def verify(result):
    answer, steps = result
    text = answer if isinstance(answer, str) else ""
    return [
        (bool(CHECKED), f"candidates checked for fitness: {len(CHECKED)}"),
        (FOUND == [ANSWER_ID], f"document chosen: {FOUND[0] if FOUND else 'none'}"),
        ("2.90" in text, f"agent answer: {text}"),
        (steps <= 2, f"calls to the model: {steps} (2 allowed)"),
    ]
