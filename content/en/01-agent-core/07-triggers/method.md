# Method · Drain it, do not walk it

The difference between the two loops is **where the question about the queue
stands**.

**Step 1. Move the question inside the loop.** It has to be asked before every
event, not once before all of them:

```python
while step < MAX_STEPS:
    pending = run_tool("pending", {})
```

**Step 2. Exit on the queue's answer, not on the end of a list.** `EMPTY` is the
condition for closing the shift:

```python
    if pending == EMPTY:
        break
```

**Step 3. Take one event, not all of them.** The rest are not going anywhere, and
by the next round their composition may have changed:

```python
    event = pending.split(" | ")[0]
```

**Step 4. Cap the loop.** The exit condition now depends on the outside world,
and the outside world can be wrong. `while step < MAX_STEPS` is there for exactly
that: the limiter from level 02 has not gone anywhere, it simply moved.

---

An honesty check: **count how many times your code asks `pending`.** Once — you
are walking a photograph. As many times as there are events — you are draining
the queue.
