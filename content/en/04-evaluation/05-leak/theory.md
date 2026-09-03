# Theory · An answer the agent already knows

By this level the measurement is in order: there is a set, there is semantic
checking, the judge is independent, the rubric is written down. The result is
five of eight.

Four of those five the agent did not solve. It remembered them.

## How examples get into the set

There is no malice here, and that is the main danger.

The agent's prompt contains examples — everybody does this: a couple of
illustrative questions with correct answers noticeably improves behaviour. The
examples are taken from real life, that is from the same real cases the test set
is later assembled from.

A month goes by. The set grows, the prompt is edited, somebody adds a good
example, somebody adds a case to the set. Nobody cross-checks the two, because
they are different files and often different people.

**A leak is not made — it happens.**

## What is being measured

On a case from the prompt the agent does not reason. The answer is in front of
it, and the task reduces to copying it out. That it does flawlessly.

So the score on such cases is always near perfect — and **says nothing about the
system's work**. It speaks about its memory, and memory does not interest us: in
production there will not be a single question whose answer sits in the prompt.

Counted honestly:

```
whole set        5 of 8   (63%)
unseen cases     1 of 4   (25%)
```

The difference between sixty-three and twenty-five is not measurement error. It
is the difference between "the system works" and "the system does not work".

## What to do

**Separate them.** Cases that ended up in the prompt are excluded from the main
score. Not thrown out of the set — they are useful as a regression check — but
counted separately.

Both numbers are worth showing side by side, and the gap between them is useful
in itself: it shows how much the system leans on memory rather than skill.

**Check it automatically.** Manually verifying "is this case in the prompt" works
exactly until the third person joins the team. The check belongs in the same
script as the run, and it should fail on its own.

## A related trouble

The same mechanism breaks anything that learns: if a case was in the training
data, measuring on it is meaningless. The statement is the same for prompts, for
fine-tuning and for answer caches:

> **You can only measure on what the system has not seen.**
