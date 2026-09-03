"use client";

import { useState } from "react";
import Star, { type Hint } from "./Star";
import { dictFor, type Lang } from "@/lib/i18n";

/** Звезда на странице урока. Прогона здесь ещё нет, поэтому подсказки
    статические — из самого уровня. Состояние держит она сама: серверная
    страница им управлять не может. */
export default function LevelStar({ hints, lang }: { hints: Hint[]; lang: Lang }) {
  const dict = dictFor(lang);
  const [open, setOpen] = useState(false);

  return (
    <Star
      hints={hints}
      mood="idle"
      open={open}
      onOpenChange={setOpen}
      heading={dict.starHeading}
      lang={lang}
    />
  );
}
