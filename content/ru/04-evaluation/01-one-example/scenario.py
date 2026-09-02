"""Первая смена трека. Один удачный пример объявили улучшением."""

TITLE = "Трек «Оценка» · Уровень 01 · Один пример — не измерение"
BRIEF = """Правку проверили на том случае, ради которого её делали.
Он починился. Два других сломались, и о них никто не спросил."""

CASES = [
    {"id": "c1", "question": "Ставка на Ларедо — Ньюарк?", "expected": "2.90"},
    {"id": "c2", "question": "Предел моста Кэрролл?", "expected": "18 т"},
    {"id": "c3", "question": "Топливная надбавка?", "expected": "0.35"},
    {"id": "c4", "question": "Время приёмки в Ньюарке?", "expected": "18:00"},
    {"id": "c5", "question": "Вес по накладной 4471?", "expected": "24 т"},
    {"id": "c6", "question": "Ставка на Ларедо — Чикаго?", "expected": "2.75"},
]

# Старая версия ошибалась на c3 — ради него правку и делали.
OLD = {"c1": "2.90", "c2": "18 т", "c3": "не знаю", "c4": "18:00", "c5": "24 т", "c6": "2.75"}
# Новая чинит c3 и ломает c1 и c5.
NEW = {"c1": "3.10", "c2": "18 т", "c3": "0.35", "c4": "18:00", "c5": "19 т", "c6": "2.75"}

ASKED = []


def run_tool(name, arguments):
    """Задаёт один вопрос одной версии агента."""
    if name != "ask":
        raise ValueError(f"инструмента '{name}' не существует")
    version, case = arguments["version"], arguments["case"]
    table = {"old": OLD, "new": NEW}.get(version)
    if table is None:
        raise ValueError(f"версии '{version}' не существует")
    if case not in table:
        raise ValueError(f"случая '{case}' нет в наборе")
    ASKED.append((version, case))
    return table[case]


class Model:
    """Считает итог по числу пройденных случаев."""

    def verdict(self, old_passed, new_passed, total):
        if new_passed > old_passed:
            change = "стало лучше"
        elif new_passed < old_passed:
            change = "стало хуже"
        else:
            change = "не изменилось"
        return (
            f"Старая {old_passed} из {total}, новая {new_passed} из {total} — {change}."
        )


def play(agent):
    ASKED.clear()
    return agent.run()


def explain(exc):
    if isinstance(exc, ValueError) and "нет в наборе" in str(exc):
        return ("Случаи набора лежат в CASES, у каждого есть id.\n"
                "        Спрашивать надо по этому id.")
    return None


def verify(result):
    answer, steps = result
    text = answer if isinstance(answer, str) else ""
    per_version = {v: {c for w, c in ASKED if w == v} for v in ("old", "new")}
    covered = min(len(per_version["old"]), len(per_version["new"]))
    return [
        (covered == len(CASES), f"случаев прогнано на каждой версии: {covered} из {len(CASES)}"),
        ("стало хуже" in text, f"вердикт: {text or 'нет ответа'}"),
        ("5 из 6" in text and "4 из 6" in text, f"счёт назван: {'да' if '5 из 6' in text else 'нет'}"),
        (steps <= 2, f"обращений к модели: {steps} (допустимо 2)"),
    ]
