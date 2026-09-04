"""Уровень 02 · эталон."""


def solve(miles: str) -> str:
    loaded = int(miles)                     # текст "1450" стал числом 1450
    total = loaded + 60                     # числа складываются: 1510
    return miles + " + 60 = " + str(total)  # str() пускает число обратно в текст
