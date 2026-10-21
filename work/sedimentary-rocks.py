import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TIP = "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."

data = {
    "id": "sedimentary-rocks",
    "name": "Sedimentary rocks",
    "mono": "SED",
    "category": "Earth Science",
    "qbCategory": "Science · Other Science (Earth Science)",
    "kicker": "Rocks made of pressed, cemented layers of sediment · Hold nearly all fossils",
    "dates": "Form in layers over thousands to millions of years",
    "briefing": "Sedimentary rocks form when sand, mud, pebbles, and bits of shell settle in layers, get buried, and are pressed and cemented into stone. Sandstone, shale, limestone, and coal are all examples. Their stacked layers, called strata, read like pages in Earth’s history book, and they hold nearly all of the world’s fossils; most of the Grand Canyon’s colorful walls are a giant stack of them.",
    "answerHtml": "<b><u>Sedimentary</u></b> rocks (prompt on <u>clastic</u> rocks, <u>detrital</u> rocks, or <u>sediment</u>; do not accept “igneous rocks,” “metamorphic rocks,” or a single rock such as “shale” or “sandstone”)",
    "accept": [
        "sedimentary",
        "sedimentary rock",
        "sedimentary rocks",
        "sedimentary rock type",
        "sedimentary stone",
        "sedimentary stones",
        "sedimentary strata",
        "sedimentary layers",
        "sedimentary formations"
    ],
    "prompt": [
        "sediment",
        "sediments",
        "clastic rock",
        "clastic rocks",
        "detrital rock",
        "detrital rocks",
        "stratified rock",
        "stratified rocks",
        "layered rock",
        "layered rocks"
    ],
    "reject": [
        "igneous",
        "igneous rock",
        "igneous rocks",
        "metamorphic",
        "metamorphic rock",
        "metamorphic rocks",
        "volcanic rock",
        "volcanic rocks",
        "shale",
        "sandstone",
        "limestone",
        "conglomerate",
        "breccia",
        "siltstone",
        "mudstone",
        "chalk",
        "coal",
        "rock salt",
        "halite",
        "gypsum",
        "chert",
        "flint",
        "dolomite",
        "coquina",
        "evaporite",
        "evaporites",
        "fossil",
        "fossils",
        "rock cycle",
        "lithification",
        "sedimentation",
        "diagenesis",
        "magma",
        "lava",
        "marble",
        "slate",
        "quartzite",
        "granite",
        "basalt",
        "sand",
        "clay"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Sedimentary_rock",
    "qb": {"q": "sedimentary", "found": 0, "tip": TIP},
    "sample": {"n": 0, "note": "no real tossups checked yet"},
    "tossups": [
        {
            "p": "At Siccar Point, Scotland, James Hutton saw nearly vertical gray layers of these rocks topped by gently sloping red ones, and he realized the scene recorded an enormous span of time. Such buried erosion surfaces, called unconformities, mark places where layers of these rocks were worn away before new ones were laid down.",
            "r": "These rocks form from compacted and cemented layers of sediment. For 10 points, name this class of rocks that includes sandstone and shale."
        },
        {
            "p": "In 1815, William “Strata” Smith published the first geologic map of an entire country, England and Wales, after matching up layers of these rocks across long distances by the fossils they held. His principle of faunal succession says that fossils in these rocks appear in the same order wherever they are found.",
            "r": "Nearly all fossils are found in these rocks. For 10 points, name this rock type that forms when layers of sediment harden."
        },
        {
            "p": "Nicolas Steno, who showed that “tongue stones” found in rocks were really fossil shark teeth, stated in 1669 that in undisturbed layers of these rocks, the oldest layer lies at the bottom. That rule is called the law of superposition.",
            "r": "Steno also said that the layers of these rocks, called strata, start out flat. For 10 points, name this class of rocks that form from layers of sand, mud, and other sediment."
        },
        {
            "p": "Chester Wentworth’s 1922 scale sorts the grains in many of these rocks by size, from clay and silt up through sand, granules, pebbles, cobbles, and boulders. A kind of these rocks with rounded pebbles cemented together is called conglomerate, while one with sharp, angular pieces is called breccia [“BRETCH-ee-uh”].",
            "r": "Sandstone and shale are clastic kinds of these rocks. For 10 points, name this rock type made of compacted, cemented sediment."
        },
        {
            "p": "Geologists use the word diagenesis for the physical and chemical changes that turn loose grains into these rocks after the grains are laid down, short of the heat and pressure of metamorphism. During lithification, the grains of these rocks are squeezed together and glued by minerals like calcite and quartz.",
            "r": "These rocks form in layers called strata. For 10 points, name this rock type, which forms from compacted and cemented sediment."
        },
        {
            "p": "John Wesley Powell named the Great Unconformity, a gap of hundreds of millions of years where Cambrian layers of these rocks rest on far older rock. Above it, layer after layer of these rocks records shallow seas, rivers, and deserts that came and went over time.",
            "r": "Most of the Grand Canyon’s colorful walls are stacked layers of these rocks. For 10 points, name this rock type that holds most fossils."
        },
        {
            "p": "Varves are pairs of light and dark layers of these rocks laid down in lakes, with each pair marking a single year, so they can be counted like tree rings. Ripple marks and mud cracks preserved in these rocks show how water once moved and dried.",
            "r": "These rocks form in flat layers called strata. For 10 points, name this rock type that includes sandstone, shale, and limestone."
        },
        {
            "p": "Underwater avalanches of muddy water called turbidity currents leave behind turbidites, layers of these rocks in which coarse grains settle at the bottom and fine grains on top. In 1929, an earthquake off Newfoundland set off one such current that snapped undersea telegraph cables one after another.",
            "r": "These rocks are one of the three main rock types, along with igneous and metamorphic rocks. For 10 points, name this rock type that contains most fossils."
        },
        {
            "p": "Australia’s Uluru is made of arkose, a feldspar-rich variety of these rocks, and the nearby domes of Kata Tjuta are made of conglomerate. In Utah’s Zion National Park, giant slanting layers called cross-beds in these rocks preserve the shapes of ancient sand dunes.",
            "r": "Sandstone is a common example of these rocks. For 10 points, name this rock type, which also includes shale and limestone."
        },
        {
            "p": "The ancient city of Petra in Jordan was carved directly into cliffs of these rocks, and Utah’s Arches National Park holds more than 2,000 natural arches carved from them by erosion. Tiny spaces between the grains of these rocks often hold groundwater, oil, and natural gas.",
            "r": "These rocks form from compacted and cemented layers of sediment. For 10 points, name this rock class that includes sandstone."
        },
        {
            "p": "Chert and its dark variety, flint, are very hard kinds of these rocks made of microscopic quartz crystals, and early humans chipped them into sharp-edged tools. The White Cliffs of Dover are made of chalk, a soft kind of these rocks built from the shells of microscopic algae.",
            "r": "Nearly all fossils are found in these rocks. For 10 points, name this class of rocks that form in layers from sediment."
        },
        {
            "p": "Thick beds of salt and gypsum beneath the Mediterranean Sea show that it nearly dried up about 6 million years ago, in the Messinian salinity crisis. Such evaporites are chemical members of this rock class that form when salty water evaporates.",
            "r": "Coal is an organic member of this class, made from buried plant remains. For 10 points, name this class of rocks, which also includes sandstone and shale."
        },
        {
            "p": "Index fossils, like certain ammonites and trilobites, lived for short spans of time but spread widely, so geologists use them to match and date layers of these rocks on different continents. Steno’s principle of original horizontality says that the layers of these rocks are first laid down flat.",
            "r": "These rocks form in layers called strata. For 10 points, name this rock type in which nearly all fossils are found."
        },
        {
            "p": "Buried peat from ancient swamps is squeezed into lignite and then bituminous coal, an organic member of this rock class, while further heat and pressure turn it into metamorphic anthracite. Much of the world’s coal formed during the Carboniferous period, which is named for it.",
            "r": "Shale and sandstone are other members of this class. For 10 points, name this rock type formed from compacted, cemented sediment."
        },
        {
            "p": "In 2012, NASA’s Curiosity rover found rounded pebbles cemented into conglomerate on Mars, showing that a stream once flowed in Gale Crater. Later, the rover drilled into fine-grained mudstone of this rock class, which formed at the bottom of an ancient lake.",
            "r": "On Earth, these rocks include sandstone, shale, and limestone. For 10 points, name this rock class formed from layers of sediment."
        }
    ],
    "clues": [
        {"id": "definition", "tier": "giveaway",
         "t": "Rocks formed when layers of sediment, like sand, mud, and bits of shell, are buried, compacted, and cemented together",
         "k": ["compacted", "cemented", "sediment"], "n": 0},
        {"id": "three-types", "tier": "giveaway",
         "t": "One of the three main rock types, along with igneous and metamorphic rocks",
         "k": ["three main", "igneous", "metamorphic"], "n": 0, "rabbit": "Igneous rocks"},
        {"id": "examples", "tier": "giveaway",
         "t": "Examples include sandstone, shale, limestone, conglomerate, chalk, and coal",
         "k": ["sandstone", "shale", "limestone", "coal"], "n": 0, "rabbit": "Shale"},
        {"id": "fossils", "tier": "giveaway",
         "t": "Hold nearly all fossils, since they form gently at Earth’s surface without melting",
         "k": ["fossils", "nearly all"], "n": 0},
        {"id": "strata", "tier": "giveaway",
         "t": "Form in flat layers called strata, like most of the walls of the Grand Canyon",
         "k": ["strata", "grand canyon"], "n": 0},
        {"id": "lithification", "tier": "middle",
         "t": "Lithification turns sediment into stone by compaction (squeezing) and cementation (minerals like calcite and quartz gluing grains)",
         "k": ["lithification", "compaction", "cementation"], "n": 0},
        {"id": "superposition", "tier": "middle",
         "t": "Nicolas Steno’s law of superposition (1669): in undisturbed layers, the oldest is at the bottom and the youngest on top",
         "k": ["superposition", "steno", "1669"], "n": 0},
        {"id": "horizontality", "tier": "middle",
         "t": "Steno’s principle of original horizontality: layers start out flat, so tilted or folded layers were moved later",
         "k": ["original horizontality", "tilted"], "n": 0},
        {"id": "three-kinds", "tier": "middle",
         "t": "Three kinds: clastic (broken bits of rock), chemical (minerals left by water), and organic or biochemical (remains of living things)",
         "k": ["clastic", "chemical", "organic"], "n": 0},
        {"id": "conglomerate-breccia", "tier": "middle",
         "t": "Conglomerate is made of rounded pebbles cemented together; breccia has sharp, angular pieces",
         "k": ["conglomerate", "breccia", "angular"], "n": 0},
        {"id": "evaporites", "tier": "middle",
         "t": "Evaporites, like rock salt (halite) and gypsum, form when salty water evaporates",
         "k": ["evaporites", "rock salt", "gypsum"], "n": 0},
        {"id": "coal", "tier": "middle",
         "t": "Coal is an organic kind made from buried swamp plants; more heat and pressure turn it into metamorphic anthracite",
         "k": ["coal", "swamp", "anthracite"], "n": 0},
        {"id": "structures", "tier": "middle",
         "t": "Ripple marks, mud cracks, and cross-beds preserved in them show how ancient water and wind moved",
         "k": ["ripple marks", "mud cracks", "cross-beds"], "n": 0},
        {"id": "index-fossils", "tier": "middle",
         "t": "Index fossils, like certain ammonites and trilobites, help geologists match and date layers on different continents",
         "k": ["index fossils", "ammonites", "trilobites"], "n": 0},
        {"id": "porous", "tier": "middle",
         "t": "Tiny spaces between the grains of porous kinds, like sandstone, hold groundwater, oil, and natural gas",
         "k": ["porous", "groundwater", "natural gas"], "n": 0, "rabbit": "Aquifers"},
        {"id": "hutton-siccar", "tier": "power",
         "t": "At Siccar Point, Scotland (1788), James Hutton saw tilted gray layers under sloping red ones: an unconformity, a gap in the rock record",
         "k": ["siccar point", "hutton", "unconformity", "1788"], "n": 0},
        {"id": "william-smith", "tier": "power",
         "t": "William “Strata” Smith matched layers by their fossils (faunal succession) and made the first geologic map of a whole country, England and Wales (1815)",
         "k": ["william", "faunal succession", "geologic map", "1815"], "n": 0},
        {"id": "steno-teeth", "tier": "power",
         "t": "Nicolas Steno also showed that “tongue stones” found in rocks were fossil shark teeth",
         "k": ["tongue stones", "shark teeth"], "n": 0},
        {"id": "wentworth", "tier": "power",
         "t": "Chester Wentworth’s 1922 scale sorts grains by size: clay, silt, sand, granules, pebbles, cobbles, boulders",
         "k": ["wentworth", "1922", "cobbles"], "n": 0},
        {"id": "diagenesis", "tier": "power",
         "t": "Diagenesis: all the physical and chemical changes after sediment is laid down, short of metamorphism",
         "k": ["diagenesis", "metamorphism"], "n": 0},
        {"id": "great-unconformity", "tier": "power",
         "t": "John Wesley Powell named the Grand Canyon’s Great Unconformity, where Cambrian layers rest on far older rock",
         "k": ["great unconformity", "powell", "cambrian"], "n": 0, "rabbit": "Cambrian period"},
        {"id": "varves", "tier": "power",
         "t": "Varves are light-and-dark pairs of lake layers, one pair per year, counted like tree rings",
         "k": ["varves", "tree rings"], "n": 0},
        {"id": "turbidites", "tier": "power",
         "t": "Turbidity currents (underwater avalanches) leave graded beds called turbidites; one off Newfoundland in 1929 snapped undersea cables",
         "k": ["turbidites", "turbidity currents", "graded", "1929"], "n": 0},
        {"id": "uluru-zion", "tier": "power",
         "t": "Uluru is arkose, a feldspar-rich kind; Kata Tjuta is conglomerate; Zion’s cliffs show cross-beds of ancient sand dunes",
         "k": ["uluru", "arkose", "kata tjuta", "zion"], "n": 0},
        {"id": "petra-arches", "tier": "power",
         "t": "Jordan’s Petra was carved into cliffs of them, and Utah’s Arches National Park has more than 2,000 natural arches",
         "k": ["petra", "arches", "2,000"], "n": 0},
        {"id": "chert-flint", "tier": "power",
         "t": "Chert and flint are very hard kinds made of microscopic quartz crystals; early humans chipped them into tools",
         "k": ["chert", "flint", "tools"], "n": 0},
        {"id": "messinian", "tier": "power",
         "t": "Salt and gypsum beds under the Mediterranean show it nearly dried up about 6 million years ago (the Messinian salinity crisis)",
         "k": ["messinian", "mediterranean", "6 million"], "n": 0},
        {"id": "curiosity", "tier": "power",
         "t": "NASA’s Curiosity rover (2012) found conglomerate and lake-bottom mudstone in Mars’s Gale Crater",
         "k": ["curiosity", "gale crater", "mudstone"], "n": 0}
    ],
    "trap": {
        "title": "The class, not one rock",
        "body": "Tossups on sedimentary rocks are packed with examples like sandstone, shale, limestone, and coal, and with words like “fossils” and “strata,” which tempts players to buzz with one of them. The question wants the whole class of rocks. Igneous rocks (cooled from melted rock) and metamorphic rocks (changed by heat and pressure) are the other two classes, and they are wrong here.",
        "fix": "Listen for the noun: “this class of rocks” or “these rocks” means the category. Layers, cementing, sediment, fossils, and Steno’s law of superposition mean sedimentary; cooling magma or lava means igneous; heat and pressure without melting means metamorphic. Saying just “sediment” earns a prompt.",
        "line": "Real answer line: <b><u>Sedimentary</u></b> rocks (prompt on clastic rocks or sediment; do not accept “igneous rocks,” “metamorphic rocks,” or a single rock like “shale”)"
    },
    "tests": {
        "right": ["Sedimentary rocks", "sedimentary", "Sedimentary rock", "Sedimentry rocks", "Clastic sedimentary rocks"],
        "prompt": ["Sediment", "Clastic rocks"],
        "wrong": ["Igneous rocks", "Metamorphic rocks", "Shale", "Sandstone", "Limestone", "Fossils"]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
