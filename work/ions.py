import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "ions",
    "name": "Ions",
    "mono": "ION",
    "category": "Chemistry",
    "qbCategory": "Science · Chemistry",
    "kicker": "Atoms and molecules with an electric charge · The particles in salt and nerves",
    "dates": "Named by Michael Faraday, 1834",
    "briefing": "Michael Faraday named ions in 1834, from the Greek word for “going”: they are atoms or molecules that have gained or lost electrons, which gives them an electric charge. Atoms that lose electrons become positive cations, like the sodium in table salt, and atoms that gain electrons become negative anions, like chloride. Opposite charges attract, so ions lock together into crystals, carry electric current through salty water, and send signals along your nerves.",
    "answerHtml": "<b><u>Ions</u></b> (accept <u>ion</u>; prompt on <u>charged particles</u>; do not accept “cations” or “anions” alone)",
    "accept": [
        "ions",
        "ion",
        "cations and anions",
        "anions and cations"
    ],
    "prompt": [
        "charged particles",
        "charged particle",
        "charged atoms",
        "charged atom"
    ],
    "reject": [
        "cation",
        "cations",
        "anion",
        "anions",
        "electron",
        "electrons",
        "proton",
        "protons",
        "neutron",
        "neutrons",
        "isotope",
        "isotopes",
        "atom",
        "atoms",
        "molecule",
        "molecules",
        "electrolyte",
        "electrolytes",
        "electrode",
        "electrodes",
        "ionic bond",
        "ionic bonds",
        "ionic compound",
        "ionic compounds",
        "salt",
        "salts",
        "free radicals",
        "radicals",
        "zwitterion",
        "zwitterions",
        "isomers",
        "ionization",
        "ionosphere",
        "plasma"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Ion",
    "qb": {
        "q": "ions",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "Svante Arrhenius won the 1903 Nobel Prize in Chemistry for proposing that salts break apart into these particles when they dissolve, even with no electric current flowing. Peter Debye [“duh-BYE”] and Erich Hückel later described how each of these particles in a solution is surrounded by an “atmosphere” of oppositely charged ones.",
            "r": "During electrolysis, the positive ones travel to the cathode. For 10 points, name these charged atoms or molecules."
        },
        {
            "p": "In 1834, William Whewell [“HYOO-ul”] helped a scientist choose the name for these particles, along with the words “anode” and “cathode.” That scientist, Michael Faraday, took their name from the Greek word for “going,” because they travel toward the electrodes during electrolysis.",
            "r": "For 10 points, name these particles, which are called cations if positive and anions if negative."
        },
        {
            "p": "Sodium’s plus-one version of these particles, fluoride, and a neon atom are isoelectronic, since each has 10 electrons. The positive kind of these particles is smaller than the atom it came from, while the negative kind is larger.",
            "r": "Table salt is a crystal of sodium and chloride ones. For 10 points, name these atoms that carry a charge after gaining or losing electrons."
        },
        {
            "p": "In water, each of these particles is wrapped in a hydration shell: water molecules point their oxygen ends toward the positive ones and their hydrogen ends toward the negative ones. Simple negative ones get names ending in “-ide,” such as oxide and sulfide.",
            "r": "Salts conduct electricity when dissolved because these particles are free to move. For 10 points, name these charged particles, which include sodium and chloride."
        },
        {
            "p": "A mass spectrometer turns molecules into these particles and then sorts them by their mass-to-charge ratio. Examples of these particles made of several atoms bonded together, such as sulfate, nitrate, and ammonium, are called polyatomic.",
            "r": "Atoms become these particles by gaining or losing electrons. For 10 points, name these charged particles, called cations when positive."
        },
        {
            "p": "NASA’s Dawn spacecraft reached the asteroid Vesta and the dwarf planet Ceres using engines that shoot out a beam of these particles made from xenon. During electrolysis, the positive ones move toward the cathode and the negative ones move toward the anode.",
            "r": "Michael Faraday named these particles in 1834. For 10 points, name these atoms or molecules that have an electric charge."
        },
        {
            "p": "A salt bridge lets these particles flow between the two halves of a galvanic cell, keeping the charges balanced as the cell makes electricity. Salts conduct electricity when melted or dissolved, but not as solids, because these particles must be free to move.",
            "r": "For 10 points, name these particles, which form when atoms gain or lose electrons."
        },
        {
            "p": "Particles of this kind that appear unchanged on both sides of a reaction are called “spectators” and are left out of the net equation. Roman numerals show the charge of these particles in compound names such as iron(III) chloride.",
            "r": "For 10 points, name these charged particles, which are called anions when they are negative."
        },
        {
            "p": "Water softeners use resin beads to swap the calcium and magnesium versions of these particles for sodium ones. Examples of these particles made of several atoms, such as sulfate and nitrate, are called polyatomic.",
            "r": "For 10 points, name these charged atoms or molecules, such as the sodium and chloride in seawater."
        },
        {
            "p": "In a sodium chloride crystal, each of these particles is surrounded by six of the opposite charge, and lattice energy measures how tightly they hold together. Group 2 metals like magnesium form these particles with a charge of plus two.",
            "r": "For 10 points, name these charged particles, which are called cations if positive and anions if negative."
        },
        {
            "p": "The Debye–Hückel theory describes how each of these particles in a solution is surrounded by a cloud of oppositely charged ones. Pure water conducts electricity poorly, but dissolving a salt in it releases these particles and lets a current flow.",
            "r": "Electrolytes, like the ones in sports drinks, release these particles in water. For 10 points, name these charged particles."
        },
        {
            "p": "For every two potassium particles of this kind that the sodium-potassium pump brings into a cell, it pushes three sodium ones out, which helps nerve cells send signals. Protein channels in cell membranes let these particles flow in and out.",
            "r": "For 10 points, name these charged atoms, which come in positive and negative varieties."
        },
        {
            "p": "An atom grows larger when it becomes the negative kind of these particles and shrinks when it becomes the positive kind. Group 1 metals form these particles with a charge of plus one, while halogens form ones with a charge of minus one.",
            "r": "Metals form the positive kind by losing electrons. For 10 points, name these charged particles."
        },
        {
            "p": "Acids release positive hydrogen particles of this kind, which join water molecules to form hydronium, while bases release negative hydroxide ones. The pH scale measures the concentration of the hydrogen ones in a solution.",
            "r": "For 10 points, name these atoms or groups of atoms that carry an electric charge after gaining or losing electrons."
        },
        {
            "p": "The attraction between two of these particles follows Coulomb’s law, growing stronger as their charges increase and weaker as they move apart. Ammonium, which contains one nitrogen atom and four hydrogen atoms, is a positive polyatomic one.",
            "r": "For 10 points, name these charged particles, which form when atoms gain or lose electrons."
        }
    ],
    "clues": [
        {
            "id": "definition",
            "tier": "giveaway",
            "t": "Atoms or molecules with an electric charge, because they have gained or lost electrons",
            "k": ["electric charge", "gained or lost", "electrons"],
            "n": 0
        },
        {
            "id": "cations-anions",
            "tier": "giveaway",
            "t": "Positive ones are called cations; negative ones are called anions",
            "k": ["cations", "anions", "positive", "negative"],
            "n": 0
        },
        {
            "id": "table-salt",
            "tier": "giveaway",
            "t": "Table salt is a crystal of positive sodium ones and negative chloride ones",
            "k": ["table salt", "sodium", "chloride"],
            "n": 0,
            "rabbit": "Sodium"
        },
        {
            "id": "lose-gain",
            "tier": "giveaway",
            "t": "Metals lose electrons to form positive ones; nonmetals gain electrons to form negative ones",
            "k": ["metals", "nonmetals", "lose electrons"],
            "n": 0
        },
        {
            "id": "faraday",
            "tier": "middle",
            "t": "Michael Faraday named them in 1834, from the Greek word for “going”",
            "k": ["faraday", "1834", "going"],
            "n": 0,
            "rabbit": "Michael Faraday"
        },
        {
            "id": "electrodes",
            "tier": "middle",
            "t": "In electrolysis, positive ones move to the cathode and negative ones move to the anode",
            "k": ["cathode", "anode", "electrolysis"],
            "n": 0,
            "rabbit": "Electrolysis"
        },
        {
            "id": "polyatomic",
            "tier": "middle",
            "t": "Polyatomic ones contain several atoms bonded together, such as sulfate, nitrate, hydroxide, and ammonium",
            "k": ["polyatomic", "sulfate", "ammonium"],
            "n": 0
        },
        {
            "id": "ide-names",
            "tier": "middle",
            "t": "Simple negative ones get names ending in “-ide,” such as chloride, oxide, and sulfide",
            "k": ["-ide", "oxide", "sulfide"],
            "n": 0
        },
        {
            "id": "conduct",
            "tier": "middle",
            "t": "Salts conduct electricity when melted or dissolved, but not as solids, because these charged particles must be free to move",
            "k": ["melted or dissolved", "free to move", "conduct"],
            "n": 0
        },
        {
            "id": "electrolytes",
            "tier": "middle",
            "t": "Electrolytes, like those in sports drinks, release them in water, so the solution conducts electricity",
            "k": ["electrolytes", "sports drinks"],
            "n": 0,
            "rabbit": "Electrolytes"
        },
        {
            "id": "size",
            "tier": "middle",
            "t": "Positive ones are smaller than the atoms they came from; negative ones are larger",
            "k": ["smaller", "larger"],
            "n": 0
        },
        {
            "id": "charges",
            "tier": "middle",
            "t": "Group 1 metals form +1 ones, group 2 metals form +2 ones, and halogens form −1 ones",
            "k": ["group 1", "group 2", "halogens"],
            "n": 0,
            "rabbit": "Halogens"
        },
        {
            "id": "acids-bases",
            "tier": "middle",
            "t": "Acids release H+, which joins water to form hydronium (H3O+); bases release hydroxide (OH−); pH measures the hydrogen ones",
            "k": ["hydronium", "hydroxide", "acids"],
            "n": 0,
            "rabbit": "pH"
        },
        {
            "id": "nerves",
            "tier": "middle",
            "t": "The sodium-potassium pump moves 3 sodium ones out of a cell for every 2 potassium ones in, helping nerves send signals",
            "k": ["sodium-potassium pump", "nerves", "potassium"],
            "n": 0,
            "rabbit": "Potassium"
        },
        {
            "id": "roman-numerals",
            "tier": "middle",
            "t": "Roman numerals show their charge in names like iron(III) chloride, for metals that can form more than one",
            "k": ["roman numerals", "iron(iii)"],
            "n": 0
        },
        {
            "id": "arrhenius",
            "tier": "power",
            "t": "Svante Arrhenius won the 1903 Nobel Prize in Chemistry for proposing that salts split into them when they dissolve",
            "k": ["arrhenius", "1903", "split"],
            "n": 0
        },
        {
            "id": "whewell",
            "tier": "power",
            "t": "William Whewell helped Faraday pick their name, along with the words “anode” and “cathode”",
            "k": ["whewell", "anode", "cathode"],
            "n": 0
        },
        {
            "id": "isoelectronic",
            "tier": "power",
            "t": "Na+, F−, and a neon atom are isoelectronic: each has 10 electrons",
            "k": ["isoelectronic", "10 electrons", "neon"],
            "n": 0
        },
        {
            "id": "hydration",
            "tier": "power",
            "t": "In water, each is wrapped in a hydration shell, with water’s oxygen ends pointing toward the positive ones",
            "k": ["hydration shell", "oxygen ends"],
            "n": 0
        },
        {
            "id": "debye-huckel",
            "tier": "power",
            "t": "Debye–Hückel theory: each one in a solution is surrounded by an “atmosphere” of oppositely charged ones",
            "k": ["debye", "hückel", "atmosphere"],
            "n": 0
        },
        {
            "id": "mass-spec",
            "tier": "power",
            "t": "A mass spectrometer turns molecules into them and sorts them by mass-to-charge ratio",
            "k": ["mass spectrometer", "mass-to-charge"],
            "n": 0
        },
        {
            "id": "dawn",
            "tier": "power",
            "t": "NASA’s Dawn spacecraft reached Vesta and Ceres with engines that shoot out a beam of them made from xenon",
            "k": ["dawn", "xenon", "vesta", "ceres"],
            "n": 0
        },
        {
            "id": "salt-bridge",
            "tier": "power",
            "t": "A salt bridge lets them flow between the halves of a galvanic cell to keep the charges balanced",
            "k": ["salt bridge", "galvanic cell"],
            "n": 0
        },
        {
            "id": "spectators",
            "tier": "power",
            "t": "Ones that appear unchanged on both sides of a reaction are “spectators,” left out of the net equation",
            "k": ["spectators", "net equation"],
            "n": 0
        },
        {
            "id": "water-softeners",
            "tier": "power",
            "t": "Water softeners use resin beads to swap calcium and magnesium ones for sodium ones",
            "k": ["water softeners", "calcium", "magnesium", "resin"],
            "n": 0
        },
        {
            "id": "lattice",
            "tier": "power",
            "t": "In a sodium chloride crystal, each is surrounded by six of the opposite charge; lattice energy measures how tightly they hold together",
            "k": ["lattice energy", "six", "crystal"],
            "n": 0,
            "rabbit": "Lattice energy"
        },
        {
            "id": "coulomb",
            "tier": "power",
            "t": "The force between two of them follows Coulomb’s law: stronger with bigger charges, weaker as they move apart",
            "k": ["coulomb", "move apart"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Both kinds, not one",
        "body": "These particles come in two kinds, and clues often name only one: positive cations like sodium, or negative anions like chloride. A player who hears “positive” and blurts “cations” loses the tossup when the question wants the whole family. Electrons are the other trap: atoms gain or lose them to become these particles, but electrons are not the answer.",
        "fix": "If the question asks for “these particles” and mentions both charges, give the general name. Say “cations” or “anions” only when the question asks for one kind, and answer “electrons” only for “these negative subatomic particles.”",
        "line": "Real answer line: <b><u>Ions</u></b> (accept <u>ion</u>; prompt on <u>charged particles</u>; do not accept “cations” or “anions” alone)"
    },
    "tests": {
        "right": [
            "Ions",
            "ion",
            "ION",
            "positive and negative ions",
            "Cations and anions"
        ],
        "prompt": [
            "charged particles"
        ],
        "wrong": [
            "Cations",
            "Anions",
            "Electrons",
            "Isotopes",
            "Electrolytes",
            "Ionic bonds",
            "Iron"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
