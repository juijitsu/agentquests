"""Девятая смена. Согласующий читает первые два запроса, дальше жмёт «да»."""

from engine.kit import Response, ToolCall

TITLE = "Агентный трек · Уровень 09 · Человек в контуре"
BRIEF = """Диспетчер на смене читает внимательно первые два запроса.
Агент спрашивает про всё — и главное попадает в хвост."""

ATTENTION = 2

ACTIONS = [
    {"name": "сверить накладную TX-118", "irreversible": False},
    {"name": "забронировать слот на складе", "irreversible": False},
    {"name": "перенести время подачи", "irreversible": False},
    {"name": "нанять стороннего перевозчика за тройную цену", "irreversible": True},
]
ROUTINE = [a["name"] for a in ACTIONS if not a["irreversible"]]
COSTLY = next(a["name"] for a in ACTIONS if a["irreversible"])

DONE = []
REFUSED = []
ASKED = []
BLIND = []

TOOLS = [
    {
        "name": "act",
        "description": "Выполняет действие.",
        "parameters": {"name": "string"},
    },
    {
        "name": "ask",
        "description": "Отправляет действие на согласование диспетчеру смены.",
        "parameters": {"name": "string"},
    },
]


def run_tool(name, arguments):
    action = arguments["name"]
    if name == "act":
        DONE.append(action)
        return f"{action}: выполнено"
    if name == "ask":
        ASKED.append(action)
        if len(ASKED) > ATTENTION:
            BLIND.append(action)
            return "да"
        if action == COSTLY:
            return "нет, тройная цена не согласована — вези своим тягачом"
        return "да"
    raise ValueError(f"инструмента '{name}' не существует")


class Model:
    """Предлагает следующее действие и честно говорит, обратимо ли оно."""

    def call(self, messages, tools):
        left = [a for a in ACTIONS if a["name"] not in DONE and a["name"] not in REFUSED]
        if left:
            return Response(tool_calls=[ToolCall("act", dict(left[0]))])
        return Response(
            text=f"Смена закрыта. Выполнено: {len(DONE)}, отклонено: {len(REFUSED)}."
        )


def play(agent):
    for store in (DONE, REFUSED, ASKED, BLIND):
        store.clear()
    return agent.run()


def explain(exc):
    if isinstance(exc, KeyError) and "irreversible" in str(exc):
        return ("Модель кладёт в аргументы вызова поле irreversible —\n"
                "        по нему и решается, нужен ли человек.")
    return None


def verify(result):
    answer, steps = result
    text = answer if isinstance(answer, str) else ""
    return [
        (ASKED == [COSTLY], f"отправлено на согласование: {len(ASKED)} (нужно 1)"),
        (not BLIND, f"согласовано не глядя: {', '.join(BLIND) or 'ничего'}"),
        (COSTLY not in DONE, f"перевозчик нанят: {'да' if COSTLY in DONE else 'нет'}"),
        (DONE == ROUTINE, f"выполнено обратимых: {len(DONE)} из {len(ROUTINE)}"),
        (steps <= 6, f"итераций потрачено: {steps} (допустимо 6)"),
    ]
