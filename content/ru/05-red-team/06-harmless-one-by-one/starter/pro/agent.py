"""Уровень 06 · профессионал.

Контракт:
    run() -> tuple[str, int]

Второе значение — сколько раз вы обратились к модели.

Доступно:
    run_tool("list_batch", {"batch": BATCH_ID}) -> шаги партии по порядку,
        у каждого id, pos, action, system, target
    model.check(step_id) -> {"step": ..., "allowed": bool} против записи
        в её нынешнем виде; ничего не меняет
    model.run_step(step_id) -> отдаёт шаг исполнителю; приговор не сообщает
    model.reset_account() -> возвращает запись в исходное состояние
    model.report(found) -> str, found — список id

Искомое: шаги, которым проверка отказывает поодиночке и разрешает в тот
момент, когда они реально запускаются внутри партии.
"""

from scenario import BATCH_ID, Model, run_tool


def run() -> tuple[str, int]:
    raise NotImplementedError
