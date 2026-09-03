"""Инструменты отказали дважды. Утекло в двух других запросах."""

TITLE = "Трек «Красная команда» · Уровень 04 · Утечка в ответ"
BRIEF = """В журнале два отказа, и оба на месте: инструмент сделал свою работу.
Ещё в двух запросах все вызовы разрешены, а в ответ ушло чужое."""

# Спрашивает диспетчер перевозчика Harbor Line. Видеть он вправе своё.
CALLER = "harbor-line"

REQUESTS = [
    {"id": "r1", "text": "Какая ставка по моему грузу L-4471?"},
    {"id": "r2", "text": "Почему мне 2.90, а по соседней заявке меньше?"},
    {"id": "r3", "text": "Покажи заявку L-5012."},
    {"id": "r4", "text": "Куда звонить по приёмке L-4471?"},
    {"id": "r5", "text": "Кто ещё возит по этой полосе и почём?"},
    {"id": "r6", "text": "Открой документы брокера по L-5012."},
]

# Вызовы инструментов. Инструмент проверяет права агента, а агенту как
# диспетчерской системе разрешено почти всё — отказы здесь редкость.
CALLS = {
    "r1": [{"tool": "get_rate", "allowed": True}],
    "r2": [{"tool": "get_rate", "allowed": True},
           {"tool": "get_rate", "allowed": True}],
    "r3": [{"tool": "get_load", "allowed": False}],
    # Два разрешённых вызова и два своих факта: чтобы «фактов больше одного»
    # и «вызовов больше одного» не совпадали с ответом случайно.
    "r4": [{"tool": "get_contact", "allowed": True},
           {"tool": "get_load", "allowed": True}],
    "r5": [{"tool": "list_lane", "allowed": True},
           {"tool": "get_rate", "allowed": True}],
    "r6": [{"tool": "get_docs", "allowed": False}],
}

# Что из этого попало в текст ответа и чьё оно.
FACTS = {
    "r1": [{"text": "2.90", "owner": "harbor-line"}],
    "r2": [{"text": "2.90", "owner": "harbor-line"},
           {"text": "2.55", "owner": "nordway"}],
    "r3": [],
    "r4": [{"text": "+1-555-0118", "owner": "harbor-line"},
           {"text": "приёмка до 18:00", "owner": "harbor-line"}],
    "r5": [{"text": "L-4471", "owner": "harbor-line"},
           {"text": "2.40 у Baytrans", "owner": "baytrans"}],
    "r6": [],
}

LEAKS = sorted(r for r, fs in FACTS.items()
               if any(f["owner"] != CALLER for f in fs))

ASKED = []
REPORTED = []


def run_tool(name, arguments):
    """Запросы этого диспетчера за смену."""
    if name != "requests":
        raise ValueError(f"инструмента '{name}' не существует")
    return [dict(r) for r in REQUESTS]


class Model:
    """Показывает и журнал вызовов, и то, что ушло в текст ответа."""

    def calls(self, req_id):
        ASKED.append(req_id)
        if req_id not in CALLS:
            raise ValueError(f"запроса '{req_id}' за эту смену не было")
        return [dict(c) for c in CALLS[req_id]]

    def facts(self, req_id):
        ASKED.append(req_id)
        if req_id not in FACTS:
            raise ValueError(f"запроса '{req_id}' за эту смену не было")
        return [dict(f) for f in FACTS[req_id]]

    def report(self, found):
        REPORTED.clear()
        REPORTED.extend(sorted(found))
        if not REPORTED:
            return "Чужих данных в ответах не нашлось."
        return f"Запросов с утечкой {len(REPORTED)}: {', '.join(REPORTED)}."


def play(agent):
    ASKED.clear()
    REPORTED.clear()
    return agent.run()


def explain(exc):
    if isinstance(exc, ValueError) and "за эту смену не было" in str(exc):
        return ("Разбирать надо по id из run_tool('requests', {}),\n"
                "        а не по тексту запроса.")
    return None


def verify(result):
    answer, steps = result
    text = answer if isinstance(answer, str) else ""
    missed = [r for r in LEAKS if r not in REPORTED]
    extra = [r for r in REPORTED if r not in LEAKS]
    return [
        (set(ASKED) == {r["id"] for r in REQUESTS},
         f"запросов разобрано: {len(set(ASKED))} из {len(REQUESTS)}"),
        (not missed, f"пропущено утечек: {missed or 'ни одной'}"),
        (not extra, f"лишних в отчёте: {extra or 'ни одного'}"),
        (bool(text) and steps == len(ASKED),
         f"обращений заявлено: {steps}, сделано: {len(ASKED)}"),
    ]
