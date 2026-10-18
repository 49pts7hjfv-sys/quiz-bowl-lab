import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "lanthanides",
    "name": "Lanthanides",
    "mono": "LN",
    "category": "Chemistry",
    "qbCategory": "Science · Chemistry",
    "kicker": "Elements 57 to 71 · The “rare earth” metals inside magnets and screens",
    "dates": "Cerium found 1803; promethium identified 1945",
    "briefing": "The lanthanides are the 15 metals from lanthanum to lutetium, usually shown in their own row below the main periodic table. Along with scandium and yttrium they are called the “rare earth” elements, though most are not actually rare. They are so alike that chemists struggled for over a century to separate them, and they power super-strong neodymium magnets, the colors in screens, and the motors of electric cars.",
    "answerHtml": "<b><u>Lanthanide</u></b>s (accept <u>lanthanoid</u>s; prompt on <u>rare earth</u> elements, <u>f-block</u> elements, or <u>inner transition</u> metals; do not accept “actinides”)",
    "accept": [
        "lanthanides",
        "lanthanide",
        "lanthanoids",
        "lanthanoid",
        "lanthanide series",
        "lanthanoid series",
        "lanthanide elements",
        "lanthanide metals"
    ],
    "prompt": [
        "rare earth elements",
        "rare earth element",
        "rare earths",
        "rare earth",
        "rare earth metals",
        "rare earth metal",
        "f block",
        "f block elements",
        "f block metals",
        "inner transition metals",
        "inner transition metal",
        "inner transition elements"
    ],
    "reject": [
        "actinides",
        "actinide",
        "actinoids",
        "actinoid",
        "lanthanum",
        "lutetium",
        "cerium",
        "neodymium",
        "europium",
        "gadolinium",
        "promethium",
        "samarium",
        "alkaline earth metals",
        "alkaline earth metal",
        "alkali metals",
        "alkali metal",
        "noble gases",
        "halogens",
        "metalloids",
        "chalcogens",
        "pnictogens",
        "d block",
        "s block",
        "p block",
        "scandium",
        "yttrium",
        "group 3",
        "uranium",
        "thorium"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Lanthanide",
    "qb": {
        "q": "lanthanide",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "Four elements are named after the Swedish village of Ytterby, whose quarry supplied the minerals in which they were found. Three of those four, terbium, erbium, and ytterbium, belong to this series, while the fourth, yttrium, does not.",
            "r": "For 10 points, name this series of 15 metals, from element 57 to element 71, found in the f-block."
        },
        {
            "p": "A steady shrinking of atomic size across this series, caused by poor shielding from 4f electrons, makes zirconium and hafnium almost exactly the same size. That “contraction” named for this series makes those two elements very hard to separate.",
            "r": "For 10 points, name these 15 elements that, along with scandium and yttrium, make up the rare earth elements."
        },
        {
            "p": "In 1984, General Motors and Sumitomo announced super-strong permanent magnets made of iron, boron, and neodymium, a member of this series. Magnets made with samarium, another member of this series, mixed with cobalt, keep working at even higher temperatures.",
            "r": "For 10 points, name this series of 15 elements, running from atomic number 57 to 71."
        },
        {
            "p": "The only member of this series with no stable isotopes was first identified in 1945 in uranium fission products at Oak Ridge, and it was named for the Titan who stole fire from the gods.",
            "r": "For 10 points, name this series of rare earth elements that sits in its own row below the main periodic table, above the actinides."
        },
        {
            "p": "In 1794, the Finnish chemist Johan Gadolin found a new “earth,” or oxide, containing the element yttrium, and a member of this series is named for him. That member, gadolinium, whose ion has seven unpaired electrons, is injected into patients as a contrast agent to make MRI images clearer.",
            "r": "For 10 points, name this series of 15 metals, from element 57 to element 71, often called rare earths."
        },
        {
            "p": "Red phosphors in old color TV screens and glowing anti-counterfeiting marks on euro banknotes use europium, a member of this series. Erbium, another member, boosts the light signals that carry internet data through fiber-optic cables.",
            "r": "For 10 points, name this series of f-block metals named for its first member, element 57."
        },
        {
            "p": "Carl Auer von Welsbach [“OW-er fon VELS-bahk”] showed in 1885 that a supposed element called didymium, meaning “twin,” was really a mixture of two members of this series, praseodymium and neodymium. Glassblowers wear goggles made with didymium glass to block the yellow glare of hot sodium.",
            "r": "For 10 points, name this series of rare earth metals from element 57 to element 71."
        },
        {
            "p": "Carl Gustaf Mosander named the first member of this series from a Greek word meaning “to lie hidden,” because it had been hiding in a cerium compound. Dysprosium, another member, gets its name from a Greek word meaning “hard to get.”",
            "r": "For 10 points, name this row of 15 elements that, along with the actinides, forms the f-block."
        },
        {
            "p": "Cerium, the most abundant member of this series, is about as common in Earth’s crust as copper. Almost every member of this series forms a stable +3 ion, though cerium can also reach +4 and europium can drop to +2.",
            "r": "For 10 points, name this series of elements numbered 57 through 71, often called rare earth metals."
        },
        {
            "p": "Monazite [“MON-uh-zite”] and bastnäsite [“BAST-nuh-site”] are the main ores of these metals, and the Bayan Obo mine in Inner Mongolia holds the largest known deposit of them. China produces most of the world’s supply of these elements.",
            "r": "For 10 points, name these elements, numbers 57 through 71, which include the neodymium used in magnets for electric car motors."
        },
        {
            "p": "Because members of this series behave so alike chemically, chemists once needed thousands of slow crystallization steps to separate them, until Frank Spedding’s team at Iowa State developed ion-exchange methods in the 1940s.",
            "r": "For 10 points, name this series of rare earth elements that sits below the main periodic table, just above the actinides."
        },
        {
            "p": "One member of this series was named in 1803 for Ceres, which had been discovered two years earlier and is classified as a dwarf planet. An alloy rich in that member, mixed with iron, makes the flints that throw sparks in lighters and camping fire starters.",
            "r": "For 10 points, name this series of metals from element 57 to element 71, also called rare earth elements."
        },
        {
            "p": "Chemists have debated whether this series’s last member, lutetium, or its first member belongs in group 3 of the periodic table. Lutetium was named by Georges Urbain [“oor-BAN”] for Lutetia, the ancient Roman name for Paris.",
            "r": "For 10 points, name this series of 15 elements in the f-block, often called rare earths."
        },
        {
            "p": "Holmium is named for Stockholm, and thulium is named for Thule, an old name for the far north; both belong to this series. Ytterbium, another member, is used in some of the world’s most precise atomic clocks.",
            "r": "For 10 points, name this series that runs from atomic number 57 to atomic number 71."
        },
        {
            "p": "Across this series, electrons fill the 4f subshell, which can hold up to 14 electrons. Members of this series are often placed in a separate row at the bottom of the periodic table to keep the table from getting too wide.",
            "r": "Along with the actinides, they are called inner transition metals. For 10 points, name this series of elements numbered 57 to 71."
        }
    ],
    "clues": [
        {
            "id": "range",
            "tier": "giveaway",
            "t": "The 15 metals from atomic number 57 (lanthanum) through 71 (lutetium)",
            "k": ["57", "71", "lanthanum", "lutetium", "15 metals"],
            "n": 0
        },
        {
            "id": "own-row",
            "tier": "giveaway",
            "t": "Usually shown in a separate row below the main periodic table, just above the actinides",
            "k": ["separate row", "actinides"],
            "n": 0
        },
        {
            "id": "rare-earths",
            "tier": "giveaway",
            "t": "With scandium and yttrium, they make up the rare earth elements, though most are not very rare",
            "k": ["rare earth", "scandium", "yttrium"],
            "n": 0
        },
        {
            "id": "f-block",
            "tier": "giveaway",
            "t": "Their electrons fill the 4f subshell; with the actinides they form the f-block, or inner transition metals",
            "k": ["4f", "f-block", "inner transition"],
            "n": 0
        },
        {
            "id": "magnets",
            "tier": "giveaway",
            "t": "Neodymium, one member, makes the strongest permanent magnets, used in headphones and electric car motors",
            "k": ["neodymium", "magnets", "electric car"],
            "n": 0,
            "rabbit": "Magnetism"
        },
        {
            "id": "plus-three",
            "tier": "middle",
            "t": "Almost all form stable +3 ions; cerium can also be +4 and europium +2",
            "k": ["+3", "cerium", "europium"],
            "n": 0
        },
        {
            "id": "contraction",
            "tier": "middle",
            "t": "Their “contraction”: atoms shrink across the series because 4f electrons shield the nucleus poorly",
            "k": ["contraction", "shield", "shrink"],
            "n": 0
        },
        {
            "id": "zr-hf",
            "tier": "middle",
            "t": "That contraction makes zirconium and hafnium nearly the same size and hard to separate",
            "k": ["zirconium", "hafnium"],
            "n": 0
        },
        {
            "id": "ytterby",
            "tier": "middle",
            "t": "Terbium, erbium, and ytterbium (plus yttrium) are named for the Swedish village of Ytterby",
            "k": ["ytterby", "terbium", "erbium"],
            "n": 0
        },
        {
            "id": "promethium",
            "tier": "middle",
            "t": "Promethium, named for Prometheus, is the only member with no stable isotopes; it was identified in 1945",
            "k": ["promethium", "prometheus", "no stable isotopes"],
            "n": 0,
            "rabbit": "Prometheus"
        },
        {
            "id": "gadolinium",
            "tier": "middle",
            "t": "Gadolinium, whose ion has seven unpaired electrons, is used as an MRI contrast agent",
            "k": ["gadolinium", "mri", "contrast agent"],
            "n": 0
        },
        {
            "id": "cerium-ceres",
            "tier": "middle",
            "t": "Cerium, the most abundant member (about as common as copper), was named in 1803 for Ceres",
            "k": ["ceres", "most abundant", "copper"],
            "n": 0
        },
        {
            "id": "china",
            "tier": "middle",
            "t": "China produces most of the world’s supply, much of it from Bayan Obo in Inner Mongolia; the main ores are monazite and bastnäsite",
            "k": ["china", "bayan obo", "monazite", "bastnäsite"],
            "n": 0
        },
        {
            "id": "mosander",
            "tier": "power",
            "t": "Carl Gustaf Mosander named the first member (1839) from the Greek for “to lie hidden”",
            "k": ["mosander", "lie hidden", "1839"],
            "n": 0
        },
        {
            "id": "dysprosium",
            "tier": "power",
            "t": "Dysprosium’s name comes from the Greek for “hard to get”",
            "k": ["dysprosium", "hard to get"],
            "n": 0
        },
        {
            "id": "didymium",
            "tier": "power",
            "t": "Carl Auer von Welsbach split “didymium” (“twin”) into praseodymium and neodymium in 1885; didymium goggles block sodium’s yellow glare",
            "k": ["didymium", "praseodymium", "auer von welsbach", "goggles"],
            "n": 0
        },
        {
            "id": "gadolin",
            "tier": "power",
            "t": "Gadolinium honors Johan Gadolin, the Finnish chemist who found yttrium’s oxide in 1794",
            "k": ["johan gadolin", "finnish", "1794"],
            "n": 0
        },
        {
            "id": "samarium-cobalt",
            "tier": "power",
            "t": "Samarium–cobalt magnets keep working at higher temperatures than neodymium magnets",
            "k": ["samarium", "cobalt"],
            "n": 0
        },
        {
            "id": "gm-sumitomo",
            "tier": "power",
            "t": "General Motors and Sumitomo announced neodymium–iron–boron magnets in 1984",
            "k": ["sumitomo", "general motors", "boron", "1984"],
            "n": 0
        },
        {
            "id": "europium",
            "tier": "power",
            "t": "Europium makes red phosphors in old TV screens and glows in euro banknote security marks",
            "k": ["europium", "red phosphors", "euro banknote"],
            "n": 0
        },
        {
            "id": "erbium",
            "tier": "power",
            "t": "Erbium boosts light signals in fiber-optic cables",
            "k": ["erbium", "fiber-optic"],
            "n": 0
        },
        {
            "id": "spedding",
            "tier": "power",
            "t": "Frank Spedding’s team at Iowa State separated them with ion exchange in the 1940s, replacing thousands of slow crystallizations",
            "k": ["spedding", "ion exchange", "iowa state"],
            "n": 0
        },
        {
            "id": "mischmetal",
            "tier": "power",
            "t": "Mischmetal, an alloy rich in cerium, is mixed with iron to make the flints in lighters and fire starters",
            "k": ["mischmetal", "flints", "fire starters"],
            "n": 0
        },
        {
            "id": "lutetium",
            "tier": "power",
            "t": "Lutetium, the last member, is named for Lutetia, the Roman name for Paris; chemists debate whether it belongs in group 3",
            "k": ["lutetia", "paris", "group 3"],
            "n": 0
        },
        {
            "id": "holmium-thulium",
            "tier": "power",
            "t": "Holmium is named for Stockholm, and thulium for Thule, an old name for the far north",
            "k": ["holmium", "stockholm", "thulium", "thule"],
            "n": 0
        },
        {
            "id": "ytterbium-clocks",
            "tier": "power",
            "t": "Ytterbium is used in some of the most precise atomic clocks",
            "k": ["ytterbium", "atomic clocks"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Not the actinides",
        "body": "The actinides sit in the row just below this series, and the two rows are twins on the periodic table: both are f-block “inner transition metals” pulled out into their own rows. The actinides (elements 89 to 103) include uranium and plutonium, and all of them are radioactive. “Rare earth elements” is a near miss too, because that group also includes scandium and yttrium, so it may earn only a prompt.",
        "fix": "Neodymium magnets, the Ytterby elements, the contraction that shrinks atoms, 4f orbitals, and element numbers 57 to 71 point here. Radioactivity, uranium, thorium, plutonium, 5f orbitals, and element numbers 89 to 103 point to the actinides.",
        "line": "Real answer line: <b><u>Lanthanide</u></b>s (accept <u>lanthanoid</u>s; prompt on <u>rare earth</u> elements, <u>f-block</u> elements, or <u>inner transition</u> metals; do not accept “actinides”)"
    },
    "tests": {
        "right": [
            "Lanthanides",
            "lanthanide",
            "Lanthanoids",
            "Lanthanide series",
            "lanthenides"
        ],
        "prompt": [
            "Rare earth elements",
            "Inner transition metals",
            "f-block"
        ],
        "wrong": [
            "Actinides",
            "Lanthanum",
            "Alkaline earth metals",
            "Transition metals",
            "Neodymium",
            "Actinoids"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
