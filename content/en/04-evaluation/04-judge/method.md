# Method · A rule, an expected answer, a received one

**Step 1. Separate the judge from the author.** In code that is literally a
different call:

```python
model.judge_blind(RUBRIC, c["expected"], c["got"])
```

**Step 2. Hand the judge the rule.** The rubric comes first for a reason: it sets
what "correct" even means, and it has to exist before anyone looked at the
answers.

**Step 3. Do not pass anything extra.** No version, no author, no record of what
counted as correct last time. Everything the judge knows beyond the expected and
received answer works towards bias.

**Step 4. Judge everything the same way.** All cases by one judge and one rubric.
Mixing grades from different judges into one score is the same as measuring half
the set with a ruler and half by eye.

---

An honesty check: **take a dozen cases and judge them yourself without looking at
the judge's verdicts, then compare.** A disagreement on more than a couple out of
ten means you are measuring the judge, not the system.
