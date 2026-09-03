# Theory · What survives a restart

For seven levels running we quietly assumed there is one run and it reaches the
end. The agent started with a clean history, filled it up and returned an answer.
Nothing happened between the beginning and the end.

In real life something does. A deploy restarts the process, the scheduler kills
the task on timeout, the kernel takes it out on memory, the machine reboots. The
haul does not end at that point — it still has to be finished.

## Two memories that are easy to confuse

**The conversation history** is `messages`. It lives in the process's memory and
disappears with it. No earlier level could notice this, because the process never
died.

**The state of the work** is the record of what has already been done in the
world. It has to live outside the process: in a file, in a database, in a queue.
Here the `DONE` list plays that part, and it is the only thing that survives a
crash.

The difference shows up in one question: **if the process died right now, what
would be left?** Everything that never made it into the state has to be done
again.

## Why "do it again" is not free

While actions are read-only, repetition is harmless: you can re-read a route ten
times. But here a booking is **paid for and irreversible**. A restart with no
state means a second tractor on the same leg and a second invoice for the
customer.

Irreversible actions are exactly what separates toy agents from real ones.
Sending an email, a payment, a publication, a deletion — all of them share one
property: they cannot simply be repeated.

## The order of writing decides

It seems you could write at any moment. You cannot:

- **Written before the action** — a crash between the write and the action leaves
  a mark for work that never happened. The agent comes back up and skips a leg.
- **Written after the action** — a crash between the action and the write forces
  one step to be repeated. Annoying, but recoverable.

Of the two evils the second is chosen, and on this level only it passes the
check. **Write down what has already happened, not what you are about to do.**

## Why a crash cannot be caught

`Crash` inherits from `BaseException`, not from `Exception` — like the real
`KeyboardInterrupt` and `SystemExit`. This is not hierarchy pedantry: if a crash
were caught by an ordinary `except Exception`, the habit from the Foundations
lesson "an error is a message" would let you wrap it in a `try` and never solve
the task.

A real `kill -9` is caught by nothing. The only way to prepare for it is in
advance.
