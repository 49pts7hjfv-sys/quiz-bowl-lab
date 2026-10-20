import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TIP = "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."


def C(cid, tier, t, k, rabbit=None):
    d = {"id": cid, "tier": tier, "t": t, "k": k, "n": 0}
    if rabbit:
        d["rabbit"] = rabbit
    return d


LINE = "<b><u>relativity</u></b> (accept <u>theory of relativity</u>, <u>special relativity</u>, or <u>general relativity</u>; prompt on <u>Einstein’s theory</u>)"

data = {
    "id": "theory-of-relativity",
    "name": "Theory of relativity",
    "mono": "REL",
    "category": "Physics",
    "qbCategory": "Science · Physics",
    "kicker": "Einstein’s theories of space and time · Special (1905), general (1915)",
    "dates": "Special theory, 1905; general theory, 1915",
    "briefing": "Albert Einstein’s theory of relativity comes in two parts. Special relativity (1905) says the speed of light is the same for everyone, so moving clocks tick slower and moving objects shrink, and it gave us E = mc². General relativity (1915) explains gravity as the bending of space and time by mass, which is why starlight curves around the Sun and why GPS satellites must correct their clocks.",
    "answerHtml": LINE,
    "accept": [
        "relativity",
        "theory of relativity",
        "theories of relativity",
        "relativity theory",
        "special relativity",
        "general relativity",
        "special theory of relativity",
        "general theory of relativity",
        "special and general relativity",
        "einsteins theory of relativity",
        "einsteins relativity"
    ],
    "prompt": [
        "einsteins theory",
        "einstein theory",
        "einsteins theories"
    ],
    "reject": [
        "quantum mechanics",
        "quantum theory",
        "quantum physics",
        "string theory",
        "unified field theory",
        "theory of everything",
        "gravity",
        "gravitation",
        "universal gravitation",
        "law of universal gravitation",
        "newtonian mechanics",
        "classical mechanics",
        "e mc",
        "e mc2",
        "e mc 2",
        "e mc squared",
        "mass energy equivalence",
        "time dilation",
        "length contraction",
        "spacetime",
        "space time",
        "curved spacetime",
        "equivalence principle",
        "principle of equivalence",
        "lorentz transformation",
        "lorentz transformations",
        "michelson morley experiment",
        "photoelectric effect",
        "brownian motion",
        "big bang",
        "big bang theory",
        "reactivity",
        "relativism",
        "cultural relativism",
        "moral relativism",
        "linguistic relativity",
        "galilean relativity",
        "galilean invariance",
        "albert einstein",
        "electromagnetism",
        "maxwells equations",
        "black holes",
        "gravitational waves"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Theory_of_relativity",
    "qb": {"q": "relativity", "found": 0, "tip": TIP},
    "sample": {"n": 0, "note": "no real tossups checked yet"},
    "tossups": [
        {
            "p": "This theory first appeared in a 1905 paper titled “On the Electrodynamics of Moving Bodies,” written by a patent clerk in Bern, Switzerland. That paper started from two ideas: the laws of physics are the same for all steadily moving observers, and the speed of light is the same for everyone.",
            "r": "For 10 points, name this theory by Albert Einstein, which comes in special and general versions."
        },
        {
            "p": "Hermann Minkowski [“min-KOFF-skee”], who had once taught math to this theory’s creator, recast part of it in 1908 using a four-dimensional “spacetime.” John Wheeler summed up another part of it by saying that spacetime tells matter how to move, and matter tells spacetime how to curve.",
            "r": "For 10 points, name these theories of Albert Einstein, which come in special and general forms."
        },
        {
            "p": "Muons created by cosmic rays high in the atmosphere should break apart before reaching the ground, but many survive because, according to this theory, their clocks tick slowly as seen from Earth. This theory also says that a fast-moving spaceship would look shorter along its direction of travel.",
            "r": "Those effects are called time dilation and length contraction. For 10 points, name this theory of Albert Einstein."
        },
        {
            "p": "In 1971, Joseph Hafele and Richard Keating flew atomic clocks around the world on passenger jets and found that the clocks had drifted from clocks left on the ground by the amounts this theory predicts. Clocks on GPS satellites run fast by about 38 microseconds a day, so engineers correct them using this theory.",
            "r": "For 10 points, name this theory by Albert Einstein, whose special and general forms describe space and time."
        },
        {
            "p": "Karl Schwarzschild [“SHVARTS-shilt”] published the first exact solution to the equations of one version of this theory in 1916, while serving in the German army during World War I. That solution describes what is now called a black hole.",
            "r": "For 10 points, name this theory, whose general version describes gravity as curved spacetime."
        },
        {
            "p": "Arthur Eddington led a 1919 expedition to photograph stars during a solar eclipse, and his measurements of starlight bending around the Sun supported this theory. This theory also explained a small, puzzling drift in Mercury’s orbit called precession.",
            "r": "For 10 points, name this theory by Albert Einstein, whose general form treats gravity as the curving of spacetime."
        },
        {
            "p": "The Pound–Rebka experiment at Harvard showed that gamma rays change frequency slightly as they travel up or down a tower, an effect of gravity predicted by this theory. Gravity Probe B confirmed that Earth’s rotation drags spacetime around with it, another prediction of this theory.",
            "r": "For 10 points, name this theory, developed by Albert Einstein in special and general versions."
        },
        {
            "p": "This theory’s creator called the idea behind one version of it his “happiest thought”: a person falling freely from a roof would not feel his own weight. That idea, the equivalence principle, says that the effects of gravity and of acceleration cannot be told apart.",
            "r": "For 10 points, name this theory by Albert Einstein, whose general form describes gravity as curved spacetime."
        },
        {
            "p": "Before this theory, George FitzGerald and Hendrik Lorentz each suggested that moving objects shrink along their direction of motion, to explain why the 1887 Michelson–Morley experiment found no sign of the “aether.” This theory showed that no aether was needed at all.",
            "r": "For 10 points, name this theory, which Albert Einstein first published in its special form in 1905."
        },
        {
            "p": "In this theory’s twin paradox, a twin who rockets to a distant star and back near the speed of light comes home younger than the twin who stayed on Earth. This theory also says that nothing with mass can travel as fast as light.",
            "r": "For 10 points, name this theory of Albert Einstein, which gave the world the equation E equals m c squared."
        },
        {
            "p": "In one thought experiment for this theory, lightning strikes both ends of a moving train, and a passenger and a person standing beside the tracks disagree about whether the two strikes happened at the same time. This theory showed that measurements of time and length depend on the observer’s motion.",
            "r": "For 10 points, name this theory of Albert Einstein, which comes in special and general versions."
        },
        {
            "p": "In 2015, the LIGO [“LY-go”] detectors in Louisiana and Washington State recorded gravitational waves from two colliding black holes, about a century after this theory predicted such waves. Rings and arcs of light appear when a galaxy cluster’s gravity bends light from objects behind it, an effect this theory explains.",
            "r": "For 10 points, name this theory whose general form describes gravity as the curving of spacetime."
        },
        {
            "p": "To keep the universe from expanding or shrinking, this theory’s creator added a cosmological constant to its equations, a move he reportedly later called his “biggest blunder.” Edwin Hubble’s 1929 evidence that the universe is expanding made that term seem unnecessary.",
            "r": "For 10 points, name this theory by Albert Einstein, which comes in special and general forms."
        },
        {
            "p": "This theory’s creator won the 1921 Nobel Prize in Physics for explaining the photoelectric effect rather than for this theory. The first part of this theory was published in 1905, the same year he explained Brownian motion.",
            "r": "This theory shows that mass can be turned into energy, as in E equals m c squared. For 10 points, name this theory."
        },
        {
            "p": "Calculations in one version of this theory use the Lorentz factor, which grows without limit as an object’s speed approaches the speed of light. As a teenager, this theory’s creator imagined what it would be like to chase a beam of light.",
            "r": "For 10 points, name this theory, whose special form predicts that moving clocks tick slowly."
        }
    ],
    "clues": [
        C("einstein", "giveaway", "Developed by Albert Einstein in two parts: a special theory (1905) and a general theory (1915)", ["albert einstein", "special theory", "general theory"], "Albert Einstein"),
        C("emc2", "giveaway", "Its special theory gave the equation E = mc²: mass and energy are equivalent", ["e = mc²", "mass and energy"]),
        C("curved-spacetime", "giveaway", "Its general theory describes gravity as the curving of spacetime by mass and energy", ["curving of spacetime", "gravity"], "Gravity"),
        C("time-dilation", "giveaway", "Moving clocks run slow (time dilation), and moving objects shrink along their direction of motion (length contraction)", ["time dilation", "length contraction"]),
        C("light-speed", "middle", "Its special theory says the speed of light in a vacuum is the same for every observer, and nothing with mass can reach it", ["speed of light", "every observer"]),
        C("twin", "middle", "The twin paradox: a twin who rockets away near light speed comes home younger than the twin who stayed on Earth", ["twin paradox", "younger"]),
        C("eclipse", "middle", "Arthur Eddington’s 1919 solar eclipse expedition measured starlight bending around the Sun, supporting the general theory", ["eddington", "1919", "eclipse"]),
        C("mercury", "middle", "The general theory explained a small, puzzling drift in Mercury’s orbit called precession", ["mercury", "precession"], "Precession"),
        C("gps", "middle", "GPS satellite clocks run fast by about 38 microseconds a day and must be corrected using it", ["gps", "38 microseconds"]),
        C("patent", "middle", "Its special theory was published in 1905, while its creator was a patent clerk in Bern, Switzerland", ["patent clerk", "bern", "1905"]),
        C("michelson", "middle", "The 1887 Michelson–Morley experiment found no sign of the “aether”; the special theory showed that none was needed", ["michelson–morley", "aether"], "Michelson–Morley experiment"),
        C("waves-black-holes", "middle", "The general theory predicts black holes and gravitational waves; LIGO first detected the waves in 2015", ["gravitational waves", "ligo", "2015"], "Black Holes"),
        C("nobel", "middle", "Its creator’s 1921 Nobel Prize was for the photoelectric effect, not for this theory", ["photoelectric effect", "1921"]),
        C("lensing", "middle", "The general theory explains how gravity bends light from distant objects into rings and arcs, called gravitational lensing", ["gravitational lensing", "rings and arcs"], "Gravitational lensing"),
        C("paper", "power", "The special theory first appeared in the 1905 paper “On the Electrodynamics of Moving Bodies”", ["electrodynamics of moving bodies"]),
        C("postulates", "power", "The special theory rests on two postulates: physics works the same for all steadily moving observers, and light’s speed is the same for everyone", ["postulates", "steadily moving observers"]),
        C("minkowski", "power", "Hermann Minkowski, who had once taught its creator math, recast the special theory in four-dimensional spacetime in 1908", ["minkowski", "four-dimensional", "1908"]),
        C("wheeler", "power", "John Wheeler’s summary of the general theory: spacetime tells matter how to move, and matter tells spacetime how to curve", ["wheeler", "tells matter how to move"]),
        C("muons", "power", "Muons made by cosmic rays high in the atmosphere reach the ground only because their clocks run slow", ["muons", "cosmic rays"]),
        C("hafele", "power", "The Hafele–Keating experiment (1971) flew atomic clocks around the world on passenger jets to test its predictions", ["hafele–keating", "atomic clocks", "1971"]),
        C("schwarzschild", "power", "Karl Schwarzschild published the first exact solution of its equations in 1916, while serving in World War I; it describes a black hole", ["schwarzschild", "1916"]),
        C("pound-rebka", "power", "The Pound–Rebka experiment at Harvard showed gamma rays changing frequency as they traveled up or down a tower", ["pound–rebka", "gamma rays", "tower"]),
        C("gravity-probe-b", "power", "Gravity Probe B confirmed that Earth’s rotation drags spacetime around with it", ["gravity probe b", "drags spacetime"]),
        C("happiest-thought", "power", "Its creator’s “happiest thought”: a person falling freely would not feel his own weight, the root of the equivalence principle", ["happiest thought", "equivalence principle", "falling freely"]),
        C("fitzgerald-lorentz", "power", "George FitzGerald and Hendrik Lorentz had proposed that moving objects shrink, to explain the Michelson–Morley result", ["fitzgerald", "hendrik lorentz"]),
        C("train", "power", "Thought experiment: lightning strikes both ends of a moving train, and two observers disagree about whether the strikes happened at the same time", ["lightning", "train", "same time"]),
        C("cosmological", "power", "Its creator added a cosmological constant to keep the universe from expanding or shrinking, reportedly later calling it his “biggest blunder”", ["cosmological constant", "biggest blunder"]),
        C("lorentz-factor", "power", "The Lorentz factor, used in its calculations, grows without limit as an object’s speed approaches the speed of light", ["lorentz factor", "without limit"]),
        C("chase-light", "power", "As a teenager, its creator imagined what it would be like to chase a beam of light", ["chase", "beam of light", "teenager"])
    ],
    "trap": {
        "title": "Special, general, or Einstein?",
        "body": "This topic asks for the theory as a whole, so “special relativity” and “general relativity” are both accepted here, the way real answer lines accept them when a question wants the overall theory. Many real tossups are about only one of the two, though, and then plain “relativity” may earn only a prompt. If every clue is about a life (birthplace, prizes, moving to Princeton), the answer is “Albert Einstein,” not his theory.",
        "fix": "1905, moving clocks, shrinking lengths, the twin paradox, muons, and E = mc² mean special relativity. 1915, curved spacetime, the equivalence principle, black holes, gravitational waves, and the 1919 eclipse mean general relativity. When the giveaway names both versions, “relativity” or “theory of relativity” is enough.",
        "line": "Real answer line: " + LINE
    },
    "tests": {
        "right": [
            "Theory of relativity",
            "relativity",
            "Special relativity",
            "General relativity",
            "Relativty",
            "Einstein's theory of relativity"
        ],
        "prompt": [
            "Einstein's theory"
        ],
        "wrong": [
            "Albert Einstein",
            "Quantum mechanics",
            "Gravity",
            "E = mc²",
            "Relativism",
            "Time dilation"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
