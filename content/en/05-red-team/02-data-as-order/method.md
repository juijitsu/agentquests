# Method · A control and a difference

**Step 1. Take a control.**

```python
base = model.handle(None)
```

This is what the agent does with no note. One call, and after it any sentence
in the report stops being an impression.

**Step 2. Run every note.**

```python
model.handle(note["id"])
```

Every one, the boring ones included. There is nothing to pre-select: selecting
by the text is the very mistake being checked here.

**Step 3. Compare whole actions.**

```python
model.handle(note["id"]) != base
```

Not the length of the list, not the first step, not the presence of a
suspicious call. Whole, arguments included: a swapped phone number matches on
every other sign.

**Step 4. Do not fix anything.** The list of notes that worked is the result.
What to do about them is the defence's decision, and it is made at a different
level.

---

An honesty check: **take a note you selected and name the action that appeared
or changed because of it.** If there is nothing to name, it is not a finding
but an impression of the text.
