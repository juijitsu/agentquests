import type { Metadata } from "next";
import Shell, { themeScript, type Entry } from "./Shell";
import { allLevels } from "@/lib/content";
import "./globals.css";

export const metadata: Metadata = {
  title: "AgentQuests — курс по инженерии ИИ-агентов",
  description:
    "Восемь треков, каждый уровень проверяется тестами. Теория, метод, задание — и проверка, которую не пройти чтением.",
};

const base = process.env.NEXT_PUBLIC_BASE_PATH ?? "";

export default function RootLayout({ children }: { children: React.ReactNode }) {
  const entries: Entry[] = allLevels().map((l) => ({
    title: l.title,
    track: l.track,
    idea: l.idea,
    order: l.order,
    href: `${base}/${l.trackSlug}/${l.slug}/`,
  }));

  return (
    <html lang="ru">
      <head>
        <script dangerouslySetInnerHTML={{ __html: themeScript }} />
      </head>
      <body>
        <Shell entries={entries} />
        <main>{children}</main>
        <footer
          style={{
            borderTop: "2px solid var(--line)",
            marginTop: "4rem",
            padding: "1.5rem clamp(1rem, 4vw, 2rem)",
            fontSize: "0.84rem",
            color: "var(--ink-3)",
          }}
        >
          <div
            style={{
              maxWidth: "72rem",
              margin: "0 auto",
              display: "flex",
              gap: "0.6rem 1.4rem",
              flexWrap: "wrap",
            }}
          >
            <span>Уровни и движок — MIT.</span>
            <span>Ни ключа, ни пакетов, ни сети.</span>
            <a
              href="https://github.com/juijitsu/agentquests"
              style={{ marginLeft: "auto", fontWeight: 600, color: "var(--ink-2)" }}
            >
              GitHub ↗
            </a>
          </div>
        </footer>
      </body>
    </html>
  );
}
