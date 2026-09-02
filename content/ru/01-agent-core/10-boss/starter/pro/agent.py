"""Уровень 10 · профессионал. Финал трека.

Контракт:
    run() -> tuple[str, int]

run() будет вызвана дважды: смену прервёт крах, второй заход обязан её
дозакрыть. Crash наследуется от BaseException — поймать нельзя.

Доступно:
    run_tool("pending", {})           -> действия через " | " либо EMPTY
    run_tool("ask", {"name": ...})    -> согласование у человека
    run_tool("handle", {"name": ...}) -> выполнение
    model.judge(action) -> bool       -> необратимо ли
    model.close()       -> str        -> отчёт о смене
    APPROVED — список, переживающий крах

Смена засчитана, если разобраны все действия, включая рождённые по ходу;
человека потревожили ровно один раз и только по необратимому; ни одно
согласование не прошло вслепую.
"""

from scenario import APPROVED, EMPTY, Model, TOOLS, run_tool


def run() -> tuple[str, int]:
    raise NotImplementedError
