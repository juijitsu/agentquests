# Method · Assemble the window

Three steps.

**Step 1. Single out what is always needed.** Walk through the task and ask of
every fact: will it be needed on the last step? The rate — yes. The report on the
second hop — no.

**Step 2. Build the window from the constant part plus the tail.** The constant
goes first, the recent follows:

```python
def window(history):
    return [terms] + history[-(WINDOW - 1):]
```

Note the `WINDOW - 1`: room for the constant part has to be left, or the window
overflows by exactly one message.

**Step 3. Test it on a long task.** A short one fits in the window whole and
proves nothing. Compaction bugs are visible only when the history genuinely does
not fit.

---

A sign compaction was done wrongly: the agent walks the whole task but at the end
cannot answer a question whose answer was at the start.
