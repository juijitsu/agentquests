# Method · How to solve it, step by step

## Step 1. Run the starter as it is

It works and it is wrong. The verdict:

```
✓ returned text: yes
✗ labels matched: 1 of 10
✗ first difference: on the label '  dallas run 47 '
      expected: 'DAL47'
      got:      '  d7 '
                 ^
```

Both strings are shown in quotes on purpose. Spaces and newlines are invisible
on screen, but inside quotes the edges show: `'  d7 '` starts with two spaces
and ends with one. The caret stands where the answers parted: the first
character still matched (the quote), and after that they diverge.

## Step 2. Work out why exactly one label matched

Ten labels, one matched. That is a clue, not a coincidence.

The starter cuts `text` exactly as it arrived. So it will land on the right
answer only when the label is **already clean and already in capitals** —
there is nothing to clean in that case.

There is one such label in the set: `"OMAHA RUN 33"`. On all the others either
a space at the edge, or lower case, or both get in the way.

The conclusion: the cutting is right, the cleaning is not.

## Step 3. Find the idle lines

```python
def solve(text: str) -> str:
    text.strip()
    text.upper()
    return text[:3] + text[-2:]
```

Look at the first two lines: each is a single call, and the result goes
nowhere. No `=`, no `return`, not an argument to another call.

`text.strip()` really did compute a clean string. And threw it away the same
moment, because there was nobody to take it. `text` did not change — strings
in Python do not change at all.

## Step 4. Catch the result in a name

```python
    clean = text.strip()
    code = clean.upper()
```

Now every piece of cleaning has an address. `clean` is the label without its
edges, `code` is the same label in capitals. Note the second line: what stands
before the dot is `clean`, not `text`. Leave `text` there and the second
cleaning takes the dirty original again, and half the work is lost.

## Step 5. Cut the clean string

```python
    return code[:3] + code[-2:]
```

- `code[:3]` — the first three characters;
- `code[-2:]` — the last two;
- `+` between two pieces of text glues them, as on the previous level.

All together:

```python
def solve(text: str) -> str:
    clean = text.strip()
    code = clean.upper()
    return code[:3] + code[-2:]
```

Three lines, and every one of them can be checked on its own.

## Step 6. Run it

```
✓ returned text: yes
✓ labels matched: 10 of 10
✓ first difference: all matched
```

## Step 7. If it does not match

**Exactly one label matched** — the result of the cleaning is still not caught.
Check that `name =` stands in front of `text.strip()`.

**Some matched and the answers are lower case** — `.upper()` is called but its
result is not caught, or the slice runs over `clean` instead of `code`.

**Spaces show in the answer** — `text` is being cut, not `code`. Look at what
is inside the square brackets on the `return` line.

**Almost all matched but one** — most likely spaces were removed from inside
too, not only from the edges. A space inside the label carries meaning: the
rule about the first three characters means literally the first three
characters of the cleaned string, even when one of them is a space.

**`TypeError: ... is not subscriptable`** — a method lost its brackets:
`text.strip[:3]` instead of `text.strip()[:3]`.

**`AttributeError: 'str' object has no attribute ...`** — a typo in the method
name. The right ones: `strip`, `upper`.

**`IndexError`** — a single index somewhere instead of a slice. `code[3]` may
not exist; `code[:3]` always does.

## Step 8. Check yourself

Without looking: why does `text` still have spaces in it after `text.strip()`?
If the answer comes straight away, the level has landed — and this trap will
not catch you on any of the levels that follow.
