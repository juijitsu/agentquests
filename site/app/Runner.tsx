"use client";

import { useCallback, useEffect, useRef, useState } from "react";
import type { Solution, Tier } from "@/lib/content";
import { saveDone } from "./progress";
import Editor from "./Editor";
import Terminal, { TermWindow } from "./Terminal";
import Star, { type Hint } from "./Star";
import { dictFor, type Dict, type Lang } from "@/lib/i18n";
import { explainSyntax, type Problem } from "@/lib/hints";

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
  const seq = useRef(0);
  const [problem, setProblem] = useState<Problem | null>(null);
  const [touched, setTouched] = useState(false);

  useEffect(() => () => worker.current?.terminate(), []);

  function reset(next: Tier, source?: string) {
    setTier(next);
    setCode(source ?? starters[next]?.code ?? "");
    setOutput("");
    setVerdict(null);
    setProblem(null);
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

  /* Воркер один на страницу и живёт между прогонами: в нём же разбирается
     код для живых подсказок. Второй Pyodide рядом — это ещё двенадцать
     мегабайт и вторая копия интерпретатора в памяти.

     Долгая жизнь интерпретатора здесь предусмотрена: загрузчик воркера
     кладёт каждый прогон в свежий каталог и чистит имена модулей, иначе
     второй запуск получил бы код первого. Снимаем воркер только по кнопке
     «Прервать», по сбою и при уходе со страницы. */
  const ensureWorker = useCallback(() => {
    if (worker.current) return worker.current;
    const base = process.env.NEXT_PUBLIC_BASE_PATH ?? "";
    const w = new Worker(`${base}/runner.js`, { type: "module" });

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
      const data = event.data as {
        type: string;
        text?: string;
        code?: number;
        seq?: number;
        name?: string;
        message?: string;
        line?: number;
        column?: number;
      };

      if (data.type === "check") {
        // Ответ на устаревший запрос: код с тех пор успели поправить.
        if (data.seq !== seq.current) return;
        const said = explainSyntax(data.name ?? "", data.message ?? "", dict);
        setProblem(
          said ? { line: data.line ?? 1, column: data.column ?? 1, message: said } : null,
        );
        return;
      }

      if (data.type === "stage") {
        setStage(data.text ?? "");
        return;
      }

      setStage("");
      setState("done");
      setOutput(data.text ?? "");
      setVerdict(data.code ?? 1);
      if (data.code === 0) saveDone(levelId);
    };

    worker.current = w;
    return w;
  }, [dict, levelId]);

  const run = useCallback(() => {
    const w = ensureWorker();

    setState("busy");
    setOutput("");
    setVerdict(null);
    setHintOpen(false);
    setStage(dict.preparing);

    const name = starters[tier]?.file ?? "agent.py";
    w.postMessage({
      kit: engine.kit,
      check: engine.check,
      scenario,
      agent: code,
      agentName: name,
      where: `${name} · ${tier}`,
    });
  }, [code, dict, engine, ensureWorker, scenario, starters, tier]);

  /* Разбор по паузе в наборе. Пока не тронули код — не разбираем и воркер
     не поднимаем: тот, кто просто читает страницу, не должен платить
     двенадцатью мегабайтами. Во время прогона молчим, чтобы не мешать. */
  useEffect(() => {
    if (!touched || state === "busy") return;
    // Разобрать без запуска умеет только питон. У прочих языков подсказки
    // нет, и ставить её нечем: reset уже чистит её при смене сложности.
    if (!(starters[tier]?.file ?? "agent.py").endsWith(".py")) return;
    const timer = setTimeout(() => {
      seq.current += 1;
      ensureWorker().postMessage({ kind: "check", seq: seq.current, source: code });
    }, 450);
    return () => clearTimeout(timer);
  }, [code, touched, state, tier, starters, ensureWorker]);

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
        <Editor
          value={code}
          file={starters[tier]?.file ?? "agent.py"}
          problem={problem}
          onChange={(next) => {
            setCode(next);
            setTouched(true);
          }}
          onRun={() => {
            if (!busy) run();
          }}
        />
      </TermWindow>

      {/* Метка на поле редактора крохотная, а текст к ней показывается только
          по наведению — новичок его не найдёт. Поэтому подсказка стоит ещё и
          строкой под окном, где её видно без действий. */}
      {problem ? (
        <p
          style={{
            margin: "-0.5rem 0 0",
            fontSize: "0.86rem",
            color: "var(--no)",
            display: "flex",
            gap: "0.5rem",
            alignItems: "baseline",
            flexWrap: "wrap",
          }}
        >
          <span className="chip">{dict.liveAt(problem.line)}</span>
          <span>{problem.message}</span>
        </p>
      ) : null}

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
