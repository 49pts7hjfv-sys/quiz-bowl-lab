"""Check a media backfill file before it is merged into a topic.

usage: python3 tools/check_media.py work/media/<id>.json [...]

A media file looks like:
  {"id": "<topic id>",
   "media": [ {group, kind, title, source, url, note}, ... ],   # the COMPLETE final list for the topic
   "mediaPending": false,                                        # true only if < 3 focus videos or no read link
   "report": "one line for the reviewer"}

Rules (same as TOPIC_SPEC.md Step 3 and validate.py):
  - focus: 3-5 videos mainly about this exact topic, listed first, shortest/easiest first
  - background: 0-2 optional bigger-picture videos
  - read: exactly 1 kid-friendly article, listed last
  - video urls exactly https://www.youtube.com/watch?v=<11-char id>
  - every field non-empty; no straight double quotes in title/note (use curly quotes)
Lines starting with "!!" are errors. Lines starting with ".." are warnings.
"""
import json, re, sys, glob
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
YT = re.compile(r"^https://www\.youtube\.com/watch\?v=[A-Za-z0-9_-]{11}$")
MAN = {t["id"]: t for t in json.loads((ROOT / "data" / "manifest.json").read_text(encoding="utf-8"))["topics"]}
GROUP_ORDER = {"focus": 0, "background": 1, "read": 2}


def used_elsewhere(url, tid):
    hits = []
    for f in glob.glob(str(ROOT / "topics" / "*.json")):
        if Path(f).stem == tid:
            continue
        try:
            t = json.loads(Path(f).read_text(encoding="utf-8"))
        except Exception:  # noqa: BLE001
            continue
        if any(m.get("url") == url for m in t.get("media", [])):
            hits.append(t["id"])
    return hits


def check(path):
    errs, warns = [], []
    try:
        d = json.loads(Path(path).read_text(encoding="utf-8"))
    except Exception as e:  # noqa: BLE001
        return [f"not valid JSON: {e}"], warns
    tid = d.get("id")
    if tid not in MAN:
        errs.append(f"id {tid!r} is not in data/manifest.json")
    if Path(path).stem != tid:
        errs.append(f"file must be named {tid}.json")
    media = d.get("media")
    if not isinstance(media, list):
        return errs + ["media must be a list"], warns
    if not isinstance(d.get("mediaPending"), bool):
        errs.append("mediaPending must be true or false")
    if not d.get("report"):
        warns.append("no report line")
    seen = set()
    last = -1
    counts = {"focus": 0, "background": 0, "read": 0}
    for m in media:
        label = m.get("title") or m.get("url")
        for k in ("group", "kind", "title", "source", "url", "note"):
            if not str(m.get(k, "")).strip():
                errs.append(f"missing {k}: {label}")
        g = m.get("group")
        if g not in GROUP_ORDER:
            errs.append(f"group must be focus/background/read: {label}")
            continue
        counts[g] += 1
        if GROUP_ORDER[g] < last:
            errs.append(f"order must be focus items, then background, then read: {label}")
        last = max(last, GROUP_ORDER[g])
        kind = m.get("kind")
        if g in ("focus", "background") and kind != "video":
            errs.append(f"{g} items must be kind 'video': {label}")
        if g == "read" and kind != "article":
            errs.append(f"read item must be kind 'article': {label}")
        url = m.get("url", "")
        if kind == "video" and not YT.match(url):
            errs.append(f"video url must be exactly https://www.youtube.com/watch?v=ID (11 chars): {url}")
        if kind == "article" and not url.startswith("https://"):
            errs.append(f"article url must start with https:// : {url}")
        if "wikipedia.org" in url:
            errs.append(f"no Wikipedia links in media (the app adds wiki itself): {url}")
        if url in seen:
            errs.append(f"duplicate url: {url}")
        seen.add(url)
        for k in ("title", "note", "source"):
            if '"' in str(m.get(k, "")):
                errs.append(f"straight double quote in {k} (use “ ”): {label}")
        if kind == "video":
            other = used_elsewhere(url, tid)
            if other:
                warns.append(f"video also used by {', '.join(other)} (fine only if it is mainly about THIS topic too): {label}")
    if counts["focus"] > 5:
        errs.append(f"{counts['focus']} focus videos (max 5)")
    if counts["background"] > 2:
        errs.append(f"{counts['background']} background videos (max 2)")
    if counts["read"] > 1:
        errs.append(f"{counts['read']} read links (exactly 1)")
    complete = 3 <= counts["focus"] <= 5 and counts["read"] == 1
    if d.get("mediaPending") is False and not complete:
        errs.append(f"mediaPending is false but topic has {counts['focus']} focus videos and {counts['read']} read link(s) (needs 3-5 and 1)")
    if d.get("mediaPending") is True and complete:
        errs.append("topic is complete (3-5 focus + 1 read) so mediaPending must be false")
    warns.append(f"focus {counts['focus']}, background {counts['background']}, read {counts['read']} -> {'COMPLETE' if complete else 'STILL PENDING'}")
    return errs, warns


def main():
    files = sys.argv[1:] or sorted(glob.glob(str(ROOT / "work" / "media" / "*.json")))
    total = 0
    for f in files:
        errs, warns = check(f)
        total += len(errs)
        print(f"== {Path(f).name}: {'OK' if not errs else f'{len(errs)} error(s)'}")
        for e in errs:
            print(f"  !! {e}")
        for w in warns:
            print(f"  .. {w}")
    print(f"\nErrors: {total}")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
