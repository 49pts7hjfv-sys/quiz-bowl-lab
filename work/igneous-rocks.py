import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "igneous-rocks",
    "name": "Igneous rocks",
    "mono": "IGN",
    "category": "Earth Science",
    "qbCategory": "Science · Other Science (Earth Science)",
    "kicker": "Rocks formed from cooled magma or lava · One of the three main rock types",
    "dates": "Form whenever magma or lava cools and hardens",
    "briefing": "Igneous rocks are “fire-formed” rocks: their name comes from the Latin word for fire, because they harden from molten magma or lava. Magma that cools slowly underground grows big crystals, making coarse rocks like granite, while lava that cools fast at the surface keeps its crystals tiny, as in basalt, or freezes into glassy obsidian. Along with sedimentary and metamorphic rocks, they are one of the three main kinds of rock.",
    "answerHtml": "<b><u>Igneous rock</u></b>s (accept <u>intrusive</u> or <u>extrusive igneous rock</u>s or <u>magmatic rock</u>s; prompt on <u>volcanic rock</u>s, <u>plutonic rock</u>s, <u>intrusive rock</u>s, or <u>extrusive rock</u>s; do not accept “sedimentary rocks,” “metamorphic rocks,” “magma,” or “lava”)",
    "accept": [
        "igneous",
        "igneous rock",
        "igneous rocks",
        "magmatic rock",
        "magmatic rocks"
    ],
    "prompt": [
        "volcanic rock",
        "volcanic rocks",
        "plutonic rock",
        "plutonic rocks",
        "intrusive rock",
        "intrusive rocks",
        "extrusive rock",
        "extrusive rocks"
    ],
    "reject": [
        "sedimentary",
        "sedimentary rock",
        "sedimentary rocks",
        "metamorphic",
        "metamorphic rock",
        "metamorphic rocks",
        "magma",
        "lava",
        "basalt",
        "granite",
        "obsidian",
        "pumice",
        "gabbro",
        "rhyolite",
        "andesite",
        "diorite",
        "scoria",
        "tuff",
        "mineral",
        "minerals",
        "crystal",
        "crystals",
        "volcano",
        "volcanoes",
        "rock cycle",
        "bowens reaction series"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Igneous_rock",
    "qb": {
        "q": "igneous rocks",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "Norman Bowen’s reaction series lists the order in which minerals crystallize from the molten material that forms these rocks, starting with olivine and ending with quartz. Bowen worked out that order by melting and cooling rock samples in a laboratory.",
            "r": "These rocks are called extrusive if they cool quickly at the surface. For 10 points, name this class of rocks that form when magma or lava cools and hardens."
        },
        {
            "p": "Geologists classify coarse-grained examples of these rocks on a diamond-shaped QAPF diagram, devised by Albert Streckeisen, using their amounts of quartz, alkali feldspar, plagioclase, and minerals called feldspathoids. Examples very low in silica, like peridotite, are called ultramafic.",
            "r": "Light felsic examples like granite are rich in silica, unlike dark mafic ones like basalt. For 10 points, name these rocks that harden from magma or lava."
        },
        {
            "p": "Komatiites [“koh-MAH-tee-ites”], named for a river in South Africa, are rare, extremely hot examples of these rocks that erupted mostly early in Earth’s history. They often hold long, needle-like olivine crystals in a pattern called spinifex texture, named for a spiky Australian grass.",
            "r": "Obsidian is a glassy example of these rocks that cooled too fast to grow crystals. For 10 points, name these rocks that form when molten magma or lava solidifies."
        },
        {
            "p": "Peridotite, a green example of these rocks named for the gem peridot, is made mostly of olivine and makes up most of Earth’s upper mantle. Its makeup is called ultramafic, because it holds even less silica than mafic rocks do.",
            "r": "Dark, iron-rich examples of these rocks, like basalt and gabbro, are called mafic. For 10 points, name this rock type that forms when magma or lava cools."
        },
        {
            "p": "New Mexico’s Shiprock, a peak sacred to the Navajo people, is the eroded throat of an ancient volcano made of these rocks, with long, wall-like dikes radiating out from it. Those dikes formed when molten rock squeezed into cracks and hardened.",
            "r": "Sheets of these rocks that slip between rock layers are called sills. For 10 points, name these rocks, including granite and basalt, that form from cooled magma or lava."
        },
        {
            "p": "Wyoming’s Devils Tower, the first U.S. national monument and the alien landing site in the film _Close Encounters of the Third Kind_, is a giant mass of these rocks that cracked into tall columns. It was left standing after softer sedimentary rock around it wore away.",
            "r": "Similar columns of these rocks form Northern Ireland’s Giant’s Causeway. For 10 points, name this rock type that forms when magma or lava cools."
        },
        {
            "p": "After studying Utah’s Henry Mountains in the 1870s, Grove Karl Gilbert described laccoliths, mushroom-shaped masses of these rocks that bowed the layers above them up into domes. Gilbert showed that those masses had pushed in as molten rock between existing rock layers.",
            "r": "Much larger underground masses of these rocks, called batholiths, form the cores of ranges like the Sierra Nevada. For 10 points, name this class of rocks that form when magma or lava cools."
        },
        {
            "p": "Chunks of older rock that fell into molten material and got trapped as it hardened into these rocks are called xenoliths [“ZEN-uh-liths”], from Greek words meaning “foreign stones.” Such chunks must be older than the rock that surrounds them.",
            "r": "Magma that cools slowly underground into these rocks grows large crystals, as in granite. For 10 points, name this class of rocks that harden from magma or lava."
        },
        {
            "p": "These rocks are the best kind for radiometric dating, because the atomic “clocks” in their minerals start ticking when the molten material crystallizes. Dating layers of these rocks found above and below a fossil can bracket that fossil’s age.",
            "r": "They form one of the three main rock types, with sedimentary and metamorphic rocks. For 10 points, name this rock type named from the Latin word for “fire.”"
        },
        {
            "p": "James Hutton’s followers, called Plutonists, argued that rocks of this type formed from molten material deep inside Earth, rather than settling out of an ancient ocean as Abraham Werner’s Neptunists believed. Both Plutonism and some of these rocks are named for the Roman god of the underworld.",
            "r": "Examples of these rocks that cool slowly underground are called intrusive or plutonic. For 10 points, name this class of rocks that form from cooled magma or lava."
        },
        {
            "p": "The Moon’s bright highlands are made of anorthosite [“an-OR-thuh-site”], an example of these rocks that formed as an ocean of molten rock covering the young Moon cooled and its light crystals floated to the top. The dark lunar maria [“MAR-ee-uh”] are also made of these rocks.",
            "r": "Pumice, an example of these rocks full of gas bubbles, can float on water. For 10 points, name this class of rocks that form when magma or lava cools."
        },
        {
            "p": "Geologists call the texture of these rocks aphanitic [“af-uh-NIT-ik”] when their crystals are too small to see, phaneritic [“fan-uh-RIT-ik”] when the crystals are visible to the naked eye, and pegmatitic when the crystals are enormous. Those textures depend mostly on how fast the molten material cooled.",
            "r": "Examples with big crystals scattered in a fine background are called porphyritic. For 10 points, name this rock type that forms when magma or lava cools and hardens."
        },
        {
            "p": "The Siberian Traps, a giant staircase of these rocks built by enormous floods of molten rock, are linked to the end-Permian mass extinction about 252 million years ago. India’s Deccan Traps, another huge pile of these rocks, formed around the time the dinosaurs died out.",
            "r": "Quickly cooled, extrusive examples of these rocks have tiny crystals. For 10 points, name these rocks, such as basalt and granite, that form from cooled magma or lava."
        },
        {
            "p": "Diamonds reach Earth’s surface inside kimberlite, an example of these rocks that blasted up through narrow, carrot-shaped pipes from deep in the mantle. South Africa’s “Big Hole” at Kimberley was dug largely by hand to mine one of those pipes.",
            "r": "Gas bubbles called vesicles fill some of these rocks, like pumice and scoria. For 10 points, name this class of rocks that form when magma or lava cools."
        },
        {
            "p": "A porphyritic [“por-fuh-RIT-ik”] example of these rocks has large crystals called phenocrysts [“FEE-nuh-krists”] scattered through a fine-grained background, a sign that its molten material began cooling slowly underground, growing big crystals, and then finished cooling quickly at the surface.",
            "r": "Obsidian is a glassy example of these rocks. For 10 points, name this rock type, one of the three main types along with sedimentary and metamorphic rocks."
        }
    ],
    "clues": [
        {
            "id": "cooled-magma",
            "tier": "giveaway",
            "t": "Rocks that form when molten magma or lava cools and hardens",
            "k": ["magma", "lava", "hardens"],
            "n": 0,
            "rabbit": "Magma"
        },
        {
            "id": "latin-fire",
            "tier": "giveaway",
            "t": "Their name comes from the Latin word ignis, meaning “fire”",
            "k": ["ignis", "fire", "latin"],
            "n": 0
        },
        {
            "id": "three-types",
            "tier": "giveaway",
            "t": "One of the three main rock types in the rock cycle, along with sedimentary and metamorphic rocks",
            "k": ["sedimentary", "metamorphic", "rock cycle"],
            "n": 0,
            "rabbit": "Sedimentary rocks"
        },
        {
            "id": "examples",
            "tier": "giveaway",
            "t": "Examples include granite, basalt, obsidian, and pumice",
            "k": ["granite", "basalt", "obsidian", "pumice"],
            "n": 0,
            "rabbit": "Granite"
        },
        {
            "id": "intrusive-extrusive",
            "tier": "middle",
            "t": "Intrusive (plutonic) kinds cool slowly underground; extrusive (volcanic) kinds cool quickly at the surface",
            "k": ["intrusive", "extrusive", "plutonic", "volcanic"],
            "n": 0
        },
        {
            "id": "crystal-size",
            "tier": "middle",
            "t": "Slow cooling grows big crystals, as in coarse-grained granite; fast cooling leaves tiny crystals, as in fine-grained basalt",
            "k": ["coarse-grained", "fine-grained", "crystals"],
            "n": 0,
            "rabbit": "Basalt"
        },
        {
            "id": "obsidian-glass",
            "tier": "middle",
            "t": "Obsidian is natural volcanic glass that cooled too fast to grow any crystals",
            "k": ["obsidian", "volcanic glass", "too fast"],
            "n": 0,
            "rabbit": "Obsidian"
        },
        {
            "id": "vesicles-pumice",
            "tier": "middle",
            "t": "Gas bubbles leave holes called vesicles, as in scoria; bubbly pumice can even float on water",
            "k": ["vesicles", "pumice", "float"],
            "n": 0
        },
        {
            "id": "felsic-mafic",
            "tier": "middle",
            "t": "Sorted by silica: light felsic kinds like granite are silica-rich, while dark mafic kinds like basalt and gabbro are rich in magnesium and iron",
            "k": ["felsic", "mafic", "silica"],
            "n": 0
        },
        {
            "id": "pluto-name",
            "tier": "middle",
            "t": "“Plutonic” kinds are named for Pluto, the Roman god of the underworld",
            "k": ["pluto", "underworld"],
            "n": 0
        },
        {
            "id": "dikes-sills",
            "tier": "middle",
            "t": "Molten rock squeezed into cracks hardens into dikes, which cut across rock layers, and sills, which slip between them",
            "k": ["dikes", "sills"],
            "n": 0
        },
        {
            "id": "porphyritic",
            "tier": "middle",
            "t": "Porphyritic kinds have large crystals (phenocrysts) in a fine background, a sign they cooled in two stages",
            "k": ["porphyritic", "phenocrysts", "two stages"],
            "n": 0
        },
        {
            "id": "columnar-jointing",
            "tier": "middle",
            "t": "Thick masses that cool and shrink can crack into tall columns, as at Northern Ireland’s Giant’s Causeway",
            "k": ["columns", "giant’s causeway", "giants causeway", "shrink"],
            "n": 0
        },
        {
            "id": "batholiths",
            "tier": "middle",
            "t": "Huge underground masses called batholiths form the cores of mountain ranges like the Sierra Nevada",
            "k": ["batholiths", "sierra nevada"],
            "n": 0
        },
        {
            "id": "bowen",
            "tier": "power",
            "t": "Norman Bowen’s reaction series gives the order in which minerals crystallize from cooling magma, from olivine first to quartz last",
            "k": ["norman bowen", "reaction series", "olivine"],
            "n": 0,
            "rabbit": "Bowen’s reaction series"
        },
        {
            "id": "qapf",
            "tier": "power",
            "t": "Coarse-grained kinds are classified on Albert Streckeisen’s diamond-shaped QAPF diagram by quartz, alkali feldspar, plagioclase, and feldspathoids",
            "k": ["qapf", "streckeisen", "feldspathoids"],
            "n": 0
        },
        {
            "id": "komatiites",
            "tier": "power",
            "t": "Komatiites, extremely hot ultramafic lavas from early in Earth’s history, are named for a South African river and show needle-like spinifex texture",
            "k": ["komatiites", "spinifex", "ultramafic"],
            "n": 0
        },
        {
            "id": "peridotite",
            "tier": "power",
            "t": "Peridotite, a green, olivine-rich kind named for the gem peridot, makes up most of the upper mantle",
            "k": ["peridotite", "peridot", "upper mantle"],
            "n": 0,
            "rabbit": "Olivine"
        },
        {
            "id": "kimberlite",
            "tier": "power",
            "t": "Diamonds ride up from the mantle inside kimberlite, which fills carrot-shaped pipes like the one dug out at Kimberley’s “Big Hole”",
            "k": ["kimberlite", "diamonds", "big hole"],
            "n": 0,
            "rabbit": "Diamond"
        },
        {
            "id": "shiprock",
            "tier": "power",
            "t": "New Mexico’s Shiprock, sacred to the Navajo, is an ancient volcano’s eroded throat with dikes radiating from it",
            "k": ["shiprock", "navajo", "radiating"],
            "n": 0
        },
        {
            "id": "devils-tower",
            "tier": "power",
            "t": "Wyoming’s Devils Tower, the first U.S. national monument, is a columned mass left standing after softer rock eroded",
            "k": ["devils tower", "wyoming", "national monument"],
            "n": 0
        },
        {
            "id": "gilbert-laccoliths",
            "tier": "power",
            "t": "G. K. Gilbert described mushroom-shaped laccoliths, which dome up the layers above them, in Utah’s Henry Mountains",
            "k": ["laccoliths", "gilbert", "henry mountains"],
            "n": 0
        },
        {
            "id": "xenoliths",
            "tier": "power",
            "t": "Trapped chunks of older rock are called xenoliths, Greek for “foreign stones,” and must be older than the rock around them",
            "k": ["xenoliths", "foreign stones"],
            "n": 0
        },
        {
            "id": "radiometric",
            "tier": "power",
            "t": "Best for radiometric dating, since their minerals’ atomic “clocks” start when they crystallize; layers of them can bracket a fossil’s age",
            "k": ["radiometric dating", "clocks", "fossil"],
            "n": 0
        },
        {
            "id": "hutton-plutonists",
            "tier": "power",
            "t": "James Hutton’s Plutonists said they formed from molten rock, against Abraham Werner’s Neptunists, who said they settled out of an ocean",
            "k": ["plutonists", "hutton", "neptunists"],
            "n": 0
        },
        {
            "id": "moon",
            "tier": "power",
            "t": "The Moon’s bright highlands are anorthosite, formed as an ancient ocean of molten rock cooled; its dark maria are this kind of rock too",
            "k": ["anorthosite", "highlands", "maria"],
            "n": 0
        },
        {
            "id": "textures",
            "tier": "power",
            "t": "Textures with crystals too small to see are aphanitic, visible ones phaneritic, and giant ones pegmatitic",
            "k": ["aphanitic", "phaneritic", "pegmatitic"],
            "n": 0
        },
        {
            "id": "siberian-traps",
            "tier": "power",
            "t": "The Siberian Traps, a vast pile of flood lava, are linked to the end-Permian extinction; India’s Deccan Traps formed around when the dinosaurs died out",
            "k": ["siberian traps", "deccan traps", "end-permian"],
            "n": 0
        }
    ],
    "trap": {
        "title": "The class, not one rock",
        "body": "Igneous-rock tossups are packed with examples like granite, basalt, obsidian, and pumice, and with the words magma and lava, which tempts players to buzz with one of them. The question wants the whole class of rocks. The other two classes trip players up too: sedimentary rocks form from pressed-together sediment, and metamorphic rocks are changed by heat and pressure without melting.",
        "fix": "Listen for “this class of rocks” or “these rocks.” Molten material, crystal size, plutonic, or volcanic means igneous; layers, fossils, and cementing mean sedimentary; squeezing, banding, and heat without melting mean metamorphic. Saying “volcanic rocks” or “plutonic rocks” earns only a prompt.",
        "line": "Real answer line: <b><u>Igneous rock</u></b>s (prompt on volcanic rocks or plutonic rocks; do not accept “sedimentary rocks,” “metamorphic rocks,” “magma,” or “lava”)"
    },
    "tests": {
        "right": ["Igneous rocks", "igneous", "Ingneous rock", "extrusive igneous rock", "Igneus rocks"],
        "prompt": ["Volcanic rocks", "plutonic rock"],
        "wrong": ["Sedimentary rocks", "Metamorphic rocks", "Magma", "Basalt", "Granite", "Obsidian"]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
