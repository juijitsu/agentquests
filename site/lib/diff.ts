/* Чем заготовка отличается от решения, построчно.

   Нужно это ровно для одного: показать превращение одного в другое по шагам,
   а не вывалить готовый ответ целиком. Поэтому важна не красота разбора, а
   то, чтобы куски шли по порядку и покрывали все различия.

   Сравнение по наибольшей общей подпоследовательности: строки короткие, их
   десятки, так что квадратичная таблица здесь дешевле любой хитрости. */

export type Hunk = {
  /** Номер строки в исходном тексте, начиная с нуля. */
  at: number;
  remove: string[];
  insert: string[];
};

export function lineDiff(before: string[], after: string[]): Hunk[] {
  const n = before.length;
  const m = after.length;

  // table[i][j] — длина общей подпоследовательности хвостов before[i:] и after[j:]
  const table: number[][] = Array.from({ length: n + 1 }, () => new Array(m + 1).fill(0));
  for (let i = n - 1; i >= 0; i--) {
    for (let j = m - 1; j >= 0; j--) {
      table[i][j] =
        before[i] === after[j]
          ? table[i + 1][j + 1] + 1
          : Math.max(table[i + 1][j], table[i][j + 1]);
    }
  }

  const hunks: Hunk[] = [];
  let i = 0;
  let j = 0;
  let open: Hunk | null = null;

  const close = () => {
    if (open && (open.remove.length || open.insert.length)) hunks.push(open);
    open = null;
  };

  while (i < n || j < m) {
    if (i < n && j < m && before[i] === after[j]) {
      close();
      i++;
      j++;
      continue;
    }
    if (!open) open = { at: i, remove: [], insert: [] };
    // Идём туда, где общего хвоста больше: так различие получается минимальным.
    if (j >= m || (i < n && table[i + 1][j] >= table[i][j + 1])) {
      open.remove.push(before[i]);
      i++;
    } else {
      open.insert.push(after[j]);
      j++;
    }
  }
  close();

  return hunks;
}
