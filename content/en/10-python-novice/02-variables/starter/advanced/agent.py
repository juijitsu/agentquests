"""Level 02 · advanced.

    solve("1450") -> "1450 + 60 = 1510"
"""


def solve(miles: str) -> str:
    # The sixty is stuck onto the miles instead of being added to them.
    total = miles + "60"
    return miles + " + 60 = " + total
