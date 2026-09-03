"""Первая смена трека. Проверили поле ввода и решили, что дыр нет."""

TITLE = "Трек «Красная команда» · Уровень 01 · Где можно надавить"
BRIEF = """Поле ввода проверено, инъекций не найдено, отчёт закрыт.
Из шести входов агента три заполняются людьми не из компании."""

# Что агент читает в окно. Кто управляет содержимым — знает только модель:
# в списке этого поля нет намеренно, иначе спрашивать было бы не о чем.
INPUTS = [
    {"id": "question", "text": "вопрос диспетчера"},
    {"id": "shipper_note", "text": "примечание грузоотправителя"},
    {"id": "rate_sheet", "text": "тариф компании"},
    {"id": "consignee_contact", "text": "контакт получателя"},
    {"id": "driver_log", "text": "отметки водителя за смену"},
    {"id": "customs_doc", "text": "документ от таможенного брокера"},
]

# Заполняется без участия вашего сотрудника.
OUTSIDE = sorted(["shipper_note", "consignee_contact", "customs_doc"])
FROM_OUTSIDE = "снаружи"
OUR_OWN = "наша команда"

ASKED = []
REPORTED = []


def run_tool(name, arguments):
    """Список входов агента. Без того, кто ими управляет."""
    if name != "inputs":
        raise ValueError(f"инструмента '{name}' не существует")
    return [dict(i) for i in INPUTS]


class Model:
    """Знает, кто пишет в каждый вход. Спросить надо про каждый."""

    def who_controls(self, input_id):
        ASKED.append(input_id)
        found = next((i for i in INPUTS if i["id"] == input_id), None)
        if found is None:
            raise ValueError(f"входа '{input_id}' у агента нет")
        return FROM_OUTSIDE if input_id in OUTSIDE else OUR_OWN

    def report(self, surface):
        REPORTED.clear()
        REPORTED.extend(sorted(surface))
        if not REPORTED:
            return "Поверхность атаки пуста: снаружи не управляют ничем."
        return (
            f"Поверхность атаки, входов {len(REPORTED)}: {', '.join(REPORTED)}."
        )


def play(agent):
    ASKED.clear()
    REPORTED.clear()
    return agent.run()


def explain(exc):
    if isinstance(exc, ValueError) and "у агента нет" in str(exc):
        return ("Спрашивать надо по id входа из run_tool(\"inputs\"),\n"
                "        а не по его описанию.")
    return None


def verify(result):
    answer, steps = result
    text = answer if isinstance(answer, str) else ""
    extra = [i for i in REPORTED if i not in OUTSIDE]
    missed = [i for i in OUTSIDE if i not in REPORTED]
    return [
        (set(ASKED) == {i["id"] for i in INPUTS},
         f"входов проверено: {len(set(ASKED))} из {len(INPUTS)}"),
        (not missed, f"пропущено входов снаружи: {missed or 'ни одного'}"),
        (not extra, f"лишних входов в поверхности: {extra or 'ни одного'}"),
        (bool(text) and steps <= 2, f"обращений к модели: {steps} (допустимо 2)"),
    ]
