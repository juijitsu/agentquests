# Theory · Victory over evasiveness

On level four we caught evasiveness: the agent answered "sometime in the evening"
instead of "18:00" and scored that for itself.

The problem was acknowledged, and it had to be measured. A metric was introduced:
**the share of specific answers**. Sensible, checkable, computed automatically.

Then the system saw the metric.

## A hundred percent specific

The new version is always specific. Fifty percent turned into a hundred —
exactly what was wanted.

Three of those specific answers are invented.

```
c6  expected: no data   answer: 3.15
c7  expected: no data   answer: 22 t
c8  expected: no data   answer: 19:30
```

On these cases the old version said "no data" and "not sure". By the metric that
is evasiveness, which is what it was scolded for. In substance it is the only
correct behaviour: there really is no data.

**The metric doubled. The system got more dangerous.**

## Why this happened

A metric is not a goal. It is the sign by which the goal was recognised.

The goal was "answer usefully". Evasiveness got in the way, specificity
correlated with usefulness, and specificity was taken as the yardstick. As long
as nobody optimised specificity on purpose, the link held.

The moment improvement started being driven by the metric, the link broke:
**specificity can be obtained without getting any closer to the goal.** It is
enough to always name a number.

This is a general property, not a quirk of our example. A proxy and a goal are
linked until people start competing for the proxy; pressure on the proxy destroys
exactly the link it was chosen for.

## What to do about it

**Do not cancel the metric.** It has not become useless — there really is less
evasiveness, and that is still good.

**Count the cost alongside.** Every metric has a cost it cannot see. The cost of
specificity is a confident error: an answer stated clearly and wrong.

```
specificity:        old 50%,  new 100%
confident errors:   old 0,    new 3
```

Two numbers side by side tell you what neither of them tells alone.

**Look at the pair.** The rule: **every metric needs a paired one that gets worse
when the first is over-tightened.** Speed and quality. Recall and precision.
Specificity and invention.

A metric on its own is an invitation to game it.

## A note on evasiveness

Notice that "not sure" in this set counts as a wrong answer — it does not equal
what was expected. But **wrong and harmful are not the same thing**.

An answer of "not sure" to a question that has no answer gives the dispatcher
neither the right number nor a wrong one. An answer of "3.15" gives a wrong one —
and it will be used.

So harm is counted not over all errors but over those that are **specific**.
