# Method · How to solve it, step by step

## Step 1. Run the starter as it is

It works and it is wrong. The verdict:

```
✓ returned a number: yes
✗ sets matched: 2 of 9
✗ first difference: on the bids [1200, 900, 1450]
      in order: [900, 1200, 1450]
      expected: 1200
      got:      900
```

The verdict prints two lines in a row: the set as it arrived, and the same set
in order. That is the whole level. In the middle of the set that arrived
stands `900`; in the middle of the ordered one, `1200`. Different bids.

## Step 2. Work out why exactly two sets matched

Nine sets, two matched. Neither is an accident, and each has its own reason.

**The first:** `[700, 1100, 950, 800, 1300]`. Here `950` already stands in its
place: two bids below it, two above. The carriers sent them in that order by
chance, but the middle lines up.

**The second:** `[1750]`. One bid. There is nothing to sort, and the middle is
always the bid itself. A set like that passes with any approach.

Both say the same thing: the code does not "work sometimes", it does not do
the required job at all, and the matches come from the data.

## Step 3. Look at what the starter actually takes

```python
def solve(quotes: list[int]) -> int:
    middle = len(quotes) // 2
    return quotes[middle]
```

Both lines are honest: `len(quotes) // 2` really does give the number of the
middle, and `quotes[middle]` really does take the element with that number.

What is missing is the step between them. The number of the middle only means
something once the list is in ascending order. The list from the carriers is
not: it comes in whatever order they hit send.

## Step 4. Put the bids in order

```python
    in_order = sorted(quotes)
```

`sorted()` returns a **new** list in ascending order. The original `quotes`
stays as it was — we will not need it again, but knowing that matters.

**Do not write this:**

```python
    in_order = quotes.sort()    # in_order becomes None
```

`sort()` reorders the list in place and returns nothing. If you want that one,
use it without an assignment:

```python
    quotes.sort()
    middle = len(quotes) // 2
    return quotes[middle]
```

Both are correct. The walkthrough below follows the first.

## Step 5. Count the middle on the ordered list

```python
    middle = len(in_order) // 2
    return in_order[middle]
```

Note that both the length and the element come from `in_order`. The two lists
have the same length, so `len(quotes)` here would not be a mistake — but
`quotes[middle]` on the last line would give back the same wrong value again.
It is simpler to stay on one name and not have to think about it.

All together:

```python
def solve(quotes: list[int]) -> int:
    in_order = sorted(quotes)
    middle = len(in_order) // 2
    return in_order[middle]
```

## Step 6. Run it

```
✓ returned a number: yes
✓ sets matched: 9 of 9
✓ first difference: all matched
```

## Step 7. If it does not match

**Still two sets matched** — the sorting is either not applied, or applied
while the element is taken from the old list. Check that the square brackets
on the last line hold `in_order`, not `quotes`.

**`TypeError: object of type 'NoneType' has no len()`** — the line reads
`in_order = quotes.sort()`. The `sort()` method returns `None`. Use
`sorted(quotes)`, or drop the assignment.

**`TypeError: 'NoneType' object is not subscriptable`** — the same thing, the
error just surfaced on the line with the index.

**`AttributeError: 'list' object has no attribute 'sorted'`** — the line reads
`quotes.sorted()`. `sorted` is a function: `sorted(quotes)`. The list's own
method is called `sort`.

**`TypeError: list indices must be integers`** — dividing with one slash gave
a fraction. It has to be `//`.

**`IndexError: list index out of range`** — a number past the end. With whole
division that usually means something was added to the middle.

## Step 8. Check yourself

Without looking: why is `quotes[len(quotes) // 2]` right for
`[700, 1100, 950, 800, 1300]` and wrong for `[1200, 900, 1450]`? If the answer
comes straight away, the link "a number only means something once the order is
known" has landed — and that is half of all the work with lists.
