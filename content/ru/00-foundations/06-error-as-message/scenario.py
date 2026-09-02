"""Смена шестая. В заявке опечатка, и диспетчер опускает руки."""

from engine.kit import Response, ToolCall

TITLE = "Уровень 06 · Ошибка как сообщение"
BRIEF = """Клиент написал «Хоргус» вместо «Хоргос».
Диспетчер ответил, что перехода не существует, и на этом закончил."""

CROSSINGS = {
    "Хоргос": "очередь 40 машин, ожидание около 6 часов",
    "Достык": "очередь 12 машин, ожидание около 2 часов",
    "Актау": "паром по расписанию, ожидание около суток",
}

ASKED = []  # какие значения агент пробовал

TOOLS = [{
    "name": "check_border_status",
    "description": "Показывает очередь на погранпереходе. Значения: Хоргос, Достык, Актау.",
    "parameters": {"crossing": "string"},
}]


def run_tool(name, arguments):
    if name != "check_border_status":
        raise ValueError(f"инструмента '{name}' не существует")
    crossing = arguments["crossing"]
    ASKED.append(crossing)
    if crossing not in CROSSINGS:
        raise ValueError(
            f"перехода '{crossing}' не существует. "
            f"Доступны: {', '.join(CROSSINGS)}"
        )
    return f"переход {crossing}: {CROSSINGS[crossing]}"


class Model:
    """Сначала повторяет написание из заявки, затем читает подсказку из ошибки."""

    def call(self, messages, tools):
        tool_notes = [m["content"] for m in messages if m.get("role") == "tool"]
        if not tool_notes:
            return Response(tool_calls=[ToolCall("check_border_status", {"crossing": "Хоргус"})])
        if "не существует" in tool_notes[-1]:
            return Response(tool_calls=[ToolCall("check_border_status", {"crossing": "Хоргос"})])
        return Response(text=f"По вашему запросу: {tool_notes[-1]}")


def play(agent):
    ASKED.clear()
    return agent.run("Что сейчас на переходе Хоргус?")


def explain(exc):
    if isinstance(exc, ValueError):
        return ("Инструмент отказался работать с неверным аргументом, и исключение\n"
                "        прошло сквозь цикл наружу. Модель об этом так и не узнала —\n"
                "        а узнав, исправилась бы сама.")
    return None


def verify(result):
    answer, steps = result
    return [
        (len(ASKED) >= 2, f"агент пробовал значения: {ASKED or 'ни одного'}"),
        (isinstance(answer, str) and "очередь" in answer, f"ответ агента: {answer}"),
        (steps <= 3, f"итераций потрачено: {steps} (допустимо 3)"),
    ]
