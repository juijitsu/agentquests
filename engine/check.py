"""Раннер проверок. Один на все уровни: уровень описывает условие, а не реализует его.

    python engine/check.py <путь к решению>
"""

import importlib.util
import sys
import traceback
from pathlib import Path

# Консоль Windows по умолчанию не в UTF-8 — без этого падает на первом же символе.
for stream in (sys.stdout, sys.stderr):
    try:
        stream.reconfigure(encoding="utf-8")
    except Exception:
        pass


def repo_root(start: Path) -> Path:
    """Корень — ближайшая папка вверх, где лежит engine/. Не зависит от глубины уровня."""
    for parent in [start, *start.parents]:
        if (parent / "engine" / "model.py").exists():
            return parent
    return Path.cwd()

EXPECTED = "Хоргос"
MAX_STEPS = 3


def load(path: Path):
    # Пути настраивает раннер, а не ученик: в файле уровня не должно быть плумбинга.
    root = repo_root(path.resolve())
    if str(root) not in sys.path:
        sys.path.insert(0, str(root))
    spec = importlib.util.spec_from_file_location("solution", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    if len(sys.argv) < 2:
        print("укажите путь к решению")
        return 2

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"FAIL  файла нет: {path}")
        return 1

    print(f"\n  Уровень 01 · Что вообще происходит")
    print(f"  Решение: {path}\n")

    try:
        module = load(path)
        answer, steps = module.run("Где груз KZ-4471?")
    except NotImplementedError:
        print("  ✗ run() ещё не реализована")
        print("
  FAIL  Это заготовка для сложности «профессионал».")
        print("        Соберите цикл сами или возьмите starter/advanced.
")
        return 1
    except RecursionError:
        print("  \u2717 агент зациклился")
        print("\n  FAIL  Модель просит инструмент снова и снова.")
        print("        Значит она не видит его результата — посмотрите,")
        print("        что происходит с ответом инструмента после вызова.\n")
        return 1
    except Exception:
        print("  \u2717 решение упало с ошибкой:\n")
        traceback.print_exc()
        return 1

    ok = True

    if answer is None or not isinstance(answer, str):
        print("  \u2717 run() не вернул строку с ответом")
        ok = False
    elif EXPECTED not in answer:
        print(f"  \u2717 в ответе нет ожидаемого: {answer!r}")
        print("        агент не донёс результат инструмента до финального ответа")
        ok = False
    else:
        print(f"  \u2713 агент ответил: {answer}")

    if steps > MAX_STEPS:
        print(f"  \u2717 потрачено итераций: {steps}, допустимо {MAX_STEPS}")
        ok = False
    elif ok:
        print(f"  \u2713 уложился в {steps} итерации из {MAX_STEPS}")

    print("\n  " + ("PASS  уровень 02 открыт\n" if ok else "FAIL\n"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
