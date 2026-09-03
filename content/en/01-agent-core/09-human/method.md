# Method · One border and two rules

**Step 1. Find the irreversibility mark.** It arrives with the action — no
guessing needed:

```python
if call.arguments["irreversible"]:
```

Everything else runs silently. Not because it does not matter, but because a
mistake in it can be corrected.

**Step 2. Ask before executing.** The approval call stands **before** `act`, not
after. After is a notification.

**Step 3. Obey the answer.** A refusal has to interrupt the action, not accompany
it:

```python
if not verdict.startswith("yes"):
    REFUSED.append(name)
    continue
```

**Step 4. Record the refusal where it will be seen.** A rejected action must not
resurface on the next round as unfinished — otherwise the agent asks about it
again and again, until it gets a "yes" from a tired person.

---

An honesty check: **count how many requests the person gets in a shift.** If it
is more than the number of irreversible actions, you are spending somebody else's
attention — and the request standing last will be the first to feel it.
