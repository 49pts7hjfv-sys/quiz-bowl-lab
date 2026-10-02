"""Merge media backfill files (work/media/<id>.json) into topics/<id>.json.

usage: python3 tools/merge_media.py [work/media/<id>.json ...]   (default: every file in work/media/)

Only the topic's "media" and "mediaPending" fields change; everything else in the topic file is kept
as-is. Source names are normalized so the same site/channel is always spelled the same way.
Run tools/check_media.py first, and validate.py --cross afterwards.
"""
import glob, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

SOURCE_FIX = {
    "Britannica Kids (Students)": "Britannica Kids",
    "Encyclopaedia Britannica": "Britannica",
    "Encyclopedia Britannica": "Britannica",
}


def norm_source(m):
    s = m.get("source", "").strip()
    s = SOURCE_FIX.get(s, s)
    if s in ("CrashCourse", "Crash Course"):
        hit = re.search(r"Crash Course ((?:[A-Z][A-Za-z&’']*\s?)+?)\s*#\d+", m.get("title", ""))
        s = f"Crash Course {hit.group(1).strip()}" if hit else "Crash Course"
    m["source"] = s
    return m


def save(path, data):
    tmp = path.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    tmp.replace(path)


def main():
    files = sys.argv[1:] or sorted(glob.glob(str(ROOT / "work" / "media" / "*.json")))
    done = pending = 0
    for f in files:
        d = json.loads(Path(f).read_text(encoding="utf-8"))
        tp = ROOT / "topics" / f"{d['id']}.json"
        t = json.loads(tp.read_text(encoding="utf-8"))
        out = {}
        for k, v in t.items():           # keep key order; media/mediaPending stay where they were
            if k == "mediaPending":
                continue
            out[k] = v
            if k == "media":
                out["media"] = [norm_source(dict(m)) for m in d["media"]]
                if d["mediaPending"]:
                    out["mediaPending"] = True
        save(tp, out)
        pending += bool(d["mediaPending"])
        done += 1
    print(f"merged {done} media files ({done - pending} complete, {pending} still pending)")


if __name__ == "__main__":
    main()
