import Link from "next/link";
import { marked } from "marked";
import {
  allLevels,
  directory,
  engineSources,
  findLevel,
  outline,
} from "@/lib/content";
import Gate from "../../../Gate";
import Runner from "../../../Runner";

const base = process.env.NEXT_PUBLIC_BASE_PATH ?? "";

export function generateStaticParams() {
  return allLevels()
    .filter((l) => l.runnable)
    .map((l) => ({ track: l.trackSlug, level: l.slug }));
}

export default async function SolvePage({
  params,
}: {
  params: Promise<{ track: string; level: string }>;
}) {
  const { track, level: slug } = await params;
  const level = findLevel(track, slug);
  if (!level) return null;

  const siblings = allLevels().filter((l) => l.trackSlug === track);
  const next = siblings[siblings.findIndex((l) => l.slug === slug) + 1];
  const levelId = `${level.trackSlug}/${level.slug}`;

  return (
    <Gate outline={outline()} levelId={levelId} titles={directory(base)}>
      <div
        style={{
          maxWidth: "60rem",
          margin: "0 auto",
          padding: "clamp(1.2rem, 4vw, 2.4rem) clamp(1rem, 4vw, 2rem)",
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
          <Link
            href={`/${level.trackSlug}/${level.slug}/`}
            style={{ fontSize: "0.84rem", color: "var(--ink-2)", fontWeight: 600 }}
          >
            ← к разбору
          </Link>
          <span className="chip">{level.track}</span>
          <span className="chip">{level.lang}</span>
        </div>

        <h1
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
        <p style={{ color: "var(--ink-2)", margin: "0 0 1.6rem", maxWidth: "40rem" }}>
          {level.idea}
        </p>

        <Runner
          levelId={levelId}
          command={level.command}
          engine={engineSources()}
          scenario={level.scenario}
          starters={level.starters}
          solution={level.solution}
          hintHtml={level.hint ? (marked.parse(level.hint, { async: false }) as string) : ""}
          nextHref={next ? `${base}/${next.trackSlug}/${next.slug}/` : null}
          nextTitle={next ? next.title : null}
        />
      </div>
    </Gate>
  );
}
