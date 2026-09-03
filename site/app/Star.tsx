"use client";

import { useEffect, useId, useRef, useState } from "react";
import { dictFor, type Lang } from "@/lib/i18n";

export type Hint = { title: string; body: string; html?: boolean };
export type Mood = "idle" | "think" | "cheer" | "sad";

/* Пятиконечная звезда: внешние вершины на радиусе 41, внутренние на 19,
   первая смотрит вверх. Углы посчитаны, а не подобраны на глаз — иначе лучи
   выходят разной длины и это видно. Скруглены не дугами, а обводкой того же
   цвета со скруглением стыков: одна фигура вместо двадцати команд пути. */
const STAR =
  "M50 9 L61.17 34.63 L88.99 37.33 L68.07 55.87 L74.1 83.17 " +
  "L50 69 L25.9 83.17 L31.93 55.87 L11.01 37.33 L38.83 34.63 Z";

/** Четырёхлучевой блик. Вогнутые стороны — иначе это просто крестик. */
const SPARK = "M0 -7 Q1.2 -1.2 7 0 Q1.2 1.2 0 7 Q-1.2 1.2 -7 0 Q-1.2 -1.2 0 -7 Z";

const SPARKS = [
  { x: 14, y: 20, s: 0.85, d: "0s" },
  { x: 87, y: 26, s: 0.6, d: "0.7s" },
  { x: 78, y: 79, s: 0.7, d: "1.4s" },
];

function Face({ mood }: { mood: Mood }) {
  const eyes =
    mood === "cheer" ? (
      <>
        <path className="star-line" d="M34.8 46.6 Q41 38.8 47.2 46.6" />
        <path className="star-line" d="M52.8 46.6 Q59 38.8 65.2 46.6" />
      </>
    ) : (
      <g className="star-eyes">
        <ellipse className="star-ink" cx="41" cy="45" rx="4.4" ry="5.8" />
        <ellipse className="star-ink" cx="59" cy="45" rx="4.4" ry="5.8" />
        <circle className="star-glint" cx="42.6" cy="42.6" r="1.5" />
        <circle className="star-glint" cx="60.6" cy="42.6" r="1.5" />
      </g>
    );

  const mouth =
    mood === "cheer" ? (
      <path className="star-ink" d="M40.5 55.5 Q50 66.5 59.5 55.5 Z" />
    ) : mood === "think" ? (
      <ellipse className="star-ink" cx="50" cy="58" rx="3" ry="3.4" />
    ) : mood === "sad" ? (
      <path className="star-line" d="M43 60.5 Q50 55.5 57 60.5" />
    ) : (
      <path className="star-line" d="M43 56 Q50 62.5 57 56" />
    );

  return (
    <g>
      {eyes}
      {mouth}
    </g>
  );
}

type Props = {
  hints: Hint[];
  mood: Mood;
  open: boolean;
  onOpenChange: (open: boolean) => void;
  /** Что звезда говорит первой строкой облачка. */
  heading: string;
  lang: Lang;
};

export default function Star({ hints, mood, open, onOpenChange, heading, lang }: Props) {
  const dict = dictFor(lang);
  const uid = useId();
  const grad = `star-body-${uid}`;
  // Подсказки выдаются по одной: облачко, вываливающее всё разом, решает
  // уровень за ученика, а этого уровни не переживут.
  const [shown, setShown] = useState(1);
  const dock = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (open) setShown(1);
  }, [open, hints]);

  useEffect(() => {
    if (!open) return;
    function onKey(e: KeyboardEvent) {
      if (e.key === "Escape") onOpenChange(false);
    }
    function onDown(e: MouseEvent) {
      if (!dock.current?.contains(e.target as Node)) onOpenChange(false);
    }
    addEventListener("keydown", onKey);
    addEventListener("mousedown", onDown);
    return () => {
      removeEventListener("keydown", onKey);
      removeEventListener("mousedown", onDown);
    };
  }, [open, onOpenChange]);

  const face: Mood = open ? "think" : mood;

  return (
    <div className="star-dock" ref={dock}>
      {open ? (
        <div className="star-bubble" role="dialog" aria-label="Подсказки">
          <div className="star-bubble-head">
            <strong>{heading}</strong>
            <button
              className="star-close"
              onClick={() => onOpenChange(false)}
              aria-label={dict.starClose}
            >
              ✕
            </button>
          </div>

          <div className="star-bubble-body">
            {hints.slice(0, shown).map((hint) => (
              <div key={hint.title} className="star-hint">
                <span className="chip">{hint.title}</span>
                {hint.html ? (
                  <div className="prose" dangerouslySetInnerHTML={{ __html: hint.body }} />
                ) : (
                  <p>{hint.body}</p>
                )}
              </div>
            ))}
          </div>

          {shown < hints.length ? (
            <button className="btn btn-small" onClick={() => setShown((n) => n + 1)}>
              {dict.starMore(hints.length - shown)}
            </button>
          ) : (
            <p className="star-done">{dict.starNoMore}</p>
          )}
        </div>
      ) : null}

      {/* Хвост облачка: он и делает знак размышления, без него это просто окно. */}
      <div className={`star-tail${open ? " star-tail-on" : ""}`} aria-hidden="true">
        <span />
        <span />
        <span />
      </div>

      <button
        className={`star-button${open ? " star-thinking" : ""}`}
        onClick={() => onOpenChange(!open)}
        aria-expanded={open}
        aria-label={open ? dict.hideHints : dict.starShow}
        title={open ? dict.hideHints : dict.starStuck}
      >
        <svg viewBox="0 0 100 100" className="star-svg" aria-hidden="true">
          <defs>
            <linearGradient id={grad} x1="0" y1="0" x2="0.25" y2="1">
              <stop offset="0" stopColor="#ffe792" />
              <stop offset="0.5" stopColor="#ffc53a" />
              <stop offset="1" stopColor="#f2990d" />
            </linearGradient>
          </defs>
          {/* Место задаёт атрибут группы, а не CSS: анимация внутри тоже
              крутит transform, и одно затёрло бы другое. */}
          {SPARKS.map((s) => (
            <g key={s.d} transform={`translate(${s.x} ${s.y}) scale(${s.s})`}>
              <path className="star-spark" d={SPARK} style={{ animationDelay: s.d }} />
            </g>
          ))}
          <path
            className="star-shape"
            d={STAR}
            fill={`url(#${grad})`}
            stroke={`url(#${grad})`}
          />
          <Face mood={face} />
        </svg>
      </button>
    </div>
  );
}
