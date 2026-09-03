# Method · Separate planning from execution

Three steps. The order matters: planning comes entirely before execution.

**Step 1. Get the plan before the first tool call.** Not along the way, but as a
separate action while nothing has happened yet:

```python
plan = model.make_plan(question)
```

**Step 2. Put the plan into the history as its own message.** Do not mix it into
the question text — there it gets lost among everything else. A separate role
makes the plan visible both in the log and to the model:

```python
messages.append({"role": "plan", "content": plan})
```

**Step 3. Execute while checking against the list.** The loop does not change —
what changes is what the model now sees in the history. It walks the items
itself, because it knows what the task consists of.

---

A check on yourself: print the plan before the loop. If you cannot tell from it
in advance how many tool calls there will be, the plan is too vague.
