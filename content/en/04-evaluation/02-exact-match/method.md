# Method · Check the answer, not the writing

**Step 1. Leave the run as it was.** The whole set, both versions — nothing
changes from the previous level.

**Step 2. Replace the comparison with a check.**

```python
model.same_answer(c["expected"], run_tool(...))
```

Instead of `==`. The argument order matters for readability: expected first,
then what was received.

**Step 3. Check both versions the same way.** The temptation to check only the
new version by meaning — "we know the old one" — ruins the comparison: the two
versions end up measured with different rulers.

**Step 4. Do not fix it with strings.** Lowercasing, stripping spaces and
punctuation help against typos and are powerless against a rephrasing.

---

An honesty check: **rewrite one expected answer in the set in different words
without changing its meaning.** If the score changes, you are measuring the set
author's handwriting rather than the system's work.
