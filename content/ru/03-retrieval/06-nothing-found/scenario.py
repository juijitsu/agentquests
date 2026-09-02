"""Шестая смена трека. Ответа в корпусе нет, а поиск всё равно отвечает."""

TITLE = "Трек «Поиск» · Уровень 06 · Ответа нет в корпусе"
BRIEF = """Про мост Талмадж в документах нет ничего, и агент отвечает
про мост Кэрролл. Верный ответ на другой вопрос."""

THRESHOLD = 0.8

MISSING_Q = "Какая предельная масса на мосту Талмадж?"
PRESENT_Q = "Какая предельная масса на мосту Кэрролл?"
SUBJECT = "мост Талмадж"

DOCS = [
    {"id": "carroll", "text": "Мост Кэрролл: предельная масса 18 т.",
     "concepts": {"мост", "кэрролл", "масса", "предел"}},
    {"id": "greenville", "text": "Мост Гринвилл: предельная масса 30 т.",
     "concepts": {"мост", "гринвилл", "масса", "предел"}},
    {"id": "ramp", "text": "Съезд 12 на I-55 закрыт на ремонт.",
     "concepts": {"дорога", "ремонт"}},
    {"id": "dock", "text": "Склад в Ньюарке принимает до 18:00.",
     "concepts": {"склад", "время"}},
]

QUERIES = {
    MISSING_Q: {"мост", "талмадж", "масса", "предел"},
    PRESENT_Q: {"мост", "кэрролл", "масса", "предел"},
}

ANSWERS = []


class Model:
    """Считает похожесть и умеет честно сказать, что искомого нет."""

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
        """О чём спрашивают — то, чего может не оказаться в документах."""
        return SUBJECT if question == MISSING_Q else "мост Кэрролл"

    def say_missing(self, question):
        return f"Про {self.subject(question)} в документах ничего нет."

    def reply(self, question, doc):
        if doc["id"] == "carroll":
            return "Мост Кэрролл держит 18 т."
        if doc["id"] == "greenville":
            return "Мост Гринвилл держит 30 т."
        return f"По найденному: {doc['text']}"


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
        return ("Когда подходящего документа нет, отвечать по нему нельзя:\n"
                "        воспользуйтесь model.say_missing(question).")
    return None


def verify(result):
    answers, steps = result
    missing = answers[0] if len(answers) > 0 else ""
    present = answers[1] if len(answers) > 1 else ""
    return [
        ("ничего нет" in missing, f"про отсутствующий мост: {missing or 'нет ответа'}"),
        (SUBJECT in missing, f"предмет вопроса назван: {'да' if SUBJECT in missing else 'нет'}"),
        ("18 т" in present, f"про имеющийся мост: {present or 'нет ответа'}"),
        (steps <= 4, f"обращений к модели: {steps} (допустимо 4)"),
    ]
