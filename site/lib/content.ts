import { readFileSync, readdirSync, existsSync } from "node:fs";
import runs from "./runs.json";
import { join } from "node:path";

/** Уровни лежат рядом с сайтом и остаются единственным источником правды. */
const ROOT = join(process.cwd(), "..", "content", "ru");
const ENGINE = join(process.cwd(), "..", "engine");

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
  /** Запуск в своей консоли. Нужен там, где браузер не выручает: движок сам
      зовёт node для TypeScript, поэтому команда одна на все языки. */
  command: string;
  theory: string;
  method: string;
  task: string;
  scenario: string;
  /** Блок «Если застряли» из задания — им подсвечивается провал. */
  hint: string;
  solution: Solution | null;
  starters: Partial<Record<Tier, Solution>>;
  /** Уровень исполним в браузере: сценарий на Python, решение на Python или SQL. */
  runnable: boolean;
  /** Настоящие прогоны, снятые при сборке: заготовка и эталон. */
  demo: { novice?: Run; solution?: Run };
  /** Порядковый номер трека и уровня — по ним считаются замки. */
  trackIndex: number;
  indexInTrack: number;
};

export type Run = { output: string; code: number };

/** Исходники движка едут в браузер как есть — второй реализации вердикта нет. */
export function engineSources(): { kit: string; check: string } {
  return {
    kit: read(join(ENGINE, "kit.py")),
    check: read(join(ENGINE, "check.py")),
  };
}

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

/** На странице задание показывается без двух блоков.

    Первый — команда `python engine/check.py …`: на сайте запускают кнопкой,
    и длинный путь к файлу там только висит лишней строкой. Второй — таблица
    «Выберите сложность»: сложность выбирается кнопками на странице решения,
    и папки starter/ посетителю сайта ни о чём не говорят.

    Из файлов ничего не удаляется: их читают из репозитория и из командной
    строки, где обе вещи как раз нужны. */
function taskForWeb(task: string): string {
  const lines = task.split("\n");
  const out: string[] = [];
  let dropping = false;

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    if (line.startsWith("## ")) dropping = line.startsWith("## Выберите сложность");
    if (dropping) continue;

    const opensRun =
      line.startsWith("```") && /^(python|node) engine[/]check/.test(lines[i + 1] ?? "");
    if (opensRun) {
      while (i + 1 < lines.length && !lines[i + 1].startsWith("```")) i++;
      i++;
      // Подводка «Запустите как есть:» без команды повисает — снимаем и её.
      while (out.length && !out[out.length - 1].trim()) out.pop();
      if (out.length && out[out.length - 1].trimEnd().endsWith(":")) out.pop();
      continue;
    }

    out.push(line);
  }

  return out.join("\n").trim();
}

/** «Если застряли» уже написан в каждом задании — незачем сочинять второй. */
function hintFrom(task: string): string {
  const at = task.indexOf("## Если застряли");
  if (at < 0) return "";
  const rest = task.slice(at + "## Если застряли".length);
  const end = rest.indexOf("\n## ");
  return (end < 0 ? rest : rest.slice(0, end)).trim();
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
          const here = `content/ru/${trackDir}/${levelDir}`;
          return {
            slug,
            trackSlug,
            track: TRACK_TITLES[trackSlug] ?? trackSlug,
            order: Number(card.order ?? 0),
            title: card.title ?? levelDir,
            idea: card.idea ?? "",
            minutes: card.minutes ?? "",
            lang: solution?.lang ?? "—",
            path: here,
            command: `python engine/check.py ${here}/starter/novice/${
              starters.novice?.file ?? "agent.py"
            }`,
            theory: read(join(dir, "theory.md")),
            method: read(join(dir, "method.md")),
            task: taskForWeb(read(join(dir, "task.md"))),
            scenario: scenarioIn(dir).code,
            hint: hintFrom(read(join(dir, "task.md"))),
            solution,
            starters,
            demo: (runs as Record<string, Level["demo"]>)[card.id] ?? {},
            trackIndex: 0,
            indexInTrack: 0,
            runnable:
              scenarioIn(dir).name.endsWith(".py") &&
              (solution?.file.endsWith(".py") || solution?.file.endsWith(".sql")) === true,
          };
        })
        .filter((l): l is Level => l !== null);

      levels.forEach((l, i) => {
        l.indexInTrack = i;
      });

      const first = levels[0];
      return {
        slug: first?.trackSlug ?? trackDir,
        dir: trackDir,
        title: first?.track ?? trackDir,
        levels,
      };
    })
    .filter((t) => t.levels.length > 0);

  cache.forEach((t, i) => t.levels.forEach((l) => (l.trackIndex = i)));

  return cache;
}

export function allLevels(): Level[] {
  return tracks().flatMap((t) => t.levels);
}

export function findLevel(trackSlug: string, slug: string): Level | undefined {
  return allLevels().find((l) => l.trackSlug === trackSlug && l.slug === slug);
}

/** Порядок треков и уровней — по нему клиент считает замки. */
export function outline(): { track: string; levels: string[] }[] {
  return tracks().map((t) => ({
    track: t.slug,
    levels: t.levels.map((l) => `${l.trackSlug}/${l.slug}`),
  }));
}

/** Названия и адреса всех уровней — чтобы замок мог сказать, куда идти. */
export function directory(base: string): Record<string, { title: string; href: string }> {
  const out: Record<string, { title: string; href: string }> = {};
  for (const l of allLevels()) {
    out[`${l.trackSlug}/${l.slug}`] = {
      title: l.title,
      href: `${base}/${l.trackSlug}/${l.slug}/`,
    };
  }
  return out;
}
