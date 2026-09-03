# Shift 10 · The whole dispatcher

The finale of the track. No new techniques — everything you need you have already
covered. Only one thing is new: it all works at once.

The shift starts with three events. Handling the breakdown spawns a fourth —
hiring a carrier at triple price. It is irreversible, so it goes to a human. The
human agrees. The process dies exactly between the yes and the doing.

```
python engine/check.py content/en/01-agent-core/10-boss/starter/novice/agent.py
```

The starter breaks the first three conditions, and the check shows that line by
line — fix them one at a time, each verdict line belongs to its own level. The
fourth it satisfies by accident: walking a snapshot is finite on its own. Live
reading takes that property away, and the limiter becomes yours to add.

## Done when

- all four actions were handled, including the one born mid-shift;
- the human was disturbed only about the irreversible;
- there was one request to them, not two;
- no approval went through blind;
- the report names the right number;
- the second run stayed within 6 iterations.

## Choose a difficulty

| Folder | What you get |
|---|---|
| `starter/novice/` | four `TODO`s, each naming the level the skill came from |
| `starter/advanced/` | the list of four conditions and code breaking all of them |
| `starter/pro/` | the contract and the acceptance criteria |

## If you get stuck

Work through one verdict line at a time, not all of them at once. The order they
come in matches the order of actions inside a round: queue first, then the human,
then execution.

## After this level

The Agent Core track is finished. You can build an agent that plans, replans,
remembers what matters, checks itself, works through a stream of tasks, survives
a restart and knows when to call a human.

Next is the Context track: how none of this falls apart once there is more data
than fits.
