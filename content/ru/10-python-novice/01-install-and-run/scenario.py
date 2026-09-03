"""Первый запуск. Программа получает вход и возвращает выход."""

# Точка входа курса: ученик пишет solve, а не run.
ENTRY = "solve"
TITLE = "Курс «Python: старт» · Уровень 01 · Установка и первый запуск"
BRIEF = """Функция solve получает имя и должна вернуть приветствие.
В задании показаны два имени, проверка прогонит пять."""

# В условии показаны только первые два. Остальные три нужны, чтобы решением
# была написанная функция, а не подогнанный под примеры ответ.
CASES = [
    ("Мария", "Привет, Мария!"),
    ("Иван", "Привет, Иван!"),
    ("Ким", "Привет, Ким!"),
    ("Анна-Мария", "Привет, Анна-Мария!"),
    ("Ли", "Привет, Ли!"),
]


def play(agent):
    return [agent.solve(name) for name, _ in CASES], len(CASES)


def explain(exc):
    """Первая ошибка новичка обычно не про задачу, а про синтаксис."""
    name = type(exc).__name__
    text = str(exc)
    if name == "IndentationError":
        return ("Тело функции должно быть сдвинуто вправо на четыре пробела\n"
                "        относительно строки def.")
    if name == "SyntaxError":
        return ("Питон не смог прочитать файл. Чаще всего это незакрытая\n"
                "        кавычка или скобка, либо пропущенное двоеточие\n"
                "        после def solve(name).")
    if name == "NameError":
        return (f"Имени из ошибки не существует: {text}.\n"
                "        Если это текст, его надо взять в кавычки.")
    if name == "TypeError" and "str" in text:
        return ("Строку и число сложить нельзя. Всё, что склеивается\n"
                "        через плюс, должно быть строкой.")
    if name == "AttributeError" and "solve" in text:
        return ("В файле нет функции solve. Она должна называться именно\n"
                "        так: с этим именем её вызывает проверка.")
    return None


def verify(result):
    got, total = result

    wrong_type = [name for (name, _), g in zip(CASES, got) if not isinstance(g, str)]
    wrong = [(name, expected, g) for (name, expected), g in zip(CASES, got)
             if isinstance(g, str) and g != expected]
    right = total - len(wrong_type) - len(wrong)

    if wrong_type:
        first = f"на имени «{wrong_type[0]}» вернулось не текстовое значение"
    elif wrong:
        name, expected, g = wrong[0]
        first = f"на имени «{name}» ждали «{expected}», получили «{g}»"
    else:
        first = "все совпали"

    return [
        (not wrong_type,
         f"вернулся текст: {'да' if not wrong_type else 'нет, ' + str(len(wrong_type)) + ' из ' + str(total)}"),
        (right == total, f"совпало имён: {right} из {total}"),
        (not wrong_type and not wrong, f"первое расхождение: {first}"),
    ]
