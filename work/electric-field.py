import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "electric-field",
    "name": "Electric field",
    "mono": "EF",
    "category": "Physics",
    "qbCategory": "Science · Physics",
    "kicker": "Force per unit charge around every charge · Mapped with lines of force",
    "dates": "Lines of force pictured by Michael Faraday, 1800s",
    "briefing": "An electric field is the invisible zone of push and pull that surrounds every electric charge. Michael Faraday pictured it as lines that point away from positive charges and toward negative ones, and the closer together the lines, the stronger the field. A balloon rubbed on your hair tugs on it through its electric field, and sharks can sense the faint electric fields made by the muscles of hidden prey.",
    "answerHtml": "<b><u>electric field</u></b> (accept <u>E-field</u> or <u>electrostatic field</u>; prompt on <u>field</u> or <u>electromagnetic field</u>; do not accept “magnetic field”)",
    "accept": [
        "electric field",
        "electric fields",
        "e field",
        "e fields",
        "electrostatic field",
        "electrostatic fields",
        "electrical field",
        "electrical fields",
        "electric field strength",
        "electric field intensity"
    ],
    "prompt": [
        "field",
        "fields",
        "electromagnetic field",
        "electromagnetic fields",
        "em field"
    ],
    "reject": [
        "magnetic field",
        "magnetic fields",
        "b field",
        "earths magnetic field",
        "electric charge",
        "electric current",
        "electric potential",
        "electric potential energy",
        "electric flux",
        "electric force",
        "electric dipole",
        "voltage",
        "potential difference",
        "coulombs law",
        "gausss law",
        "gauss law",
        "gravitational field",
        "electromotive force",
        "emf",
        "capacitance"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Electric_field",
    "qb": {
        "q": "electric field",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "Johannes Stark won a Nobel Prize for discovering that this quantity splits the spectral lines of atoms. Inside a closed metal box called a Faraday cage, this quantity is zero, which shields anything inside from outside charges.",
            "r": "For 10 points, name this vector quantity, measured in newtons per coulomb, that equals the force on a charge divided by the charge."
        },
        {
            "p": "Gauss’s law says that the flux of this quantity through any closed surface equals the charge inside divided by the permittivity of free space. Lines showing this quantity begin on positive charges and end on negative charges.",
            "r": "For 10 points, name this quantity, the force per unit charge at each point around a charged object."
        },
        {
            "p": "Robert Millikan measured the charge of a single electron by adjusting this quantity between two metal plates until tiny charged oil drops hung motionless in midair. Between two oppositely charged parallel plates, this quantity is nearly the same everywhere.",
            "r": "For 10 points, name this quantity, measured in volts per meter or newtons per coulomb."
        },
        {
            "p": "This quantity equals the negative gradient of the voltage, so it points “downhill” from high voltage toward low voltage. Lines showing this quantity always cross equipotential surfaces at right angles, and they never cross each other.",
            "r": "For 10 points, name this quantity whose lines point away from positive charges and toward negative ones."
        },
        {
            "p": "When this quantity reaches about three million volts per meter, dry air breaks down and conducts, letting a spark jump across a gap. Michael Faraday pictured this quantity using “lines of force” that spread out from every charge.",
            "r": "For 10 points, name this quantity, the force per unit charge, that surrounds every charged object."
        },
        {
            "p": "In gel electrophoresis [“ih-lek-troh-fuh-REE-sis”], scientists use this quantity to pull DNA fragments through a gel, sorting them by size. Any charged particle placed in this quantity feels a force equal to its charge times the strength of this quantity.",
            "r": "For 10 points, name this quantity found by dividing the force on a small test charge by the size of that charge."
        },
        {
            "p": "Sharks use jelly-filled pores called ampullae of Lorenzini to sense faint versions of this quantity given off by the muscles of hidden prey. Platypuses can also sense this quantity with their bills while hunting underwater with their eyes closed.",
            "r": "For 10 points, name this quantity, which points away from positive charges and toward negative ones."
        },
        {
            "p": "The strength of this quantity around a dipole falls off with the cube of the distance, faster than around a single point charge. Around a point charge, Coulomb’s law says this quantity falls off with the square of the distance.",
            "r": "For 10 points, name this vector quantity, which can be drawn as lines of force around any charge."
        },
        {
            "p": "According to Faraday’s law of induction, a changing magnetic field creates a curling version of this quantity. Light is a wave made of this quantity and a magnetic partner that vibrate at right angles to each other.",
            "r": "For 10 points, name this quantity whose SI units are newtons per coulomb, the force per unit charge."
        },
        {
            "p": "The metal dome of a Van de Graaff generator builds up enough charge to create a strong version of this quantity, which can make a person’s hair stand on end. Charge on a conductor crowds onto sharp points, making this quantity strongest there.",
            "r": "For 10 points, name this quantity that tells how a charge would be pushed or pulled at each point in space."
        },
        {
            "p": "The energy stored per cubic meter in a region with this quantity equals one-half the permittivity of free space times this quantity squared. Dielectric materials placed in this quantity become polarized, which reduces this quantity inside them.",
            "r": "Capacitors store energy in this quantity. For 10 points, name this quantity measured in volts per meter."
        },
        {
            "p": "In 1897, J. J. Thomson bent cathode rays using this quantity and a magnetic one to find the charge-to-mass ratio of the electron. Oscilloscope tubes once steered their electron beams with plates that created this quantity.",
            "r": "For 10 points, name this quantity that points away from positive charges and toward negative charges."
        },
        {
            "p": "Around a very large flat sheet of charge, this quantity has the same strength at every distance, while around a long charged wire, it weakens in proportion to one over the distance. A small positive test charge is used to map this quantity.",
            "r": "For 10 points, name this quantity, the force per unit charge, which Michael Faraday drew as lines of force."
        },
        {
            "p": "Linear particle accelerators, like the two-mile-long machine at SLAC, use oscillating versions of this quantity to speed up electrons. In a uniform version of this quantity, a charged particle speeds up steadily, just as a falling ball does in gravity.",
            "r": "For 10 points, name this quantity, measured in newtons per coulomb, whose lines Michael Faraday drew around charges."
        },
        {
            "p": "St. Elmo’s fire glows on ship masts and airplane wings during storms when this quantity becomes very strong around pointed objects. This quantity is strongest wherever the lines that represent it are packed closest together.",
            "r": "Its SI unit is the newton per coulomb. For 10 points, name this quantity, the force per unit charge, which surrounds every charged object."
        }
    ],
    "clues": [
        {
            "id": "definition",
            "tier": "giveaway",
            "t": "The force a charge would feel at each point in space, divided by the size of that charge (force per unit charge)",
            "k": ["force per unit charge", "each point"],
            "n": 0
        },
        {
            "id": "units",
            "tier": "giveaway",
            "t": "Measured in newtons per coulomb, which is the same as volts per meter",
            "k": ["newtons per coulomb", "volts per meter"],
            "n": 0
        },
        {
            "id": "direction",
            "tier": "giveaway",
            "t": "Points away from positive charges and toward negative charges",
            "k": ["away from positive", "toward negative"],
            "n": 0
        },
        {
            "id": "faraday-lines",
            "tier": "giveaway",
            "t": "Drawn as lines of force, an idea from Michael Faraday; closer lines mean a stronger push",
            "k": ["lines of force", "michael faraday"],
            "n": 0,
            "rabbit": "Michael Faraday"
        },
        {
            "id": "made-by-charges",
            "tier": "giveaway",
            "t": "Made by charges, even ones sitting still; its magnetic partner comes from moving charges and magnets",
            "k": ["sitting still", "moving charges"],
            "n": 0,
            "rabbit": "Magnetic fields"
        },
        {
            "id": "coulomb",
            "tier": "middle",
            "t": "Around a point charge it follows Coulomb’s law, falling off with the square of the distance",
            "k": ["coulomb’s law", "square of the distance"],
            "n": 0,
            "rabbit": "Coulomb’s law"
        },
        {
            "id": "force-qe",
            "tier": "middle",
            "t": "A charge placed in it feels a force equal to the charge times its strength (F = qE)",
            "k": ["f = qe", "charge times"],
            "n": 0
        },
        {
            "id": "faraday-cage",
            "tier": "middle",
            "t": "Zero inside a closed metal shell (a Faraday cage) or inside any conductor whose charges are at rest",
            "k": ["faraday cage", "conductor"],
            "n": 0
        },
        {
            "id": "parallel-plates",
            "tier": "middle",
            "t": "Nearly uniform between two oppositely charged parallel plates, as in a capacitor",
            "k": ["parallel plates", "capacitor"],
            "n": 0,
            "rabbit": "Capacitors"
        },
        {
            "id": "gradient",
            "tier": "middle",
            "t": "Points “downhill” from high voltage to low; it equals the negative gradient of the voltage",
            "k": ["gradient", "downhill"],
            "n": 0,
            "rabbit": "Voltage"
        },
        {
            "id": "light",
            "tier": "middle",
            "t": "Light is a wave of it and its magnetic partner, vibrating at right angles to each other",
            "k": ["light", "right angles"],
            "n": 0
        },
        {
            "id": "gauss",
            "tier": "middle",
            "t": "Gauss’s law: its flux through a closed surface equals the charge inside divided by the permittivity of free space",
            "k": ["gauss’s law", "flux", "closed surface"],
            "n": 0,
            "rabbit": "Gauss’s law"
        },
        {
            "id": "sharks",
            "tier": "middle",
            "t": "Sharks (using ampullae of Lorenzini) and platypuses can sense faint ones made by hidden prey",
            "k": ["sharks", "platypuses", "lorenzini"],
            "n": 0
        },
        {
            "id": "stark",
            "tier": "power",
            "t": "The Stark effect: it splits atoms’ spectral lines (Johannes Stark, Nobel Prize 1919)",
            "k": ["stark effect", "spectral lines"],
            "n": 0
        },
        {
            "id": "millikan",
            "tier": "power",
            "t": "Robert Millikan balanced charged oil drops in it to measure the electron’s charge",
            "k": ["millikan", "oil drops"],
            "n": 0,
            "rabbit": "Millikan oil drop experiment"
        },
        {
            "id": "breakdown",
            "tier": "power",
            "t": "Dry air breaks down and sparks when it reaches about 3 million volts per meter",
            "k": ["3 million", "sparks"],
            "n": 0
        },
        {
            "id": "dipole",
            "tier": "power",
            "t": "Around a dipole it falls off with the cube of the distance",
            "k": ["dipole", "cube"],
            "n": 0,
            "rabbit": "Dipoles"
        },
        {
            "id": "electrophoresis",
            "tier": "power",
            "t": "Gel electrophoresis uses it to pull DNA fragments through a gel and sort them by size",
            "k": ["electrophoresis", "dna fragments"],
            "n": 0
        },
        {
            "id": "thomson",
            "tier": "power",
            "t": "J. J. Thomson bent cathode rays with it (and a magnetic one) to find the electron’s charge-to-mass ratio in 1897",
            "k": ["cathode rays", "charge-to-mass", "1897"],
            "n": 0,
            "rabbit": "Electrons"
        },
        {
            "id": "energy-density",
            "tier": "power",
            "t": "Energy stored per cubic meter = ½ × the permittivity of free space × its strength squared",
            "k": ["energy stored", "squared"],
            "n": 0
        },
        {
            "id": "sheet-wire",
            "tier": "power",
            "t": "Same strength at any distance from a huge flat sheet of charge; falls as 1/r around a long charged wire",
            "k": ["flat sheet", "charged wire"],
            "n": 0
        },
        {
            "id": "equipotentials",
            "tier": "power",
            "t": "Its lines cross equipotential surfaces at right angles and never cross each other",
            "k": ["equipotential", "never cross"],
            "n": 0
        },
        {
            "id": "induction",
            "tier": "power",
            "t": "Faraday’s law of induction: a changing magnetic field creates a curling version of it",
            "k": ["induction", "curling"],
            "n": 0
        },
        {
            "id": "van-de-graaff",
            "tier": "power",
            "t": "A Van de Graaff generator makes a strong one that can make hair stand on end; it is strongest near sharp points",
            "k": ["van de graaff", "hair", "sharp points"],
            "n": 0
        },
        {
            "id": "dielectric",
            "tier": "power",
            "t": "Dielectric materials become polarized in it, which reduces it inside them",
            "k": ["dielectric", "polarized"],
            "n": 0
        },
        {
            "id": "linac",
            "tier": "power",
            "t": "Linear accelerators like SLAC’s two-mile machine use oscillating ones to speed up electrons",
            "k": ["linear accelerators", "slac"],
            "n": 0
        },
        {
            "id": "st-elmo",
            "tier": "power",
            "t": "St. Elmo’s fire glows on ship masts and airplane wings when it gets very strong around pointed objects",
            "k": ["elmo", "masts", "pointed objects"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Electric or magnetic?",
        "body": "Electric and magnetic fields are partners (light is a wave of both), and quiz bowl has separate answer lines for each. Charges make an electric field even when they sit still, and it pushes on any charge, moving or not; a magnetic field comes from moving charges or magnets, and it pushes only on charges that are moving. Some tossups instead want related answers like electric potential (voltage) or electric flux.",
        "fix": "Newtons per coulomb, volts per meter, Coulomb’s law, Gauss’s law, the Stark effect, or Millikan’s oil drops means electric field. Teslas, compass needles, the right-hand rule, the Hall effect, or the Zeeman effect means magnetic field.",
        "line": "Real answer line: <b><u>electric field</u></b> (accept <u>E-field</u>; prompt on <u>field</u>; do not accept “magnetic field”)"
    },
    "tests": {
        "right": [
            "Electric field",
            "electric fields",
            "E-field",
            "Electrostatic field",
            "Electirc field"
        ],
        "prompt": [
            "Field",
            "Electromagnetic field"
        ],
        "wrong": [
            "Magnetic field",
            "Electric current",
            "Voltage",
            "Electric potential",
            "Gravitational field"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
