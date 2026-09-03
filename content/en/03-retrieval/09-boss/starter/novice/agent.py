"""Level 09 · novice. Five violations in one pass."""

from scenario import DOCS, THRESHOLD, TOP_K, Model, run_tool


def run(question: str) -> tuple[str, int]:
    model = Model()

    # TODO 1 (level 05): the question has two halves and there is one query.
    #        model.split(question) returns the sub-questions — handle each one.
    # TODO 2 (level 07): if a sub-question holds an identifier
    #        (model.identifier), narrow the corpus with run_tool("exact", ...) —
    #        otherwise waybill 4478 gets into the selection, it is fresher.
    # TODO 3 (level 08): rank by similarity multiplied by model.freshness(d),
    #        otherwise the tariff from two years ago wins.
    # TODO 4 (level 04): skip repeats via model.same_fact, otherwise three
    #        copies of the rate crowd out the fuel surcharge.
    # TODO 5 (level 06): if the best score is below THRESHOLD there is no
    #        answer — hand back model.say_missing(part) instead of a selection.
    picked = sorted(
        DOCS, key=lambda d: model.similarity(question, d["text"]), reverse=True
    )[:TOP_K]

    return model.reply(question, [picked]), 1
