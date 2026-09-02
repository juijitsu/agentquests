"""Вторая смена трека. Верный ответ другими словами засчитан как ошибка."""

TITLE = "Трек «Оценка» · Уровень 02 · Совпадение строк — не правильность"
BRIEF = """Новая версия отвечает верно на все шесть случаев.
Три ответа сформулированы иначе, и метрика требует откатить правку."""

CASES = [
    {"id": "c1", "question": "Ставка на Ларедо — Ньюарк?", "expected": "2.90"},
    {"id": "c2", "question": "Предел моста Кэрролл?", "expected": "18 т"},
    {"id": "c3", "question": "Топливная надбавка?", "expected": "0.35"},
    {"id": "c4", "question": "Время приёмки в Ньюарке?", "expected": "18:00"},
    {"id": "c5", "question": "Вес по накладной 4471?", "expected": "24 т"},
    {"id": "c6", "question": "Ставка на Ларедо — Чикаго?", "expected": "2.75"},
]

OLD = {"c1": "2.90", "c2": "18 т", "c3": "не знаю",
       "c4": "18:00", "c5": "24 т", "c6": "2.75"}
NEW = {"c1": "2 доллара 90 центов", "c2": "18 т", "c3": "0.35",
       "c4": "до шести вечера", "c5": "двадцать четыре тонны", "c6": "2.75"}

# Пересказы, которые модель признаёт тем же ответом.
SAME = {
    ("2.90", "2 доллара 90 центов"),
    ("18:00", "до шести вечера"),
    ("24 т", "двадцать четыре тонны"),
}

JUDGED = []


def run_tool(name, arguments):
    if name != "ask":
        raise ValueError(f"инструмента '{name}' не существует")
    table = {"old": OLD, "new": NEW}.get(arguments["version"])
    if table is None:
        raise ValueError(f"версии '{arguments['version']}' не существует")
    return table[arguments["case"]]


class Model:
    """Умеет сказать, тот же это ответ или другой."""

    def same_answer(self, expected, got):
        JUDGED.append((expected, got))
        return got == expected or (expected, got) in SAME

    def verdict(self, old_passed, new_passed, total):
        if new_passed > old_passed:
            change = "стало лучше"
        elif new_passed < old_passed:
            change = "стало хуже"
        else:
            change = "не изменилось"
        return f"Старая {old_passed} из {total}, новая {new_passed} из {total} — {change}."


def play(agent):
    JUDGED.clear()
    return agent.run()


def explain(exc):
    if isinstance(exc, KeyError):
        return ("Случаи набора лежат в CASES: у каждого id, question\n"
                "        и expected. Спрашивать надо по id.")
    return None


def verify(result):
    answer, steps = result
    text = answer if isinstance(answer, str) else ""
    return [
        (len(JUDGED) >= 2 * len(CASES),
         f"сверок по смыслу: {len(JUDGED)} (нужно {2 * len(CASES)})"),
        ("стало лучше" in text, f"вердикт: {text or 'нет ответа'}"),
        ("6 из 6" in text, f"счёт новой версии: {'6 из 6' if '6 из 6' in text else 'не назван'}"),
        (steps <= 2, f"обращений к модели: {steps} (допустимо 2)"),
    ]
