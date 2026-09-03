# Theory · Ninety percent of what

For two levels running we fixed the measurement: first we added a set, then we
learned to check answers by meaning. Now the measurement works and produces a
number.

Ninety percent. Eighteen cases out of twenty. A good result — ship it.

## What that number is made of

The set holds three kinds of case.

**Rates** — six cases, six correct. A mistake here costs money and is fixed by
reissuing an invoice.

**Schedule** — six cases, six correct. A mistake shifts a pickup.

**Overweight** — eight cases, **four correct**. A mistake puts a loaded tractor
on a bridge that will not hold it.

Half the overweight answers are wrong. The overall percentage says not one word
about that, because twelve flawless cases from two easy kinds pull the average
up.

## An average over the incomparable

An overall percentage is an average over things that cannot be averaged. A rate
mistake and an overweight mistake differ not in degree but in **kind**: the first
is fixed by an invoice, the second by a tow truck.

Hence an unpleasant property: **the overall percentage rises with every easy case
in the set.** Add a dozen simple schedule questions and the metric grows, though
the system did not change by a line. The number can be raised without touching
the system, and that is a sure sign it measures the wrong thing.

## The breakdown

The cure is to compute the share **within each kind**:

```
rates        100%
schedule     100%
overweight    50%   ← the weak spot
```

Not one new run — the same twenty cases, the same check. Only the way of looking
changed, and the failure hidden in the average became visible.

## The overall percentage is still needed

Do not conclude that the average is useless and should be thrown out. It answers
a legitimate question: how much of the work the system does correctly overall. It
is convenient for tracking movement release to release.

What is bad is not that it exists but that it is **alone**. One number cannot
answer both "how much in total" and "where exactly it is bad", and decisions are
made on the second.

The rule is simple: **the overall percentage is for the trend, the breakdown is
for decisions.**

## How to choose the kinds

Split by **what makes the cost of a mistake different**, not by what is
convenient to slice the data on. Kinds by question length or by arrival date tell
you nothing; kinds by the consequence of a miss tell you at once.
