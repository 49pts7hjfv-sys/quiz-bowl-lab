"""Build the team Quiz Bowl Lab: the site pages, its content chunks, and (optionally) Anki CSVs.

Topics come from data/manifest.json (every topic on the team's study list, in display order).
A topic is "built" when topics/<id>.json exists and passes the basic checks below; every other
manifest topic is shipped as an "upcoming" stub so the site can show it as coming soon.

Outputs
  index.html                     the published site (GitHub Pages): app + lean index of every topic
  dist/quiz-bowl-lab.html        the same page without doctype/charset/viewport (claude.ai artifact)
  content/<area>-<nn>.<hash>.json  full built topics, loaded on demand by the page (publish these
                                 next to either page; names change whenever their content does)
  dist/quiz-bowl-lab-offline.html  everything inlined, for opening from disk / local testing

The lean index (`#qb-data`) holds, for every manifest topic in display order: id, name, category,
order, aka (other spellings, for search) and built; built topics add mono, kicker, freq [rank,
count(, list)], clues and tossups (counts), mediaPending and chunk (an index into `chunks`).
Team study lists refer to topics by their position in `topics` (`ix`) to keep the page small.

Content chunks follow manifest positions: chunk n of an area holds the built topics at that area's
positions (n-1)*CHUNK_SIZE .. n*CHUNK_SIZE-1, so a new batch of topics only rewrites the chunks it
lands in.
"""
import csv, hashlib, html, io, json, os, re, sys, unicodedata
from datetime import date
from pathlib import Path

ROOT = Path(__file__).parent
DIST = ROOT / "dist"
CONTENT = ROOT / "content"
CHUNK_SIZE = 12          # manifest positions per content chunk (about 12 built topics each)
MAX_CHUNKS = 200         # the claude.ai copy can publish at most 255 files at once
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


def released_ids():
    """New topics (added after the original 215) go live only once listed in data/release.json,
    i.e. after they pass validation and an independent fact review. Writers may be mid-way through
    other topic files at any time, so the build never picks those up on its own."""
    base = ROOT / "research" / "manifest_base.json"
    rel = ROOT / "data" / "release.json"
    if not base.exists():
        return None
    original = {t["id"] for t in json.loads(base.read_text(encoding="utf-8"))["topics"]}
    cleared = set(json.loads(rel.read_text(encoding="utf-8"))) if rel.exists() else set()
    return original | cleared


def load():
    manifest = json.loads((ROOT / "data" / "manifest.json").read_text(encoding="utf-8"))
    built, upcoming, skipped = [], [], []
    live = released_ids()
    for m in manifest["topics"]:
        f = ROOT / "topics" / f"{m['id']}.json"
        t = None
        if f.exists() and (live is None or m["id"] in live):
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


def norm(s):
    """Same normalization as QBCore.norm in app/app.js (used to drop duplicate spellings)."""
    s = unicodedata.normalize("NFD", str(s).lower())
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    s = s.replace("&", " and ")
    s = re.sub(r"[’'`]", "", s)
    s = re.sub(r"[^a-z0-9$]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def to_json(obj):
    """Compact JSON that is safe inside a <script> element."""
    return json.dumps(obj, ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c")


def display_order(manifest):
    """Manifest topics in display order: area order, then `order`. Topics in an unknown area go last."""
    rank = {a["name"]: i for i, a in enumerate(manifest["areas"])}
    return sorted(manifest["topics"], key=lambda m: (rank.get(m["category"], len(rank)), m["order"]))


def plan_chunks(manifest, built):
    """[(name, [full topics])]: per area, CHUNK_SIZE manifest positions per chunk, built topics only."""
    by_id = {t["id"]: t for t in built}
    per_area = {}
    for m in display_order(manifest):
        per_area.setdefault(m["category"], []).append(m)
    chunks = []
    for area, ms in per_area.items():
        for start in range(0, len(ms), CHUNK_SIZE):
            members = [by_id[m["id"]] for m in ms[start:start + CHUNK_SIZE] if m["id"] in by_id]
            if members:
                chunks.append((f"{slug(area) or 'other'}-{start // CHUNK_SIZE + 1:02d}", members))
    return chunks


def other_spellings(m):
    """Extra names for search: the manifest's aka list plus the coach's original spelling."""
    seen, out = {norm(m["name"])}, []
    for s in list(m.get("aka") or []) + [m.get("source") or ""]:
        k = norm(s)
        if k and k not in seen:
            seen.add(k)
            out.append(s)
    return out


def build_site(manifest, built):
    """Returns (index_data, chunk_files) where chunk_files = [(published path, json text, topics)]."""
    chunk_files, chunk_of = [], {}
    for name, members in plan_chunks(manifest, built):
        text = json.dumps({"topics": members}, ensure_ascii=False, separators=(",", ":"))
        digest = hashlib.sha256(text.encode("utf-8")).hexdigest()[:8]
        path = f"content/{name}.{digest}.json"
        for t in members:
            chunk_of[t["id"]] = len(chunk_files)
        chunk_files.append((path, text, members))
    by_id = {t["id"]: t for t in built}
    entries, pos = [], {}
    for m in display_order(manifest):
        e = {"id": m["id"], "name": m["name"], "category": m["category"], "order": m["order"]}
        aka = other_spellings(m)
        if aka:
            e["aka"] = aka
        t = by_id.get(m["id"])
        e["built"] = t is not None
        if t is not None:
            e["mono"] = t["mono"]
            e["kicker"] = t["kicker"]
            f = t.get("freq")
            if f and f.get("rank"):
                e["freq"] = [f["rank"], f.get("count", 0)] + ([f["list"]] if f.get("list") and f["list"] != m["category"] else [])
            e["clues"] = len(t["clues"])
            e["tossups"] = len(t["tossups"])
            if t.get("mediaPending"):
                e["mediaPending"] = True
            e["chunk"] = chunk_of[m["id"]]
        pos[m["id"]] = len(entries)
        entries.append(e)
    lists = [{"n": l["n"], "label": l["label"], "ix": [pos[i] for i in l["ids"] if i in pos]} for l in manifest["lists"]]
    data = {"built": date.today().isoformat(), "areas": manifest["areas"], "lists": lists,
            "chunks": [p for p, _, _ in chunk_files], "topics": entries}
    return data, chunk_files


def build_html(data, chunk_files):
    """(offline document with all content inlined, lean document, lean artifact page, index json)."""
    css = (ROOT / "app" / "style.css").read_text(encoding="utf-8")
    js = (ROOT / "app" / "app.js").read_text(encoding="utf-8")
    assert "</script" not in js.lower()
    data_json = to_json(data)
    head = (f"<title>{TITLE}</title>\n"
            f'<link rel="preconnect" href="https://fonts.googleapis.com">\n'
            f'<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
            f'<link rel="stylesheet" href="{FONTS}">\n'
            f"<style>\n{css}\n</style>\n")
    index_tag = f'<script id="qb-data" type="application/json">{data_json}</script>\n'
    inline = "".join(f'<script type="application/json" data-chunk="{html.escape(p)}">{text.replace("<", chr(92) + "u003c")}</script>\n'
                     for p, text, _ in chunk_files)
    app_tag = f"<script>\n{js}\n</script>\n"

    def document(body):
        return ("<!doctype html>\n<html lang=\"en\">\n<head>\n"
                "<meta charset=\"utf-8\">\n"
                "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, viewport-fit=cover\">\n"
                f"{head}</head>\n<body>\n{body}</body>\n</html>\n")
    lean_body = f"{SHELL}\n{index_tag}{app_tag}"
    offline = document(f"{SHELL}\n{index_tag}{inline}{app_tag}")
    lean = document(lean_body)
    artifact = head + lean_body  # the artifact host supplies doctype, charset and viewport
    return offline, lean, artifact, data_json


def write_atomic(path, text):
    """Write via a temp file + rename so a server never hands out a half-written file."""
    path = Path(path)
    tmp = path.with_name(f".{path.name}.{os.getpid()}.tmp")
    tmp.write_text(text, encoding="utf-8")
    os.replace(tmp, path)


class BuildLock:
    """Serializes concurrent builds (they share content/), where the platform supports it."""
    def __enter__(self):
        self.f = open(DIST / ".build.lock", "w")
        try:
            import fcntl
            fcntl.flock(self.f, fcntl.LOCK_EX)
        except (ImportError, OSError):
            pass
        return self

    def __exit__(self, *exc):
        self.f.close()


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


def kb(n):
    return f"{n / 1024:.0f} KB" if n < 1024 * 1024 else f"{n / 1024 / 1024:.1f} MB"


def main():
    DIST.mkdir(exist_ok=True)
    CONTENT.mkdir(exist_ok=True)
    manifest, built, upcoming, skipped = load()
    data, chunk_files = build_site(manifest, built)
    offline, lean, artifact, data_json = build_html(data, chunk_files)
    with BuildLock():
        keep = set()
        for path, text, _ in chunk_files:       # chunks first, so the pages never point at a missing file
            keep.add(Path(path).name)
            target = ROOT / path
            if not target.exists() or target.read_text(encoding="utf-8") != text:
                write_atomic(target, text)
        write_atomic(DIST / "quiz-bowl-lab-offline.html", offline)
        write_atomic(DIST / "quiz-bowl-lab.html", artifact)
        write_atomic(ROOT / "index.html", lean)      # the published site (GitHub Pages)
        for old in CONTENT.glob("*.json"):             # chunks no page refers to any more
            if old.name not in keep:
                old.unlink()
        for tmp in CONTENT.glob(".*.tmp"):             # left behind by an interrupted build
            tmp.unlink()
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
    content_bytes = sum(len(text.encode()) for _, text, _ in chunk_files)
    print(f"built topics: {len(built)} / {len(built) + len(upcoming)}, tossups: {sum(len(t['tossups']) for t in built)}, "
          f"clues: {sum(len(t['clues']) for t in built)}")
    print(f"index: {kb(len(data_json.encode()))} inline JSON for {len(data['topics'])} topics, "
          f"content: {len(chunk_files)} chunk files ({kb(content_bytes)}) in content/")
    print(f"index.html: {kb(len(lean.encode()))}, artifact html: {kb(len(artifact.encode()))}, "
          f"offline html (content inlined): {kb(len(offline.encode()))}, anki rows: {total}")
    if len(chunk_files) > MAX_CHUNKS:
        print(f"  WARNING: {len(chunk_files)} chunk files (keep under {MAX_CHUNKS}); raise CHUNK_SIZE in build.py")
    for tid, why in skipped:
        print(f"  SKIPPED {tid}: {why}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
