"""Шестая смена трека. Один прогон дал пять из шести. Второй — три."""

TITLE = "Трек «Оценка» · Уровень 06 · Одна попытка ничего не значит"
BRIEF = """Два случая отвечают то верно, то неверно.
На одном прогоне они выпали удачно, и агент назвал систему рабочей."""

RUNS = 5

# Что выдаёт агент на каждом из пяти прогонов. Модель недетерминирована,
# и часть случаев на ней держится через раз.
OUTCOMES = {
    "c1": [True, True, True, True, True],
    "c2": [True, True, True, True, True],
    "c3": [True, True, True, True, True],
    "c4": [False, False, False, False, False],
    "c5": [True, False, True, False, True],
    "c6": [True, True, False, False, False],
}
CASES = [{"id": k} for k in OUTCOMES]

STABLE_OK = sorted(k for k, v in OUTCOMES.items() if all(v))
FLAKY = sorted(k for k, v in OUTCOMES.items() if any(v) and not all(v))

SEEN = []


def run_tool(name, arguments):
    """Прогоняет случай на указанном прогоне. Прогоны нумеруются с нуля."""
    if name != "check":
        raise ValueError(f"инструмента '{name}' не существует")
    case, run = arguments["case"], arguments["run"]
    if case not in OUTCOMES:
        raise ValueError(f"случая '{case}' нет в наборе")
    if not 0 <= run < RUNS:
        raise ValueError(f"прогона {run} не существует, их {RUNS}")
    SEEN.append((case, run))
    return "верно" if OUTCOMES[case][run] else "неверно"


class Model:
    """Складывает отчёт из устойчивых и неустойчивых случаев."""

    def report(self, stable_ok, flaky, total):
        if not flaky:
            return f"Устойчиво верных {len(stable_ok)} из {total}."
        return (
            f"Устойчиво верных {len(stable_ok)} из {total}. "
            f"Неустойчивых {len(flaky)}: {', '.join(sorted(flaky))}."
        )


def play(agent):
    SEEN.clear()
    return agent.run()


def explain(exc):
    if isinstance(exc, ValueError) and "прогона" in str(exc):
        return ("Прогоны нумеруются с нуля и их RUNS штук.\n"
                "        Перебирайте range(RUNS).")
    return None


def verify(result):
    answer, steps = result
    text = answer if isinstance(answer, str) else ""
    per_case = {c["id"]: len({r for k, r in SEEN if k == c["id"]}) for c in CASES}
    covered = min(per_case.values()) if per_case else 0
    named = all(f in text for f in FLAKY)
    return [
        (covered == RUNS, f"прогонов на случай: {covered} из {RUNS}"),
        (named, f"неустойчивые названы: {', '.join(FLAKY) if named else 'нет'}"),
        (f"Устойчиво верных {len(STABLE_OK)} из {len(CASES)}" in text,
         f"отчёт: {text or 'нет ответа'}"),
        (steps <= 2, f"обращений к модели: {steps} (допустимо 2)"),
    ]
