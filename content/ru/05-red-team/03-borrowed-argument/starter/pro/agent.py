"""Уровень 03 · профессионал.

Контракт:
    run() -> tuple[str, int]

Второе значение — сколько раз вы обратились к модели.

Доступно:
    run_tool("calls", {}) -> аргументы вызова, у каждого id и call
    model.trace(arg_id) -> {"source": id входа, "path": BY_MODEL или BY_CODE}
    model.report(found) -> str, found — список id
    SURFACE -> входы, которыми управляют снаружи, с уровня 01

Аргумент входит в поверхность, если его значение пришло из входа, которым
управляют снаружи.
"""

from scenario import BY_CODE, BY_MODEL, SURFACE, Model, run_tool


def run() -> tuple[str, int]:
    raise NotImplementedError
