# Method · Trace one fact all the way through

When the agent answers wrongly and nothing crashes, you check memory, not logic.
A three-step procedure.

**Step 1. Name the fact.** What exactly did the agent need to know in order to
answer correctly? On this level it is the weight of the load. One concrete fact,
not "context in general".

**Step 2. Find where the fact enters the history.** Usually that is the
customer's original message. Make sure it made it into the list at all.

**Step 3. Follow it to the last model call.** This is where it breaks. Between
entering the list and the final call, three things can lose a fact:

- the list was rebuilt from scratch inside the loop;
- the model was handed a slice instead of the whole list;
- old messages were collapsed or dropped.

Printing beats reasoning. Add one line before the model call:

```python
print(f"[{step}] messages going to the model: {len(messages)}")
```

If the number does not grow, history is being lost. If it grows and the fact is
still missing, look at what you actually pass to `model.call`, not at what you
accumulated.
