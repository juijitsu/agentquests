/* Два языка интерфейса. Русский живёт без префикса — старые адреса не
   ломаются, — английский под /en/.

   Уроки пока написаны только по-русски. Слой контента уже умеет читать
   content/en, поэтому английский урок начинает работать в тот момент,
   когда файл появляется; пока его нет, страница честно об этом говорит. */

export const LANGS = ["ru", "en"] as const;
export type Lang = (typeof LANGS)[number];

/** Адрес страницы на нужном языке: русский без префикса, английский с /en. */
export function at(lang: Lang, base: string, path: string): string {
  const clean = path.startsWith("/") ? path : `/${path}`;
  return `${base}${lang === "en" ? "/en" : ""}${clean}`;
}

const ru = {
  htmlLang: "ru",
  other: "en" as Lang,
  otherLabel: "EN",
  switchTitle: "Switch to English",

  siteTitle: "AgentQuests — курс по инженерии ИИ-агентов",
  siteDescription:
    "Восемь треков, каждый уровень проверяется тестами. Теория, метод, задание — и проверка, которую не пройти чтением.",

  search: "Поиск",
  searchPlaceholder: "Уровень, трек или суть",
  nothingFound: "Ничего не нашлось.",
  toLight: "Светлая тема",
  toDark: "Тёмная тема",

  footerLicense: "Уровни и движок — MIT.",
  footerOffline: "Ни ключа, ни пакетов, ни сети.",

  heroTitle: "Курс, который нельзя пройти чтением",
  heroLead:
    "Уровень даёт теорию, затем метод, затем задание. Следующий открывается, когда проходят тесты, — а не когда вы дочитали.",
  chipDone: (done: number, total: number) => `готово уровней: ${done} из ${total}`,
  chipBrowser: "запуск прямо в браузере",
  homeNote:
    "Слева — теория и задание, справа — разбор с настоящими прогонами. Решают на отдельной странице, в терминале прямо в браузере. Первый уровень открыт в каждом треке: начинать можно с любого. Дальше внутри трека по порядку — там уровень честно опирается на предыдущий. Поиск —",

  tracks: {
    foundations: "Фундамент",
    "agent-core": "Агентный трек",
    context: "Контекст",
    retrieval: "Поиск",
    evaluation: "Оценка",
    "red-team": "Красная команда",
  } as Record<string, string>,
  passed: (n: number) => `пройдено ${n}`,
  firstOpen: "первый уровень открыт — начинать можно отсюда",

  gateTitle: "Уровень ещё закрыт",
  gateBody: "Порядок здесь не формальность: каждый уровень опирается на предыдущий.",
  gateBodyMore: " Откройте его, пройдя вот этот.",

  allTracks: "← все треки",
  minutes: "мин",
  backToLesson: "← к разбору",

  /* Заголовки внутри задания. По ним со страницы снимается таблица сложностей
     и достаётся подсказка, поэтому в переводе они обязаны совпадать с тем,
     что написано в самих файлах. */
  taskTiers: "## Выберите сложность",
  taskHint: "## Если застряли",

  notTranslatedTitle: "",
  notTranslatedBody: "",

  // Страница 404 не принадлежит ни одному языку: на неё попадают по
  // опечатке в любом адресе. Поэтому она печатает обе строки сразу.
  notFoundTitle: "Такой страницы нет",
  notFoundBody: "Адрес набран с опечаткой или уровень ещё не написан.",
  notFoundHome: "К списку треков",

  otherLangTitle: (lang: string) => `Уровень на ${lang}`,
  otherLangBody:
    "В браузере он не запускается: там живёт только Python. Значит запуск один — в своей консоли, из корня репозитория.",
  ownTerminal: "в своём терминале",

  walkTitle: "Разбор",
  stepOf: (at_: number, total: number) => `шаг ${at_} из ${total}`,
  checkWindow: "проверка",
  stepStarterTitle: "Заготовка",
  stepStarterNote: "С этого кода начинают. Он рабочий и делает не то.",
  stepOutputTitle: "Что она выдаёт",
  stepOutputNote: "Настоящий прогон заготовки — то же, что покажет вам проверка.",
  stepFixTitle: "Что меняется",
  stepFixNote: "Решение целиком. Открывайте после своей попытки.",
  stepDoneTitle: "Итог",
  stepDoneNote: "Прогон решения. Все условия сходятся.",
  revealBody: "Дальше — решение. Сперва попробуйте сами: подсказки в теории хватает.",
  revealButton: "Всё равно показать",
  back: "← Назад",
  next: "Дальше →",
  solveCta: "Решать этот уровень →",

  tierTitles: { novice: "Новичок", advanced: "Продвинутый", pro: "Профессионал" },
  tierNotes: {
    novice: "место правки помечено TODO",
    advanced: "тот же код без указания, где править",
    pro: "только контракт, решение с нуля",
  },
  editorTitle: (file: string) => `${file} — правьте здесь`,
  run: "Запустить",
  stop: "Прервать",
  resetStarter: "Вернуть заготовку",
  fillSolution: "Подставить эталон",
  idleOutput: "Нажмите «Запустить» — вывод появится здесь.",
  preparing: "готовлю прогон",
  interrupted: "^C  прогон прерван вручную",
  workerFailed: (why: string) => `воркер не запустился: ${why}`,
  unknownError: "неизвестная ошибка",
  passedTitle: "Уровень пройден",
  failedTitle: "Пока не сходится",
  passedNote: "Следующий уровень открыт.",
  failedNote: "Каждая строка с ✗ называет своё условие.",
  askStar: "Спросить звезду",
  hideHints: "Убрать подсказки",

  starHeading: "Чем помочь?",
  starHeadingDone: "Готово!",
  starMore: (left: number) => `Ещё подсказку (${left})`,
  starNoMore: "Больше подсказок у меня нет.",
  starClose: "Закрыть подсказки",
  starShow: "Показать подсказки",
  starStuck: "Застряли? Нажмите",

  hStartTitle: "с чего начать",
  hStartBody:
    "Проверка ещё не запускалась. Запустите заготовку как есть — она назовёт условия, которые не сошлись. Это быстрее, чем вычитывать код глазами.",
  hDoneTitle: "всё сошлось",
  hDoneBody:
    "Условия выполнены, уровень засчитан. Следующий уже открыт — ссылка в зелёной полосе.",
  hOneFailed: "не сошлось условие",
  hManyFailed: "не сошлись условия",
  hNoChecksTitle: "прогон не дошёл до проверки",
  hNoChecksBody:
    "Условия даже не считались. Смотрите вывод целиком: там сказано, на чём всё оборвалось.",
  hEngineTitle: "что говорит движок",
  hLevelTitle: "подсказка уровня",
  hWhereTitle: "куда ещё посмотреть",
  hWhereNovice: "Сложность «Новичок» показывает место правки: нужная строка помечена TODO. ",
  hWhereBody:
    "В разборе рядом с уроком второй шаг показывает, что выдаёт заготовка, третий — решение целиком.",

  hAboutTitle: "про что уровень",
  hSolveTitle: "где решать",
  hSolveBrowser:
    "Кнопка «Решать этот уровень» открывает страницу с терминалом прямо в браузере. Заготовка там уже лежит — её и правят.",
  hSolveConsole: (command: string) =>
    `Этот уровень в браузере не идёт. Запуск в своей консоли, из корня репозитория: ${command}`,

  homeHints: (done: number, total: number) => [
    {
      title: "с чего начать",
      body: "Первый уровень открыт в каждом треке — начинать можно с любого. Нужны агенты с нуля — берите «Фундамент». Интересен поиск или оценка — идите прямо туда.",
    },
    {
      title: "как устроен уровень",
      body: "Слева теория, метод и задание. Справа разбор из четырёх шагов, и вывод в нём не пересказан, а снят с настоящего прогона. Решают на отдельной странице, в терминале прямо в браузере.",
    },
    {
      title: "что нужно поставить",
      body: "Ничего: ни ключа, ни пакетов, ни сети. Проверку считает Python, запущенный в самом браузере.",
    },
    {
      title: "почему часть уровней с замком",
      body: `Внутри трека порядок обязателен: уровень опирается на предыдущий. Замок снимается, когда предыдущий пройден. Готово уровней: ${done} из ${total}.`,
    },
    {
      title: "если потерялись",
      body: "Ctrl+K открывает поиск по всем уровням — по названию, треку и смыслу.",
    },
  ],
};

export type Dict = typeof ru;

const en: Dict = {
  htmlLang: "en",
  other: "ru",
  otherLabel: "RU",
  switchTitle: "Перейти на русский",

  siteTitle: "AgentQuests — a course in AI agent engineering",
  siteDescription:
    "Eight tracks, every level checked by tests. Theory, method, task — and a check you cannot pass by reading.",

  search: "Search",
  searchPlaceholder: "Level, track or idea",
  nothingFound: "Nothing found.",
  toLight: "Light theme",
  toDark: "Dark theme",

  footerLicense: "Levels and engine — MIT.",
  footerOffline: "No key, no packages, no network.",

  heroTitle: "A course you cannot finish by reading",
  heroLead:
    "A level gives you theory, then method, then a task. The next one opens when the tests pass — not when you reach the end of the page.",
  chipDone: (done: number, total: number) => `levels ready: ${done} of ${total}`,
  chipBrowser: "runs in your browser",
  homeNote:
    "Theory and task on the left, a walkthrough with real runs on the right. You solve on a separate page, in a terminal inside the browser. The first level of every track is open: start wherever you like. After that the order inside a track holds — each level genuinely builds on the one before. Search —",

  tracks: {
    foundations: "Foundations",
    "agent-core": "Agent Core",
    context: "Context",
    retrieval: "Retrieval",
    evaluation: "Evaluation",
    "red-team": "Red Team",
  },
  passed: (n: number) => `${n} done`,
  firstOpen: "first level is open — you can start here",

  gateTitle: "This level is still locked",
  gateBody: "The order is not a formality: each level builds on the one before it.",
  gateBodyMore: " Pass that one to open this.",

  allTracks: "← all tracks",
  minutes: "min",
  backToLesson: "← back to lesson",

  taskTiers: "## Choose a difficulty",
  taskHint: "## If you get stuck",

  notTranslatedTitle: "Lesson is in Russian",
  notTranslatedBody:
    "The interface is English, but this lesson has not been translated yet — the text below and the checker output are Russian.",

  notFoundTitle: "No such page",
  notFoundBody: "The address has a typo, or the level is not written yet.",
  notFoundHome: "Back to the tracks",

  otherLangTitle: (lang: string) => `A ${lang} level`,
  otherLangBody:
    "It does not run in the browser: only Python lives there. So there is one way to run it — your own console, from the repository root.",
  ownTerminal: "in your own terminal",

  walkTitle: "Walkthrough",
  stepOf: (at_: number, total: number) => `step ${at_} of ${total}`,
  checkWindow: "check",
  stepStarterTitle: "Starter",
  stepStarterNote: "This is where you begin. It runs, and it does the wrong thing.",
  stepOutputTitle: "What it prints",
  stepOutputNote: "A real run of the starter — exactly what the check will show you.",
  stepFixTitle: "What changes",
  stepFixNote: "The whole solution. Open it after your own attempt.",
  stepDoneTitle: "Result",
  stepDoneNote: "A run of the solution. Every condition holds.",
  revealBody: "The solution comes next. Try it yourself first — the theory tells you enough.",
  revealButton: "Show it anyway",
  back: "← Back",
  next: "Next →",
  solveCta: "Solve this level →",

  tierTitles: { novice: "Novice", advanced: "Advanced", pro: "Pro" },
  tierNotes: {
    novice: "the line to change is marked TODO",
    advanced: "same code, no marker to tell you where",
    pro: "the contract only, write it from scratch",
  },
  editorTitle: (file: string) => `${file} — edit here`,
  run: "Run",
  stop: "Stop",
  resetStarter: "Reset to starter",
  fillSolution: "Paste the solution",
  idleOutput: "Press Run — the output shows up here.",
  preparing: "getting the run ready",
  interrupted: "^C  run stopped by hand",
  workerFailed: (why: string) => `the worker did not start: ${why}`,
  unknownError: "unknown error",
  passedTitle: "Level passed",
  failedTitle: "Not there yet",
  passedNote: "The next level is open.",
  failedNote: "Every ✗ line names the condition it checks.",
  askStar: "Ask the star",
  hideHints: "Hide hints",

  starHeading: "Need a hand?",
  starHeadingDone: "Nice one!",
  starMore: (left: number) => `One more hint (${left})`,
  starNoMore: "That is everything I know.",
  starClose: "Close hints",
  starShow: "Show hints",
  starStuck: "Stuck? Give me a click",

  hStartTitle: "where to start",
  hStartBody:
    "You have not run the check yet. Run the starter as it is — it will name the conditions that do not hold. That beats reading the code line by line.",
  hDoneTitle: "everything holds",
  hDoneBody: "Every condition passed and the level is counted. The next one is open — the link is in the green bar.",
  hOneFailed: "one condition failed",
  hManyFailed: "conditions that failed",
  hNoChecksTitle: "the run never reached the checks",
  hNoChecksBody:
    "The conditions were never evaluated. Read the whole output: it says where things stopped.",
  hEngineTitle: "what the engine says",
  hLevelTitle: "hint from the level",
  hWhereTitle: "where else to look",
  hWhereNovice: "The Novice tier marks the spot: the line you need is tagged TODO. ",
  hWhereBody:
    "In the walkthrough beside the lesson, step two shows what the starter prints and step three shows the whole solution.",

  hAboutTitle: "what this level is about",
  hSolveTitle: "where to solve it",
  hSolveBrowser:
    "The “Solve this level” button opens a page with a terminal right in the browser. The starter is already loaded there — that is what you edit.",
  hSolveConsole: (command: string) =>
    `This level does not run in the browser. Run it in your own console, from the repository root: ${command}`,

  homeHints: (done: number, total: number) => [
    {
      title: "where to start",
      body: "The first level of every track is open — start wherever you like. Want agents from the ground up? Take Foundations. Curious about retrieval or evaluation? Go straight there.",
    },
    {
      title: "how a level works",
      body: "Theory, method and task on the left. On the right a four-step walkthrough whose output is not paraphrased — it is captured from a real run. You solve on a separate page, in a terminal inside the browser.",
    },
    {
      title: "what you need to install",
      body: "Nothing: no key, no packages, no network. The check is computed by Python running inside the browser itself.",
    },
    {
      title: "why some levels are locked",
      body: `Inside a track the order holds: each level builds on the one before. The lock lifts once you pass that one. Levels ready: ${done} of ${total}.`,
    },
    {
      title: "if you get lost",
      body: "Ctrl+K opens search across every level — by title, track and idea.",
    },
  ],
};

export const STRINGS: Record<Lang, Dict> = { ru, en };

export function dictFor(lang: Lang): Dict {
  return STRINGS[lang];
}
