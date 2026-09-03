# Method · One assembly, five conditions

The whole assembler is one loop over a sorted list. The difference between a
working one and a broken one is four lines inside it.

**Sort by return, not by order and not by price.**

```python
ranked = sorted(blocks, key=lambda b: model.worth(b) / b["cost"], reverse=True)
```

**Skip, do not break.** An expensive block in the middle must not end the pass —
cheap ones that still fit come after it:

```python
if spent + block["cost"] > BUDGET:
    continue
```

**Put the block in whole, with a role and a source.**

```python
{"role": "data", "id": ..., "source": ..., "text": ..., "cost": ...}
```

The role says how to read it. The source says whom to call. The cost is there so
the budget can be checked rather than taken on trust.

**Collapse nothing and drop nothing.** Two weight readings travel as two blocks.
The planted paper travels as data. Deciding what to believe and what to do about
the attempt happens higher up.

---

One honesty check for all five: **walk the brief and for every block say why it
is here and why in this shape.** If for some block the answer is "left over from
the previous sort" or "where else would it go", you assembled not a brief but the
remains of a budget.
