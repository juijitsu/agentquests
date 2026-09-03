import { tracks, allLevels } from "@/lib/content";
import Tracks, { type Group } from "./Tracks";

const PLANNED: Record<string, number> = {
  foundations: 8,
  "agent-core": 10,
  context: 8,
  retrieval: 9,
  evaluation: 8,
};

const TOTAL_PLANNED = 76;
const base = process.env.NEXT_PUBLIC_BASE_PATH ?? "";

export default function Home() {
  const done = allLevels().length;
  const langs = [...new Set(allLevels().map((l) => l.lang))].filter((l) => l !== "—");

  const groups: Group[] = tracks().map((t) => ({
    slug: t.slug,
    title: t.title,
    planned: PLANNED[t.slug] ?? t.levels.length,
    levels: t.levels.map((l) => ({
      id: `${l.trackSlug}/${l.slug}`,
      href: `${base}/${l.trackSlug}/${l.slug}/`,
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
          Курс, который нельзя пройти чтением
        </h1>
        <p
          style={{
            color: "var(--ink-2)",
            fontSize: "1.08rem",
            fontWeight: 500,
            margin: "0 0 1.3rem",
          }}
        >
          Уровень даёт теорию, затем метод, затем задание. Следующий открывается,
          когда проходят тесты, — а не когда вы дочитали.
        </p>

        <div style={{ display: "flex", flexWrap: "wrap", gap: "0.45rem" }}>
          <span className="chip">готово уровней: {done} из {TOTAL_PLANNED}</span>
          {langs.map((l) => (
            <span key={l} className="chip">
              {l}
            </span>
          ))}
          <span className="chip">запуск прямо в браузере</span>
        </div>

        <p
          style={{
            marginTop: "1.3rem",
            marginBottom: 0,
            fontSize: "0.92rem",
            color: "var(--ink-2)",
          }}
        >
          Открывайте любой уровень, правьте код и жмите «Запустить» — Python
          подгрузится сам. Ставить ничего не нужно. Поиск по уровням —{" "}
          <span className="chip">Ctrl K</span>
        </p>
      </section>

      <Tracks groups={groups} />
    </div>
  );
}
