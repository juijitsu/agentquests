"""Десятая смена. Диспетчер целиком: очередь, человек, крах."""

from engine.kit import Response, ToolCall

TITLE = "Агентный трек · Уровень 10 · Босс: диспетчер целиком"
BRIEF = """Одна смена от побудки до отчёта. Очередь растёт на ходу,
необратимое требует человека, процесс умирает после согласования."""

EMPTY = "очередь пуста"
ATTENTION = 2

INBOX = ["сверить накладную TX-118", "поломка под Мемфисом", "гололёд на I-80"]
HIRE = "нанять стороннего перевозчика за тройную цену"
FOLLOWUP = {"поломка под Мемфисом": HIRE}
IRREVERSIBLE = {HIRE}
EXPECTED = INBOX + [HIRE]

QUEUE = []
HANDLED = []
APPROVED = []
ASKED = []
BLIND = []
KILLED = []
CRASHED = []


class Crash(BaseException):
    """Процесс убит извне. Как и на уровне 08, обычным except его не поймать."""


TOOLS = [
    {"name": "pending", "description": "Что ждёт разбора прямо сейчас.", "parameters": {}},
    {"name": "ask", "description": "Отправляет действие на согласование диспетчеру.",
     "parameters": {"name": "string"}},
    {"name": "handle", "description": "Выполняет действие. Необратимое — платное.",
     "parameters": {"name": "string"}},
]


def run_tool(name, arguments):
    if name == "pending":
        return " | ".join(QUEUE) if QUEUE else EMPTY

    action = arguments["name"]
    if name == "ask":
        ASKED.append(action)
        if len(ASKED) > ATTENTION:
            BLIND.append(action)
        return "да, нанимай"
    if name == "handle":
        if action not in QUEUE:
            raise ValueError(f"'{action}' нет в очереди")
        if action in IRREVERSIBLE and not CRASHED:
            CRASHED.append(True)
            raise Crash("процесс убит между согласованием и исполнением")
        QUEUE.remove(action)
        HANDLED.append(action)
        if action in FOLLOWUP:
            QUEUE.append(FOLLOWUP[action])
            return f"{action}: разобрано. Появилась задача — {FOLLOWUP[action]}"
        return f"{action}: разобрано"
    raise ValueError(f"инструмента '{name}' не существует")


class Model:
    """Судит об обратимости и закрывает смену. Очередь и состояние — не её дело."""

    def judge(self, action):
        return action in IRREVERSIBLE

    def close(self):
        return f"Смена закрыта. Разобрано: {len(HANDLED)}, согласований: {len(ASKED)}."


def play(agent):
    QUEUE.clear()
    QUEUE.extend(INBOX)
    for store in (HANDLED, APPROVED, ASKED, BLIND, KILLED, CRASHED):
        store.clear()
    result = None
    for _ in range(2):
        try:
            result = agent.run()
        except Crash:
            KILLED.append(True)
    return result


def explain(exc):
    if isinstance(exc, ValueError) and "нет в очереди" in str(exc):
        return ("Действие разбирается второй раз. Очередь надо перечитывать,\n"
                "        а не держать снимок, сделанный при побудке.")
    return None


def verify(result):
    answer, steps = result
    text = answer if isinstance(answer, str) else ""
    return [
        (HANDLED == EXPECTED, f"разобрано: {len(HANDLED)} из {len(EXPECTED)}"),
        (set(ASKED) == {HIRE}, f"беспокоили из-за: {', '.join(sorted(set(ASKED))) or 'ничего'}"),
        (len(ASKED) == 1, f"обращений к человеку: {len(ASKED)} (достаточно 1)"),
        (not BLIND, f"согласовано вслепую: {', '.join(BLIND) or 'ничего'}"),
        (f"Разобрано: {len(EXPECTED)}" in text, f"отчёт: {text}"),
        (steps <= 6, f"итераций во втором заходе: {steps} (допустимо 6)"),
    ]
