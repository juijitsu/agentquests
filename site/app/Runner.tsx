"use client";

import { useCallback, useEffect, useRef, useState } from "react";
import type { Solution, Tier } from "@/lib/content";
import { saveDone } from "./progress";
import Terminal, { TermWindow } from "./Terminal";
import Star, { type Hint } from "./Star";

const TIER_TITLES: Record<Tier, string> = {
  novice: "Новичок",
  advanced: "Продвинутый",
  pro: "Профессионал",
};

const TIER_NOTES: Record<Tier, string> = {
  novice: "место правки помечено TODO",
  advanced: "тот же код без указания, где править",
  pro: "только контракт, решение с нуля",
};

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
    hints.push({
      title: "с чего начать",
      body: "Проверка ещё не запускалась. Запустите заготовку как есть — она назовёт условия, которые не сошлись. Это быстрее, чем вычитывать код глазами.",
    });
  } else if (verdict === 0) {
    hints.push({
      title: "всё сошлось",
      body: "Условия выполнены, уровень засчитан. Следующий уже открыт — ссылка в зелёной полосе.",
    });
  } else if (failed.length > 0) {
    hints.push({
      title: failed.length === 1 ? "не сошлось условие" : "не сошлись условия",
      body: failed.join("\n"),
    });
  } else {
    hints.push({
      title: "прогон не дошёл до проверки",
      body: "Условия даже не считались. Смотрите вывод целиком: там сказано, на чём всё оборвалось.",
    });
  }

  if (said) hints.push({ title: "что говорит движок", body: said.replace(/^FAIL\s*/, "") });
  if (levelHint) hints.push({ title: "подсказка уровня", body: levelHint, html: true });

  if (verdict !== 0) {
    hints.push({
      title: "куда ещё посмотреть",
      body:
        (tier !== "novice" && hasNovice
          ? "Сложность «Новичок» показывает место правки: нужная строка помечена TODO. "
          : "") + "В разборе рядом с уроком второй шаг показывает, что выдаёт заготовка, третий — решение целиком.",
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
    setOutput("^C  прогон прерван вручную");
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
    setStage("готовлю прогон");

    // Без этого сбой воркера не виден вовсе: он не всплывает в консоль страницы.
    w.onerror = (event) => {
      setStage("");
      setState("done");
      setVerdict(2);
      setOutput(`воркер не запустился: ${event.message ?? "неизвестная ошибка"}`);
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
  }, [code, engine, levelId, scenario, starters, tier]);

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
            {TIER_TITLES[t]}
          </button>
        ))}
        <span style={{ fontSize: "0.82rem", color: "var(--ink-3)" }}>{TIER_NOTES[tier]}</span>
      </div>

      <TermWindow title={`${starters[tier]?.file ?? "agent.py"} — правьте здесь`}>
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
          rows={Math.min(30, Math.max(14, code.split("\n").length + 1))}
        />
      </TermWindow>

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
      </div>

      <Terminal
        title={`agentquests — ${starters[tier]?.file ?? "agent.py"}`}
        prompt={busy || output ? `$ ${command}\n` : ""}
        output={output || (busy ? stage : "Нажмите «Запустить» — вывод появится здесь.")}
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
            {passed ? "Уровень пройден" : "Пока не сходится"}
          </strong>
          <span style={{ fontSize: "0.88rem", color: "var(--ink-2)" }}>
            {passed
              ? "Следующий уровень открыт."
              : "Каждая строка с ✗ называет своё условие."}
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
              {hintOpen ? "Убрать подсказки" : "Спросить звезду"}
            </button>
          ) : null}
        </div>
      ) : null}

      {/* Подсказки живут в одном месте — у звезды. Кнопка выше только
          открывает её облачко, второй панели с подсказкой на странице нет. */}
      <Star
        hints={hintsFrom(output, verdict, tier, !!starters.novice, hintHtml)}
        mood={busy ? "think" : passed ? "cheer" : verdict === null ? "idle" : "sad"}
        open={hintOpen}
        onOpenChange={setHintOpen}
        heading={passed ? "Готово!" : "Чем помочь?"}
      />
    </div>
  );
}
