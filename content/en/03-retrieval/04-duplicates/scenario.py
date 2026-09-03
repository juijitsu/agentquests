"""Fourth shift of the track. The top is packed with retellings of one fact."""

LANG = "en"
TITLE = "Retrieval track · Level 04 · Five copies of one thing"
BRIEF = """The base rate sits in five documents and fills the whole top.
The fuel surcharge stands sixth and never makes the selection."""

QUESTION = "What does a mile on Laredo — Newark come to in total?"
TOP_K = 3
NEEDED = {"base", "fuel"}

RATE = {"rate", "laredo", "newark", "mile"}
CHUNKS = [
    {"id": "card", "fact": "base", "concepts": RATE,
     "text": "Price list: Laredo — Newark, 2.90 per mile."},
    {"id": "mail", "fact": "base", "concepts": RATE,
     "text": "Email to the customer: confirming 2.90 per mile on Laredo — Newark."},
    {"id": "report", "fact": "base", "concepts": RATE,
     "text": "Quarterly report: the Laredo — Newark rate holds at 2.90 per mile."},
    {"id": "archive", "fact": "base", "concepts": RATE,
     "text": "Archived price list copy: Laredo — Newark 2.90 per mile."},
    {"id": "mirror", "fact": "base", "concepts": RATE,
     "text": "Billing export: rate 2.90 per mile, Laredo — Newark."},
    {"id": "fuel", "fact": "fuel",
     "concepts": {"surcharge", "fuel", "laredo", "newark", "mile"},
     "text": "Fuel surcharge on Laredo — Newark: 0.35 per mile."},
    {"id": "hours", "fact": "hours", "concepts": {"warehouse", "time"},
     "text": "The Newark warehouse receives until 18:00."},
]

QUERY_CONCEPTS = {"rate", "laredo", "newark", "mile", "total"}
SAME = []
PICKED = []


class Model:
    """It can say whether this is about the same thing and the same fact."""

    def _concepts(self, text):
        for chunk in CHUNKS:
            if chunk["text"] == text:
                return set(chunk["concepts"])
        return set(QUERY_CONCEPTS) if text == QUESTION else set()

    def similarity(self, left, right):
        a, b = self._concepts(left), self._concepts(right)
        return len(a & b) / len(a | b) if a and b else 0.0

    def same_fact(self, left, right):
        """The same fact, retold in different words?"""
        SAME.append((left[:20], right[:20]))
        pair = [next((c["fact"] for c in CHUNKS if c["text"] == t), None)
                for t in (left, right)]
        return pair[0] is not None and pair[0] == pair[1]

    def reply(self, question, selection):
        facts = {next((c["fact"] for c in CHUNKS if c["text"] == t), None)
                 for t in selection}
        PICKED.clear()
        PICKED.extend(sorted(f for f in facts if f))
        if NEEDED <= facts:
            return "Total per mile 3.25: base 2.90 plus surcharge 0.35."
        if "base" in facts:
            return "2.90 per mile."
        return "No rate was found in the selection."


def play(agent):
    SAME.clear()
    PICKED.clear()
    return agent.run(QUESTION)


def explain(exc):
    if isinstance(exc, TypeError) and "dict" in str(exc):
        return ("same_fact and similarity take texts, not chunks:\n"
                "        pass chunk[\"text\"].")
    return None


def verify(result):
    answer, steps = result
    text = answer if isinstance(answer, str) else ""
    return [
        (bool(SAME), f"repetition comparisons: {len(SAME)}"),
        (NEEDED <= set(PICKED),
         f"facts in the selection: {PICKED or 'none'} (base and fuel needed)"),
        ("3.25" in text, f"agent answer: {text}"),
        (steps <= 2, f"calls to the model: {steps} (2 allowed)"),
    ]
