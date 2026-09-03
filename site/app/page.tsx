import Link from "next/link";
import { tracks, allLevels } from "@/lib/content";

const PLANNED: Record<string, number> = {
  foundations: 8,
  "agent-core": 10,
  context: 8,
  retrieval: 9,
  evaluation: 8,
};

const TOTAL_PLANNED = 76;

export default function Home() {
  const list = tracks();
  const done = allLevels().length;
  const langs = [...new Set(allLevels().map((l) => l.lang))].filter((l) => l !== "—");

  return (
    <div style={{ maxWidth: "72rem", margin: "0 auto", padding: "clamp(2rem, 6vw, 4rem) clamp(1rem, 4vw, 2rem)" }}>
      <section style={{ maxWidth: "42rem" }}>
        <h1
          style={{
            fontSize: "clamp(1.8rem, 5vw, 2.6rem)",
            lineHeight: 1.1,
            letterSpacing: "-0.025em",
            margin: "0 0 0.8rem",
            textWrap: "balance",
          }}
        >
          Курс, который нельзя пройти чтением
        </h1>
        <p style={{ color: "var(--ink-2)", fontSize: "1.05rem", margin: "0 0 1.2rem" }}>
          Каждый уровень даёт теорию, затем метод, затем задание. Следующий
          открывается, когда проходят тесты, — а не когда вы дочитали.
        </p>

        <div
          style={{
            display: "flex",
            flexWrap: "wrap",
            gap: "0.4rem 1.4rem",
            fontFamily: "var(--mono)",
            fontSize: "0.76rem",
            color: "var(--ink-3)",
          }}
        >
          <span>готово уровней: {done} из {TOTAL_PLANNED}</span>
          <span>{langs.join(" · ")}</span>
          <span>без ключей и пакетов</span>
        </div>

        <pre
          style={{
            marginTop: "1.4rem",
            background: "var(--panel)",
            border: "1px solid var(--line)",
            borderRadius: 6,
            padding: "0.8rem 1rem",
            overflowX: "auto",
            fontFamily: "var(--mono)",
            fontSize: "0.78rem",
            color: "var(--ink-2)",
          }}
        >
          python engine/check.py content/ru/00-foundations/01-what-is-an-agent/starter/novice/agent.py
        </pre>
      </section>

      <section style={{ marginTop: "3.5rem", display: "flex", flexDirection: "column", gap: "2.5rem" }}>
        {list.map((track) => {
          const planned = PLANNED[track.slug] ?? track.levels.length;
          return (
            <div key={track.slug}>
              <div
                style={{
                  display: "flex",
                  alignItems: "baseline",
                  gap: "0.8rem",
                  borderBottom: "1px solid var(--line)",
                  paddingBottom: "0.5rem",
                  marginBottom: "0.9rem",
                }}
              >
                <h2 style={{ fontSize: "1.05rem", margin: 0, letterSpacing: "-0.01em" }}>
                  {track.title}
                </h2>
                <span
                  style={{
                    fontFamily: "var(--mono)",
                    fontSize: "0.72rem",
                    color: track.levels.length === planned ? "var(--ok)" : "var(--ink-3)",
                  }}
                >
                  {track.levels.length} из {planned}
                </span>
              </div>

              <div
                style={{
                  display: "grid",
                  gridTemplateColumns: "repeat(auto-fill, minmax(17rem, 1fr))",
                  gap: "0.6rem",
                }}
              >
                {track.levels.map((level) => (
                  <Link
                    key={level.slug}
                    href={`/${level.trackSlug}/${level.slug}/`}
                    style={{
                      display: "block",
                      border: "1px solid var(--line)",
                      borderRadius: 6,
                      padding: "0.7rem 0.85rem",
                      background: "var(--panel)",
                    }}
                  >
                    <div style={{ display: "flex", gap: "0.55rem", alignItems: "baseline" }}>
                      <span
                        style={{
                          fontFamily: "var(--mono)",
                          fontSize: "0.72rem",
                          color: "var(--ink-3)",
                        }}
                      >
                        {String(level.order).padStart(2, "0")}
                      </span>
                      <span style={{ fontWeight: 500, fontSize: "0.94rem" }}>{level.title}</span>
                      <span
                        style={{
                          marginLeft: "auto",
                          fontFamily: "var(--mono)",
                          fontSize: "0.65rem",
                          color: "var(--ink-3)",
                        }}
                      >
                        {level.lang}
                      </span>
                    </div>
                    <p
                      style={{
                        margin: "0.3rem 0 0",
                        fontSize: "0.83rem",
                        color: "var(--ink-2)",
                        lineHeight: 1.45,
                      }}
                    >
                      {level.idea}
                    </p>
                  </Link>
                ))}
              </div>
            </div>
          );
        })}
      </section>
    </div>
  );
}
