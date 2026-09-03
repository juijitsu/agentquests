"use client";

import { useEffect, useRef } from "react";

const DOTS = ["#ff5f57", "#febc2e", "#28c840"];

type Props = {
  title?: string;
  output: string;
  live?: boolean;
  prompt?: string;
};

/** Окно терминала в духе macOS: три огня, заголовок, моноширинное тело.
    Цвета вердикта берутся из тех же ✓ и ✗, что печатает движок. */
export default function Terminal({ title = "agentquests", output, live, prompt }: Props) {
  const body = useRef<HTMLPreElement>(null);

  useEffect(() => {
    if (body.current) body.current.scrollTop = body.current.scrollHeight;
  }, [output]);

  return (
    <div className="term">
      <div className="term-bar">
        {DOTS.map((c) => (
          <span key={c} className="term-dot" style={{ background: c }} />
        ))}
        <span className="term-title">{title}</span>
      </div>
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
    </div>
  );
}
