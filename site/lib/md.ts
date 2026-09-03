import { marked, type Tokens } from "marked";

/* Разбор урока стал длинным, и по нему надо уметь ходить: ссылка «в конце
   этого урока» должна куда-то вести. Стандартный marked заголовкам id не
   ставит, поэтому ставим сами.

   Слаг строится из текста заголовка: нижний регистр, всё кроме букв, цифр,
   пробелов и дефисов выкидывается, пробелы становятся дефисами. Кириллица
   остаётся кириллицей — в адресе её кодирует браузер, и якорь всё равно
   находится. */

function slug(text: string): string {
  return text
    .replace(/<[^>]+>/g, "")
    .toLowerCase()
    .replace(/[^\p{L}\p{N}\s-]/gu, "")
    .trim()
    .replace(/\s+/g, "-");
}

marked.use({
  renderer: {
    heading(this: { parser: { parseInline: (t: Tokens.Generic[]) => string } }, token: Tokens.Heading) {
      const inner = this.parser.parseInline(token.tokens);
      return `<h${token.depth} id="${slug(token.text)}">${inner}</h${token.depth}>\n`;
    },
  },
});

/** Единственная точка рендера markdown на сайте. */
export function render(md: string): string {
  return marked.parse(md, { async: false }) as string;
}
