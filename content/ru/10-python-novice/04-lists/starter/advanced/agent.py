"""Уровень 04 · продвинутый.

    solve([1200, 900, 1450]) -> 1200
"""


def solve(quotes: list[int]) -> int:
    # Берётся середина списка, а список никто не выстраивал по возрастанию.
    middle = len(quotes) // 2
    return quotes[middle]
