"""Level 04 · novice.

    solve([1200, 900, 1450]) -> 1200
"""


def solve(quotes: list[int]) -> int:
    # TODO: the middle of the list is not the middle by money. The bids
    #       arrive in whatever order the carriers sent them, and the middle
    #       of a list like that is an accident.
    #       Put the bids in order first:   in_order = sorted(quotes)
    #       Count the middle on that one:  middle = len(in_order) // 2
    #       And take the element from it:  in_order[middle]
    middle = len(quotes) // 2
    return quotes[middle]
