import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "lead-element",
    "name": "Lead (element)",
    "mono": "PB",
    "category": "Chemistry",
    "qbCategory": "Science · Chemistry",
    "kicker": "Element 82 · The soft, heavy metal of old pipes, paint, and batteries",
    "dates": "Used since ancient times",
    "briefing": "Lead is a soft, heavy, bluish-gray metal that people have used for thousands of years; the Romans made water pipes from it, and its Latin name, plumbum, gave us the word “plumbing.” Car batteries and the heavy aprons worn during X-rays still use it. Because lead is poisonous, especially to children, it was taken out of gasoline and house paint, and the “lead” in your pencil is really harmless graphite.",
    "answerHtml": "<b><u>Lead</u></b> (accept <u>Pb</u>)",
    "accept": [
        "lead",
        "pb",
        "lead element",
        "elemental lead",
        "lead metal"
    ],
    "prompt": [],
    "reject": [
        "graphite",
        "pencil lead",
        "plumbago",
        "tin",
        "mercury",
        "bismuth",
        "thallium",
        "uranium",
        "galena",
        "solder",
        "pewter",
        "lead poisoning",
        "tetraethyl lead",
        "tetraethyllead",
        "leaded gasoline",
        "lead paint",
        "lead oxide",
        "lead dioxide",
        "lead acetate",
        "lead sulfide",
        "lead carbonate",
        "lead iodide",
        "red lead",
        "white lead",
        "lead white",
        "lead acid battery",
        "lead crystal",
        "zinc",
        "silver",
        "copper",
        "nickel",
        "cadmium",
        "carbon",
        "germanium",
        "flerovium"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Lead",
    "qb": {
        "q": "lead",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "The inert pair effect explains why this element’s +2 oxidation state is far more stable than its +4 state, unlike the lighter members of its group. This element’s most common isotope has a “doubly magic” nucleus, because both its number of protons and its number of neutrons are magic numbers.",
            "r": "For 10 points, name this soft, heavy metal with atomic number 82, whose symbol comes from the Latin word plumbum."
        },
        {
            "p": "Clair Patterson measured isotopes of this element in meteorites to calculate in 1956 that Earth is about 4.55 billion years old. During that work, Patterson discovered how much of this element people had spread into the environment, and he spent years campaigning to get it out of gasoline.",
            "r": "Uranium slowly decays into this element. For 10 points, name this toxic metal with atomic number 82."
        },
        {
            "p": "Working for General Motors in 1921, Thomas Midgley Jr. found that a compound of this metal with four ethyl groups stopped car engines from “knocking.” The United States banned gasoline containing that compound for cars in 1996, because this metal is toxic.",
            "r": "This metal was also taken out of house paint. For 10 points, name this heavy metal with atomic number 82."
        },
        {
            "p": "Gaston Planté [“plahn-TAY”] invented the first rechargeable battery in 1859 using sheets of this metal in sulfuric acid. In a car battery, plates of this metal and of its dioxide both turn into this metal’s sulfate as the battery runs down.",
            "r": "Its main ore is the mineral galena. For 10 points, name this dense metal with atomic number 82."
        },
        {
            "p": "In 1746, John Roebuck began making sulfuric acid on a large scale inside huge chambers lined with sheets of this metal, which resists attack by that acid. Ancient Romans bent sheets of this soft metal into water pipes.",
            "r": "The word “plumbing” comes from this metal’s Latin name. For 10 points, name this heavy element with atomic number 82."
        },
        {
            "p": "Alchemists linked this metal with the planet Saturn, so poisoning by it was once called “saturnism.” For centuries, artists painted with a white pigment made from a carbonate of this metal, until safer titanium and zinc whites mostly replaced it.",
            "r": "This metal was banned from U.S. house paint in 1978. For 10 points, name this element with atomic number 82."
        },
        {
            "p": "Below about 7 kelvins, this metal becomes a superconductor that carries electric current with no resistance. Because it melts at only about 327 degrees Celsius, this soft, dense metal is easy to cast into fishing sinkers and the heavy weights in sailboat keels.",
            "r": "Aprons containing this metal protect patients during X-rays. For 10 points, name this element with atomic number 82."
        },
        {
            "p": "Ancient Athens paid for its warships with silver from the mines at Laurium, where the silver was separated from ores of this metal. Early “crystal radio” sets used a thin wire touching a cube-shaped crystal of galena, a sulfide of this metal.",
            "r": "For 10 points, name this toxic metal, whose chemical symbol comes from the Latin word plumbum."
        },
        {
            "p": "After Flint, Michigan, switched its water source in 2014 without treating the water to control corrosion, this metal began dissolving from old pipes into people’s tap water. Health agencies say there is no known safe level of this metal in a child’s blood.",
            "r": "For 10 points, name this toxic heavy metal, which was also removed from gasoline and house paint."
        },
        {
            "p": "The uranium-238 decay series ends with this element’s stable isotope of mass number 206, and the thorium-232 series ends with its isotope of mass number 208. Geologists measure uranium and this element in tiny zircon crystals to find the ages of ancient rocks.",
            "r": "This metal is used in car batteries. For 10 points, name this heavy metal with atomic number 82."
        },
        {
            "p": "Flerovium, element 114, sits directly below this element on the periodic table. Traditional solder for joining wires and pipes is an alloy of tin and this element, which sits just below tin in the carbon group.",
            "r": "For 10 points, name this soft, toxic metal that ancient Romans used to make water pipes."
        },
        {
            "p": "The word “miniature” comes from minium, a bright red oxide of this metal that medieval artists used to decorate handwritten books. That same red oxide was later painted onto iron and steel to keep them from rusting.",
            "r": "Its main ore is galena. For 10 points, name this heavy metal with atomic number 82."
        },
        {
            "p": "In the 1670s, George Ravenscroft developed a sparkling English glass that gets its brilliance from an oxide of this metal. Thick windows made of that same kind of glass let scientists safely watch radioactive materials.",
            "r": "Aprons containing this metal protect patients from X-rays. For 10 points, name this dense, poisonous element with atomic number 82."
        },
        {
            "p": "Graphite was once called plumbago because people mistook it for an ore of this metal. That old mistake is why the gray core of a pencil is still named after this metal, even though pencils contain none of it.",
            "r": "For 10 points, name this toxic heavy metal, whose chemical symbol comes from the Latin word plumbum."
        },
        {
            "p": "Mixing solutions of potassium iodide and a nitrate of this metal makes a bright yellow solid. When that solid dissolves in hot water and then cools, it forms glittering flakes nicknamed “golden rain.”",
            "r": "This metal sits just below tin in group 14. For 10 points, name this element with atomic number 82."
        }
    ],
    "clues": [
        {
            "id": "element-82",
            "tier": "giveaway",
            "t": "Element with atomic number 82; its symbol comes from the Latin word plumbum",
            "k": ["plumbum", "latin", "82"],
            "n": 0
        },
        {
            "id": "plumbing",
            "tier": "giveaway",
            "t": "Romans made water pipes from it, so the word “plumbing” comes from its Latin name",
            "k": ["plumbing", "water pipes", "romans"],
            "n": 0
        },
        {
            "id": "toxic",
            "tier": "giveaway",
            "t": "A toxic heavy metal that harms the brain and nervous system, especially in young children",
            "k": ["toxic", "heavy metal", "nervous system"],
            "n": 0
        },
        {
            "id": "paint-gasoline",
            "tier": "giveaway",
            "t": "In the U.S., it was banned from house paint in 1978 and from gasoline for cars in 1996",
            "k": ["house paint", "gasoline", "1978", "1996"],
            "n": 0
        },
        {
            "id": "pencil",
            "tier": "giveaway",
            "t": "The gray core of a pencil is named after it, but it is really graphite, a form of carbon",
            "k": ["graphite", "pencil"],
            "n": 0,
            "rabbit": "Carbon"
        },
        {
            "id": "car-battery",
            "tier": "middle",
            "t": "Car batteries use plates of it and its dioxide soaked in sulfuric acid",
            "k": ["car batteries", "sulfuric acid", "dioxide"],
            "n": 0,
            "rabbit": "Sulfuric acid"
        },
        {
            "id": "x-rays",
            "tier": "middle",
            "t": "So dense that it blocks radiation; aprons containing it protect patients during X-rays",
            "k": ["x-rays", "aprons", "radiation"],
            "n": 0
        },
        {
            "id": "galena",
            "tier": "middle",
            "t": "Its main ore is galena, a shiny, cube-shaped sulfide mineral",
            "k": ["galena", "sulfide"],
            "n": 0
        },
        {
            "id": "group-14",
            "tier": "middle",
            "t": "In group 14, the carbon group, just below tin; flerovium (element 114) sits below it",
            "k": ["group 14", "carbon group", "tin", "flerovium"],
            "n": 0
        },
        {
            "id": "solder-pewter",
            "tier": "middle",
            "t": "Traditional solder is an alloy of tin and this metal, and old pewter often contained it",
            "k": ["solder", "pewter", "alloy"],
            "n": 0
        },
        {
            "id": "soft-dense",
            "tier": "middle",
            "t": "Soft enough to scratch with a fingernail, very dense, and melts at only about 327 °C",
            "k": ["fingernail", "dense", "327"],
            "n": 0
        },
        {
            "id": "decay-series",
            "tier": "middle",
            "t": "The stable end product of the uranium and thorium radioactive decay series",
            "k": ["uranium", "thorium", "decay series"],
            "n": 0
        },
        {
            "id": "midgley",
            "tier": "middle",
            "t": "In 1921, Thomas Midgley Jr. found that a compound of it with four ethyl groups stopped engine “knocking” in gasoline",
            "k": ["midgley", "knocking", "ethyl", "1921"],
            "n": 0
        },
        {
            "id": "flint",
            "tier": "middle",
            "t": "In 2014, Flint, Michigan, switched water sources, and it dissolved from old pipes into tap water",
            "k": ["flint", "michigan", "2014"],
            "n": 0
        },
        {
            "id": "inert-pair",
            "tier": "power",
            "t": "The inert pair effect makes its +2 oxidation state more stable than its +4 state",
            "k": ["inert pair", "oxidation state"],
            "n": 0
        },
        {
            "id": "doubly-magic",
            "tier": "power",
            "t": "Its most common isotope, mass number 208, has a “doubly magic” nucleus; it is the heaviest element with stable isotopes",
            "k": ["doubly magic", "208", "stable isotopes"],
            "n": 0
        },
        {
            "id": "patterson",
            "tier": "power",
            "t": "Clair Patterson used its isotopes in meteorites to date Earth at about 4.55 billion years (1956), then fought to get it out of gasoline",
            "k": ["patterson", "meteorites", "4.55 billion"],
            "n": 0
        },
        {
            "id": "zircon",
            "tier": "power",
            "t": "Geologists date ancient rocks by measuring uranium and this metal in zircon crystals",
            "k": ["zircon", "ancient rocks"],
            "n": 0
        },
        {
            "id": "plante",
            "tier": "power",
            "t": "Gaston Planté invented the first rechargeable battery, using sheets of it, in 1859",
            "k": ["plante", "planté", "rechargeable", "1859"],
            "n": 0
        },
        {
            "id": "roebuck",
            "tier": "power",
            "t": "John Roebuck’s 1746 process made sulfuric acid in huge chambers lined with it",
            "k": ["roebuck", "chambers", "1746"],
            "n": 0
        },
        {
            "id": "saturn",
            "tier": "power",
            "t": "Alchemists linked it with the planet Saturn, so poisoning by it was called “saturnism”",
            "k": ["saturn", "saturnism", "alchemists"],
            "n": 0
        },
        {
            "id": "white-pigment",
            "tier": "power",
            "t": "For centuries, artists painted with a white pigment made from its carbonate",
            "k": ["white pigment", "carbonate", "artists"],
            "n": 0
        },
        {
            "id": "minium",
            "tier": "power",
            "t": "Minium, its bright red oxide, decorated medieval books (giving us “miniature”) and kept iron from rusting",
            "k": ["minium", "miniature", "red oxide"],
            "n": 0
        },
        {
            "id": "ravenscroft",
            "tier": "power",
            "t": "George Ravenscroft’s sparkling 1670s glass, known as crystal, gets its brilliance from its oxide",
            "k": ["ravenscroft", "crystal", "glass"],
            "n": 0
        },
        {
            "id": "plumbago",
            "tier": "power",
            "t": "Graphite was once called plumbago because people mistook it for an ore of this metal",
            "k": ["plumbago", "mistook"],
            "n": 0
        },
        {
            "id": "superconductor",
            "tier": "power",
            "t": "It becomes a superconductor below about 7 kelvins",
            "k": ["superconductor", "7 kelvins"],
            "n": 0
        },
        {
            "id": "golden-rain",
            "tier": "power",
            "t": "Its iodide is a bright yellow solid that recrystallizes from hot water into glittering “golden rain” flakes",
            "k": ["golden rain", "iodide", "yellow"],
            "n": 0
        },
        {
            "id": "laurium",
            "tier": "power",
            "t": "Galena crystals were detectors in early crystal radios; the silver from Athens’s Laurium mines came from its ores",
            "k": ["crystal radio", "laurium", "silver"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Not graphite, not tin",
        "body": "Pencil cores carry this element’s name, but they are really graphite, a form of carbon, so a tossup about pencils or plumbago may want graphite or carbon instead. Tin is the other trap: it sits just above this element in group 14, and the two metals were mixed together in solder and pewter. Mercury, another toxic heavy metal, also tempts early buzzers.",
        "fix": "Atomic number 82, plumbum, galena, car batteries, X-ray aprons, and old gasoline and paint point here. Tin is element 50 (its symbol, Sn, comes from stannum) and coats “tin cans”; mercury is the liquid metal in old thermometers.",
        "line": "Real answer line: <b><u>Lead</u></b> (accept <u>Pb</u>)"
    },
    "tests": {
        "right": [
            "Lead",
            "Pb",
            "LEAD",
            "Lead (element)",
            "lead metal",
            "Elemental lead"
        ],
        "prompt": [],
        "wrong": [
            "Graphite",
            "Tin",
            "Mercury",
            "Pencil lead",
            "Lead poisoning",
            "Bismuth",
            "Galena",
            "Lead paint"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
