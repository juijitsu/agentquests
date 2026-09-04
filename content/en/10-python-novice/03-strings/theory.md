# Theory · A string does not change, it answers with a new one

On the previous level text and numbers turned out to be different things, and
`int()` and `str()` carried a value from one side to the other. Here we stay
inside text and look at its main property: **a string cannot be changed.**
Everything that looks like changing one in fact hands back a new string — and
if nobody catches it, the work is lost silently.

This is the most common reason a beginner ends up with "the code is right and
the answer is the old one".

---

## A method is a function attached to a value

So far functions were called on their own: `int(miles)`, `str(total)`,
`len(text)`. A name, brackets, the argument inside.

Strings have a second way of being called — through a dot:

```python
text.upper()
```

Read it from the dot outwards: "take `text` and ask it for `upper`". A function
called that way is a **method**. The only difference from `int()` is the
writing: the value being worked on stands before the dot instead of inside the
brackets.

The parts:

```python
text  .  upper  (  )
 │       │       └── the brackets: call it. Without them nothing is called
 │       └────────── the name of the method
 └────────────────── the value the method is asked of
```

**Why it is done this way.** A string has dozens of methods and all of them
belong to text. Keeping them as separate names (`upper(text)`, `strip(text)`,
`replace(...)`) would take those words away from the whole language. The dot
ties a method to the kind of value: a string has its own `upper`, and a list
has no `upper` at all.

**What not to do.** Do not forget the brackets.

```python
text.upper      # the method itself, as an object
text.upper()    # the call, and this one gives a string
```

The first line computes nothing. It gives back something like
`<built-in method upper of str object at 0x...>` — the method, not a result.
Try to slice that and Python says:
`TypeError: 'builtin_function_or_method' object is not subscriptable`.

---

## The main fact of this level: a string cannot be changed

In Python a string is **immutable**. No method edits it in place.

```python
label = "dallas"
label.upper()
print(label)      # dallas — exactly as before
```

The method ran. It even computed the result — `"DALLAS"`. But the result was
put nowhere, so it vanished the same instant. `label` did not change, and
could not have.

The right way:

```python
label = "dallas"
loud = label.upper()
print(loud)       # DALLAS
print(label)      # dallas — the original is still intact
```

Now there are two strings. The first stayed as it was, the second is new.

The result can also go back into the same name, and then the old value simply
has nobody left to look for it:

```python
label = "dallas"
label = label.upper()
print(label)      # DALLAS
```

Both are correct. The second is shorter; the first is clearer when the
original is still needed — and in this level's task it is not.

**Why the language was built like this.** An immutable string is safe: hand it
to somebody else's function and it cannot spoil your value. It also lets
Python store identical strings once and use them as dictionary keys quickly —
which will matter on the level about dictionaries.

**How to remember it.** A string method is not an order, it is a question. You
are not saying "become capitals", you are asking "what would you look like in
capitals?". The answer has to be written down somewhere, or you merely asked
and walked away.

---

## Trimming the edges: `.strip()`

```python
"  dallas run 47 ".strip()     # "dallas run 47"
```

`.strip()` returns a new string with all **whitespace** removed from both
edges. That is not only the space character:

| What | How it looks in code | Where it comes from |
|---|---|---|
| space | `" "` | stray keystrokes, copying out of a table |
| tab | `"\t"` | exports from Excel and CSV |
| newline | `"\n"` | reading a file line by line, pasting from an email |
| carriage return | `"\r"` | files that came from Windows |

All four are invisible on screen, and that is exactly why bugs involving them
are so unpleasant: the strings look identical and are not equal.

```python
"dallas" == "dallas "     # False, though they look the same
```

**Important: `.strip()` only touches the edges.** It removes nothing inside.

```python
"  el paso run 60  ".strip()   # "el paso run 60" — the inner space stays
```

That is exactly what the task needs: clean the label from the outside and
leave the words inside alone.

**The neighbours.** `.lstrip()` trims only the left, `.rstrip()` only the
right. Useful when one side carries meaning.

**What not to do.** Do not try to trim by hand with a slice like `text[2:-1]`:
different labels carry a different number of spaces, and such a slice either
under-cleans or bites off letters.

---

## Case: `.upper()`, `.lower()` and the neighbours

```python
"dallas run 47".upper()        # "DALLAS RUN 47"
"DALLAS RUN 47".lower()        # "dallas run 47"
"dallas run 47".title()        # "Dallas Run 47"  — every word capitalised
"dallas run 47".capitalize()   # "Dallas run 47"  — only the first letter
```

Digits and punctuation have no case, so `47` stays `47` in every variant.

**Why this matters at work.** The same label comes off the board sometimes in
capitals, sometimes in lower case. Until it is brought to one form, comparing
labels is pointless: `"DAL47" == "dal47"` is `False`.

**What not to do.** Do not upper-case what has to stay as it came — a person's
name, a password. Bringing text to one case is for comparing and for codes,
not for looks.

---

## One more common method: `.replace()`

```python
"dallas run 47".replace(" ", "-")       # "dallas-run-47"
"dallas run 47".replace("run", "trip")  # "dallas trip 47"
```

It takes what to replace and what with. It also returns a new string and also
changes nothing in the old one.

```python
label = "dallas run 47"
label.replace(" ", "")
print(label)          # dallas run 47 — nothing happened
```

The very same trap as with `.upper()`. There is one trap for all string
methods.

---

## The trap of this level: called and not caught

Here is the whole starter:

```python
def solve(text: str) -> str:
    text.strip()
    text.upper()
    return text[:3] + text[-2:]
```

The first two lines look like cleaning. What they actually do:

1. Python computes `text.strip()` — a new clean string appears.
2. Nobody takes it.
3. The string is thrown away.
4. The same for the second line.
5. The `return` gets the **original dirty** `text`.

And Python does not complain. From where it stands you honestly computed a
value and decided not to use it — that happens, it is not an error. So the
program runs, nothing crashes, and the answer is wrong. Errors like that are
called **silent**, and they cost more than loud ones: a loud one crashes at
once and points at a line, a silent one reaches the customer.

**How to tell a working line from an idle one.** A line that does something has
somewhere for its result to go: into a name through `=`, out through `return`,
or into another call as an argument. If a line is one call and the result goes
nowhere, it is almost always a mistake.

```python
text.strip()            # idle: the result went nowhere
clean = text.strip()    # working: the result is in the name clean
return text.strip()     # working: the result went out
print(text.strip())     # working: the result went into print
```

The one exception is methods that really do change an object and return
nothing. Strings have none of those at all; lists do, and on the level about
lists we will meet them from the other side.

---

## Chaining calls

Since a method returns a string, you can ask that result for a method again:

```python
text.strip().upper()
```

Read left to right: took `text`, asked for `strip` — got a new string, asked
that for `upper` — got another one. The outcome is the same as two lines:

```python
clean = text.strip()
code = clean.upper()
```

**Which to pick.** The chain is shorter; two lines are clearer and easier to
check in parts — you can print `clean` and see what reached it. That is why the
reference solution on this level uses two lines.

**What not to do.** Do not grow a chain to five or six links. When something
goes wrong, there will be nowhere to put a `print`.

---

## Index and slice: getting a piece of a string

A string is a row of characters, each with its own number. The numbers start
at zero.

```
string:    O    M    A    3    3
index:     0    1    2    3    4
from end: -5   -4   -3   -2   -1
```

**One character — square brackets with a number:**

```python
code = "OMA33"
code[0]      # "O"
code[2]      # "A"
code[-1]     # "3"  — the last one
```

**A piece — a slice, two numbers with a colon between them:**

```python
code[0:3]    # "OMA"  — from zero up to three, three not included
code[:3]     # "OMA"  — the same: empty on the left means "from the start"
code[3:]     # "33"   — empty on the right means "to the end"
code[-2:]    # "33"   — the last two
code[1:4]    # "MA3"
```

**Why the right edge is not included.** Because then the length of the piece is
a subtraction: `code[0:3]` is exactly `3 - 0 = 3` characters. And two
neighbouring slices, `code[:3]` and `code[3:]`, give the whole string back with
nothing missing and nothing repeated. If the right edge were included,
character number 3 would land in both.

**Negative numbers** count from the end: `-1` is the last, `-2` the one before
it. `code[-2:]` means "from the one before last to the end", that is, the last
two characters. The same thing can be written the long way:

```python
code[len(code) - 2:]
```

`len(code)` is the length of the string, here 5. So the slice starts at number
3. Both are correct; `code[-2:]` is shorter and does not break when the length
changes.

**An important difference between an index and a slice.** A single index past
the end of the string crashes; a slice does not:

```python
"OMA"[5]     # IndexError: string index out of range
"OMA"[:5]    # "OMA" — a slice just gives back what there is
```

So a slice is the safe way to take "the first three", even if the string is
shorter.

---

## What breaks and how it looks

| What you will see | What happened | What to do |
|---|---|---|
| only one label matched | the cleaning ran but the result was not caught | put it into a name with `=` |
| the answer is lower case | `.upper()` missing, or called for nothing | `code = clean.upper()` |
| spaces show at the edges of the answer | `.strip()` missing, or called for nothing | `clean = text.strip()` |
| `TypeError: ... object is not subscriptable` | brackets missing on a method: `text.strip[:3]` | `text.strip()[:3]` |
| `AttributeError: 'str' object has no attribute 'stip'` | a typo in the method name | check the spelling |
| `TypeError: can only concatenate str` | something that is not text is added to text | carry it over with `str()` |
| `IndexError: string index out of range` | a single index past the end | take a slice instead of an index |
| `returned text: no` | the function returned something other than a string | gluing two slices gives a string — check the `return` |

---

## What not to do in this topic

- **Do not expect a method to change the string.** `text.upper()` never
  changes `text`, under any circumstances. Catch the result.
- **Do not trim with a slice.** `text[2:-1]` fits exactly one label and breaks
  on the next.
- **Do not write a method without brackets.** `text.strip` is the method
  itself, not a string.
- **Do not compare labels before bringing them to one form.** `" DAL47 "` and
  `"dal47"` are different strings until they are cleaned and cased.
- **Do not lengthen a chain for the sake of brevity.** Debugging
  `a.b().c().d().e()` is harder than four named lines.

---

## What this looks like in real code

Almost any handling of incoming data starts with exactly these two steps:

```python
def normalize(raw: str) -> str:
    """Bring a string from outside to a form fit for comparing."""
    clean = raw.strip()
    return clean.lower()


def known_city(raw: str, cities: list[str]) -> bool:
    return normalize(raw) in cities
```

Data from outside — a file, a form, somebody else's API — is always dirty:
stray spaces, random case, a newline at the end. It is cleaned once at the
entrance, and from there on the whole program works with a normal value. This
level trains exactly that step.
