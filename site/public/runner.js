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
`;

self.onmessage = async (event) => {
  const { kit, check, scenario, agent, agentName, where } = event.data;

  try {
    if (python === null) {
      self.postMessage({ type: "stage", text: "Загружаю Python… первый раз это 12 МБ" });
      python = await loadPyodide({ indexURL: PYODIDE });
      python.runPython(BOOTSTRAP);
    }

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
