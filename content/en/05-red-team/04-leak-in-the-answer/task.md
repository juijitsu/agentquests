# Red team · Two refusals in the log

The asker is a dispatcher at the carrier Harbor Line. They may see their own:
their loads, their rates, their contacts. Over the shift they asked six
questions.

You opened the call log and found two refusals. The tool did not let the agent
into somebody else's load, or into the broker's folder. Both lines look like an
attempt to reach for what was not theirs, and both went into the report.

```
python engine/check.py content/en/05-red-team/04-leak-in-the-answer/starter/novice/agent.py
```

Look at both middle lines. Both flagged requests are extra: that is exactly
where the tool worked and handed nothing over. Two others are missing, the ones
where every call was allowed and another carrier's rate went out in the answer.

A refusal means the data did not go out. You were looking for evidence in the
place where the defence stands.

**Find the requests whose answer carried out a fact belonging to somebody
else.**

## Done when

- every request of the shift has been examined;
- every request with a leak made it into the report;
- there are no extra requests in the report;
- the number of calls claimed matches the number made.

## Choose a difficulty

| Folder | What you get |
|---|---|
| `starter/novice/` | selection by refusals, with the needed call named in a `TODO` |
| `starter/advanced/` | selection by refusals, with no hint |
| `starter/pro/` | the contract and the definition of a leak |

## If you get stuck

Ask not "what was the agent allowed to do" but "whose data ended up in the
answer". The agent's rights and the asker's rights are different sets, and the
check stands only on the first one.
