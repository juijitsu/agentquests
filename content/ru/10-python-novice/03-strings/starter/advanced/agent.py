"""Уровень 03 · продвинутый.

    solve("  dallas run 47 ") -> "DAL47"
"""


def solve(text: str) -> str:
    # Уборка сделана, но результат никуда не положен, и режется грязная метка.
    text.strip()
    text.upper()
    return text[:3] + text[-2:]
