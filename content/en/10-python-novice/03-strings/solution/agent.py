"""Level 03 · reference."""


def solve(text: str) -> str:
    clean = text.strip()         # a new string, without the edge whitespace
    code = clean.upper()         # another new string, now in capitals
    return code[:3] + code[-2:]  # the first three characters and the last two
