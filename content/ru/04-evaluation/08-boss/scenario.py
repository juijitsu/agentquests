"""Восьмая смена трека. Оценка целиком: выкатывать или нет."""

TITLE = "Трек «Оценка» · Уровень 08 · Босс: оценка целиком"
BRIEF = """Новая версия готова к релизу. Один прогон с самооценкой даёт
девять из девяти. Правда — тридцать три процента на перегрузе."""

RUNS = 3
BAR = 90
RUBRIC = """Ответ засчитан, если называет конкретное верное значение.
Уклончивая формулировка и приблизительная оценка не засчитываются."""

CASES = [
    {"id": "w1", "kind": "перегруз"},
    {"id": "w2", "kind": "перегруз"},
    {"id": "w3", "kind": "перегруз"},
    {"id": "r1", "kind": "ставки"},
    {"id": "r2", "kind": "ставки"},
    {"id": "r3", "kind": "ставки"},
    {"id": "s1", "kind": "расписание"},
    {"id": "s2", "kind": "расписание"},
    {"id": "s3", "kind": "расписание"},
]

# Эти случаи дословно лежат в промпте агента как примеры.
IN_PROMPT = {"w1", "r1"}

# Что на самом деле выдаёт новая версия на каждом из трёх прогонов.
TRUTH = {
    "w1": [True, True, True],
    "w2": [False, False, False],
    "w3": [True, False, True],
    "r1": [True, True, True],
    "r2": [True, True, True],
    "r3": [True, True, True],
    "s1": [True, True, True],
    "s2": [True, True, True],
    "s3": [True, False, False],
}

WHO = []
LOOKED = []
SEEN = []


def run_tool(name, arguments):
    if name == "answer":
        case, run = arguments["case"], arguments["run"]
        if case not in TRUTH:
            raise ValueError(f"случая '{case}' нет в наборе")
        if not 0 <= run < RUNS:
            raise ValueError(f"прогона {run} не существует, их {RUNS}")
        SEEN.append((case, run))
        return f"{case}:{run}"
    if name == "in_prompt":
        LOOKED.append(arguments["case"])
        return arguments["case"] in IN_PROMPT
    raise ValueError(f"инструмента '{name}' не существует")


class Model:
    """Судит в двух ролях и складывает решение из готовых чисел."""

    def judge_own(self, answer):
        WHO.append("автор")
        return True

    def judge_blind(self, rubric, answer):
        WHO.append("независимый")
        case, run = answer.split(":")
        return TRUTH[case][int(run)]

    def decide(self, by_kind, flaky):
        worst = min(by_kind, key=lambda k: by_kind[k]) if by_kind else None
        lines = ", ".join(f"{k} {by_kind[k]}%" for k in sorted(by_kind))
        verdict = (
            "выкатывать нельзя"
            if flaky or (worst is not None and by_kind[worst] < BAR)
            else "можно выкатывать"
        )
        tail = f" Неустойчивых {len(flaky)}: {', '.join(sorted(flaky))}." if flaky else ""
        return f"По видам: {lines}.{tail} Решение — {verdict}."


def play(agent):
    for store in (WHO, LOOKED, SEEN):
        store.clear()
    return agent.run()


def explain(exc):
    if isinstance(exc, ZeroDivisionError):
        return ("В каком-то виде не осталось случаев. Утечку исключают\n"
                "        из счёта, а не из набора видов.")
    return None


def _expected():
    clean = [c for c in CASES if c["id"] not in IN_PROMPT]
    by_kind, flaky = {}, []
    for kind in {c["kind"] for c in clean}:
        same = [c for c in clean if c["kind"] == kind]
        stable = 0
        for c in same:
            runs = TRUTH[c["id"]]
            if all(runs):
                stable += 1
            elif any(runs):
                flaky.append(c["id"])
        by_kind[kind] = round(100 * stable / len(same))
    return by_kind, sorted(flaky)


def verify(result):
    answer, steps = result
    text = answer if isinstance(answer, str) else ""
    by_kind, flaky = _expected()
    weakest = min(by_kind, key=lambda k: by_kind[k])
    # Протёкшие случаи гонять и не надо — считаем покрытие по остальным.
    per_case = {
        c["id"]: len({r for k, r in SEEN if k == c["id"]})
        for c in CASES if c["id"] not in IN_PROMPT
    }
    covered = min(per_case.values()) if per_case else 0
    return [
        (sorted(set(WHO)) == ["независимый"], f"кто судил: {', '.join(sorted(set(WHO))) or 'никто'}"),
        (set(LOOKED) == {c["id"] for c in CASES},
         f"проверено на утечку: {len(set(LOOKED))} из {len(CASES)}"),
        (covered == RUNS, f"прогонов на случай: {covered} из {RUNS}"),
        (f"{weakest} {by_kind[weakest]}%" in text,
         f"слабый вид: {weakest} {by_kind[weakest]}% — {'назван' if f'{weakest} {by_kind[weakest]}%' in text else 'нет'}"),
        ("выкатывать нельзя" in text, f"решение: {text or 'нет ответа'}"),
        (steps <= 2, f"обращений к модели: {steps} (допустимо 2)"),
    ]
