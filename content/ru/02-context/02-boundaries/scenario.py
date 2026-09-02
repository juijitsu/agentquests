"""Вторая смена трека. Отбор выдрал строки из документов вместе с границами."""

import re

TITLE = "Трек «Контекст» · Уровень 02 · Границы источников"
BRIEF = """Три тарифа, три строки про рефрижератор, ни одной подписи.
Надбавку соседа модель записывает на «Дельту»."""

BUDGET = 4

SHEETS = {
    "Ридж": [
        "ставка 2.40 за милю",
        "рефрижератор +0.60",
        "минимальный заказ 300 миль",
    ],
    "Дельта": [
        "ставка 2.10 за милю",
        "рефрижераторы не возим",
        "минимальный заказ 150 миль",
    ],
    "Кассель": [
        "ставка 2.85 за милю",
        "рефрижератор +0.35",
        "минимальный заказ 500 миль",
    ],
}
OWNER = {line: who for who, lines in SHEETS.items() for line in lines}

QUESTION = "Возьмёт ли Дельта рефрижератор и почём?"
PASSED = []


def run_tool(name, arguments):
    if name == "about":
        topic = arguments["topic"].lower()
        found = [line for line in OWNER if topic in line.lower()]
        return " | ".join(found) if found else "по этой теме строк нет"
    if name == "source":
        line = arguments["line"]
        if line not in OWNER:
            raise ValueError(f"строка '{line}' не из наших тарифов")
        return OWNER[line]
    raise ValueError(f"инструмента '{name}' не существует")


class Model:
    """Привязывает факт к подписи. Нет подписи — привязывает к первой строке."""

    def topic(self, question):
        return "рефрижератор"

    def ask(self, question, blocks):
        PASSED.clear()
        PASSED.extend(blocks)
        who = next((c for c in SHEETS if c in question), "перевозчик")

        signed = [b for b in blocks if b.startswith(f"{who}:")]
        line = signed[0] if signed else (blocks[0] if blocks else "")

        if "не возим" in line:
            return f"{who} рефрижераторы не возит."
        rate = re.search(r"\+([\d.]+)", line)
        if rate:
            return f"{who} возит рефрижератор, надбавка {rate.group(1)} за милю."
        return f"По {who} ничего не нашёл."


def play(agent):
    PASSED.clear()
    return agent.run(QUESTION)


def explain(exc):
    if isinstance(exc, ValueError) and "не из наших тарифов" in str(exc):
        return ("Инструмент source ждёт строку ровно в том виде, в каком её\n"
                "        вернул about — без добавленной подписи.")
    return None


def verify(result):
    answer, steps = result
    text = answer if isinstance(answer, str) else ""
    marks = tuple(f"{who}:" for who in SHEETS)
    signed = [b for b in PASSED if b.startswith(marks)]
    return [
        (PASSED and len(signed) == len(PASSED),
         f"подписано источником: {len(signed)} из {len(PASSED)} блоков"),
        ("не возит" in text, f"ответ агента: {text}"),
        (PASSED and len(PASSED) <= BUDGET,
         f"блоков отправлено: {len(PASSED)} (допустимо {BUDGET})"),
        (steps <= 2, f"обращений к модели: {steps} (допустимо 2)"),
    ]
