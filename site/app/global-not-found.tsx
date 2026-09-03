import type { Metadata } from "next";
import { themeScript } from "./Shell";
import { dictFor } from "@/lib/i18n";
import "./globals.css";

/* Корневых макетов два, по одному на язык, поэтому собрать 404 из layout.js
   и not-found.js не из чего: у неподошедшего адреса нет языка. Next держит
   для этого случая global-not-found — файл в обход макетов, отдающий целый
   документ. Отсюда и собственный импорт стилей, и собственный скрипт темы.

   Язык документа — русский, как у корня сайта. Английская половина помечена
   lang="en" отдельно, иначе читалка озвучит её по-русски. */

const base = process.env.NEXT_PUBLIC_BASE_PATH ?? "";
const ru = dictFor("ru");
const en = dictFor("en");

export const metadata: Metadata = {
  title: `404 — ${ru.siteTitle}`,
  description: ru.notFoundBody,
};

function Half({
  lang,
  title,
  body,
  home,
  href,
}: {
  lang: "ru" | "en";
  title: string;
  body: string;
  home: string;
  href: string;
}) {
  return (
    <section lang={lang} style={{ marginTop: "2rem" }}>
      <h1
        style={{
          fontSize: "1.25rem",
          fontWeight: 750,
          letterSpacing: "-0.02em",
          margin: "0 0 0.4rem",
        }}
      >
        {title}
      </h1>
      <p style={{ color: "var(--ink-2)", margin: "0 0 0.8rem" }}>{body}</p>
      <a href={href} style={{ fontWeight: 600 }}>
        {home} →
      </a>
    </section>
  );
}

export default function GlobalNotFound() {
  return (
    <html lang={ru.htmlLang} suppressHydrationWarning>
      <head>
        <script dangerouslySetInnerHTML={{ __html: themeScript }} />
      </head>
      <body>
        <main
          style={{
            maxWidth: "34rem",
            margin: "0 auto",
            padding: "clamp(3rem, 12vh, 7rem) clamp(1rem, 4vw, 2rem)",
          }}
        >
          <p
            style={{
              fontFamily: "var(--mono)",
              fontSize: "3.2rem",
              fontWeight: 700,
              lineHeight: 1,
              letterSpacing: "-0.04em",
              color: "var(--ink-3)",
              margin: 0,
            }}
          >
            404
          </p>

          <Half
            lang="ru"
            title={ru.notFoundTitle}
            body={ru.notFoundBody}
            home={ru.notFoundHome}
            href={`${base}/`}
          />

          <hr
            style={{
              border: 0,
              borderTop: "2px solid var(--line)",
              margin: "2rem 0 0",
            }}
          />

          <Half
            lang="en"
            title={en.notFoundTitle}
            body={en.notFoundBody}
            home={en.notFoundHome}
            href={`${base}/en/`}
          />
        </main>
      </body>
    </html>
  );
}
