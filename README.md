# agentquests

**Learn AI engineering by shipping.** Eight career tracks, every level verified by tests — you can't skip by reading.

> **Status: early.** Four tracks are complete — Foundations (8 levels), Agent core (10), Context (8) and Retrieval (9) — plus five Evaluation levels: 40 playable end to end. The other 36 are specified but not written yet.

```bash
python engine/check.py content/ru/00-foundations/01-what-is-an-agent/starter/novice/agent.py
```

No API key, no packages to install, no network — levels run on recorded model behaviour.

Each level is written in the language the job is actually done in: Python for agent loops, TypeScript where data shape is the point, SQL where the question belongs to the store. One command runs them all — the runner picks the right one. TypeScript levels need Node 24, which strips types with no build step.

No Python on this machine? Open the repo in a ready-made environment instead — same version the tests run on:

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/juijitsu/agentquests)

---

## What this is

Not another course you read. Each level hands you theory, then the method, then a task — and the next level unlocks only when the tests pass.

- **Theory → method → task.** Most courses skip the middle step, which is where people get lost: they understood the idea but were never shown the procedure.
- **Runs offline.** Levels ship with recorded model responses, so you can start without an API key and the checks are deterministic.
- **Locked progression.** Passing is the proof. Reading ahead does not move you forward.
- **Three difficulties.** Same theory and method for everyone; only the amount of scaffolding in the task changes.

## Tracks

| # | Track | Role it prepares you for | Levels |
|---|-------|--------------------------|--------|
| 00 | Foundations | required before any track | 8 |
| 01 | Agent core | Agent Engineer | 10 |
| 02 | Context | Context Engineer | 8 |
| 03 | Retrieval | RAG / Search Engineer | 9 |
| 04 | Evaluation | AI Evaluation Engineer | 8 |
| 05 | Red team | AI Red Teamer | 8 |
| 06 | Guardrails | AI Security Engineer | 8 |
| 07 | Operations | AI Platform Engineer | 9 |
| 08 | Data | AI Data Engineer | 8 |

All eight tracks run in one world: a US freight company moving cargo from the Texas border to the East Coast. The agent you build in track 01 is the one you attack in track 05.

## Roadmap

- [x] Level engine and check runner
- [x] Foundations track
- [ ] Agent core track
- [ ] Public launch
- [ ] Remaining tracks
- [ ] English, Russian and Arabic

## Contributing

Not open for contributions yet — the level format is still moving. Once the first track ships, there will be a level template, CI that validates submissions, and `good first level` issues.

## License

MIT
