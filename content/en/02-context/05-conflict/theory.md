# Theory · When you must not choose

The previous level also began with two different values of one field, and there
it settled easily: one was fresh, the other stale. Time put them in order.

Here both documents are today's.

## A dispute between equals

Bill of lading 4471 says twenty-four tons. The Laredo weigh station says
twenty-six point four. Both documents are real, both are dated today, both were
issued by people entitled to issue them.

The gap is explainable: a bill of lading is written from the declared weight, a
weigh ticket from the actual one. Two-odd tons of difference is ordinary — the
load got damp, something was topped up on site, a conversion was off.

**Neither of the two documents is wrong.** They simply answer slightly different
questions, and one question is being put to both.

## Why this is not a trifle

The bridge holds twenty-six tons.

By the bill of lading the load passes. By the weigh ticket it does not. A
discrepancy that is so easy not to report **decides the outcome**: in one case we
drive, in the other we look for a detour.

An agent that silently took whichever value came first did not "get it slightly
wrong". It produced a confident answer to a question that **has no answer in the
available data**.

## What it looks like in code

The mistake does not look like a mistake. It looks like tidy assembly:

```python
merged = {f["field"]: f["value"] for f in facts}
```

Three facts in, two keys out. One simply vanished — a dict holds one value per
key, and the second reading overwrote the first. No exception, no warning.

**Collapsing is a decision taken, disguised as formatting.** You chose which
document to believe, and did not even notice you were choosing.

## What to do instead

Accumulate rather than overwrite:

```python
merged.setdefault(fact["field"], []).append((fact["source"], fact["value"]))
```

One field, as many readings as you like, each with its own source. After that the
decision is made by whoever has the right to make it: the model reports the
disagreement, a person clarifies.

> **The context assembler's job is to convey the dispute, not to settle it.**

And note why the source matters here: a message saying "the weight is either 24
or 26.4" is useless. What is useful is "bill of lading 24, weigh ticket 26.4" —
from that you can see whom to call. That is exactly the skill from level 02, only
now it saves you not from somebody else's surcharge but from a trailer off a
bridge.
