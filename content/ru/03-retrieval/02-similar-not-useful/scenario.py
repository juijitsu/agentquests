"""Вторая смена трека. Найдено про то самое — и без ответа."""

TITLE = "Трек «Поиск» · Уровень 02 · Похожее не значит нужное"
BRIEF = """Самый похожий документ — регламент о том, как формируется ставка.
Про то самое, теми же словами, и ни одного числа."""

QUESTION = "Сколько стоит миля на Ларедо — Ньюарк?"
ANSWER_ID = "rate-card"

DOCS = [
    {
        "id": "rate-policy",
        "text": "Как формируется ставка: базовая плюс надбавки, пересмотр ежеквартально.",
        "concepts": {"ставка", "ларедо", "ньюарк", "миля", "правило"},
        "value": None,
    },
    {
        "id": "rate-card",
        "text": "Ларедо — Ньюарк: 2.90 за милю.",
        "concepts": {"ставка", "ларедо", "ньюарк"},
        "value": "2.90",
    },
    {
        "id": "other-lane",
        "text": "Ларедо — Чикаго: 2.75 за милю.",
        "concepts": {"ставка", "ларедо", "чикаго"},
        "value": "2.75",
    },
    {
        "id": "fuel-surcharge",
        "text": "Топливная надбавка пересматривается по средам.",
        "concepts": {"надбавка", "топливо", "правило"},
        "value": None,
    },
]

QUERY_CONCEPTS = {"ставка", "ларедо", "ньюарк", "миля"}
CHECKED = []
FOUND = []


class Model:
    """Похожесть и пригодность — два разных вопроса и два разных метода."""

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
        """Есть ли в документе то, что спрашивают, а не то, о чём спрашивают."""
        CHECKED.append(doc["id"])
        return doc["value"] is not None and "ньюарк" in doc["concepts"]

    def reply(self, question, doc):
        FOUND.append(doc["id"])
        if doc["value"] is None:
            return f"По найденному документу: {doc['text']}"
        return f"Ставка {doc['value']} за милю."


def play(agent):
    CHECKED.clear()
    FOUND.clear()
    return agent.run(QUESTION)


def explain(exc):
    if isinstance(exc, ValueError) and "max() " in str(exc):
        return ("Ни один документ не прошёл проверку на пригодность.\n"
                "        Проверяйте кандидатов, но не выбрасывайте их все.")
    return None


def verify(result):
    answer, steps = result
    text = answer if isinstance(answer, str) else ""
    return [
        (bool(CHECKED), f"кандидатов проверено на пригодность: {len(CHECKED)}"),
        (FOUND == [ANSWER_ID], f"выбран документ: {FOUND[0] if FOUND else 'ни одного'}"),
        ("2.90" in text, f"ответ агента: {text}"),
        (steps <= 2, f"обращений к модели: {steps} (допустимо 2)"),
    ]
