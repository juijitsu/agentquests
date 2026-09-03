# Method · A role and a source on every piece

**Step 1. Do not glue.** Any `"\n".join(...)` over fetched documents erases their
origin. After the glue-up it cannot be restored — you have already handed the
model uniform text.

**Step 2. Mark every piece with a role.**

```python
{"role": "data", "source": d["source"], "text": d["text"]}
```

The role answers the question "how do I read this", and for anything fetched from
outside the answer is always the same: as data.

**Step 3. Keep the source.** It is needed twice: to report who tried to give
instructions, and so there is somebody to call. The same argument as on level 02.

**Step 4. Do not filter by words.** The temptation to cut out "ignore" is strong
and useless: the phrasing will be dodged, and you will break a legitimate note.
The border runs along the text's origin, not along its content.

---

An honesty check: **imagine the note says anything else at all.** If your defence
depends on particular words, it will be dodged by the first rephrasing. If it
depends on where the text came from, it cannot be dodged at all.
