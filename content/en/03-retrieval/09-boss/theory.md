# Theory · The whole search engine

Eight levels took one failure at a time. Here there are five at once, and one
props up the next.

## What is being asked

What does waybill 4471 come to now **and** will the load pass over the Talmadge
bridge.

The first half: the answer exists, and it is hidden behind three obstacles at
once. The second half: there is no answer at all — no such bridge exists in the
documents.

| What is needed | Where the skill came from | What breaks without it |
|---|---|---|
| Split the question | level 05 | one query for two topics — both halves go unanswered |
| Narrow by the number | level 07 | waybill 4478 climbs into the selection |
| Discount by time | level 08 | the tariff from two years ago wins |
| Drop repeats | level 04 | three copies of the rate crowd out the surcharge |
| Know about the threshold | level 06 | a confident answer is given about the Talmadge bridge |

## Why they line up in exactly this order

The order on this level is not arbitrary, and it is worth understanding.

**Splitting comes first**, because everything after it is done for each half
separately. One has an identifier, the other does not; one has an answer, the
other does not. Handling them together means averaging the incomparable.

**Exact narrowing comes before ranking**, because it answers "which one" while
ranking answers "which is better". Picking the best of a wrong set is pointless:
waybill 4478 is fresher than the one you want and beats it on any sensible score.

**Discounting by time is part of the ranking**, not a step after it: it is a
multiplier on similarity, not a separate filter.

**The threshold is checked against the best one**, that is after ranking and
before building the selection. Building a selection out of documents none of
which fit is wasted work.

**Dropping repeats is last**, because a repeat is defined relative to what is
already taken, and taking only begins now.

## An answer that is half a refusal

The result comes out in an unfamiliar shape: a number for one half and "there is
nothing in the documents" for the other.

That is the right answer, not half an answer. The dispatcher learns the full cost
and learns that there is no data about the Talmadge bridge — so it has to be
looked up elsewhere or a document has to be created.

A bad search engine gives two confident figures on this question, and both are
wrong: last year's rate and another bridge's limit. **The difference between good
and bad here is not how much it found but whether it knows what it did not
find.**
