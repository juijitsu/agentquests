# Method · Three claimants on the window

On level 03 the window had two occupants: the terms and the tail. Now there are
three.

**Step 1. Count the slots.** The window is fixed. The terms take one, the notepad
takes as many as it holds entries, the tail gets the remainder:

```python
tail = WINDOW - 1 - len(notes)
```

This is not a formality: get the arithmetic wrong and the window overflows by
exactly one message, and the model refuses to work.

**Step 2. Assemble the window by priority.** The order reflects importance — what
is always needed goes first:

```python
return [terms] + notes + history[-tail:]
```

**Step 3. Watch the notepad's size.** It grows, the tail shrinks. If entries pile
up, the agent is writing down too much — either the `write_note` description is
too vague, or the task genuinely needs smarter selection.

---

A sign the notepad is not being delivered: the agent wrote a fact down, it is
visible in the log, and the fact is absent from the final answer. Gathered but
undelivered is the most galling loss of all, because the work is already done.
