# Method · How to shape a refusal

Protection that fails with an exception protects the code and abandons the user.
A three-step procedure.

**Step 1. Decide what kind of event this is.** Running out of budget is neither a
programmer error nor a fault. It is a result: the agent honestly tried and could
not. So it should come back as a result, by the same path as success.

**Step 2. Collect diagnostic data as you go.** A message saying "it did not work"
is useless. A useful message answers three questions: how many steps were spent,
what the agent did last, why it made no progress.

Which means the information has to be accumulated inside the loop, not
reconstructed afterwards:

```python
last_tool = None
...
    last_tool = call.name
```

**Step 3. Return it in the same shape as a successful answer.** The calling code
should not have to tell success from refusal in two different ways — it already
knows how to read `(text, steps)`.

---

A check on yourself: read your refusal message through the eyes of a dispatcher
who knows nothing about agents. Is it clear to them what to do next?
