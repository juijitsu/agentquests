# Theory · A selection built from one fact

For three levels running we fixed the search: it found the wrong subject, it
found the right subject with no answer, it found half a fact. Here it finds
correctly.

Every chunk in the selection is relevant. Every one holds the rate you want.
Every one would pass any check from the previous levels.

And the answer is still incomplete, because **all three chunks say the same
thing**.

## One fact lives in many documents

The base rate for Laredo — Newark sits in the price list. And in the email to the
customer where it was confirmed. And in the quarterly report. And in the archived
copy of the price list. And in the billing export.

Five documents, five different phrasings, one fact. That is not a mess in the
data but the normal state of any working archive: what matters gets repeated,
because what matters gets forwarded, copied and quoted.

To the search all five are equally similar to the question. A top-3 honestly
takes three of them.

## What gets crowded out

The question was: what does it come to **in total**. And in total is the base
rate plus the fuel surcharge: 2.90 plus 0.35.

The surcharge sits in one single document and stands sixth by similarity. Five
copies of the base rate pushed it out of the selection, and the agent answers:
2.90.

**The number is right. The answer is incomplete.** And the incompleteness is
invisible: the selection holds three relevant documents, all confirming the same
thing, and the picture looks even more convincing than usual.

## Similarity awards slots, but what you need is the increment

Hence the idea of the level.

Ranking by similarity answers the question "how well does this chunk fit the
query". It knows nothing about **what is already in the selection**. A fifth
retelling of the same rate fits the query exactly as well as the first — and adds
exactly zero.

The right criterion is different: **a slot in the selection is earned by what it
adds to what is already there.** The first chunk is taken for similarity, each
next one for saying something the selection does not yet hold.

Real systems call this selection diversity, and its best known form is maximal
marginal relevance. The name is grand, the idea is simple: at every step choose
between "similar" and "new", not only between "similar".

## Why not by comparing texts

The temptation: since these are copies, drop the matching lines.

Look at them again. "Price list: Laredo — Newark, 2.90 per mile" and "Email to
the customer: confirming 2.90 per mile on Laredo — Newark" share no identical
line, the word order differs, the prefixes differ. There is no text match, and the
fact is one.

Character equality catches only literal duplicates, and in a living archive those
are the minority. Whether the fact is the same is judged by the model.
