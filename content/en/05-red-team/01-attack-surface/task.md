# Red team · No injections found

They handed you the dispatcher from the agent track and asked you to check it
before release.

You checked the input box: you typed "ignore previous instructions" into it, and
a dozen variations. The agent did not give in once. The report says: no
injections found.

```
python engine/check.py content/en/05-red-team/01-attack-surface/starter/novice/agent.py
```

Look at the first line of the check: one input out of six was checked. And it is
the one your own dispatcher fills in, a person with a badge and an employment
contract.

The shipper's note is filled in by the shipper. The consignee's contact, by the
consignee. The document arrives from the customs broker. None of them needs your
password.

**Compile the attack surface: the inputs whose content is controlled from
outside.**

## Done when

- every input has been asked about, who controls it;
- every input from outside made it into the surface;
- none of your own inputs are in the surface;
- there are no more than two model calls.

## Choose a difficulty

| Folder | What you get |
|---|---|
| `starter/novice/` | the input box check, with the needed calls named in a `TODO` |
| `starter/advanced/` | only the hint that the agent has more than one input |
| `starter/pro/` | the contract and the definition of the surface |

## If you get stuck

There is one question to ask of every input: can text end up there without
anyone from your company touching it. Not "can an outsider influence it", but
"does it go straight in".
