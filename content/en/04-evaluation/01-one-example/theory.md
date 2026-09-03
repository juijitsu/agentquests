# Theory · The case the fix was made for

The agent was fixed. Did it get better?

The question looks simple, and it usually gets answered like this: take the case
the fix was made for, run it, see the right answer, close the task.

That is exactly what happens here. The old version did not know about the fuel
surcharge, the new one does. The fix works.

The new version also quotes a rate from two years ago and gets the waybill weight
wrong. Nobody asked about that.

## Why your favourite example says nothing

The case a fix was made for is **the worst possible way to test it**. It was not
chosen at random: it was chosen because it was broken, and the fix was sharpened
against it. It is obliged to pass. Its passing confirms that you did what you set
out to do — and says nothing about what else you did.

A change in a system where everything is connected is rarely local. Fix the
number parsing and the dates drift. Add a tool and the model starts calling it
instead of the right one. Sharpen a wording and the neighbouring case that leaned
on it breaks.

**A fix almost always mends one thing and breaks another.** The question is not
whether it mends but what that cost.

## What a measurement is

A measurement starts with a set: several cases with the correct answers known in
advance. Not one, not "let us glance at a couple of examples" — a fixed set, the
same one for every version.

After that it is simple: both versions go through the whole set, you count the
matches and compare the numbers.

```
old 5 of 6
new 4 of 6
```

Now you can see what was invisible: the fix mended one case at the cost of two.
**It got worse**, even though the thing it was made for works.

## One set for every version

The condition without which comparison is meaningless: both versions go through
**the same** set in full. Not "we will check the old one on the old cases and the
new one on the new ones" — that compares two different quantities and gives a
number meaning nothing.

This sounds obvious right up to the moment the set starts growing with the
system: a new case was added for a new capability, and the old version naturally
does not pass it. The comparison then has to be made on the common part.

## What this level does not yet solve

Comparison here goes by exact string match: an answer is correct if it is
character-for-character equal to the expected one. For this set that works, and
thank goodness — otherwise the track's first level would have to start with the
second.

What to do when the correct answer is phrased differently is the next level.
