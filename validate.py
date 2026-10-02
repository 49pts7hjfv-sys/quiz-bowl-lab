"""Validate Quiz Bowl Lab topic files.

usage:
  python3 validate.py topics/<id>.json [...]   check specific files (writer agents use this)
  python3 validate.py                          check every topic file
  python3 validate.py --cross                  also check answer-line conflicts across topics

Lines starting with "!!" are errors that must be fixed. Lines starting with ".." are warnings.
"""
import json, re, subprocess, sys, unicodedata
from pathlib import Path

ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT))
from build import problems_in  # noqa: E402

TIERS = ("giveaway", "middle", "power")
YT = re.compile(r"^https://www\.youtube\.com/watch\?v=[A-Za-z0-9_-]{11}$")
MANIFEST = json.loads((ROOT / "data" / "manifest.json").read_text(encoding="utf-8"))
MAN = {t["id"]: t for t in MANIFEST["topics"]}


def norm(s):
    s = unicodedata.normalize("NFD", str(s).lower())
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    s = s.replace("&", " and ")
    s = re.sub(r"[’'`]", "", s)
    s = re.sub(r"[^a-z0-9$]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def clean(s):
    s = re.sub(r"\s*\[“[^”]*”\]", "", s)
    return s.replace("_", "")


def cloze_term(clue):
    text = clue["t"].replace("_", "")
    best = None
    for k in clue["k"]:
        if len(k) < 4:
            continue
        m = re.search(r"(?<![A-Za-z0-9])" + re.escape(k) + r"(?![A-Za-z0-9])", text, re.I)
        if m and (best is None or len(m.group(0)) > len(best)):
            best = m.group(0)
    return best


def check(path):
    errs, warns = [], []
    try:
        t = json.loads(Path(path).read_text(encoding="utf-8"))
    except Exception as e:  # noqa: BLE001
        return [f"not valid JSON: {e}"], []
    errs += problems_in(t)
    if errs:
        return errs, warns
    tid = t["id"]
    if tid not in MAN:
        errs.append(f"id {tid!r} is not in data/manifest.json")
    if Path(path).name != f"{tid}.json":
        errs.append(f"file must be named {tid}.json")
    if not re.fullmatch(r"[A-Z0-9]{1,3}", t["mono"]):
        errs.append("mono must be 1-3 capital letters/digits")
    for k in ("accept", "prompt", "reject"):
        if not isinstance(t[k], list):
            errs.append(f"{k} must be a list")
    if not t["accept"]:
        errs.append("accept is empty")
    # tossups
    fracs, lens = [], []
    accept_phrases = [norm(a) for a in t["accept"] if len(norm(a)) > 3]
    for i, tu in enumerate(t["tossups"], 1):
        pw = len(clean(tu["p"]).split()); rw = len(clean(tu["r"]).split())
        frac = pw / max(1, pw + rw)
        fracs.append(frac); lens.append(pw + rw)
        if frac < 0.38 or frac > 0.82:
            errs.append(f"tossup {i}: power part is {frac:.0%} of the words (keep it 40-80%)")
        if pw + rw < 40 or pw + rw > 105:
            errs.append(f"tossup {i}: {pw + rw} words (keep 45-95)")
        if tu["p"].count("_") % 2 or tu["r"].count("_") % 2:
            errs.append(f"tossup {i}: unbalanced _italics_ underscores")
        if '"' in tu["p"] or '"' in tu["r"]:
            errs.append(f"tossup {i}: straight double quote (use “ ”)")
        if "(*)" in tu["p"] + tu["r"] or "<" in tu["p"] + tu["r"]:
            errs.append(f"tossup {i}: no (*) or HTML inside p/r; the app adds the power mark")
        if not re.search(r"\bFor 10 points\b", tu["r"]):
            errs.append(f"tossup {i}: r must contain “For 10 points” (exact casing)")
        text = " " + norm(clean(tu["p"] + " " + tu["r"])) + " "
        for a in accept_phrases:
            if f" {a} " in text:
                errs.append(f"tossup {i}: gives away the answer (contains “{a}”)")
                break
    if lens:
        warns.append(f"tossups: {min(lens)}–{max(lens)} words, power share avg {sum(fracs)/len(fracs):.2f}")
    # clues
    tiers = {k: 0 for k in TIERS}
    name_words = set(norm(MAN.get(tid, t)["name"]).split())
    no_cloze = 0
    for c in t["clues"]:
        tiers[c["tier"]] += 1
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", c["id"]):
            errs.append(f"clue id {c['id']!r} must be kebab-case")
        if c["t"].count("_") % 2:
            errs.append(f"clue {c['id']}: unbalanced underscores")
        if not isinstance(c.get("k"), list) or not c["k"]:
            errs.append(f"clue {c['id']}: needs note keywords k")
            continue
        if not isinstance(c.get("n"), int) or c["n"] < 0:
            errs.append(f"clue {c['id']}: n must be a whole number (real tossups using this clue)")
        for k in c["k"]:
            if k != k.lower():
                errs.append(f"clue {c['id']}: keyword {k!r} must be lowercase")
            nk = norm(k)
            if nk and (nk in name_words or nk == norm(MAN.get(tid, t)["name"])):
                errs.append(f"clue {c['id']}: keyword {k!r} is part of the answer itself")
        if not cloze_term(c):
            no_cloze += 1
        ctext = " " + norm(c["t"]) + " "
        for a in accept_phrases:
            if f" {a} " in ctext:
                errs.append(f"clue {c['id']}: contains the answer “{a}”")
                break
    if not 3 <= tiers["giveaway"] <= 6:
        errs.append(f"{tiers['giveaway']} giveaway clues (want 3-6)")
    if not 5 <= tiers["middle"] <= 11:
        errs.append(f"{tiers['middle']} middle clues (want 5-11)")
    if not 8 <= tiers["power"] <= 15:
        errs.append(f"{tiers['power']} power clues (want 8-15)")
    if no_cloze > len(t["clues"]) * 0.25:
        errs.append(f"{no_cloze} clues have no fill-in-the-blank keyword (a keyword of 4+ letters must appear in the clue text)")
    stocked = sum(1 for c in t["clues"] if c.get("n", 0) >= 2)
    if t["sample"]["n"] >= 4 and stocked < 4:
        warns.append(f"only {stocked} clues marked as stock (n >= 2) from {t['sample']['n']} real tossups")
    warns.append(f"clues: {tiers}")
    # media
    for m in t["media"]:
        for k in ("group", "kind", "title", "source", "url", "note"):
            if not m.get(k):
                errs.append(f"media item missing {k}: {m.get('title') or m.get('url')}")
        if m.get("kind") == "video" and not YT.match(m.get("url", "")):
            errs.append(f"video url must look like https://www.youtube.com/watch?v=ID: {m.get('url')}")
        if m.get("group") == "focus" and m.get("kind") not in ("video", "museum"):
            errs.append(f"focus items must be videos: {m.get('title')}")
    if t.get("mediaPending"):
        nf = sum(1 for m in t["media"] if m.get("group") == "focus")
        warns.append(f"MEDIA PENDING: {nf} focused video(s) so far; needs 3-5 plus a read link later")
    if not str(t["wiki"]).startswith("https://en.wikipedia.org/wiki/"):
        errs.append("wiki must be an en.wikipedia.org/wiki/ link")
    for k in ("q", "found", "tip"):
        if k not in t["qb"]:
            errs.append(f"qb.{k} missing")
    if not isinstance(t["qb"].get("found"), int):
        errs.append("qb.found must be a number")
    if not isinstance(t["sample"].get("n"), int) or not t["sample"].get("note"):
        errs.append("sample needs n (number) and note")
    if "<b><u>" not in t["answerHtml"] or "<b><u>" not in t["trap"]["line"]:
        errs.append("answerHtml and trap.line must underline the required part with <b><u>…</u></b>")
    words = len(t["briefing"].split())
    if words < 30 or words > 95:
        errs.append(f"briefing is {words} words (want 2-3 sentences, 35-90 words)")
    return errs, warns


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    cross = "--cross" in sys.argv
    files = [Path(a) for a in args] or sorted((ROOT / "topics").glob("*.json"))
    total = 0
    for f in files:
        errs, warns = check(f)
        total += len(errs)
        status = "OK" if not errs else f"{len(errs)} error(s)"
        print(f"== {f.name}: {status}")
        for e in errs:
            print(f"  !! {e}")
        for w in warns:
            print(f"  .. {w}")
    cmd = ["node", str(ROOT / "tools" / "judge_check.js")] + (["--cross"] if cross else []) + [str(f) for f in files]
    r = subprocess.run(cmd, capture_output=True, text=True)
    print(r.stdout.strip())
    if r.returncode:
        total += r.stdout.count("FAIL ")
    print(f"\nErrors: {total}")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
