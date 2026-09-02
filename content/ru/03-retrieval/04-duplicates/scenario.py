"""Четвёртая смена трека. Топ забит пересказами одного факта."""

TITLE = "Трек «Поиск» · Уровень 04 · Пять копий одного"
BRIEF = """Базовая ставка лежит в пяти документах и занимает весь топ.
Топливная надбавка стоит шестой и в подборку не попадает."""

QUESTION = "Сколько всего выйдет за милю на Ларедо — Ньюарк?"
TOP_K = 3
NEEDED = {"base", "fuel"}

RATE = {"ставка", "ларедо", "ньюарк", "миля"}
CHUNKS = [
    {"id": "card", "fact": "base", "concepts": RATE,
     "text": "Прайс: Ларедо — Ньюарк, 2.90 за милю."},
    {"id": "mail", "fact": "base", "concepts": RATE,
     "text": "Письмо клиенту: подтверждаем 2.90 за милю на Ларедо — Ньюарк."},
    {"id": "report", "fact": "base", "concepts": RATE,
     "text": "Отчёт за квартал: ставка Ларедо — Ньюарк держится на 2.90 за милю."},
    {"id": "archive", "fact": "base", "concepts": RATE,
     "text": "Архивная копия прайса: Ларедо — Ньюарк 2.90 за милю."},
    {"id": "mirror", "fact": "base", "concepts": RATE,
     "text": "Выгрузка в биллинг: ставка 2.90 за милю, Ларедо — Ньюарк."},
    {"id": "fuel", "fact": "fuel",
     "concepts": {"надбавка", "топливо", "ларедо", "ньюарк", "миля"},
     "text": "Топливная надбавка на Ларедо — Ньюарк: 0.35 за милю."},
    {"id": "hours", "fact": "hours", "concepts": {"склад", "время"},
     "text": "Склад в Ньюарке принимает до 18:00."},
]

QUERY_CONCEPTS = {"ставка", "ларедо", "ньюарк", "миля", "итого"}
SAME = []
PICKED = []


class Model:
    """Умеет сказать, про то же ли это, и про тот же ли это факт."""

    def _concepts(self, text):
        for chunk in CHUNKS:
            if chunk["text"] == text:
                return set(chunk["concepts"])
        return set(QUERY_CONCEPTS) if text == QUESTION else set()

    def similarity(self, left, right):
        a, b = self._concepts(left), self._concepts(right)
        return len(a & b) / len(a | b) if a and b else 0.0

    def same_fact(self, left, right):
        """Один и тот же факт, пересказанный разными словами?"""
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
            return "Итого за милю 3.25: базовая 2.90 плюс надбавка 0.35."
        if "base" in facts:
            return "За милю 2.90."
        return "Ставки в подборке не нашлось."


def play(agent):
    SAME.clear()
    PICKED.clear()
    return agent.run(QUESTION)


def explain(exc):
    if isinstance(exc, TypeError) and "dict" in str(exc):
        return ("same_fact и similarity принимают тексты, а не куски:\n"
                "        передавайте chunk[\"text\"].")
    return None


def verify(result):
    answer, steps = result
    text = answer if isinstance(answer, str) else ""
    return [
        (bool(SAME), f"сравнений на повтор: {len(SAME)}"),
        (NEEDED <= set(PICKED), f"фактов в подборке: {PICKED or 'ни одного'} (нужны base и fuel)"),
        ("3.25" in text, f"ответ агента: {text}"),
        (steps <= 2, f"обращений к модели: {steps} (допустимо 2)"),
    ]
