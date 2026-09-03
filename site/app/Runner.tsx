"use client";

import { useCallback, useEffect, useRef, useState } from "react";
import type { Solution, Tier } from "@/lib/content";
import { saveDone } from "./progress";
import Terminal, { TermWindow } from "./Terminal";
import Star, { type Hint } from "./Star";
import { dictFor, type Dict, type Lang } from "@/lib/i18n";

type Props = {
  levelId: string;
  command: string;
  engine: { kit: string; check: string };
  scenario: string;
  starters: Partial<Record<Tier, Solution>>;
  solution: Solution | null;
  hintHtml: string;
  nextHref: string | null;
  nextTitle: string | null;
  lang: Lang;
};

type State = "idle" | "busy" | "done";

/** Что звезда знает про положение дел. Всё берётся из настоящего вывода
    проверки: строки с ✗ — это условия, которые не сошлись, а строка FAIL
    несёт объяснение самого движка. Ничего не сочиняется. */
function hintsFrom(
  output: string,
  verdict: number | null,
  tier: Tier,
  hasNovice: boolean,
  levelHint: string,
  dict: Dict,
): Hint[] {
  const lines = output.split("\n").map((l) => l.trim());
  const failed = lines.filter((l) => l.startsWith("✗")).map((l) => l.slice(1).trim());

  // Объяснение движка занимает несколько строк: заголовок FAIL и перенос
  // фразы под ним. Взять одну строку — значит оборвать её на полуслове.
  const at = lines.findIndex((l) => l.startsWith("FAIL"));
  let said = "";
  if (at >= 0) {
    const block = [lines[at].replace(/^FAIL\s*/, "")];
    for (let i = at + 1; i < lines.length && lines[i]; i++) block.push(lines[i]);
    said = block.join(" ").trim();
  }

  const hints: Hint[] = [];

  if (verdict === null) {
    hints.push({ title: dict.hStartTitle, body: dict.hStartBody });
  } else if (verdict === 0) {
    hints.push({ title: dict.hDoneTitle, body: dict.hDoneBody });
  } else if (failed.length > 0) {
    hints.push({
      title: failed.length === 1 ? dict.hOneFailed : dict.hManyFailed,
      body: failed.join("\n"),
    });
  } else {
    hints.push({ title: dict.hNoChecksTitle, body: dict.hNoChecksBody });
  }

  if (said) hints.push({ title: dict.hEngineTitle, body: said });
  if (levelHint) hints.push({ title: dict.hLevelTitle, body: levelHint, html: true });

  if (verdict !== 0) {
    hints.push({
      title: dict.hWhereTitle,
      body: (tier !== "novice" && hasNovice ? dict.hWhereNovice : "") + dict.hWhereBody,
    });
  }

  return hints;
}

export default function Runner({
  levelId,
  command,
  engine,
  scenario,
  starters,
  solution,
  hintHtml,
  nextHref,
  nextTitle,
  lang,
}: Props) {
  const dict = dictFor(lang);
  const tiers = (Object.keys(starters) as Tier[]).filter((t) => starters[t]);
  const first = tiers[0] ?? "novice";
  const [tier, setTier] = useState<Tier>(first);
  const [code, setCode] = useState(starters[first]?.code ?? "");
  const [state, setState] = useState<State>("idle");
  const [stage, setStage] = useState("");
  const [output, setOutput] = useState("");
  const [verdict, setVerdict] = useState<number | null>(null);
  const [hintOpen, setHintOpen] = useState(false);
  const worker = useRef<Worker | null>(null);

  useEffect(() => () => worker.current?.terminate(), []);

  function reset(next: Tier, source?: string) {
    setTier(next);
    setCode(source ?? starters[next]?.code ?? "");
    setOutput("");
    setVerdict(null);
    setHintOpen(false);
    setState("idle");
  }

  function stop() {
    worker.current?.terminate();
    worker.current = null;
    setState("done");
    setStage("");
    setVerdict(2);
    setOutput(dict.interrupted);
  }

  const run = useCallback(() => {
    // Каждый прогон — свой воркер: так его можно снять, если решение зациклится.
    worker.current?.terminate();
    const base = process.env.NEXT_PUBLIC_BASE_PATH ?? "";
    const w = new Worker(`${base}/runner.js`, { type: "module" });
    worker.current = w;

    setState("busy");
    setOutput("");
    setVerdict(null);
    setHintOpen(false);
    setStage(dict.preparing);

    // Без этого сбой воркера не виден вовсе: он не всплывает в консоль страницы.
    w.onerror = (event) => {
      setStage("");
      setState("done");
      setVerdict(2);
      setOutput(dict.workerFailed(event.message ?? dict.unknownError));
      w.terminate();
      worker.current = null;
    };

    w.onmessage = (event) => {
      const data = event.data as { type: string; text: string; code?: number };
      if (data.type === "stage") {
        setStage(data.text);
        return;
      }
      setStage("");
      setState("done");
      setOutput(data.text);
      setVerdict(data.code ?? 1);
      if (data.code === 0) saveDone(levelId);
      w.terminate();
      worker.current = null;
    };

    const name = starters[tier]?.file ?? "agent.py";
    w.postMessage({
      kit: engine.kit,
      check: engine.check,
      scenario,
      agent: code,
      agentName: name,
      where: `${name} · ${tier}`,
    });
  }, [code, dict, engine, levelId, scenario, starters, tier]);

  const busy = state === "busy";
  const passed = verdict === 0;

  return (
    <div style={{ display: "flex", flexDirection: "column", gap: "1rem" }}>
      <div style={{ display: "flex", gap: "0.4rem", flexWrap: "wrap", alignItems: "center" }}>
        {tiers.map((t) => (
          <button
            key={t}
            className="btn btn-small"
            onClick={() => reset(t)}
            disabled={busy}
            style={
              t === tier
                ? { background: "var(--accent-soft)", borderColor: "var(--accent)" }
                : { color: "var(--ink-2)" }
            }
          >
            {dict.tierTitles[t]}
          </button>
        ))}
        <span style={{ fontSize: "0.82rem", color: "var(--ink-3)" }}>{dict.tierNotes[tier]}</span>
      </div>

      <TermWindow title={dict.editorTitle(starters[tier]?.file ?? "agent.py")}>
        <textarea
          className="term-edit"
          value={code}
          onChange={(e) => setCode(e.target.value)}
          onKeyDown={(e) => {
            if ((e.metaKey || e.ctrlKey) && e.key === "Enter") {
              e.preventDefault();
              if (!busy) run();
            }
          }}
          spellCheck={false}
          rows={Math.min(22, Math.max(12, code.split("\n").length + 1))}
        />
      </TermWindow>

      <div style={{ display: "flex", gap: "0.5rem", alignItems: "center", flexWrap: "wrap" }}>
        <button className="btn btn-go" onClick={run} disabled={busy}>
          {dict.run}
        </button>
        <span className="chip">Ctrl ⏎</span>
        {busy ? (
          <button className="btn btn-quiet" onClick={stop}>
            {dict.stop}
          </button>
        ) : null}
        <button className="btn btn-quiet" onClick={() => reset(tier)} disabled={busy}>
          {dict.resetStarter}
        </button>
        {solution ? (
          <button
            className="btn btn-quiet"
            onClick={() => reset(tier, solution.code)}
            disabled={busy}
          >
            {dict.fillSolution}
          </button>
        ) : null}
      </div>

      <Terminal
        title={`agentquests — ${starters[tier]?.file ?? "agent.py"}`}
        prompt={busy || output ? `$ ${command}\n` : ""}
        output={output || (busy ? stage : dict.idleOutput)}
        live={busy}
      />

      {verdict !== null ? (
        <div
          className="card"
          style={{
            padding: "0.75rem 1rem",
            display: "flex",
            gap: "0.7rem",
            alignItems: "center",
            flexWrap: "wrap",
            background: passed ? "var(--ok-soft)" : "var(--no-soft)",
            borderColor: passed ? "var(--ok)" : "var(--no)",
          }}
        >
          <strong
            style={{ fontSize: "1rem", fontWeight: 750, color: passed ? "var(--ok)" : "var(--no)" }}
          >
            {passed ? dict.passedTitle : dict.failedTitle}
          </strong>
          <span style={{ fontSize: "0.88rem", color: "var(--ink-2)" }}>
            {passed ? dict.passedNote : dict.failedNote}
          </span>
          {passed && nextHref ? (
            <a className="btn btn-small btn-go" href={nextHref} style={{ marginLeft: "auto" }}>
              {nextTitle} →
            </a>
          ) : null}
          {!passed ? (
            <button
              className="btn btn-small"
              style={{ marginLeft: "auto" }}
              onClick={() => setHintOpen((was) => !was)}
            >
              {hintOpen ? dict.hideHints : dict.askStar}
            </button>
          ) : null}
        </div>
      ) : null}

      {/* Подсказки живут в одном месте — у звезды. Кнопка выше только
          открывает её облачко, второй панели с подсказкой на странице нет. */}
      <Star
        hints={hintsFrom(output, verdict, tier, !!starters.novice, hintHtml, dict)}
        mood={busy ? "think" : passed ? "cheer" : verdict === null ? "idle" : "sad"}
        open={hintOpen}
        onOpenChange={setHintOpen}
        heading={passed ? dict.starHeadingDone : dict.starHeading}
        lang={lang}
      />
    </div>
  );
}
