import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "basalt",
    "name": "Basalt",
    "mono": "BSL",
    "category": "Earth Science",
    "qbCategory": "Science · Other Science (Earth Science)",
    "kicker": "Dark, fine-grained volcanic rock · Makes up most of the ocean floor",
    "dates": "Forms constantly at mid-ocean ridges",
    "briefing": "Basalt is the dark, heavy rock that forms when runny lava cools quickly, too fast for big crystals to grow. It makes up most of the ocean floor, the islands of Hawaii and Iceland, and even the dark “seas” you can see on the Moon. When a thick flow cools slowly and evenly, it can crack into giant six-sided columns, like the roughly 40,000 columns of Northern Ireland’s Giant’s Causeway.",
    "answerHtml": "<b><u>Basalt</u></b> (accept <u>basaltic</u> rock or lava, <u>flood basalt</u>s, or <u>pillow basalt</u>s; prompt on <u>volcanic rock</u>, <u>igneous rock</u>, or <u>mafic rock</u>; do not accept “gabbro”)",
    "accept": [
        "basalt",
        "basalts",
        "basaltic",
        "basaltic rock",
        "basaltic rocks",
        "basaltic lava",
        "basalt lava",
        "flood basalt",
        "flood basalts",
        "pillow basalt",
        "pillow basalts",
        "columnar basalt",
        "olivine basalt",
        "mid ocean ridge basalt"
    ],
    "prompt": [
        "volcanic rock",
        "volcanic rocks",
        "igneous rock",
        "igneous rocks",
        "extrusive rock",
        "extrusive igneous rock",
        "mafic rock",
        "mafic igneous rock",
        "lava rock"
    ],
    "reject": [
        "gabbro",
        "granite",
        "andesite",
        "rhyolite",
        "dacite",
        "obsidian",
        "pumice",
        "scoria",
        "diabase",
        "dolerite",
        "tuff",
        "peridotite",
        "komatiite",
        "magma",
        "pyroxene",
        "plagioclase",
        "feldspar"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Basalt",
    "qb": {
        "q": "basalt",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "Followers of the German geologist Abraham Gottlob Werner, called Neptunists, wrongly argued that this rock had settled out of a vast ancient ocean. Other geologists showed that it actually forms from lava, partly by tracing its outcrops in France’s Auvergne [“oh-VAIRN”] region back to long-extinct volcanoes.",
            "r": "For 10 points, name this dark, fine-grained igneous rock that makes up most of the ocean floor."
        },
        {
            "p": "The word “trap” in the names of giant, step-like piles of this rock comes from a Swedish word for “stairs.” Eruptions that built the Siberian Traps from this rock are linked to the end-Permian mass extinction, and India’s Deccan Traps erupted around the time the dinosaurs disappeared.",
            "r": "For 10 points, name this dark volcanic rock that forms the six-sided columns of Northern Ireland’s Giant’s Causeway."
        },
        {
            "p": "Felix Mendelssohn wrote his overture _The Hebrides_ after visiting Fingal’s Cave, a sea cave on the Scottish island of Staffa that is lined with columns of this rock. Such columns form when a thick lava flow cools and shrinks, cracking into mostly six-sided pillars.",
            "r": "Similar columns make up Northern Ireland’s Giant’s Causeway. For 10 points, name this dark igneous rock that makes up most of the oceanic crust."
        },
        {
            "p": "Apollo astronauts brought back samples of this rock from the lunar maria [“MAR-ee-uh”], the dark plains that early astronomers thought were seas on the Moon. On Earth, it is the most common kind of volcanic rock, and Hawaii’s shield volcanoes erupt it as runny lava.",
            "r": "Its slowly cooled, coarse-grained cousin is called gabbro. For 10 points, name this dark, fine-grained rock that forms most of the ocean floor."
        },
        {
            "p": "A medium-grained rock with the same chemistry as this one, called diabase or dolerite, often forms the sheet-like intrusions called dikes and sills. This mafic rock is rich in magnesium and iron, which give it a dark color.",
            "r": "It is made mostly of pyroxene and plagioclase feldspar. For 10 points, name this fine-grained volcanic rock that forms the oceanic crust and Hawaii’s lava flows."
        },
        {
            "p": "When gas-bubble holes called vesicles in this rock are later filled in with minerals such as zeolites [“ZEE-uh-lites”], the filled pockets are called amygdules [“uh-MIG-dyoolz”]. Scoria, a very bubbly volcanic rock that builds many cinder cones, usually has this rock’s chemistry.",
            "r": "For 10 points, name this dark, fine-grained igneous rock whose slowly cooled, coarse-grained cousin is gabbro."
        },
        {
            "p": "In Irish legend, the giant Finn McCool built a path across the sea toward Scotland out of interlocking columns of this rock. Those mostly six-sided columns in County Antrim, numbering about 40,000, formed as a thick flow of lava slowly cooled, shrank, and cracked.",
            "r": "For 10 points, name this dark volcanic rock that forms the famous columns of Northern Ireland’s Giant’s Causeway."
        },
        {
            "p": "Millions of years ago, long cracks in the ground poured out lava that hardened into layer after layer of this rock across Washington, Oregon, and Idaho, forming the Columbia River Plateau. Such fissure eruptions can build huge regions of this rock called large igneous provinces.",
            "r": "Hawaii’s shield volcanoes also erupt it as runny lava. For 10 points, name this dark rock that makes up most of the ocean floor."
        },
        {
            "p": "Geologists use the abbreviation MORB for samples of this rock collected along mid-ocean ridges, where its lava erupts underwater and cools almost instantly into rounded “pillows.” Iceland, which sits on top of the Mid-Atlantic Ridge, is built mostly of this rock.",
            "r": "For 10 points, name this dark igneous rock that makes up most of the oceanic crust."
        },
        {
            "p": "Pyroxene and calcium-rich plagioclase, minerals that crystallize at high temperatures in Bowen’s reaction series, are the main ingredients of this rock. Because this rock’s lava is low in silica, it flows easily and usually erupts gently instead of exploding.",
            "r": "For 10 points, name this dark, fine-grained rock that builds Hawaii’s shield volcanoes and the ocean floor."
        },
        {
            "p": "Melted and spun into thin fibers, this rock is used to make fire-resistant rock wool insulation. Crushed pieces of this hard, heavy rock are commonly used to build roads and to hold railroad tracks in place.",
            "r": "Its coarse-grained equivalent is gabbro. For 10 points, name this extrusive igneous rock that forms Hawaii’s volcanoes and most of the ocean floor."
        },
        {
            "p": "Because this rock is denser than granite, oceanic crust made of it sinks beneath the lighter continents at subduction zones. New crust made of this rock forms constantly where tectonic plates pull apart along mid-ocean ridges.",
            "r": "For 10 points, name this dark, fine-grained igneous rock whose slowly cooled, coarse-grained cousin is gabbro."
        },
        {
            "p": "Soviet Venera landers found this rock on the surface of Venus, and it also covers much of Mars, where giant shield volcanoes like Olympus Mons erupted it as lava. On Earth, it erupts at hotspots like Hawaii and along the Mid-Atlantic Ridge.",
            "r": "For 10 points, name this dark volcanic rock that makes up most of the ocean floor."
        },
        {
            "p": "Smooth, ropy pahoehoe [“pa-HOH-ay-HOH-ay”] and rough, jagged a‘a [“AH-ah”] are the two main kinds of lava flows made of this rock, named with Hawaiian words. Hawaii’s Mauna Loa and Kilauea [“kee-luh-WAY-uh”] are broad shield volcanoes built from its runny lava.",
            "r": "For 10 points, name this dark, fine-grained volcanic rock that makes up most of the ocean floor."
        },
        {
            "p": "This rock’s crystals are usually too small to see without a magnifying glass, because its lava cools quickly at Earth’s surface. Geologists call it extrusive, while gabbro, which has the same minerals but cooled slowly underground, is called intrusive.",
            "r": "For 10 points, name this most common volcanic rock, a dark rock that forms the oceanic crust."
        }
    ],
    "clues": [
        {
            "id": "dark-fine-grained",
            "tier": "giveaway",
            "t": "A dark, fine-grained igneous rock that forms when runny lava cools quickly at Earth’s surface",
            "k": ["fine-grained", "dark", "cools quickly", "lava"],
            "n": 0
        },
        {
            "id": "ocean-floor",
            "tier": "giveaway",
            "t": "Makes up most of the oceanic crust, the rock of the ocean floor",
            "k": ["oceanic crust", "ocean floor"],
            "n": 0
        },
        {
            "id": "hawaii",
            "tier": "giveaway",
            "t": "Erupts as runny lava from Hawaii’s shield volcanoes, like Mauna Loa and Kilauea",
            "k": ["shield volcanoes", "hawaii", "mauna loa", "kilauea"],
            "n": 0,
            "rabbit": "Volcanoes"
        },
        {
            "id": "giants-causeway",
            "tier": "giveaway",
            "t": "Forms the roughly 40,000 mostly six-sided columns of Northern Ireland’s Giant’s Causeway",
            "k": ["giant’s causeway", "giants causeway", "six-sided", "columns"],
            "n": 0
        },
        {
            "id": "most-common",
            "tier": "giveaway",
            "t": "The most common volcanic rock on Earth",
            "k": ["most common", "volcanic rock"],
            "n": 0
        },
        {
            "id": "gabbro",
            "tier": "middle",
            "t": "Its coarse-grained cousin, gabbro, has the same minerals but cooled slowly underground",
            "k": ["gabbro", "coarse-grained", "underground"],
            "n": 0,
            "rabbit": "Igneous rocks"
        },
        {
            "id": "mafic",
            "tier": "middle",
            "t": "Mafic: rich in magnesium and iron and low in silica, which makes it dark and its lava runny",
            "k": ["mafic", "magnesium", "iron", "silica"],
            "n": 0
        },
        {
            "id": "minerals",
            "tier": "middle",
            "t": "Made mostly of pyroxene and calcium-rich plagioclase feldspar, sometimes with olivine",
            "k": ["pyroxene", "plagioclase", "olivine"],
            "n": 0,
            "rabbit": "Plagioclase"
        },
        {
            "id": "pillow-lava",
            "tier": "middle",
            "t": "Erupting underwater at mid-ocean ridges, its lava cools almost instantly into rounded “pillows”",
            "k": ["pillows", "pillow", "mid-ocean ridges", "underwater"],
            "n": 0,
            "rabbit": "Seafloor spreading"
        },
        {
            "id": "lunar-maria",
            "tier": "middle",
            "t": "The dark lunar maria (“seas”) of the Moon are plains of this rock, sampled by Apollo astronauts",
            "k": ["lunar maria", "maria", "apollo"],
            "n": 0
        },
        {
            "id": "columnar-jointing",
            "tier": "middle",
            "t": "A thick flow that cools and shrinks evenly can crack into six-sided columns, called columnar jointing",
            "k": ["columnar jointing", "six-sided", "shrinks"],
            "n": 0
        },
        {
            "id": "fingal",
            "tier": "middle",
            "t": "Fingal’s Cave on the Scottish island of Staffa, lined with its columns, inspired Felix Mendelssohn’s overture _The Hebrides_",
            "k": ["fingal’s cave", "fingal", "staffa", "mendelssohn", "hebrides"],
            "n": 0,
            "rabbit": "Felix Mendelssohn"
        },
        {
            "id": "iceland",
            "tier": "middle",
            "t": "Iceland, which sits on the Mid-Atlantic Ridge, is built mostly of this rock",
            "k": ["iceland", "mid-atlantic ridge"],
            "n": 0
        },
        {
            "id": "scoria-vesicles",
            "tier": "middle",
            "t": "Gas bubbles leave holes called vesicles; scoria, a very bubbly rock that builds cinder cones, usually has its chemistry",
            "k": ["vesicles", "scoria", "cinder cones"],
            "n": 0
        },
        {
            "id": "werner-neptunists",
            "tier": "power",
            "t": "Abraham Werner’s Neptunists wrongly said it settled out of an ancient ocean; outcrops in France’s Auvergne helped prove it volcanic",
            "k": ["werner", "neptunists", "auvergne"],
            "n": 0
        },
        {
            "id": "siberian-traps",
            "tier": "power",
            "t": "The Siberian Traps, huge stacked flows of it, are linked to the end-Permian extinction, the largest in Earth’s history",
            "k": ["siberian traps", "end-permian", "permian"],
            "n": 0
        },
        {
            "id": "deccan-traps",
            "tier": "power",
            "t": "India’s Deccan Traps erupted around the time the dinosaurs died out, about 66 million years ago",
            "k": ["deccan traps", "deccan", "india"],
            "n": 0
        },
        {
            "id": "trap-stairs",
            "tier": "power",
            "t": "“Trap” comes from a Swedish word for “stairs,” after the step-like look of its stacked flows",
            "k": ["swedish", "stairs", "step-like"],
            "n": 0
        },
        {
            "id": "columbia-river",
            "tier": "power",
            "t": "Fissure eruptions buried parts of Washington, Oregon, and Idaho under the Columbia River flows, a large igneous province",
            "k": ["columbia river", "large igneous province", "fissure"],
            "n": 0
        },
        {
            "id": "diabase",
            "tier": "power",
            "t": "Its medium-grained version, diabase (also called dolerite), often forms dikes and sills",
            "k": ["diabase", "dolerite", "dikes", "sills"],
            "n": 0
        },
        {
            "id": "morb",
            "tier": "power",
            "t": "Samples collected along mid-ocean ridges are abbreviated MORB",
            "k": ["morb"],
            "n": 0
        },
        {
            "id": "amygdules",
            "tier": "power",
            "t": "Vesicles later filled in with minerals like zeolites are called amygdules",
            "k": ["amygdules", "zeolites"],
            "n": 0
        },
        {
            "id": "finn-mccool",
            "tier": "power",
            "t": "Irish legend says the giant Finn McCool built the Giant’s Causeway as a path to Scotland",
            "k": ["finn mccool", "mccool", "legend"],
            "n": 0
        },
        {
            "id": "bowen",
            "tier": "power",
            "t": "Its main minerals crystallize at high temperatures in Bowen’s reaction series",
            "k": ["bowen’s reaction series", "bowens reaction series", "high temperatures"],
            "n": 0,
            "rabbit": "Bowen’s reaction series"
        },
        {
            "id": "venus-mars",
            "tier": "power",
            "t": "Soviet Venera landers found it on Venus, and it covers much of Mars, including giant shield volcanoes like Olympus Mons",
            "k": ["venera", "venus", "mars", "olympus mons"],
            "n": 0
        },
        {
            "id": "denser-than-granite",
            "tier": "power",
            "t": "Denser than granite, so oceanic crust made of it sinks beneath continents at subduction zones",
            "k": ["denser", "granite", "subduction"],
            "n": 0,
            "rabbit": "Subduction"
        },
        {
            "id": "rock-wool",
            "tier": "power",
            "t": "Melted and spun into fibers to make rock wool insulation; crushed for roads and railroad beds",
            "k": ["rock wool", "insulation", "railroad"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Basalt or gabbro?",
        "body": "Basalt and gabbro are made of the same minerals, so clues about pyroxene, plagioclase, or a mafic, iron-rich makeup fit both. The difference is where they cooled: basalt’s lava cooled fast at the surface, so its crystals are tiny, while gabbro’s magma cooled slowly underground into big crystals. Players also mix up basalt with granite, the light-colored, quartz-rich rock of the continents.",
        "fix": "Fine-grained, extrusive, lava, the ocean floor, Hawaii, pillows, or the Giant’s Causeway means basalt. Coarse-grained, intrusive, or “cooled slowly underground” means gabbro. Light-colored, quartz, and continental crust mean granite, and natural volcanic glass means obsidian.",
        "line": "Real answer line: <b><u>Basalt</u></b> (accept flood basalt or pillow basalt; prompt on volcanic rock or igneous rock; do not accept “gabbro”)"
    },
    "tests": {
        "right": [
            "Basalt",
            "basalts",
            "Bassalt",
            "Flood basalt",
            "basaltic lava"
        ],
        "prompt": [
            "Volcanic rock",
            "igneous rock"
        ],
        "wrong": [
            "Gabbro",
            "Granite",
            "Obsidian",
            "Pumice",
            "Andesite",
            "Diabase"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
