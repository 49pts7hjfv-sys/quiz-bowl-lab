"""Second round of consistency fixes (after the 2026-10-02 content review). Safe to re-run.

- cross-area facts the area reviewers flagged in each other's files
- short-poem titles in quotation marks, not italics
- BC/AD -> BCE/CE everywhere (the site's majority style)
- kickers: capital letter after " · ", and the 20 longest rewritten to the ~70-character spec
"""
import glob, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from merge_media import save  # noqa: E402

done = []


def load(tid):
    return json.loads((ROOT / "topics" / f"{tid}.json").read_text(encoding="utf-8"))


def put(t):
    save(ROOT / "topics" / f"{t['id']}.json", t)


def sub_all(t, old, new, where="tossups clues briefing"):
    """Replace text in tossups (p and r), clue texts and the briefing; return number of replacements."""
    n = 0
    if "tossups" in where:
        for tu in t["tossups"]:
            for k in ("p", "r"):
                if old in tu[k]:
                    tu[k] = tu[k].replace(old, new); n += 1
    if "clues" in where:
        for c in t["clues"]:
            if old in c["t"]:
                c["t"] = c["t"].replace(old, new); n += 1
    if "briefing" in where and old in t["briefing"]:
        t["briefing"] = t["briefing"].replace(old, new); n += 1
    return n


def fix(tid, pairs, where="tossups clues briefing"):
    t = load(tid)
    total = 0
    for old, new in pairs:
        k = sub_all(t, old, new, where)
        if k == 0 and old not in json.dumps(t, ensure_ascii=False):
            continue  # already applied
        total += k
    put(t)
    done.append((tid, total))
    return t


# 1. Cross-area facts flagged by reviewers ---------------------------------------------------
fix("achilles", [("dragged his body around the walls of Troy", "dragged his body behind his chariot")])
fix("joseph-stalin", [
    ("He signed a 1939 nonaggression pact with Adolf Hitler", "His government signed a 1939 nonaggression pact with Adolf Hitler"),
    ("He signed a nonaggression pact with Hitler in 1939", "His government signed a nonaggression pact with Hitler in 1939"),
    ("Signed a 1939 nonaggression pact with Hitler that divided up Poland, then was invaded by Germany in 1941’s Operation Barbarossa",
     "His government signed a 1939 nonaggression pact with Hitler that divided up Poland; Germany invaded anyway in 1941’s Operation Barbarossa"),
])
fix("george-washington", [("That is why he is called the “Father of His Country.”", "Americans still call him the “Father of His Country.”")])
fix("woodrow-wilson", [("directed a team of experts called “The Inquiry”", "organized a team of experts called “The Inquiry”"),
                       ("his closest adviser, directed “The Inquiry,”", "his closest adviser, organized “The Inquiry,”")])
fix("queen-victoria", [("“New Crowns for Old!”", "“New Crowns for Old Ones!”")])
fix("black-holes", [
    ("These astronomical bodies emit a radiation partially named for physicist Jacob Bekenstein, alongside Stephen Hawking.",
     "These astronomical bodies have an entropy formula named for physicist Jacob Bekenstein, alongside Stephen Hawking."),
    ("Part of the radiation these objects emit is named for physicist Jacob Bekenstein, alongside Hawking",
     "Their entropy formula is named for physicist Jacob Bekenstein, alongside Hawking"),
])

# lungs: prompt on its organ system, like heart / brain / kidneys
t = load("lungs")
if "respiratory system" in t["reject"]:
    t["reject"].remove("respiratory system")
if "respiratory system" not in t["prompt"]:
    t["prompt"].append("respiratory system")
t["tests"].setdefault("prompt", [])
if "Respiratory system" not in t["tests"]["prompt"]:
    t["tests"]["prompt"].append("Respiratory system")
t["answerHtml"] = "<b><u>Lungs</u></b> (accept book lungs; prompt on respiratory system; do not accept “heart”)"
t["trap"]["line"] = "Real answer line: <b><u>Lungs</u></b> (accept book lungs; prompt on respiratory system; do not accept heart)"
put(t); done.append(("lungs", "prompt on respiratory system"))

# 2. Short poems take quotation marks, not italics --------------------------------------------
POEMS = ["The New Colossus", "The Hollow Men", "Dulce et Decorum Est"]
for f in sorted(glob.glob(str(ROOT / "topics" / "*.json"))):
    raw = Path(f).read_text(encoding="utf-8")
    if not any(f"_{p}_" in raw for p in POEMS):
        continue
    t = json.loads(raw)
    def q(s):
        for p in POEMS:
            s = re.sub(r"_" + re.escape(p) + r"_([,.]?)", lambda m: f"“{p}{m.group(1)}”", s)
        return s
    for tu in t["tossups"]:
        tu["p"], tu["r"] = q(tu["p"]), q(tu["r"])
    for c in t["clues"]:
        c["t"] = q(c["t"])
    t["briefing"] = q(t["briefing"])
    for k in ("title", "body", "fix"):
        t["trap"][k] = q(t["trap"][k])
    put(t); done.append((t["id"], "poem title quotes"))

# 3. BC/AD -> BCE/CE ------------------------------------------------------------------------
def era(s):
    s = re.sub(r"(?<![\w“-])AD (\d{1,4})\b", r"\1 CE", s)          # AD 100 -> 100 CE
    s = re.sub(r"\b(\d{1,4}) AD\b(?!-)", r"\1 CE", s)                # 132 AD -> 132 CE
    s = re.sub(r"\b(\d{1,4}s?|century) BC\b(?!E)", r"\1 BCE", s)     # 399 BC / 700s BC / century BC
    return s
for f in sorted(glob.glob(str(ROOT / "topics" / "*.json"))):
    t = json.loads(Path(f).read_text(encoding="utf-8"))
    before = json.dumps(t, ensure_ascii=False)
    t["dates"], t["kicker"], t["briefing"] = era(t["dates"]), era(t["kicker"]), era(t["briefing"])
    for tu in t["tossups"]:
        tu["p"], tu["r"] = era(tu["p"]), era(tu["r"])
    for c in t["clues"]:
        c["t"] = era(c["t"])
    for k in ("body", "fix"):
        t["trap"][k] = era(t["trap"][k])
    t["qb"]["tip"] = era(t["qb"]["tip"])
    if json.dumps(t, ensure_ascii=False) != before:
        put(t); done.append((t["id"], "BCE/CE"))

# 4. Kickers ----------------------------------------------------------------------------------
KICK = {
    "albert-einstein": "Physicist behind relativity · Rethought space, time, and gravity",
    "candide": "Voltaire’s satirical novella · Mocks “the best of all possible worlds”",
    "cell-wall": "Rigid layer outside plant, fungal, and bacterial cells · Gives them shape",
    "cu-chulainn": "Ulster’s legendary champion · Fights in a frenzy called the “warp spasm”",
    "evolution": "Change in species over generations · Driven mainly by natural selection",
    "immanuel-kant": "German Enlightenment philosopher · Ethics of the categorical imperative",
    "ireland": "Ireland in myth and legend · The clues quiz bowl uses for the Emerald Isle",
    "loki": "Norse trickster god · Caused Baldr’s death, bound until Ragnarök",
    "moby-dick": "Herman Melville’s whaling novel · Captain Ahab hunts a white whale",
    "odyssey": "Homer’s epic of Odysseus’s trip home · The model for every journey story",
    "paradise-lost": "Milton’s epic of Satan’s fall · Grand English verse without rhyme",
    "refraction": "Bending of a wave entering a new material · Why straws look broken",
    "ribosomes": "Tiny organelles that build proteins · Read mRNA to link amino acids",
    "stephen-hawking": "British theoretical physicist · Black holes and A Brief History of Time",
    "the-adventures-of-tom-sawyer": "Mark Twain’s mischievous boy hero · A classic American boyhood adventure",
    "the-divine-comedy": "Dante’s journey through the afterlife · Medieval Europe’s great epic poem",
    "the-great-gatsby": "Fitzgerald’s Jazz Age novel · A millionaire’s doomed pursuit of lost love",
    "the-last-supper": "Leonardo’s mural of Jesus’s final meal · A landmark of linear perspective",
    "thor": "Norse god of thunder · Wields Mjolnir, dies fighting the world serpent",
    "volcanoes": "Vents where magma erupts from Earth’s crust · Common on the Ring of Fire",
}
caps = 0
for f in sorted(glob.glob(str(ROOT / "topics" / "*.json"))):
    t = json.loads(Path(f).read_text(encoding="utf-8"))
    k = KICK.get(t["id"], t["kicker"])
    if " · " in k:
        a, b = k.split(" · ", 1)
        if b[:1].islower() and not re.match(r"(c\.|e\.g\.|vs\.)\s", b):
            b = b[0].upper() + b[1:]; caps += 1
        k = f"{a} · {b}"
    if k != t["kicker"]:
        t["kicker"] = k; put(t)
print(f"capitalized after the dot: {caps}; rewrote {len(KICK)} long kickers")
for d in done:
    print("  ", d)
