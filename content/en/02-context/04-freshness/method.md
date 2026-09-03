# Method · The maximum inside a group

**Step 1. Name the key.** It is the thing freshness is computed within. Here it is
`lane`: every lane has its own history.

**Step 2. Find the maximum time for that same key.** The link between the outer
and the inner query is the whole point of the technique:

```sql
WHERE quoted_at = (
  SELECT MAX(quoted_at) FROM rates AS latest WHERE latest.lane = rates.lane
)
```

Remove the `latest.lane = rates.lane` condition and you get the maximum across
the whole table — which is exactly the wrong fix.

**Step 3. Return only the columns you need.** The question is about the lane and
the price; the date was for filtering, not for the answer.

**Step 4. Fit it into one query.** Picking the fresh row is not a multi-step
procedure. If it takes two queries, you are computing in the second what the
database can compute in the first.

---

An honesty check: **add one more fresh row for a different lane and run the query
in your head.** If the answer for your lane changed, freshness is being computed
across the table rather than within the group.
