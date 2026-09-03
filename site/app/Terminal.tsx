"use client";

import { useEffect, useRef, type ReactNode } from "react";

const DOTS = ["#ff5f57", "#febc2e", "#28c840"];

/** Рама окна в духе macOS. Одна на весь сайт: вывод проверки, код разбора и
    редактор на странице решения — это одно и то же окно с разным содержимым. */
export function TermWindow({ title, children }: { title: string; children: ReactNode }) {
  return (
    <div className="term">
      <div className="term-bar">
        {DOTS.map((colour) => (
          <span key={colour} className="term-dot" style={{ background: colour }} />
        ))}
        <span className="term-title">{title}</span>
      </div>
      {children}
    </div>
  );
}

type Props = {
  title?: string;
  output: string;
  live?: boolean;
  prompt?: string;
};

/** Тело окна. Цвета вердикта берутся из тех же ✓ и ✗, что печатает движок. */
export default function Terminal({ title = "agentquests", output, live, prompt }: Props) {
  const body = useRef<HTMLPreElement>(null);

  useEffect(() => {
    if (body.current) body.current.scrollTop = body.current.scrollHeight;
  }, [output]);

  return (
    <TermWindow title={title}>
      <pre ref={body} className="term-body">
        {prompt ? (
          <span style={{ color: "var(--accent)", fontWeight: 650 }}>{prompt}</span>
        ) : null}
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
              style={{ display: "block", color: colour, fontWeight: colour ? 620 : 500 }}
            >
              {line || " "}
            </span>
          );
        })}
        {live ? <span className="caret" /> : null}
      </pre>
    </TermWindow>
  );
}
