# Method · Reacting to impossibility

Four steps.

**Step 1. Separate ordinary results from invalidating ones.** Not every tool
answer is equal. "Cleared" advances the plan; "no through road" zeroes it. The
distinguishing mark has to be explicit and checkable:

```python
if "no through road" in result:
```

**Step 2. Ask for a new plan, saying what broke.** Not what to do — only what
does not work:

```python
new_plan = model.make_plan(question, blocked=call.arguments["leg"])
```

**Step 3. Put the new plan into the history.** It stands next to the old one, not
in place of it: the model reads the latest, and you see both when reviewing.

**Step 4. Continue the loop unchanged.** Nothing needs restarting — the next
iteration picks up the current plan and follows it.

---

An honesty check: delete from your code everything that names specific cities,
except what came out of tool answers. If the solution stopped working, you wrote
a branch, not replanning.
