"use client";

import { useState } from "react";
import Star, { type Hint } from "./Star";

/** Звезда на странице урока. Прогона здесь ещё нет, поэтому подсказки
    статические — из самого уровня. Состояние держит она сама: серверная
    страница им управлять не может. */
export default function LevelStar({ hints }: { hints: Hint[] }) {
  const [open, setOpen] = useState(false);

  return (
    <Star
      hints={hints}
      mood="idle"
      open={open}
      onOpenChange={setOpen}
      heading="Чем помочь?"
    />
  );
}
