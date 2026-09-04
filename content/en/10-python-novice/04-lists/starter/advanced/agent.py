"""Level 04 · advanced.

    solve([1200, 900, 1450]) -> 1200
"""


def solve(quotes: list[int]) -> int:
    # The middle of the list is taken, and nobody put the list in order.
    middle = len(quotes) // 2
    return quotes[middle]
