"""Level 03 · novice.

    solve("  dallas run 47 ") -> "DAL47"
"""


def solve(text: str) -> str:
    # TODO: the two lines below run for nothing. text.strip() and
    #       text.upper() do not change text — they hand back a NEW string,
    #       and nobody here catches it, so the cutting still happens on the
    #       dirty label.
    #       Catch the result in a name:      clean = text.strip()
    #       And the next one too:            code = clean.upper()
    #       Cut the clean string:            code[:3] + code[-2:]
    text.strip()
    text.upper()
    return text[:3] + text[-2:]
