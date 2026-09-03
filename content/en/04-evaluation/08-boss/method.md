# Method · Five steps in one order

**Step 1. Exclude the leak.**

```python
clean = [c for c in CASES if not run_tool("in_prompt", {"case": c["id"]})]
```

Every case is checked, not the suspicious ones. They are excluded from the score,
not from the set of kinds.

**Step 2. Run every remaining case several times, judging independently.**

```python
results = [
    model.judge_blind(RUBRIC, run_tool("answer", {"case": case["id"], "run": n}))
    for n in range(RUNS)
]
```

The judge is called per run: a case has as many answers as there are runs.

**Step 3. Split into stable and unstable.** `all` before `any`, or the
always-correct ones land among the unstable.

**Step 4. Compute the share within a kind.** The denominator is the size of the
kind after the leak is excluded.

**Step 5. Hand the decision to the rule.** The bar and the condition about
instability are written down in advance; your job is to count, not to decide.

---

An honesty check: **remove each of the five steps in turn and watch where the
number goes.** It goes up in all five cases — and that is the whole point.
