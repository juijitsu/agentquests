"""Level 04 · reference."""


def solve(quotes: list[int]) -> int:
    in_order = sorted(quotes)     # a new list, the bids in ascending order
    middle = len(in_order) // 2   # the number of the middle: whole division
    return in_order[middle]
