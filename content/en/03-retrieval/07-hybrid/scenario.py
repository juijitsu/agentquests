"""Seventh shift of the track. A number has no meaning — it has identity."""

LANG = "en"
TITLE = "Retrieval track · Level 07 · Hybrid: a number and a meaning"
BRIEF = """Waybills 4471 and 4478 are alike to meaning, and the agent answers
with somebody else's cargo weight. Exact search on its own misses too."""

QUESTION = "What weight is stated on waybill 4471?"
TOKEN = "4471"
ANSWER_ID = "wb-4471"

CARGO = {"waybill", "cargo", "weight"}
DOCS = [
    {"id": "wb-4478", "text": "Waybill 4478: pipe, 19 t.", "concepts": CARGO},
    {"id": "wb-4471", "text": "Waybill 4471: sheet glass, 24 t.", "concepts": CARGO},
    {"id": "wb-4502", "text": "Waybill 4502: pallets, 12 t.", "concepts": CARGO},
    {"id": "mail-4471", "text": "Email: for waybill 4471 confirm the pickup time.",
     "concepts": {"email", "time", "waybill"}},
    {"id": "pay-4471", "text": "Payment for waybill 4471 arrived on 2 September.",
     "concepts": {"payment", "waybill"}},
]

QUERY_CONCEPTS = {"waybill", "cargo", "weight"}
EXACT = []
SEMANTIC = []
FOUND = []


def run_tool(name, arguments):
    """Exact search: a literal substring occurrence, no meaning at all."""
    if name != "exact":
        raise ValueError(f"tool '{name}' does not exist")
    token = arguments["token"]
    EXACT.append(token)
    return [d for d in DOCS if token in d["text"]]


class Model:
    """Understands meaning and can tell an identifier from a word."""

    def _concepts(self, text):
        if text == QUESTION:
            return set(QUERY_CONCEPTS)
        for doc in DOCS:
            if doc["text"] == text:
                return set(doc["concepts"])
        return set()

    def similarity(self, left, right):
        SEMANTIC.append(right[:24])
        a, b = self._concepts(left), self._concepts(right)
        return len(a & b) / len(a | b) if a and b else 0.0

    def identifier(self, question):
        """What in the question is an identifier rather than a concept."""
        return TOKEN if TOKEN in question else None

    def reply(self, question, doc):
        FOUND.append(doc["id"])
        weights = {"wb-4471": "24 t", "wb-4478": "19 t", "wb-4502": "12 t"}
        if doc["id"] in weights:
            number = doc["text"].split()[1].rstrip(":")
            return f"On waybill {number}: {weights[doc['id']]}."
        return f"From what was found: {doc['text']}"


def play(agent):
    EXACT.clear()
    SEMANTIC.clear()
    FOUND.clear()
    return agent.run(QUESTION)


def explain(exc):
    if isinstance(exc, ValueError) and "max()" in str(exc):
        return ("The exact search found nothing. Check that you are searching\n"
                "        for the identifier from the question, not the whole question.")
    return None


def verify(result):
    answer, steps = result
    text = answer if isinstance(answer, str) else ""
    both = bool(EXACT) and bool(SEMANTIC)
    return [
        (both,
         f"signals: exact — {'yes' if EXACT else 'no'}, semantic — {'yes' if SEMANTIC else 'no'}"),
        (FOUND == [ANSWER_ID], f"document chosen: {FOUND[0] if FOUND else 'none'}"),
        ("24 t" in text, f"agent answer: {text}"),
        (steps <= 2, f"calls to the model: {steps} (2 allowed)"),
    ]
