import Shell, { themeScript, type Entry } from "../Shell";
import { allLevels } from "@/lib/content";
import { at, dictFor, type Lang } from "@/lib/i18n";
import "../globals.css";

const base = process.env.NEXT_PUBLIC_BASE_PATH ?? "";

/** Общее тело обоих корневых макетов. Их два, потому что `<html lang>` может
    задать только корневой макет, а язык страницы обязан быть настоящим:
    английский текст под lang="ru" читалка озвучит по-русски. */
export default function Root({ lang, children }: { lang: Lang; children: React.ReactNode }) {
  const dict = dictFor(lang);
  const entries: Entry[] = allLevels(lang).map((l) => ({
    title: l.title,
    track: l.track,
    idea: l.idea,
    order: l.order,
    href: at(lang, base, `/${l.trackSlug}/${l.slug}/`),
  }));

  return (
    // Скрипт темы правит data-theme до гидратации — расхождение здесь
    // ожидаемое, и подавляется именно на этом узле.
    <html lang={dict.htmlLang} suppressHydrationWarning>
      <head>
        <script dangerouslySetInnerHTML={{ __html: themeScript }} />
      </head>
      <body>
        <Shell entries={entries} lang={lang} home={at(lang, base, "/")} />
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
            <span>{dict.footerLicense}</span>
            <span>{dict.footerOffline}</span>
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
