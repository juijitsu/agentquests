# Theory · Step done ≠ task done

On the previous level the plan was known in advance: four legs, walk them all,
add them up. Tasks like that are convenient and rare.

More often there is no plan, because none can be made. Dispatch hands you only
the next stop: get to Dallas and you find out what comes after Dallas. The route
is discovered on the way, and even the number of steps is unknown up front.

## Where the mistake comes from

Remember the loop exit condition you wrote in Foundations:

```python
if not response.tool_calls:
    return response.text, step
```

It means "the model stopped asking for tools". In a simple task that coincided
with "the task is solved" — because the task was one step long.

In a multi-step task it does not coincide. The model reports on a **step**: "we
reached Dallas". It needs no tools at that moment, `tool_calls` is empty, the
loop exits — and an intermediate result goes out the door dressed as a final one.

**The exit condition was technical. The task needs a meaningful one.**

## Who decides the work is finished

Not the model. It sees one step and reports on it honestly — nobody asked it for
more.

Your code decides, because the goal is stated in it:

```python
if GOAL in response.text:
    return response.text, step
```

That is the difference between an agent that performs steps and an agent that
solves a task.

## What to do when the task is not finished

Continue the loop, telling the model where things now stand. A model with no
memory and no context will again see only the last step — so that step has to be
handed to it. Hence the addition to the history: "we reached Dallas, where next".

The loop continues exactly until the goal is reached or the steps run out. The
limiter matters especially here: in a task of unknown length it is easy to drive
off into infinity.
