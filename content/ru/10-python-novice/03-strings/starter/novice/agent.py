"""Уровень 03 · новичок.

    solve("  dallas run 47 ") -> "DAL47"
"""


def solve(text: str) -> str:
    # TODO: две строки ниже работают вхолостую. text.strip() и text.upper()
    #       не меняют text — они возвращают НОВУЮ строку, а её здесь никто
    #       не ловит, поэтому режется по-прежнему грязная метка.
    #       Поймайте результат в имя:      clean = text.strip()
    #       И следующий тоже:              code = clean.upper()
    #       Режьте уже чистую строку:      code[:3] + code[-2:]
    text.strip()
    text.upper()
    return text[:3] + text[-2:]
