"""Level 07 · reference. One case per complaint."""

# The week's complaints log. Each one is a separate kind of request:
#   1. the queue at the Laredo crossing
#   2. the status of shipment TX-4471
#   3. the price of hauling a 12-ton load
#   4. delivery time
#   5. a crossing with a typo in the name — "Loredo"

CASES = [
    ("What is the queue at Laredo?", "queue of 40 trucks"),
    ("Where is shipment TX-4471?", "arriving in 4 days"),
    ("How much does it cost to haul a 12-ton load?", "1080"),
    ("What is the delivery time?", "11 days"),
    ("What is it like at the Loredo crossing?", "does not exist"),
]
