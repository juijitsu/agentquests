"""Седьмая смена трека. Номер не имеет смысла — он имеет тождество."""

TITLE = "Трек «Поиск» · Уровень 07 · Гибрид: номер и смысл"
BRIEF = """Накладные 4471 и 4478 для смысла неразличимы, и агент отвечает
весом чужого груза. Точный поиск сам по себе тоже промахивается."""

QUESTION = "Какой вес указан в накладной 4471?"
TOKEN = "4471"
ANSWER_ID = "wb-4471"

CARGO = {"накладная", "груз", "вес"}
DOCS = [
    {"id": "wb-4478", "text": "Накладная 4478: трубы, 19 т.", "concepts": CARGO},
    {"id": "wb-4471", "text": "Накладная 4471: стекло листовое, 24 т.", "concepts": CARGO},
    {"id": "wb-4502", "text": "Накладная 4502: поддоны, 12 т.", "concepts": CARGO},
    {"id": "mail-4471", "text": "Письмо: по накладной 4471 уточните время подачи.",
     "concepts": {"письмо", "время", "накладная"}},
    {"id": "pay-4471", "text": "Оплата по накладной 4471 поступила 2 сентября.",
     "concepts": {"оплата", "накладная"}},
]

QUERY_CONCEPTS = {"накладная", "груз", "вес"}
EXACT = []
SEMANTIC = []
FOUND = []


def run_tool(name, arguments):
    """Точный поиск: буквальное вхождение строки, никакого смысла."""
    if name != "exact":
        raise ValueError(f"инструмента '{name}' не существует")
    token = arguments["token"]
    EXACT.append(token)
    return [d for d in DOCS if token in d["text"]]


class Model:
    """Понимает смысл и умеет отличить обозначение от слова."""

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
        """Что в вопросе обозначение, а не понятие."""
        return TOKEN if TOKEN in question else None

    def reply(self, question, doc):
        FOUND.append(doc["id"])
        weights = {"wb-4471": "24 т", "wb-4478": "19 т", "wb-4502": "12 т"}
        if doc["id"] in weights:
            return f"По накладной {doc['text'].split()[1].rstrip(':')}: {weights[doc['id']]}."
        return f"По найденному: {doc['text']}"


def play(agent):
    EXACT.clear()
    SEMANTIC.clear()
    FOUND.clear()
    return agent.run(QUESTION)


def explain(exc):
    if isinstance(exc, ValueError) and "max()" in str(exc):
        return ("Точный поиск ничего не нашёл. Проверьте, что ищете\n"
                "        обозначение из вопроса, а не весь вопрос целиком.")
    return None


def verify(result):
    answer, steps = result
    text = answer if isinstance(answer, str) else ""
    both = bool(EXACT) and bool(SEMANTIC)
    return [
        (both, f"сигналов: точный — {'да' if EXACT else 'нет'}, смысловой — {'да' if SEMANTIC else 'нет'}"),
        (FOUND == [ANSWER_ID], f"выбран документ: {FOUND[0] if FOUND else 'ни одного'}"),
        ("24 т" in text, f"ответ агента: {text}"),
        (steps <= 2, f"обращений к модели: {steps} (допустимо 2)"),
    ]
