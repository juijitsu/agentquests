# Method · Count within the kind

**Step 1. Run the set as before.** Nothing changes: the same cases, the same
check.

**Step 2. Collect the kinds from the set itself.**

```python
for kind in {c["kind"] for c in CASES}:
```

Do not write the list of kinds by hand: add a new one and you will forget about
it, and the metric will not tell you.

**Step 3. Compute the share within a kind, not the kind's share of the total.**

```python
same = [c for c in CASES if c["kind"] == kind]
hit = [c for c in same if c in passed]
by_kind[kind] = round(100 * len(hit) / len(same))
```

The denominator is the size of the kind. That is the whole difference between
"half the overweight answers are wrong" and "overweight gives twenty percent of
all errors".

**Step 4. Keep the overall percentage.** It does no harm and is useful for the
trend. What matters is that it is not the only one.

---

An honesty check: **add ten easy cases to the set and count again.** If your
headline metric grew, it measures the composition of the set rather than the work
of the system.
