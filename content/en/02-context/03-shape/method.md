# Method · Parse it once

**Step 1. Find where the data still has a shape.** Here it is the sentence: it
holds the weight, the day and the number. The shape is not lost — it is merely
expressed in words.

**Step 2. Parse each one into a record.** One call per sentence:

```ts
const payload = SENTENCES.map(parse);
```

Note that this is `map`, not `join`. The difference between them is the whole
point of the level: `map` keeps the record boundaries, `join` erases them.

**Step 3. Keep every field.** The temptation is to pass only the weight — the
question is about the heaviest, after all. But the filter runs on the day, and
that is what you would throw away. **The field you filter by is needed no less
than the one you compare by.**

**Step 4. Do not do the model's arithmetic.** Selecting today's and finding the
maximum is something it can do — given something to do it with. Your work ends at
the shape.

---

An honesty check: **take one record and swap its fields around.** If the answer
did not change, the shape is real. If the data sits as text, order decides
everything, and that is the first sign you handed the model work you should have
done yourself.
