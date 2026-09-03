import type { Metadata } from "next";
import Link from "next/link";
import "./globals.css";

export const metadata: Metadata = {
  title: "AgentQuests — курс по инженерии ИИ-агентов",
  description:
    "Восемь треков, каждый уровень проверяется тестами. Теория, метод, задание — и проверка, которую не пройти чтением.",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="ru">
      <body>
        <header
          style={{
            borderBottom: "1px solid var(--line)",
            background: "var(--panel)",
            position: "sticky",
            top: 0,
            zIndex: 10,
          }}
        >
          <div
            style={{
              maxWidth: "72rem",
              margin: "0 auto",
              padding: "0.7rem clamp(1rem, 4vw, 2rem)",
              display: "flex",
              alignItems: "baseline",
              gap: "1rem",
              flexWrap: "wrap",
            }}
          >
            <Link href="/" style={{ fontWeight: 600, letterSpacing: "-0.01em" }}>
              AgentQuests
            </Link>
            <span
              style={{
                fontFamily: "var(--mono)",
                fontSize: "0.72rem",
                color: "var(--ink-3)",
              }}
            >
              инженерия агентов на задачах
            </span>
            <a
              href="https://github.com/juijitsu/agentquests"
              style={{
                marginLeft: "auto",
                fontSize: "0.82rem",
                color: "var(--ink-2)",
              }}
            >
              GitHub ↗
            </a>
          </div>
        </header>

        <main>{children}</main>

        <footer
          style={{
            borderTop: "1px solid var(--line)",
            marginTop: "4rem",
            padding: "1.5rem clamp(1rem, 4vw, 2rem)",
            fontSize: "0.8rem",
            color: "var(--ink-3)",
          }}
        >
          <div style={{ maxWidth: "72rem", margin: "0 auto" }}>
            Уровни и движок — MIT. Ни API-ключа, ни пакетов, ни сети: проверки
            работают на записанном поведении модели.
          </div>
        </footer>
      </body>
    </html>
  );
}
