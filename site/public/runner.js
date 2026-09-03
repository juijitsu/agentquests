/* Прогон уровня в браузере. Живёт в воркере, чтобы бесконечный цикл в
   решении ученика можно было прервать: главный поток делает terminate().

   Вердикт считает тот же engine/check.py, что и командная строка, —
   второй реализации в проекте нет.

   Рантайм лежит рядом, а не на чужом CDN: воркеру нельзя грузить скрипт
   с другого origin, да и сторонний хост однажды отвалится.

   Воркер модульный: классические поддерживаются не везде, модульные —
   во всех современных браузерах. */

import { loadPyodide } from "./pyodide/pyodide.mjs";

const PYODIDE = new URL("./pyodide/", import.meta.url).href;

let python = null;
let runs = 0;

/* Каждый прогон получает свежий каталог и чистые имена модулей. Иначе
   интерпретатор, живущий всю жизнь вкладки, отдаст закэшированный код
   прошлого запуска — молча и без ошибки. */
const BOOTSTRAP = `
import importlib, os, sys, traceback


def run_level(run_id, kit_src, check_src, scenario_src, agent_src, agent_name, where):
    work = "/run%d" % run_id
    os.makedirs(work + "/engine", exist_ok=True)

    def put(path, text):
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(text)

    put(work + "/engine/kit.py", kit_src)
    put(work + "/aq_check.py", check_src)
    put(work + "/scenario.py", scenario_src)

    is_sql = agent_name.endswith(".sql")
    if not is_sql:
        put(work + "/agent.py", agent_src)

    for name in ("scenario", "agent", "engine", "engine.kit", "aq_check"):
        sys.modules.pop(name, None)
    sys.path.insert(0, work)
    importlib.invalidate_caches()

    try:
        check = importlib.import_module("aq_check")
        scenario = importlib.import_module("scenario")
        if is_sql:
            def load_agent():
                return agent_src
        else:
            def load_agent():
                return importlib.import_module("agent")
        lines, code = check.report(scenario, load_agent, where)
        return "\\n".join(lines), code
    except Exception:
        return traceback.format_exc(), 2
    finally:
        if work in sys.path:
            sys.path.remove(work)


def check_syntax(src):
    """Разбирает исходник, не исполняя его.

    Настоящий компилятор питона, а не догадка по тексту: ложных срабатываний
    в подсказке новичку быть не должно. Дальше синтаксиса он не видит —
    NameError и прочее случаются только при запуске.
    """
    try:
        compile(src, "agent.py", "exec")
    except SyntaxError as exc:
        return (type(exc).__name__, exc.msg or "", exc.lineno or 1, exc.offset or 1)
    except Exception as exc:
        return (type(exc).__name__, str(exc), 1, 1)
    return ("", "", 0, 0)
`;

async function ready(announce) {
  if (python !== null) return python;
  // Про загрузку сообщаем только когда её ждёт человек. Проверка синтаксиса
  // грузит рантайм молча: её никто не просил.
  if (announce) self.postMessage({ type: "stage", text: "Загружаю Python… первый раз это 12 МБ" });
  python = await loadPyodide({ indexURL: PYODIDE });
  python.runPython(BOOTSTRAP);
  return python;
}

self.onmessage = async (event) => {
  if (event.data.kind === "check") {
    const { seq, source } = event.data;
    try {
      await ready(false);
      const call = python.globals.get("check_syntax");
      const result = call(source);
      const [name, message, line, column] = result.toJs();
      result.destroy();
      call.destroy();
      self.postMessage({ type: "check", seq, name, message, line, column });
    } catch {
      // Не сложилось — молчим: подсказка необязательна, ломать из-за неё
      // страницу нельзя.
      self.postMessage({ type: "check", seq, name: "", message: "", line: 0, column: 0 });
    }
    return;
  }

  const { kit, check, scenario, agent, agentName, where } = event.data;

  try {
    await ready(true);

    self.postMessage({ type: "stage", text: "Прогоняю уровень…" });

    const call = python.globals.get("run_level");
    const result = call(++runs, kit, check, scenario, agent, agentName, where);
    const [text, code] = result.toJs();
    // PyProxy держит кадры traceback и течёт, если его не освободить.
    result.destroy();
    call.destroy();

    self.postMessage({ type: "done", text, code });
  } catch (error) {
    self.postMessage({ type: "done", text: `Не удалось выполнить: ${error}`, code: 2 });
  }
};
