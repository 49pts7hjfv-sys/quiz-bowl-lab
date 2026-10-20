import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TIP = "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."


def C(cid, tier, t, k, rabbit=None):
    d = {"id": cid, "tier": tier, "t": t, "k": k, "n": 0}
    if rabbit:
        d["rabbit"] = rabbit
    return d


LINE = "<b><u>Hooke’s law</u></b> (prompt on <u>Hooke</u> or <u>elasticity</u>)"

data = {
    "id": "hookes-law",
    "name": "Hooke’s law",
    "mono": "HK",
    "category": "Physics",
    "qbCategory": "Science · Physics",
    "kicker": "A spring’s stretch grows with the force · F = −kx",
    "dates": "Published as an anagram, 1676; solved, 1678",
    "briefing": "Hooke’s law says that the force needed to stretch or squeeze a spring is proportional to how far you stretch or squeeze it: pull twice as hard and it stretches twice as far. Robert Hooke first hid the idea in a scrambled Latin anagram in 1676, then revealed it two years later as “ut tensio, sic vis,” meaning “as the extension, so the force.” The rule works only up to a spring’s elastic limit.",
    "answerHtml": LINE,
    "accept": [
        "hookes law",
        "hooke law",
        "hooks law",
        "hookes law of elasticity"
    ],
    "prompt": [
        "hooke",
        "robert hooke",
        "elasticity",
        "spring force",
        "restoring force"
    ],
    "reject": [
        "spring constant",
        "youngs modulus",
        "young modulus",
        "elastic potential energy",
        "potential energy",
        "simple harmonic motion",
        "harmonic motion",
        "boyles law",
        "hubbles law",
        "ohms law",
        "coulombs law",
        "charles law",
        "henrys law",
        "newtons law",
        "newtons laws",
        "newtons laws of motion",
        "newtons second law",
        "newtons third law",
        "hookes joint",
        "universal joint",
        "tension",
        "stress",
        "strain",
        "elastic limit",
        "plasticity",
        "torsion"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Hooke%27s_law",
    "qb": {"q": "Hooke", "found": 0, "tip": TIP},
    "sample": {"n": 0, "note": "no real tossups checked yet"},
    "tossups": [
        {
            "p": "This law was first published in 1676 as the scrambled Latin anagram “ceiiinosssttuv.” Two years later, its discoverer revealed the answer: “ut tensio, sic vis” [“oot TEN-see-oh, sik VEES”], meaning “as the extension, so the force.”",
            "r": "For 10 points, name this law stating that the force on a spring is proportional to how far it is stretched."
        },
        {
            "p": "Isaac Newton’s line about “standing on the shoulders of giants” appeared in a letter to this law’s namesake, who later claimed that Newton had taken his idea that gravity follows an inverse-square law. This law can be written with a spring constant measured in newtons per meter.",
            "r": "For 10 points, name this law, written F equals negative k x, that describes how springs stretch."
        },
        {
            "p": "A quantity named for Thomas Young extends this law to solid materials by stating that stress is proportional to strain. Beyond a point called the elastic limit, a material stops obeying this law and is permanently stretched out of shape.",
            "r": "For 10 points, name this law about springs, written F equals negative k x, where k is the spring constant."
        },
        {
            "p": "Chemists predict where a chemical bond will absorb infrared light by treating the bond as a spring that obeys this law, so stiffer bonds vibrate at higher frequencies. A mass hanging from a spring that obeys this law bobs up and down in simple harmonic motion.",
            "r": "For 10 points, name this law stating that a spring’s restoring force is proportional to its stretch."
        },
        {
            "p": "This law’s namesake was the Royal Society’s first Curator of Experiments and helped survey London after the Great Fire of 1666. In his 1665 book _Micrographia_, he coined the word “cell” after looking at thin slices of cork through a microscope.",
            "r": "For 10 points, name this law, written F equals negative k x, that describes springs."
        },
        {
            "p": "On a graph of force against stretch, this law appears as a straight line through the origin, and the slope of that line is the spring constant. The minus sign in this law shows that a spring pulls back opposite to its stretch.",
            "r": "For 10 points, name this law, written F equals negative k x, that describes springs."
        },
        {
            "p": "Because the force in this law grows steadily with the stretch, a spring stretched a distance x stores elastic potential energy equal to one-half k x squared. So stretching such a spring twice as far stores four times as much energy.",
            "r": "Spring scales work because of it. For 10 points, name this law, written F equals negative k x."
        },
        {
            "p": "According to this law, two identical springs hung side by side act like one spring that is twice as stiff, while the same two springs joined end to end are only half as stiff. A larger spring constant in this law means a stiffer spring.",
            "r": "For 10 points, name this law stating that the force needed to stretch a spring is proportional to the stretch."
        },
        {
            "p": "Any system whose restoring force obeys this law is called a harmonic oscillator, because it vibrates in simple harmonic motion. A real spring obeys this law only until it reaches its elastic limit, past which it stays permanently stretched.",
            "r": "Spring scales use it to measure weight. For 10 points, name this law, written F equals negative k x."
        },
        {
            "p": "This law’s namesake quarreled with Christiaan Huygens [“HY-gunz”] over who first invented the balance spring, the tiny coiled spring that keeps time in a watch. In this law, a stiffer spring has a larger spring constant, measured in newtons per meter.",
            "r": "For 10 points, name this law stating that the force on a spring is proportional to its stretch."
        },
        {
            "p": "For a mass on a spring that obeys this law, the period of each bounce equals two pi times the square root of the mass divided by the spring constant, so a heavier mass bobs more slowly.",
            "r": "That bouncing is called simple harmonic motion. For 10 points, name this law, written F equals negative k x."
        },
        {
            "p": "A twisting version of this law, in which the twist of a thin wire is proportional to the turning force on it, made possible the torsion balances of Charles-Augustin de Coulomb [“KOO-lohm”] and Henry Cavendish. Its minus sign shows that the force points back toward the resting position.",
            "r": "For 10 points, name this law stating that the force on a spring is proportional to how far it is stretched."
        },
        {
            "p": "This law was explained in its discoverer’s 1678 lecture _De Potentia Restitutiva_ [“day poh-TEN-tee-ah res-tih-too-TEE-vah”], or _Of Spring_, which revealed the meaning of an anagram he had published two years earlier. That anagram’s Latin solution means “as the extension, so the force.”",
            "r": "For 10 points, name this law stating that a spring’s stretch is proportional to the force on it."
        },
        {
            "p": "Under this law, a spring with a constant of 200 newtons per meter stretches 10 centimeters when pulled with a force of 20 newtons. A graph of force against stretch for that spring is a straight line with a slope of 200 newtons per meter.",
            "r": "For 10 points, name this law relating a spring’s stretch to the force on it, written F equals negative k x."
        },
        {
            "p": "This law’s namesake also gives his name to a universal joint that lets a rotating shaft drive another shaft set at an angle, as in a car’s driveshaft. Earlier, he worked as Robert Boyle’s assistant and built the air pump that Boyle used to study gases.",
            "r": "For 10 points, name this law, written F equals negative k x, that describes springs."
        }
    ],
    "clues": [
        C("proportional", "giveaway", "The force needed to stretch or compress a spring is proportional to how far it is stretched or compressed", ["proportional", "stretched", "compressed"]),
        C("formula", "giveaway", "Written F = −kx, where k is the spring constant and x is the stretch", ["spring constant", "f = −kx"]),
        C("spring-scales", "giveaway", "Explains spring scales (newton meters), which measure weight by how far a spring stretches", ["spring scales", "newton meters", "weight"]),
        C("doubling", "giveaway", "Doubling the force on a spring doubles its stretch", ["doubling", "doubles"]),
        C("elastic-limit", "middle", "Works only up to the elastic limit; stretched past it, a spring is permanently bent out of shape", ["elastic limit", "permanently"]),
        C("units", "middle", "The spring constant is measured in newtons per meter; a stiffer spring has a larger one", ["newtons per meter", "stiffer"]),
        C("graph", "middle", "A graph of force against stretch is a straight line through the origin, with the spring constant as its slope", ["straight line", "slope"]),
        C("minus-sign", "middle", "The minus sign shows that the restoring force points back toward the resting position, opposite to the stretch", ["minus sign", "restoring force"]),
        C("energy", "middle", "A stretched spring stores elastic potential energy equal to one-half k x squared", ["elastic potential energy", "one-half"], "Potential energy"),
        C("shm", "middle", "A mass on such a spring moves in simple harmonic motion; its period is 2π times the square root of m divided by k", ["simple harmonic motion", "period"], "Pendulums"),
        C("micrographia", "middle", "Its namesake coined the word “cell” after viewing slices of cork in his book _Micrographia_ (1665)", ["micrographia", "cork", "cell"]),
        C("anagram", "power", "First published in 1676 as the Latin anagram “ceiiinosssttuv”", ["anagram", "ceiiinosssttuv", "1676"]),
        C("ut-tensio", "power", "Solved in 1678 as “ut tensio, sic vis”: “as the extension, so the force”", ["ut tensio", "sic vis", "1678"]),
        C("lecture", "power", "Explained in the 1678 lecture _De Potentia Restitutiva_, or _Of Spring_", ["de potentia restitutiva", "of spring"]),
        C("young", "power", "Young’s modulus extends it to solid materials: stress is proportional to strain", ["young’s modulus", "stress", "strain"]),
        C("infrared", "power", "Treating chemical bonds as springs that obey it predicts where they absorb infrared light; stiffer bonds vibrate faster", ["infrared", "chemical bonds"], "Infrared spectroscopy"),
        C("series-parallel", "power", "Two identical springs side by side are twice as stiff as one; joined end to end, they are half as stiff", ["side by side", "end to end", "twice as stiff"]),
        C("oscillator", "power", "Any system whose restoring force obeys it is called a harmonic oscillator", ["harmonic oscillator"]),
        C("torsion", "power", "A twisting version, with the twist of a thin wire proportional to the turning force, made the torsion balances of Coulomb and Cavendish work", ["torsion balances", "cavendish", "coulomb"], "Torque"),
        C("newton-letter", "power", "Isaac Newton’s line about “standing on the shoulders of giants” appeared in a letter to its namesake", ["shoulders of giants", "letter"], "Isaac Newton"),
        C("inverse-square", "power", "Its namesake claimed that Newton had taken his idea that gravity follows an inverse-square law", ["inverse-square", "gravity"]),
        C("curator", "power", "Its namesake was the Royal Society’s first Curator of Experiments", ["curator of experiments", "royal society"]),
        C("great-fire", "power", "Its namesake helped survey London after the Great Fire of 1666", ["great fire", "1666", "survey"]),
        C("huygens", "power", "Its namesake quarreled with Christiaan Huygens over who first invented the balance spring for watches", ["huygens", "balance spring", "watch"]),
        C("boyle", "power", "Its namesake worked as Robert Boyle’s assistant and built the air pump Boyle used to study gases", ["boyle", "air pump"], "Boyle’s law"),
        C("joint", "power", "Its namesake’s name is also on a universal joint used in car driveshafts", ["universal joint", "driveshafts"])
    ],
    "trap": {
        "title": "Law, constant, or motion?",
        "body": "Spring tossups have several look-alike answers. This law is the rule F = −kx; the spring constant k is just one number in it, simple harmonic motion is the bouncing that results, and Young’s modulus is the version for solid materials. Clues about Robert Boyle’s air pump can also lure a wrong buzz of “Boyle’s law,” since this law’s namesake built that pump, and answering just “Hooke” earns only a prompt.",
        "fix": "Proportional stretch, F = −kx, the 1676 anagram, and “ut tensio, sic vis” mean this law. If the giveaway asks for “this quantity” measured in newtons per meter, say spring constant; for the back-and-forth motion, say simple harmonic motion; for the pressure and volume of a gas, say Boyle’s law.",
        "line": "Real answer line: " + LINE
    },
    "tests": {
        "right": [
            "Hooke's law",
            "Hookes law",
            "Hooke law",
            "Hooks law",
            "Hooke’s Law",
            "Hooke's law of elasticity"
        ],
        "prompt": [
            "Hooke",
            "Robert Hooke",
            "Elasticity"
        ],
        "wrong": [
            "Spring constant",
            "Boyle's law",
            "Young's modulus",
            "Simple harmonic motion",
            "Newton's third law",
            "Hubble's law"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
