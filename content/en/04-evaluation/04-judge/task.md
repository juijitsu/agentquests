# Evaluation · Six of six

The agent ran the set and graded itself: six of six.

Two of those six answers:

```
expected: 18:00   answer: sometime in the evening
expected: 2.90    answer: around three dollars
```

```
python engine/check.py content/en/04-evaluation/04-judge/starter/novice/agent.py
```

Look at the first check line: the author did the judging. It did not cheat — it
knows what it meant to say, and behind "sometime in the evening" it sees the very
eighteen hundred hours it had in mind.

A judge who did not write the answer sees only the text. And the text does not
answer the question "at what time".

**Hand the grading to whoever did not write the answer, and give them a rule.**

## Done when

- an independent judge did the grading, not the author;
- all six cases were judged;
- the score is four of six;
- no more than two calls to the model.

## Choose a difficulty

| Folder | What you get |
|---|---|
| `starter/novice/` | grading by the author, with the call you need named in the `TODO` |
| `starter/advanced/` | only a note that everything follows the earlier lessons |
| `starter/pro/` | the contract and both judges |

## If you get stuck

The rubric comes first for a reason: it sets what "correct" means, and it has to
exist before anyone looked at the answers.
