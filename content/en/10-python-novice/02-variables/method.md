# Method · How to solve it, step by step

## Step 1. Run the starter as it is

It works and it is wrong. The verdict:

```
✓ returned text: yes
✗ loads matched: 0 of 6
✗ first difference: on the miles "1450"
    expected: 1450 + 60 = 1510
    got:      1450 + 60 = 145060
                           ^
```

The arrow stands where the answers parted. Everything to the left of it
matched; after it come extra digits: instead of a sum, the digits of sixty got
stuck on.

## Step 2. Find the place where text has to become a number

The starter says:

```python
    total = miles + "60"
```

`miles` is text, `"60"` is text too, so the plus glues. What is needed is
numbers on both sides.

## Step 3. Three lines instead of one

```python
    loaded = int(miles)
    total = loaded + 60
    return miles + " + 60 = " + str(total)
```

- `int(miles)` — a number came out of the text and went into `loaded`;
- `loaded + 60` — both are numbers, so the plus adds;
- `str(total)` — the number went back into text so it can be glued on;
- `miles` on the left was left alone: that is how it should stay.

Notice: the `60` in the calculation has **no quotes** — it is a number. The
`" + 60 = "` in the answer is **in quotes** — it is text that is merely shown.
The same sixty in two different roles.

## Step 4. Run it

```
✓ returned text: yes
✓ loads matched: 6 of 6
✓ first difference: all matched
```

## Step 5. If it does not match

**Extra digits on the right** — the addition is still gluing. So `int()` is
either not applied, or applied to the wrong thing.

**`returned text: no`** — a number came back. The whole answer has to be text,
so the sum needs `str()` around it.

**`TypeError`** — the two sides of the plus are of different kinds. Look at
what is on the left and on the right: both text, or both numbers.

**`ValueError`** — something other than digits got into `int()`.

## Step 6. Check yourself

Without looking: why does the number 1450 appear twice in
`"1450 + 60 = 1510"` and yet is written differently? If the answer comes
straight away, the level has landed.
