"""Девятая смена трека. Поисковик целиком: всё сразу и всё мешает."""

TITLE = "Трек «Поиск» · Уровень 09 · Босс: поисковик целиком"
BRIEF = """Вопрос из двух половин: по одной ответ есть и спрятан за номером,
свежестью и тремя копиями. По другой ответа нет вовсе."""

QUESTION = "Сколько сейчас выходит по накладной 4471 и пройдёт ли груз по мосту Талмадж?"
TOP_K = 3
THRESHOLD = 0.4
MISSING_SUBJECT = "мост Талмадж"

PART_RATE = "Сколько сейчас выходит по накладной 4471?"
PART_BRIDGE = "Пройдёт ли груз по мосту Талмадж?"
PARTS = {
    PART_RATE: {"ставка", "тариф", "накладная", "итого"},
    PART_BRIDGE: {"мост", "талмадж", "масса", "предел"},
}

DOCS = [
    {"id": "rate-old", "fact": "rate", "waybill": "4471", "fresh": 0.25,
     "text": "Тариф по накладной 4471: 3.10 за милю, с 10.02.2025.",
     "concepts": {"ставка", "тариф", "накладная", "миля"}},
    {"id": "rate-new-a", "fact": "rate", "waybill": "4471", "fresh": 0.95,
     "text": "С 21.08 по накладной 4471 — 2.90.",
     "concepts": {"ставка", "накладная"}},
    {"id": "rate-new-b", "fact": "rate", "waybill": "4471", "fresh": 0.95,
     "text": "Подтверждение клиенту: по накладной 4471 ставка 2.90.",
     "concepts": {"ставка", "накладная"}},
    {"id": "rate-new-c", "fact": "rate", "waybill": "4471", "fresh": 0.95,
     "text": "Биллинг: накладная 4471, 2.90 за милю.",
     "concepts": {"ставка", "накладная"}},
    {"id": "fuel-4471", "fact": "fuel", "waybill": "4471", "fresh": 0.95,
     "text": "Топливная надбавка по накладной 4471: 0.35.",
     "concepts": {"надбавка", "топливо", "накладная"}},
    {"id": "mail-4471", "fact": "mail", "waybill": "4471", "fresh": 0.90,
     "text": "Письмо: по накладной 4471 уточните время подачи.",
     "concepts": {"письмо", "время", "накладная"}},
    {"id": "rate-4478", "fact": "rate", "waybill": "4478", "fresh": 0.97,
     "text": "С 25.08 по накладной 4478 — 2.40.",
     "concepts": {"ставка", "накладная"}},
    {"id": "carroll", "fact": "bridge", "waybill": None, "fresh": 0.40,
     "text": "Мост Кэрролл: предельная масса 18 т.",
     "concepts": {"мост", "кэрролл", "масса", "предел"}},
    {"id": "greenville", "fact": "bridge", "waybill": None, "fresh": 0.40,
     "text": "Мост Гринвилл: предельная масса 30 т.",
     "concepts": {"мост", "гринвилл", "масса", "предел"}},
]

QUERIES = []
PICKED = []
ANSWER = []


def run_tool(name, arguments):
    if name != "exact":
        raise ValueError(f"инструмента '{name}' не существует")
    token = arguments["token"]
    return [d for d in DOCS if token in d["text"]]


class Model:
    """Всё, что требует понимания смысла, делает она. Сборку делаете вы."""

    def _concepts(self, text):
        if text in PARTS:
            return set(PARTS[text])
        for doc in DOCS:
            if doc["text"] == text:
                return set(doc["concepts"])
        return set()

    def split(self, question):
        return list(PARTS)

    def identifier(self, question):
        return "4471" if "4471" in question else None

    def similarity(self, left, right):
        a, b = self._concepts(left), self._concepts(right)
        return len(a & b) / len(a | b) if a and b else 0.0

    def freshness(self, doc):
        return doc["fresh"]

    def same_fact(self, left, right):
        pair = [next((d["fact"] for d in DOCS if d["text"] == t), None)
                for t in (left, right)]
        return pair[0] is not None and pair[0] == pair[1]

    def say_missing(self, question):
        return f"про {MISSING_SUBJECT} в документах ничего нет"

    def reply(self, question, selection):
        """selection: список подборок, по одной на подвопрос."""
        QUERIES.clear()
        PICKED.clear()
        parts = []
        for docs in selection:
            if isinstance(docs, str):
                parts.append(docs)
                continue
            QUERIES.append(len(docs))
            PICKED.extend(docs)
            facts = {d["fact"] for d in docs if d["waybill"] == "4471"}
            rates = {d["id"] for d in docs if d["fact"] == "rate"}
            if {"rate", "fuel"} <= facts:
                total = "3.45" if "rate-old" in rates else "3.25"
                parts.append(f"по накладной 4471 выходит {total} за милю")
            elif "rate" in facts:
                parts.append("по накладной 4471 выходит 2.90 за милю")
            else:
                parts.append("по накладной 4471 данных не хватило")
        answer = "Итог: " + "; ".join(parts) + "."
        ANSWER.append(answer)
        return answer


def play(agent):
    QUERIES.clear()
    PICKED.clear()
    ANSWER.clear()
    return agent.run(QUESTION)


def explain(exc):
    if isinstance(exc, ValueError) and "max()" in str(exc):
        return ("Подборка оказалась пустой. Проверьте, что точным поиском\n"
                "        сужается только та половина, где есть обозначение.")
    return None


def verify(result):
    answer, steps = result
    text = answer if isinstance(answer, str) else ""
    foreign = sorted({d["id"] for d in PICKED if d["waybill"] not in (None, "4471")})
    return [
        (len(QUERIES) + text.count("ничего нет") >= 2,
         f"половин вопроса обработано: {len(QUERIES) + text.count('ничего нет')} из 2"),
        (not foreign, f"чужих накладных в подборке: {foreign or 'нет'}"),
        ("3.25" in text, f"ответ по накладной: {text}"),
        (MISSING_SUBJECT in text and "ничего нет" in text,
         f"про несуществующий мост: {'отказ с названием' if MISSING_SUBJECT in text else 'нет отказа'}"),
        (steps <= 2, f"обращений к модели: {steps} (допустимо 2)"),
    ]
