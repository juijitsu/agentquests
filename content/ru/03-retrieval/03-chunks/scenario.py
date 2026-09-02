"""Третья смена трека. Факт разрезан по границе куска."""

TITLE = "Трек «Поиск» · Уровень 03 · Границы кусков"
BRIEF = """Мост назван в одном куске, его предел — в соседнем.
Целым лежит только чужой мост, и агент отвечает про него."""

QUESTION = "Какая предельная масса на мосту Кэрролл?"
ANSWER_BRIDGE = "Кэрролл"

CHUNKS = [
    {
        "id": "carroll-1", "doc": "carroll",
        "text": "Мост Кэрролл на I-55 прошёл реконструкцию в 2024 году.",
        "concepts": {"мост", "кэрролл", "ремонт"},
    },
    {
        "id": "carroll-2", "doc": "carroll",
        "text": "Предельная масса после неё — 24 т.",
        "concepts": {"масса", "предел"},
    },
    {
        "id": "greenville-1", "doc": "greenville",
        "text": "Мост Гринвилл: предельная масса 30 т.",
        "concepts": {"мост", "гринвилл", "масса", "предел"},
    },
    {
        "id": "fuel-1", "doc": "fuel",
        "text": "Заправка Уэйко работает круглосуточно.",
        "concepts": {"топливо"},
    },
]

QUERY_CONCEPTS = {"мост", "кэрролл", "масса", "предел"}
STITCHED = []
FOUND = []


def run_tool(name, arguments):
    """Соседи по документу: тот же кусок вместе с теми, что рядом."""
    if name != "neighbours":
        raise ValueError(f"инструмента '{name}' не существует")
    chunk = next((c for c in CHUNKS if c["id"] == arguments["id"]), None)
    if chunk is None:
        raise ValueError(f"куска '{arguments['id']}' нет в индексе")
    STITCHED.append(chunk["id"])
    return [c for c in CHUNKS if c["doc"] == chunk["doc"]]


class Model:
    """Понятия текста — объединение понятий всех кусков, которые в нём есть."""

    def embed(self, text):
        if text == QUESTION:
            return set(QUERY_CONCEPTS)
        found = set()
        for chunk in CHUNKS:
            if chunk["text"] in text:
                found |= chunk["concepts"]
        return found

    def similarity(self, left, right):
        a, b = self.embed(left), self.embed(right)
        return len(a & b) / len(a | b) if a and b else 0.0

    def answers(self, question, text):
        """Самодостаточен ли кусок: назван ли мост и указана ли его масса."""
        concepts = self.embed(text)
        return {"кэрролл", "масса"} <= concepts

    def reply(self, question, text):
        bridge = "Кэрролл" if "Кэрролл" in text else (
            "Гринвилл" if "Гринвилл" in text else "неизвестный"
        )
        FOUND.append(bridge)
        if bridge == ANSWER_BRIDGE and "24 т" in text:
            return "Мост Кэрролл держит 24 т."
        return f"По найденному: {text}"


def play(agent):
    STITCHED.clear()
    FOUND.clear()
    return agent.run(QUESTION)


def explain(exc):
    if isinstance(exc, ValueError) and "max()" in str(exc):
        return ("Ни один кусок не оказался самодостаточным — это и есть\n"
                "        симптом уровня. Достройте кусок соседями, а не\n"
                "        снижайте требования к нему.")
    return None


def verify(result):
    answer, steps = result
    text = answer if isinstance(answer, str) else ""
    return [
        (bool(STITCHED), f"кусков достроено соседями: {len(STITCHED)}"),
        (FOUND == [ANSWER_BRIDGE], f"мост в ответе: {FOUND[0] if FOUND else 'ни одного'}"),
        ("24 т" in text, f"ответ агента: {text}"),
        (steps <= 2, f"обращений к модели: {steps} (допустимо 2)"),
    ]
