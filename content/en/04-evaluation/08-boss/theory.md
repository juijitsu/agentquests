# Theory · Ship it or not

Seven levels took one failure of measurement at a time. Here there are five at
once, and the outcome drives a real decision: ship the new version or not.

## What the quick report shows

One run, self-grading, one number: **nine of nine**. A hundred percent. Ship it.

Now honestly.

| What is needed | Where the skill came from | What the leniency hides |
|---|---|---|
| An independent judge | level 04 | the author scores everything for itself |
| Exclude the leak | level 05 | two cases sit in the prompt |
| Several runs | level 06 | broken is indistinguishable from unstable |
| A breakdown by kind | level 03 | easy kinds pull the average up |
| Stability in the score | level 06 | correct-every-other-time counts as correct |

The result after all five:

```
rates        100%
schedule      67%
overweight     0%      ← the weak spot
unstable 2: s3, w3
```

Zero percent on overweight. Of the two remaining cases one never works and the
other works every other time. Every mistake there puts a loaded tractor on a
bridge that will not hold it.

## The leniencies all lean one way

Here is the main observation of the level, and it is not obvious.

Each of the five leniencies looks like a trifle on its own. So the author did the
judging. So it was run once. So it was not split by kind. Each adds a few
percent.

But **they all shift the result upwards**. Not one shifts it down.

That is no coincidence: leniencies are taken where checking is more expensive,
and checking is more expensive where the system works worse. An author is softer
on itself. One run is more convenient than five. A single number is more pleasant
than a breakdown showing a failure.

That is how a hundred percent turns not into ninety but into zero on the kind
that matters most.

## The order in the report

It is not arbitrary.

**The leak is excluded first**, before everything else: counting runs and kinds
over cases whose answers sit in the prompt is wasted work.

**Runs come before stability**, because stability is determined from several
runs, not the other way round.

**The judge is called per run**, not per case: a case does not have one answer,
it has RUNS of them.

**The breakdown is last**, because it groups what has already been counted.

## The rule makes the decision, not a person

Note the last line of the report: the decision follows from the numbers
mechanically — if any kind is below the bar or there is any unstable case, it
cannot ship.

That matters for exactly the reason a rubric is written before the answers are
read. **A rule formulated after seeing the numbers bends towards the desired
decision** — and always towards "ship it, it is almost fine".
