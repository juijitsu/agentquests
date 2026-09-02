"""Пятая смена трека. Половина набора лежит в самом промпте."""

TITLE = "Трек «Оценка» · Уровень 05 · Тест протёк в промпт"
BRIEF = """Пять из восьми — приличный результат. Четыре из этих пяти
случаев дословно лежат в промпте агента как примеры."""

CASES = [
    {"id": "c1", "question": "Ставка на Ларедо — Ньюарк?", "ok": True},
    {"id": "c2", "question": "Предел моста Кэрролл?", "ok": True},
    {"id": "c3", "question": "Топливная надбавка?", "ok": True},
    {"id": "c4", "question": "Время приёмки в Ньюарке?", "ok": True},
    {"id": "c5", "question": "Ставка на Ларедо — Хьюстон?", "ok": True},
    {"id": "c6", "question": "Предел моста Гринвилл?", "ok": False},
    {"id": "c7", "question": "Надбавка за ожидание?", "ok": False},
    {"id": "c8", "question": "Время приёмки в Далласе?", "ok": False},
]

# Эти случаи дословно приведены в промпте агента как примеры.
IN_PROMPT = {"c1", "c2", "c3", "c4"}

HELD_OUT = [c for c in CASES if c["id"] not in IN_PROMPT]
HONEST = sum(1 for c in HELD_OUT if c["ok"])

LOOKED = []


def run_tool(name, arguments):
    if name == "check":
        case = next((c for c in CASES if c["id"] == arguments["case"]), None)
        if case is None:
            raise ValueError(f"случая '{arguments['case']}' нет в наборе")
        return "верно" if case["ok"] else "неверно"
    if name == "in_prompt":
        LOOKED.append(arguments["case"])
        return arguments["case"] in IN_PROMPT
    raise ValueError(f"инструмента '{name}' не существует")


class Model:
    """Складывает отчёт из двух чисел: по всему набору и по незнакомым."""

    def report(self, all_passed, all_total, clean_passed, clean_total):
        if clean_total == all_total:
            return f"По набору {all_passed} из {all_total}."
        return (
            f"По всему набору {all_passed} из {all_total}, "
            f"по незнакомым случаям {clean_passed} из {clean_total}."
        )


def play(agent):
    LOOKED.clear()
    return agent.run()


def explain(exc):
    if isinstance(exc, ZeroDivisionError):
        return ("Незнакомых случаев не осталось: вы отбросили весь набор.\n"
                "        Исключать надо только те, что лежат в промпте.")
    return None


def verify(result):
    answer, steps = result
    text = answer if isinstance(answer, str) else ""
    return [
        (set(LOOKED) == {c["id"] for c in CASES},
         f"случаев проверено на утечку: {len(set(LOOKED))} из {len(CASES)}"),
        (f"по незнакомым случаям {HONEST} из {len(HELD_OUT)}" in text,
         f"честный счёт: {'назван' if str(HONEST) in text else 'не назван'}"),
        ("По всему набору 5 из 8" in text, f"отчёт: {text or 'нет ответа'}"),
        (steps <= 2, f"обращений к модели: {steps} (допустимо 2)"),
    ]
