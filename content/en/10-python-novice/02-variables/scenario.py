"""Text that looks like a number is not a number."""

LANG = "en"
ENTRY = "solve"
TITLE = "Python from scratch · Level 02 · Add the deadhead"
BRIEF = """The miles arrive from the board as text, and a number has to be added to them.
The task shows two loads; the check runs six."""

# The first two are shown in the task and deliberately dull: the answer is the
# same length as the input. Everything interesting is hidden, and that is what
# fitting an answer to the examples breaks on.
CASES = [
    ("1450", "1450 + 60 = 1510"),
    ("300", "300 + 60 = 360"),
    ("9", "9 + 60 = 69"),          # the answer is longer than the input
    ("40", "40 + 60 = 100"),       # the carry changes the length
    ("0", "0 + 60 = 60"),          # the input digit vanishes from the sum
    ("1234567", "1234567 + 60 = 1234627"),  # the carry lands in the middle
]


def play(agent):
    return [agent.solve(miles) for miles, _ in CASES], len(CASES)


def explain(exc):
    name = type(exc).__name__
    text = str(exc)
    if name == "TypeError" and "concatenate" in text:
        return ("Text and a number cannot be added. The number has to become\n"
                "        text first: str(number). Or the text a number: int(text).")
    if name == "TypeError" and "unsupported operand" in text:
        return ("Python does not understand a plus between a number and text.\n"
                "        Both sides have to be of one kind: both numbers or both text.")
    if name == "ValueError" and "invalid literal" in text:
        return ("int() takes text made of digits and nothing else. Something\n"
                "        else got in: a space, a sign or a letter.")
    if name == "IndentationError":
        return ("The body of a function has to be indented four spaces\n"
                "        further than the def line.")
    if name == "SyntaxError":
        return ("Python could not read the file: an unclosed quote or bracket,\n"
                "        or a missing colon after def solve(miles).")
    if name == "NameError":
        return (f"The name in the error does not exist: {text}.\n"
                "        If it is meant to be text, it needs quotes around it.")
    if name == "AttributeError" and "solve" in text:
        return ("There is no function called solve in the file. It has to have\n"
                "        exactly that name: that is how the check calls it.")
    return None


def _diff(expected, got):
    """Two similar strings side by side do not read: show where they part."""
    limit = min(len(expected), len(got))
    at = next((i for i in range(limit) if expected[i] != got[i]), limit)
    return ("\n        expected: " + expected +
            "\n        got:      " + got +
            "\n        " + " " * (10 + at) + "^")


def verify(result):
    got, total = result

    wrong_type = [miles for (miles, _), g in zip(CASES, got) if not isinstance(g, str)]
    wrong = [(miles, expected, g) for (miles, expected), g in zip(CASES, got)
             if isinstance(g, str) and g != expected]
    right = total - len(wrong_type) - len(wrong)

    if wrong_type:
        first = f"on the miles \"{wrong_type[0]}\" the result was not text"
    elif wrong:
        miles, expected, g = wrong[0]
        first = f"on the miles \"{miles}\"" + _diff(expected, g)
    else:
        first = "all matched"

    return [
        (not wrong_type,
         f"returned text: {'yes' if not wrong_type else 'no, ' + str(len(wrong_type)) + ' of ' + str(total)}"),
        (right == total, f"loads matched: {right} of {total}"),
        (not wrong_type and not wrong, f"first difference: {first}"),
    ]
