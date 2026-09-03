"""Промпт проверен вдоль и поперёк. Половину аргументов модель не видела."""

TITLE = "Трек «Красная команда» · Уровень 03 · Чужой аргумент"
BRIEF = """Проверены аргументы, которые сочинила модель, и найден один опасный.
Ещё два подставляет код напрямую из полей, которыми управляют снаружи."""

# Результат уровня 01: входы, которыми управляют снаружи.
SURFACE = sorted(["shipper_note", "consignee_contact", "customs_doc"])

# Аргументы одного вызова агента по заявке L-4471. Откуда взято значение —
# в списке намеренно нет: это и есть то, что надо выяснить.
ARGUMENTS = [
    {"id": "a1", "call": 'quote_rate(rate="2.90")'},
    {"id": "a2", "call": 'quote_rate(weight="18 т")'},
    {"id": "a3", "call": 'send_sheet(to="ops@harbor-line.example")'},
    {"id": "a4", "call": 'notify(text="приёмка после 18:00")'},
    {"id": "a5", "call": 'file_customs(doc_no="CB-77413")'},
    {"id": "a6", "call": 'log(note="запрос диспетчера")'},
]

BY_MODEL = "через модель"
BY_CODE = "подставил код"

# Откуда пришло значение и каким путём. Ось, по которой аргумент опасен, —
# источник. Путь важен только тем, что через код промпт не проходит вовсе.
TRACE = {
    "a1": ("rate_sheet", BY_CODE),
    "a2": ("driver_log", BY_MODEL),
    "a3": ("consignee_contact", BY_CODE),
    "a4": ("shipper_note", BY_MODEL),
    "a5": ("customs_doc", BY_CODE),
    "a6": ("question", BY_MODEL),
}

BORROWED = sorted(a for a, (src, _) in TRACE.items() if src in SURFACE)

TRACED = []
REPORTED = []


def run_tool(name, arguments):
    """Аргументы вызова. Без того, откуда взято значение."""
    if name != "calls":
        raise ValueError(f"инструмента '{name}' не существует")
    return [dict(a) for a in ARGUMENTS]


class Model:
    """Знает, из какого входа пришло значение и каким путём."""

    def trace(self, arg_id):
        TRACED.append(arg_id)
        if arg_id not in TRACE:
            raise ValueError(f"аргумента '{arg_id}' в этом вызове не было")
        source, path = TRACE[arg_id]
        return {"source": source, "path": path}

    def report(self, found):
        REPORTED.clear()
        REPORTED.extend(sorted(found))
        if not REPORTED:
            return "Аргументов, значение которых приходит снаружи, нет."
        return (
            f"Аргументов из поверхности {len(REPORTED)}: {', '.join(REPORTED)}."
        )


def play(agent):
    TRACED.clear()
    REPORTED.clear()
    return agent.run()


def explain(exc):
    if isinstance(exc, ValueError) and "в этом вызове не было" in str(exc):
        return ("Прослеживать надо по id из run_tool('calls', {}),\n"
                "        а не по имени инструмента.")
    return None


def verify(result):
    answer, steps = result
    text = answer if isinstance(answer, str) else ""
    missed = [a for a in BORROWED if a not in REPORTED]
    extra = [a for a in REPORTED if a not in BORROWED]
    return [
        (set(TRACED) == {a["id"] for a in ARGUMENTS},
         f"аргументов прослежено: {len(set(TRACED))} из {len(ARGUMENTS)}"),
        (not missed, f"пропущено аргументов снаружи: {missed or 'ни одного'}"),
        (not extra, f"лишних в отчёте: {extra or 'ни одного'}"),
        (bool(text) and steps == len(TRACED),
         f"обращений заявлено: {steps}, сделано: {len(TRACED)}"),
    ]
