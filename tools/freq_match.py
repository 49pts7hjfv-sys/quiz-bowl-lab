"""Attach QBReader frequency-list ranks to topics.

usage: python3 tools/freq_match.py            dry run: print matches for review
       python3 tools/freq_match.py --apply    write "freq": {rank, count, list} into topics/<id>.json

Lists live in research/freq/<area>.txt (header "# <url> | entries: N", then "count|answer" lines, sorted
by count). They are QBReader's Middle School + Easy High School tossup frequency lists (difficulties 1,2)
for the area's QBReader category/subcategory.

Matching: a list entry matches a topic when its normalized answer equals the topic's name, QBReader query,
or any accept-list answer (also after dropping a leading title like "Saint", "King", "The"). QBReader counts
each spelling separately, so the strongest matching entry is used. Rank is shared by ties (competition
ranking): rank = 1 + number of answers with a higher count. For lists cut off at the limit, answers whose
count equals the cut-off count may be missing from the file; a topic found in the file still gets its
(exact) rank, and a topic not found gets no badge.
"""
import json, re, sys, unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from merge_media import save  # noqa: E402

AREA_FILE = {
    "American History": "american-history", "European History": "european-history",
    "Literature": "literature", "Mythology": "mythology", "Religion": "religion",
    "Philosophy": "philosophy", "Social Science": "social-science", "Fine Arts": "fine-arts",
    "Physics": "physics", "Biology": "biology", "Earth Science": "earth-science",
}
# Spellings QBReader uses that a topic's accept list leaves out on purpose (e.g. "Notre-Dame de Paris"
# is also Hugo's novel, so the topic doesn't accept it — but in the Fine Arts list it means the cathedral).
ALIASES = {
    "notre-dame-cathedral": ["Notre-Dame de Paris"],
    "sistine-chapel": ["ceiling of the Sistine Chapel"],
}
# Accepted answers that are really a different answer line on QBReader's list.
EXCLUDE = {
    "refraction": ["index of refraction"],
}
TITLES = ("saint ", "st ", "king ", "queen ", "sir ", "emperor ", "empress ", "tsar ", "czar ", "pope ",
          "the ", "prophet ", "lord ", "president ", "general ", "dr ")


def norm(s):
    s = unicodedata.normalize("NFD", str(s).lower())
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    s = re.sub(r"[´`'’‘“”\"]", "", s).replace("&", " and ")
    s = re.sub(r"[^a-z0-9]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def untitle(s):
    again = True
    while again:
        again = False
        for h in TITLES:
            if s.startswith(h) and len(s) > len(h) + 2:
                s, again = s[len(h):], True
    return s


def load_list(area):
    lines = (ROOT / "research" / "freq" / f"{AREA_FILE[area]}.txt").read_text(encoding="utf-8").splitlines()
    total = int(re.search(r"entries: (\d+)", lines[0]).group(1))
    limit = int(re.search(r"limit=(\d+)", lines[0]).group(1))
    entries = []
    for ln in lines[1:]:
        if "|" in ln:
            c, a = ln.split("|", 1)
            entries.append((int(c), a.strip()))
    cutoff = entries[-1][0] if total >= limit else 0
    return entries, cutoff


def main():
    apply = "--apply" in sys.argv
    man = json.loads((ROOT / "data" / "manifest.json").read_text(encoding="utf-8"))
    lists = {a: load_list(a) for a in AREA_FILE}
    shown = missing = 0
    for area in AREA_FILE:
        entries, cutoff = lists[area]
        print(f"\n## {area}  ({len(entries)} answers{'; cut off at count ' + str(cutoff) if cutoff else ', full list'})")
        for mt in [t for t in man["topics"] if t["category"] == area]:
            p = ROOT / "topics" / f"{mt['id']}.json"
            t = json.loads(p.read_text(encoding="utf-8"))
            forms = {norm(t["name"]), norm(t["qb"].get("q", ""))} | {norm(a) for a in t["accept"]}
            forms |= {norm(a) for a in ALIASES.get(mt["id"], [])}
            forms -= {norm(a) for a in EXCLUDE.get(mt["id"], [])}
            forms |= {untitle(f) for f in forms}
            forms.discard("")
            hits = [(c, a) for c, a in entries if norm(a) in forms or untitle(norm(a)) in forms]
            freq = None
            if hits:
                c, a = max(hits, key=lambda x: x[0])
                if c >= cutoff:
                    rank = 1 + sum(1 for cc, _ in entries if cc > c)
                    freq = {"rank": rank, "count": c, "list": area}
                    others = ", ".join(f"{aa} {cc}" for cc, aa in hits if aa != a)
                    print(f"   #{rank:<4} {c:>2}  {mt['id']:30s} ← {a}" + (f"   (also: {others})" if others else ""))
            if not freq:
                missing += 1
                print(f"   ---       {mt['id']:30s}   not on list" + (" above the cut-off" if hits else ""))
            else:
                shown += 1
            if apply:
                if freq:
                    t["freq"] = freq
                else:
                    t.pop("freq", None)
                save(p, t)
    print(f"\n{shown} topics ranked, {missing} not on their area's list" + (" — written to topics/" if apply else " (dry run)"))


if __name__ == "__main__":
    main()
