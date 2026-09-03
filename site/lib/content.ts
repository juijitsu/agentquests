import { readFileSync, readdirSync, existsSync } from "node:fs";
import { join } from "node:path";

/** Уровни лежат рядом с сайтом и остаются единственным источником правды. */
const ROOT = join(process.cwd(), "..", "content", "ru");

const TIERS = ["novice", "advanced", "pro"] as const;
const LANGS: Record<string, string> = { ".py": "Python", ".ts": "TypeScript", ".sql": "SQL" };

export type Tier = (typeof TIERS)[number];

export type Solution = { file: string; lang: string; code: string };

export type Level = {
  slug: string;
  track: string;
  trackSlug: string;
  order: number;
  title: string;
  idea: string;
  minutes: string;
  lang: string;
  path: string;
  theory: string;
  method: string;
  task: string;
  scenario: string;
  solution: Solution | null;
  starters: Partial<Record<Tier, Solution>>;
};

export type Track = {
  slug: string;
  dir: string;
  title: string;
  levels: Level[];
};

const TRACK_TITLES: Record<string, string> = {
  foundations: "Фундамент",
  "agent-core": "Агентный трек",
  context: "Контекст",
  retrieval: "Поиск",
  evaluation: "Оценка",
};

function read(path: string): string {
  return existsSync(path) ? readFileSync(path, "utf8") : "";
}

/** level.yaml — плоские «ключ: значение» по одному в строке, парсер не нужен. */
function meta(dir: string): Record<string, string> {
  const lines = read(join(dir, "level.yaml")).split("\n");
  const out: Record<string, string> = {};
  for (const line of lines) {
    const at = line.indexOf(": ");
    if (at > 0) out[line.slice(0, at)] = line.slice(at + 2).trim();
  }
  return out;
}

function codeIn(dir: string): Solution | null {
  if (!existsSync(dir)) return null;
  const file = readdirSync(dir).find((n) => n.startsWith("agent."));
  if (!file) return null;
  const ext = file.slice(file.lastIndexOf("."));
  return { file, lang: LANGS[ext] ?? ext.slice(1), code: read(join(dir, file)) };
}

function scenarioIn(dir: string): { name: string; code: string } {
  const file = readdirSync(dir).find((n) => n.startsWith("scenario."));
  return file ? { name: file, code: read(join(dir, file)) } : { name: "", code: "" };
}

let cache: Track[] | null = null;

export function tracks(): Track[] {
  if (cache) return cache;

  cache = readdirSync(ROOT)
    .filter((d) => existsSync(join(ROOT, d)))
    .sort()
    .map((trackDir) => {
      const levels = readdirSync(join(ROOT, trackDir))
        .sort()
        .map((levelDir): Level | null => {
          const dir = join(ROOT, trackDir, levelDir);
          const card = meta(dir);
          if (!card.id) return null;

          const solution = codeIn(join(dir, "solution"));
          const starters: Partial<Record<Tier, Solution>> = {};
          for (const tier of TIERS) {
            const found = codeIn(join(dir, "starter", tier));
            if (found) starters[tier] = found;
          }

          const [trackSlug, slug] = card.id.split("/");
          return {
            slug,
            trackSlug,
            track: TRACK_TITLES[trackSlug] ?? trackSlug,
            order: Number(card.order ?? 0),
            title: card.title ?? levelDir,
            idea: card.idea ?? "",
            minutes: card.minutes ?? "",
            lang: solution?.lang ?? "—",
            path: `content/ru/${trackDir}/${levelDir}`,
            theory: read(join(dir, "theory.md")),
            method: read(join(dir, "method.md")),
            task: read(join(dir, "task.md")),
            scenario: scenarioIn(dir).code,
            solution,
            starters,
          };
        })
        .filter((l): l is Level => l !== null);

      const first = levels[0];
      return {
        slug: first?.trackSlug ?? trackDir,
        dir: trackDir,
        title: first?.track ?? trackDir,
        levels,
      };
    })
    .filter((t) => t.levels.length > 0);

  return cache;
}

export function allLevels(): Level[] {
  return tracks().flatMap((t) => t.levels);
}

export function findLevel(trackSlug: string, slug: string): Level | undefined {
  return allLevels().find((l) => l.trackSlug === trackSlug && l.slug === slug);
}
