# Theory · What to drop when everything is needed

The first level of the track taught selection by topic: not "what do we have" but
"what bears on the question". The technique works while what you selected fits.

Here it does not fit. All five blocks are relevant, none is extra, and the budget
covers three. For the first time in the track you have to rank rather than
filter.

## Age is not value

The first thing people do when something does not fit: throw out the old. The
logic is clear — fresher is usually more current.

The Carroll bridge limit was set in twenty nineteen. It is the oldest thing in
the pile, and it is the only thing that answers the question. Today's weather is
seven years fresher and settles nothing.

**Freshness matters where data gets updated** — as on the previous level, where
rates were superseded by new ones. A bridge limit does not get updated: the
bridge held eighteen tons then and holds eighteen tons now.

Cutting by age means applying the previous level's rule where it does not work.

## Value is not the answer either

Fine — sort by value and take the most valuable.

The most valuable block here is the bridge's repair history. It genuinely bears
on the matter, it holds a lot that is important, and it costs seventy out of
eighty. Take it and you spend almost the whole budget and can take neither the
limit nor the load weight — the two cheap blocks that actually give the answer.

**An expensive, useful block crowds out two cheap, decisive ones.** That is not a
rare case but the norm: long documents almost always look more substantial than
short lines.

## Return per unit of cost

The right quantity is neither value nor price on its own but their ratio:

```
worth(block) / block.cost
```

The limit: nine for twenty — zero point four five. The repair history: ten for
seventy — zero point one four. The history looks more valuable, yet for the same
money the limit gives three times as much.

After that comes a greedy pass: take in descending order of return while it
fits. That is the same technique used to pack a knapsack and to allocate an
advertising budget; in context engineering it works exactly the same way.

> **A budget is spent not on the most important thing but on what returns the
> most per unit spent.**

## Who computes the value

Not your code. A block's price is measurable — it is its size, and you can see
it. Value depends on the question: a repair history is useless for a question
about weight and irreplaceable when investigating an accident.

That is why `cost` is a field of the block and `worth` is a method of the model.
Your job is to divide one by the other and sort.
