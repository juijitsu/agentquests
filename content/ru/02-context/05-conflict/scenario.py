"""Пятая смена трека. Два документа спорят, и спор решает исход."""

TITLE = "Трек «Контекст» · Уровень 05 · Противоречие источников"
BRIEF = """Накладная говорит 24 тонны, весовая — 26.4. Оба документа сегодняшние.
Мост держит 26, и молчаливый выбор одного из них решает исход рейса."""

FACTS = [
    {"source": "весовая Ларедо", "field": "вес", "value": 26.4},
    {"source": "накладная 4471", "field": "вес", "value": 24.0},
    {"source": "маршрутный лист", "field": "мост", "value": 26.0},
]
WEIGHTS = sorted({f["value"] for f in FACTS if f["field"] == "вес"})
SOURCES = [f["source"] for f in FACTS if f["field"] == "вес"]

QUESTION = "Пройдёт ли груз TX-118 по мосту?"
PASSED = {}


def run_tool(name, arguments):
    if name != "facts":
        raise ValueError(f"инструмента '{name}' не существует")
    return sorted(FACTS, key=lambda f: f["source"])


def _readings(merged, field):
    """Одно значение или несколько — приводим к общему виду, не теряя источник."""
    got = merged.get(field)
    if isinstance(got, list):
        return got
    return [("источник не указан", got)]


class Model:
    """Считает по тому, что дали. Спор замечает, только если оба значения дошли."""

    def ask(self, question, merged):
        PASSED.clear()
        PASSED.update(merged)

        weights = _readings(merged, "вес")
        limit = min(v for _, v in _readings(merged, "мост"))
        distinct = sorted({v for _, v in weights})

        if len(distinct) > 1:
            listing = ", ".join(f"{who} {value}" for who, value in weights)
            return (
                f"Источники расходятся по весу: {listing}. "
                f"При лимите {limit} т ответ зависит от того, чему верить — нужно уточнить."
            )
        weight = distinct[0]
        return f"Груз {weight} т, лимит {limit} т — {'пройдёт' if weight <= limit else 'не пройдёт'}."


def play(agent):
    PASSED.clear()
    return agent.run(QUESTION)


def explain(exc):
    if isinstance(exc, TypeError) and "float" in str(exc):
        return ("В значении поля оказалось одно число вместо списка показаний.\n"
                "        Накапливайте показания, а не перезаписывайте их.")
    return None


def verify(result):
    answer, steps = result
    text = answer if isinstance(answer, str) else ""
    got = PASSED.get("вес")
    reached = len({v for _, v in got}) if isinstance(got, list) else (0 if got is None else 1)
    named = [s for s in SOURCES if s in text]
    return [
        (reached == len(WEIGHTS), f"значений веса дошло до модели: {reached} из {len(WEIGHTS)}"),
        ("расходятся" in text, f"ответ агента: {text}"),
        (len(named) == len(SOURCES), f"названо источников: {len(named)} из {len(SOURCES)}"),
        (steps <= 2, f"обращений к модели: {steps} (допустимо 2)"),
    ]
