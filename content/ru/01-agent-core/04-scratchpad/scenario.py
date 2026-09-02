"""Четвёртая смена. Важное выясняется в середине пути, а не в заявке."""

import re

from engine.kit import Response, ToolCall

TITLE = "Агентный трек · Уровень 04 · Блокнот агента"
BRIEF = """На третьем перегоне выясняется ограничение по весу на мосту.
В заявке его не было — а к концу маршрута про него уже никто не помнит."""

# Мост на втором перегоне, маршрут длинный: к финалу факт о нём уезжает из хвоста.
LEGS = ["Laredo", "San Antonio", "Austin", "Dallas", "Little Rock", "Nashville", "Newark"]
BRIDGE_LEG = "San Antonio"
BRIDGE_LIMIT = 20
WINDOW = 8
NOTES = []
DRIVEN = []

TOOLS = [
    {
        "name": "drive_leg",
        "description": "Проезжает перегон маршрута и сообщает обстановку на нём.",
        "parameters": {"leg": "string"},
    },
    {
        "name": "write_note",
        "description": "Записывает в блокнот факт, который понадобится позже.",
        "parameters": {"text": "string"},
    },
]


def run_tool(name, arguments):
    if name == "drive_leg":
        leg = arguments["leg"]
        if leg not in LEGS:
            raise ValueError(f"перегона '{leg}' нет в маршруте")
        DRIVEN.append(leg)
        if leg == BRIDGE_LEG:
            return f"{leg}: проехали. Ограничение на мосту — до {BRIDGE_LIMIT} тонн"
        return f"{leg}: проехали, ограничений нет"
    if name == "write_note":
        NOTES.append(arguments["text"])
        return "записано"
    raise ValueError(f"инструмента '{name}' не существует")


def _weight(messages):
    for m in messages:
        found = re.search(r"(\d+)\s*тонн", str(m.get("content", "")))
        if found:
            return int(found.group(1))
    return None


class Model:
    """Замечает ограничение и записывает его. В конце решает по тому, что видит."""

    def __init__(self):
        self.done = 0
        self.noted = False

    def call(self, messages, tools):
        if len(messages) > WINDOW:
            raise ValueError(f"контекст переполнен: {len(messages)} при лимите {WINDOW}")

        last = next((m["content"] for m in reversed(messages) if m.get("role") == "tool"), "")
        if "Ограничение" in str(last) and not self.noted:
            self.noted = True
            return Response(tool_calls=[ToolCall("write_note", {"text": str(last)})])

        if self.done < len(LEGS):
            leg = LEGS[self.done]
            self.done += 1
            return Response(tool_calls=[ToolCall("drive_leg", {"leg": leg})])

        weight = _weight(messages)
        seen_limit = re.search(r"до (\d+) тонн", " ".join(str(m.get("content", "")) for m in messages))
        if weight and seen_limit and weight > int(seen_limit.group(1)):
            return Response(text=(
                f"Маршрут не подходит: на мосту ограничение {seen_limit.group(1)} тонн, "
                f"а груз {weight} тонн."
            ))
        return Response(text="Маршрут свободен, ограничений не обнаружено.")


def play(agent):
    NOTES.clear()
    DRIVEN.clear()
    return agent.run("Груз 25 тонн. Проведи по маршруту и скажи, пройдёт ли он.")


def explain(exc):
    if isinstance(exc, ValueError) and "переполнен" in str(exc):
        return ("Окно переполнено. Блокнот подставляется в окно вместе с условием\n"
                "        и хвостом — на все три места нужно оставить запас.")
    return None


def verify(result):
    answer, steps = result
    return [
        (DRIVEN == LEGS, f"перегонов пройдено: {len(DRIVEN)} из {len(LEGS)}"),
        (len(NOTES) == 1, f"записей в блокноте: {len(NOTES)}"),
        (isinstance(answer, str) and "не подходит" in answer, f"ответ агента: {answer}"),
        (steps <= 12, f"итераций потрачено: {steps} (допустимо 12)"),
    ]
