# Evaluation · The finale of the track

No new techniques. What is new is only that all five work at once, and the
outcome drives a real decision: ship the new version or not.

The quick report — one run, self-grading, one number — shows nine of nine. A
hundred percent.

```
python engine/check.py content/en/04-evaluation/08-boss/starter/novice/agent.py
```

The starter breaks all five conditions, and the check shows that line by line.
Fix them one at a time — each verdict line belongs to its own level of the track.

The honest report gives zero percent on overweight and two unstable cases. One of
the three overweight cases was in the prompt — exclude it and the kind is left
with one broken case and one unstable one. Every mistake there puts a loaded
tractor on a bridge that will not hold it.

## Done when

- an independent judge did the grading;
- all nine cases were checked for a leak;
- every case was run three times;
- the report names the weak kind with its share;
- the decision is that it cannot ship;
- no more than two calls to the model.

## Choose a difficulty

| Folder | What you get |
|---|---|
| `starter/novice/` | five `TODO`s naming the level each skill came from |
| `starter/advanced/` | the list of five conditions and a report breaking all of them |
| `starter/pro/` | the contract and the acceptance criteria |

## After this level

The Evaluation track is finished. You can measure a system in a way you can
trust: with a set rather than an example; by meaning rather than by characters;
with an independent judge against a rubric written in advance; on data the system
has not seen; over several runs; broken down by the cost of a mistake; and with a
paired metric that gets worse when the main one is over-tightened.

Next is the Red Team track: how to break what you built before somebody else
does.
