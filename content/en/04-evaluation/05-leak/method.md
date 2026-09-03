# Method · Separate the familiar from the unseen

**Step 1. Run the whole set.** The overall score is needed: it shows how much the
system leans on memory.

**Step 2. Ask of every case whether it sits in the prompt.**

```python
clean = [c for c in CASES if not run_tool("in_prompt", {"case": c["id"]})]
```

Of **every** one, not of the suspicious ones: the suspicious ones will turn out
to be the wrong ones.

**Step 3. Compute the score separately over the unseen cases.**

```python
clean_passed = [c for c in clean if c in passed]
```

**Step 4. Show both numbers.** Do not replace one with the other: the gap between
them is the useful quantity.

---

An honesty check: **take the agent's prompt and search it for the texts of cases
from the set.** If you find even one, the score you showed yesterday was
inflated, and it has to be recounted.
