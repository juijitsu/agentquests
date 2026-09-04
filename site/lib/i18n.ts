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
  toCourses: "Ещё здесь есть курсы по языкам",
  toAgents: "К курсу по инженерии ИИ-агентов",
  coursesTitle: "Языки программирования, с нуля и дальше",
  coursesLead:
    "Три ступени на язык: старт, средний, старший. Каждая задача про свою тему, и каждая проверяется тем же способом, что и остальной сайт — прогоном, а не галочкой.",
  coursesNote:
    "Ставить ничего не нужно: питон работает прямо на странице. Установка на свою машину разобрана в первом уровне.",
  homeNote:
    "Слева — теория и задание, справа — разбор с настоящими прогонами. Решают на отдельной странице, в терминале прямо в браузере. Первый уровень открыт в каждом треке: начинать можно с любого. Дальше внутри трека по порядку — там уровень честно опирается на предыдущий. Поиск —",

  tracks: {
    foundations: "Фундамент",
    "agent-core": "Агентный трек",
    context: "Контекст",
    retrieval: "Поиск",
    evaluation: "Оценка",
    "red-team": "Красная команда",
    "python-novice": "Python: старт",
    "python-middle": "Python: средний",
    "python-senior": "Python: старший",
    "ts-novice": "TypeScript: старт",
    "ts-middle": "TypeScript: средний",
    "ts-senior": "TypeScript: старший",
  } as Record<string, string>,
  /* Отметки прогресса. Число попыток и дата — факты, посчитанные по
     засчитанным прогонам; ничего не придумано. */
  markPassed: (when: string | null, runs: number) =>
    when ? `сдан ${when}${runs ? ` · попыток: ${runs}` : ""}` : "сдан",
  markStuck: (when: string, runs: number) => `не сошлось ${when} · попыток: ${runs}`,
  markLast: (when: string, runs: number) =>
    `Прошлый раз, ${when}. Попыток: ${runs}. Не сошлось:`,

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
  stepFixNote: "Заготовка превращается в решение: лишнее уходит, нужное набирается. Открывайте после своей попытки.",
  walkPause: "Пауза",
  walkResume: "Продолжить",
  walkReplay: "Повторить",
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

  /* Живые подсказки: питон разбирает код, пока его набирают, и говорит
     по-английски своими словами. Здесь они переведены на человеческий. */
  /* Звезда отвечает на то, что случилось, а не даёт один и тот же совет.
     Каждое правило доказуемо: имя исключения из трассы, состояние вердикта,
     сравнение кода с заготовкой. */
  star: {
    crashTitle: "программа упала",
    syntaxTitle: "код не разбирается",
    noteTitle: "что видно в вашем коде",
    untouched: "Код совпадает с заготовкой: вы ещё ничего не поменяли. Заготовка рабочая и делает не то — с неё и начинают.",
    renamed: (name: string) => `В файле нет функции ${name}. Проверка ищет её по имени и другую не найдёт: верните название как было.`,
    printNoReturn: "В коде есть print и нет ни одного return. Печать показывает значение на экране, а проверка смотрит на возвращённое. Замените print на return.",
    todoLeft: "Строка с TODO ещё на месте. В ней написано, что именно надо набрать вместо неё.",
    runtime: {
      NameError: "Питон не нашёл имени. Так бывает, когда текст написан без кавычек, когда в имени опечатка или когда переменную ещё не создали.",
      TypeError: "Значения разных видов оказались в одном действии. Чаще всего складывают текст и число: число надо сперва превратить в текст через str(), либо текст в число через int().",
      AttributeError: "У значения нет такого свойства или метода. Проверьте, у чего вы его вызываете: у списка одни методы, у строки другие.",
      IndexError: "Обращение за границу списка: элемента с таким номером нет. Нумерация начинается с нуля, последний элемент имеет номер len(x) - 1.",
      KeyError: "В словаре нет такого ключа. Проверьте написание или возьмите значение через .get(ключ, запасное).",
      ValueError: "Значение не того вида. Классический случай — int() от текста, в котором не только цифры.",
      ZeroDivisionError: "Деление на ноль. Проверьте, чем делите: там оказался ноль.",
      UnboundLocalError: "Переменную читают раньше, чем ей что-то присвоили.",
      RecursionError: "Функция вызывает сама себя без конца. Нужен случай, в котором она возвращает ответ и больше не вызывает себя.",
      ModuleNotFoundError: "Такого модуля нет. В этом уровне он и не нужен: всё решается тем, что уже разобрано.",
      ImportError: "Не получилось взять имя из модуля. Проверьте, что именно вы импортируете.",
      generic: "Программа запустилась и упала. Название ошибки выше — по нему видно, что именно не сошлось.",
    },
  },

  liveAt: (line: number) => `строка ${line}`,
  live: {
    unclosed: "Скобка открыта и не закрыта. Найдите пару к последней открытой.",
    unterminatedString: "Кавычка открыта и не закрыта: строка не кончилась.",
    unterminatedTriple: "Тройная кавычка открыта и не закрыта.",
    colon: "Пропущено двоеточие в конце строки-заголовка.",
    needIndent: "Нет отступа: тело должно быть сдвинуто на четыре пробела вправо.",
    extraIndent: "Лишний отступ: эта строка сдвинута, а сдвигаться не должна.",
    mixedIndent: "Отступ не совпадает ни с одним внешним: строка сдвинута не на столько.",
    tabs: "Смешаны табы и пробелы. Оставьте что-то одно, лучше пробелы.",
    returnOutside: "return стоит снаружи функции: он должен быть внутри, с отступом.",
    assignTo: "Слева от знака равенства должно стоять имя, а не выражение.",
    invalidChar: "В коде посторонний символ: чаще всего это кавычка из текстового редактора.",
    leadingZero: "У числа не может быть ведущих нулей.",
    missingComma: "Похоже, пропущена запятая между значениями.",
    generic: "Питон не может разобрать эту строку.",
  },

  coursesHints: (done: number, total: number) => [
    {
      title: "с чего начать",
      body: "Если языка не знаете совсем — «Python: старт», первый уровень. Там же разобрана установка на Windows, macOS и Linux. Знаете основы — берите средний.",
    },
    {
      title: "ставить ли что-то",
      body: "Нет. Питон загружается прямо в браузер и работает на странице решения. Установка нужна только чтобы запускать у себя, и она не обязательна.",
    },
    {
      title: "как проверяется",
      body: "Вы пишете функцию, проверка прогоняет её на наборе случаев и показывает первое расхождение целиком: что подали, что ждали, что получили.",
    },
    {
      title: "сколько готово",
      body: `Написано уровней: ${done} из ${total}. Курсы выходят по одному, каждый целиком, а не по кусочкам.`,
    },
  ],

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
  toCourses: "There are language courses here too",
  toAgents: "Back to the AI agent engineering course",
  coursesTitle: "Programming languages, from nothing and onwards",
  coursesLead:
    "Three steps per language: from scratch, middle, senior. Every task is on its own topic, and every one is checked the way the rest of the site checks things — by running it, not by ticking a box.",
  coursesNote:
    "Nothing to install: Python runs on the page itself. Installing it on your own machine is covered by the first level.",
  homeNote:
    "Theory and task on the left, a walkthrough with real runs on the right. You solve on a separate page, in a terminal inside the browser. The first level of every track is open: start wherever you like. After that the order inside a track holds — each level genuinely builds on the one before. Search —",

  tracks: {
    foundations: "Foundations",
    "agent-core": "Agent Core",
    context: "Context",
    retrieval: "Retrieval",
    evaluation: "Evaluation",
    "red-team": "Red Team",
    "python-novice": "Python from scratch",
    "python-middle": "Python, middle",
    "python-senior": "Python, senior",
    "ts-novice": "TypeScript from scratch",
    "ts-middle": "TypeScript, middle",
    "ts-senior": "TypeScript, senior",
  },
  /* Progress marks. The attempt count and the date are facts counted from
     runs that actually finished; nothing is invented. */
  markPassed: (when: string | null, runs: number) =>
    when ? `passed ${when}${runs ? ` · attempts: ${runs}` : ""}` : "passed",
  markStuck: (when: string, runs: number) => `did not pass, ${when} · attempts: ${runs}`,
  markLast: (when: string, runs: number) =>
    `Last time, ${when}. Attempts: ${runs}. What did not hold:`,

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
  stepFixNote: "The starter turns into the solution: what is spare goes, what is needed gets typed. Open it after your own attempt.",
  walkPause: "Pause",
  walkResume: "Resume",
  walkReplay: "Replay",
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

  /* Live hints: Python parses the code as it is typed and complains in its
     own English. Here that is turned into plain language. */
  /* The star answers what actually happened instead of repeating one piece
     of advice. Every rule is provable: the exception name from the trace,
     the state of the verdict, the code compared against the starter. */
  star: {
    crashTitle: "the program crashed",
    syntaxTitle: "the code does not parse",
    noteTitle: "what your code shows",
    untouched: "The code is identical to the starter: nothing has been changed yet. The starter works and does the wrong thing — that is where you begin.",
    renamed: (name: string) => `There is no function called ${name} in the file. The check looks for it by name and will not find another: put the name back.`,
    printNoReturn: "The code has a print and not a single return. Printing shows a value on the screen, and the check looks at what is returned. Replace print with return.",
    todoLeft: "The TODO line is still there. It says exactly what to type in its place.",
    runtime: {
      NameError: "Python could not find a name. That happens when text is written without quotes, when a name has a typo, or when a variable has not been created yet.",
      TypeError: "Values of different kinds ended up in one operation. Most often text and a number are added: the number has to become text with str() first, or the text a number with int().",
      AttributeError: "The value has no such property or method. Check what you are calling it on: a list has some methods, a string has others.",
      IndexError: "Reaching past the end of a list: there is no item with that number. Numbering starts at zero, and the last item is len(x) - 1.",
      KeyError: "The dictionary has no such key. Check the spelling, or take the value with .get(key, fallback).",
      ValueError: "The value is of the wrong shape. The classic case is int() on text that is not only digits.",
      ZeroDivisionError: "Division by zero. Check what you are dividing by: it turned out to be zero.",
      UnboundLocalError: "A variable is read before anything has been assigned to it.",
      RecursionError: "The function calls itself without end. It needs a case in which it returns an answer and stops calling itself.",
      ModuleNotFoundError: "There is no such module. This level does not need one: everything is solved with what has already been covered.",
      ImportError: "A name could not be taken from the module. Check what exactly you are importing.",
      generic: "The program started and crashed. The name of the error above says what did not line up.",
    },
  },

  liveAt: (line: number) => `line ${line}`,
  live: {
    unclosed: "A bracket is open and never closed. Find the pair for the last one opened.",
    unterminatedString: "A quote is open and never closed: the string does not end.",
    unterminatedTriple: "A triple quote is open and never closed.",
    colon: "A colon is missing at the end of the header line.",
    needIndent: "No indent: the body has to be shifted four spaces to the right.",
    extraIndent: "Extra indent: this line is shifted and should not be.",
    mixedIndent: "The indent matches no outer level: the line is shifted by the wrong amount.",
    tabs: "Tabs and spaces are mixed. Keep one of them, spaces preferably.",
    returnOutside: "return sits outside a function: it has to be inside, indented.",
    assignTo: "The left of an equals sign has to be a name, not an expression.",
    invalidChar: "There is a stray character in the code: usually a quote from a word processor.",
    leadingZero: "A number cannot have leading zeros.",
    missingComma: "A comma looks to be missing between values.",
    generic: "Python cannot parse this line.",
  },

  coursesHints: (done: number, total: number) => [
    {
      title: "where to start",
      body: "If you do not know the language at all, take the first level of Python from scratch. It also covers installing on Windows, macOS and Linux. If you know the basics, take the middle course.",
    },
    {
      title: "is there anything to install",
      body: "No. Python loads straight into the browser and runs on the solve page. Installing it locally is only for running things on your own machine, and it is optional.",
    },
    {
      title: "how it is checked",
      body: "You write a function, the check runs it over a set of cases and shows the first difference in full: what went in, what was expected, what came out.",
    },
    {
      title: "how much is ready",
      body: `Levels written: ${done} of ${total}. Courses ship one at a time, each one whole rather than in pieces.`,
    },
  ],

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
