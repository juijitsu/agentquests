import Link from "next/link";
import { marked } from "marked";
import { allLevels, engineSources, findLevel, type Solution } from "@/lib/content";
import Runner from "../../Runner";

export function generateStaticParams() {
  return allLevels().map((l) => ({ track: l.trackSlug, level: l.slug }));
}

const TIER_TITLES: Record<string, string> = {
  novice: "Новичок",
  advanced: "Продвинутый",
  pro: "Профессионал",
};

function html(md: string) {
  return { __html: marked.parse(md, { async: false }) as string };
}

function Code({ title, note, item }: { title: string; note?: string; item: Solution }) {
  return (
    <div style={{ border: "1px solid var(--line)", borderRadius: 6, overflow: "hidden" }}>
      <div
        style={{
          display: "flex",
          alignItems: "baseline",
          gap: "0.7rem",
          padding: "0.45rem 0.85rem",
          background: "var(--panel-2)",
          fontSize: "0.82rem",
        }}
      >
        <b style={{ fontWeight: 600 }}>{title}</b>
        {note ? <span style={{ color: "var(--ink-2)", fontSize: "0.78rem" }}>{note}</span> : null}
        <span
          style={{
            marginLeft: "auto",
            fontFamily: "var(--mono)",
            fontSize: "0.7rem",
            color: "var(--ink-3)",
          }}
        >
          {item.file}
        </span>
      </div>
      <pre
        style={{
          margin: 0,
          padding: "0.85rem 1rem",
          overflowX: "auto",
          background: "var(--panel)",
          fontFamily: "var(--mono)",
          fontSize: "0.78rem",
          lineHeight: 1.6,
        }}
      >
        {item.code.trimEnd()}
      </pre>
    </div>
  );
}

export default async function LevelPage({
  params,
}: {
  params: Promise<{ track: string; level: string }>;
}) {
  const { track, level: slug } = await params;
  const level = findLevel(track, slug);
  if (!level) return null;

  const siblings = allLevels().filter((l) => l.trackSlug === track);
  const at = siblings.findIndex((l) => l.slug === slug);
  const prev = siblings[at - 1];
  const next = siblings[at + 1];

  return (
    <article
      style={{
        maxWidth: "50rem",
        margin: "0 auto",
        padding: "clamp(1.5rem, 5vw, 3rem) clamp(1rem, 4vw, 2rem)",
      }}
    >
      <div
        style={{
          display: "flex",
          gap: "0.5rem 1rem",
          flexWrap: "wrap",
          fontFamily: "var(--mono)",
          fontSize: "0.72rem",
          color: "var(--ink-3)",
        }}
      >
        <Link href="/" style={{ color: "var(--ink-2)" }}>
          ← все треки
        </Link>
        <span>{level.track}</span>
        <span>{level.minutes} мин</span>
        <span>{level.lang}</span>
      </div>

      <h1
        style={{
          fontSize: "clamp(1.6rem, 4vw, 2.1rem)",
          lineHeight: 1.15,
          letterSpacing: "-0.02em",
          margin: "0.6rem 0 0.5rem",
          textWrap: "balance",
        }}
      >
        {level.title}
      </h1>
      <p style={{ color: "var(--ink-2)", margin: "0 0 1.2rem", fontSize: "1.02rem" }}>
        {level.idea}
      </p>

      <pre
        style={{
          background: "var(--panel)",
          border: "1px solid var(--line)",
          borderRadius: 6,
          padding: "0.7rem 0.9rem",
          overflowX: "auto",
          fontFamily: "var(--mono)",
          fontSize: "0.74rem",
          color: "var(--ink-2)",
          margin: "0 0 2.5rem",
        }}
      >
        python engine/check.py {level.path}/starter/novice/{level.starters.novice?.file ?? "agent.py"}
      </pre>

      <div className="prose" dangerouslySetInnerHTML={html(level.theory)} />
      <div className="prose" style={{ marginTop: "3rem" }} dangerouslySetInnerHTML={html(level.method)} />
      <div className="prose" style={{ marginTop: "3rem" }} dangerouslySetInnerHTML={html(level.task)} />

      {level.runnable ? (
        <Runner
          levelId={`${level.trackSlug}/${level.slug}`}
          engine={engineSources()}
          scenario={level.scenario}
          starters={level.starters}
          solution={level.solution}
          hintHtml={level.hint ? (marked.parse(level.hint, { async: false }) as string) : ""}
        />
      ) : (
        <p
          style={{
            marginTop: "3rem",
            padding: "0.8rem 1rem",
            border: "1px solid var(--line)",
            borderRadius: 6,
            color: "var(--ink-2)",
            fontSize: "0.9rem",
          }}
        >
          Этот уровень на {level.lang} — в браузере он не запускается, для него
          остаются чтение и командная строка.
        </p>
      )}

      <section style={{ marginTop: "3rem", display: "flex", flexDirection: "column", gap: "1rem" }}>
        <h2 style={{ fontSize: "1.28rem", margin: 0, letterSpacing: "-0.015em" }}>Код уровня</h2>
        <p style={{ margin: 0, color: "var(--ink-2)", fontSize: "0.9rem", maxWidth: "38rem" }}>
          Заготовки отличаются только количеством подсказок. Эталон стоит
          открывать после своей попытки — иначе уровень превращается в чтение.
        </p>

        {(["novice", "advanced", "pro"] as const).map((tier) => {
          const item = level.starters[tier];
          return item ? (
            <Code key={tier} title={TIER_TITLES[tier]} item={item} />
          ) : null;
        })}

        {level.solution ? (
          <details>
            <summary
              style={{
                cursor: "pointer",
                fontSize: "0.9rem",
                color: "var(--accent)",
                padding: "0.3rem 0",
              }}
            >
              Показать эталон
            </summary>
            <div style={{ marginTop: "0.6rem" }}>
              <Code title="Эталон" note="решение, проходящее проверку" item={level.solution} />
            </div>
          </details>
        ) : null}
      </section>

      <nav
        style={{
          marginTop: "3rem",
          paddingTop: "1.2rem",
          borderTop: "1px solid var(--line)",
          display: "flex",
          justifyContent: "space-between",
          gap: "1rem",
          fontSize: "0.88rem",
        }}
      >
        {prev ? (
          <Link href={`/${prev.trackSlug}/${prev.slug}/`} style={{ color: "var(--ink-2)" }}>
            ← {prev.title}
          </Link>
        ) : (
          <span />
        )}
        {next ? (
          <Link href={`/${next.trackSlug}/${next.slug}/`} style={{ color: "var(--accent)", textAlign: "right" }}>
            {next.title} →
          </Link>
        ) : (
          <span />
        )}
      </nav>
    </article>
  );
}
