# Method · A meaningful stopping condition

Three steps.

**Step 1. State the goal so it can be checked.** Not "deliver the freight" but
"the answer contains Newark". The condition has to be something code can compute,
not something a person can appraise.

**Step 2. Check the goal where you used to exit.** Same place — the moment the
model stopped asking for tools. What changed is the meaning: it used to be an
exit, now it is a fork.

```python
if not response.tool_calls:
    if goal_reached(response.text):
        return response.text, step
    ...keep going...
```

**Step 3. Hand the model the new state of things.** It does not remember where
you are. Add a message with the current position to the history, or the next
iteration will repeat the previous one.

---

A sign the exit condition is wrong: the agent answers fast and confidently, and
the number of completed steps is lower than expected. Count the steps — they do
not lie.
