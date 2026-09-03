# Method · One round, four conditions

The whole dispatcher is a single loop. The difference between a working one and a
broken one is four lines inside it.

**A round starts with a question to the world, not with a memory of it.**

```python
pending = run_tool("pending", {})
if pending == EMPTY:
    break
```

Exiting on the queue's answer is the condition for closing the shift. A snapshot
taken at the wake-up describes the past by the third round.

**The loop is still capped from above.**

```python
while step < MAX_STEPS:
```

The exit condition moved outside, and the outside world can be wrong. The limiter
from level 02 insures against exactly that.

**The human is bothered by a mark, not by habit.**

```python
if model.judge(action) and action not in APPROVED:
    run_tool("ask", {"name": action})
    APPROVED.append(action)
```

Two conditions in one line, and both are required. The first cuts off routine,
the second cuts off a repeat after a crash. Remove either and the human is
disturbed for nothing.

**Execution goes last.**

```python
run_tool("handle", {"name": action})
```

Up to that line the decision can still be undone. After it, no.

---

One honesty check for all four: **imagine the process dying on each line of the
loop in turn.** For every death, say what the agent will see on the next start.
If even once the answer is "it will ask the human a second time" or "it will
handle an action twice", the state is written in the wrong place.
