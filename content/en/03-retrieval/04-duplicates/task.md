# Retrieval · Three documents about one thing

The dispatcher asks what a mile on Laredo — Newark comes to **in total**. The
right answer is 3.25: the base rate 2.90 plus the fuel surcharge 0.35.

The agent answers: 2.90.

```
python engine/check.py content/en/03-retrieval/04-duplicates/starter/novice/agent.py
```

Look at the second check line: the selection holds one fact. The base rate sits
in five documents — the price list, the email to the customer, the report, the
archived copy and the billing export — and three of them took the whole
selection. The surcharge stands sixth and never made it.

**Build the selection so that every next chunk adds something new.**

## Done when

- chunks were compared for repetition;
- the selection holds both facts — the rate and the surcharge;
- the answer names 3.25;
- no more than two calls to the model.

## Choose a difficulty

| Folder | What you get |
|---|---|
| `starter/novice/` | a top-3 slice, with the call you need named in the `TODO` |
| `starter/advanced/` | only a note that the ranking is correct |
| `starter/pro/` | the contract and both quantities |

## If you get stuck

Comparing by text will not help here: "Price list: Laredo — Newark, 2.90 per
mile" and "Email to the customer: confirming 2.90 per mile" share not one line.
One fact, different words.
