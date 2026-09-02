"""Пятая смена трека. Один вектор на два вопроса попадает между ними."""

TITLE = "Трек «Поиск» · Уровень 05 · Составной вопрос"
BRIEF = """Спросили про мост и про приёмку разом. Поиск принёс обе бумаги
про приёмку, а про мост — ни одной."""

QUESTION = "Пройдёт ли TX-118 по мосту Кэрролл и успеем ли к приёмке в Ньюарке?"
TOP_K = 2
NEEDED = {"bridge", "cargo", "hours", "eta"}

DOCS = [
    {"id": "bridge-limit", "fact": "bridge",
     "text": "Мост Кэрролл: предельная масса 18 т.",
     "concepts": {"мост", "масса", "предел"}},
    {"id": "cargo-weight", "fact": "cargo",
     "text": "Груз TX-118 по весовой: 24 т.",
     "concepts": {"груз", "масса"}},
    {"id": "dock-hours", "fact": "hours",
     "text": "Склад в Ньюарке принимает до 18:00.",
     "concepts": {"склад", "время", "приёмка", "ньюарк"}},
    {"id": "eta", "fact": "eta",
     "text": "Расчётное прибытие TX-118 в Ньюарк: 16:30.",
     "concepts": {"время", "прибытие", "ньюарк"}},
    {"id": "dock-address", "fact": "address",
     "text": "Склад в Ньюарке: ворота 4, въезд с Дойл-стрит.",
     "concepts": {"склад", "ньюарк", "адрес", "приёмка"}},
]

WHOLE = {"мост", "приёмка", "ньюарк", "время"}
PARTS = {
    "Пройдёт ли TX-118 по мосту Кэрролл?": {"мост", "масса", "предел", "груз"},
    "Успеем ли к приёмке в Ньюарке?": {"приёмка", "ньюарк", "время"},
}

QUERIES = []
PICKED = []


def _concepts(text):
    if text == QUESTION:
        return set(WHOLE)
    if text in PARTS:
        return set(PARTS[text])
    for doc in DOCS:
        if doc["text"] == text:
            return set(doc["concepts"])
    return set()


def run_tool(name, arguments):
    """Поиск по одному запросу. Считает, сколько раз его позвали."""
    if name != "search":
        raise ValueError(f"инструмента '{name}' не существует")
    query = arguments["query"]
    QUERIES.append(query)
    scored = sorted(
        DOCS,
        key=lambda d: len(_concepts(query) & d["concepts"])
        / len(_concepts(query) | d["concepts"]),
        reverse=True,
    )
    return scored[:TOP_K]


class Model:
    """Раскладывает вопрос на части. Считать ответ — уже её дело."""

    def split(self, question):
        return list(PARTS)

    def reply(self, question, docs):
        facts = {d["fact"] for d in docs}
        PICKED.clear()
        PICKED.extend(sorted(facts))

        parts = []
        if {"bridge", "cargo"} <= facts:
            parts.append("по мосту не пройдёт: 24 т при пределе 18 т")
        if {"hours", "eta"} <= facts:
            parts.append("к приёмке успеваете: 16:30 при закрытии в 18:00")
        if not parts:
            return "Ответить не по чему."
        return "Итог — " + "; ".join(parts) + "."


def play(agent):
    QUERIES.clear()
    PICKED.clear()
    return agent.run(QUESTION)


def explain(exc):
    if isinstance(exc, TypeError) and "unhashable" in str(exc):
        return ("Поиск возвращает документы, а не тексты: складывайте\n"
                "        списки, а не множества.")
    return None


def verify(result):
    answer, steps = result
    text = answer if isinstance(answer, str) else ""
    return [
        (len(QUERIES) >= 2, f"запросов к поиску: {len(QUERIES)} (вопрос составной)"),
        (NEEDED <= set(PICKED), f"фактов в подборке: {PICKED or 'ни одного'}"),
        ("не пройдёт" in text, f"ответ агента: {text}"),
        (steps <= 2, f"обращений к модели: {steps} (допустимо 2)"),
    ]
