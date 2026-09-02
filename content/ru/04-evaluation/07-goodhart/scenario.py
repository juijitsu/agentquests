"""Седьмая смена трека. Метрика выросла вдвое, система стала опаснее."""

TITLE = "Трек «Оценка» · Уровень 07 · Метрика оптимизируется, цель нет"
BRIEF = """Прошлый уровень боролся с уклончивостью, и её измерили долей
конкретных ответов. Новая версия конкретна всегда — включая три выдумки."""

CASES = [
    {"id": "c1", "expected": "2.90"},
    {"id": "c2", "expected": "18 т"},
    {"id": "c3", "expected": "0.35"},
    {"id": "c4", "expected": "18:00"},
    {"id": "c5", "expected": "24 т"},
    {"id": "c6", "expected": "нет данных"},
    {"id": "c7", "expected": "нет данных"},
    {"id": "c8", "expected": "нет данных"},
]

# Старая: конкретна там, где знает, и честно уклоняется там, где нет.
OLD = {"c1": "2.90", "c2": "18 т", "c3": "0.35", "c4": "не уверен",
       "c5": "24 т", "c6": "нет данных", "c7": "нет данных",
       "c8": "не уверен"}
# Новая: конкретна всегда. Три последние конкретности — выдуманы.
NEW = {"c1": "2.90", "c2": "18 т", "c3": "0.35", "c4": "18:00",
       "c5": "24 т", "c6": "3.15", "c7": "22 т", "c8": "19:30"}

HEDGES = {"не уверен", "нет данных"}
CHECKED_GOAL = []


def run_tool(name, arguments):
    if name != "answer":
        raise ValueError(f"инструмента '{name}' не существует")
    table = {"old": OLD, "new": NEW}.get(arguments["version"])
    if table is None:
        raise ValueError(f"версии '{arguments['version']}' не существует")
    return table[arguments["case"]]


class Model:
    """Умеет мерить и метрику, и цель. Спросить надо обе."""

    def is_specific(self, answer):
        """Метрика: назван ли конкретный ответ вместо уклончивого."""
        return answer not in HEDGES

    def is_correct(self, expected, answer):
        """Цель: верен ли ответ. Уклончивое «не уверен» неверно, но безвредно."""
        CHECKED_GOAL.append((expected, answer))
        return answer == expected

    def report(self, metric, harm):
        return (
            f"Конкретность: старая {metric['old']}%, новая {metric['new']}%. "
            f"Уверенных ошибок: старая {harm['old']}, новая {harm['new']}. "
            f"Метрика выросла, цель — нет."
        )


def play(agent):
    CHECKED_GOAL.clear()
    return agent.run()


def explain(exc):
    if isinstance(exc, KeyError) and "old" in str(exc):
        return ("report ждёт два словаря с ключами old и new:\n"
                "        отдельно проценты метрики и отдельно число ошибок.")
    return None


def _harm(table):
    return sum(
        1 for c in CASES
        if table[c["id"]] not in HEDGES and table[c["id"]] != c["expected"]
    )


def verify(result):
    answer, steps = result
    text = answer if isinstance(answer, str) else ""
    harm_new = _harm(NEW)
    return [
        (bool(CHECKED_GOAL), f"цель измерялась: {'да' if CHECKED_GOAL else 'нет'}"),
        (f"старая {_harm(OLD)}, новая {harm_new}" in text,
         f"уверенных ошибок: {'сошлись' if f'старая {_harm(OLD)}, новая {harm_new}' in text else 'не сошлись'}"),
        ("Конкретность: старая 50%, новая 100%" in text, f"отчёт: {text or 'нет ответа'}"),
        (steps <= 2, f"обращений к модели: {steps} (допустимо 2)"),
    ]
