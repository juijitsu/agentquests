import { tracks, allLevels, outline } from "@/lib/content";
import { at, dictFor, type Lang } from "@/lib/i18n";
import Tracks, { type Group } from "../Tracks";
import LevelStar from "../LevelStar";

const PLANNED: Record<string, number> = {
  foundations: 8,
  "agent-core": 10,
  context: 8,
  retrieval: 9,
  evaluation: 8,
  "red-team": 8,
};

const TOTAL_PLANNED = 76;
const base = process.env.NEXT_PUBLIC_BASE_PATH ?? "";

export default function Home({ lang }: { lang: Lang }) {
  const dict = dictFor(lang);
  const done = allLevels(lang).length;
  const langs = [...new Set(allLevels(lang).map((l) => l.lang))].filter((l) => l !== "—");

  const groups: Group[] = tracks(lang).map((t) => ({
    slug: t.slug,
    title: t.title,
    planned: PLANNED[t.slug] ?? t.levels.length,
    levels: t.levels.map((l) => ({
      id: `${l.trackSlug}/${l.slug}`,
      href: at(lang, base, `/${l.trackSlug}/${l.slug}/`),
      order: l.order,
      title: l.title,
      idea: l.idea,
      lang: l.lang,
    })),
  }));

  return (
    <div
      style={{
        maxWidth: "72rem",
        margin: "0 auto",
        padding: "clamp(2rem, 6vw, 3.5rem) clamp(1rem, 4vw, 2rem)",
      }}
    >
      <section style={{ maxWidth: "44rem" }}>
        <h1
          style={{
            fontSize: "clamp(2rem, 6vw, 3rem)",
            fontWeight: 850,
            lineHeight: 1.05,
            letterSpacing: "-0.035em",
            margin: "0 0 0.7rem",
            textWrap: "balance",
          }}
        >
          {dict.heroTitle}
        </h1>
        <p
          style={{
            color: "var(--ink-2)",
            fontSize: "1.08rem",
            fontWeight: 500,
            margin: "0 0 1.3rem",
          }}
        >
          {dict.heroLead}
        </p>

        <div style={{ display: "flex", flexWrap: "wrap", gap: "0.45rem" }}>
          <span className="chip">{dict.chipDone(done, TOTAL_PLANNED)}</span>
          {langs.map((l) => (
            <span key={l} className="chip">
              {l}
            </span>
          ))}
          <span className="chip">{dict.chipBrowser}</span>
        </div>

        <p
          style={{
            marginTop: "1.3rem",
            marginBottom: 0,
            fontSize: "0.92rem",
            color: "var(--ink-2)",
          }}
        >
          {dict.homeNote} <span className="chip">Ctrl K</span>
        </p>
      </section>

      <Tracks groups={groups} outline={outline()} lang={lang} />

      {/* Подсказки главной — про устройство курса. Всё сказанное здесь
          проверяемо на самой странице: замки, разбор, запуск в браузере. */}
      <LevelStar hints={dict.homeHints(done, TOTAL_PLANNED)} lang={lang} />
    </div>
  );
}
