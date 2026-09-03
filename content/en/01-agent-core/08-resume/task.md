# Shift 8 · A second invoice for the same leg

A haul of four legs: Laredo, Dallas, Chicago, Newark. After two bookings the
process is killed. The agent comes back up and assembles the haul — the whole
thing, from the very start.

```
python engine/check.py content/en/01-agent-core/08-resume/starter/novice/agent.py
```

Look at the second check line: `Laredo | Dallas | Laredo | Dallas | Chicago |
Newark`. Six bookings for four legs. Laredo and Dallas were paid for twice — the
customer gets an invoice for both.

The agent is not at fault: everything it knew about its own work sat in
`messages`, and they died with the process.

**Make what has been done survive a restart.**

## Done when

- the first run really was cut short by a crash;
- exactly four legs were booked, once each;
- none was paid for twice;
- the agent reported four legs;
- the second run stayed within 4 iterations.

## Choose a difficulty

| Folder | What you get |
|---|---|
| `starter/novice/` | the write point marked `TODO`, with a hint about DONE |
| `starter/advanced/` | only the question of what survives the process |
| `starter/pro/` | the contract and a warning that booking is irreversible |

## If you get stuck

Try writing the leg down **before** the tool call and see what changes. The
difference between "before" and "after" is worth one leg here.
