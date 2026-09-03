"use client";

import { useCallback, useEffect, useRef, useState } from "react";
import type { Solution, Tier } from "@/lib/content";

const TIER_TITLES: Record<Tier, string> = {
  novice: "Новичок",
  advanced: "Продвинутый",
  pro: "Профессионал",
};

const DONE_KEY = "aq-done";

type Props = {
  levelId: string;
  engine: { kit: string; check: string };
  scenario: string;
  starters: Partial<Record<Tier, Solution>>;
  solution: Solution | null;
  hintHtml: string;
};

type State = "idle" | "busy" | "done";

function remember(levelId: string) {
  try {
    const raw = localStorage.getItem(DONE_KEY);
    const done: string[] = raw ? JSON.parse(raw) : [];
    if (!done.includes(levelId)) {
      localStorage.setItem(DONE_KEY, JSON.stringify([...done, levelId]));
    }
  } catch {
    /* приватный режим — прогресс просто не сохранится */
  }
}

export default function Runner({
  levelId,
  engine,
  scenario,
  starters,
  solution,
  hintHtml,
}: Props) {
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
    setOutput("Прогон прерван вручную.");
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
    setStage("Готовлю прогон…");

    // Без этого сбой воркера не виден вовсе: он не всплывает в консоль страницы.
    w.onerror = (event) => {
      setStage("");
      setState("done");
      setVerdict(2);
      setOutput(`Воркер не запустился: ${event.message ?? "неизвестная ошибка"}`);
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
      if (data.code === 0) remember(levelId);
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
  }, [code, engine, levelId, scenario, starters, tier]);

  const busy = state === "busy";

  return (
    <section
      id="run"
      style={{ marginTop: "3rem", display: "flex", flexDirection: "column", gap: "0.9rem" }}
    >
      <h2 style={{ fontSize: "1.3rem", fontWeight: 750, margin: 0, letterSpacing: "-0.015em" }}>
        Проверить решение
      </h2>
      <p style={{ margin: 0, color: "var(--ink-2)", fontSize: "0.92rem", maxWidth: "38rem" }}>
        Правьте код и запускайте — проверка та же, что в командной строке.
        Python подгружается по первому запуску; пока вы читаете, он не тратится.
      </p>

      <div style={{ display: "flex", gap: "0.4rem", flexWrap: "wrap" }}>
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
            {TIER_TITLES[t]}
          </button>
        ))}
      </div>

      <textarea
        value={code}
        onChange={(e) => setCode(e.target.value)}
        onKeyDown={(e) => {
          if ((e.metaKey || e.ctrlKey) && e.key === "Enter") {
            e.preventDefault();
            if (!busy) run();
          }
        }}
        spellCheck={false}
        rows={Math.min(28, Math.max(12, code.split("\n").length + 1))}
        style={{
          width: "100%",
          background: "var(--panel)",
          color: "var(--ink)",
          border: "2px solid var(--line-strong)",
          borderRadius: 10,
          padding: "0.85rem 1rem",
          fontFamily: "var(--mono)",
          fontSize: "0.8rem",
          fontWeight: 500,
          lineHeight: 1.6,
          resize: "vertical",
          boxShadow: "4px 4px 0 var(--shadow)",
        }}
      />

      <div style={{ display: "flex", gap: "0.5rem", alignItems: "center", flexWrap: "wrap" }}>
        <button className="btn btn-go" onClick={run} disabled={busy}>
          Запустить
        </button>
        <span className="chip">Ctrl ⏎</span>

        {busy ? (
          <button className="btn btn-quiet" onClick={stop}>
            Прервать
          </button>
        ) : null}

        <button className="btn btn-quiet" onClick={() => reset(tier)} disabled={busy}>
          Вернуть заготовку
        </button>

        {solution ? (
          <button
            className="btn btn-quiet"
            onClick={() => reset(tier, solution.code)}
            disabled={busy}
          >
            Подставить эталон
          </button>
        ) : null}

        {stage ? (
          <span style={{ fontSize: "0.86rem", fontWeight: 600, color: "var(--ink-3)" }}>
            {stage}
          </span>
        ) : null}
      </div>

      {verdict !== null ? (
        <div
          className="card"
          style={{
            padding: "0.7rem 1rem",
            display: "flex",
            gap: "0.7rem",
            alignItems: "center",
            flexWrap: "wrap",
            background: verdict === 0 ? "var(--ok-soft)" : "var(--no-soft)",
            borderColor: verdict === 0 ? "var(--ok)" : "var(--no)",
          }}
        >
          <strong
            style={{
              fontSize: "1rem",
              fontWeight: 800,
              color: verdict === 0 ? "var(--ok)" : "var(--no)",
            }}
          >
            {verdict === 0 ? "Уровень пройден" : "Пока не сходится"}
          </strong>
          <span style={{ fontSize: "0.88rem", color: "var(--ink-2)" }}>
            {verdict === 0
              ? "Все условия выполнены — можно идти дальше."
              : "Смотрите строки с ✗ ниже: каждая называет своё условие."}
          </span>
          {verdict !== 0 && hintHtml ? (
            <button
              className="btn btn-small"
              style={{ marginLeft: "auto" }}
              onClick={() => setHintOpen((was) => !was)}
            >
              {hintOpen ? "Скрыть подсказку" : "Подсказка"}
            </button>
          ) : null}
        </div>
      ) : null}

      {hintOpen && hintHtml ? (
        <div
          className="prose card"
          style={{ padding: "0.9rem 1.1rem", maxWidth: "none" }}
          dangerouslySetInnerHTML={{ __html: hintHtml }}
        />
      ) : null}

      {output ? (
        <pre
          className="card"
          style={{
            margin: 0,
            padding: "0.9rem 1rem",
            overflowX: "auto",
            whiteSpace: "pre-wrap",
            fontFamily: "var(--mono)",
            fontSize: "0.8rem",
            fontWeight: 500,
            lineHeight: 1.6,
          }}
        >
          {output.split("\n").map((line, i) => {
            const mark = line.trimStart()[0];
            const colour =
              mark === "✓" || line.includes("PASS")
                ? "var(--ok)"
                : mark === "✗" || line.includes("FAIL")
                  ? "var(--no)"
                  : undefined;
            return (
              <span
                key={i}
                style={{ color: colour, display: "block", fontWeight: colour ? 600 : 500 }}
              >
                {line || " "}
              </span>
            );
          })}
        </pre>
      ) : null}
    </section>
  );
}
