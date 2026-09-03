"use client";

import { useEffect, useState } from "react";
import { blockedBy, levelOpen, readDone, type Outline } from "./progress";

type Props = {
  outline: Outline;
  levelId: string;
  titles: Record<string, { title: string; href: string }>;
  children: React.ReactNode;
};

export default function Gate({ outline, levelId, titles, children }: Props) {
  const [state, setState] = useState<"checking" | "open" | "locked">("checking");
  const [need, setNeed] = useState<string | null>(null);

  useEffect(() => {
    const done = readDone();
    if (levelOpen(outline, levelId, done)) {
      setState("open");
      return;
    }
    setNeed(blockedBy(outline, levelId, done));
    setState("locked");
  }, [outline, levelId]);

  // Пока не прочитан прогресс, показываем содержимое: мигать замком на
  // каждой загрузке хуже, чем на долю секунды показать лишнее.
  if (state !== "locked") return <>{children}</>;

  const target = need ? titles[need] : undefined;

  return (
    <div
      style={{
        maxWidth: "40rem",
        margin: "0 auto",
        padding: "clamp(3rem, 10vw, 6rem) clamp(1rem, 4vw, 2rem)",
        textAlign: "center",
      }}
    >
      <div style={{ fontSize: "2.4rem", lineHeight: 1 }}>🔒</div>
      <h1
        style={{
          fontSize: "1.6rem",
          fontWeight: 750,
          letterSpacing: "-0.02em",
          margin: "0.8rem 0 0.5rem",
        }}
      >
        Уровень ещё закрыт
      </h1>
      <p style={{ color: "var(--ink-2)", margin: "0 0 1.4rem" }}>
        Порядок здесь не формальность: каждый уровень опирается на предыдущий.
        {target ? " Откройте его, пройдя вот этот." : ""}
      </p>
      {target ? (
        <a className="btn btn-go" href={target.href}>
          {target.title} →
        </a>
      ) : null}
    </div>
  );
}
