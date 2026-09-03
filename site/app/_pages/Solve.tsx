import { marked } from "marked";
import { allLevels, directory, engineSources, findLevel, outline } from "@/lib/content";
import { at, dictFor, type Lang } from "@/lib/i18n";
import Gate from "../Gate";
import Runner from "../Runner";

const base = process.env.NEXT_PUBLIC_BASE_PATH ?? "";

export default function Solve({
  lang,
  track,
  slug,
}: {
  lang: Lang;
  track: string;
  slug: string;
}) {
  const dict = dictFor(lang);
  const level = findLevel(lang, track, slug);
  if (!level) return null;

  const here = (path: string) => at(lang, base, path);
  const siblings = allLevels(lang).filter((l) => l.trackSlug === track);
  const next = siblings[siblings.findIndex((l) => l.slug === slug) + 1];
  const levelId = `${level.trackSlug}/${level.slug}`;
  const lesson = level.translated ? undefined : "ru";

  return (
    <Gate
      outline={outline()}
      levelId={levelId}
      titles={directory(lang, here(""))}
      lang={lang}
    >
      <div
        style={{
          maxWidth: "60rem",
          margin: "0 auto",
          padding: "var(--top-gap) clamp(1rem, 4vw, 2rem)",
        }}
      >
        <div
          style={{
            display: "flex",
            gap: "0.5rem 1rem",
            flexWrap: "wrap",
            alignItems: "baseline",
            marginBottom: "0.5rem",
          }}
        >
          <a
            href={here(`/${level.trackSlug}/${level.slug}/`)}
            style={{ fontSize: "0.84rem", color: "var(--ink-2)", fontWeight: 600 }}
          >
            {dict.backToLesson}
          </a>
          <span className="chip">{level.track}</span>
          <span className="chip">{level.lang}</span>
        </div>

        <h1
          lang={lesson}
          style={{
            fontSize: "clamp(1.5rem, 4vw, 1.9rem)",
            fontWeight: 750,
            letterSpacing: "-0.02em",
            margin: "0 0 0.35rem",
            textWrap: "balance",
          }}
        >
          {level.title}
        </h1>
        <p lang={lesson} style={{ color: "var(--ink-2)", margin: "0 0 1.6rem", maxWidth: "40rem" }}>
          {level.idea}
        </p>

        {/* Вердикт проверки печатается ниже, и на непереведённом уровне он
            русский. Предупреждение о нём должно стоять на той странице, где
            он появляется, а не только на странице урока. */}
        {lesson === "ru" && lang !== "ru" ? (
          <div
            className="card"
            style={{
              padding: "0.7rem 0.9rem",
              marginBottom: "1.6rem",
              fontSize: "0.88rem",
              color: "var(--ink-2)",
              maxWidth: "40rem",
            }}
          >
            <strong style={{ color: "var(--ink)", fontWeight: 680 }}>
              {dict.notTranslatedTitle}
            </strong>{" "}
            {dict.notTranslatedBody}
          </div>
        ) : null}

        <Runner
          levelId={levelId}
          command={level.command}
          engine={engineSources()}
          scenario={level.scenario}
          starters={level.starters}
          solution={level.solution}
          hintHtml={level.hint ? (marked.parse(level.hint, { async: false }) as string) : ""}
          nextHref={next ? here(`/${next.trackSlug}/${next.slug}/`) : null}
          nextTitle={next ? next.title : null}
          lang={lang}
        />
      </div>
    </Gate>
  );
}
