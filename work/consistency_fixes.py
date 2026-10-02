"""One-off consistency fixes found by the 2026-10-02 audit (safe to re-run).

- unique monograms (15 pairs shared the same letters)
- drop the legacy "batch" field (11 topics)
- normalize media source names everywhere (CrashCourse -> series name, Britannica variants)
- remove duplicate entries in accept/prompt/reject lists
- straight double quotes -> curly quotes in qb.tip / sample.note
"""
import glob, json, re, sys, unicodedata
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from merge_media import norm_source, save  # noqa: E402

MONO = {  # second topic of each clashing pair gets a distinct monogram
    "jason": "JSN", "passover": "PSV", "the-thinker": "THK", "adolf-hitler": "HTL",
    "acceleration": "ACC", "mona-lisa": "MLS", "cell-membrane": "CMB", "black-holes": "BHL",
    "the-catcher-in-the-rye": "CIR", "berlin-wall": "BLW", "odin": "ODN", "lincoln-memorial": "LNM",
    "stephen-hawking": "SWH", "quartz": "QTZ", "inertia": "INR",
}


def n(s):
    s = unicodedata.normalize("NFD", str(s).lower())
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9]+", " ", s)).strip()


def curly(s):
    return re.sub(r'"([^"]*)"', "“\\1”", s)


changes = Counter()
for f in sorted(glob.glob(str(ROOT / "topics" / "*.json"))):
    p = Path(f)
    t = json.loads(p.read_text(encoding="utf-8"))
    before = json.dumps(t, ensure_ascii=False)
    if t["id"] in MONO and t["mono"] != MONO[t["id"]]:
        t["mono"] = MONO[t["id"]]; changes["mono"] += 1
    if "batch" in t:
        del t["batch"]; changes["batch"] += 1
    t["media"] = [norm_source(dict(m)) for m in t["media"]]
    for k in ("accept", "prompt", "reject"):
        seen, out = set(), []
        for x in t[k]:
            if n(x) in seen:
                changes[f"dup {k}"] += 1
                continue
            seen.add(n(x)); out.append(x)
        t[k] = out
    for k in ("qb", "sample"):
        for kk, v in t[k].items():
            if isinstance(v, str) and '"' in v:
                t[k][kk] = curly(v); changes["quotes"] += 1
    if json.dumps(t, ensure_ascii=False) != before:
        save(p, t); changes["files"] += 1

monos = Counter(json.loads(Path(f).read_text(encoding="utf-8"))["mono"] for f in glob.glob(str(ROOT / "topics" / "*.json")))
dups = {m: c for m, c in monos.items() if c > 1}
print(dict(changes))
print("duplicate monograms left:", dups or "none")
