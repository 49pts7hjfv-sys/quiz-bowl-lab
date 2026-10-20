import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TIP = "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."


def C(cid, tier, t, k, rabbit=None):
    d = {"id": cid, "tier": tier, "t": t, "k": k, "n": 0}
    if rabbit:
        d["rabbit"] = rabbit
    return d


LINE = "<b><u>Ampère’s law</u></b> (accept <u>Ampère’s circuital law</u> or <u>Ampère–Maxwell law</u>; prompt on <u>Ampère</u> or <u>Maxwell’s equations</u>; do not accept “Biot–Savart law” or “Faraday’s law”)"

data = {
    "id": "amperes-law",
    "name": "Ampère’s law",
    "mono": "ACL",
    "category": "Physics",
    "qbCategory": "Science · Physics",
    "kicker": "Magnetic fields from electric currents · One of Maxwell’s equations",
    "dates": "Named for André-Marie Ampère; corrected by Maxwell in the early 1860s",
    "briefing": "Ampère’s law says that if you add up the magnetic field all the way around any closed loop, you get a number set by the electric current passing through that loop. Physicists use it to find the magnetic field around a straight wire or inside a coil without hard calculations. James Clerk Maxwell later added a missing piece, and the corrected law became one of the four Maxwell’s equations that describe electricity, magnetism, and light.",
    "answerHtml": LINE,
    "accept": [
        "amperes law",
        "ampere law",
        "amperes circuital law",
        "ampere circuital law",
        "ampere maxwell law",
        "amperes maxwell law",
        "maxwell ampere law",
        "ampere maxwell equation",
        "law of ampere"
    ],
    "prompt": [
        "ampere",
        "amperes",
        "andre marie ampere",
        "andre ampere",
        "maxwells equations",
        "maxwell equations",
        "maxwells equation",
        "circuital law"
    ],
    "reject": [
        "biot savart law",
        "biot savart",
        "faradays law",
        "faraday law",
        "faradays law of induction",
        "lenzs law",
        "gausss law",
        "gauss law",
        "gausss law for magnetism",
        "coulombs law",
        "ohms law",
        "kirchhoffs law",
        "kirchhoffs laws",
        "amperes force law",
        "ampere force law",
        "lorentz force",
        "lorentz force law",
        "right hand rule",
        "magnetic field",
        "magnetic fields",
        "electric current",
        "current",
        "displacement current",
        "electromagnetic induction",
        "hookes law",
        "maxwells demon"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Amp%C3%A8re%27s_circuital_law",
    "qb": {"q": "Ampère’s law", "found": 0, "tip": TIP},
    "sample": {"n": 0, "note": "no real tossups checked yet"},
    "tossups": [
        {
            "p": "This law gives the wrong answer in the gap of a charging capacitor unless it includes a “displacement current” term, which James Clerk Maxwell added in the early 1860s. With that term, a changing electric field makes a magnetic field, just as a current does.",
            "r": "For 10 points, name this law relating the magnetic field around a closed loop to the electric current passing through the loop."
        },
        {
            "p": "Using this law with a circular path around a long, straight wire shows that the wire’s magnetic field weakens in proportion to one over the distance from the wire. This law plays the same role for magnetism that Gauss’s law plays for electricity, making problems with lots of symmetry easy.",
            "r": "It is applied using closed paths called Amperian loops. For 10 points, name this law, one of Maxwell’s equations."
        },
        {
            "p": "Inside a doughnut-shaped coil called a toroid, this law shows that the magnetic field weakens with distance from the doughnut’s center, while outside the coil the field is zero. This law also gives the nearly uniform field inside a long, straight coil called a solenoid.",
            "r": "For 10 points, name this law, one of Maxwell’s equations, that links a magnetic field to the electric current that makes it."
        },
        {
            "p": "Outside a coaxial cable whose inner wire and outer sleeve carry equal currents in opposite directions, this law predicts no magnetic field at all, since no net current passes through a loop drawn around the cable. When using this law, only the current that passes through the chosen closed path counts.",
            "r": "For 10 points, name this law relating the magnetic field around any closed loop to the current through it."
        },
        {
            "p": "James Clerk Maxwell called this law’s namesake “the Newton of electricity.” That namesake began his experiments in 1820, within weeks of learning that Hans Christian Ørsted had made a compass needle swing using a current.",
            "r": "For 10 points, name this law, named for a French physicist, about the magnetic field produced by electric currents."
        },
        {
            "p": "The original form of this law works only for steady currents that do not change over time. Maxwell’s corrected version of this law, together with Faraday’s law of induction, predicted waves of electric and magnetic fields traveling at the speed of light.",
            "r": "For 10 points, name this law, one of Maxwell’s equations, which says that electric currents produce magnetic fields that circle around them."
        },
        {
            "p": "The Biot–Savart [“bee-OH suh-VAR”] law gives the same answers as this law, but this law is far easier to use when a problem has a lot of symmetry. The constant in this law, mu-naught, is called the permeability of free space.",
            "r": "This law says that the magnetic field added up around a closed loop is proportional to the current through it. For 10 points, name this law."
        },
        {
            "p": "This law contains the constant mu-naught, the permeability of free space, which is about four pi times ten to the negative seventh in SI units. That constant multiplies the current that passes through the closed path in this law.",
            "r": "For 10 points, name this law that links the magnetic field around a loop to the current through it, one of Maxwell’s four equations."
        },
        {
            "p": "This law’s namesake called his new field of study “electrodynamics.” When using this law around a wire, a right-hand rule gives the direction of the magnetic field: point your thumb along the current, and your fingers curl the way the field circles.",
            "r": "For 10 points, name this law, one of Maxwell’s equations, about the magnetic fields made by currents."
        },
        {
            "p": "This law’s namesake also showed in 1820 that two parallel wires carrying currents in the same direction attract each other, a result described by a separate “force law” named for him. James Clerk Maxwell later added a displacement current term to this law.",
            "r": "This law relates the magnetic field around a closed loop to the current inside it. For 10 points, name this law."
        },
        {
            "p": "This law’s namesake, one of 72 scientists whose names are engraved on the Eiffel Tower, was largely self-taught and became a professor at the École Polytechnique [“ay-KOHL po-lee-tek-NEEK”] in Paris. Maxwell’s corrected version of this law is one of his four famous equations.",
            "r": "This law relates the magnetic field around a closed loop to the current passing through it. For 10 points, name this law."
        },
        {
            "p": "This law shows that the magnetic field just outside a long, tightly wound solenoid is nearly zero, while inside it equals mu-naught times the number of turns per meter times the current. It works easily around a straight wire, where the field is equally strong all the way around a circle.",
            "r": "For 10 points, name this law, one of Maxwell’s equations, that links a magnetic field to the current that makes it."
        },
        {
            "p": "Faraday’s law says that a changing magnetic field makes an electric field, while the corrected form of this law says that a changing electric field makes a magnetic field. That pairing led James Clerk Maxwell to predict that light is an electromagnetic wave.",
            "r": "For 10 points, name this law relating the magnetic field around a closed loop to the current through the loop."
        },
        {
            "p": "Applying this law inside a thick wire with current spread evenly across it shows that the magnetic field grows in proportion to the distance from the wire’s center, then weakens outside the wire. The magnetic field lines around the wire form closed circles.",
            "r": "For 10 points, name this law, one of Maxwell’s equations, that relates a magnetic field to the electric current producing it."
        },
        {
            "p": "The left side of this law adds up the magnetic field all the way around a closed path, a quantity called the field’s circulation. This law’s namesake proposed that tiny loops of current inside magnets cause their magnetism.",
            "r": "The right side of this law is mu-naught times the current through the path. For 10 points, name this law."
        }
    ],
    "clues": [
        C("loop", "giveaway", "Relates the magnetic field around a closed loop to the electric current passing through the loop", ["closed loop", "magnetic field", "current"], "Magnetic fields"),
        C("maxwell-eq", "giveaway", "One of the four Maxwell’s equations, along with Gauss’s law, Gauss’s law for magnetism, and Faraday’s law", ["maxwell’s equations", "four"]),
        C("namesake", "giveaway", "Named for a French physicist whose name is also the SI unit of current", ["french physicist", "unit of current"], "Electric current"),
        C("wire-field", "giveaway", "Used to show that the magnetic field around a long, straight wire weakens in proportion to one over the distance", ["straight wire", "one over the distance"]),
        C("displacement", "middle", "James Clerk Maxwell added a “displacement current” term in the early 1860s, so a changing electric field also makes a magnetic field", ["displacement current", "maxwell", "changing electric field"]),
        C("capacitor", "middle", "Without Maxwell’s term, it gives the wrong answer in the gap of a charging capacitor", ["capacitor", "gap"], "Capacitors"),
        C("light", "middle", "Maxwell’s corrected version, with Faraday’s law, predicted electromagnetic waves traveling at the speed of light", ["electromagnetic waves", "speed of light"]),
        C("faraday-pair", "middle", "Faraday’s law: a changing magnetic field makes an electric field; its corrected form: a changing electric field makes a magnetic field", ["faraday’s law", "changing magnetic field"], "Michael Faraday"),
        C("solenoid", "middle", "Gives the nearly uniform field inside a long solenoid (mu-naught × turns per meter × current); just outside, the field is nearly zero", ["solenoid", "turns per meter"]),
        C("closed-path", "middle", "Applied by drawing an imaginary closed path, often a circle around a wire, and adding up the magnetic field along it", ["imaginary closed path", "circle"]),
        C("gauss-analogy", "middle", "Plays the same role for magnetism that Gauss’s law plays for electricity, making symmetric problems easy", ["gauss’s law", "symmetric"], "Gauss’s law"),
        C("right-hand", "middle", "Right-hand rule: point your thumb along the current, and your fingers curl the way the magnetic field circles", ["right-hand rule", "thumb"]),
        C("mu-naught", "middle", "Its constant is mu-naught, the permeability of free space, about 4π × 10⁻⁷ in SI units", ["mu-naught", "permeability of free space"]),
        C("biot-savart", "power", "The Biot–Savart law gives the same fields but is much harder to use when a problem has lots of symmetry", ["biot–savart", "symmetry"]),
        C("toroid", "power", "Inside a doughnut-shaped toroid coil, the field weakens with distance from the center; outside the coil, it is zero", ["toroid", "doughnut-shaped"]),
        C("coax", "power", "Outside a coaxial cable carrying equal and opposite currents, it predicts no magnetic field at all", ["coaxial cable", "equal and opposite"]),
        C("thick-wire", "power", "Inside a thick wire with evenly spread current, the field grows in proportion to the distance from the center", ["thick wire", "proportion"]),
        C("steady", "power", "Its original form works only for steady currents that do not change over time", ["steady currents"]),
        C("newton-of-electricity", "power", "James Clerk Maxwell called its namesake “the Newton of electricity”", ["newton of electricity"]),
        C("orsted", "power", "Its namesake began his experiments in 1820, within weeks of learning of Hans Christian Ørsted’s compass-needle discovery", ["ørsted", "oersted", "1820"]),
        C("electrodynamics", "power", "Its namesake called his new field of study “electrodynamics”", ["electrodynamics"]),
        C("force-law", "power", "Its namesake showed in 1820 that parallel wires carrying currents in the same direction attract, described by a separate force law", ["force law", "parallel wires", "attract"]),
        C("eiffel", "power", "Its namesake is one of 72 scientists whose names are engraved on the Eiffel Tower", ["eiffel tower", "72"]),
        C("polytechnique", "power", "Its namesake was largely self-taught and became a professor at the École Polytechnique in Paris", ["self-taught", "école polytechnique"]),
        C("molecular", "power", "Its namesake proposed that tiny loops of current inside magnets cause their magnetism", ["tiny loops", "magnetism"]),
        C("circulation", "power", "Its left side, the magnetic field added up all the way around a closed path, is called the field’s circulation", ["circulation", "closed path"])
    ],
    "trap": {
        "title": "Which electromagnetism law?",
        "body": "Several laws of electricity and magnetism show up together. This law links the magnetic field circling a closed loop to the current passing through it; Gauss’s law links the electric field through a closed surface to the charge inside; Faraday’s law says a changing magnetic field makes a voltage; and the Biot–Savart law builds up a magnetic field piece by piece. The same French physicist also has a separate force law about parallel wires, and the unit of current carries his name, so saying just “Ampère” earns only a prompt.",
        "fix": "Closed loops (Amperian loops), the current enclosed, solenoids, toroids, and Maxwell’s displacement current mean this law. Closed surfaces and enclosed charge mean Gauss’s law; induction, generators, and Lenz’s law mean Faraday’s law; adding up the field from tiny pieces of wire means the Biot–Savart law.",
        "line": "Real answer line: " + LINE
    },
    "tests": {
        "right": [
            "Ampère's law",
            "Amperes law",
            "Ampere's circuital law",
            "Ampere-Maxwell law",
            "Amperes lw"
        ],
        "prompt": [
            "Ampère",
            "Maxwell's equations"
        ],
        "wrong": [
            "Biot-Savart law",
            "Faraday's law",
            "Gauss's law",
            "Ampère's force law",
            "Electric current",
            "Magnetic field"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
