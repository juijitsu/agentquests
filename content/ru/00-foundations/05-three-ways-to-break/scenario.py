"""Смена пятая. Диспетчер завис на запросе, который не может выполнить."""

from engine.kit import Response, ToolCall

TITLE = "Уровень 05 · Три способа сломаться"
BRIEF = """Достык не отвечает третьи сутки. Диспетчер спрашивает про него
снова и снова, пока не упрётся в потолок итераций."""

LIMIT = 10  # столько итераций отпущено агенту

TOOLS = [{
    "name": "check_border_status",
    "description": "Показывает очередь на погранпереходе. Значения: Хоргос, Достык, Актау.",
    "parameters": {"crossing": "string"},
}]


def run_tool(name, arguments):
    if name == "check_border_status":
        return "данные временно недоступны, повторите запрос"
    return f"инструмента '{name}' не существует"


class Model:
    """Никогда не заканчивает: инструмент отвечает бесполезным, она пробует снова."""

    def call(self, messages, tools):
        return Response(tool_calls=[ToolCall("check_border_status", {"crossing": "Достык"})])


def play(agent):
    return agent.run("Что с очередью на Достыке?")


def explain(exc):
    return ("Агент упал с исключением вместо того, чтобы объяснить, что случилось.\n"
            "        Исчерпание лимита — штатная ситуация, а не авария: она должна\n"
            "        возвращаться человеку понятным сообщением.")


def verify(result):
    answer, steps = result
    text = answer if isinstance(answer, str) else ""
    return [
        (steps == LIMIT, f"дошёл до потолка: {steps} итераций из {LIMIT}"),
        (str(LIMIT) in text, "в сообщении названо число потраченных шагов"),
        ("check_border_status" in text, "в сообщении назван последний вызванный инструмент"),
    ]
