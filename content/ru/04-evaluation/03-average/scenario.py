"""Третья смена трека. Девяносто процентов, и все провалы в одном месте."""

TITLE = "Трек «Оценка» · Уровень 03 · Среднее прячет провал"
BRIEF = """Итог по набору — 90 процентов, и его несут в релиз.
Все четыре провала в перегрузе: там половина ответов неверна."""

GOOD = "верно"
CASES = [
    # Перегруз: ошибка ставит гружёный тягач на мост, который его не держит.
    {"id": "w1", "kind": "перегруз", "ok": True},
    {"id": "w2", "kind": "перегруз", "ok": False},
    {"id": "w3", "kind": "перегруз", "ok": True},
    {"id": "w4", "kind": "перегруз", "ok": False},
    {"id": "w5", "kind": "перегруз", "ok": True},
    {"id": "w6", "kind": "перегруз", "ok": False},
    {"id": "w7", "kind": "перегруз", "ok": True},
    {"id": "w8", "kind": "перегруз", "ok": False},
    # Ставки: ошибка стоит денег и правится счётом.
    {"id": "r1", "kind": "ставки", "ok": True},
    {"id": "r2", "kind": "ставки", "ok": True},
    {"id": "r3", "kind": "ставки", "ok": True},
    {"id": "r4", "kind": "ставки", "ok": True},
    {"id": "r5", "kind": "ставки", "ok": True},
    {"id": "r6", "kind": "ставки", "ok": True},
    # Расписание: ошибка сдвигает подачу.
    {"id": "s1", "kind": "расписание", "ok": True},
    {"id": "s2", "kind": "расписание", "ok": True},
    {"id": "s3", "kind": "расписание", "ok": True},
    {"id": "s4", "kind": "расписание", "ok": True},
    {"id": "s5", "kind": "расписание", "ok": True},
    {"id": "s6", "kind": "расписание", "ok": True},
]

WEAKEST = "перегруз"
GROUPED = []


def run_tool(name, arguments):
    """Прогоняет один случай и говорит, верен ли ответ."""
    if name != "check":
        raise ValueError(f"инструмента '{name}' не существует")
    case = next((c for c in CASES if c["id"] == arguments["case"]), None)
    if case is None:
        raise ValueError(f"случая '{arguments['case']}' нет в наборе")
    return GOOD if case["ok"] else "неверно"


class Model:
    """Складывает отчёт. Разбивку по видам делаете вы."""

    def report(self, overall, by_kind):
        GROUPED.clear()
        GROUPED.extend(sorted(by_kind))
        if not by_kind:
            return f"Итог по набору: {overall}%."
        worst = min(by_kind, key=lambda k: by_kind[k])
        lines = ", ".join(f"{k} {by_kind[k]}%" for k in sorted(by_kind))
        return (
            f"Итог по набору: {overall}%. По видам: {lines}. "
            f"Слабое место — {worst}."
        )


def play(agent):
    GROUPED.clear()
    return agent.run()


def explain(exc):
    if isinstance(exc, ZeroDivisionError):
        return ("В какой-то вид не попало ни одного случая.\n"
                "        Считайте долю только по непустым видам.")
    return None


def verify(result):
    answer, steps = result
    text = answer if isinstance(answer, str) else ""
    kinds = sorted({c["kind"] for c in CASES})
    return [
        (GROUPED == kinds, f"видов посчитано: {GROUPED or 'ни одного'} (нужно {kinds})"),
        (f"Слабое место — {WEAKEST}" in text, f"слабое место названо: {WEAKEST in text}"),
        ("перегруз 50%" in text, f"доля по перегрузу: {'50%' if 'перегруз 50%' in text else 'не названа'}"),
        (steps <= 2, f"обращений к модели: {steps} (допустимо 2)"),
    ]
