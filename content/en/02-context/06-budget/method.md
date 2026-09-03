# Method · A greedy pass by return

**Step 1. Compute the return of every block.** Value is divided by cost, not
compared with it:

```ts
model.worth(block) / block.cost
```

**Step 2. Sort in descending order.** A copy, not the original array: `BLOCKS`
belongs to the scenario, and somebody else may need its order.

```ts
const ranked = [...BLOCKS].sort((a, b) => model.worth(b) / b.cost - model.worth(a) / a.cost);
```

**Step 3. Take while it fits.** The check goes before adding, not after:

```ts
if (spent + block.cost <= BUDGET) { ... }
```

**Step 4. Do not stop at the first one that does not fit.** An expensive block in
the middle of the list must not end the pass: cheap ones that still fit may come
after it. The difference between `continue` and `break` here is worth one block.

---

An honesty check: **double the cost of the most valuable block and run the
selection again.** If the brief did not change, you are sorting by value rather
than by return, and you have merely been lucky so far.
