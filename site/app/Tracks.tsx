"use client";

import { useEffect, useState } from "react";

const DONE_KEY = "aq-done";

export type Card = {
  id: string;
  href: string;
  order: number;
  title: string;
  idea: string;
  lang: string;
};

export type Group = { slug: string; title: string; planned: number; levels: Card[] };

export default function Tracks({ groups }: { groups: Group[] }) {
  const [done, setDone] = useState<string[]>([]);

  useEffect(() => {
    try {
      const raw = localStorage.getItem(DONE_KEY);
      if (raw) setDone(JSON.parse(raw));
    } catch {
      /* приватный режим — прогресса просто не будет */
    }
  }, []);

  return (
    <section style={{ marginTop: "3.5rem", display: "flex", flexDirection: "column", gap: "2.6rem" }}>
      {groups.map((group) => {
        const passed = group.levels.filter((l) => done.includes(l.id)).length;
        const ready = group.levels.length === group.planned;
        return (
          <div key={group.slug}>
            <div
              style={{
                display: "flex",
                alignItems: "baseline",
                gap: "0.7rem",
                flexWrap: "wrap",
                borderBottom: "2px solid var(--line)",
                paddingBottom: "0.5rem",
                marginBottom: "1rem",
              }}
            >
              <h2 style={{ fontSize: "1.24rem", fontWeight: 800, margin: 0, letterSpacing: "-0.02em" }}>
                {group.title}
              </h2>
              <span className="chip" style={ready ? { color: "var(--ok)" } : undefined}>
                {group.levels.length}/{group.planned} написано
              </span>
              {passed > 0 ? (
                <span className="chip" style={{ background: "var(--ok-soft)", color: "var(--ok)" }}>
                  пройдено {passed}
                </span>
              ) : null}
            </div>

            <div
              style={{
                display: "grid",
                gridTemplateColumns: "repeat(auto-fill, minmax(17.5rem, 1fr))",
                gap: "0.8rem",
              }}
            >
              {group.levels.map((level) => {
                const ok = done.includes(level.id);
                return (
                  <a
                    key={level.id}
                    href={level.href}
                    className="card"
                    style={{
                      display: "block",
                      padding: "0.75rem 0.9rem",
                      borderColor: ok ? "var(--ok)" : "var(--line-strong)",
                      background: ok ? "var(--ok-soft)" : "var(--panel)",
                    }}
                  >
                    <div style={{ display: "flex", gap: "0.5rem", alignItems: "baseline" }}>
                      <span className="chip" style={ok ? { color: "var(--ok)" } : undefined}>
                        {String(level.order).padStart(2, "0")}
                      </span>
                      <span style={{ fontWeight: 700, fontSize: "0.96rem" }}>{level.title}</span>
                      <span
                        className="chip"
                        style={{ marginLeft: "auto", background: "transparent" }}
                      >
                        {ok ? "✓" : level.lang}
                      </span>
                    </div>
                    <p
                      style={{
                        margin: "0.3rem 0 0",
                        fontSize: "0.86rem",
                        color: "var(--ink-2)",
                        lineHeight: 1.45,
                      }}
                    >
                      {level.idea}
                    </p>
                  </a>
                );
              })}
            </div>
          </div>
        );
      })}
    </section>
  );
}
