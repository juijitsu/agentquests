"""Седьмая смена. Работа приходит сама и продолжает приходить."""

from engine.kit import Response, ToolCall

TITLE = "Агентный трек · Уровень 07 · Триггеры и очередь"
BRIEF = """Диспетчера будит не человек, а событие.
Пока он разбирает первые три, приходят ещё два."""

EMPTY = "очередь пуста"
INBOX = ["опоздание TX-118", "поломка под Мемфисом", "гололёд на I-80"]
FOLLOWUP = {
    "поломка под Мемфисом": "перецепить груз TX-441",
    "гололёд на I-80": "объезд для TX-903",
}
EXPECTED = INBOX + ["перецепить груз TX-441", "объезд для TX-903"]

QUEUE = []
HANDLED = []
ASKED = []

TOOLS = [
    {
        "name": "pending",
        "description": "Сообщает, какие события ждут разбора прямо сейчас.",
        "parameters": {},
    },
    {
        "name": "handle",
        "description": "Разбирает одно событие из очереди.",
        "parameters": {"event": "string"},
    },
]


def run_tool(name, arguments):
    if name == "pending":
        ASKED.append(len(QUEUE))
        return " | ".join(QUEUE) if QUEUE else EMPTY
    if name == "handle":
        event = arguments["event"]
        if event not in QUEUE:
            raise ValueError(f"события '{event}' нет в очереди")
        QUEUE.remove(event)
        HANDLED.append(event)
        if event in FOLLOWUP:
            QUEUE.append(FOLLOWUP[event])
            return f"{event}: разобрано. Появилась задача — {FOLLOWUP[event]}"
        return f"{event}: разобрано"
    raise ValueError(f"инструмента '{name}' не существует")


class Model:
    """Разбирает событие, которое ей показали. В очередь сама не смотрит."""

    def call(self, messages, tools, event=None):
        if event:
            return Response(tool_calls=[ToolCall("handle", {"event": event})])
        return Response(text=f"Смена закрыта. Разобрано событий: {len(HANDLED)}.")


def play(agent):
    QUEUE.clear()
    QUEUE.extend(INBOX)
    HANDLED.clear()
    ASKED.clear()
    return agent.run()


def explain(exc):
    if isinstance(exc, TypeError) and "run()" in str(exc):
        return ("У run() на этом уровне нет аргумента: агента не спрашивают,\n"
                "        его будят. Задача приходит из очереди, а не из вопроса.")
    return None


def verify(result):
    answer, steps = result
    text = answer if isinstance(answer, str) else ""
    return [
        (HANDLED == EXPECTED, f"разобрано событий: {len(HANDLED)} из {len(EXPECTED)}"),
        (not QUEUE, f"осталось в ящике: {' | '.join(QUEUE) or 'ничего'}"),
        (len(ASKED) >= len(EXPECTED), f"опросов очереди: {len(ASKED)}, событий: {len(EXPECTED)}"),
        (f"событий: {len(EXPECTED)}" in text, f"ответ агента: {text}"),
        (steps <= 8, f"итераций потрачено: {steps} (допустимо 8)"),
    ]
