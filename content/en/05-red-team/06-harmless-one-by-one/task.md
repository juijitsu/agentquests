# Red team · Before and after look the same

The nightly maintenance batch ran over carrier record CX-4471: ten steps, each
with its own access check.

You took two snapshots. You asked the guard about every step before the batch,
ran the batch, and asked again afterwards. Whatever turned from refused into
permitted went into the report.

```
python engine/check.py content/en/05-red-team/06-harmless-one-by-one/starter/novice/agent.py
```

Look at both middle lines. One step is extra: the dedicated lane is permitted
at the end, but it ran third, two steps before the insurance was verified. And
two steps are missing, the ones the whole thing was about: the credit hold was
released and the load was tendered.

They are invisible because the last step of the batch put the defaults back.
The carrier is provisional again, the hold is on again. And the hazmat load has
been tendered.

**Find the steps the guard refuses on their own and permits at the moment they
run.**

## Done when

- every step has been probed on its own against the untouched record;
- the whole batch has been run, in order;
- every step permitted only inside the batch made it into the report;
- there are no extra steps in the report.

## Choose a difficulty

| Folder | What you get |
|---|---|
| `starter/novice/` | two snapshots, with a `TODO` naming where to move the question |
| `starter/advanced/` | two snapshots, with no hint |
| `starter/pro/` | the contract and the definition of the step you are after |

## If you get stuck

The guard reads the record at the moment the step runs. So that is where you
have to ask it: inside the loop, right before `run_step`. The record after the
batch answers a different question.
