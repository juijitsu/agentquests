# Theory · Five of six, but which five

The set is clean, there is no leak, the judge is independent. The run gives five
of six.

A second run of the same set by the same system gives three of six.

## The model does not always answer the same way

This is not a breakage and not a fluke in the data. A language model is
non-deterministic by construction: the same request can produce different
answers, and the harder the case, the more often they diverge.

Inside the set it looks like this:

```
c1  ✓ ✓ ✓ ✓ ✓     holds every time
c2  ✓ ✓ ✓ ✓ ✓
c3  ✓ ✓ ✓ ✓ ✓
c4  ✗ ✗ ✗ ✗ ✗     never works
c5  ✓ ✗ ✓ ✗ ✓     every other time
c6  ✓ ✓ ✗ ✗ ✗     every other time
```

Three cases are reliable, one is reliably broken, and two are **not reliable in
either direction**.

On run zero both unstable ones came out lucky. Hence five of six.

## One number instead of three states

The main mistake here is not that the score is inflated. It is that cases of
different kinds are glued into one number.

A case has three states, not two:

- **works** — correct on every run;
- **does not work** — wrong on every run;
- **does not hold** — sometimes one way, sometimes the other.

The third state is worse than the second. Broken things get fixed: they are
visible, they reproduce, a ticket gets filed. An unstable one lives for years: it
reproduced for one developer and not for another, the ticket is closed as "cannot
reproduce", and in production it fails once every three days.

Measuring with one run, you **cannot tell the second from the third** and so
cannot even learn that you have a problem of that kind.

## How many runs

Enough for the instability to show itself. One is always too few, two is almost
always too few, five already shows something. The exact number depends on how
rare the failures are and how expensive a run is.

The rule is simpler than the number: **if a case never changed its verdict, you
have not run it enough times to claim that.**

## What to show

Not the average share. "Case c5 is correct in sixty percent of runs" sounds
scientific and does not help: the decision about it is binary anyway — can you
build on it or not.

A list is more useful: what holds and what does not. **Unstable cases are a line
of their own in the report**, because the work on them is its own too.
