"""Финал фундамента. Вам передали чужого агента перед сдачей заказчику."""

import re

from engine.kit import Response, ToolCall

TITLE = "Уровень 08 · Финал: читаем чужого агента"
BRIEF = """Разработчик уволился, агент уходит заказчику в пятницу.
Из пяти обращений проходит не всё."""

CROSSINGS = {"Laredo": "очередь 40 машин", "El Paso": "очередь 12 машин"}
SHIPMENTS = {"TX-4471": "в пути, прибытие через 4 дня", "TX-5120": "на оформлении в Otay Mesa"}

CASES = [
    ("Какая очередь на Laredo?", "очередь 40 машин"),
    ("Что на переходе El Paso?", "очередь 12 машин"),
    ("Где груз TX-4471?", "прибытие через 4 дня"),
    ("Что на переходе Loredo?", "очередь 40 машин"),
    ("Где груз TX-5120?", "на оформлении в Otay Mesa"),
]


def run_tool(name, arguments):
    if name == "check_border_status":
        crossing = arguments["crossing"]
        if crossing not in CROSSINGS:
            raise ValueError(
                f"перехода '{crossing}' не существует. Доступны: {', '.join(CROSSINGS)}"
            )
        return f"переход {crossing}: {CROSSINGS[crossing]}"
    if name == "get_shipment_status":
        code = arguments["shipment_id"]
        if code not in SHIPMENTS:
            raise ValueError(f"груза '{code}' нет в системе")
        return f"груз {code}: {SHIPMENTS[code]}"
    raise ValueError(f"инструмента '{name}' не существует")


def _score(query, tool):
    # Порог в четыре символа, а не пять: в «Где груз TX-4471?» нет слов длиннее.
    words = {w[:5] for w in re.findall(r"\w+", query.lower()) if len(w) >= 4}
    text = (tool["name"] + " " + tool["description"]).lower()
    return sum(1 for w in words if w in text)


def _arguments(name, query):
    if name == "get_shipment_status":
        found = re.search(r"TX-\d+", query)
        return {"shipment_id": found.group() if found else "TX-0000"}
    for crossing in CROSSINGS:
        if crossing.lower() in query.lower():
            return {"crossing": crossing}
    return {"crossing": "Loredo"}  # так, как написал клиент


class Model:
    """Выбирает инструмент по описанию и умеет исправиться, если ей сказали как."""

    def call(self, messages, tools):
        notes = [m["content"] for m in messages if m.get("role") == "tool"]
        if notes and "не существует" in notes[-1]:
            return Response(tool_calls=[ToolCall("check_border_status", {"crossing": "Laredo"})])
        if notes:
            return Response(text=f"По вашему запросу: {notes[-1]}")
        query = messages[0]["content"]
        best = max(tools, key=lambda t: _score(query, t))
        return Response(tool_calls=[ToolCall(best["name"], _arguments(best["name"], query))])


def play(agent):
    passed, report = 0, []
    for question, expected in CASES:
        try:
            answer, _ = agent.run(question)
        except Exception as exc:
            report.append(f"«{question}» → упал: {type(exc).__name__}")
            continue
        if isinstance(answer, str) and expected in answer:
            passed += 1
        else:
            report.append(f"«{question}» → {answer}")
    return passed, report


def verify(result):
    passed, report = result
    lines = [(passed == len(CASES), f"обращений проходит: {passed} из {len(CASES)}")]
    lines += [(False, f"  {line}") for line in report[:3]]
    return lines
