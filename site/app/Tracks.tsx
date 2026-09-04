"use client";

import { useSyncExternalStore } from "react";
import {
  levelOpen,
  noMarks,
  readMarks,
  watchMarks,
  whenText,
  type Outline,
} from "./progress";
import { dictFor, type Lang } from "@/lib/i18n";

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
  lang,
}: {
  groups: Group[];
  outline: Outline;
  lang: Lang;
}) {
  const dict = dictFor(lang);
  /* Прогресс читается подпиской, а не эффектом: на сервере его нет, и
     установка состояния из эффекта тянула бы лишний рендер. Объект между
     записями один и тот же, поэтому подписка не зацикливается. */
  const marks = useSyncExternalStore(watchMarks, readMarks, noMarks);
  const progress = Object.keys(marks).filter((id) => marks[id].done);
  // На сервере записей нет, и до гидратации считаем всё открытым: замки,
  // мигающие на каждой загрузке, раздражают сильнее, чем доля секунды без них.
  const known = marks !== noMarks();

  return (
    <section style={{ marginTop: "3rem", display: "flex", flexDirection: "column", gap: "2.4rem" }}>
      {groups.map((group) => {
        const passed = group.levels.filter((l) => progress.includes(l.id)).length;

        return (
          <div key={group.slug}>
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
                  {dict.passed(passed)}
                </span>
              ) : (
                <span style={{ fontSize: "0.82rem", color: "var(--ink-3)" }}>
                  {dict.firstOpen}
                </span>
              )}
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
                    {/* Отметка — только у тронутых уровней. У остальных карточка
                        выглядит ровно как раньше. */}
                    {(() => {
                      const mark = marks[level.id];
                      if (!mark) return null;
                      const when = mark.at ? whenText(mark.at, lang) : null;
                      return (
                        <p
                          style={{
                            margin: "0.3rem 0 0",
                            fontSize: "0.78rem",
                            color: mark.done ? "var(--ok)" : "var(--ink-3)",
                          }}
                        >
                          {mark.done
                            ? dict.markPassed(when, mark.runs)
                            : dict.markStuck(when ?? "", mark.runs)}
                        </p>
                      );
                    })()}
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
