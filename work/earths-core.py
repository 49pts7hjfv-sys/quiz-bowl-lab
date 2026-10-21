import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Prompts are matched only exactly (or by small typos), so list the common ways a kid types one part.
PARTS = []
for part in ("inner core", "outer core"):
    for pre in ("", "the ", "earths ", "earth ", "the earths "):
        PARTS.append(pre + part)
    PARTS += [part + " of the earth", part + " of earth", "the " + part + " of the earth"]
PARTS += [
    "solid inner core", "the solid inner core", "earths solid inner core",
    "liquid outer core", "the liquid outer core", "earths liquid outer core",
    "molten outer core", "the molten outer core", "earths molten outer core",
    "center of the earth", "the center of the earth", "center of earth", "earths center"
]

data = {
    "id": "earths-core",
    "name": "Earth’s core",
    "mono": "ECR",
    "category": "Earth Science",
    "qbCategory": "Science · Other Science (Earth Science)",
    "kicker": "Earth’s iron-and-nickel center · Its liquid outer part makes the magnetic field",
    "dates": "Begins about 2,900 km below the surface",
    "briefing": "Nearly 2,900 kilometers beneath your feet lies Earth’s core, a ball made mostly of iron and nickel. Its outer part is a churning layer of liquid metal that acts like a giant generator, making Earth’s magnetic field. Its inner part is roughly as hot as the surface of the Sun, yet crushing pressure keeps it solid. No one has ever been close: the deepest hole ever drilled reached only about 12 kilometers.",
    "answerHtml": "Earth’s <b><u>core</u></b> (prompt on <u>inner core</u> or <u>outer core</u>; do not accept “mantle” or “crust”)",
    "accept": [
        "earths core",
        "earth core",
        "core",
        "cores",
        "earths cores",
        "core of the earth",
        "core of earth",
        "planetary core",
        "iron core",
        "earths iron core",
        "iron nickel core",
        "metallic core",
        "metal core"
    ],
    "prompt": PARTS,
    "reject": [
        "mantle",
        "earths mantle",
        "upper mantle",
        "lower mantle",
        "crust",
        "earths crust",
        "lithosphere",
        "asthenosphere",
        "mesosphere",
        "gutenberg discontinuity",
        "lehmann discontinuity",
        "mohorovicic discontinuity",
        "moho",
        "magnetic field",
        "earths magnetic field",
        "geodynamo",
        "dynamo",
        "magnetosphere",
        "magma",
        "suns core",
        "solar core",
        "ice core",
        "ice cores",
        "core sample",
        "core samples",
        "apple core",
        "kola superdeep borehole",
        "iron ore",
        "ceres",
        "pope",
        "the pope"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Structure_of_Earth",
    "qb": {
        "q": "core",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "In 1936, Danish seismologist Inge Lehmann [“LAY-mun”] published a paper titled simply “P′” [“P-prime”], using faint earthquake waves that showed up where they were not expected to reveal that this region has a solid inner part.",
            "r": "For 10 points, name this central layer of Earth, beneath the mantle, made mostly of iron and nickel."
        },
        {
            "p": "In 1906, Richard Dixon Oldham used records of earthquake waves to argue that Earth has a dense central zone that slows some waves down, the first strong evidence for this region. Beno Gutenberg later figured out how deep it lies.",
            "r": "It begins about 2,900 kilometers below the surface. For 10 points, name this innermost layer of Earth, made mostly of iron and nickel."
        },
        {
            "p": "In 1926, Harold Jeffreys argued that the outer part of this region must be liquid. Shear waves, or S waves, cannot travel through liquids, which leaves an S-wave shadow zone on the far side of Earth from an earthquake.",
            "r": "For 10 points, name this innermost layer of Earth, whose solid inner part is surrounded by liquid metal."
        },
        {
            "p": "Geologists in the early 1900s nicknamed this region “Nife,” after the chemical symbols of its two main elements, just as they nicknamed the rocky layers above it “sial” and “sima” for their main elements.",
            "r": "Those two main elements are nickel and iron. For 10 points, name this innermost layer of Earth, found beneath the mantle."
        },
        {
            "p": "The Kola Superdeep Borehole in Russia, the deepest hole ever drilled, reached only about 12 kilometers down, a tiny fraction of the roughly 2,900 kilometers to the top of this region.",
            "r": "This region’s center is roughly as hot as the surface of the Sun. For 10 points, name this iron-and-nickel center of Earth."
        },
        {
            "p": "Earthquake waves travel slightly faster through the solid inner part of this region from north to south than they do parallel to the equator, a puzzle that seismologists are still studying. Some scientists think the metal crystals there tend to line up in one direction.",
            "r": "Enormous pressure keeps that inner part solid. For 10 points, name this iron-and-nickel center of Earth."
        },
        {
            "p": "This region is slightly less dense than pure iron and nickel would be, so scientists think lighter elements, perhaps sulfur, oxygen, or silicon, are mixed into it. Iron meteorites, thought to be chunks of the metal centers of shattered asteroids, give other clues to what it is made of.",
            "r": "Swirling liquid metal in its outer part produces Earth’s magnetic field. For 10 points, name this central layer of Earth, beneath the mantle."
        },
        {
            "p": "This region formed early in Earth’s history, when heavy molten iron sank toward the middle of the young planet while lighter rock rose above it, a sorting process called differentiation. Mercury has an unusually large version of this region for its size.",
            "r": "For 10 points, name this innermost part of Earth, which has a solid inner layer and a liquid outer layer."
        },
        {
            "p": "As Earth slowly cools, liquid metal in the outer part of this region freezes onto its solid inner part, so that inner part keeps growing. That freezing releases heat that helps keep the surrounding liquid churning.",
            "r": "That churning liquid makes Earth’s magnetic field. For 10 points, name this iron-and-nickel center of Earth."
        },
        {
            "p": "This region holds about a third of Earth’s mass while taking up only about a sixth of its volume, because its metal is so dense. Its radius is a little more than half of Earth’s radius.",
            "r": "For 10 points, name this innermost layer of Earth, made mostly of iron and nickel."
        },
        {
            "p": "P waves bend sharply as they enter this region, so seismographs about 104 to 140 degrees away from an earthquake pick up almost no direct P waves, a band called the P-wave shadow zone.",
            "r": "S waves cannot cross its liquid outer part at all. For 10 points, name this innermost layer of Earth, made of iron and nickel."
        },
        {
            "p": "In 1913, Beno Gutenberg calculated the depth of the boundary between this region and the mantle, about 2,900 kilometers down, a boundary now named for him. S waves from earthquakes cannot pass below that boundary.",
            "r": "For 10 points, name this innermost layer of Earth, where swirling molten iron produces Earth’s magnetic field."
        },
        {
            "p": "In 1995, Gary Glatzmaier and Paul Roberts built a computer model of churning liquid metal in the outer part of this region, and the magnetic field it produced flipped direction on its own.",
            "r": "That swirling metal acts like a giant electric generator, or geodynamo. For 10 points, name this innermost layer of Earth, made mostly of iron and nickel."
        },
        {
            "p": "Scientists recreate conditions inside this region by squeezing tiny samples of iron between the tips of two diamonds in devices called diamond anvil cells, then heating them with lasers to see when the iron melts.",
            "r": "Those experiments help estimate how hot this region is. For 10 points, name this innermost layer of Earth, made mostly of iron and nickel."
        },
        {
            "p": "The solid inner part of this region is about 1,220 kilometers in radius, roughly 70 percent of the Moon’s radius, and it sits inside a liquid outer layer more than 2,000 kilometers thick. Enormous pressure keeps that inner part solid.",
            "r": "Its center is roughly as hot as the surface of the Sun. For 10 points, name this central layer of Earth, made mostly of iron and nickel."
        }
    ],
    "clues": [
        {
            "id": "innermost",
            "tier": "giveaway",
            "t": "Earth’s innermost layer, at the center of the planet, beneath the mantle",
            "k": ["innermost layer", "center", "mantle"],
            "n": 0,
            "rabbit": "Mantle"
        },
        {
            "id": "iron-nickel",
            "tier": "giveaway",
            "t": "Made mostly of iron and nickel",
            "k": ["iron", "nickel"],
            "n": 0
        },
        {
            "id": "solid-liquid",
            "tier": "giveaway",
            "t": "Has a solid inner part and a liquid outer part",
            "k": ["solid inner part", "liquid outer part"],
            "n": 0
        },
        {
            "id": "magnetic-field",
            "tier": "giveaway",
            "t": "Swirling molten iron in its liquid outer part makes Earth’s magnetic field",
            "k": ["magnetic field", "molten iron"],
            "n": 0,
            "rabbit": "Earth’s magnetic field"
        },
        {
            "id": "hot-as-sun",
            "tier": "middle",
            "t": "Its center is roughly as hot as the surface of the Sun",
            "k": ["surface of the sun", "hot"],
            "n": 0
        },
        {
            "id": "pressure",
            "tier": "middle",
            "t": "Enormous pressure keeps its inner part solid despite the heat",
            "k": ["pressure", "solid"],
            "n": 0
        },
        {
            "id": "s-wave-shadow",
            "tier": "middle",
            "t": "S waves cannot pass through its liquid outer part, leaving an S-wave shadow zone",
            "k": ["s waves", "shadow zone"],
            "n": 0
        },
        {
            "id": "p-wave-shadow",
            "tier": "middle",
            "t": "P waves bend as they enter it, leaving a P-wave shadow zone about 104 to 140 degrees from an earthquake",
            "k": ["p waves", "104 to 140 degrees"],
            "n": 0
        },
        {
            "id": "gutenberg",
            "tier": "middle",
            "t": "The Gutenberg discontinuity, about 2,900 km down, marks its boundary with the mantle",
            "k": ["gutenberg discontinuity", "2,900 km"],
            "n": 0
        },
        {
            "id": "lehmann",
            "tier": "middle",
            "t": "Danish seismologist Inge Lehmann discovered its solid inner part in 1936",
            "k": ["inge lehmann", "1936", "danish"],
            "n": 0
        },
        {
            "id": "geodynamo",
            "tier": "middle",
            "t": "Its churning liquid metal acts like a giant electric generator, called the geodynamo",
            "k": ["geodynamo", "generator"],
            "n": 0
        },
        {
            "id": "volume-mass",
            "tier": "middle",
            "t": "About a sixth of Earth’s volume but about a third of its mass; its radius is a little more than half of Earth’s",
            "k": ["sixth", "third", "mass"],
            "n": 0
        },
        {
            "id": "differentiation",
            "tier": "middle",
            "t": "Formed early on as heavy molten iron sank to the middle of the young planet, a process called differentiation",
            "k": ["differentiation", "sank"],
            "n": 0
        },
        {
            "id": "oldham",
            "tier": "power",
            "t": "Richard Dixon Oldham used earthquake records to find the first strong evidence for it in 1906",
            "k": ["oldham", "1906"],
            "n": 0
        },
        {
            "id": "gutenberg-1913",
            "tier": "power",
            "t": "Beno Gutenberg calculated the depth of its boundary with the mantle in 1913",
            "k": ["beno gutenberg", "1913"],
            "n": 0
        },
        {
            "id": "jeffreys",
            "tier": "power",
            "t": "Harold Jeffreys argued in 1926 that its outer part is liquid",
            "k": ["jeffreys", "1926"],
            "n": 0
        },
        {
            "id": "p-prime",
            "tier": "power",
            "t": "Lehmann’s 1936 paper about its solid inner part was titled simply “P′” (P-prime)",
            "k": ["p-prime", "titled"],
            "n": 0
        },
        {
            "id": "nife",
            "tier": "power",
            "t": "Early 1900s geologists nicknamed it “Nife,” from the chemical symbols Ni and Fe",
            "k": ["nife", "ni and fe"],
            "n": 0
        },
        {
            "id": "light-elements",
            "tier": "power",
            "t": "It is a bit less dense than pure iron and nickel, so lighter elements, perhaps sulfur, oxygen, or silicon, are mixed in",
            "k": ["lighter elements", "less dense", "sulfur"],
            "n": 0
        },
        {
            "id": "meteorites",
            "tier": "power",
            "t": "Iron meteorites, thought to be chunks of shattered asteroids’ metal centers, hint at what it is made of",
            "k": ["iron meteorites", "asteroids"],
            "n": 0
        },
        {
            "id": "kola",
            "tier": "power",
            "t": "The Kola Superdeep Borehole, the deepest hole ever drilled, reached only about 12 km down",
            "k": ["kola superdeep borehole", "12 km"],
            "n": 0
        },
        {
            "id": "anisotropy",
            "tier": "power",
            "t": "Earthquake waves cross its solid inner part faster from north to south than parallel to the equator",
            "k": ["north to south", "faster", "equator"],
            "n": 0
        },
        {
            "id": "growing",
            "tier": "power",
            "t": "Its solid inner part grows as liquid metal freezes onto it, releasing heat that keeps the liquid churning",
            "k": ["grows", "freezes"],
            "n": 0
        },
        {
            "id": "glatzmaier",
            "tier": "power",
            "t": "In 1995, Gary Glatzmaier and Paul Roberts’s computer model of its churning metal made a magnetic field that flipped on its own",
            "k": ["glatzmaier", "roberts", "1995"],
            "n": 0
        },
        {
            "id": "anvil-cells",
            "tier": "power",
            "t": "Scientists squeeze iron between two diamond tips in anvil cells and heat it with lasers to recreate its conditions",
            "k": ["anvil cells", "lasers", "diamond"],
            "n": 0,
            "rabbit": "Diamond"
        },
        {
            "id": "mercury",
            "tier": "power",
            "t": "Mercury’s is unusually large for the size of the planet",
            "k": ["mercury", "unusually large"],
            "n": 0
        },
        {
            "id": "inner-size",
            "tier": "power",
            "t": "Its solid inner part is about 1,220 km in radius, roughly 70 percent of the Moon’s radius",
            "k": ["1,220 km", "70 percent"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Whole core, or one part?",
        "body": "Core tossups often describe just one part, like the solid inner core that Inge Lehmann found or the liquid outer core that makes the magnetic field, so players say “inner core” or “outer core” when the question wants the whole layer; that earns only a prompt. Boundary clues, like the Gutenberg discontinuity and the S-wave shadow zone, also tempt players to say “mantle,” the rocky layer just above.",
        "fix": "If the question says “this layer” or “this region” and its clues cover both parts, say “Earth’s core” or just “core.” If you get a prompt after “inner core,” say “core.” The Mohorovičić discontinuity is the crust–mantle boundary; the Gutenberg discontinuity is the mantle–core boundary.",
        "line": "Real answer line: Earth’s <b><u>core</u></b> (prompt on <u>inner core</u> or <u>outer core</u>; do not accept “mantle”)"
    },
    "tests": {
        "right": [
            "Earth's core",
            "core",
            "the core",
            "earths cor",
            "Core of the Earth",
            "iron core"
        ],
        "prompt": [
            "Inner core",
            "Outer core",
            "the inner core",
            "Earth's outer core"
        ],
        "wrong": [
            "Mantle",
            "Crust",
            "Earth's magnetic field",
            "Lower mantle",
            "Gutenberg discontinuity",
            "Sun's core"
        ]
    }
}

with open(ROOT / "topics" / "earths-core.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("wrote topics/earths-core.json")
