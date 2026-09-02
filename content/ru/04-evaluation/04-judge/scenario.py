"""Четвёртая смена трека. Судья оценивает собственный вывод."""

TITLE = "Трек «Оценка» · Уровень 04 · Судья подыгрывает"
BRIEF = """Агент сам себя проверяет и ставит шесть из шести.
Два ответа — уклончивые: «около трёх долларов» и «где-то к вечеру»."""

CASES = [
    {"id": "c1", "expected": "2.90", "got": "2.90"},
    {"id": "c2", "expected": "18 т", "got": "18 т"},
    {"id": "c3", "expected": "0.35", "got": "0.35"},
    {"id": "c4", "expected": "18:00", "got": "где-то к вечеру"},
    {"id": "c5", "expected": "24 т", "got": "24 т"},
    {"id": "c6", "expected": "2.90", "got": "около трёх долларов"},
]

VAGUE = {"где-то к вечеру", "около трёх долларов"}
TRUE_SCORE = sum(1 for c in CASES if c["got"] not in VAGUE)

RUBRIC = """Ответ засчитан, если называет конкретное значение.
Диапазон, приблизительная оценка и уклончивая формулировка не засчитываются."""

WHO = []


class Model:
    """Один и тот же собеседник в двух ролях: автор и судья."""

    def judge_own(self, expected, got):
        """Автор оценивает собственный ответ. Знает, что хотел сказать."""
        WHO.append("автор")
        return True

    def judge_blind(self, rubric, expected, got):
        """Судья видит только эталон и ответ. Кто его написал — не знает."""
        WHO.append("независимый")
        if got == expected:
            return True
        return got not in VAGUE

    def report(self, passed, total, judge):
        return f"Судил {judge}: {passed} из {total}."


def play(agent):
    WHO.clear()
    return agent.run()


def explain(exc):
    if isinstance(exc, TypeError) and "positional" in str(exc):
        return ("judge_blind принимает три аргумента: рубрику, эталон\n"
                "        и полученный ответ. Рубрика лежит в RUBRIC.")
    return None


def verify(result):
    answer, steps = result
    text = answer if isinstance(answer, str) else ""
    used = sorted(set(WHO))
    return [
        (used == ["независимый"], f"кто судил: {', '.join(used) or 'никто'}"),
        (f"{TRUE_SCORE} из {len(CASES)}" in text,
         f"счёт: {text or 'нет ответа'}"),
        (len(WHO) == len(CASES), f"случаев отсужено: {len(WHO)} из {len(CASES)}"),
        (steps <= 2, f"обращений к модели: {steps} (допустимо 2)"),
    ]
