import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "bowens-reaction-series",
    "name": "Bowen’s reaction series",
    "mono": "BRS",
    "category": "Earth Science",
    "qbCategory": "Science · Other Science (Earth Science)",
    "kicker": "Order minerals crystallize from cooling magma · Olivine first, quartz last",
    "dates": "Worked out by Norman Bowen in the early 1900s",
    "briefing": "Bowen’s reaction series is the recipe for how cooling magma turns into rock. In the early 1900s, Canadian scientist Norman Bowen melted samples in a lab furnace and cooled them step by step, and he found that minerals crystallize in a set order: olivine first, at the hottest temperatures, and quartz last. His Y-shaped chart explains why dark basalt and pale granite are made of such different minerals.",
    "answerHtml": "<b><u>Bowen’s reaction series</u></b> (accept <u>Bowen’s series</u>; prompt on <u>reaction series</u>, <u>Bowen</u>, or one branch, like the <u>discontinuous series</u>; do not accept “Goldich dissolution series” or “fractional crystallization”)",
    "accept": [
        "bowens reaction series",
        "bowen reaction series",
        "bowens reaction",
        "bowen reaction",
        "bowens series",
        "bowen series",
        "bowens crystallization series",
        "bowen crystallization series"
    ],
    "prompt": [
        "reaction series",
        "bowen",
        "bowens",
        "norman bowen",
        "discontinuous series",
        "continuous series",
        "discontinuous branch",
        "continuous branch",
        "discontinuous reaction series",
        "continuous reaction series",
        "crystallization series"
    ],
    "reject": [
        "goldich dissolution series",
        "goldich series",
        "goldich",
        "dissolution series",
        "fractional crystallization",
        "magmatic differentiation",
        "differentiation",
        "crystal settling",
        "partial melting",
        "rock cycle",
        "igneous rocks",
        "igneous rock",
        "mohs hardness scale",
        "mohs scale",
        "bowen ratio",
        "olivine",
        "quartz",
        "plagioclase",
        "feldspar",
        "pyroxene",
        "amphibole",
        "biotite",
        "magma"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Bowen%27s_reaction_series",
    "qb": {
        "q": "Bowen's reaction series",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "Samuel Goldich showed that minerals break down at Earth’s surface in about the same order as this sequence, so the earliest minerals in it weather the fastest. This sequence’s continuous branch is made up of the plagioclase feldspars.",
            "r": "For 10 points, name this sequence that shows the order in which minerals crystallize from cooling magma."
        },
        {
            "p": "Plagioclase crystals with calcium-rich cores and sodium-rich rims, called zoned crystals, form when magma cools too quickly for them to finish reacting with the melt along one branch of this sequence. That branch is called continuous, because its crystal structure never changes.",
            "r": "For 10 points, name this sequence of minerals crystallizing from magma, from olivine to quartz."
        },
        {
            "p": "Olivine crystals wrapped in rims of pyroxene record a step in this sequence, in which an early mineral reacts with the leftover melt and starts turning into the next one. Minerals far apart in this sequence are rarely found together in the same rock.",
            "r": "For 10 points, name this sequence that shows the order in which minerals form as magma cools, ending with quartz."
        },
        {
            "p": "Going down one branch of this sequence, each mineral’s silicon–oxygen tetrahedra are linked more fully than in the mineral before it: first as separate units, then in single chains, then in double chains, and finally in sheets.",
            "r": "That discontinuous branch runs from olivine to biotite mica. For 10 points, name this sequence of minerals crystallizing from cooling magma."
        },
        {
            "p": "At the Carnegie Institution’s Geophysical Laboratory in Washington, D.C., this sequence’s namesake heated samples in a furnace, cooled them to set temperatures, and then quickly quenched them to see which crystals had formed at each step.",
            "r": "For 10 points, name this sequence, worked out by a Canadian scientist, that lists the order in which minerals crystallize from magma."
        },
        {
            "p": "Read in reverse, this sequence explains partial melting: when a rock is heated, the minerals at the bottom of this sequence melt first, so the first melt is richer in silica than the rock it came from.",
            "r": "Read forward, it begins with olivine. For 10 points, name this sequence that shows the order in which minerals crystallize from magma."
        },
        {
            "p": "One branch of this sequence starts with anorthite and ends with albite, because the same crystals slowly trade calcium for sodium as the magma around them cools. Those two minerals are the end members of the plagioclase feldspars.",
            "r": "For 10 points, name this sequence that shows which minerals crystallize first and last from cooling magma."
        },
        {
            "p": "Dense crystals that form early in this sequence, such as olivine, can sink to the floor of a magma chamber, a process called crystal settling. Removing those early crystals leaves the remaining melt richer in silica, in a process called fractional crystallization.",
            "r": "For 10 points, name this Y-shaped sequence of minerals that crystallize from magma, ending with quartz."
        },
        {
            "p": "Because the first and last minerals in this sequence form at such different temperatures, an igneous rock rarely contains both of them. Heated together, those two minerals react to make pyroxene, the mineral that comes second on one branch of this sequence.",
            "r": "For 10 points, name this sequence in which olivine crystallizes first and quartz crystallizes last from cooling magma."
        },
        {
            "p": "Minerals from the middle of this sequence, like hornblende and plagioclase containing both calcium and sodium, build intermediate rocks such as andesite and diorite. Minerals from the very top of this sequence build ultramafic rocks such as peridotite.",
            "r": "Its bottom minerals build light, felsic rocks like granite. For 10 points, name this sequence of crystallizing minerals."
        },
        {
            "p": "Augite crystallizes before hornblende on one branch of this sequence, where each mineral reacts with the surrounding liquid to become a mineral with a brand-new crystal structure. That branch is called discontinuous.",
            "r": "For 10 points, name this sequence, which begins with olivine and ends with quartz, showing how minerals crystallize from magma."
        },
        {
            "p": "This sequence was explained in the 1928 book _The Evolution of the Igneous Rocks_, whose author argued that removing early crystals from a basalt magma could leave behind a melt that would harden into granite-like rock.",
            "r": "For 10 points, name this sequence, named for a Canadian scientist, that lists the order in which minerals crystallize from magma."
        },
        {
            "p": "Biotite, a dark mica, is the last mineral on one branch of this sequence, while muscovite, a light mica, crystallizes after its two branches join. The place where those branches meet makes diagrams of this sequence look like a letter Y.",
            "r": "For 10 points, name this sequence of minerals that crystallize from cooling magma, starting with olivine and ending with quartz."
        },
        {
            "p": "The dark, ferromagnesian minerals on the left side of this sequence are rich in iron and magnesium, which is why the first rocks to form from a cooling basalt magma are dark. The right side of this sequence holds plagioclase feldspar.",
            "r": "For 10 points, name this Y-shaped sequence that shows the order in which minerals crystallize from cooling magma."
        },
        {
            "p": "This sequence explains why dark basalt is full of pyroxene and calcium-rich plagioclase, while pale granite is made mostly of potassium feldspar and quartz. It splits into discontinuous and continuous branches that come together near its low-temperature end.",
            "r": "For 10 points, name this sequence, worked out by a Canadian scientist, in which olivine crystallizes first and quartz last."
        }
    ],
    "clues": [
        {
            "id": "crystallize-order",
            "tier": "giveaway",
            "t": "The order in which minerals crystallize as magma cools, from the hottest temperatures down to the coolest",
            "k": ["crystallize", "magma cools", "order"],
            "n": 0
        },
        {
            "id": "olivine-quartz",
            "tier": "giveaway",
            "t": "Olivine crystallizes first, at the highest temperatures; quartz crystallizes last",
            "k": ["olivine", "quartz", "first", "last"],
            "n": 0,
            "rabbit": "Olivine"
        },
        {
            "id": "y-shape",
            "tier": "giveaway",
            "t": "Drawn like a letter Y: two branches at the top join into one line near the bottom",
            "k": ["letter y", "two branches", "join"],
            "n": 0
        },
        {
            "id": "canadian-lab",
            "tier": "giveaway",
            "t": "Worked out in the early 1900s by a Canadian scientist who melted and cooled samples in a laboratory",
            "k": ["canadian", "laboratory", "early 1900s"],
            "n": 0
        },
        {
            "id": "discontinuous",
            "tier": "middle",
            "t": "Discontinuous branch: olivine, then pyroxene, then amphibole, then biotite mica, each with a new crystal structure",
            "k": ["discontinuous", "pyroxene", "amphibole", "biotite"],
            "n": 0
        },
        {
            "id": "continuous",
            "tier": "middle",
            "t": "Continuous branch: plagioclase feldspar changes smoothly from calcium-rich to sodium-rich, keeping the same crystal structure",
            "k": ["continuous", "plagioclase", "calcium-rich", "sodium-rich"],
            "n": 0,
            "rabbit": "Plagioclase"
        },
        {
            "id": "bottom-three",
            "tier": "middle",
            "t": "After the branches join come potassium feldspar, then muscovite mica, then quartz, the main minerals of granite",
            "k": ["potassium feldspar", "muscovite", "granite"],
            "n": 0,
            "rabbit": "Granite"
        },
        {
            "id": "mafic-felsic",
            "tier": "middle",
            "t": "Minerals near the top build dark, mafic rocks like basalt; minerals near the bottom build light, felsic rocks like granite",
            "k": ["mafic", "felsic", "basalt"],
            "n": 0,
            "rabbit": "Basalt"
        },
        {
            "id": "fractional-crystallization",
            "tier": "middle",
            "t": "Fractional crystallization: when early crystals are removed, the leftover melt grows richer in silica",
            "k": ["fractional crystallization", "silica", "leftover melt"],
            "n": 0
        },
        {
            "id": "next-mineral",
            "tier": "middle",
            "t": "On the discontinuous branch, each mineral reacts with the surrounding melt and turns into the next mineral",
            "k": ["next mineral", "surrounding melt"],
            "n": 0
        },
        {
            "id": "ferromagnesian",
            "tier": "middle",
            "t": "Its left branch holds dark ferromagnesian minerals, which are rich in iron and magnesium",
            "k": ["ferromagnesian", "iron", "magnesium"],
            "n": 0
        },
        {
            "id": "goldich",
            "tier": "power",
            "t": "Samuel Goldich’s dissolution series: minerals that crystallize first, like olivine, also weather fastest, while quartz resists weathering best",
            "k": ["goldich", "dissolution series", "weather"],
            "n": 0,
            "rabbit": "Quartz"
        },
        {
            "id": "zoned-plagioclase",
            "tier": "power",
            "t": "Zoned plagioclase crystals have calcium-rich cores and sodium-rich rims, because they did not finish reacting with the melt",
            "k": ["zoned", "cores", "rims"],
            "n": 0
        },
        {
            "id": "pyroxene-rims",
            "tier": "power",
            "t": "Olivine crystals wrapped in rims of pyroxene show one mineral partway through turning into the next",
            "k": ["rims of pyroxene", "wrapped"],
            "n": 0
        },
        {
            "id": "tetrahedra",
            "tier": "power",
            "t": "Down the discontinuous branch, silicon–oxygen tetrahedra link more fully: separate units, single chains, double chains, then sheets",
            "k": ["tetrahedra", "single chains", "double chains", "sheets"],
            "n": 0
        },
        {
            "id": "quench",
            "tier": "power",
            "t": "Its namesake heated samples in a furnace, cooled them to set temperatures, and quenched them at the Carnegie Institution’s Geophysical Laboratory",
            "k": ["quenched", "geophysical laboratory", "carnegie"],
            "n": 0
        },
        {
            "id": "book-1928",
            "tier": "power",
            "t": "Explained in the 1928 book _The Evolution of the Igneous Rocks_, which argued that basalt magma could leave behind a granite-like melt",
            "k": ["evolution of the igneous rocks", "1928"],
            "n": 0,
            "rabbit": "Igneous rocks"
        },
        {
            "id": "partial-melting",
            "tier": "power",
            "t": "Read in reverse, it explains partial melting: minerals near the bottom melt first, so the first melt is rich in silica",
            "k": ["partial melting", "in reverse"],
            "n": 0
        },
        {
            "id": "anorthite-albite",
            "tier": "power",
            "t": "The continuous branch runs from calcium-rich anorthite down to sodium-rich albite",
            "k": ["anorthite", "albite"],
            "n": 0,
            "rabbit": "Feldspar"
        },
        {
            "id": "rarely-together",
            "tier": "power",
            "t": "Minerals far apart in it, like olivine and quartz, are rarely found together; heated together they react to make pyroxene",
            "k": ["rarely", "far apart"],
            "n": 0
        },
        {
            "id": "augite-hornblende",
            "tier": "power",
            "t": "Augite (a pyroxene) crystallizes before hornblende (an amphibole) on the discontinuous branch",
            "k": ["augite", "hornblende"],
            "n": 0
        },
        {
            "id": "crystal-settling",
            "tier": "power",
            "t": "Dense early crystals such as olivine can sink to the floor of a magma chamber, a process called crystal settling",
            "k": ["crystal settling", "magma chamber", "sink"],
            "n": 0
        },
        {
            "id": "intermediate-ultramafic",
            "tier": "power",
            "t": "Middle minerals build intermediate rocks like andesite and diorite; the very top minerals build ultramafic rocks like peridotite",
            "k": ["intermediate", "andesite", "diorite", "ultramafic", "peridotite"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Crystallizing, not weathering",
        "body": "The Goldich dissolution series lists almost the same minerals in almost the same order, with olivine at one end and quartz at the other, but it ranks how fast minerals weather at Earth’s surface, not how they crystallize from magma. Fractional crystallization is the process of removing early crystals, which this series helps explain, but it is a different answer. Players also hear “olivine” or “quartz” and blurt out a mineral instead of the whole series.",
        "fix": "Cooling magma, crystallizing, high and low temperatures, a Y-shaped chart, and continuous and discontinuous branches mean Bowen’s reaction series. Weathering, dissolving, and stability at Earth’s surface mean the Goldich dissolution series. Saying only “reaction series” earns a prompt.",
        "line": "Real answer line: <b><u>Bowen’s reaction series</u></b> (accept Bowen’s series; prompt on reaction series; do not accept “Goldich dissolution series”)"
    },
    "tests": {
        "right": [
            "Bowen’s reaction series",
            "Bowens reaction series",
            "Bowen reaction series",
            "Bowen's series",
            "Bowens reaction seires"
        ],
        "prompt": [
            "Reaction series",
            "Bowen",
            "Discontinuous series"
        ],
        "wrong": [
            "Goldich dissolution series",
            "Fractional crystallization",
            "Rock cycle",
            "Igneous rocks",
            "Mohs scale",
            "Bowen ratio"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
