"use client";

import { useEffect, useMemo, useState, useSyncExternalStore } from "react";
import Terminal from "./Terminal";
import { lineDiff } from "@/lib/diff";
import { dictFor, type Lang } from "@/lib/i18n";

/* Третий шаг разбора раньше вываливал решение целиком. Готовый ответ мало
   чему учит: из него не видно, что код пишут по частям, а не достают
   готовым.

   Здесь заготовка превращается в решение на глазах: лишние строки уходят по
   одной, новые набираются посимвольно. Кадры считаются заранее и сложены в
   массив, поэтому перемотка — это прыжок по номеру, а не отдельная машина
   состояний. */

const CHAR = 16;
const LINE_GONE = 90;
const HUNK_GAP = 420;
/* На больших правках анимация превращается в долгое кино, которое никто не
   досмотрит. Тогда честнее показать решение как есть. */
const MAX_FRAMES = 1400;

type Frame = { text: string; wait: number };

function build(before: string, after: string): Frame[] | null {
  const a = before.split("\n");
  const b = after.split("\n");
  const hunks = lineDiff(a, b);
  if (!hunks.length) return null;

  const doc = [...a];
  const frames: Frame[] = [{ text: doc.join("\n"), wait: HUNK_GAP }];
  // Номера в кусках указывают на исходный текст, а правим мы уже изменённый,
  // поэтому сдвиг копится от куска к куску.
  let shift = 0;

  for (const hunk of hunks) {
    const at = hunk.at + shift;

    for (let k = 0; k < hunk.remove.length; k++) {
      doc.splice(at, 1);
      frames.push({ text: doc.join("\n"), wait: LINE_GONE });
    }

    for (let k = 0; k < hunk.insert.length; k++) {
      doc.splice(at + k, 0, "");
      const full = hunk.insert[k];
      for (let c = 1; c <= full.length; c++) {
        doc[at + k] = full.slice(0, c);
        frames.push({ text: doc.join("\n"), wait: CHAR });
      }
      if (full.length === 0) frames.push({ text: doc.join("\n"), wait: LINE_GONE });
    }

    shift += hunk.insert.length - hunk.remove.length;
    frames[frames.length - 1].wait = HUNK_GAP;
    if (frames.length > MAX_FRAMES) return null;
  }

  return frames;
}

/** Настройку «меньше движения» читаем подпиской, а не в эффекте: на сервере
    её нет, а установка состояния из эффекта тянет лишний рендер. */
function useCalmMotion(): boolean {
  return useSyncExternalStore(
    (notify) => {
      const query = matchMedia("(prefers-reduced-motion: reduce)");
      query.addEventListener("change", notify);
      return () => query.removeEventListener("change", notify);
    },
    () => matchMedia("(prefers-reduced-motion: reduce)").matches,
    () => false,
  );
}

export default function Retype({
  from,
  to,
  title,
  lang,
}: {
  from: string;
  to: string;
  title: string;
  lang: Lang;
}) {
  const dict = dictFor(lang);
  const frames = useMemo(() => build(from, to), [from, to]);
  const calm = useCalmMotion();
  const [at, setAt] = useState(0);
  const [playing, setPlaying] = useState(true);

  // «Меньше движения» — это просьба не двигать самому, а не отказ от показа
  // по шагам. Поэтому при ней проводка остаётся, но ждёт нажатия.
  const [nudged, setNudged] = useState(false);
  const live = frames !== null;
  const last = frames ? frames.length - 1 : 0;
  const done = at >= last;
  const rolling = playing && (nudged || !calm);

  useEffect(() => {
    if (!live || !rolling || done) return;
    const timer = setTimeout(() => setAt((i) => i + 1), frames[at].wait);
    return () => clearTimeout(timer);
  }, [live, rolling, done, frames, at]);

  if (!live) return <Terminal title={title} output={to.trimEnd()} />;

  return (
    <div style={{ display: "flex", flexDirection: "column", gap: "0.5rem" }}>
      <Terminal title={title} output={frames[at].text.trimEnd()} />
      <div style={{ display: "flex", gap: "0.4rem", alignItems: "center", flexWrap: "wrap" }}>
        <button
          className="btn btn-small btn-quiet"
          onClick={() => {
            setNudged(true);
            if (done) {
              setAt(0);
              setPlaying(true);
            } else {
              // Именно по факту движения, а не переключением: при «меньше
              // движения» playing уже true, и слепой переворот выключал бы
              // проводку вместо того, чтобы её запустить.
              setPlaying(!rolling);
            }
          }}
        >
          {done ? dict.walkReplay : rolling ? dict.walkPause : dict.walkResume}
        </button>
        <div
          aria-hidden
          style={{ flex: 1, height: 3, borderRadius: 2, background: "var(--line)" }}
        >
          <div
            style={{
              width: `${Math.round((at / last) * 100)}%`,
              height: "100%",
              borderRadius: 2,
              background: "var(--accent)",
            }}
          />
        </div>
      </div>
    </div>
  );
}
