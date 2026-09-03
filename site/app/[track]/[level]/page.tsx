import Link from "next/link";
import { marked } from "marked";
import { allLevels, directory, findLevel, outline } from "@/lib/content";
import Gate from "../../Gate";
import Walkthrough from "../../Walkthrough";
import Terminal from "../../Terminal";
import LevelStar from "../../LevelStar";

const base = process.env.NEXT_PUBLIC_BASE_PATH ?? "";

export function generateStaticParams() {
  return allLevels().map((l) => ({ track: l.trackSlug, level: l.slug }));
}

function html(md: string) {
  return { __html: marked.parse(md, { async: false }) as string };
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
  const levelId = `${level.trackSlug}/${level.slug}`;
  const solveHref = `${base}/${level.trackSlug}/${level.slug}/solve/`;

  return (
    <Gate outline={outline()} levelId={levelId} titles={directory(base)}>
      <div
        style={{
          maxWidth: "78rem",
          margin: "0 auto",
          padding: "clamp(1.2rem, 4vw, 2.4rem) clamp(1rem, 4vw, 2rem)",
        }}
      >
        <div
          style={{
            display: "flex",
            gap: "0.5rem 0.8rem",
            flexWrap: "wrap",
            alignItems: "baseline",
          }}
        >
          <Link href="/" style={{ fontSize: "0.84rem", color: "var(--ink-2)", fontWeight: 600 }}>
            ← все треки
          </Link>
          <span className="chip">{level.track}</span>
          <span className="chip">{level.minutes} мин</span>
          <span className="chip">{level.lang}</span>
        </div>

        <h1
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
        <p
          style={{
            color: "var(--ink-2)",
            margin: "0 0 2rem",
            fontSize: "1.04rem",
            maxWidth: "42rem",
          }}
        >
          {level.idea}
        </p>

        <div className="split">
          <div>
            <div className="prose" dangerouslySetInnerHTML={html(level.theory)} />
            <div
              className="prose"
              style={{ marginTop: "3rem" }}
              dangerouslySetInnerHTML={html(level.method)}
            />
            <div
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
                <Link href={`/${prev.trackSlug}/${prev.slug}/`} style={{ color: "var(--ink-2)" }}>
                  ← {prev.title}
                </Link>
              ) : (
                <span />
              )}
              {next ? (
                <Link
                  href={`/${next.trackSlug}/${next.slug}/`}
                  style={{ color: "var(--accent)", textAlign: "right" }}
                >
                  {next.title} →
                </Link>
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
              solveHref={solveHref}
            />
          ) : (
            <aside
              style={{
                position: "sticky",
                top: "4.2rem",
                display: "flex",
                flexDirection: "column",
                gap: "0.7rem",
              }}
            >
              <div className="card" style={{ padding: "1rem" }}>
                <strong style={{ fontWeight: 700 }}>Уровень на {level.lang}</strong>
                <p style={{ margin: "0.4rem 0 0", fontSize: "0.9rem", color: "var(--ink-2)" }}>
                  В браузере он не запускается: там живёт только Python. Значит
                  запуск один — в своей консоли, из корня репозитория.
                </p>
              </div>
              {/* Команда нужна именно здесь: другого способа проверить себя
                  на этом уровне нет. Там, где работает кнопка, её не показываем. */}
              <Terminal title="в своём терминале" output={`$ ${level.command}`} />
            </aside>
          )}
        </div>

        {/* Подсказки уровня — только из самого уровня: его смысл, его блок
            «Если застряли» и способ запуска. Ничего сверх того, что написано. */}
        <LevelStar
          hints={[
            { title: "про что уровень", body: level.idea },
            ...(level.hint
              ? [
                  {
                    title: "подсказка уровня",
                    body: marked.parse(level.hint, { async: false }) as string,
                    html: true,
                  },
                ]
              : []),
            {
              title: "где решать",
              body: level.runnable
                ? "Кнопка «Решать этот уровень» открывает страницу с терминалом прямо в браузере. Заготовка там уже лежит — её и правят."
                : `Этот уровень в браузере не идёт. Запуск в своей консоли, из корня репозитория: ${level.command}`,
            },
          ]}
        />
      </div>
    </Gate>
  );
}
