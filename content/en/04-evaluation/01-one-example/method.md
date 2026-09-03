# Method · A set, both versions, a score

**Step 1. Take the whole set.** Not the first case, not your favourite, not the
one you were fixing. All of them.

```python
for c in CASES:
```

**Step 2. Run both versions over the same set.**

```python
for version in ("old", "new"):
```

The loop order does not matter; what matters is that the outer loop walks
versions, the inner one walks cases, and the inner one is identical for both.

**Step 3. Count the matches.**

```python
run_tool("ask", {"version": version, "case": c["id"]}) == c["expected"]
```

**Step 4. Compare numbers, not impressions.** "It seems better" is not the result
of a measurement. The result of a measurement is two numbers and the difference
between them.

---

An honesty check: **remove the case the fix was made for and count again.** If
the fix then looks like a failure, it is one, and you have just learned something
you did not know.
