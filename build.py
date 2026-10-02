"""Build the team Quiz Bowl Lab: offline HTML, publishable artifact HTML, and Anki CSVs.

Topics come from data/manifest.json (every topic on the team's study list, in display order).
A topic is "built" when topics/<id>.json exists and passes the basic checks below; every other
manifest topic is shipped as an "upcoming" stub so the site can show it as coming soon.
"""
import csv, html, io, json, re, sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).parent
DIST = ROOT / "dist"
TITLE = "Quiz Bowl Lab"
FONTS = ("https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400"
         "&family=Big+Shoulders+Display:wght@700;800;900"
         "&family=Literata:ital,opsz,wght@0,7..72,400;0,7..72,700;1,7..72,400&display=swap")

SHELL = """<div class="app" id="app">
  <header class="topbar">
    <button class="menu-btn" id="menuBtn" data-act="menu" aria-label="Open the menu"></button>
    <span class="tb-brand">Quiz Bowl Lab</span>
    <span class="tb-xp" id="tbXp"></span>
  </header>
  <aside class="rail" id="rail" aria-label="Binder"></aside>
  <div class="scrim" data-act="menu-close"></div>
  <main class="main" id="main" tabindex="-1">
    <noscript><p>This study app needs JavaScript turned on.</p></noscript>
  </main>
</div>
<div class="toast" id="toast" role="status" aria-live="polite"></div>"""

GROUPS = {"focus", "read", "background"}
TIERS = ("giveaway", "middle", "power")


def problems_in(t):
    """Basic structural checks. Anything listed here keeps the topic out of the build."""
    out = []
    req = ["id", "name", "mono", "kicker", "dates", "briefing", "answerHtml", "accept", "prompt", "reject",
           "media", "wiki", "qb", "sample", "tossups", "clues", "trap"]
    for k in req:
        if k not in t:
            out.append(f"missing {k}")
    if out:
        return out
    if len(t["tossups"]) != 15:
        out.append(f"{len(t['tossups'])} tossups")
    for i, tu in enumerate(t["tossups"], 1):
        if not tu.get("p") or not tu.get("r"):
            out.append(f"tossup {i} empty part")
        elif "for 10 points" not in tu["r"].lower():
            out.append(f"tossup {i} lacks 'For 10 points'")
    groups = [m.get("group") for m in t["media"]]
    if not set(groups) <= GROUPS:
        out.append(f"bad media group {groups}")
    pending = bool(t.get("mediaPending"))   # videos still being found (e.g. web search unavailable)
    if not (0 if pending else 3) <= groups.count("focus") <= 5:
        out.append(f"{groups.count('focus')} focused videos (need 3 to 5, or set mediaPending)")
    if "read" not in groups and not pending:
        out.append("no read link")
    urls = [m.get("url") for m in t["media"]]
    if len(urls) != len(set(urls)):
        out.append("duplicate media link")
    tiers = [c.get("tier") for c in t["clues"]]
    if any(x not in TIERS for x in tiers):
        out.append("bad clue tier")
    if tiers != sorted(tiers, key=TIERS.index):
        out.append("clues not ordered giveaway -> middle -> power")
    ids = [c.get("id") for c in t["clues"]]
    if len(ids) != len(set(ids)):
        out.append("duplicate clue ids")
    if not 15 <= len(t["clues"]) <= 32:
        out.append(f"{len(t['clues'])} clues")
    for k in ("title", "body", "fix", "line"):
        if not t["trap"].get(k):
            out.append(f"trap.{k} missing")
    return out


def load():
    manifest = json.loads((ROOT / "data" / "manifest.json").read_text(encoding="utf-8"))
    built, upcoming, skipped = [], [], []
    for m in manifest["topics"]:
        f = ROOT / "topics" / f"{m['id']}.json"
        t = None
        if f.exists():
            try:
                t = json.loads(f.read_text(encoding="utf-8"))
            except json.JSONDecodeError as e:
                skipped.append((m["id"], f"bad JSON: {e}"))
                t = None
        if t is not None:
            probs = problems_in(t)
            if t.get("id") != m["id"]:
                probs.append(f"id {t.get('id')!r} != manifest id")
            if probs:
                skipped.append((m["id"], "; ".join(probs)))
                t = None
        if t is None:
            upcoming.append({"id": m["id"], "name": m["name"], "category": m["category"], "order": m["order"]})
            continue
        t["name"] = m["name"]          # the manifest spelling is what the picker and lists show
        t["category"] = m["category"]
        t["qbCategory"] = t.get("qbCategory") or m["qbCategory"]
        t["order"] = m["order"]
        t.pop("tests", None)          # answer-checker test cases are for validate.py only
        built.append(t)
    return manifest, built, upcoming, skipped


def build_html(manifest, built, upcoming):
    css = (ROOT / "app" / "style.css").read_text(encoding="utf-8")
    js = (ROOT / "app" / "app.js").read_text(encoding="utf-8")
    assert "</script" not in js.lower()
    data = {"built": date.today().isoformat(), "areas": manifest["areas"], "lists": manifest["lists"],
            "topics": built, "upcoming": upcoming}
    data_json = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c")
    head = (f"<title>{TITLE}</title>\n"
            f'<link rel="preconnect" href="https://fonts.googleapis.com">\n'
            f'<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
            f'<link rel="stylesheet" href="{FONTS}">\n'
            f"<style>\n{css}\n</style>\n")
    body = (f"{SHELL}\n"
            f'<script id="qb-data" type="application/json">{data_json}</script>\n'
            f"<script>\n{js}\n</script>\n")
    offline = ("<!doctype html>\n<html lang=\"en\">\n<head>\n"
               "<meta charset=\"utf-8\">\n"
               "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, viewport-fit=cover\">\n"
               f"{head}</head>\n<body>\n{body}</body>\n</html>\n")
    artifact = head + body  # the artifact host supplies doctype, charset and viewport
    return offline, artifact


def rich(text):
    """Clue text -> small HTML for Anki (escape, then _italics_)."""
    return re.sub(r"_([^_]+)_", r"<i>\1</i>", html.escape(text, quote=False))


TIER_LABEL = {"giveaway": "Giveaway clue", "middle": "10-point clue", "power": "Power clue"}


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def csv_for(topics):
    buf = io.StringIO()
    buf.write("#separator:Comma\n#html:true\n#notetype:Basic\n#columns:Front,Back,Tags,Deck\n#tags column:3\n#deck column:4\n")
    w = csv.writer(buf, quoting=csv.QUOTE_MINIMAL, lineterminator="\n")
    rows = 0
    for t in topics:
        deck = f"Quiz Bowl::{t['category']}"
        tslug = t["id"].replace("-", "_")
        cat = slug(t["category"]).replace("-", "_")
        answer = f"<b>{html.escape(t['name'])}</b><br><small>{t['answerHtml']}</small>"
        for c in t["clues"]:
            front = f"<small>{TIER_LABEL[c['tier']]} · {html.escape(t['category'])}</small><br>{rich(c['t'])}"
            w.writerow([front, answer, f"quizbowl qb::{cat} qb::{tslug} {c['tier']}", deck])
            rows += 1
        parts = []
        for tier, label in (("giveaway", "Giveaway"), ("middle", "10-point"), ("power", "Power")):
            items = [rich(c["t"]) for c in t["clues"] if c["tier"] == tier]
            parts.append(f"<b>{label}</b><br>" + "<br>".join("• " + i for i in items))
        w.writerow([f"<small>Recite every clue you know</small><br><b>{html.escape(t['name'])}</b>",
                    "<br><br>".join(parts), f"quizbowl qb::{cat} qb::{tslug} recite", deck])
        rows += 1
    return buf.getvalue(), rows


def main():
    DIST.mkdir(exist_ok=True)
    manifest, built, upcoming, skipped = load()
    offline, artifact = build_html(manifest, built, upcoming)
    (DIST / "quiz-bowl-lab-offline.html").write_text(offline, encoding="utf-8")
    (DIST / "quiz-bowl-lab.html").write_text(artifact, encoding="utf-8")
    (ROOT / "index.html").write_text(offline, encoding="utf-8")   # the published site (GitHub Pages)
    total = 0
    anki = DIST / "anki"
    if "--anki" in sys.argv:          # Anki CSVs are paused (focus on the HTML); run with --anki to make them
      anki.mkdir(exist_ok=True)
      for old in anki.glob("*.csv"):
        old.unlink()
    for area in (manifest["areas"] if "--anki" in sys.argv else []):
        ts = [t for t in built if t["category"] == area["name"]]
        if not ts:
            continue
        text, rows = csv_for(ts)
        (anki / f"quiz-bowl-{slug(area['name'])}-anki.csv").write_text(text, encoding="utf-8")
        total += rows
    js = (ROOT / "app" / "app.js").read_text(encoding="utf-8")
    core = js.split("/* ===== END QBCORE ===== */")[0]
    (DIST / "_core_for_test.js").write_text(core + "\nmodule.exports = QBCore;\n", encoding="utf-8")
    print(f"built topics: {len(built)} / {len(built) + len(upcoming)}, tossups: {sum(len(t['tossups']) for t in built)}, "
          f"clues: {sum(len(t['clues']) for t in built)}")
    print(f"offline html: {len(offline.encode())/1024:.0f} KB, artifact html: {len(artifact.encode())/1024:.0f} KB, anki rows: {total}")
    for tid, why in skipped:
        print(f"  SKIPPED {tid}: {why}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
