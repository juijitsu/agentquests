"""Уровень 03 · новичок. Приём прошлого уровня перестал работать."""

from scenario import CHUNKS, Model, run_tool


def run(question: str) -> tuple[str, int]:
    model = Model()

    # TODO: проверку не проходит ни один кусок — про мост Кэрролл сказано в
    #       одном, а его предел в соседнем. Достройте каждый кусок соседями
    #       по документу: run_tool("neighbours", {"id": c["id"]}) вернёт их
    #       по порядку, склейте тексты и проверяйте уже склеенное.
    fit = [c["text"] for c in CHUNKS if model.answers(question, c["text"])]
    best = max(fit or [c["text"] for c in CHUNKS],
               key=lambda t: model.similarity(question, t))

    return model.reply(question, best), 1
