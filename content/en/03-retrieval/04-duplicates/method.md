# Method · Collect with a repetition check

**Step 1. Rank by similarity as before.** Nothing new: the order of candidates is
still set by closeness to the question.

**Step 2. Take them one at a time and check for repetition.**

```python
if any(model.same_fact(chunk["text"], taken) for taken in picked):
    continue
```

You compare against **every one already taken**, not only the previous one: the
third chunk may repeat the first while skipping the second.

**Step 3. Stop on the selection size, not on the end of the list.**

```python
if len(picked) == TOP_K:
    break
```

**Step 4. Do not replace the check with a string comparison.**
`a["text"] == b["text"]` catches only literal copies. In a living archive a fact
repeats as a retelling, not as a copy-paste.

---

An honesty check: **count how many distinct facts are in your selection.** If
there are fewer than there are slots, you are paying slots for repetitions.
