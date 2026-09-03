"use client";

import { useEffect, useState } from "react";
import type { Run } from "@/lib/content";
import Terminal from "./Terminal";

type Step = { title: string; note: string; kind: "code" | "run"; body: string; bad?: boolean };

type Props = {
  idea: string;
  starter: string;
  solution: string | null;
  demo: { novice?: Run; solution?: Run };
  solveHref: string;
};

/** Разбор строится из настоящих прогонов, снятых при сборке. Ничего не
    придумано: что показано, то движок и выдаёт. */
function buildSteps(p: Props): Step[] {
  const steps: Step[] = [
    {
      title: "Заготовка",
      note: "С этого кода начинают. Он рабочий и делает не то.",
      kind: "code",
      body: p.starter,
    },
  ];

  if (p.demo.novice) {
    steps.push({
      title: "Что она выдаёт",
      note: "Настоящий прогон заготовки — то же, что покажет вам проверка.",
      kind: "run",
      body: p.demo.novice.output,
      bad: p.demo.novice.code !== 0,
    });
  }

  if (p.solution) {
    steps.push({
      title: "Что меняется",
      note: "Решение целиком. Открывайте после своей попытки.",
      kind: "code",
      body: p.solution,
    });
  }

  if (p.demo.solution) {
    steps.push({
      title: "Итог",
      note: "Прогон решения. Все условия сходятся.",
      kind: "run",
      body: p.demo.solution.output,
      bad: p.demo.solution.code !== 0,
    });
  }

  return steps;
}

export default function Walkthrough(props: Props) {
  const steps = buildSteps(props);
  const [at, setAt] = useState(0);
  const [revealed, setRevealed] = useState(false);

  useEffect(() => {
    setRevealed(false);
  }, [at]);

  const step = steps[at];
  // Решение и его прогон прячем: иначе уровень проходится чтением.
  const secret = at >= 2;
  const show = !secret || revealed;

  return (
    <aside
      style={{
        position: "sticky",
        top: "4.2rem",
        display: "flex",
        flexDirection: "column",
        gap: "0.7rem",
      }}
    >
      <div style={{ display: "flex", alignItems: "baseline", gap: "0.5rem", flexWrap: "wrap" }}>
        <h2 style={{ margin: 0, fontSize: "1.05rem", fontWeight: 700, letterSpacing: "-0.015em" }}>
          Разбор
        </h2>
        <span className="chip">
          шаг {at + 1} из {steps.length}
        </span>
      </div>

      <div style={{ display: "flex", gap: "0.3rem" }}>
        {steps.map((s, i) => (
          <button
            key={s.title}
            onClick={() => setAt(i)}
            aria-label={s.title}
            style={{
              flex: 1,
              height: 4,
              padding: 0,
              border: "none",
              borderRadius: 2,
              cursor: "pointer",
              background: i <= at ? "var(--accent)" : "var(--line)",
            }}
          />
        ))}
      </div>

      <div>
        <strong style={{ fontSize: "0.95rem", fontWeight: 680 }}>{step.title}</strong>
        <p style={{ margin: "0.15rem 0 0", fontSize: "0.85rem", color: "var(--ink-2)" }}>
          {step.note}
        </p>
      </div>

      {show ? (
        step.kind === "run" ? (
          <Terminal title="проверка" output={step.body} />
        ) : (
          <pre
            className="card"
            style={{
              margin: 0,
              padding: "0.8rem 0.9rem",
              overflow: "auto",
              maxHeight: "26rem",
              fontFamily: "var(--mono)",
              fontSize: "0.74rem",
              fontWeight: 500,
              lineHeight: 1.6,
            }}
          >
            {step.body.trimEnd()}
          </pre>
        )
      ) : (
        <div
          className="card"
          style={{
            padding: "1.6rem 1rem",
            textAlign: "center",
            color: "var(--ink-2)",
            fontSize: "0.9rem",
          }}
        >
          <p style={{ margin: "0 0 0.8rem" }}>
            Дальше — решение. Сперва попробуйте сами: подсказки в теории хватает.
          </p>
          <button className="btn btn-small" onClick={() => setRevealed(true)}>
            Всё равно показать
          </button>
        </div>
      )}

      <div style={{ display: "flex", gap: "0.4rem", alignItems: "center" }}>
        <button
          className="btn btn-small btn-quiet"
          onClick={() => setAt((i) => Math.max(0, i - 1))}
          disabled={at === 0}
        >
          Назад
        </button>
        <button
          className="btn btn-small btn-quiet"
          onClick={() => setAt((i) => Math.min(steps.length - 1, i + 1))}
          disabled={at === steps.length - 1}
        >
          Дальше
        </button>
        <a className="btn btn-small btn-go" href={props.solveHref} style={{ marginLeft: "auto" }}>
          Решать →
        </a>
      </div>
    </aside>
  );
}
