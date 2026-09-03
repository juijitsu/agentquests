# Method · Return the error into the loop

Four steps. The same procedure works for any tool.

**Step 1. Decide who the refusal is addressed to.** Ask one question: can the
model fix this by changing the arguments? Yes — the refusal is for the model. No
— for the human.

**Step 2. Catch the exception at the call site.** Not inside the tool and not
outside the loop, but exactly where you call it:

```python
try:
    result = run_tool(call.name, call.arguments)
except ValueError as exc:
    result = str(exc)
```

The error stopped being an exception and became an ordinary result.

**Step 3. Put it into the history under the same role.** Role `tool`, the same as
a successful result. To the model this is just another tool answer — it does not
distinguish successful from failed, it reads text.

**Step 4. Continue the loop.** Interrupt nothing. The next iteration is the
correction attempt.

---

A check on yourself: count how many different values the agent tried. If it is
one, there was no self-correction, whatever the agent answered in the end.
