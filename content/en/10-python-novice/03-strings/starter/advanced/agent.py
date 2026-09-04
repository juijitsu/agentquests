"""Level 03 · advanced.

    solve("  dallas run 47 ") -> "DAL47"
"""


def solve(text: str) -> str:
    # The cleaning is done, but the result is put nowhere, so the dirty label
    # is what gets cut.
    text.strip()
    text.upper()
    return text[:3] + text[-2:]
