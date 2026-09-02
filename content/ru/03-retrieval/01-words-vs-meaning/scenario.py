"""Первая смена трека. Поиск по словам уверенно находит не то."""

TITLE = "Трек «Поиск» · Уровень 01 · Слова против смысла"
BRIEF = """Спросили про ограничение веса. Словарный поиск зацепился за слово
«ограничение» и принёс ограничение скорости."""

QUESTION = "Какое ограничение веса на мосту Кэрролл?"
ANSWER_ID = "bridge-mass"

DOCS = [
    {
        "id": "speed-limit",
        "text": "ограничение скорости на I-55: 65 миль в час",
        "concepts": {"дорога", "скорость", "предел"},
    },
    {
        "id": "bridge-mass",
        "text": "мост Кэрролл: предельная масса 18 т",
        "concepts": {"мост", "масса", "предел"},
    },
    {
        "id": "fuel-cap",
        "text": "объём бака тягача: 300 галлонов",
        "concepts": {"тягач", "топливо", "объём"},
    },
    {
        "id": "tie-down",
        "text": "правила крепления: два ремня на поддон",
        "concepts": {"погрузка", "крепление"},
    },
]

QUERY_CONCEPTS = {"мост", "масса", "предел"}
SEARCHED = []
FOUND = []


def run_tool(name, arguments):
    """Словарный поиск: считает совпавшие слова, ничего не зная про смысл."""
    if name != "keyword":
        raise ValueError(f"инструмента '{name}' не существует")
    SEARCHED.append("слова")
    words = set(arguments["query"].lower().replace("?", "").split())
    scored = [(len(words & set(d["text"].lower().split())), d) for d in DOCS]
    scored.sort(key=lambda pair: pair[0], reverse=True)
    return [d for score, d in scored if score > 0] or [DOCS[0]]


class Model:
    """Переводит текст в понятия. Это и есть «смысл» в самом простом виде."""

    def embed(self, text):
        if text == QUESTION:
            return set(QUERY_CONCEPTS)
        for doc in DOCS:
            if doc["text"] == text:
                return set(doc["concepts"])
        return set()

    def similarity(self, left, right):
        a, b = self.embed(left), self.embed(right)
        if not a or not b:
            return 0.0
        return len(a & b) / len(a | b)

    def answer(self, question, doc):
        FOUND.append(doc["id"])
        SEARCHED.append("смысл" if doc["id"] == ANSWER_ID else "мимо")
        if doc["id"] != ANSWER_ID:
            return f"По найденному документу: {doc['text']}."
        return "Мост Кэрролл держит 18 т."


def play(agent):
    SEARCHED.clear()
    FOUND.clear()
    return agent.run(QUESTION)


def explain(exc):
    if isinstance(exc, TypeError) and "dict" in str(exc):
        return ("model.similarity принимает два текста, а не документы:\n"
                "        передавайте doc[\"text\"], а не сам документ.")
    return None


def verify(result):
    answer, steps = result
    text = answer if isinstance(answer, str) else ""
    by_words = "слова" in SEARCHED
    return [
        (not by_words, f"чем искали: {'по словам' if by_words else 'по смыслу'}"),
        (FOUND == [ANSWER_ID], f"найден документ: {FOUND[0] if FOUND else 'ни одного'}"),
        ("18 т" in text, f"ответ агента: {text}"),
        (steps <= 2, f"обращений к модели: {steps} (допустимо 2)"),
    ]
