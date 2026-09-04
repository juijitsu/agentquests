"""String methods hand back a new string and leave the old one alone."""

LANG = "en"
ENTRY = "solve"
TITLE = "Python from scratch · Level 03 · The whiteboard label"
BRIEF = """A label off the board has to be cleaned up and turned into a short code.
The task shows four labels; the check runs ten."""

# The first four are shown in the task. The fourth is already clean and in
# capitals: the starter hits it by accident, and the verdict says so — "one of
# ten". The other six are hidden, so there is nothing to fit an answer to.
CASES = [
    ("  dallas run 47 ", "DAL47"),
    ("memphis run 08", "MEM08"),          # clean edges, but lower case
    ("  Reno Run 12", "REN12"),           # spaces on the left, mixed case
    ("OMAHA RUN 33", "OMA33"),            # already clean: the starter guesses it
    ("tulsa run 90   ", "TUL90"),         # spaces on the right
    ("\nlittle rock run 21\n", "LIT21"),  # newlines around the edges
    ("   fargo run 05", "FAR05"),
    ("Boise Run 76 ", "BOI76"),
    ("el paso run 60", "EL 60"),          # the first word is under three letters
    ("  cheyenne run 14  ", "CHE14"),
]


def play(agent):
    return [agent.solve(text) for text, _ in CASES], len(CASES)


def explain(exc):
    name = type(exc).__name__
    text = str(exc)
    if name == "AttributeError" and "solve" in text:
        return ("There is no function called solve in the file. It has to have\n"
                "        exactly that name: that is how the check calls it.")
    if name == "TypeError" and "not subscriptable" in text:
        return ("A method is called with brackets: text.strip(), not\n"
                "        text.strip. Without them it is the method itself,\n"
                "        and you cannot slice that.")
    if name == "TypeError" and "not callable" in text:
        return ("There are brackets where nothing is being called. That happens\n"
                "        when an operator went missing before an opening bracket.")
    if name == "TypeError" and "concatenate" in text:
        return ("A plus joins two pieces of text. One of the sides is not text\n"
                "        — carry it over with str().")
    if name == "AttributeError" and "has no attribute" in text:
        return ("A string has no such method — usually a typo in the name:\n"
                "        strip, upper, lower, replace are spelled out in full.")
    if name == "IndexError":
        return ("A single index ran past the end of the string. A slice like\n"
                "        code[:3] never does that; code[3] on a short one does.")
    if name == "IndentationError":
        return ("The body of a function has to be indented four spaces\n"
                "        further than the def line.")
    if name == "SyntaxError":
        return ("Python could not read the file: an unclosed quote or bracket,\n"
                "        or a missing colon after def solve(text).")
    if name == "NameError":
        return (f"The name in the error does not exist: {text}.\n"
                "        If it is meant to be text, it needs quotes around it.")
    return None


def _diff(expected, got):
    """Spaces at the edges and newlines are invisible in printed output, so
    both strings are shown through repr: the quotes mark the edges and a
    newline shows up as \\n. The caret is measured against the same text that
    is printed — otherwise it slides by the length of the escaping."""
    left, right = repr(expected), repr(got)
    limit = min(len(left), len(right))
    at = next((i for i in range(limit) if left[i] != right[i]), limit)
    return ("\n        expected: " + left +
            "\n        got:      " + right +
            "\n        " + " " * (10 + at) + "^")


def verify(result):
    got, total = result

    wrong_type = [text for (text, _), g in zip(CASES, got) if not isinstance(g, str)]
    wrong = [(text, expected, g) for (text, expected), g in zip(CASES, got)
             if isinstance(g, str) and g != expected]
    right = total - len(wrong_type) - len(wrong)

    if wrong_type:
        first = f"on the label {wrong_type[0]!r} the result was not text"
    elif wrong:
        text, expected, g = wrong[0]
        first = f"on the label {text!r}" + _diff(expected, g)
    else:
        first = "all matched"

    return [
        (not wrong_type,
         f"returned text: {'yes' if not wrong_type else 'no, ' + str(len(wrong_type)) + ' of ' + str(total)}"),
        (right == total, f"labels matched: {right} of {total}"),
        (not wrong_type and not wrong, f"first difference: {first}"),
    ]
