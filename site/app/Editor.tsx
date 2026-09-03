"use client";

import { useEffect, useRef } from "react";
import { Compartment, EditorState } from "@codemirror/state";
import {
  EditorView,
  keymap,
  lineNumbers,
  highlightActiveLine,
  highlightActiveLineGutter,
  drawSelection,
} from "@codemirror/view";
import {
  defaultKeymap,
  history,
  historyKeymap,
  indentWithTab,
} from "@codemirror/commands";
import {
  HighlightStyle,
  bracketMatching,
  indentOnInput,
  indentUnit,
  syntaxHighlighting,
} from "@codemirror/language";
import { closeBrackets, closeBracketsKeymap } from "@codemirror/autocomplete";
import { python } from "@codemirror/lang-python";
import { sql } from "@codemirror/lang-sql";
import { tags } from "@lezer/highlight";

/* Раньше здесь было голое поле ввода. Половина ошибок новичка приходилась не
   на задачу, а на механику: не поставил четыре пробела, не закрыл кавычку.
   Редактор эти две ошибки просто не даёт совершить.

   Цвета берутся из переменных темы. Окно терминала тёмное в обеих темах
   сайта, поэтому набор цветов один. */

const highlight = HighlightStyle.define([
  { tag: [tags.keyword, tags.controlKeyword, tags.moduleKeyword], color: "var(--code-kw)" },
  { tag: [tags.string, tags.special(tags.string)], color: "var(--code-str)" },
  { tag: [tags.number, tags.bool, tags.null], color: "var(--code-num)" },
  { tag: [tags.comment, tags.lineComment, tags.blockComment], color: "var(--code-com)", fontStyle: "italic" },
  { tag: [tags.function(tags.variableName), tags.function(tags.propertyName)], color: "var(--code-fn)" },
  { tag: [tags.definition(tags.variableName), tags.definition(tags.propertyName)], color: "var(--code-def)" },
  { tag: [tags.operator, tags.punctuation, tags.separator, tags.bracket], color: "var(--code-op)" },
  { tag: [tags.className, tags.typeName], color: "var(--code-type)" },
  { tag: [tags.self, tags.constant(tags.variableName)], color: "var(--code-builtin)" },
]);

const look = EditorView.theme(
  {
    "&": {
      color: "var(--term-ink)",
      backgroundColor: "transparent",
      fontSize: "0.8rem",
      maxHeight: "26rem",
    },
    "&.cm-focused": { outline: "none" },
    ".cm-scroller": {
      fontFamily: "var(--mono)",
      fontWeight: "500",
      lineHeight: "1.62",
      overflow: "auto",
    },
    ".cm-content": { padding: "0.85rem 0", caretColor: "var(--accent)" },
    ".cm-line": { padding: "0 1rem" },
    ".cm-gutters": {
      backgroundColor: "transparent",
      color: "var(--code-com)",
      border: "0",
      paddingLeft: "0.7rem",
      userSelect: "none",
    },
    ".cm-activeLineGutter": { backgroundColor: "transparent", color: "var(--ink-2)" },
    ".cm-activeLine": { backgroundColor: "rgba(255, 255, 255, 0.035)" },
    ".cm-cursor, .cm-dropCursor": { borderLeftColor: "var(--accent)", borderLeftWidth: "2px" },
    "&.cm-focused .cm-selectionBackground, .cm-selectionBackground, ::selection": {
      backgroundColor: "var(--accent-soft)",
    },
    ".cm-matchingBracket, &.cm-focused .cm-matchingBracket": {
      backgroundColor: "var(--accent-soft)",
      outline: "none",
    },
  },
  { dark: true },
);

const languages: Record<string, () => ReturnType<typeof python>> = {
  py: python,
  sql: () => sql() as ReturnType<typeof python>,
};

function langFor(file: string) {
  const ext = file.split(".").pop() ?? "py";
  return (languages[ext] ?? python)();
}

export default function Editor({
  value,
  file,
  onChange,
  onRun,
}: {
  value: string;
  file: string;
  onChange: (next: string) => void;
  onRun: () => void;
}) {
  const host = useRef<HTMLDivElement | null>(null);
  const view = useRef<EditorView | null>(null);
  // Колбэки живут в ref: пересобирать редактор на каждый рендер нельзя,
  // иначе теряются курсор, выделение и история отмен. Обновляются они в
  // эффекте, а не во время рендера: отброшенный рендер иначе оставил бы в
  // ref колбэки, которых на экране нет.
  const latest = useRef({ onChange, onRun });
  useEffect(() => {
    latest.current = { onChange, onRun };
  }, [onChange, onRun]);
  const language = useRef(new Compartment());

  useEffect(() => {
    if (!host.current) return;

    const state = EditorState.create({
      doc: value,
      extensions: [
        lineNumbers(),
        highlightActiveLine(),
        highlightActiveLineGutter(),
        drawSelection(),
        history(),
        indentOnInput(),
        indentUnit.of("    "),
        bracketMatching(),
        closeBrackets(),
        syntaxHighlighting(highlight),
        language.current.of(langFor(file)),
        look,
        // Запуск обязан перехватываться раньше редактора, иначе Ctrl+Enter
        // просто вставит перевод строки.
        keymap.of([
          {
            key: "Mod-Enter",
            preventDefault: true,
            run: () => {
              latest.current.onRun();
              return true;
            },
          },
        ]),
        keymap.of([...closeBracketsKeymap, ...defaultKeymap, ...historyKeymap, indentWithTab]),
        EditorView.updateListener.of((u) => {
          if (u.docChanged) latest.current.onChange(u.state.doc.toString());
        }),
      ],
    });

    const created = new EditorView({ state, parent: host.current });
    view.current = created;
    return () => {
      created.destroy();
      view.current = null;
    };
    // Редактор создаётся один раз: значение и язык доезжают отдельными
    // эффектами ниже.
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  // Код меняют и снаружи: «вернуть заготовку», «подставить эталон», смена
  // сложности. Сверяем с текущим документом, иначе правка вернётся сама в
  // себя бесконечным кругом.
  useEffect(() => {
    const v = view.current;
    if (!v || v.state.doc.toString() === value) return;
    v.dispatch({ changes: { from: 0, to: v.state.doc.length, insert: value } });
  }, [value]);

  useEffect(() => {
    const v = view.current;
    if (!v) return;
    v.dispatch({ effects: language.current.reconfigure(langFor(file)) });
  }, [file]);

  return <div className="term-edit" ref={host} />;
}
