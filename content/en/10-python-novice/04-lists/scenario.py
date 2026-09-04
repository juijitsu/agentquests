"""Where an element sits depends on order, and order does not appear by itself."""

LANG = "en"
ENTRY = "solve"
TITLE = "Python from scratch · Level 04 · The middle bid"
BRIEF = """Carriers have sent in their bids for a run. The middle one by rank is wanted, not by money.
The task shows three sets; the check runs nine."""

# The first three are shown in the task. In the second set the middle of the
# list happens to be the middle by rank — the starter guesses that one, and the
# verdict says so. The eighth set holds a single bid: it checks that the code
# does not fall over when there is nothing to sort.
CASES = [
    ([1200, 900, 1450], 1200),
    ([700, 1100, 950, 800, 1300], 950),      # the starter guesses: the middle is already in place
    ([2400, 1800, 2150], 2150),
    ([3000, 500, 900, 1200, 2600], 1200),
    ([450, 480, 460], 460),                  # close bids, order still decides
    ([4000, 3800, 950, 1000, 900], 1000),
    ([600, 2200, 1400, 900, 3100, 1750, 1050], 1400),
    ([1750], 1750),                          # a single bid: nothing to sort
    ([300, 800, 2000, 1500, 1200], 1200),    # nearly in order, but not quite
]


def play(agent):
    # The list is handed over as a copy. Sorting in place is a legitimate
    # solution, but it would reorder our own data, and the verdict would print
    # the sorted set instead of the one that arrived.
    return [agent.solve(list(quotes)) for quotes, _ in CASES], len(CASES)


def explain(exc):
    name = type(exc).__name__
    text = str(exc)
    if name == "AttributeError" and "solve" in text:
        return ("There is no function called solve in the file. It has to have\n"
                "        exactly that name: that is how the check calls it.")
    if name == "TypeError" and "NoneType" in text:
        return ("quotes.sort() returns nothing: it reorders the list in place\n"
                "        and puts None into the name. Either sort in place and\n"
                "        keep working with the same list, or take a new one\n"
                "        with sorted(quotes).")
    if name == "AttributeError" and "sorted" in text:
        return ("sorted is a function, not a method: sorted(quotes), not\n"
                "        quotes.sorted(). The list's own method is called sort().")
    if name == "IndexError":
        return ("An index ran past the end of the list. The middle is\n"
                "        len(quotes) // 2 — with two slashes, or you get\n"
                "        a fraction.")
    if name == "TypeError" and "list indices" in text:
        return ("A list index is a whole number. A single slash gives a\n"
                "        fraction: it has to be len(quotes) // 2, not\n"
                "        len(quotes) / 2.")
    if name == "TypeError" and "'<' not supported" in text:
        return ("Sorting compares the elements with each other, and the list\n"
                "        holds values of different kinds.")
    if name == "IndentationError":
        return ("The body of a function has to be indented four spaces\n"
                "        further than the def line.")
    if name == "SyntaxError":
        return ("Python could not read the file: an unclosed bracket, or a\n"
                "        missing colon after def solve(quotes).")
    if name == "NameError":
        return (f"The name in the error does not exist: {text}.\n"
                "        Check whether it is a typo in a variable name.")
    return None


def verify(result):
    got, total = result

    # A bool is also an int in Python, so it is ruled out separately: True in
    # place of a bid would otherwise pass the check for a number.
    wrong_type = [quotes for (quotes, _), g in zip(CASES, got)
                  if not isinstance(g, int) or isinstance(g, bool)]
    wrong = [(quotes, expected, g) for (quotes, expected), g in zip(CASES, got)
             if isinstance(g, int) and not isinstance(g, bool) and g != expected]
    right = total - len(wrong_type) - len(wrong)

    if wrong_type:
        first = f"on the bids {wrong_type[0]} the result was not a whole number"
    elif wrong:
        quotes, expected, g = wrong[0]
        # The sorted set in the verdict is the whole lesson: you can see that
        # the middle of the list and the middle by rank sit in different places.
        first = (f"on the bids {quotes}"
                 f"\n        in order: {sorted(quotes)}"
                 f"\n        expected: {expected}"
                 f"\n        got:      {g}")
    else:
        first = "all matched"

    return [
        (not wrong_type,
         f"returned a number: {'yes' if not wrong_type else 'no, ' + str(len(wrong_type)) + ' of ' + str(total)}"),
        (right == total, f"sets matched: {right} of {total}"),
        (not wrong_type and not wrong, f"first difference: {first}"),
    ]
