import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "carbon",
    "name": "Carbon",
    "mono": "C",
    "category": "Chemistry",
    "qbCategory": "Science · Chemistry",
    "kicker": "Element 6 · The backbone of life and of organic chemistry",
    "dates": "Known since prehistoric times",
    "briefing": "Carbon is element number six, and it is the backbone of every living thing: its atoms link into chains and rings to build sugars, fats, proteins, and DNA. The same element makes soft, gray graphite in pencils and diamond, the hardest natural substance, depending only on how its atoms are arranged. Scientists even use a radioactive form of carbon to find the ages of ancient wood and bones.",
    "answerHtml": "<b><u>Carbon</u></b> (accept <u>C</u>)",
    "accept": [
        "carbon",
        "c"
    ],
    "prompt": [],
    "reject": [
        "carbon dioxide",
        "carbon monoxide",
        "carbonate",
        "carbonates",
        "carbonic acid",
        "carbon dating",
        "carbon 14 dating",
        "radiocarbon dating",
        "radiocarbon",
        "carbon cycle",
        "carbon fiber",
        "carbon fibre",
        "carbon footprint",
        "carbon tetrachloride",
        "carbon nanotube",
        "carbon nanotubes",
        "carbon black",
        "carbide",
        "carbohydrate",
        "carbohydrates",
        "hydrocarbon",
        "hydrocarbons",
        "diamond",
        "diamonds",
        "graphite",
        "graphene",
        "fullerene",
        "buckminsterfullerene",
        "buckyball",
        "charcoal",
        "coal",
        "soot",
        "coke",
        "steel",
        "silicon",
        "nitrogen",
        "oxygen",
        "hydrogen",
        "boron",
        "organic chemistry"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Carbon",
    "qb": {
        "q": "carbon",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "Fred Hoyle predicted that this element’s nucleus has a special excited state, now named for him, which lets stars build it by fusing three helium nuclei in the triple-alpha process. In stars more massive than the Sun, this element acts as a catalyst in a fusion cycle that also involves nitrogen and oxygen.",
            "r": "Atoms of this element usually form four bonds and can link into long chains. For 10 points, name this element with atomic number 6, the basis of organic chemistry."
        },
        {
            "p": "In 1858, August Kekulé [“KAY-kuh-lay”] and Archibald Scott Couper independently proposed that atoms of this element form four bonds and can link to one another in chains. Kekulé later said that a dream of a snake biting its own tail inspired his ring-shaped structure for benzene.",
            "r": "Benzene is made of six atoms of this element and six of hydrogen. For 10 points, name this element, whose compounds are the subject of organic chemistry."
        },
        {
            "p": "Willard Libby won the 1960 Nobel Prize in Chemistry for a dating method based on this element’s radioactive isotope with mass number 14, which has a half-life of about 5,730 years. That isotope forms high in the atmosphere when neutrons from cosmic rays strike nitrogen atoms.",
            "r": "For 10 points, name this element found in all living things, whose pure forms include diamond and graphite."
        },
        {
            "p": "Harold Kroto, Robert Curl, and Richard Smalley shared the 1996 Nobel Prize in Chemistry for discovering a hollow, soccer-ball-shaped molecule made of 60 atoms of this element. That molecule, nicknamed the “buckyball,” was named for the architect Buckminster Fuller, whose geodesic domes it resembles.",
            "r": "Like diamond and graphite, that molecule is a pure form of this element. For 10 points, name this element with atomic number 6."
        },
        {
            "p": "Andre Geim and Konstantin Novoselov used sticky tape to peel off graphene, a sheet of this element just one atom thick, and won the 2010 Nobel Prize in Physics for their work on it. Rolling such sheets into tiny hollow tubes makes nanotubes, which are far stronger than steel for their weight.",
            "r": "Pencil “lead” is really another form of this element, graphite. For 10 points, name this element, which also forms diamond."
        },
        {
            "p": "Smithson Tennant burned a diamond and showed that it produced the same gas as an equal weight of charcoal, proving the two were made of the same element. In diamond, each atom of this element is bonded to four neighbors in a rigid three-dimensional network.",
            "r": "Graphite’s atoms form flat sheets that slide past one another. For 10 points, name this element with atomic number 6."
        },
        {
            "p": "About 1.1 percent of this element’s atoms belong to a stable isotope with mass number 13, which chemists study using nuclear magnetic resonance. The atomic mass unit is defined as one-twelfth the mass of an atom of this element’s most common isotope.",
            "r": "For 10 points, name this element, whose radioactive isotope with mass number 14 is used to date ancient wood and bones."
        },
        {
            "p": "An atom of this element bonded to four different groups is called a chiral center, which can make a molecule “handed” like a pair of gloves. In methane, an atom of this element sits at the center of a tetrahedron, with bond angles of about 109.5 degrees.",
            "r": "For 10 points, name this element, which forms four bonds in nearly all of its compounds and is the basis of organic chemistry."
        },
        {
            "p": "Coke, a fuel made mostly of this element, is burned in blast furnaces to remove oxygen from iron ore, and adding a little of this element to iron makes steel. This element’s monoxide is a colorless, odorless, poisonous gas that binds to hemoglobin more tightly than oxygen does.",
            "r": "For 10 points, name this element, whose dioxide is the gas that plants take in for photosynthesis."
        },
        {
            "p": "This element’s ground-state electron configuration is 1s² 2s² 2p², giving it four valence electrons. Its ability to bond to itself in long chains and rings, called catenation, is unmatched by any other element.",
            "r": "This element sits at the top of group 14, directly above silicon. For 10 points, name this element with atomic number 6, found in diamond and graphite."
        },
        {
            "p": "In 1828, Friedrich Wöhler [“VUR-ler”] made urea from nonliving starting materials, showing that a compound of this element produced by living things could also be made in a lab. That result weakened the old idea of vitalism. Urea contains one atom of this element, along with oxygen, nitrogen, and hydrogen.",
            "r": "Organic chemistry is the study of this element’s compounds. For 10 points, name this element found in every living thing."
        },
        {
            "p": "Volcanoes, the weathering of rocks, and the burning of fossil fuels all move this element through a global cycle among the air, the oceans, rocks, and living things. Limestone, built largely from the shells and skeletons of sea creatures, stores a huge amount of this element.",
            "r": "Plants take in this element from the air as a dioxide during photosynthesis. For 10 points, name this element with atomic number 6."
        },
        {
            "p": "Atoms of this element are sp³ hybridized in its hardest form but sp² hybridized in the form used in pencils. That hardest form scores a 10, the top value, on the Mohs scale and conducts heat better than any other natural material.",
            "r": "Its atoms also form the backbone of every organic molecule. For 10 points, name this element, whose pure forms include diamond and graphite."
        },
        {
            "p": "By mass, this element is the fourth most common element in the universe and the second most common in the human body, after oxygen. Science fiction writers sometimes imagine life based on silicon instead of this element, since both can form four bonds.",
            "r": "Its atoms make up the backbones of sugars, fats, proteins, and DNA. For 10 points, name this element, the basis of all known life."
        },
        {
            "p": "Gas masks and water filters often contain a porous, “activated” form of this element, whose huge surface area traps harmful molecules. Charcoal and soot are mostly this element, whose name comes from the Latin word for charcoal.",
            "r": "For 10 points, name this element with atomic number 6, whose pure forms include diamond and graphite."
        }
    ],
    "clues": [
        {
            "id": "element-6",
            "tier": "giveaway",
            "t": "Element number 6: six protons and four valence electrons",
            "k": ["element number 6", "six protons", "four valence"],
            "n": 0
        },
        {
            "id": "organic",
            "tier": "giveaway",
            "t": "Organic chemistry is the study of its compounds",
            "k": ["organic chemistry", "compounds"],
            "n": 0
        },
        {
            "id": "life",
            "tier": "giveaway",
            "t": "The backbone of all known life: found in sugars, fats, proteins, and DNA",
            "k": ["backbone", "all known life", "proteins"],
            "n": 0
        },
        {
            "id": "allotropes",
            "tier": "giveaway",
            "t": "Its pure forms (allotropes) include diamond, graphite, and buckyballs",
            "k": ["allotropes", "diamond", "graphite"],
            "n": 0,
            "rabbit": "Diamond"
        },
        {
            "id": "isotope-14",
            "tier": "giveaway",
            "t": "Its radioactive isotope with mass number 14 is used to date ancient wood and bones",
            "k": ["mass number 14", "radioactive", "ancient wood"],
            "n": 0
        },
        {
            "id": "four-bonds",
            "tier": "middle",
            "t": "Forms four covalent bonds and links to itself in long chains and rings, called catenation",
            "k": ["catenation", "four covalent bonds", "chains"],
            "n": 0
        },
        {
            "id": "diamond",
            "tier": "middle",
            "t": "Diamond: each atom (sp³ hybridized) bonds to four others in a rigid 3-D network; 10 on the Mohs scale, the hardest natural substance",
            "k": ["mohs", "hardest", "network"],
            "n": 0
        },
        {
            "id": "graphite",
            "tier": "middle",
            "t": "Graphite: flat sheets of sp²-hybridized atoms in hexagons that slide past each other; it conducts electricity and is used in pencils",
            "k": ["graphite", "pencils", "sheets"],
            "n": 0
        },
        {
            "id": "dioxide",
            "tier": "middle",
            "t": "Its dioxide is breathed out by animals, used by plants in photosynthesis, and traps heat as a greenhouse gas",
            "k": ["dioxide", "photosynthesis", "greenhouse"],
            "n": 0,
            "rabbit": "Carbon dioxide"
        },
        {
            "id": "monoxide",
            "tier": "middle",
            "t": "Its monoxide is a colorless, odorless, poisonous gas that grabs hemoglobin more tightly than oxygen does",
            "k": ["monoxide", "poisonous", "hemoglobin"],
            "n": 0
        },
        {
            "id": "steel",
            "tier": "middle",
            "t": "Iron plus a little of it makes steel; coke, a fuel made from coal, is burned in blast furnaces to free iron from its ore",
            "k": ["steel", "coke", "blast furnaces"],
            "n": 0,
            "rabbit": "Iron"
        },
        {
            "id": "group-14",
            "tier": "middle",
            "t": "Sits at the top of group 14, directly above silicon; its electron configuration is 1s² 2s² 2p²",
            "k": ["group 14", "silicon"],
            "n": 0
        },
        {
            "id": "cycle",
            "tier": "middle",
            "t": "Moves among the air, oceans, rocks, and living things in a global cycle; burning fossil fuels releases it into the air",
            "k": ["global cycle", "fossil fuels"],
            "n": 0
        },
        {
            "id": "libby",
            "tier": "power",
            "t": "Willard Libby invented dating with its isotope of mass 14 (half-life about 5,730 years) and won the 1960 Nobel Prize in Chemistry",
            "k": ["libby", "5,730", "half-life"],
            "n": 0
        },
        {
            "id": "abundance",
            "tier": "power",
            "t": "By mass, the fourth most common element in the universe and the second most common in the human body (after oxygen)",
            "k": ["human body", "fourth most common", "universe"],
            "n": 0
        },
        {
            "id": "triple-alpha",
            "tier": "power",
            "t": "Stars make it by fusing three helium nuclei in the triple-alpha process; Fred Hoyle predicted the excited “Hoyle state” this needs",
            "k": ["triple-alpha", "hoyle", "helium nuclei"],
            "n": 0,
            "rabbit": "Nuclear fusion"
        },
        {
            "id": "cno-cycle",
            "tier": "power",
            "t": "In stars more massive than the Sun, it is a catalyst in a fusion cycle with nitrogen and oxygen",
            "k": ["catalyst", "fusion cycle", "nitrogen and oxygen"],
            "n": 0
        },
        {
            "id": "cosmic-rays",
            "tier": "power",
            "t": "Its isotope of mass 14 forms high in the atmosphere when neutrons from cosmic rays hit nitrogen",
            "k": ["cosmic rays", "neutrons", "atmosphere"],
            "n": 0
        },
        {
            "id": "amu",
            "tier": "power",
            "t": "The atomic mass unit is one-twelfth the mass of an atom of its most common isotope, which has mass number 12",
            "k": ["atomic mass unit", "one-twelfth"],
            "n": 0
        },
        {
            "id": "nmr",
            "tier": "power",
            "t": "About 1.1 percent of its atoms are a stable isotope of mass 13, studied with nuclear magnetic resonance (NMR)",
            "k": ["nuclear magnetic resonance", "nmr", "mass 13"],
            "n": 0
        },
        {
            "id": "kekule-couper",
            "tier": "power",
            "t": "August Kekulé and Archibald Scott Couper (1858) proposed that its atoms form four bonds and link together; Kekulé’s benzene ring followed a snake dream",
            "k": ["kekulé", "couper", "1858", "benzene"],
            "n": 0,
            "rabbit": "Benzene"
        },
        {
            "id": "buckyball",
            "tier": "power",
            "t": "Kroto, Curl, and Smalley found buckminsterfullerene, a 60-atom soccer-ball molecule, and won the 1996 Nobel Prize in Chemistry",
            "k": ["buckminsterfullerene", "kroto", "smalley", "1996"],
            "n": 0
        },
        {
            "id": "graphene",
            "tier": "power",
            "t": "Andre Geim and Konstantin Novoselov peeled off one-atom-thick graphene with sticky tape (2010 Nobel Prize in Physics); rolled-up sheets form nanotubes",
            "k": ["graphene", "geim", "novoselov", "nanotubes"],
            "n": 0
        },
        {
            "id": "tennant",
            "tier": "power",
            "t": "Smithson Tennant burned a diamond to prove it is made of the same element as charcoal",
            "k": ["tennant", "burned a diamond", "charcoal"],
            "n": 0
        },
        {
            "id": "wohler",
            "tier": "power",
            "t": "Friedrich Wöhler’s 1828 synthesis of urea weakened vitalism, the idea that only living things could make organic compounds",
            "k": ["wöhler", "urea", "vitalism", "1828"],
            "n": 0
        },
        {
            "id": "chiral",
            "tier": "power",
            "t": "An atom of it bonded to four different groups is a chiral center; in methane its four bonds point to the corners of a tetrahedron (109.5°)",
            "k": ["chiral center", "tetrahedron", "109.5"],
            "n": 0
        },
        {
            "id": "activated",
            "tier": "power",
            "t": "A porous “activated” form traps harmful molecules in gas masks and water filters; its name comes from the Latin word for charcoal",
            "k": ["activated", "gas masks", "latin"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Element, not diamond",
        "body": "Tossups on this element are full of clues about its famous forms and compounds, like diamond, graphite, buckyballs, and the gases carbon dioxide and carbon monoxide, which tempt players to blurt one of those names. Silicon is the other trap: it sits right below this element in group 14, also forms four bonds, and stars in science-fiction stories about alien life.",
        "fix": "If the question asks for “this element,” name the element itself, even when the clue is about diamond or a gas it forms. Atomic number 6, organic chemistry, dating ancient remains, and Willard Libby all point here; computer chips, sand, and glass point to silicon.",
        "line": "Real answer line: <b><u>Carbon</u></b> (accept <u>C</u>)"
    },
    "tests": {
        "right": [
            "Carbon",
            "C",
            "Carbn",
            "elemental carbon",
            "carbon atoms"
        ],
        "prompt": [],
        "wrong": [
            "Carbon dioxide",
            "Diamond",
            "Graphite",
            "Silicon",
            "Carbon dating",
            "Carbonate",
            "Nitrogen"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
