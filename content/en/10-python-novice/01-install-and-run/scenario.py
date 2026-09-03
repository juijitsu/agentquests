"""First run. A program takes an input and returns an output."""

LANG = "en"
# The course entry point: the learner writes solve, not run.
ENTRY = "solve"
TITLE = "Python from scratch · Level 01 · Install and first run"
BRIEF = """The function solve takes a name and must return a greeting.
The task shows two names; the check runs five."""

# Only the first two are shown in the task. The other three are there so that
# the solution has to be a written function, not an answer fitted to examples.
CASES = [
    ("Maria", "Hello, Maria!"),
    ("John", "Hello, John!"),
    ("Kim", "Hello, Kim!"),
    ("Anna-Maria", "Hello, Anna-Maria!"),
    ("Li", "Hello, Li!"),
]


def play(agent):
    return [agent.solve(name) for name, _ in CASES], len(CASES)


def explain(exc):
    """A beginner's first error is usually not about the task but the syntax."""
    name = type(exc).__name__
    text = str(exc)
    if name == "IndentationError":
        return ("The body of a function has to be indented four spaces\n"
                "        further than the def line.")
    if name == "SyntaxError":
        return ("Python could not read the file. Usually that is an unclosed\n"
                "        quote or bracket, or a missing colon after\n"
                "        def solve(name).")
    if name == "NameError":
        return (f"The name in the error does not exist: {text}.\n"
                "        If it is meant to be text, it needs quotes around it.")
    if name == "TypeError" and "str" in text:
        return ("A string and a number cannot be added. Everything joined\n"
                "        with a plus has to be text.")
    if name == "AttributeError" and "solve" in text:
        return ("There is no function called solve in the file. It has to\n"
                "        have exactly that name: that is how the check calls it.")
    return None


def verify(result):
    got, total = result

    wrong_type = [name for (name, _), g in zip(CASES, got) if not isinstance(g, str)]
    wrong = [(name, expected, g) for (name, expected), g in zip(CASES, got)
             if isinstance(g, str) and g != expected]
    right = total - len(wrong_type) - len(wrong)

    if wrong_type:
        first = f"on the name \"{wrong_type[0]}\" the result was not text"
    elif wrong:
        name, expected, g = wrong[0]
        first = f"on the name \"{name}\" expected \"{expected}\", got \"{g}\""
    else:
        first = "all matched"

    return [
        (not wrong_type,
         f"returned text: {'yes' if not wrong_type else 'no, ' + str(len(wrong_type)) + ' of ' + str(total)}"),
        (right == total, f"names matched: {right} of {total}"),
        (not wrong_type and not wrong, f"first difference: {first}"),
    ]
