"use client";

import { useEffect, useMemo, useRef, useState } from "react";

export type Entry = {
  title: string;
  track: string;
  idea: string;
  href: string;
  order: number;
};

const THEME_KEY = "aq-theme";

/** Ставит тему до первой отрисовки: иначе на долю секунды мигает чужая. */
export const themeScript = `(function(){try{var t=localStorage.getItem("${THEME_KEY}");if(t)document.documentElement.dataset.theme=t}catch(e){}})()`;

export default function Shell({ entries, home }: { entries: Entry[]; home: string }) {
  const [theme, setTheme] = useState<"light" | "dark" | null>(null);
  const [open, setOpen] = useState(false);
  const [query, setQuery] = useState("");
  const [cursor, setCursor] = useState(0);
  const input = useRef<HTMLInputElement>(null);

  useEffect(() => {
    const saved = document.documentElement.dataset.theme as "light" | "dark" | undefined;
    setTheme(
      saved ??
        (matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light"),
    );
  }, []);

  useEffect(() => {
    function onKey(e: KeyboardEvent) {
      if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === "k") {
        e.preventDefault();
        setOpen((was) => !was);
        return;
      }
      if (e.key === "Escape") setOpen(false);
    }
    addEventListener("keydown", onKey);
    return () => removeEventListener("keydown", onKey);
  }, []);

  useEffect(() => {
    if (open) {
      setQuery("");
      setCursor(0);
      requestAnimationFrame(() => input.current?.focus());
    }
  }, [open]);

  function flip() {
    const next = theme === "dark" ? "light" : "dark";
    setTheme(next);
    document.documentElement.dataset.theme = next;
    try {
      localStorage.setItem(THEME_KEY, next);
    } catch {
      /* приватный режим — тема просто не запомнится */
    }
  }

  const found = useMemo(() => {
    const q = query.trim().toLowerCase();
    const list = q
      ? entries.filter((e) =>
          `${e.title} ${e.track} ${e.idea}`.toLowerCase().includes(q),
        )
      : entries;
    return list.slice(0, 40);
  }, [entries, query]);

  function go(at: number) {
    const target = found[at];
    if (target) location.href = target.href;
  }

  return (
    <>
      <header
        style={{
          borderBottom: "2px solid var(--line-strong)",
          background: "var(--panel)",
          position: "sticky",
          top: 0,
          zIndex: 20,
        }}
      >
        <div
          style={{
            maxWidth: "72rem",
            margin: "0 auto",
            padding: "0.6rem clamp(0.8rem, 4vw, 2rem)",
            display: "flex",
            alignItems: "center",
            gap: "0.8rem",
          }}
        >
          <a href={home} style={{ fontWeight: 800, fontSize: "1.02rem", letterSpacing: "-0.02em" }}>
            AgentQuests
          </a>

          <button
            className="btn btn-quiet btn-small"
            onClick={() => setOpen(true)}
            style={{ marginLeft: "auto", display: "flex", gap: "0.45rem", alignItems: "center" }}
            aria-label="Открыть поиск по уровням"
          >
            Поиск
            <span className="chip">Ctrl K</span>
          </button>

          <button
            className="btn btn-quiet btn-small"
            onClick={flip}
            aria-label="Переключить тему"
            title="Переключить тему"
            style={{ minWidth: "2.6rem" }}
          >
            {theme === "dark" ? "☾" : "☀"}
          </button>
        </div>
      </header>

      {open ? (
        <div
          onClick={() => setOpen(false)}
          style={{
            position: "fixed",
            inset: 0,
            zIndex: 40,
            background: "color-mix(in srgb, var(--shadow) 55%, transparent)",
            display: "flex",
            justifyContent: "center",
            paddingTop: "10vh",
          }}
        >
          <div
            className="card"
            onClick={(e) => e.stopPropagation()}
            style={{
              width: "min(38rem, 92vw)",
              maxHeight: "70vh",
              display: "flex",
              flexDirection: "column",
              overflow: "hidden",
            }}
          >
            <input
              ref={input}
              value={query}
              placeholder="Уровень или трек…"
              onChange={(e) => {
                setQuery(e.target.value);
                setCursor(0);
              }}
              onKeyDown={(e) => {
                if (e.key === "ArrowDown") {
                  e.preventDefault();
                  setCursor((c) => Math.min(c + 1, found.length - 1));
                }
                if (e.key === "ArrowUp") {
                  e.preventDefault();
                  setCursor((c) => Math.max(c - 1, 0));
                }
                if (e.key === "Enter") go(cursor);
              }}
              style={{
                font: "inherit",
                fontWeight: 600,
                fontSize: "1rem",
                padding: "0.8rem 1rem",
                border: "none",
                borderBottom: "2px solid var(--line)",
                background: "transparent",
                color: "var(--ink)",
                outline: "none",
              }}
            />
            <div style={{ overflowY: "auto" }}>
              {found.length === 0 ? (
                <p style={{ padding: "1rem", margin: 0, color: "var(--ink-3)" }}>
                  Ничего не нашлось.
                </p>
              ) : (
                found.map((e, i) => (
                  <a
                    key={e.href}
                    href={e.href}
                    onMouseEnter={() => setCursor(i)}
                    style={{
                      display: "flex",
                      gap: "0.6rem",
                      alignItems: "baseline",
                      padding: "0.5rem 1rem",
                      background: i === cursor ? "var(--accent-soft)" : "transparent",
                      borderLeft: `4px solid ${i === cursor ? "var(--accent)" : "transparent"}`,
                    }}
                  >
                    <span className="chip">{String(e.order).padStart(2, "0")}</span>
                    <span style={{ fontWeight: 600 }}>{e.title}</span>
                    <span
                      style={{
                        marginLeft: "auto",
                        fontSize: "0.78rem",
                        color: "var(--ink-3)",
                        whiteSpace: "nowrap",
                      }}
                    >
                      {e.track}
                    </span>
                  </a>
                ))
              )}
            </div>
          </div>
        </div>
      ) : null}
    </>
  );
}
