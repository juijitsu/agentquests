# Method · Run several times, split into three

**Step 1. Iterate runs inside a case.**

```python
results = [
    run_tool("check", {"case": case["id"], "run": n}) == "correct"
    for n in range(RUNS)
]
```

The outer loop walks cases, the inner one walks runs, not the other way round:
what you need is the history of every case, not a slice of every run.

**Step 2. Split into three states.**

```python
if all(results):
    stable_ok.append(...)
elif any(results):
    flaky.append(...)
```

The order of the checks matters: `all` is stricter, so it comes first. Start with
`any` and you will file the always-correct ones as unstable too.

**Step 3. Do not average.** The share of successful runs is a pretty number you
cannot make a decision from. A list of unstable cases is an ugly number you can.

**Step 4. Do not dump the unstable ones into the failures.** These are different
states and different work: broken things get fixed from a reproduction, unstable
ones first have to be caught.

---

An honesty check: **run the set twice and compare the reports.** If they differ,
your measurement is itself unstable, and any comparison of versions through it is
meaningless.
