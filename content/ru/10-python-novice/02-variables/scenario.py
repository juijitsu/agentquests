"""Текст, похожий на число, числом не является."""

ENTRY = "solve"
TITLE = "Курс «Python: старт» · Уровень 02 · Прибавить порожний пробег"
BRIEF = """Пробег приходит с доски текстом, а прибавить к нему надо число.
В задании показаны две заявки, проверка прогонит шесть."""

# Первые две показаны в задании и нарочно скучные: длина ответа совпадает с
# длиной входа. Всё интересное спрятано — на нём и разваливается подгонка.
CASES = [
    ("1450", "1450 + 60 = 1510"),
    ("300", "300 + 60 = 360"),
    ("9", "9 + 60 = 69"),          # ответ длиннее входа
    ("40", "40 + 60 = 100"),       # перенос меняет длину
    ("0", "0 + 60 = 60"),          # цифра входа исчезает из суммы
    ("1234567", "1234567 + 60 = 1234627"),  # перенос в середине
]


def play(agent):
    return [agent.solve(miles) for miles, _ in CASES], len(CASES)


def explain(exc):
    name = type(exc).__name__
    text = str(exc)
    if name == "TypeError" and "concatenate" in text:
        return ("Текст и число сложить нельзя. Число надо сперва превратить\n"
                "        в текст: str(число). А текст в число — int(текст).")
    if name == "TypeError" and "unsupported operand" in text:
        return ("Плюс между числом и текстом питон не понимает. Обе части\n"
                "        должны быть одного вида: либо оба числа, либо оба текста.")
    if name == "ValueError" and "invalid literal" in text:
        return ("int() принимает только текст из одних цифр. Здесь внутрь\n"
                "        попало что-то ещё — пробел, знак или буква.")
    if name == "IndentationError":
        return ("Тело функции должно быть сдвинуто вправо на четыре пробела\n"
                "        относительно строки def.")
    if name == "SyntaxError":
        return ("Питон не смог прочитать файл: незакрытая кавычка или скобка,\n"
                "        либо пропущенное двоеточие после def solve(miles).")
    if name == "NameError":
        return (f"Имени из ошибки не существует: {text}.\n"
                "        Если это текст, его надо взять в кавычки.")
    if name == "AttributeError" and "solve" in text:
        return ("В файле нет функции solve. Она должна называться именно так:\n"
                "        с этим именем её вызывает проверка.")
    return None


def _diff(expected, got):
    """Две похожие строки рядом не читаются: показываем, где разошлись."""
    limit = min(len(expected), len(got))
    at = next((i for i in range(limit) if expected[i] != got[i]), limit)
    return ("\n        ждали:    " + expected +
            "\n        получили: " + got +
            "\n        " + " " * (10 + at) + "^")


def verify(result):
    got, total = result

    wrong_type = [miles for (miles, _), g in zip(CASES, got) if not isinstance(g, str)]
    wrong = [(miles, expected, g) for (miles, expected), g in zip(CASES, got)
             if isinstance(g, str) and g != expected]
    right = total - len(wrong_type) - len(wrong)

    if wrong_type:
        first = f"на пробеге «{wrong_type[0]}» вернулось не текстовое значение"
    elif wrong:
        miles, expected, g = wrong[0]
        first = f"на пробеге «{miles}»" + _diff(expected, g)
    else:
        first = "все совпали"

    return [
        (not wrong_type,
         f"вернулся текст: {'да' if not wrong_type else 'нет, ' + str(len(wrong_type)) + ' из ' + str(total)}"),
        (right == total, f"совпало заявок: {right} из {total}"),
        (not wrong_type and not wrong, f"первое расхождение: {first}"),
    ]
