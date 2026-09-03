import { tracks, allLevels, outline } from "@/lib/content";
import { at, dictFor, type Lang } from "@/lib/i18n";
import { COURSES, COURSES_TOTAL, isCourse } from "@/lib/sections";
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

/** Полка раздела. Разделов два, и различаются они только тем, какие треки
    считают своими и какими словами о себе говорят; всё остальное совпадает,
    поэтому страница одна. */
export default function Home({
  lang,
  section = "agents",
}: {
  lang: Lang;
  section?: "agents" | "courses";
}) {
  const dict = dictFor(lang);
  const courses = section === "courses";
  const mine = (slug: string) => (courses ? isCourse(slug) : !isCourse(slug));

  const planned = courses ? COURSES : PLANNED;
  const total = courses ? COURSES_TOTAL : TOTAL_PLANNED;

  // Счётчик раздела считает уровни раздела: «76 уровней про агентов» должно
  // оставаться правдой после того, как рядом появились курсы.
  const levels = allLevels(lang).filter((l) => mine(l.trackSlug));
  const done = levels.length;
  const langs = [...new Set(levels.map((l) => l.lang))].filter((l) => l !== "—");

  const groups: Group[] = tracks(lang)
    .filter((t) => mine(t.slug))
    .map((t) => ({
      slug: t.slug,
      title: t.title,
      planned: planned[t.slug] ?? t.levels.length,
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
          {courses ? dict.coursesTitle : dict.heroTitle}
        </h1>
        <p
          style={{
            color: "var(--ink-2)",
            fontSize: "1.08rem",
            fontWeight: 500,
            margin: "0 0 1.3rem",
          }}
        >
          {courses ? dict.coursesLead : dict.heroLead}
        </p>

        <div style={{ display: "flex", flexWrap: "wrap", gap: "0.45rem" }}>
          <span className="chip">{dict.chipDone(done, total)}</span>
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
          {courses ? dict.coursesNote : dict.homeNote}
          {courses ? null : (
            <>
              {" "}
              <span className="chip">Ctrl K</span>
            </>
          )}
        </p>

        {/* Разделы стоят рядом, а не один внутри другого: с каждого видно
            другой, и ни один не заявляет уровни соседа своими. */}
        <p style={{ margin: "1.1rem 0 0", fontSize: "0.92rem" }}>
          <a
            href={at(lang, base, courses ? "/" : "/courses/")}
            style={{ fontWeight: 600 }}
          >
            {courses ? dict.toAgents : dict.toCourses} →
          </a>
        </p>
      </section>

      <Tracks groups={groups} outline={outline()} lang={lang} />

      {/* Подсказки полки — про её устройство. Всё сказанное проверяемо на
          самой странице: замки, разбор, запуск в браузере. */}
      <LevelStar
        hints={courses ? dict.coursesHints(done, total) : dict.homeHints(done, total)}
        lang={lang}
      />
    </div>
  );
}
