import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TIP = "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."

data = {
    "id": "sunspots",
    "name": "Sunspots",
    "mono": "SSP",
    "category": "Astronomy",
    "qbCategory": "Science · Other Science (Astronomy)",
    "kicker": "Dark, cooler patches on the Sun · Rise and fall in an 11-year cycle",
    "dates": "First seen through telescopes 1610–1611; cycle found 1843",
    "briefing": "Sunspots are dark patches on the Sun’s glowing surface, and big ones can be several times wider than Earth. They look dark only because they are cooler than the gas around them, and they are cooler because powerful magnetic fields block the heat rising from below. Their numbers rise and fall in a cycle of about 11 years, and from about 1645 to 1715 they nearly vanished, a stretch called the Maunder Minimum.",
    "answerHtml": "<b><u>sunspot</u></b>s (prompt on <u>spots</u> or <u>active regions</u>; do not accept “solar flares”)",
    "accept": [
        "sunspots",
        "sunspot",
        "sun spots",
        "sun spot"
    ],
    "prompt": [
        "spots",
        "spot",
        "dark spots",
        "spots on the sun",
        "dark spots on the sun",
        "active regions",
        "active region",
        "solar active regions",
        "solar active region"
    ],
    "reject": [
        "sun",
        "sol",
        "solar flare",
        "solar flares",
        "flare",
        "flares",
        "coronal mass ejection",
        "coronal mass ejections",
        "cme",
        "cmes",
        "solar wind",
        "solar prominence",
        "solar prominences",
        "prominence",
        "prominences",
        "faculae",
        "facula",
        "plage",
        "granules",
        "granulation",
        "starspot",
        "starspots",
        "solar cycle",
        "solar maximum",
        "solar minimum",
        "maunder minimum",
        "corona",
        "photosphere"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Sunspot",
    "qb": {
        "q": "sunspot",
        "found": 0,
        "tip": TIP
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "For 17 years, Heinrich Schwabe [“SHVAH-buh”] watched the Sun almost every clear day, hoping to catch an unknown planet inside Mercury’s orbit crossing in front of it. Instead, he found that these features rise and fall in number about every ten years, a pattern he announced in 1843.",
            "r": "That cycle is usually given as about 11 years. For 10 points, name these dark, cool patches on the Sun’s surface."
        },
        {
            "p": "In 1908, George Ellery Hale studied these features at Mount Wilson Observatory in California and noticed that single lines in their spectrum were split into several lines. That splitting, the Zeeman [“ZAY-mahn”] effect, revealed the force behind them.",
            "r": "They hold intense magnetic fields, which block rising heat and make them cooler and darker than their surroundings. For 10 points, name these patches on the Sun."
        },
        {
            "p": "Writing under the pen name Apelles [“uh-PEL-eez”], the Jesuit Christoph Scheiner [“SHY-ner”] argued that these features were small objects circling the Sun. In letters to Mark Welser [“VEL-zer”], published in 1613, Galileo replied that they lay on or very near the Sun’s surface.",
            "r": "Galileo also used them to show that the Sun rotates. For 10 points, name these dark patches on the Sun."
        },
        {
            "p": "From about 1645 to 1715, astronomers saw so few of these features that the stretch is named for Edward Walter Maunder [“MAWN-der”]. That period overlapped part of the Little Ice Age, a cold spell in Europe and North America, though scientists debate how closely the two are linked.",
            "r": "For 10 points, name these dark, cooler regions on the Sun that come and go in an 11-year cycle."
        },
        {
            "p": "When Edward and Annie Maunder plotted the latitudes of these features against time in 1904, the pattern looked like a row of butterfly wings. It shows that early in each cycle these features appear at middle latitudes, and later ones form closer to the equator, a pattern called Spörer’s [“SHPUR-erz”] law.",
            "r": "These features come and go in a cycle of about 11 years. For 10 points, name these dark patches on the Sun."
        },
        {
            "p": "Rudolf Wolf of Zürich counted these features by multiplying the number of their groups by ten and adding the number of individual ones. Using old records, Wolf traced their cycles back to one that began in 1755, which is still numbered Cycle 1.",
            "r": "For 10 points, name these dark patches on the Sun, whose numbers peak about every 11 years."
        },
        {
            "p": "These features usually come in pairs or groups with opposite magnetic polarity, and the leading members of those pairs swap polarity from one cycle to the next. Because of that flip, the Sun’s full magnetic cycle lasts about 22 years, a period named for George Ellery Hale.",
            "r": "For 10 points, name these dark regions on the Sun whose numbers rise and fall every 11 years or so."
        },
        {
            "p": "In 1909, John Evershed, working at an observatory in southern India, found that gas flows outward along the streaky filaments in the outer part of these features. That flow is named the Evershed effect.",
            "r": "These features have a dark center called the umbra and a lighter rim called the penumbra. For 10 points, name these cool patches on the Sun."
        },
        {
            "p": "In 1769, the Scottish astronomer Alexander Wilson noticed that these features look lopsided as the Sun’s spin carries them toward its edge, which suggested that they are shallow dips in the Sun’s surface. Large ones can be several times wider than Earth.",
            "r": "For 10 points, name these dark, cooler patches on the Sun’s visible surface, the photosphere."
        },
        {
            "p": "The oldest known drawing of these features appears in a chronicle by the English monk John of Worcester [“WUSS-ter”], from December 1128. Chinese astronomers had recorded seeing them without telescopes more than a thousand years earlier.",
            "r": "Centuries later, Galileo studied them with a telescope. For 10 points, name these dark blotches on the Sun."
        },
        {
            "p": "By carefully tracking these features in the 1850s, Richard Carrington showed that the Sun’s equator spins faster than its higher latitudes. On September 1, 1859, Carrington saw a brilliant white-light flare burst out above a large group of them.",
            "r": "For 10 points, name these dark regions on the Sun, from which solar flares often erupt."
        },
        {
            "p": "Even though these features give off less light than their surroundings, the Sun gives off about 0.1 percent more energy when they are most common, because bright patches called faculae [“FAK-yuh-lee”] around them more than make up the difference. Satellites measuring sunlight above Earth’s atmosphere confirmed that pattern.",
            "r": "For 10 points, name these cool, dark spots on the Sun, whose numbers peak about every 11 years."
        },
        {
            "p": "Thomas Harriot made the first known drawings of these features through a telescope in December 1610. In 1611, Johannes Fabricius published the first printed account of them, arguing that their motion across the Sun showed that it spins.",
            "r": "Galileo and Christoph Scheiner soon argued about them. For 10 points, name these dark spots on the Sun."
        },
        {
            "p": "A. E. Douglass founded tree-ring dating, or dendrochronology, while searching the growth rings of trees for traces of the cycle of these features. Strong solar storms that erupt near these features can disrupt radio signals and power grids on Earth.",
            "r": "For 10 points, name these magnetic patches on the Sun, which have a dark umbra and a lighter penumbra."
        },
        {
            "p": "A stretch from about 1790 to 1830 with very few of these features is named the Dalton Minimum. In October 2024, NASA and NOAA announced that the Sun had entered the maximum phase of Solar Cycle 25, when these features are most common.",
            "r": "Their magnetic fields block rising heat, making them cooler than their surroundings. For 10 points, name these dark patches on the Sun."
        }
    ],
    "clues": [
        {
            "id": "dark-cool",
            "tier": "giveaway",
            "t": "Dark patches on the Sun’s visible surface (the photosphere) that are cooler than the gas around them",
            "k": ["dark patches", "cooler", "photosphere"],
            "n": 0,
            "rabbit": "The Sun"
        },
        {
            "id": "eleven-year",
            "tier": "giveaway",
            "t": "Their numbers rise and fall in a cycle of about 11 years",
            "k": ["11 years", "cycle"],
            "n": 0
        },
        {
            "id": "magnetic",
            "tier": "giveaway",
            "t": "Caused by strong magnetic fields that block heat rising from below",
            "k": ["magnetic fields", "block heat"],
            "n": 0,
            "rabbit": "Magnetic fields"
        },
        {
            "id": "umbra-penumbra",
            "tier": "giveaway",
            "t": "Each has a dark center, the umbra, and a lighter, streaky rim, the penumbra",
            "k": ["umbra", "penumbra"],
            "n": 0
        },
        {
            "id": "galileo",
            "tier": "middle",
            "t": "Galileo studied them with a telescope and used them to show that the Sun rotates",
            "k": ["galileo", "telescope", "rotates"],
            "n": 0,
            "rabbit": "Galileo Galilei"
        },
        {
            "id": "maunder-minimum",
            "tier": "middle",
            "t": "The Maunder Minimum (about 1645–1715) had very few of them; it overlapped part of the Little Ice Age",
            "k": ["maunder minimum", "little ice age", "1645"],
            "n": 0
        },
        {
            "id": "schwabe",
            "tier": "middle",
            "t": "Heinrich Schwabe announced their cycle in 1843, after years of watching the Sun for an unknown planet inside Mercury’s orbit",
            "k": ["schwabe", "1843", "mercury"],
            "n": 0
        },
        {
            "id": "hale-1908",
            "tier": "middle",
            "t": "George Ellery Hale used the Zeeman effect in 1908 to show that they hold strong magnetic fields",
            "k": ["hale", "zeeman effect", "1908"],
            "n": 0
        },
        {
            "id": "flares",
            "tier": "middle",
            "t": "Solar flares and coronal mass ejections often burst from the active regions around them",
            "k": ["solar flares", "coronal mass ejections", "active regions"],
            "n": 0
        },
        {
            "id": "butterfly",
            "tier": "middle",
            "t": "Plotting their latitudes over time gives the Maunders’ “butterfly diagram” (1904)",
            "k": ["butterfly diagram", "latitudes", "1904"],
            "n": 0
        },
        {
            "id": "scheiner",
            "tier": "middle",
            "t": "The Jesuit Christoph Scheiner (pen name “Apelles”) said they were objects circling the Sun; Galileo said they were on its surface",
            "k": ["scheiner", "apelles"],
            "n": 0
        },
        {
            "id": "size-life",
            "tier": "middle",
            "t": "Big ones can be several times wider than Earth; they last from a few hours to a few months",
            "k": ["wider than earth", "few months"],
            "n": 0
        },
        {
            "id": "carrington",
            "tier": "middle",
            "t": "Richard Carrington tracked them to show that the Sun’s equator spins fastest, and saw the 1859 white-light flare above a large group",
            "k": ["carrington", "1859", "equator"],
            "n": 0
        },
        {
            "id": "hale-cycle",
            "tier": "power",
            "t": "Pairs have opposite polarity, and the leaders swap polarity each cycle, so the Sun’s full magnetic (Hale) cycle is about 22 years",
            "k": ["22 years", "polarity", "hale cycle"],
            "n": 0
        },
        {
            "id": "wolf-number",
            "tier": "power",
            "t": "Rudolf Wolf’s count: ten times the number of groups plus the number of individual spots",
            "k": ["rudolf wolf", "ten times", "groups"],
            "n": 0
        },
        {
            "id": "cycle-1755",
            "tier": "power",
            "t": "Their cycles are numbered from one that began in 1755, which is called Cycle 1",
            "k": ["1755", "numbered"],
            "n": 0
        },
        {
            "id": "sporer",
            "tier": "power",
            "t": "Spörer’s law: early in a cycle they appear at middle latitudes, and later ones form closer to the equator",
            "k": ["spörer", "middle latitudes"],
            "n": 0
        },
        {
            "id": "evershed",
            "tier": "power",
            "t": "John Evershed found in 1909, in southern India, that gas flows outward through the penumbra (the Evershed effect)",
            "k": ["evershed", "1909", "outward"],
            "n": 0
        },
        {
            "id": "wilson",
            "tier": "power",
            "t": "Alexander Wilson saw in 1769 that they look lopsided near the Sun’s edge, suggesting that they are shallow dips",
            "k": ["alexander wilson", "1769", "shallow dips"],
            "n": 0
        },
        {
            "id": "worcester",
            "tier": "power",
            "t": "The oldest known drawing of them is in John of Worcester’s chronicle (1128); Chinese astronomers recorded them much earlier",
            "k": ["john of worcester", "1128", "chinese"],
            "n": 0
        },
        {
            "id": "harriot-fabricius",
            "tier": "power",
            "t": "Thomas Harriot drew them through a telescope in 1610; Johannes Fabricius published the first account of them in 1611",
            "k": ["harriot", "fabricius", "1610", "1611"],
            "n": 0
        },
        {
            "id": "welser",
            "tier": "power",
            "t": "Galileo’s letters about them to Mark Welser were published in 1613",
            "k": ["welser", "1613", "letters"],
            "n": 0
        },
        {
            "id": "faculae",
            "tier": "power",
            "t": "Bright faculae around them make the Sun about 0.1 percent brighter when they are most common",
            "k": ["faculae", "0.1 percent"],
            "n": 0
        },
        {
            "id": "douglass",
            "tier": "power",
            "t": "A. E. Douglass founded tree-ring dating (dendrochronology) while looking for their cycle in tree rings",
            "k": ["douglass", "tree-ring", "dendrochronology"],
            "n": 0,
            "rabbit": "Trees"
        },
        {
            "id": "dalton",
            "tier": "power",
            "t": "The Dalton Minimum (about 1790–1830) was another stretch with very few of them",
            "k": ["dalton minimum", "1790"],
            "n": 0
        },
        {
            "id": "cycle-25",
            "tier": "power",
            "t": "Solar Cycle 25 began in December 2019; in October 2024, NASA and NOAA announced that it had reached its maximum phase",
            "k": ["solar cycle 25", "2019", "2024"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Spots, flares, or star?",
        "body": "Sunspot clues sit right next to clues for other answer lines. Solar flares and coronal mass ejections are sudden eruptions that burst from the active regions around these spots, so players who hear about Carrington’s 1859 flare or a big solar storm may blurt out “solar flares.” Tossups about the whole Sun also mention sunspots, and then the answer is the Sun.",
        "fix": "“These dark regions” or “these features,” with the umbra and penumbra, the 11-year cycle, Schwabe, Hale’s magnetic fields, the butterfly diagram, or the Maunder Minimum, means sunspots. A sudden flash of energy is a solar flare; a giant cloud of gas blasted into space is a coronal mass ejection; “this star” means the Sun.",
        "line": "Real answer line: <b><u>sunspot</u></b>s (prompt on <u>spots</u>; do not accept “solar flares”)"
    },
    "tests": {
        "right": [
            "Sunspots",
            "sunspot",
            "Sun spots",
            "Sunspts",
            "sunspot groups"
        ],
        "prompt": [
            "spots",
            "active regions"
        ],
        "wrong": [
            "Solar flares",
            "The Sun",
            "Coronal mass ejections",
            "Faculae",
            "Solar wind",
            "Starspots"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
