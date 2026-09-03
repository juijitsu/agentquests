# Method · Build a set that discriminates

Four steps.

**Step 1. Collect real requests.** Do not invent questions. Take the complaints
log, the chat history, the list of what was asked. Five different situations are
worth more than fifty variations of one.

**Step 2. One case per situation.** One complaint, one case. Two cases about the
same thing measure the same thing and cost twice as much.

**Step 3. The expectation is a substring of the fact, not of the text.** Not the
whole answer but the one thing without which the answer is wrong:

```python
("How much does it cost to haul a 12-ton load?", "1080")
```

The number 1080 has to be there. How it is wrapped in words is not your concern.

**Step 4. Check that the set discriminates.** Run it against a broken agent and a
healthy one. The same result on both means you are measuring the wrong thing.

---

The mark of a good set is simple: **looking at the score, you can name what
exactly is broken.** If the number dropped and you cannot tell why, the cases are
too coarse.
