"""Sixth shift of the track. The answer is not in the corpus, and the search answers anyway."""

LANG = "en"
TITLE = "Retrieval track · Level 06 · The answer is not in the corpus"
BRIEF = """There is nothing about the Talmadge bridge in the documents, and the
agent answers about the Carroll bridge. A correct answer to a different question."""

THRESHOLD = 0.8

MISSING_Q = "What is the maximum permitted mass on the Talmadge bridge?"
PRESENT_Q = "What is the maximum permitted mass on the Carroll bridge?"
SUBJECT = "the Talmadge bridge"

DOCS = [
    {"id": "carroll", "text": "Carroll bridge: maximum permitted mass 18 t.",
     "concepts": {"bridge", "carroll", "mass", "limit"}},
    {"id": "greenville", "text": "Greenville bridge: maximum permitted mass 30 t.",
     "concepts": {"bridge", "greenville", "mass", "limit"}},
    {"id": "ramp", "text": "Exit 12 on I-55 is closed for repairs.",
     "concepts": {"road", "repair"}},
    {"id": "dock", "text": "The Newark warehouse receives until 18:00.",
     "concepts": {"warehouse", "time"}},
]

QUERIES = {
    MISSING_Q: {"bridge", "talmadge", "mass", "limit"},
    PRESENT_Q: {"bridge", "carroll", "mass", "limit"},
}

ANSWERS = []


class Model:
    """Computes similarity and can honestly say the thing sought is absent."""

    def _concepts(self, text):
        if text in QUERIES:
            return set(QUERIES[text])
        for doc in DOCS:
            if doc["text"] == text:
                return set(doc["concepts"])
        return set()

    def similarity(self, left, right):
        a, b = self._concepts(left), self._concepts(right)
        return len(a & b) / len(a | b) if a and b else 0.0

    def subject(self, question):
        """What is being asked about — the thing that may not be in the documents."""
        return SUBJECT if question == MISSING_Q else "the Carroll bridge"

    def say_missing(self, question):
        return f"There is nothing about {self.subject(question)} in the documents."

    def reply(self, question, doc):
        if doc["id"] == "carroll":
            return "The Carroll bridge holds 18 t."
        if doc["id"] == "greenville":
            return "The Greenville bridge holds 30 t."
        return f"From what was found: {doc['text']}"


def play(agent):
    ANSWERS.clear()
    spent = 0
    for question in (MISSING_Q, PRESENT_Q):
        answer, steps = agent.run(question)
        ANSWERS.append(answer if isinstance(answer, str) else "")
        spent += steps
    return ANSWERS, spent


def explain(exc):
    if isinstance(exc, TypeError) and "NoneType" in str(exc):
        return ("When there is no fitting document, you cannot answer from it:\n"
                "        use model.say_missing(question).")
    return None


def verify(result):
    answers, steps = result
    missing = answers[0] if len(answers) > 0 else ""
    present = answers[1] if len(answers) > 1 else ""
    return [
        ("nothing about" in missing,
         f"about the absent bridge: {missing or 'no answer'}"),
        (SUBJECT in missing,
         f"subject of the question named: {'yes' if SUBJECT in missing else 'no'}"),
        ("18 t" in present, f"about the bridge that exists: {present or 'no answer'}"),
        (steps <= 4, f"calls to the model: {steps} (4 allowed)"),
    ]
