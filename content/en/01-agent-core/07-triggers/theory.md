# Theory · The agent that gets woken up

Until now the world stood still. The question was asked once, the route was known
in advance, facts turned up along the way, but the task itself did not change.
The agent answered a person, and the person waited.

Here everything differs from the first line: **`run()` has no argument.** Nobody
is asking the agent anything. It is being woken up.

## What a trigger changes

Event-driven startup inverts the relationship with time. Work used to exist in
full before the start, and the agent drained it. Now work **keeps arriving while
the agent works** — and part of it is created by the agent itself.

The dispatcher handles the breakdown near Memphis and by doing so creates a new
task: the load on the stalled tractor has to be moved. Handling the ice storm
produces a detour. Neither task existed at the moment of the wake-up.

## Snapshot versus a live queue

Hence the single mistake of this level, and it looks entirely innocent:

```python
queue = run_tool("pending", {}).split(" | ")
for event in queue:
    ...
```

The `queue` variable is a **photograph of the queue** taken before the first
action. It is accurate for exactly one instant. After that the queue lives its
own life and the list lives its own.

The failure comes out perfectly quiet. No event was lost, no tool broke, the
agent honestly handled everything it saw and closed the shift. It just did not
see everything.

## The exit condition moved outside

The loop used to end when the model stopped asking for tools — that is, the
interlocutor decided. Now **the stopping condition belongs to the world, not to
the conversation**: the work is over when the queue says it is empty.

Only your code can ask it that, and it has to ask on every round. The model knows
nothing about the queue: it is shown one event and says what to do with it.

## Why this is how all real agents are built

Everything that does not run on a button press is built this way: a webhook
handler, mail triage, alert response, a nightly run. A task arrives, spawns
subtasks, those spawn their own. An agent that reads the queue once looks like it
works right up to the day one event first spawns another.
