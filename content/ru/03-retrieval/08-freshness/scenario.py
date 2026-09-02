"""Восьмая смена трека. Самый похожий документ — прошлогодний."""

TITLE = "Трек «Поиск» · Уровень 08 · Свежесть против похожести"
BRIEF = """Полный тариф прошлого года похож на вопрос сильнее, чем вчерашняя
правка. Самый свежий документ — про другое направление."""

QUESTION = "Какая сейчас ставка на Ларедо — Ньюарк?"
ANSWER_ID = "new-exact"

DOCS = [
    {"id": "old-exact", "dated": "2025-02-10", "fresh": 0.25,
     "text": "Тариф Ларедо — Ньюарк, сухогруз: 3.10 за милю, действует с 10.02.2025.",
     "concepts": {"ставка", "тариф", "ларедо", "ньюарк", "миля"}},
    {"id": "new-exact", "dated": "2026-08-21", "fresh": 0.95,
     "text": "С 21.08 Ларедо — Ньюарк 2.90.",
     "concepts": {"ставка", "ларедо", "ньюарк"}},
    {"id": "new-other", "dated": "2026-09-01", "fresh": 1.00,
     "text": "С 01.09 Ларедо — Чикаго 2.75 за милю.",
     "concepts": {"ставка", "ларедо", "чикаго", "миля"}},
    {"id": "policy", "dated": "2024-06-01", "fresh": 0.15,
     "text": "Тарифы пересматриваются ежеквартально.",
     "concepts": {"тариф", "правило"}},
]

QUERY_CONCEPTS = {"ставка", "ларедо", "ньюарк", "миля", "сейчас"}
ASKED_FRESH = []
FOUND = []


class Model:
    """Похожесть и свежесть — два независимых сигнала, и оба неполны."""

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
        """Во сколько раз документ обесценился к сегодняшнему дню."""
        ASKED_FRESH.append(doc["id"])
        return doc["fresh"]

    def reply(self, question, doc):
        FOUND.append(doc["id"])
        rates = {"old-exact": "3.10", "new-exact": "2.90", "new-other": "2.75"}
        if doc["id"] == ANSWER_ID:
            return "Сейчас на Ларедо — Ньюарк 2.90 за милю."
        if doc["id"] in rates:
            return f"По найденному ({doc['dated']}): {rates[doc['id']]} за милю."
        return f"По найденному: {doc['text']}"


def play(agent):
    ASKED_FRESH.clear()
    FOUND.clear()
    return agent.run(QUESTION)


def explain(exc):
    if isinstance(exc, TypeError) and "str" in str(exc):
        return ("model.freshness принимает документ целиком, а не его текст:\n"
                "        дата лежит в самом документе.")
    return None


def verify(result):
    answer, steps = result
    text = answer if isinstance(answer, str) else ""
    return [
        (bool(ASKED_FRESH), f"свежесть учтена: {'да' if ASKED_FRESH else 'нет'}"),
        (FOUND == [ANSWER_ID], f"выбран документ: {FOUND[0] if FOUND else 'ни одного'}"),
        ("2.90" in text, f"ответ агента: {text}"),
        (steps <= 2, f"обращений к модели: {steps} (допустимо 2)"),
    ]
