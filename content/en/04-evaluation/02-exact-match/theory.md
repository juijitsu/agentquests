# Theory · A false alarm

On the previous level there was no measurement at all, and that gave **false
confidence**: one lucky example was declared an improvement.

Here the measurement exists. The set is run in full, both versions, everything by
the book. And it gives a **false alarm**.

## What happens

The new version answers all six cases correctly. It is strictly better than the
old one, which did not know the answer to one case.

But three answers are phrased differently:

```
expected: 2.90        got: two dollars ninety cents
expected: 18:00       got: six in the evening
expected: 24 t        got: twenty-four tons
```

Character-by-character comparison declares all three errors. The score: old five
of six, new three of six. The conclusion: it got worse, roll the fix back.

**The measurement made you throw away an improvement.** That is worse than having
no measurement: without one, the fix would at least have been kept.

## Correctness is a property of the answer, not of the string

A phrasing is a way of writing something down. "Twenty-four tons" and "24 t" are
the same fact written differently, and both are correct.

The expected answer in the set is also merely **one of the possible writings**.
Whoever built the set wrote "18:00" because it is shorter; they could have
written "until 18 hours" or "six in the evening", and the set would not have
changed in substance.

Demanding a character-for-character match with one arbitrarily chosen writing
means measuring not correctness but **resemblance to the set author's
handwriting**.

## Why normalization does not save you

The first thought is to bring the strings to a common form. Strip the spaces,
lowercase everything, drop the punctuation.

For typos that works. For "two dollars ninety cents" against "2.90" it does not:
this is not the same text spelled differently but different texts about one fact.
No amount of string cleaning brings them closer, because they share not a single
character.

The rule: **if the difference between answers requires understanding, so does the
comparison.** String operations understand only strings.

## Who does the checking

The model does: `same_answer(expected, got)`. It answers the question "is this
the same answer", not "is this the same string".

That has a price, and it is worth knowing in advance. A judge can be wrong —
calling identical answers different or different answers identical. A judge
grading its own work is wrong systematically. That is a level of its own in this
track, and we will get to it.

For now it is enough to understand that the choice between string comparison and
semantic comparison is not a matter of convenience. String comparison **measures
the wrong thing**, and no amount of care in applying it fixes that.
