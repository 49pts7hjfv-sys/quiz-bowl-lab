import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TIP = "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."


def C(cid, tier, t, k, rabbit=None):
    d = {"id": cid, "tier": tier, "t": t, "k": k, "n": 0}
    if rabbit:
        d["rabbit"] = rabbit
    return d


LINE = "<b><u>Gauss’s law</u></b> (accept <u>Gauss’s flux theorem</u>; prompt on <u>Gauss</u> or <u>Maxwell’s equations</u>; do not accept “Coulomb’s law,” “Faraday’s law,” “Ampère’s law,” or “Gauss’s law for magnetism”)"

data = {
    "id": "gausss-law",
    "name": "Gauss’s law",
    "mono": "GSL",
    "category": "Physics",
    "qbCategory": "Science · Physics",
    "kicker": "Flux through a closed surface · Set by the charge inside",
    "dates": "Worked out by Gauss, 1835; part of Maxwell’s equations, 1860s",
    "briefing": "Imagine wrapping an invisible bubble around some electric charges and counting the field lines poking out of it. Gauss’s law says that count, called the electric flux, depends only on how much charge is inside the bubble, not on the bubble’s size or shape. Named for the German mathematician Carl Friedrich Gauss, it is one of the four Maxwell’s equations that describe electricity and magnetism.",
    "answerHtml": LINE,
    "accept": [
        "gausss law",
        "gauss law",
        "gauss s law",
        "gausss laws",
        "gausss law for electricity",
        "gauss law for electricity",
        "gausss law for electric fields",
        "gausss law of electricity",
        "gausss flux theorem",
        "gauss flux theorem",
        "law of gauss"
    ],
    "prompt": [
        "gauss",
        "carl friedrich gauss",
        "karl friedrich gauss",
        "carl gauss",
        "gausss theorem",
        "maxwells equations",
        "maxwell equations",
        "maxwells equation"
    ],
    "reject": [
        "gausss law for magnetism",
        "gauss law for magnetism",
        "gausss law for magnetic fields",
        "gausss law of magnetism",
        "gausss law for gravity",
        "gauss law for gravity",
        "coulombs law",
        "faradays law",
        "faradays law of induction",
        "amperes law",
        "ampere maxwell law",
        "biot savart law",
        "lenzs law",
        "ohms law",
        "kirchhoffs law",
        "divergence theorem",
        "gaussian surface",
        "gaussian distribution",
        "electric flux",
        "electric field",
        "electric charge",
        "maxwells demon"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Gauss%27s_law",
    "qb": {"q": "Gauss's law", "found": 0, "tip": TIP},
    "sample": {"n": 0, "note": "no real tossups checked yet"},
    "tossups": [
        {
            "p": "Joseph-Louis Lagrange stated a version of this law in 1773 while studying the gravitational pull of ellipsoids, and its namesake reached it again in 1835. A gravity version of this law says the gravitational flux through a closed surface depends only on the mass inside.",
            "r": "For 10 points, name this law, one of Maxwell’s equations, which says the electric flux through a closed surface is proportional to the charge enclosed."
        },
        {
            "p": "In Michael Faraday’s 1843 ice-pail experiment, lowering a charged ball into a metal pail without touching it produced an equal charge on the pail’s outside, a result this law explains. This law also shows that any extra charge on a solid conductor ends up on its outer surface.",
            "r": "For 10 points, name this law relating the electric flux through a closed surface to the charge inside it."
        },
        {
            "p": "Oliver Heaviside used vector notation in the 1880s to condense James Clerk Maxwell’s theory into four short equations, and this law is often listed first among them. Unlike Coulomb’s law, this law stays true even when charges are moving.",
            "r": "For 10 points, name this law stating that the electric flux through any closed surface equals the enclosed charge divided by epsilon-naught."
        },
        {
            "p": "Applying this law to a point charge at the center of a cube shows that each of the cube’s six faces carries one-sixth of the total flux. Doubling the charge inside any closed surface doubles the total flux through that surface, no matter its shape.",
            "r": "For 10 points, name this law, one of Maxwell’s equations, about electric flux through closed surfaces."
        },
        {
            "p": "Because a point charge’s field weakens with the square of the distance while a sphere’s area grows with the square of its radius, the flux through a sphere around the charge is the same at any size, a fact at the heart of this law. Applied to that sphere, this law gives back Coulomb’s law.",
            "r": "For 10 points, name this law, one of Maxwell’s equations, that relates electric flux to enclosed charge."
        },
        {
            "p": "Using this law with a short cylinder that pokes through a huge flat sheet of charge shows that the sheet’s field has the same strength at every distance. Using it with a long cylinder around a charged wire shows that the wire’s field weakens in proportion to one over the distance.",
            "r": "For 10 points, name this law relating the electric flux through a closed surface to the charge enclosed."
        },
        {
            "p": "This law shows that outside a uniformly charged ball, the electric field is the same as if all the charge sat at the center, while inside the ball, the field grows steadily from zero at the center to its largest value at the surface.",
            "r": "Inside a hollow charged metal shell, it says the field is zero. For 10 points, name this law about electric flux through closed surfaces."
        },
        {
            "p": "A companion equation, this law’s version for magnetism, says the total magnetic flux out of any closed surface is always zero, because no one has found a lone magnetic pole. Both that equation and this law appear among the four Maxwell’s equations.",
            "r": "For 10 points, name this law stating that the electric flux through a closed surface is proportional to the enclosed charge."
        },
        {
            "p": "The quantity at the center of this law is found by multiplying the electric field by the area it passes straight through, and it can be pictured as the number of field lines crossing a surface. That quantity is measured in newton square meters per coulomb.",
            "r": "For 10 points, name this law, one of Maxwell’s equations, which says that quantity through a closed surface depends only on the charge inside."
        },
        {
            "p": "This law’s namesake built an early electric telegraph with Wilhelm Weber in 1833, and a non-SI unit for magnetic fields, equal to one ten-thousandth of a tesla, also honors him. That German mathematician was nicknamed the “Prince of Mathematicians.”",
            "r": "For 10 points, name this law relating the electric flux through any closed surface to the charge inside it."
        },
        {
            "p": "A version of this law for gravity shows that inside a hollow planet, a visitor would feel no pull from the shell at all, and that outside a planet, its gravity acts as if all its mass sat at the center. Isaac Newton had proved those results long before with geometry, in his shell theorem.",
            "r": "For 10 points, name this law, one of Maxwell’s equations, which in its electric form relates flux through a closed surface to the enclosed charge."
        },
        {
            "p": "Applying this law to a tiny pillbox-shaped surface straddling the surface of a charged conductor shows that the electric field just outside points straight out and equals the surface charge density divided by the permittivity of free space.",
            "r": "Physicists choose the shape of the imaginary closed surface to match a problem’s symmetry when using it. For 10 points, name this law about electric flux."
        },
        {
            "p": "A math result sometimes named for Mikhail Ostrogradsky [“oss-truh-GRAD-skee”], the divergence theorem, turns the version of this law written for a whole closed surface into a version that holds at every single point in space. James Clerk Maxwell included this law in his famous set of equations.",
            "r": "For 10 points, name this law relating electric flux through a closed surface to the charge enclosed."
        },
        {
            "p": "For charges sitting still, this law and Coulomb’s law contain the same physics, and each can be derived from the other. This law is easiest to use when a problem has high symmetry, such as a charged sphere, a long straight wire, or a huge flat sheet.",
            "r": "For 10 points, name this law relating the electric flux through a closed surface to the charge it encloses."
        },
        {
            "p": "A closed surface that surrounds both a positive and a negative charge of equal size has zero total flux through it under this law, and so does a surface with every charge outside it. The field lines from an outside charge enter such a surface on one side and leave on the other.",
            "r": "For 10 points, name this law that says the electric flux through a closed surface equals the enclosed charge divided by epsilon-naught."
        }
    ],
    "clues": [
        C("definition", "giveaway", "The electric flux through any closed surface equals the charge enclosed divided by the permittivity of free space (ε₀)", ["electric flux", "closed surface", "charge enclosed"]),
        C("maxwell", "giveaway", "One of the four Maxwell’s equations, along with Faraday’s law and Ampère’s law", ["maxwell’s equations", "four"], "Ampère’s law"),
        C("namesake", "giveaway", "Named for the German “Prince of Mathematicians,” whose name is also on a unit for magnetic fields", ["prince of mathematicians", "german"], "Carl Friedrich Gauss"),
        C("surfaces", "giveaway", "Used with imaginary closed surfaces, like spheres, cylinders, or pillboxes, chosen to match a problem’s symmetry", ["imaginary", "symmetry", "gaussian surface"]),
        C("sphere-center", "middle", "Outside a uniformly charged sphere, the field is the same as if all the charge sat at the center", ["uniformly charged sphere", "center"]),
        C("coulomb", "middle", "Applied to a sphere around a point charge, it gives back Coulomb’s law", ["coulomb’s law", "point charge"], "Coulomb’s law"),
        C("conductor-surface", "middle", "Shows that extra charge on a conductor sits on its outer surface, with no field inside the metal", ["conductor", "outer surface"]),
        C("no-net-charge", "middle", "If a closed surface holds no net charge, the total flux through it is zero: as many field lines leave as enter", ["no net charge", "field lines"]),
        C("magnetism-version", "middle", "Its magnetic version says the total magnetic flux out of any closed surface is zero, since no lone magnetic pole has been found", ["magnetic flux", "lone magnetic pole"], "Magnetic monopoles"),
        C("flux-def", "middle", "Electric flux = field × the area it passes straight through, measured in newton square meters per coulomb", ["newton square meters per coulomb", "area"]),
        C("sheet-wire", "middle", "A huge flat sheet of charge makes a field that is the same at every distance; a long charged wire’s field falls as 1/r", ["flat sheet", "wire"], "Electric field"),
        C("lagrange", "power", "Joseph-Louis Lagrange stated a version in 1773 while studying the pull of ellipsoids; its namesake reached it in 1835", ["lagrange", "1773", "ellipsoids"]),
        C("ice-pail", "power", "Faraday’s 1843 ice-pail experiment: a charged ball lowered into a metal pail puts an equal charge on the pail’s outside", ["ice-pail", "1843", "faraday"], "Michael Faraday"),
        C("heaviside", "power", "Oliver Heaviside’s 1880s vector rewrite of Maxwell’s theory into four equations included it", ["heaviside", "vector"]),
        C("moving-charges", "power", "Unlike Coulomb’s law, it stays true even when charges move", ["charges move", "coulomb’s law"]),
        C("cube", "power", "A point charge at the center of a cube sends one-sixth of its flux through each face", ["cube", "one-sixth"]),
        C("any-size", "power", "Flux through a sphere around a point charge is the same at any radius: the field falls as 1/r² while the area grows as r²", ["any radius", "1/r²"]),
        C("inside-ball", "power", "Inside a uniformly charged ball, the field grows steadily from zero at the center to its largest value at the surface", ["uniformly charged ball", "zero at the center"]),
        C("hollow-shell", "power", "Inside a hollow charged metal shell, the electric field is zero", ["hollow", "shell"]),
        C("gravity", "power", "A gravity version links gravitational flux to the mass inside, matching Newton’s shell theorem", ["gravity version", "shell theorem"], "Gravity"),
        C("pillbox", "power", "A pillbox straddling a conductor’s surface shows the field just outside equals the surface charge density divided by ε₀", ["pillbox", "surface charge density"]),
        C("telegraph", "power", "Its namesake built an early electric telegraph with Wilhelm Weber in 1833", ["telegraph", "weber", "1833"]),
        C("ostrogradsky", "power", "The divergence theorem, sometimes named for Mikhail Ostrogradsky, links its whole-surface form to its point-by-point form", ["ostrogradsky", "divergence theorem"])
    ],
    "trap": {
        "title": "Which Maxwell equation?",
        "body": "This law is one of the four Maxwell’s equations, and tossups on each one sound alike. Gauss’s law links the electric flux through a closed surface to the charge inside; Gauss’s law for magnetism says the magnetic flux through a closed surface is always zero; Faraday’s law says a changing magnetic field makes a voltage; and Ampère’s law links the magnetic field around a loop to the current through it. Coulomb’s law gives the same answers for still charges, so it is a tempting wrong buzz.",
        "fix": "Closed surfaces, electric flux, enclosed charge, epsilon-naught, and symmetric shapes like spheres and pillboxes mean Gauss’s law. Magnetic flux that is always zero means Gauss’s law for magnetism; induction means Faraday’s law; loops around currents mean Ampère’s law. Saying just “Gauss” or “Maxwell’s equations” earns a prompt.",
        "line": "Real answer line: " + LINE
    },
    "tests": {
        "right": [
            "Gauss's law",
            "Gauss law",
            "Gausss law",
            "Gauss’s Law",
            "Gauss's flux theorem",
            "Guass's law"
        ],
        "prompt": [
            "Gauss",
            "Maxwell's equations",
            "Carl Friedrich Gauss"
        ],
        "wrong": [
            "Coulomb's law",
            "Faraday's law",
            "Ampère's law",
            "Gauss's law for magnetism",
            "Electric flux",
            "Ohm's law",
            "Divergence theorem",
            "Maxwell's demon"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
