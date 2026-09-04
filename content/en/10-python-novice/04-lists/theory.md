# Theory · A list, its order, and a place in it

So far we have had one value at a time: a piece of text, a number. Here a
**list** turns up — many values under one name, lined up in a row. And with it
comes a new idea: **place**. A value in a list has a number, and that number
depends on the order. Order does not appear by itself.

Hence the trap of this level: the middle of a list and the middle by size are
different things until the list is lined up.

---

## What a list is

```python
quotes = [1200, 900, 1450]
```

Square brackets, values separated by commas. This is one value — a list — but
inside it holds three numbers, and they stand in a definite order.

**Why.** Three bids may come in, or five, or forty. Giving each one its own
name is impossible. A list keeps them together and lets you work with them as
a single thing.

**What can go in.** Anything, including a mixture:

```python
[1200, 900, 1450]              # numbers
["dallas", "memphis"]          # strings
[]                             # an empty list is a list too
```

In practice one list holds one kind of thing: all the bids, all the cities. A
mixture of numbers and strings almost always means the data arrived dirty.

**How many elements.** The same `len` that measured the length of a string:

```python
len([1200, 900, 1450])    # 3
len([])                   # 0
```

---

## The place of an element: the index

As with a string, the elements of a list have numbers, and they start at zero.

```
list:     [1200,  900, 1450]
index:        0     1     2
from end:    -3    -2    -1
```

```python
quotes = [1200, 900, 1450]
quotes[0]     # 1200 — the first
quotes[1]     # 900
quotes[-1]    # 1450 — the last
```

**Why from zero.** An index is not "which one in the count" but "how many
steps from the start". There are no steps to take to reach the first element,
hence zero. We saw the same logic in slices on the previous level: `code[:3]`
is three steps from the start.

**What breaks.** A number past the end of the list:

```python
quotes[3]     # IndexError: list index out of range
```

Three elements means numbers 0, 1, 2. There is no 3. The last element always
has the number `len(quotes) - 1`, and that is the single most common source of
off-by-one bugs.

---

## A list is mutable, and that is the difference from a string

On the previous level we established that a string cannot be changed: every
method hands back a new one. **With a list it is the other way round** — it
can be changed in place.

```python
quotes = [1200, 900, 1450]
quotes[1] = 1000
print(quotes)          # [1200, 1000, 1450] — the same list, different contents
quotes.append(700)
print(quotes)          # [1200, 1000, 1450, 700]
```

`append` adds an element at the end and **returns nothing** — it changes the
list itself. This is exactly the exception mentioned on the previous level:
strings have no methods like that, lists do.

**Why languages do it this way.** A list is usually large and lives a long
time: things get added to it and removed from it. Copying the whole thing
every time would be expensive. A string, on the other hand, is usually small
and serves as a value, and being immutable makes it safe.

**Where the danger is.** A mutable list handed to a function is the very same
list, not a copy. If the function reorders it, it is reordered on the outside
too. That is exactly why the check on this level hands your function a copy.

---

## Two ways to put a list in order

Here the language offers two tools, and mixing them up is a classic mistake.

### `sorted(list)` — a function, gives back a new list

```python
quotes = [1200, 900, 1450]
in_order = sorted(quotes)
print(in_order)    # [900, 1200, 1450] — a new list
print(quotes)      # [1200, 900, 1450] — the old one untouched
```

It works like `len()` or `str()`: a name, brackets, the argument inside. The
result has to be caught in a name — as on the previous level.

### `list.sort()` — a method, reorders in place

```python
quotes = [1200, 900, 1450]
quotes.sort()
print(quotes)      # [900, 1200, 1450] — the same list, now in order
```

The method creates nothing new. It rearranges the elements inside the list
itself and **returns None** — that is, nothing.

**And here is where the trap sits:**

```python
in_order = quotes.sort()   # in_order became None
len(in_order)              # TypeError: object of type 'NoneType' has no len()
```

Out of habit from the previous level you want to catch the result in a name.
But there is nothing to catch: `sort()` has already done the work and handed
back emptiness.

**How to keep the difference straight.**

| | `sorted(quotes)` | `quotes.sort()` |
|---|---|---|
| what it is | a function | a list method |
| the old list | untouched | reordered |
| returns | a new list | `None` |
| catch the result | always | nothing to catch |
| works on | a list, a string, anything you can walk through | a list only |

**Which to pick.** If the original order is still needed — `sorted()` and
nothing else. If it is not, and the list is large, `sort()` is cheaper because
it copies nothing. The reference solution on this level uses `sorted()`: it
reads more plainly and does not depend on whose copy the list is.

**Descending:** `sorted(quotes, reverse=True)` or `quotes.sort(reverse=True)`.

---

## The middle: whole division

The number of the middle of a list is its length halved. But an index has to
be a whole number, and ordinary division gives a fraction:

```python
len([1200, 900, 1450]) / 2     # 1.5  — a fraction
len([1200, 900, 1450]) // 2    # 1    — whole
```

Two slashes mean **whole division**: the fractional part is dropped.

```python
quotes[1.5]    # TypeError: list indices must be integers or slices, not float
quotes[1]      # 900
```

For an odd length `len // 2` always lands exactly in the middle:

| length | indexes | `len // 2` | the middle |
|---|---|---|---|
| 1 | 0 | 0 | 0 ✓ |
| 3 | 0 1 2 | 1 | 1 ✓ |
| 5 | 0 1 2 3 4 | 2 | 2 ✓ |
| 7 | 0 … 6 | 3 | 3 ✓ |

There are as many elements to the left of the middle as to the right. For an
even length a single middle element does not exist at all — which is why the
number of bids in the task is always odd.

---

## Why the middle of an unsorted list means nothing

```
as it arrived:  [1200,  900, 1450]      the element in the middle = 900
in order:       [ 900, 1200, 1450]      the element in the middle = 1200
```

Bids arrive in whatever order the carriers hit send. That order says nothing
about money. Taking the middle element of such a list is like asking "which
bid came in third": you get an answer, and it means nothing.

Sometimes that answer happens to be right — when the middle was already in its
place. That is exactly what makes the bug dangerous: on part of the data the
code "works".

---

## Why the middle by rank and not the average

These are two different questions, and they give different answers.

```python
quotes = [900, 950, 1000, 3800, 4000]
sum(quotes) // len(quotes)   # 2130 — the arithmetic average
sorted(quotes)[2]            # 1000 — the one in the middle
```

The average is dragged up by two inflated bids. The middle by rank says
something else: half the carriers ask for under a thousand and half for more.
For the decision "what does this cost on the market" the second number is the
honest one.

The value in the middle is called the **median**. It is used wherever a few
outliers can wreck the picture: salaries, house prices, service response times.

---

## What breaks and how it looks

| What you will see | What happened | What to do |
|---|---|---|
| not all sets matched | the list was never put in ascending order | `in_order = sorted(quotes)` |
| `TypeError: object of type 'NoneType' has no len()` | the result of `sort()` was caught in a name | `sort()` returns `None`, there is nothing to catch |
| `TypeError: 'NoneType' object is not subscriptable` | the same thing, but with an index | use the list itself, not the result of `sort()` |
| `AttributeError: 'list' object has no attribute 'sorted'` | `sorted` was called as a method | `sorted(quotes)`; the method is `quotes.sort()` |
| `TypeError: list indices must be integers` | the index came out as a fraction | `//` instead of `/` |
| `IndexError: list index out of range` | a number past the end of the list | the last number is `len(quotes) - 1` |
| `TypeError: '<' not supported between instances of ...` | values of different kinds in the list | only comparable things can be sorted |

---

## What not to do in this topic

- **Do not take an element by number without knowing the order.** A number
  only means something together with an order.
- **Do not catch the result of `sort()`.** It is `None`. This is the mirror of
  the previous level: there the result had to be caught, here there is nothing
  to catch.
- **Do not halve the length with a single slash.** `len(quotes) / 2` gives a
  fraction, and an index has to be whole.
- **Do not treat `quotes[len(quotes)]` as the last element.** The last is
  `quotes[len(quotes) - 1]`, or simply `quotes[-1]`.
- **Do not sort somebody else's list in place** if its order still matters to
  them: `sort()` changes the very list you were handed.

---

## What this looks like in real code

```python
def median(values: list[int]) -> float:
    """The value in the middle. For an even length, the average of the two."""
    in_order = sorted(values)
    middle = len(in_order) // 2
    if len(in_order) % 2 == 1:
        return in_order[middle]
    return (in_order[middle - 1] + in_order[middle]) / 2
```

The first two lines are exactly what the reference solution on this level
does. After that comes the even-length case: there is no single middle
element then, so the two neighbours are averaged. The task deliberately has no
such case — the odd-count rule takes it away so that the level stays about
order rather than about branching. Branching comes on the level about
conditions.
