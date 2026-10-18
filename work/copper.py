import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "copper",
    "name": "Copper",
    "mono": "CU",
    "category": "Chemistry",
    "qbCategory": "Science · Chemistry",
    "kicker": "Element 29 · The reddish metal in wires, pennies, and the Statue of Liberty",
    "dates": "Used since prehistoric times",
    "briefing": "Copper is the reddish-orange metal in electrical wires, water pipes, and the coating on pennies, and it carries electricity better than any metal except silver. Mixing it with tin made bronze, the alloy that gave the Bronze Age its name, and the Statue of Liberty’s copper skin slowly turned green as it reacted with the air. Its symbol, Cu, comes from the Latin word cuprum, named for the island of Cyprus and its ancient mines.",
    "answerHtml": "<b><u>Copper</u></b> (accept <u>Cu</u>)",
    "accept": [
        "copper",
        "cu"
    ],
    "prompt": [],
    "reject": [
        "bronze",
        "brass",
        "tin",
        "zinc",
        "silver",
        "gold",
        "nickel",
        "iron",
        "cobalt",
        "aluminum",
        "copper sulfate",
        "copper ii sulfate",
        "copper oxide",
        "copper ii oxide",
        "copper i oxide",
        "copper carbonate",
        "copper chloride",
        "copper age",
        "cupronickel",
        "verdigris",
        "patina",
        "malachite",
        "azurite",
        "chalcopyrite",
        "cuprite",
        "cuprates",
        "hemocyanin"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Copper",
    "qb": {
        "q": "copper",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "Like chromium, this element breaks the usual filling order: its electron configuration ends in 3d10 4s1 instead of 3d9 4s2, because a completely full d subshell is extra stable. This element sits just above silver and gold in group 11.",
            "r": "Its plus-one and plus-two ions are called cuprous and cupric. For 10 points, name this element with atomic number 29."
        },
        {
            "p": "In Benedict’s test, sugars such as glucose turn this element’s blue plus-two ions into a brick-red oxide. The biuret test for proteins uses a blue sulfate of this element, which turns violet when proteins are present.",
            "r": "Mixed with tin, this metal makes bronze. For 10 points, name this reddish metal with atomic number 29."
        },
        {
            "p": "Bordeaux [“bor-DOH”] mixture, a fungicide sprayed on grapevines since the 1880s, combines lime with this element’s sulfate. That sulfate forms bright blue crystals, which turn white when heated because they lose their water.",
            "r": "For 10 points, name this element, which is mixed with zinc to make brass and with tin to make bronze."
        },
        {
            "p": "In a Daniell cell, a zinc electrode in zinc sulfate solution is connected to an electrode of this metal standing in a solution of its own sulfate. This metal and its group 11 neighbors, silver and gold, are called the coinage metals.",
            "r": "It conducts electricity better than every metal except silver. For 10 points, name this metal used in most electrical wires."
        },
        {
            "p": "The first high-temperature superconductors, found in 1986, were cuprates, ceramics built around layers of this element’s oxide. This element’s compounds give a green or blue-green color in a flame test.",
            "r": "Its plus-two ions are called cupric. For 10 points, name this reddish metal with atomic number 29, used in most electrical wires."
        },
        {
            "p": "Ötzi the Iceman, a 5,300-year-old mummy found in the Alps in 1991, carried an axe with a blade made of this metal. This metal’s most important ore is chalcopyrite, which also contains iron and sulfur.",
            "r": "This metal and tin make bronze, the alloy that named the Bronze Age. For 10 points, name this metal."
        },
        {
            "p": "Butte [“BYOOT”], Montana, was nicknamed the “Richest Hill on Earth” for its mines of this metal. Arizona produces more of this metal than any other U.S. state, and Chile mines more of it than any other country.",
            "r": "For 10 points, name this metal that is mixed with zinc to make brass."
        },
        {
            "p": "Utah’s Bingham Canyon Mine, one of the largest open-pit mines in the world, digs out ore of this metal. Colorful ores of this metal include green malachite and blue azurite [“AZH-uh-rite”].",
            "r": "Outdoors, this metal slowly turns green, as on the Statue of Liberty. For 10 points, name this element with atomic number 29."
        },
        {
            "p": "Alchemists linked this metal to the planet Venus and to the goddess Aphrodite, who was closely tied to the island of Cyprus. That island, a major source of this metal in the ancient Mediterranean, gave this metal its name.",
            "r": "Its symbol comes from the Latin word cuprum. For 10 points, name this element with atomic number 29."
        },
        {
            "p": "Octopuses and horseshoe crabs have blue blood because their oxygen-carrying protein, hemocyanin [“hee-moh-SY-uh-nin”], uses this metal instead of iron. Adding ammonia to a solution of this metal’s plus-two ions produces a deep blue color.",
            "r": "This metal’s sulfate forms bright blue crystals. For 10 points, name this metal that is alloyed with tin to make bronze."
        },
        {
            "p": "Doorknobs and hospital surfaces made of this metal and its alloys kill many of the bacteria that land on them. Some pots and pans have bottoms made of this metal because it spreads heat quickly and evenly.",
            "r": "It is also the usual metal in electrical wires. For 10 points, name this reddish-orange element with atomic number 29."
        },
        {
            "p": "This element’s atomic mass, about 63.5, is the average of its two stable isotopes, whose mass numbers are 63 and 65. Its plus-two ions give many of its compounds a blue or green color, like the blue crystals of its sulfate.",
            "r": "For 10 points, name this element, which coats U.S. pennies and makes up the skin of the Statue of Liberty."
        },
        {
            "p": "The U.S. five-cent coin called the nickel is actually three-quarters this metal, and the rest is nickel. U.S. dimes and quarters have a core of this pure metal sandwiched between layers of its alloy with nickel.",
            "r": "Since 1982, U.S. pennies have been mostly zinc with a thin coating of this metal. For 10 points, name this element with atomic number 29."
        },
        {
            "p": "Impure slabs of this metal are purified by electrolysis, and the leftover “anode mud” often contains valuable silver and gold. The green coating that slowly forms on this metal outdoors, called a patina, protects the metal underneath.",
            "r": "That coating turned the Statue of Liberty green. For 10 points, name this metal with atomic number 29."
        },
        {
            "p": "Ancient Egyptians ground up malachite, a green mineral containing this metal, to make eye paint. An alloy of this metal and zinc is used to make trumpets, tubas, and the other instruments of an orchestra’s brass section.",
            "r": "For 10 points, name this reddish metal that conducts electricity better than any metal except silver."
        }
    ],
    "clues": [
        {
            "id": "element-29",
            "tier": "giveaway",
            "t": "Element with atomic number 29; its symbol comes from the Latin word cuprum",
            "k": ["cuprum", "latin", "29"],
            "n": 0
        },
        {
            "id": "wires",
            "tier": "giveaway",
            "t": "Conducts electricity better than any metal except silver, so it is the usual metal in electrical wires",
            "k": ["electrical wires", "conducts", "silver"],
            "n": 0,
            "rabbit": "Electrical resistance"
        },
        {
            "id": "bronze",
            "tier": "giveaway",
            "t": "Mixed with tin it makes bronze, the alloy that gave the Bronze Age its name",
            "k": ["bronze", "tin", "alloy"],
            "n": 0
        },
        {
            "id": "statue",
            "tier": "giveaway",
            "t": "The Statue of Liberty’s skin is made of it; it slowly turned green as it reacted with the air",
            "k": ["statue of liberty", "green"],
            "n": 0,
            "rabbit": "Statue of Liberty"
        },
        {
            "id": "pennies",
            "tier": "giveaway",
            "t": "It coats U.S. pennies, which since 1982 have been mostly zinc inside",
            "k": ["pennies", "1982", "zinc"],
            "n": 0
        },
        {
            "id": "brass",
            "tier": "middle",
            "t": "Mixed with zinc it makes brass, used for trumpets, tubas, and other brass instruments",
            "k": ["brass", "trumpets", "zinc"],
            "n": 0
        },
        {
            "id": "cyprus",
            "tier": "middle",
            "t": "Named for the island of Cyprus, a major source of it in the ancient Mediterranean",
            "k": ["cyprus", "island"],
            "n": 0
        },
        {
            "id": "group-11",
            "tier": "middle",
            "t": "Sits above silver and gold in group 11; the three are called the coinage metals",
            "k": ["group 11", "coinage metals", "gold"],
            "n": 0,
            "rabbit": "Gold"
        },
        {
            "id": "patina",
            "tier": "middle",
            "t": "The green coating that forms on it outdoors, a patina, protects the metal underneath",
            "k": ["patina", "coating"],
            "n": 0
        },
        {
            "id": "cuprous-cupric",
            "tier": "middle",
            "t": "Its +1 and +2 ions are called cuprous and cupric",
            "k": ["cuprous", "cupric"],
            "n": 0
        },
        {
            "id": "blue-sulfate",
            "tier": "middle",
            "t": "Its sulfate forms bright blue crystals, which turn white when heated because they lose their water",
            "k": ["blue crystals", "sulfate", "white"],
            "n": 0
        },
        {
            "id": "flame",
            "tier": "middle",
            "t": "Its compounds give a green or blue-green flame test",
            "k": ["flame test", "blue-green"],
            "n": 0,
            "rabbit": "Flame test"
        },
        {
            "id": "hemocyanin",
            "tier": "middle",
            "t": "Octopuses and horseshoe crabs have blue blood because their oxygen carrier, hemocyanin, uses it instead of iron",
            "k": ["hemocyanin", "octopuses", "blue blood"],
            "n": 0,
            "rabbit": "Hemoglobin"
        },
        {
            "id": "mining",
            "tier": "middle",
            "t": "Chile mines more of it than any other country; Arizona leads the U.S.",
            "k": ["chile", "arizona"],
            "n": 0
        },
        {
            "id": "ores",
            "tier": "middle",
            "t": "Its main ore is chalcopyrite (with iron and sulfur); malachite (green) and azurite (blue) are colorful ores",
            "k": ["chalcopyrite", "malachite", "azurite"],
            "n": 0
        },
        {
            "id": "heat",
            "tier": "middle",
            "t": "Spreads heat quickly and evenly, so some pots and pans have bottoms made of it",
            "k": ["pots and pans", "heat"],
            "n": 0
        },
        {
            "id": "electron-config",
            "tier": "power",
            "t": "Like chromium, it breaks the usual filling order: its configuration ends 3d10 4s1, since a full d subshell is extra stable",
            "k": ["3d10", "4s1", "chromium", "subshell"],
            "n": 0
        },
        {
            "id": "isotopes",
            "tier": "power",
            "t": "Its atomic mass, about 63.5, averages its two stable isotopes, with mass numbers 63 and 65",
            "k": ["63.5", "isotopes", "65"],
            "n": 0
        },
        {
            "id": "lab-tests",
            "tier": "power",
            "t": "Benedict’s test: sugars like glucose turn its blue +2 ions into a brick-red oxide; the biuret test: its sulfate turns violet with proteins",
            "k": ["benedict", "biuret", "glucose", "brick-red", "violet"],
            "n": 0,
            "rabbit": "Proteins"
        },
        {
            "id": "bordeaux",
            "tier": "power",
            "t": "Bordeaux mixture, a fungicide sprayed on grapevines since the 1880s, combines its sulfate with lime",
            "k": ["bordeaux mixture", "fungicide", "grapevines"],
            "n": 0
        },
        {
            "id": "daniell",
            "tier": "power",
            "t": "A Daniell cell pairs it with zinc, each metal standing in a solution of its own sulfate",
            "k": ["daniell cell", "zinc"],
            "n": 0
        },
        {
            "id": "cuprates",
            "tier": "power",
            "t": "The first high-temperature superconductors (1986) were cuprates, ceramics built around layers of its oxide",
            "k": ["cuprates", "superconductors", "1986"],
            "n": 0,
            "rabbit": "Superconductivity"
        },
        {
            "id": "otzi",
            "tier": "power",
            "t": "Ötzi the Iceman, a 5,300-year-old mummy found in the Alps in 1991, carried an axe with a blade made of it",
            "k": ["ötzi", "iceman", "alps", "axe"],
            "n": 0
        },
        {
            "id": "butte",
            "tier": "power",
            "t": "Butte, Montana, was nicknamed the “Richest Hill on Earth” for its mines of this metal",
            "k": ["butte", "montana", "richest hill"],
            "n": 0
        },
        {
            "id": "bingham",
            "tier": "power",
            "t": "Utah’s Bingham Canyon Mine, one of the world’s largest open-pit mines, digs out its ore",
            "k": ["bingham canyon", "utah", "open-pit"],
            "n": 0
        },
        {
            "id": "venus",
            "tier": "power",
            "t": "Alchemists linked it to the planet Venus and the goddess Aphrodite, who was tied to Cyprus",
            "k": ["alchemists", "venus", "aphrodite"],
            "n": 0
        },
        {
            "id": "coins",
            "tier": "power",
            "t": "The U.S. nickel coin is three-quarters this metal; dimes and quarters have a core of it between layers of its alloy with nickel",
            "k": ["three-quarters", "dimes", "quarters", "nickel coin"],
            "n": 0
        },
        {
            "id": "anode-mud",
            "tier": "power",
            "t": "Impure slabs are purified by electrolysis; the leftover “anode mud” often holds silver and gold",
            "k": ["anode mud", "electrolysis", "purified"],
            "n": 0
        },
        {
            "id": "antimicrobial",
            "tier": "power",
            "t": "Doorknobs and hospital surfaces made of it and its alloys kill many bacteria that land on them",
            "k": ["doorknobs", "bacteria", "hospital"],
            "n": 0
        },
        {
            "id": "ammonia-blue",
            "tier": "power",
            "t": "Adding ammonia to a solution of its +2 ions makes a deep blue color",
            "k": ["ammonia", "deep blue"],
            "n": 0,
            "rabbit": "Ammonia"
        },
        {
            "id": "egypt",
            "tier": "power",
            "t": "Ancient Egyptians ground up malachite, a green mineral containing it, to make eye paint",
            "k": ["egyptians", "eye paint", "malachite"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Element, not alloy",
        "body": "Bronze and brass are both made mostly of this metal, so clues about the Bronze Age, trumpets, or church bells tempt players to name the alloy. But alloys are mixtures, not elements. Silver and gold are the other trap: they sit right below this metal in group 11, and silver is the one metal that conducts electricity even better.",
        "fix": "If the question asks for “this element” or “this metal,” name the element itself. Atomic number 29, cuprum, cuprous and cupric, the Statue of Liberty, hemocyanin, and a green flame all point here; this metal plus tin is bronze, and this metal plus zinc is brass.",
        "line": "Real answer line: <b><u>Copper</u></b> (accept <u>Cu</u>)"
    },
    "tests": {
        "right": [
            "Copper",
            "Cu",
            "CU",
            "coper",
            "copper metal"
        ],
        "prompt": [],
        "wrong": [
            "Bronze",
            "Brass",
            "Copper sulfate",
            "Silver",
            "Zinc",
            "Gold",
            "Copper Age"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
