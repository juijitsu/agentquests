# Theory · Where meaning is powerless

The first level of the track began with keyword search being systematically
wrong, and we moved to meaning. For six levels running, meaning rescued us.

This level is about where it does not work at all.

## A number has no meaning

The question: what weight is stated on waybill 4471.

There are three waybills in the corpus: 4471, 4478 and 4502. To semantic search
they are **indistinguishable**. The same concepts — waybill, cargo, weight. The
same document form. The same closeness to the question, all three at one.

The cause is not that the model is poor. The cause is the nature of a number: **an
identifier carries identity, not meaning.** "4471" means nothing — it points.
There is no semantic difference between 4471 and 4478, exactly as there is none
between Smith and Jones: the difference is in who it is, not in what it is.

Meaning answers "about what". A number answers "about which one".

## Exact search misses here too

You would think we could bring keyword search back and be done.

The waybill writes the number with a colon after it: "Waybill 4471:". The email
writes it as a bare word: "for waybill 4471 confirm the pickup time". Search the
whole question by words and the email matches on both "waybill" and "4471", while
the waybill itself matches on "waybill" alone.

So keyword search over the whole question puts the email above the waybill.
**Punctuation sinks exact search exactly where it should have won.** In other
languages the same thing happens through case endings; the mechanism is the
same — the token in the document is not spelled the way the question spells it.

## Every signal does its own job

Hence the right answer: do not choose between the methods, give each one its job.

**Exact matching narrows.** It answers "about which one" and selects every
document where that precise number occurs: the waybill, the email, the payment
note. Three documents instead of five, and all about the load you want.

**Meaning chooses.** Among the three it answers "what was asked about" — the
weight. The email is about pickup time, the payment note about money, the waybill
about the cargo. The waybill wins.

The order is exactly that, and it is not arbitrary: **narrow with what gives an
exact answer, choose with what understands the question.** The reverse does not
work: choose by meaning first and you have already lost, because to meaning three
waybills are alike.

## What counts as an identifier

A waybill number, a part number, a VIN, a tax ID, a filename, an order id, a
flight number. The common mark: **the value exists to distinguish, not to
describe.**

Telling an identifier from an ordinary word is the model's work, not a regular
expression's. "24" in a question about weight is a quantity, "4471" is an
identifier, though both strings are made of digits.

Real systems call this combination hybrid search. Usually the scores of lexical
and vector search are added together, but the idea is the one here: the two
methods have different strengths, and neither replaces the other.
