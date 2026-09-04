"""Строковые методы возвращают новую строку, а старую не трогают."""

LANG = "ru"
ENTRY = "solve"
TITLE = "Python: старт · Уровень 03 · Метка на доске"
BRIEF = """Метку с доски надо привести в порядок и собрать из неё короткий код.
В задании показаны четыре метки, проверка прогонит десять."""

# Первые четыре показаны в задании. Четвёртая уже чистая и заглавными: на ней
# заготовка случайно попадает в ответ, и это видно в вердикте — «одна из
# десяти». Остальные шесть скрыты, и подогнать ответ под показанные нечем.
CASES = [
    ("  dallas run 47 ", "DAL47"),
    ("memphis run 08", "MEM08"),          # чистые края, но строчные буквы
    ("  Reno Run 12", "REN12"),           # пробелы слева и вперемешку регистр
    ("OMAHA RUN 33", "OMA33"),            # уже чистая: заготовка её угадывает
    ("tulsa run 90   ", "TUL90"),         # пробелы справа
    ("\nlittle rock run 21\n", "LIT21"),  # переводы строк по краям
    ("   fargo run 05", "FAR05"),
    ("Boise Run 76 ", "BOI76"),
    ("el paso run 60", "EL 60"),          # первое слово короче трёх букв
    ("  cheyenne run 14  ", "CHE14"),
]


def play(agent):
    return [agent.solve(text) for text, _ in CASES], len(CASES)


def explain(exc):
    name = type(exc).__name__
    text = str(exc)
    if name == "AttributeError" and "solve" in text:
        return ("В файле нет функции solve. Имя должно быть ровно таким:\n"
                "        по нему проверка и вызывает функцию.")
    if name == "TypeError" and "not subscriptable" in text:
        return ("Метод вызывают со скобками: text.strip(), а не text.strip.\n"
                "        Без скобок это сам метод, у него нельзя взять срез.")
    if name == "TypeError" and "not callable" in text:
        return ("Скобки стоят там, где вызова нет. Так бывает, если между\n"
                "        значением и скобкой пропал знак операции.")
    if name == "TypeError" and "concatenate" in text:
        return ("Плюсом складываются два текста. Справа или слева оказалось\n"
                "        не текстовое значение — переведите его через str().")
    if name == "AttributeError" and "has no attribute" in text:
        return ("У строки нет такого метода — обычно это опечатка в имени:\n"
                "        strip, upper, lower, replace пишутся полностью.")
    if name == "IndexError":
        return ("Одиночный индекс вышел за длину строки. Срез code[:3] так\n"
                "        не падает, а вот code[3] на короткой строке — падает.")
    if name == "IndentationError":
        return ("Тело функции пишут с отступом в четыре пробела от строки\n"
                "        с def.")
    if name == "SyntaxError":
        return ("Python не смог прочитать файл: незакрытая кавычка или\n"
                "        скобка, либо пропало двоеточие после def solve(text).")
    if name == "NameError":
        return (f"Имени из ошибки не существует: {text}.\n"
                "        Если это текст — вокруг него нужны кавычки.")
    return None


def _diff(expected, got):
    """Пробелы по краям и переводы строк в выводе не видно, поэтому обе строки
    показываем через repr: кавычки очерчивают края, перевод строки виден как
    \\n. Каретку считаем по тому же тексту, который напечатан, — иначе она
    съедет ровно на длину экранирования."""
    left, right = repr(expected), repr(got)
    limit = min(len(left), len(right))
    at = next((i for i in range(limit) if left[i] != right[i]), limit)
    return ("\n        ждали:   " + left +
            "\n        пришло:  " + right +
            "\n        " + " " * (9 + at) + "^")


def verify(result):
    got, total = result

    wrong_type = [text for (text, _), g in zip(CASES, got) if not isinstance(g, str)]
    wrong = [(text, expected, g) for (text, expected), g in zip(CASES, got)
             if isinstance(g, str) and g != expected]
    right = total - len(wrong_type) - len(wrong)

    if wrong_type:
        first = f"на метке {wrong_type[0]!r} вернулся не текст"
    elif wrong:
        text, expected, g = wrong[0]
        first = f"на метке {text!r}" + _diff(expected, g)
    else:
        first = "все совпали"

    return [
        (not wrong_type,
         f"вернулся текст: {'да' if not wrong_type else 'нет, ' + str(len(wrong_type)) + ' из ' + str(total)}"),
        (right == total, f"меток совпало: {right} из {total}"),
        (not wrong_type and not wrong, f"первое расхождение: {first}"),
    ]
