"use client";

import { useEffect, useState } from "react";
import { levelOpen, readDone, trackOpen, type Outline } from "./progress";

export type Card = {
  id: string;
  href: string;
  order: number;
  title: string;
  idea: string;
  lang: string;
};

export type Group = { slug: string; title: string; planned: number; levels: Card[] };

export default function Tracks({
  groups,
  outline,
}: {
  groups: Group[];
  outline: Outline;
}) {
  const [done, setDone] = useState<string[] | null>(null);

  useEffect(() => setDone(readDone()), []);

  // Пока прогресс не прочитан, считаем всё открытым: замки, мигающие
  // на каждой загрузке, раздражают сильнее, чем доля секунды без них.
  const progress = done ?? [];
  const known = done !== null;

  return (
    <section style={{ marginTop: "3rem", display: "flex", flexDirection: "column", gap: "2.4rem" }}>
      {groups.map((group, at) => {
        const passed = group.levels.filter((l) => progress.includes(l.id)).length;
        const openTrack = !known || trackOpen(outline, at, progress);
        const previous = groups[at - 1];

        return (
          <div key={group.slug} style={{ opacity: openTrack ? 1 : 0.62 }}>
            <div
              style={{
                display: "flex",
                alignItems: "baseline",
                gap: "0.6rem",
                flexWrap: "wrap",
                borderBottom: "1px solid var(--line)",
                paddingBottom: "0.5rem",
                marginBottom: "0.9rem",
              }}
            >
              <h2
                style={{
                  fontSize: "1.18rem",
                  fontWeight: 750,
                  margin: 0,
                  letterSpacing: "-0.02em",
                }}
              >
                {group.title}
              </h2>
              <span className="chip">
                {group.levels.length}/{group.planned}
              </span>
              {passed > 0 ? (
                <span className="chip" style={{ background: "var(--ok-soft)", color: "var(--ok)" }}>
                  пройдено {passed}
                </span>
              ) : null}
              {!openTrack ? (
                <span style={{ fontSize: "0.82rem", color: "var(--ink-3)" }}>
                  🔒 откроется, когда пройден трек «{previous?.title}»
                </span>
              ) : null}
            </div>

            <div
              style={{
                display: "grid",
                gridTemplateColumns: "repeat(auto-fill, minmax(17.5rem, 1fr))",
                gap: "0.7rem",
              }}
            >
              {group.levels.map((level) => {
                const ok = progress.includes(level.id);
                const open = !known || levelOpen(outline, level.id, progress);
                const Tag = open ? "a" : "div";
                return (
                  <Tag
                    key={level.id}
                    {...(open ? { href: level.href } : {})}
                    className="card"
                    style={{
                      display: "block",
                      padding: "0.7rem 0.85rem",
                      cursor: open ? "pointer" : "default",
                      opacity: open ? 1 : 0.55,
                      borderColor: ok ? "var(--ok)" : "var(--line)",
                      background: ok ? "var(--ok-soft)" : "var(--panel)",
                    }}
                  >
                    <div style={{ display: "flex", gap: "0.5rem", alignItems: "baseline" }}>
                      <span className="chip" style={ok ? { color: "var(--ok)" } : undefined}>
                        {String(level.order).padStart(2, "0")}
                      </span>
                      <span style={{ fontWeight: 680, fontSize: "0.95rem" }}>{level.title}</span>
                      <span
                        className="chip"
                        style={{ marginLeft: "auto", background: "transparent" }}
                      >
                        {ok ? "✓" : open ? level.lang : "🔒"}
                      </span>
                    </div>
                    <p
                      style={{
                        margin: "0.28rem 0 0",
                        fontSize: "0.85rem",
                        color: "var(--ink-2)",
                        lineHeight: 1.45,
                      }}
                    >
                      {level.idea}
                    </p>
                  </Tag>
                );
              })}
            </div>
          </div>
        );
      })}
    </section>
  );
}
