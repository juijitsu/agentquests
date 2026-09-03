import { render } from "@/lib/md";
import { allLevels, directory, findLevel, outline } from "@/lib/content";
import { at, dictFor, type Lang } from "@/lib/i18n";
import Gate from "../Gate";
import Walkthrough from "../Walkthrough";
import Terminal from "../Terminal";
import LevelStar from "../LevelStar";

const base = process.env.NEXT_PUBLIC_BASE_PATH ?? "";

function html(md: string) {
  return { __html: render(md) };
}

export default function Level({
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
  const spot = siblings.findIndex((l) => l.slug === slug);
  const prev = siblings[spot - 1];
  const next = siblings[spot + 1];
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
          maxWidth: "78rem",
          margin: "0 auto",
          padding: "var(--top-gap) clamp(1rem, 4vw, 2rem)",
        }}
      >
        {/* Заголовок стоит внутри левой колонки, а не над сеткой: только так
            панель разбора начинается там же, где потом закрепляется. */}
        <div className="split">
          <div>
            <div
              style={{
                display: "flex",
                gap: "0.5rem 0.8rem",
                flexWrap: "wrap",
                alignItems: "baseline",
              }}
            >
              <a
                href={here("/")}
                style={{ fontSize: "0.84rem", color: "var(--ink-2)", fontWeight: 600 }}
              >
                {dict.allTracks}
              </a>
              <span className="chip">{level.track}</span>
              <span className="chip">
                {level.minutes} {dict.minutes}
              </span>
              <span className="chip">{level.lang}</span>
            </div>

            <h1
              lang={lesson}
              style={{
                fontSize: "clamp(1.7rem, 4.5vw, 2.3rem)",
                fontWeight: 780,
                lineHeight: 1.12,
                letterSpacing: "-0.025em",
                margin: "0.7rem 0 0.4rem",
                textWrap: "balance",
              }}
            >
              {level.title}
            </h1>
            <p lang={lesson} style={{ color: "var(--ink-2)", margin: "0 0 1.4rem", fontSize: "1.04rem" }}>
              {level.idea}
            </p>

            {/* Перевода урока ещё нет — об этом говорится прямо, а не
                подсовывается русский текст под видом английского. */}
            {lesson === "ru" && lang !== "ru" ? (
              <div
                className="card"
                style={{
                  padding: "0.7rem 0.9rem",
                  marginBottom: "2rem",
                  fontSize: "0.88rem",
                  color: "var(--ink-2)",
                }}
              >
                <strong style={{ color: "var(--ink)", fontWeight: 680 }}>
                  {dict.notTranslatedTitle}
                </strong>{" "}
                {dict.notTranslatedBody}
              </div>
            ) : (
              <div style={{ height: "1rem" }} />
            )}

            <div lang={lesson} className="prose" dangerouslySetInnerHTML={html(level.theory)} />
            <div
              lang={lesson}
              className="prose"
              style={{ marginTop: "3rem" }}
              dangerouslySetInnerHTML={html(level.method)}
            />
            <div
              lang={lesson}
              className="prose"
              style={{ marginTop: "3rem" }}
              dangerouslySetInnerHTML={html(level.task)}
            />

            <nav
              style={{
                marginTop: "3rem",
                paddingTop: "1.2rem",
                borderTop: "1px solid var(--line)",
                display: "flex",
                justifyContent: "space-between",
                gap: "1rem",
                fontSize: "0.88rem",
                fontWeight: 600,
              }}
            >
              {prev ? (
                <a href={here(`/${prev.trackSlug}/${prev.slug}/`)} style={{ color: "var(--ink-2)" }}>
                  ← {prev.title}
                </a>
              ) : (
                <span />
              )}
              {next ? (
                <a
                  href={here(`/${next.trackSlug}/${next.slug}/`)}
                  style={{ color: "var(--accent)", textAlign: "right" }}
                >
                  {next.title} →
                </a>
              ) : (
                <span />
              )}
            </nav>
          </div>

          {level.runnable ? (
            <Walkthrough
              starterName={level.starters.novice?.file ?? "agent.py"}
              starter={level.starters.novice?.code ?? ""}
              solution={level.solution?.code ?? null}
              solutionName={level.solution?.file ?? "agent.py"}
              demo={level.demo}
              solveHref={here(`/${level.trackSlug}/${level.slug}/solve/`)}
              lang={lang}
            />
          ) : (
            <aside
              style={{
                position: "sticky",
                top: "calc(var(--header-h) + var(--top-gap))",
                display: "flex",
                flexDirection: "column",
                gap: "0.7rem",
              }}
            >
              <div className="card" style={{ padding: "1rem" }}>
                <strong style={{ fontWeight: 700 }}>{dict.otherLangTitle(level.lang)}</strong>
                <p style={{ margin: "0.4rem 0 0", fontSize: "0.9rem", color: "var(--ink-2)" }}>
                  {dict.otherLangBody}
                </p>
              </div>
              {/* Команда нужна именно здесь: другого способа проверить себя
                  на этом уровне нет. Там, где работает кнопка, её не показываем. */}
              <Terminal title={dict.ownTerminal} output={`$ ${level.command}`} />
            </aside>
          )}
        </div>

        <LevelStar
          lang={lang}
          hints={[
            { title: dict.hAboutTitle, body: level.idea },
            ...(level.hint
              ? [
                  {
                    title: dict.hLevelTitle,
                    body: render(level.hint),
                    html: true,
                  },
                ]
              : []),
            {
              title: dict.hSolveTitle,
              body: level.runnable ? dict.hSolveBrowser : dict.hSolveConsole(level.command),
            },
          ]}
        />
      </div>
    </Gate>
  );
}
