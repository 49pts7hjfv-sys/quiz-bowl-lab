import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TIP = "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."

LINE = "<b><u>Gold</u></b> (accept <u>Au</u>; do not accept “fool’s gold” or “pyrite”)"

data = {
    "id": "gold",
    "name": "Gold",
    "mono": "AU",
    "category": "Chemistry",
    "qbCategory": "Science · Chemistry",
    "kicker": "Element 79, the most malleable metal · Treasured for thousands of years",
    "dates": "Known since prehistoric times",
    "briefing": "Gold is the soft, shiny yellow metal that people have treasured for thousands of years, from the funeral mask of King Tutankhamun to modern wedding rings. Its symbol, Au, comes from the Latin word aurum, and it is the most malleable metal: one gram can be hammered into a sheet about a meter on each side. Because it does not rust or tarnish, gold from ancient tombs still shines.",
    "answerHtml": LINE,
    "accept": [
        "gold",
        "au",
        "element 79",
        "gold metal",
        "elemental gold",
        "metallic gold"
    ],
    "prompt": [],
    "reject": [
        "silver",
        "ag",
        "copper",
        "platinum",
        "palladium",
        "mercury",
        "lead",
        "iron",
        "tungsten",
        "bismuth",
        "brass",
        "bronze",
        "electrum",
        "pyrite",
        "iron pyrite",
        "fools gold",
        "fool gold",
        "chalcopyrite",
        "gold rush",
        "california gold rush",
        "klondike gold rush",
        "klondike",
        "gold standard",
        "gold coast",
        "gold chloride",
        "chloroauric acid",
        "aqua regia",
        "philosophers stone",
        "midas",
        "king midas",
        "el dorado",
        "fort knox"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Gold",
    "qb": {"q": "gold", "found": 0, "tip": TIP},
    "sample": {"n": 0, "note": "no real tossups checked yet"},
    "tossups": [
        {
            "p": "In 1980, Glenn Seaborg’s team used a particle accelerator to turn several thousand atoms of bismuth into this element, a feat that cost far more than the product was worth. Alchemists linked this metal with the Sun.",
            "r": "Alchemists also sought a “philosopher’s stone” that could turn lead into this metal. For 10 points, name this precious element with atomic number 79."
        },
        {
            "p": "In the 1920s, Fritz Haber spent years trying to pull this element out of seawater to help Germany pay its World War I reparations, but the oceans held far less of it than earlier measurements had suggested.",
            "r": "This metal’s symbol comes from the Latin word aurum. For 10 points, name this precious yellow element with atomic number 79."
        },
        {
            "p": "In 1940, as German troops occupied Copenhagen, George de Hevesy [“HEV-eh-shee”] hid two Nobel Prize medals from the Nazis by dissolving them in aqua regia, a mix of nitric and hydrochloric acids that can dissolve this metal. The metal was later recovered and the medals were recast.",
            "r": "This metal does not tarnish, and it resists most other acids. For 10 points, name this precious metal, element number 79."
        },
        {
            "p": "The Roman Lycurgus [“ly-KUR-gus”] Cup looks green in reflected light but glows red when lit from behind, because its glass holds tiny particles of silver and this metal. In 1857, Michael Faraday made a ruby-red liquid holding specks of this metal far too small to see.",
            "r": "Pure samples of this metal are called 24-karat. For 10 points, name this precious yellow metal, element number 79."
        },
        {
            "p": "Einstein’s theory of relativity helps explain this metal’s color: electrons in its heavy atoms move so fast that their energies shift, so the metal absorbs blue light and reflects yellow. Sheets of this metal thin enough to see through let greenish-blue light pass.",
            "r": "One gram of this most malleable metal can be hammered into a sheet about a square meter in size. For 10 points, name this element with atomic number 79."
        },
        {
            "p": "In 2017, astronomers studied the glow from a collision of two neutron stars that gravitational-wave detectors had picked up, and found signs that such crashes forge this element and other heavy metals. On Earth, this element has only one stable isotope, with mass number 197.",
            "r": "Its chemical symbol comes from the Latin aurum. For 10 points, name this precious yellow metal, found at Sutter’s Mill in 1848."
        },
        {
            "p": "Hans Geiger and Ernest Marsden fired alpha particles at a thin foil of this metal in 1909 and saw a few of them bounce almost straight back. In 1911, Ernest Rutherford used their results to discover the atomic nucleus.",
            "r": "That foil could be made very thin because this element is the most malleable metal. For 10 points, name this element with atomic number 79."
        },
        {
            "p": "Many rapid home tests, including some for COVID-19, form their colored result line from nanoparticles of this metal, which look red instead of yellow. Electronics makers coat connectors with this metal because it conducts electricity well and does not corrode.",
            "r": "For 10 points, name this precious metal whose chemical symbol comes from the Latin word aurum."
        },
        {
            "p": "Each of the 18 hexagonal mirror segments of the James Webb Space Telescope is coated with a very thin layer of this metal, which reflects infrared light extremely well. Spacesuit helmet visors are also coated with this metal to block harsh sunlight.",
            "r": "King Midas could turn whatever he touched into this metal. For 10 points, name this element with atomic number 79."
        },
        {
            "p": "Mixing this metal with copper makes a “rose” alloy, and mixing it with nickel or palladium makes a “white” alloy. Jewelers measure this metal’s purity in karats, so an 18-karat ring is 75 percent this metal, while a 24-karat ring is pure.",
            "r": "Its atomic number is 79, between platinum and mercury. For 10 points, name this precious yellow metal."
        },
        {
            "p": "Large mines dissolve this metal out of crushed ore using a cyanide solution, while some small-scale miners use mercury, which grabs this metal to form an amalgam and pollutes rivers. This metal is about 19 times as dense as water.",
            "r": "Prospectors panned for it in California after 1848. For 10 points, name this precious metal, element number 79."
        },
        {
            "p": "Counterfeiters have hidden bars of tungsten inside fake bars of this metal, because the two metals have almost the same density. This metal’s price is usually quoted per troy ounce, which is about 31.1 grams.",
            "r": "Fort Knox in Kentucky stores much of the U.S. government’s supply of this metal. For 10 points, name this precious metal, element number 79."
        },
        {
            "p": "To win his freedom from Francisco Pizarro, the Inca ruler Atahualpa [“ah-tah-WAHL-pah”] promised to fill a room once with this metal and twice with silver. Spanish explorers also searched for El Dorado, a legendary ruler said to be covered in dust of this metal.",
            "r": "This element is number 79 on the periodic table. For 10 points, name this precious yellow metal."
        },
        {
            "p": "A discovery of this metal on the Witwatersrand [“WIT-wah-terz-rand”] in 1886 led to the founding of Johannesburg, South Africa. Ten years later, a find of this metal in Canada’s Yukon region set off the Klondike stampede.",
            "r": "James Marshall’s 1848 discovery of this metal at Sutter’s Mill drew the “forty-niners” to California. For 10 points, name this metal, element number 79."
        },
        {
            "p": "During his pilgrimage to Mecca in 1324, Mansa Musa of Mali gave away so much of this metal in Cairo that its value there fell for years. The funeral mask of the Egyptian pharaoh Tutankhamun [“too-tahn-KAH-mun”] is made mostly of this metal.",
            "r": "This metal does not rust or tarnish, so ancient objects made of it still shine. For 10 points, name this precious metal, element number 79."
        }
    ],
    "clues": [
        {
            "id": "symbol-aurum",
            "tier": "giveaway",
            "t": "Its chemical symbol comes from the Latin word aurum",
            "k": ["aurum", "latin"],
            "n": 0
        },
        {
            "id": "element-79",
            "tier": "giveaway",
            "t": "Element number 79, between platinum and mercury on the periodic table",
            "k": ["79", "platinum", "mercury"],
            "n": 0
        },
        {
            "id": "malleable",
            "tier": "giveaway",
            "t": "The most malleable metal: one gram can be hammered into a sheet about one square meter in size",
            "k": ["malleable", "square meter", "hammered"],
            "n": 0
        },
        {
            "id": "sutters-mill",
            "tier": "giveaway",
            "t": "James Marshall’s 1848 find at Sutter’s Mill drew the “forty-niners” to California",
            "k": ["sutter", "1848", "forty-niners", "marshall"],
            "n": 0,
            "rabbit": "California gold rush"
        },
        {
            "id": "midas",
            "tier": "giveaway",
            "t": "King Midas could turn whatever he touched into it",
            "k": ["midas", "touched"],
            "n": 0,
            "rabbit": "Midas"
        },
        {
            "id": "noble",
            "tier": "middle",
            "t": "A noble metal: it does not rust or tarnish, so ancient objects made of it still shine",
            "k": ["noble metal", "tarnish", "ancient"],
            "n": 0
        },
        {
            "id": "aqua-regia",
            "tier": "middle",
            "t": "Dissolves in aqua regia, a 1-to-3 mix of nitric and hydrochloric acids, but resists most other acids",
            "k": ["aqua regia", "nitric", "hydrochloric"],
            "n": 0,
            "rabbit": "Acids"
        },
        {
            "id": "karats",
            "tier": "middle",
            "t": "Purity is measured in karats: 24-karat is pure, and 18-karat is 75 percent",
            "k": ["karats", "24-karat", "18-karat"],
            "n": 0
        },
        {
            "id": "alloys",
            "tier": "middle",
            "t": "Mixed with copper it makes a “rose” alloy; mixed with nickel or palladium, a “white” alloy",
            "k": ["rose", "white", "alloy", "palladium"],
            "n": 0
        },
        {
            "id": "rutherford",
            "tier": "middle",
            "t": "Geiger and Marsden fired alpha particles at a thin foil of it (1909); Rutherford used the results to find the nucleus (1911)",
            "k": ["foil", "rutherford", "alpha particles", "nucleus"],
            "n": 0,
            "rabbit": "Scattering"
        },
        {
            "id": "dense",
            "tier": "middle",
            "t": "About 19 times as dense as water, so prospectors could pan for it in streams",
            "k": ["19 times", "dense", "pan"],
            "n": 0
        },
        {
            "id": "alchemy",
            "tier": "middle",
            "t": "Alchemists linked it with the Sun and sought a “philosopher’s stone” to turn lead into it",
            "k": ["alchemists", "philosopher’s stone", "lead"],
            "n": 0
        },
        {
            "id": "tutankhamun",
            "tier": "middle",
            "t": "The funeral mask of the pharaoh Tutankhamun is made mostly of it",
            "k": ["tutankhamun", "funeral mask"],
            "n": 0
        },
        {
            "id": "fort-knox",
            "tier": "middle",
            "t": "Fort Knox, Kentucky, stores much of the U.S. government’s supply",
            "k": ["fort knox", "kentucky"],
            "n": 0
        },
        {
            "id": "seaborg",
            "tier": "power",
            "t": "In 1980, Glenn Seaborg’s team turned several thousand atoms of bismuth into it with a particle accelerator",
            "k": ["seaborg", "bismuth", "1980"],
            "n": 0
        },
        {
            "id": "haber",
            "tier": "power",
            "t": "In the 1920s, Fritz Haber tried to extract it from seawater to help pay Germany’s World War I reparations",
            "k": ["haber", "seawater", "reparations"],
            "n": 0,
            "rabbit": "Haber process"
        },
        {
            "id": "de-hevesy",
            "tier": "power",
            "t": "In 1940, George de Hevesy dissolved two Nobel medals in aqua regia to hide them from the Nazis; the medals were later recast",
            "k": ["de hevesy", "nobel medals", "1940"],
            "n": 0,
            "rabbit": "Niels Bohr"
        },
        {
            "id": "lycurgus",
            "tier": "power",
            "t": "The Roman Lycurgus Cup, green in reflected light but red when lit from behind, holds tiny particles of it and silver",
            "k": ["lycurgus cup", "lycurgus", "reflected light"],
            "n": 0
        },
        {
            "id": "faraday-1857",
            "tier": "power",
            "t": "In 1857, Michael Faraday made a ruby-red liquid holding specks of it far too small to see",
            "k": ["faraday", "ruby-red", "1857"],
            "n": 0,
            "rabbit": "Michael Faraday"
        },
        {
            "id": "relativity",
            "tier": "power",
            "t": "Relativity helps explain its yellow color, since it absorbs blue light; sheets thin enough to see through let greenish-blue light pass",
            "k": ["relativity", "blue light", "greenish-blue"],
            "n": 0
        },
        {
            "id": "neutron-stars",
            "tier": "power",
            "t": "A 2017 neutron star collision showed signs that such crashes forge it; it has only one stable isotope, mass number 197",
            "k": ["neutron star", "2017", "stable isotope", "197"],
            "n": 0
        },
        {
            "id": "rapid-tests",
            "tier": "power",
            "t": "Its red-looking nanoparticles make the result line on many rapid tests; it coats electronic connectors because it does not corrode",
            "k": ["nanoparticles", "rapid tests", "connectors"],
            "n": 0
        },
        {
            "id": "jwst",
            "tier": "power",
            "t": "A thin layer of it coats the 18 mirror segments of the James Webb Space Telescope, reflecting infrared light, and spacesuit visors",
            "k": ["james webb", "infrared", "visors"],
            "n": 0
        },
        {
            "id": "cyanide",
            "tier": "power",
            "t": "Large mines dissolve it from crushed ore with cyanide; some small-scale miners use mercury to form an amalgam",
            "k": ["cyanide", "mercury", "amalgam"],
            "n": 0
        },
        {
            "id": "tungsten-troy",
            "tier": "power",
            "t": "Counterfeiters hide tungsten in fake bars because the two metals are nearly equally dense; its price is quoted per troy ounce (about 31.1 grams)",
            "k": ["tungsten", "troy ounce", "counterfeiters"],
            "n": 0
        },
        {
            "id": "atahualpa",
            "tier": "power",
            "t": "The Inca ruler Atahualpa promised Pizarro a room filled once with it and twice with silver; Spanish explorers sought El Dorado",
            "k": ["atahualpa", "pizarro", "el dorado"],
            "n": 0
        },
        {
            "id": "mansa-musa",
            "tier": "power",
            "t": "Mansa Musa of Mali gave away so much of it in Cairo on his 1324 pilgrimage to Mecca that its value there fell",
            "k": ["mansa musa", "cairo", "1324"],
            "n": 0
        },
        {
            "id": "witwatersrand",
            "tier": "power",
            "t": "A find on the Witwatersrand (1886) led to the founding of Johannesburg; a find in the Yukon (1896) set off the Klondike stampede",
            "k": ["witwatersrand", "johannesburg", "klondike"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Not fool’s gold",
        "body": "Pyrite, a shiny brass-colored compound of iron and sulfur, is nicknamed “fool’s gold,” and real answer lines do not accept it. Gold also shares its column of the periodic table with copper and silver, so clues about coins, jewelry, or precious metals can fit silver or platinum too. Saying “Au” is fine, but naming a compound like “gold chloride” is wrong when the question asks for the element.",
        "fix": "Atomic number 79, the Latin aurum, Sutter’s Mill, aqua regia, the most malleable metal, and Rutherford’s foil mean gold. Iron and sulfur, or crystals shaped like cubes, mean pyrite; atomic number 47, tarnishing, and the Latin argentum mean silver; atomic number 78 and catalytic converters mean platinum.",
        "line": "Real answer line: " + LINE
    },
    "tests": {
        "right": [
            "Gold",
            "AU",
            "element 79",
            "pure gold",
            "24-karat gold"
        ],
        "prompt": [],
        "wrong": [
            "Silver",
            "Pyrite",
            "Fool's gold",
            "Platinum",
            "California Gold Rush",
            "Copper",
            "Electrum",
            "Ag"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
