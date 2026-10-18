import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "avogadros-number",
    "name": "Avogadro’s number",
    "mono": "AVO",
    "category": "Chemistry",
    "qbCategory": "Science · Chemistry",
    "kicker": "About 6.02 × 10²³ · The number of particles in one mole",
    "dates": "Value fixed exactly in 2019",
    "briefing": "Avogadro’s number is about 602 sextillion (6.02 × 10²³), the number of atoms or molecules in one mole, the chemist’s supersized version of a “dozen.” Just 18 grams of water, a little more than a tablespoon, holds that many molecules. Chemistry fans celebrate Mole Day every October 23 from 6:02 a.m. to 6:02 p.m., and since 2019 the number has been fixed at exactly 6.02214076 × 10²³.",
    "answerHtml": "<b><u>Avogadro’s number</u></b> (accept <u>Avogadro’s constant</u> or <u>N<sub>A</sub></u>; prompt on <u>Avogadro</u> alone or on the value 6.02 × 10<sup>23</sup>)",
    "accept": [
        "avogadros number",
        "avogadro number",
        "avogadros constant",
        "avogadro constant",
        "n a"
    ],
    "prompt": [
        "avogadro",
        "avogadros",
        "amedeo avogadro",
        "6 02 x 10 23",
        "6 022 x 10 23",
        "6 02 10 23",
        "6 022 10 23",
        "6 02e23",
        "6 022e23",
        "6 02 times 10 to the 23rd",
        "6 022 times 10 to the 23rd",
        "6 02 x 10 to the 23rd"
    ],
    "reject": [
        "avogadros law",
        "avogadro law",
        "avogadros hypothesis",
        "avogadros principle",
        "mole",
        "moles",
        "molar mass",
        "molarity",
        "molar volume",
        "gas constant",
        "ideal gas constant",
        "boltzmann constant",
        "boltzmanns constant",
        "faraday constant",
        "faradays constant",
        "planck constant",
        "plancks constant",
        "loschmidt constant",
        "loschmidts constant",
        "loschmidt number",
        "loschmidts number",
        "dalton",
        "atomic mass unit"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Avogadro_constant",
    "qb": {
        "q": "Avogadro",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "Jean Perrin gave this number its name in 1909 and measured it by tracking the jittery Brownian motion of tiny particles, work that earned him the 1926 Nobel Prize in Physics. Albert Einstein had shown in 1905 how Brownian motion could be used to find it.",
            "r": "For 10 points, name this number of particles in one mole, about 6.02 times 10 to the 23rd."
        },
        {
            "p": "Dividing the Faraday constant, about 96,485 coulombs per mole, by the charge of a single electron gives this constant. Robert Millikan’s oil-drop measurement of that electron charge let scientists calculate this constant much more accurately.",
            "r": "For 10 points, name this constant, roughly 6.02 times 10 to the 23rd, which counts the particles in a mole."
        },
        {
            "p": "Johann Josef Loschmidt [“LOHSH-mit”] made one of the first estimates of this quantity in 1865, working from the size of gas molecules. Before 2019, this quantity equaled the number of atoms in exactly 12 grams of carbon-12.",
            "r": "For 10 points, name this number of particles in one mole, about 6.022 times 10 to the 23rd."
        },
        {
            "p": "Scientists pinned down this constant by counting the atoms in nearly perfect, polished spheres of silicon-28, using X-rays to measure the spacing of the atoms in the crystal. In 2019, the mole was redefined so that it depends on an exact value of this constant.",
            "r": "For 10 points, name this constant, about 6.02 times 10 to the 23rd per mole."
        },
        {
            "p": "At the 1860 Karlsruhe Congress, Stanislao Cannizzaro revived an 1811 hypothesis by this number’s namesake, helping chemists agree on atomic weights. That namesake, an Italian count, said that equal volumes of gases at the same temperature and pressure contain equal numbers of molecules.",
            "r": "For 10 points, name this number, about 6.02 times 10 to the 23rd, of particles in a mole."
        },
        {
            "p": "One gram equals about this many daltons, or atomic mass units, which is why a substance’s molar mass in grams per mole matches the mass of one of its molecules in daltons. About 18 grams of water contain this many molecules.",
            "r": "For 10 points, name this number of particles in one mole, roughly 6.02 times 10 to the 23rd."
        },
        {
            "p": "At standard temperature and pressure, about 22.4 liters of any ideal gas contain this many molecules, whether the gas is helium, oxygen, or carbon dioxide. That fact follows from a hypothesis made in 1811 by this number’s namesake.",
            "r": "For 10 points, name this number, about 6.02 times 10 to the 23rd, of particles in a mole."
        },
        {
            "p": "This quantity is written as N with a subscript A when it is treated as a constant with units of “per mole.” Multiplying the number of moles in a sample by this quantity gives the number of atoms or molecules in the sample.",
            "r": "Mole Day is celebrated on October 23 in its honor. For 10 points, name this number, about 6.02 times 10 to the 23rd."
        },
        {
            "p": "Albert Einstein’s 1905 doctoral thesis estimated this number by studying how dissolved sugar molecules make water thicker, or more viscous. Multiplying this number by the charge of one electron gives the Faraday constant.",
            "r": "For 10 points, name this number of particles in one mole, roughly 6.02 times 10 to the 23rd."
        },
        {
            "p": "Dividing a substance’s molar mass by this constant gives the mass of a single atom or molecule of that substance. Because its value was fixed exactly in 2019, this constant no longer has any measurement uncertainty.",
            "r": "For 10 points, name this constant, about 6.02 times 10 to the 23rd per mole."
        },
        {
            "p": "Depositing one mole of silver metal by electrolysis takes this many electrons, which together carry about 96,485 coulombs of charge. Just as a dozen means 12 of something, a mole means this many of something.",
            "r": "Chemists honor it every October 23 on Mole Day. For 10 points, name this number, about 6.02 times 10 to the 23rd."
        },
        {
            "p": "Tiny grains of a yellow resin called gamboge [“gam-BOHJ”], settling in water while gravity battled the jostling of Brownian motion, let Jean Perrin measure this number. Those experiments helped convince scientists that atoms are real.",
            "r": "For 10 points, name this number of particles in a mole, about 6.02 times 10 to the 23rd."
        },
        {
            "p": "This number explains why about 12 grams of carbon, 18 grams of water, and 2 grams of hydrogen gas all contain the same number of particles: each sample is one mole.",
            "r": "October 23 is celebrated as Mole Day in its honor. For 10 points, name this number, about 6.02 times 10 to the 23rd."
        },
        {
            "p": "This constant is named for a scientist born in Turin in 1776, the same year as the Declaration of Independence, who never measured the constant himself. That scientist’s hypothesis about gases was largely ignored until after his death.",
            "r": "For 10 points, name this number of particles in one mole, about 6.02 times 10 to the 23rd."
        },
        {
            "p": "Dividing the ideal gas constant, about 8.314 joules per mole per kelvin, by the Boltzmann constant gives this constant, which links gas laws written for single molecules to gas laws written for whole moles.",
            "r": "Since 2019, its value has been exactly 6.02214076 times 10 to the 23rd. For 10 points, name this constant, the number of particles in a mole."
        }
    ],
    "clues": [
        {
            "id": "value",
            "tier": "giveaway",
            "t": "Its value is about 6.02 × 10²³ (6.02 times 10 to the 23rd)",
            "k": ["10 to the 23rd", "6.02"],
            "n": 0
        },
        {
            "id": "mole",
            "tier": "giveaway",
            "t": "Tells how many particles (atoms, molecules, or ions) are in one mole of a substance",
            "k": ["particles", "mole"],
            "n": 0
        },
        {
            "id": "italian",
            "tier": "giveaway",
            "t": "Named for an Italian count who studied gases in the early 1800s",
            "k": ["italian", "count", "gases"],
            "n": 0
        },
        {
            "id": "mole-day",
            "tier": "giveaway",
            "t": "Mole Day is celebrated every October 23, from 6:02 a.m. to 6:02 p.m.",
            "k": ["mole day", "october 23"],
            "n": 0
        },
        {
            "id": "carbon-12",
            "tier": "giveaway",
            "t": "Before 2019, it equaled the number of atoms in exactly 12 grams of carbon-12",
            "k": ["carbon-12", "12 grams"],
            "n": 0
        },
        {
            "id": "exact-2019",
            "tier": "middle",
            "t": "Since the 2019 redefinition of SI units, it is fixed at exactly 6.02214076 × 10²³ per mole",
            "k": ["redefinition", "exactly", "2019"],
            "n": 0
        },
        {
            "id": "units",
            "tier": "middle",
            "t": "As a constant it is written N sub A (N with a subscript A) and has units of “per mole”",
            "k": ["per mole", "subscript"],
            "n": 0
        },
        {
            "id": "stp",
            "tier": "middle",
            "t": "About 22.4 liters of an ideal gas at standard temperature and pressure (0 °C, 1 atm) hold this many molecules",
            "k": ["22.4 liters", "standard temperature"],
            "n": 0,
            "rabbit": "Ideal gas law"
        },
        {
            "id": "water-18",
            "tier": "middle",
            "t": "About 18 grams of water, which is one mole, contain this many molecules",
            "k": ["18 grams", "water"],
            "n": 0
        },
        {
            "id": "daltons",
            "tier": "middle",
            "t": "One gram equals about this many daltons (atomic mass units), so molar mass in grams matches molecular mass in daltons",
            "k": ["atomic mass units", "daltons", "molar mass"],
            "n": 0
        },
        {
            "id": "one-molecule",
            "tier": "middle",
            "t": "Dividing a substance’s molar mass by it gives the mass of a single atom or molecule",
            "k": ["single atom", "dividing"],
            "n": 0
        },
        {
            "id": "hypothesis-1811",
            "tier": "middle",
            "t": "Its namesake’s 1811 hypothesis: equal volumes of gases at the same temperature and pressure contain equal numbers of molecules",
            "k": ["equal volumes", "hypothesis", "1811"],
            "n": 0
        },
        {
            "id": "born-1776",
            "tier": "middle",
            "t": "Its namesake was born in Turin in 1776 and never measured it himself",
            "k": ["turin", "1776"],
            "n": 0
        },
        {
            "id": "perrin",
            "tier": "power",
            "t": "Jean Perrin named it in 1909 and measured it using Brownian motion, winning the 1926 Nobel Prize in Physics",
            "k": ["jean perrin", "brownian motion", "1909", "1926"],
            "n": 0,
            "rabbit": "Brownian motion"
        },
        {
            "id": "gamboge",
            "tier": "power",
            "t": "Perrin watched tiny grains of gamboge resin settle in water, balancing gravity against Brownian motion",
            "k": ["gamboge", "settle"],
            "n": 0
        },
        {
            "id": "einstein",
            "tier": "power",
            "t": "Albert Einstein showed how to calculate it in 1905, in his doctoral thesis on sugar solutions and his paper on Brownian motion",
            "k": ["doctoral thesis", "einstein", "sugar"],
            "n": 0,
            "rabbit": "Albert Einstein"
        },
        {
            "id": "loschmidt",
            "tier": "power",
            "t": "Johann Josef Loschmidt made one of the first estimates of it in 1865, from the size of gas molecules",
            "k": ["loschmidt", "1865"],
            "n": 0
        },
        {
            "id": "faraday",
            "tier": "power",
            "t": "The Faraday constant (about 96,485 coulombs per mole) equals it times the charge of one electron",
            "k": ["faraday constant", "coulombs", "96,485"],
            "n": 0
        },
        {
            "id": "millikan",
            "tier": "power",
            "t": "Robert Millikan’s oil-drop measurement of the electron’s charge let scientists calculate it accurately",
            "k": ["millikan", "oil-drop"],
            "n": 0
        },
        {
            "id": "silver",
            "tier": "power",
            "t": "Depositing one mole of silver by electrolysis takes this many electrons",
            "k": ["electrolysis", "silver"],
            "n": 0,
            "rabbit": "Electrolysis"
        },
        {
            "id": "gas-constant",
            "tier": "power",
            "t": "The ideal gas constant R (about 8.314 joules per mole per kelvin) equals it times the Boltzmann constant",
            "k": ["boltzmann constant", "gas constant", "8.314"],
            "n": 0,
            "rabbit": "Gas constant"
        },
        {
            "id": "silicon-spheres",
            "tier": "power",
            "t": "Scientists counted the atoms in nearly perfect spheres of silicon-28, using X-rays to measure the spacing between atoms",
            "k": ["silicon-28", "spheres", "x-rays"],
            "n": 0
        },
        {
            "id": "cannizzaro",
            "tier": "power",
            "t": "Stanislao Cannizzaro revived its namesake’s hypothesis at the 1860 Karlsruhe Congress",
            "k": ["cannizzaro", "karlsruhe", "1860"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Number, law, or mole?",
        "body": "This number’s namesake also names a separate answer line, Avogadro’s law: equal volumes of gases at the same temperature and pressure contain equal numbers of molecules. The mole is the other trap: the mole is the unit (like “a dozen”), while this is the count of particles in one mole. Saying just “Avogadro” only earns a prompt.",
        "fix": "A value (6.02 × 10²³), Mole Day, Perrin, the Faraday constant, or silicon spheres means the number, also called the constant. “Equal volumes of gases” means Avogadro’s law, and “this unit” means the mole. Always finish with “number” or “constant.”",
        "line": "Real answer line: <b><u>Avogadro’s number</u></b> (or <u>Avogadro’s constant</u>; accept N<sub>A</sub>; prompt on <u>Avogadro</u>)"
    },
    "tests": {
        "right": [
            "Avogadro’s number",
            "Avogadro's constant",
            "Avagadros number",
            "avogadro number",
            "N_A"
        ],
        "prompt": [
            "Avogadro",
            "6.02 x 10^23"
        ],
        "wrong": [
            "Avogadro’s law",
            "Mole",
            "Gas constant",
            "Boltzmann constant",
            "Loschmidt number"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
