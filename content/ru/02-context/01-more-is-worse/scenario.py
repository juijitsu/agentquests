"""Первая смена трека. Факт лежит в окне и всё равно не найден."""

import re

TITLE = "Трек «Контекст» · Уровень 01 · Больше — не лучше"
BRIEF = """Все двадцать две бумаги по рейсу отправлены модели целиком.
Ограничение по мосту среди них есть — и ответ всё равно неверный."""

WINDOW = 6
EDGE = 3

DOCS = [
    "путевой лист TX-118: выезд из Ларедо 06:40",
    "накладная 4471: стекло листовое, 24 тонны",
    "весовая Ларедо: фактический вес 24.0 т",
    "тягач 118: пробег 412 тыс. миль, ТО пройдено",
    "прицеп 77: тент, год выпуска 2019",
    "водитель Ортис: смена начата 06:10",
    "страховка груза: полис действует до 31.12",
    "маршрут: I-35 Ларедо — Даллас",
    "маршрут: I-30 Даллас — Литл-Рок",
    "маршрут: I-55 Литл-Рок — Мемфис",
    "мост Гринвилл на I-30: ограничение 30 тонн",
    "заправка Уэйко: залито 180 галлонов",
    "мост Кэрролл на I-55, миля 212: ограничение 18 тонн",
    "стоянка Тексаркана: оплачена до утра",
    "путепровод Мемфис-Даунтаун: ограничение 26 тонн",
    "погода по Далласу: ясно, ветер слабый",
    "таможня: груз внутренний, оформление не требуется",
    "склад Ньюарк: приёмка до 18:00",
    "контакт получателя: диспетчер Ривера",
    "оплата: по факту доставки",
    "примечание: тент проверен на герметичность",
    "отметка механика: давление в шинах в норме",
]

QUESTION = "Пройдёт ли груз 24 тонны по маршруту?"
LIMIT = 18

PASSED = []
SEEN = []


def run_tool(name, arguments):
    if name != "about":
        raise ValueError(f"инструмента '{name}' не существует")
    topic = arguments["topic"]
    found = [d for d in DOCS if topic.lower() in d.lower()]
    if not found:
        return "по этой теме бумаг нет"
    return " | ".join(found)


class Model:
    """Читает целиком не больше шести блоков. Дальше — только края."""

    def topic(self, question):
        return "ограничение"

    def ask(self, question, blocks):
        PASSED.append(len(blocks))
        seen = blocks if len(blocks) <= WINDOW else blocks[:EDGE] + blocks[-EDGE:]
        SEEN.clear()
        SEEN.extend(seen)

        cargo = int(re.search(r"(\d+) тонн", question).group(1))
        limits = []
        for block in seen:
            found = re.search(r"ограничение (\d+) тонн", block)
            if found:
                limits.append(int(found.group(1)))
        if not limits:
            return "Ограничений в бумагах не нашёл — маршрут свободен."
        tightest = min(limits)
        if tightest < cargo:
            return f"Не пройдёт: самое узкое место {tightest} т, груз {cargo} т."
        return f"Пройдёт: самое узкое место {tightest} т, груз {cargo} т."


def play(agent):
    PASSED.clear()
    SEEN.clear()
    return agent.run(QUESTION)


def explain(exc):
    if isinstance(exc, AttributeError) and "group" in str(exc):
        return ("Вопрос ушёл в модель не целиком. Вес груза модель берёт\n"
                "        из самого вопроса, а не из бумаг.")
    return None


def verify(result):
    answer, steps = result
    text = answer if isinstance(answer, str) else ""
    binding = next(d for d in DOCS if f"ограничение {LIMIT} тонн" in d)
    return [
        (binding in SEEN, f"нужная бумага дошла до модели: {'да' if binding in SEEN else 'нет'}"),
        ("Не пройдёт" in text, f"ответ агента: {text}"),
        (PASSED and PASSED[-1] <= WINDOW,
         f"блоков отправлено: {PASSED[-1] if PASSED else 0} (модель читает {WINDOW})"),
        (steps <= 2, f"обращений к модели: {steps} (допустимо 2)"),
    ]
