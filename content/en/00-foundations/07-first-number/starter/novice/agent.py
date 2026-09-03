"""Level 07 · novice. The set is started, but it covers the same thing twice."""

# The week's complaints log. Each one is a separate kind of request:
#   1. the queue at the Laredo crossing
#   2. the status of shipment TX-4471
#   3. the price of hauling a 12-ton load
#   4. delivery time
#   5. a crossing with a typo in the name — "Loredo"

# A case is a pair: what to ask, and what must appear in the answer.
CASES = [
    ("What is the queue at Laredo?", "queue of 40 trucks"),
    ("What is it like at the Laredo crossing?", "queue of 40 trucks"),
    # TODO: two cases about the same thing measure nothing.
    #       Extend the set to five, one per complaint.
]
