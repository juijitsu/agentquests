"""Level 02 · reference."""


def solve(miles: str) -> str:
    loaded = int(miles)                     # the text "1450" became the number 1450
    total = loaded + 60                     # numbers add: 1510
    return miles + " + 60 = " + str(total)  # str() lets the number back into text
