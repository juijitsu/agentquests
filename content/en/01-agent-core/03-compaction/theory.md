# Theory · You will have to shorten it

In Foundations you fixed an agent that cut the history for no reason: nothing
stopped it from sending the whole thing, and the right fix was to stop cutting.

That will not work here. The model's window is finite and the task is longer than
the window. **Shortening is unavoidable — the only choice is what to keep.**

## Why the tail is a bad answer

The first idea that comes to mind: keep the last N messages. Recent beats old,
sounds reasonable.

It is reasonable right up to the moment you discover that **the terms of the task
sit in the very first message**. The rate, the load weight, the customer's
requirements, the constraints — all named once, at the start, and needed at the
end.

The tail throws out exactly that.

## What is really happening

Compaction is not deletion of the old but **selection of what will be needed
next**. What you select is facts, not messages.

Inside the history there are things of three kinds:

**The terms of the task.** Needed always, down to the last step. Never discarded.

**Intermediate results.** Needed while something rests on them. Usually collapsed
into one line: "four hops covered, 20 hours total".

**Housekeeping chatter.** Acknowledgements, step reports, repetitions. Discarded
whole, with no loss.

## The simplest compaction that works

Nothing clever is required. Keep the terms of the task as a separate line and put
it at the front of the window alongside the recent tail:

```python
window = [terms] + history[-(N - 1):]
```

That is surprisingly enough for a long time. Fancier schemes — having the model
summarise the old part, vector search over the history — come later and cost
more.
