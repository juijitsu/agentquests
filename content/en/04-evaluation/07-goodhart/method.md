# Method · A metric and its cost

**Step 1. Leave the metric as it is.** It measures what it measured and is still
useful.

**Step 2. Name the metric's cost.** Ask yourself: what can be spoiled by pushing
it up? For specificity the answer is obvious — start inventing.

**Step 3. Count the cost in the same run.**

```python
model.is_specific(answer) and not model.is_correct(expected, answer)
```

Both conditions are required. A merely wrong answer is not the same as a
confidently wrong one: the first gets in the way, the second does harm.

**Step 4. Show both quantities side by side.** Do not add them into one "overall
quality": the whole point is that they diverge, and a sum hides the divergence.

---

An honesty check: **work out how to fool your own metric without improving the
system.** If you managed it in a minute, the system will manage it too. Add a
paired metric that gets worse under that trick.
