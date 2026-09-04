"""Level 02 · novice.

    solve("1450") -> "1450 + 60 = 1510"
"""


def solve(miles: str) -> str:
    # TODO: miles is text, so miles + "60" glues the digits instead of adding
    #       them: "1450" + "60" gives "145060", while 1450 + 60 gives 1510.
    #       First make a number out of the text:   loaded = int(miles)
    #       Add to the number, not to the text:    total = loaded + 60
    #       To put the number back into a string:  str(total)
    total = miles + "60"
    return miles + " + 60 = " + total
