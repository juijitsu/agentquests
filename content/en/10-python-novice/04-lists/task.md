# Task · The middle bid

## What to do

Carriers have answered the call for a run, each naming a price. The bids
arrive as a list of whole numbers, in the order they were sent. The dispatcher
does not want the lowest one and does not want the arithmetic average — they
want the bid that ends up **exactly in the middle** once every bid is lined up
in ascending order.

Return that bid as a number.

```
solve([1200, 900, 1450])                 ->  1200
solve([700, 1100, 950, 800, 1300])       ->  950
solve([2400, 1800, 2150])                ->  2150
```

The number of bids is always odd, so there is always exactly one middle.

**Note this:** in the second example the answer happens to be the element that
was already standing in the middle of the list. That is a coincidence, not a
rule.

## Why the starter does not pass

It takes `quotes[len(quotes) // 2]` — the middle of the list exactly as it
arrived. The order in which bids were sent says nothing about their size, so
that middle is an accident.

The starter matches on two sets out of nine: in one the middle happened to be
in place already, and the other set holds a single bid.

## Done when

- the function returns a whole number instead of printing it;
- all nine sets matched.

The task shows three; the check runs nine. Among the hidden ones are a set of
seven bids, a set of one, and a set that is nearly in ascending order but not
quite.

## What not to do in this task

- **Do not take an element by number before lining the list up.** A number
  only means something together with an order.
- **Do not write `in_order = quotes.sort()`.** The `sort()` method reorders the
  list in place and returns `None` — there is nothing to catch.
- **Do not compute the arithmetic average.** `sum(quotes) // len(quotes)` is a
  different quantity, and on this data it comes out different.
- **Do not halve the length with a single slash:** `len(quotes) / 2` gives a
  fraction, and an index has to be whole.

## Choose a difficulty

| Folder | What you get |
|---|---|
| `starter/novice/` | the starter and a `TODO` with the lines you need |
| `starter/advanced/` | the starter and one line about what is wrong |
| `starter/pro/` | the function contract only |

## If you get stuck

Ask yourself what the number of an element means. It means a place, and a
place depends on the order. So the order has to be set by you — before taking
an element by its number.
