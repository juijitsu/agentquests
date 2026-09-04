"""Обход собранного сайта: то, что положено проверять после каждой правки.

    cd site && npm run build && python scripts/sweep.py

Проверяется то, что уже ломалось на практике, и ничего сверх того:

  * у страницы есть заголовок первого уровня;
  * `<html lang>` совпадает с разделом: /en/... английский, остальное русский;
  * в тексте нет undefined, NaN и [object Object];
  * пометки «урок не переведён» нет на русских страницах;
  * на английской странице нет кириллицы, то есть перевод не забыт;
  * у каждой страницы есть двойник на втором языке;
  * переключатель языка ведёт именно на этот двойник, а не куда попало;
  * заголовки не делят один id, иначе документ невалиден;
  * якорная ссылка ведёт на существующий заголовок.

Код возврата 1, если хоть что-то не сошлось: годится для CI.
"""

import re
import sys
import urllib.parse
from pathlib import Path

for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8")  # консоль Windows иначе ломает «✗»
    except Exception:
        pass

BASE = "/agentquests"
OUT = Path(__file__).resolve().parent.parent / "out"
# Страница 404 языку не принадлежит: на неё попадают с любого адреса.
APART = {"404", "_not-found"}

SWITCH = re.compile(
    r'<a[^>]*href="([^"]+)"[^>]*hrefLang="(?:ru|en)"[^>]*>(RU|EN)</a>', re.I
)
HEADING_ID = re.compile(r'<h[1-6][^>]*id="([^"]+)"')
ANCHOR = re.compile(r'href="#([^"]+)"')
LANG = re.compile(r'<html[^>]*lang="([^"]+)"')
CYRILLIC = re.compile(r"[А-Яа-яЁё]")
JUNK = ("undefined", "NaN", "[object Object]")
NOT_TRANSLATED = "has not been translated yet"


def visible(html: str) -> str:
    """Текст без скриптов и стилей: иначе NaN находится в бандле."""
    html = re.sub(r"(?is)<script.*?</script>", " ", html)
    html = re.sub(r"(?is)<style.*?</style>", " ", html)
    return re.sub(r"(?s)<[^>]+>", " ", html)


def twin_of(page: str, english: bool) -> str:
    if english:
        return page[3:] if page.startswith("en/") else ""
    return f"en/{page}" if page else "en"


def main() -> int:
    if not OUT.exists():
        print(f"нет собранного сайта: {OUT}\nсначала npm run build")
        return 2

    pages = {}
    for path in OUT.rglob("index.html"):
        name = path.parent.relative_to(OUT).as_posix()
        pages["" if name == "." else name] = path

    problems = []
    for page, path in sorted(pages.items()):
        if page in APART:
            continue
        html = path.read_text(encoding="utf-8", errors="replace")
        text = visible(html)
        english = page == "en" or page.startswith("en/")
        where = page or "/"

        if "<h1" not in html:
            problems.append(f"{where}: нет заголовка первого уровня")

        for junk in JUNK:
            if junk in text:
                problems.append(f"{where}: в тексте {junk}")

        if NOT_TRANSLATED in html and not english:
            problems.append(f"{where}: пометка о непереведённом уроке на русской странице")

        found = LANG.search(html)
        want = "en" if english else "ru"
        if not found:
            problems.append(f"{where}: у <html> нет lang")
        elif found.group(1) != want:
            problems.append(f"{where}: lang={found.group(1)}, ждали {want}")

        if english and CYRILLIC.search(text):
            problems.append(f"{where}: кириллица на английской странице")

        ids = HEADING_ID.findall(html)
        twice = sorted({i for i in ids if ids.count(i) > 1})
        if twice:
            problems.append(f"{where}: заголовки делят id {twice}")

        for anchor in {urllib.parse.unquote(a) for a in ANCHOR.findall(html)}:
            if anchor not in ids:
                problems.append(f"{where}: якорь «{anchor}» ведёт в никуда")

        switch = SWITCH.search(html)
        if not switch:
            problems.append(f"{where}: нет переключателя языка")
            continue
        href, label = switch.groups()
        twin = twin_of(page, english)
        if label != ("RU" if english else "EN"):
            problems.append(f"{where}: кнопка {label}, ждали {'RU' if english else 'EN'}")
        if href != (f"{BASE}/{twin}/" if twin else f"{BASE}/"):
            problems.append(f"{where}: переключатель ведёт на {href}")
        elif twin not in pages:
            problems.append(f"{where}: двойника {twin} нет в сборке")

    russian = {p for p in pages if p not in APART and not (p == "en" or p.startswith("en/"))}
    english = {twin_of(p, True) for p in pages if p == "en" or p.startswith("en/")}
    alone = sorted(russian ^ english)
    if alone:
        problems.append(f"без пары на втором языке: {alone[:5]}")

    print(f"  страниц: {len(pages)}   русских: {len(russian)}   английских: {len(english)}")
    print(f"  проблем: {len(problems)}")
    for line in problems:
        print(f"    ✗ {line}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
