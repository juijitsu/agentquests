"""Место элемента зависит от порядка, а порядок сам собой не появляется."""

LANG = "ru"
ENTRY = "solve"
TITLE = "Python: старт · Уровень 04 · Ставка посередине"
BRIEF = """Перевозчики прислали ставки за рейс. Нужна средняя по счёту, а не по деньгам.
В задании показаны три набора, проверка прогонит девять."""

# Первые три показаны в задании. Во втором наборе середина списка случайно
# совпадает с серединой по порядку — на нём заготовка угадывает, и это видно
# в вердикте. Девятый набор из одной ставки: он проверяет, что код не падает,
# когда сортировать нечего.
CASES = [
    ([1200, 900, 1450], 1200),
    ([700, 1100, 950, 800, 1300], 950),      # заготовка угадывает: середина уже на месте
    ([2400, 1800, 2150], 2150),
    ([3000, 500, 900, 1200, 2600], 1200),
    ([450, 480, 460], 460),                  # ставки близкие, порядок всё равно решает
    ([4000, 3800, 950, 1000, 900], 1000),
    ([600, 2200, 1400, 900, 3100, 1750, 1050], 1400),
    ([1750], 1750),                          # одна ставка: сортировать нечего
    ([300, 800, 2000, 1500, 1200], 1200),    # почти по порядку, но не совсем
]


def play(agent):
    # Список передаём копией. Сортировка на месте — законное решение, но она
    # переставила бы наши же данные, и вердикт печатал бы уже отсортированный
    # набор вместо пришедшего.
    return [agent.solve(list(quotes)) for quotes, _ in CASES], len(CASES)


def explain(exc):
    name = type(exc).__name__
    text = str(exc)
    if name == "AttributeError" and "solve" in text:
        return ("В файле нет функции solve. Имя должно быть ровно таким:\n"
                "        по нему проверка и вызывает функцию.")
    if name == "TypeError" and "NoneType" in text:
        return ("quotes.sort() ничего не возвращает: он переставляет список\n"
                "        на месте, а в имя кладёт None. Либо сортируйте на месте\n"
                "        и работайте с тем же списком, либо берите новый через\n"
                "        sorted(quotes).")
    if name == "AttributeError" and "sorted" in text:
        return ("sorted — это функция, а не метод: sorted(quotes), а не\n"
                "        quotes.sorted(). Метод у списка называется sort().")
    if name == "IndexError":
        return ("Индекс вышел за пределы списка. Середина считается как\n"
                "        len(quotes) // 2 — с двумя косыми чертами, иначе\n"
                "        получится дробь.")
    if name == "TypeError" and "list indices" in text:
        return ("Индекс списка — целое число. Одна косая черта даёт дробь:\n"
                "        нужно len(quotes) // 2, а не len(quotes) / 2.")
    if name == "TypeError" and "'<' not supported" in text:
        return ("Сортировка сравнивает элементы между собой, а в списке\n"
                "        оказались значения разных типов.")
    if name == "IndentationError":
        return ("Тело функции пишут с отступом в четыре пробела от строки\n"
                "        с def.")
    if name == "SyntaxError":
        return ("Python не смог прочитать файл: незакрытая скобка или\n"
                "        пропало двоеточие после def solve(quotes).")
    if name == "NameError":
        return (f"Имени из ошибки не существует: {text}.\n"
                "        Проверьте, не опечатка ли это в имени переменной.")
    return None


def verify(result):
    got, total = result

    # bool в Python — тоже int, поэтому его отсекаем отдельно: True вместо
    # ставки прошёл бы проверку на число.
    wrong_type = [quotes for (quotes, _), g in zip(CASES, got)
                  if not isinstance(g, int) or isinstance(g, bool)]
    wrong = [(quotes, expected, g) for (quotes, expected), g in zip(CASES, got)
             if isinstance(g, int) and not isinstance(g, bool) and g != expected]
    right = total - len(wrong_type) - len(wrong)

    if wrong_type:
        first = f"на ставках {wrong_type[0]} вернулось не целое число"
    elif wrong:
        quotes, expected, g = wrong[0]
        # Отсортированный набор в вердикте — это и есть весь урок: видно, что
        # середина списка и середина по порядку стоят в разных местах.
        first = (f"на ставках {quotes}"
                 f"\n        по порядку: {sorted(quotes)}"
                 f"\n        ждали:   {expected}"
                 f"\n        пришло:  {g}")
    else:
        first = "все совпали"

    return [
        (not wrong_type,
         f"вернулось число: {'да' if not wrong_type else 'нет, ' + str(len(wrong_type)) + ' из ' + str(total)}"),
        (right == total, f"наборов совпало: {right} из {total}"),
        (not wrong_type and not wrong, f"первое расхождение: {first}"),
    ]
