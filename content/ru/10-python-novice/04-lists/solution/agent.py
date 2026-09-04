"""Уровень 04 · эталон."""


def solve(quotes: list[int]) -> int:
    in_order = sorted(quotes)     # новый список, ставки по возрастанию
    middle = len(in_order) // 2   # номер середины: деление нацело
    return in_order[middle]
