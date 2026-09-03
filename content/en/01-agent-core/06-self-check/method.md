# Method · Review before handing over

Three steps.

**Step 1. Find the handover point.** It is the single place where a result leaves
the agent — usually the `return` after the loop. Everything that goes to the
customer passes through here.

**Step 2. Insert the review before the return.** Two items go to the check: what
came out and what was asked for.

```python
return model.review(response.text, question), step
```

Note: `question`, not a paraphrase. The terms are passed whole, because you do
not know in advance which requirement will turn out to be violated.

**Step 3. Hand over what the review returned.** Not the original answer, not both
at once. The reviewer saw the result and the terms — its version is the fuller
one.

---

A check that the review is real: **the comparison must not appear in your code.**
If it contains `if hours > deadline`, you wrote a validator for one requirement,
not an agent self-check. The customer's next requirement will demand another
line, and so on forever.
