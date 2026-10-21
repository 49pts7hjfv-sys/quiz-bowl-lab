import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "obsidian",
    "name": "Obsidian",
    "mono": "OBS",
    "category": "Earth Science",
    "qbCategory": "Science · Other Science (Earth Science)",
    "kicker": "Natural volcanic glass · Breaks into razor-sharp edges",
    "dates": "Named in Pliny the Elder’s _Natural History_, c. 77 CE",
    "briefing": "Obsidian is volcanic glass: lava, usually rich in silica, that cooled so quickly its atoms had no time to line up into crystals. It is usually shiny black, and it breaks with smooth, curved surfaces that leave edges sharper than a steel razor. Ancient peoples from Turkey to Mexico chipped it into arrowheads and knives, and some surgeons have even used obsidian scalpels.",
    "answerHtml": "<b><u>Obsidian</u></b> (prompt on volcanic glass, natural glass, or igneous rock; do not accept “pumice,” “basalt,” or “flint”)",
    "accept": [
        "obsidian",
        "obsidians",
        "obsidian glass",
        "obsidian rock",
        "snowflake obsidian",
        "mahogany obsidian",
        "rainbow obsidian",
        "volcanic obsidian"
    ],
    "prompt": [
        "volcanic glass",
        "natural glass",
        "glass",
        "igneous rock",
        "igneous rocks",
        "volcanic rock",
        "volcanic rocks",
        "extrusive rock",
        "extrusive igneous rock",
        "apache tears",
        "apache tear",
        "mineraloid"
    ],
    "reject": [
        "pumice",
        "basalt",
        "granite",
        "rhyolite",
        "andesite",
        "scoria",
        "tuff",
        "perlite",
        "flint",
        "chert",
        "quartz",
        "quartzite",
        "jet",
        "onyx",
        "jade",
        "tektite",
        "tektites",
        "fulgurite",
        "fulgurites",
        "peles hair",
        "peles tears",
        "magma",
        "lava"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Obsidian",
    "qb": {
        "q": "obsidian",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "In 1960, Irving Friedman and Robert Smith showed how to date artifacts made of this material by measuring the thin water-soaked layer, or hydration rind, that slowly grows on a freshly broken surface. Archaeologists can also trace where a piece came from by its chemical fingerprint.",
            "r": "This material forms when lava cools too quickly for crystals to grow. For 10 points, name this black volcanic glass."
        },
        {
            "p": "The Elizabethan scholar John Dee owned a polished “magic mirror” made of this material, which was brought to Europe from Mexico after the Spanish conquest and is kept in the British Museum. The Aztec god Tezcatlipoca [“tes-kaht-lee-POH-kah”], whose name means “smoking mirror,” was linked to mirrors of this material.",
            "r": "It breaks with a smooth, curved conchoidal fracture. For 10 points, name this natural volcanic glass that ancient peoples chipped into blades."
        },
        {
            "p": "Aztec warriors carried the macuahuitl [“mah-KWAH-weetl”], a flat wooden club edged with blades of this material, and the ancient city of Teotihuacan [“tay-oh-tee-wah-KAHN”] grew rich partly by working and trading green examples of it. Much of that green material came from the Sierra de las Navajas, or “Mountains of the Razors,” near Pachuca.",
            "r": "This material is a natural glass that forms when lava cools very quickly. For 10 points, name this rock that ancient peoples chipped into razor-sharp tools."
        },
        {
            "p": "A water-rich relative of this material, called perlite, puffs up like popcorn when heated and is mixed into potting soil. Rounded, dark lumps of this material called Apache tears are often found inside perlite.",
            "r": "This material forms when silica-rich lava cools too quickly to grow crystals. For 10 points, name this black volcanic glass."
        },
        {
            "p": "Over millions of years, this material slowly devitrifies, or begins to crystallize, which is why very old examples of it are rare. White, flower-like clusters of tiny crystals give its “snowflake” variety its spots.",
            "r": "This rock has no crystals at first because its lava cooled so fast. For 10 points, name this glassy igneous rock that ancient people made into arrowheads."
        },
        {
            "p": "Some surgeons have used scalpels made of this material, because a freshly broken edge of it can be just a few nanometers thick, far sharper than a steel blade. Even so, the material is brittle, and its edges chip easily.",
            "r": "Those edges come from its smooth, curved conchoidal fracture. For 10 points, name this black volcanic glass that ancient people chipped into knives and arrowheads."
        },
        {
            "p": "Pliny the Elder wrote that this material was named for a man called Obsius, who supposedly found it in Ethiopia. Its dark color usually comes from tiny specks of minerals such as magnetite, even though it is rich in pale silica.",
            "r": "For 10 points, name this natural glass that forms when lava cools too quickly for crystals to grow."
        },
        {
            "p": "Native peoples quarried this material at a cliff in Yellowstone National Park, and tools made from that cliff’s stone have been found at Hopewell sites as far away as Ohio. That cliff is named for this material.",
            "r": "This material breaks with a smooth, curved fracture into very sharp edges. For 10 points, name this black volcanic glass."
        },
        {
            "p": "Oregon’s Newberry Volcano poured out a huge flow of this material about 1,300 years ago, and visitors can hike a trail across its jagged surface. California’s Glass Mountain, near Medicine Lake Volcano, is another huge flow of it.",
            "r": "This material forms from silica-rich lava that cools too quickly to grow crystals. For 10 points, name this glassy, usually black igneous rock."
        },
        {
            "p": "Polished pieces of this material found at Çatalhöyük [“chah-TAHL-hoo-yook”], a Stone Age town in Turkey, are among the oldest known mirrors, made about 8,000 years ago. Traders carried this material across the ancient Near East from volcanoes in central Turkey.",
            "r": "It breaks with a curved, shell-like fracture. For 10 points, name this natural volcanic glass."
        },
        {
            "p": "Stone Age sailors crossed the Aegean Sea to collect this material on the Greek island of Melos, and more of it came from Lipari [“LEE-pah-ree”], a volcanic island north of Sicily. Its chemistry lets archaeologists tell which island each piece came from.",
            "r": "Toolmakers chipped this material into sharp blades and arrowheads. For 10 points, name this glassy volcanic rock."
        },
        {
            "p": "Because this material lacks an orderly arrangement of atoms, many geologists call it a mineraloid rather than a mineral. It usually has about the same silica-rich makeup as rhyolite and granite, and it rates about 5 to 5.5 on the Mohs hardness scale.",
            "r": "It breaks with a curved conchoidal fracture into razor-sharp edges. For 10 points, name this black volcanic glass."
        },
        {
            "p": "Flintknappers shape this material by pressure flaking, pressing small chips off its edge with the tip of a deer antler. Because it has no grain to follow, it breaks in smooth, predictable curves, letting skilled knappers control each flake.",
            "r": "Ancient peoples from Mexico to the Mediterranean made arrowheads and knives from it. For 10 points, name this black volcanic glass."
        },
        {
            "p": "Streaks of iron-bearing hematite give the “mahogany” variety of this material its reddish-brown color, while tiny aligned bubbles or crystals give its “sheen” varieties a golden or rainbow shimmer. Polished pieces of these varieties are sold as gemstones.",
            "r": "Ordinary examples of this material are shiny and black. For 10 points, name this natural glass formed when lava cools too fast to grow crystals."
        },
        {
            "p": "Modern surgeons have used blades of this material for very fine cuts, and Aztec warriors edged wooden clubs with it. It breaks with a smooth, curved, shell-like conchoidal fracture. Unlike frothy pumice, it is dense and has almost no gas bubbles.",
            "r": "This material forms when lava cools too fast for crystals to grow. For 10 points, name this black volcanic glass, prized for sharp arrowheads and blades."
        }
    ],
    "clues": [
        {
            "id": "volcanic-glass",
            "tier": "giveaway",
            "t": "Natural volcanic glass, usually shiny black",
            "k": ["volcanic glass", "shiny black"],
            "n": 0
        },
        {
            "id": "fast-cooling",
            "tier": "giveaway",
            "t": "Forms when lava cools so fast that no crystals can grow",
            "k": ["cools", "crystals", "lava"],
            "n": 0
        },
        {
            "id": "sharp-tools",
            "tier": "giveaway",
            "t": "Ancient peoples chipped it into razor-sharp arrowheads, knives, and blades",
            "k": ["arrowheads", "knives", "blades", "razor-sharp"],
            "n": 0
        },
        {
            "id": "extrusive",
            "tier": "giveaway",
            "t": "An extrusive igneous rock with a glassy texture",
            "k": ["extrusive", "igneous", "glassy"],
            "n": 0,
            "rabbit": "Igneous rocks"
        },
        {
            "id": "conchoidal",
            "tier": "middle",
            "t": "Breaks with a smooth, curved conchoidal (shell-like) fracture",
            "k": ["conchoidal", "shell-like", "fracture"],
            "n": 0,
            "rabbit": "Quartz"
        },
        {
            "id": "silica-magnetite",
            "tier": "middle",
            "t": "Usually silica-rich, like rhyolite and granite, but colored dark by tiny specks of magnetite",
            "k": ["silica", "rhyolite", "magnetite"],
            "n": 0
        },
        {
            "id": "scalpels",
            "tier": "middle",
            "t": "Freshly broken edges can be a few nanometers thick, so some surgeons have used it for scalpels",
            "k": ["scalpels", "surgeons", "nanometers"],
            "n": 0
        },
        {
            "id": "mineraloid",
            "tier": "middle",
            "t": "A mineraloid, not a true mineral, because its atoms are not orderly; hardness about 5 to 5.5",
            "k": ["mineraloid", "hardness"],
            "n": 0
        },
        {
            "id": "pumice",
            "tier": "middle",
            "t": "Pumice is a frothy, bubble-filled volcanic glass that floats; this rock is dense and smooth",
            "k": ["pumice", "bubble-filled", "floats"],
            "n": 0
        },
        {
            "id": "aztec",
            "tier": "middle",
            "t": "Aztec warriors edged the wooden macuahuitl with its blades; Teotihuacan traded green examples",
            "k": ["macuahuitl", "aztec", "teotihuacan"],
            "n": 0
        },
        {
            "id": "hydration-dating",
            "tier": "power",
            "t": "Hydration dating (Irving Friedman and Robert Smith, 1960) measures the water-soaked rind that grows on a broken surface",
            "k": ["hydration", "friedman", "1960"],
            "n": 0
        },
        {
            "id": "chemical-fingerprint",
            "tier": "power",
            "t": "Each source has a chemical fingerprint, so archaeologists can trace ancient trade routes",
            "k": ["chemical fingerprint", "trade routes"],
            "n": 0
        },
        {
            "id": "dee-mirror",
            "tier": "power",
            "t": "John Dee’s “magic mirror” in the British Museum is an Aztec mirror made of it",
            "k": ["john dee", "magic mirror", "british museum"],
            "n": 0
        },
        {
            "id": "tezcatlipoca",
            "tier": "power",
            "t": "Tezcatlipoca, the Aztec “Smoking Mirror” god, was linked to its mirrors",
            "k": ["tezcatlipoca", "smoking mirror"],
            "n": 0
        },
        {
            "id": "navajas",
            "tier": "power",
            "t": "Green examples came from the Sierra de las Navajas (“Mountains of the Razors”) near Pachuca",
            "k": ["sierra de las navajas", "pachuca", "razors"],
            "n": 0
        },
        {
            "id": "perlite-apache",
            "tier": "power",
            "t": "A water-rich relative is perlite, which puffs up when heated; rounded lumps inside perlite are Apache tears",
            "k": ["perlite", "apache tears"],
            "n": 0
        },
        {
            "id": "snowflake",
            "tier": "power",
            "t": "It slowly devitrifies (crystallizes), so very old examples are rare; white crystal clusters make the “snowflake” variety",
            "k": ["devitrifies", "snowflake"],
            "n": 0
        },
        {
            "id": "pliny",
            "tier": "power",
            "t": "Pliny the Elder said it was named for Obsius, who found it in Ethiopia",
            "k": ["pliny", "obsius", "ethiopia"],
            "n": 0
        },
        {
            "id": "yellowstone",
            "tier": "power",
            "t": "Native peoples quarried it at a Yellowstone cliff; tools from there reached Hopewell sites in Ohio",
            "k": ["yellowstone", "hopewell", "ohio"],
            "n": 0
        },
        {
            "id": "newberry",
            "tier": "power",
            "t": "Oregon’s Newberry Volcano erupted a huge flow of it about 1,300 years ago; California’s Glass Mountain is another",
            "k": ["newberry", "oregon", "glass mountain"],
            "n": 0
        },
        {
            "id": "catalhoyuk",
            "tier": "power",
            "t": "Polished pieces from Çatalhöyük, Turkey, about 8,000 years old, are among the oldest known mirrors",
            "k": ["çatalhöyük", "catalhoyuk", "turkey", "oldest known mirrors"],
            "n": 0
        },
        {
            "id": "melos-lipari",
            "tier": "power",
            "t": "Stone Age sailors traded it from the islands of Melos in Greece and Lipari near Sicily",
            "k": ["melos", "lipari", "sailors"],
            "n": 0
        },
        {
            "id": "knapping",
            "tier": "power",
            "t": "Flintknappers shape it by pressure flaking, pressing off chips with antler tips",
            "k": ["pressure flaking", "flintknappers", "antler"],
            "n": 0
        },
        {
            "id": "varieties",
            "tier": "power",
            "t": "“Mahogany” varieties get reddish-brown streaks from hematite; tiny bubbles or crystals give “sheen” varieties a shimmer",
            "k": ["mahogany", "hematite", "sheen"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Obsidian or pumice?",
        "body": "Pumice is volcanic glass too, often with the same silica-rich makeup, so clues about glass, silica, and lava cooling too fast for crystals fit both. Pumice is frothy, full of gas bubbles, and light enough to float, while obsidian is dense and smooth and breaks into sharp edges. Flint, a sedimentary rock that also chips into sharp tools, is another wrong answer.",
        "fix": "Sharp blades, arrowheads, mirrors, scalpels, and shiny black glass mean obsidian. Floating, frothy, and full of holes means pumice, and tools chipped from nodules found in chalk mean flint. Saying only “volcanic glass” earns a prompt, so be ready to name the rock.",
        "line": "Real answer line: <b><u>Obsidian</u></b> (prompt on volcanic glass; do not accept “pumice”)"
    },
    "tests": {
        "right": [
            "Obsidian",
            "obsidian glass",
            "Obsidain",
            "Snowflake obsidian",
            "Obsidion"
        ],
        "prompt": [
            "Volcanic glass",
            "Glass",
            "Igneous rock"
        ],
        "wrong": [
            "Pumice",
            "Basalt",
            "Flint",
            "Granite",
            "Quartz",
            "Perlite"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
