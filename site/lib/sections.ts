/* На сайте два раздела. Агентный курс — про инженерию ИИ-агентов, и его
   заявление «76 уровней» должно оставаться правдой. Курсы по языкам живут
   рядом, на своей витрине, со своим счётчиком.

   Понятия «раздел» в данных нет: трек знает только свой слаг. Поэтому
   принадлежность задаётся здесь, одним списком на оба места, где она нужна. */

export const COURSES: Record<string, number> = {
  "python-novice": 18,
  "python-middle": 16,
  "python-senior": 12,
  "ts-novice": 14,
  "ts-middle": 13,
  "ts-senior": 9,
};

export const COURSES_TOTAL = Object.values(COURSES).reduce((a, b) => a + b, 0);

export function isCourse(slug: string): boolean {
  return slug in COURSES;
}
