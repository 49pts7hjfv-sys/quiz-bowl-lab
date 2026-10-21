import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "geysers",
    "name": "Geysers",
    "mono": "GEY",
    "category": "Earth Science",
    "qbCategory": "Science · Other Science (Earth Science)",
    "kicker": "Hot springs that erupt · Old Faithful is the most famous",
    "dates": "Old Faithful named in 1870",
    "briefing": "A geyser is a hot spring with a temper: water deep underground heats up until it bursts out of the ground in a roaring column of water and steam. Only about a thousand exist on Earth, and roughly half are in Yellowstone National Park, home of Old Faithful. They are named for Geysir, a famous one in Iceland, whose name comes from an Icelandic word meaning “to gush.”",
    "answerHtml": "<b><u>Geyser</u></b>s (do not accept “hot springs,” “fumaroles,” “volcanoes,” or a single named geyser such as “Old Faithful”)",
    "accept": [
        "geyser",
        "geysers",
        "cone geyser",
        "cone geysers",
        "fountain geyser",
        "fountain geysers"
    ],
    "prompt": [],
    "reject": [
        "hot spring",
        "hot springs",
        "thermal spring",
        "thermal springs",
        "fumarole",
        "fumaroles",
        "mud pot",
        "mud pots",
        "mudpot",
        "mudpots",
        "solfatara",
        "volcano",
        "volcanoes",
        "volcanic vent",
        "hydrothermal vent",
        "hydrothermal vents",
        "black smoker",
        "black smokers",
        "old faithful",
        "steamboat",
        "steamboat geyser",
        "grand geyser",
        "beehive geyser",
        "strokkur",
        "geysir",
        "great geysir",
        "waimangu",
        "pohutu",
        "el tatio",
        "sinter",
        "geyserite",
        "artesian well"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Geyser",
    "qb": {
        "q": "geyser",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "Robert Bunsen, the chemist famous for his laboratory burner, explained how these features work after visiting Iceland in 1846, showing that water deep in a narrow tube gets hotter than its normal boiling point before suddenly flashing into steam.",
            "r": "For 10 points, name these hot springs that erupt now and then, such as Old Faithful."
        },
        {
            "p": "In 1941, scientist Tatyana Ustinova [“oo-STEE-noh-vuh”] discovered a hidden valley on Russia’s Kamchatka [“kam-CHAT-kuh”] Peninsula holding one of the world’s largest groups of these features, and part of that valley was buried by a landslide in 2007.",
            "r": "Iceland’s Strokkur [“STROH-kur”] is one that erupts every few minutes. For 10 points, name these hot springs that shoot water and steam into the air."
        },
        {
            "p": "From 1900 to 1904, New Zealand’s Waimangu [“wye-MAHNG-oo”], whose Māori name means “black water,” reportedly blasted muddy water and rocks as high as about 460 meters, making it the tallest of these features ever recorded.",
            "r": "Today the tallest active one is Steamboat, in Yellowstone. For 10 points, name these erupting hot springs."
        },
        {
            "p": "NASA’s Cassini spacecraft photographed icy jets shooting from cracks called “tiger stripes” near the south pole of Saturn’s moon Enceladus [“en-SEL-uh-dus”], which are often compared to these features. Those jets help supply one of Saturn’s rings.",
            "r": "On Earth, Yellowstone National Park holds about half of all of them. For 10 points, name these hot springs that erupt with water and steam."
        },
        {
            "p": "In 1989, Voyager 2 spotted dark plumes rising several kilometers high on Neptune’s moon Triton, which scientists compared to these features, though they may be powered by sunlight warming nitrogen ice rather than by heat from below.",
            "r": "For 10 points, name these hot springs on Earth, such as Old Faithful, that erupt now and then."
        },
        {
            "p": "Members of the Washburn Expedition named the most famous of these features in 1870 for its regular schedule. Park rangers predict its next eruption from how long the last one lasted.",
            "r": "That feature erupts in Yellowstone roughly every 60 to 110 minutes. For 10 points, name these hot springs that erupt, such as Old Faithful."
        },
        {
            "p": "Tourists gather before dawn to watch columns of steam rise at El Tatio [“el TAH-tee-oh”], a field of these features more than 4,000 meters high in Chile’s Andes, the largest such field in the Southern Hemisphere.",
            "r": "Iceland’s Geysir gave these features their name. For 10 points, name these hot springs that erupt now and then."
        },
        {
            "p": "The 1959 Hebgen Lake earthquake in Montana set off eruptions from many of these features in nearby Yellowstone and changed the timing of others. Iceland’s Strokkur, whose name means “churn,” is one that erupts every few minutes.",
            "r": "They need underground heat, water, and narrow passages that trap pressure. For 10 points, name these hot springs that erupt periodically, including Old Faithful."
        },
        {
            "p": "A pale crust of silica called sinter builds up around the openings of these features, and heat-loving microbes living in their runoff can paint the ground orange and green. Cone types shoot narrow jets of water.",
            "r": "Fountain types burst out of pools instead. For 10 points, name these hot springs that periodically erupt, like Old Faithful."
        },
        {
            "p": "Yellowstone’s Grand, the tallest of these features whose eruptions can be predicted, bursts out of a pool, making it a fountain type rather than a cone type. Steamboat, also in Yellowstone, can shoot water more than 90 meters high.",
            "r": "For 10 points, name these hot springs that erupt with water and steam, such as Old Faithful."
        },
        {
            "p": "Water deep inside one of these features can be heated well above 100 °C without boiling, because of the weight of the water above it. When some of that water flashes into steam, it pushes out the water above, and the whole column erupts.",
            "r": "For 10 points, name these erupting hot springs, which take their English name from one in Iceland."
        },
        {
            "p": "Heat from magma beneath a giant caldera, left by a supervolcano’s eruptions, powers hundreds of these features in a single U.S. national park. Only about a thousand of them exist in the whole world.",
            "r": "That park holds about half of the world’s total. For 10 points, name these erupting hot springs, such as Old Faithful."
        },
        {
            "p": "Near Green River, Utah, an old oil-exploration well sprays cold, fizzy water into the air now and then, a rare version of these features powered by carbon dioxide gas instead of heat.",
            "r": "Ordinary ones need heat from magma and narrow passages that trap pressure. For 10 points, name these hot springs that erupt, such as Old Faithful."
        },
        {
            "p": "Iceland’s Strokkur, whose name means “churn,” erupts every few minutes in the Haukadalur [“HOY-kah-dah-lur”] valley, close to a famous older one that has been mostly quiet for years. Visitors watch a blue bubble of water swell just before each burst.",
            "r": "That older one, Geysir, gave these features their English name. For 10 points, name these erupting hot springs, such as Old Faithful."
        },
        {
            "p": "In 2018, Yellowstone’s Steamboat, the tallest active one of these features, began an unusually busy phase, erupting dozens of times in some years after years of mostly staying quiet. Its biggest eruptions can top 90 meters.",
            "r": "Yellowstone’s more regular Old Faithful erupts roughly every 60 to 110 minutes. For 10 points, name these erupting hot springs."
        }
    ],
    "clues": [
        {
            "id": "erupting-springs",
            "tier": "giveaway",
            "t": "Hot springs that erupt now and then, shooting hot water and steam into the air",
            "k": ["hot springs", "erupt", "steam"],
            "n": 0
        },
        {
            "id": "old-faithful",
            "tier": "giveaway",
            "t": "Yellowstone’s Old Faithful, the most famous one, erupts roughly every 60 to 110 minutes",
            "k": ["old faithful", "60 to 110 minutes"],
            "n": 0
        },
        {
            "id": "yellowstone-half",
            "tier": "giveaway",
            "t": "Yellowstone National Park holds about half of the world’s total",
            "k": ["yellowstone", "half"],
            "n": 0
        },
        {
            "id": "iceland-geysir",
            "tier": "giveaway",
            "t": "Named for Geysir, a famous one in Iceland, from an Icelandic word meaning “to gush”",
            "k": ["geysir", "iceland", "gush"],
            "n": 0
        },
        {
            "id": "superheated",
            "tier": "middle",
            "t": "Deep water heats above 100 °C without boiling because of the pressure above it; when some flashes to steam, the whole column erupts",
            "k": ["100 °c", "pressure", "flashes to steam"],
            "n": 0
        },
        {
            "id": "plumbing",
            "tier": "middle",
            "t": "Need three things together: heat from magma, plenty of underground water, and narrow passages that trap pressure",
            "k": ["narrow passages", "magma", "trap pressure"],
            "n": 0,
            "rabbit": "Volcanoes"
        },
        {
            "id": "strokkur",
            "tier": "middle",
            "t": "Iceland’s Strokkur (“churn”) erupts every few minutes",
            "k": ["strokkur", "churn", "every few minutes"],
            "n": 0
        },
        {
            "id": "steamboat",
            "tier": "middle",
            "t": "Yellowstone’s Steamboat is the tallest active one; its biggest eruptions top 90 meters",
            "k": ["steamboat", "tallest active", "90 meters"],
            "n": 0
        },
        {
            "id": "cone-fountain",
            "tier": "middle",
            "t": "Cone types shoot narrow jets from a mound of rock; fountain types burst out of pools",
            "k": ["cone", "fountain", "pools"],
            "n": 0
        },
        {
            "id": "sinter",
            "tier": "middle",
            "t": "A pale crust of silica called sinter builds up around their openings",
            "k": ["sinter", "silica"],
            "n": 0
        },
        {
            "id": "not-fumaroles",
            "tier": "middle",
            "t": "Fumaroles vent only steam and gas, and ordinary hot springs don’t erupt",
            "k": ["fumaroles", "only steam"],
            "n": 0
        },
        {
            "id": "predict",
            "tier": "middle",
            "t": "Rangers predict Old Faithful’s next eruption from how long the last one lasted",
            "k": ["predict", "rangers", "how long"],
            "n": 0
        },
        {
            "id": "rare",
            "tier": "middle",
            "t": "Rare: only about 1,000 exist worldwide",
            "k": ["1,000", "rare", "worldwide"],
            "n": 0
        },
        {
            "id": "bunsen",
            "tier": "power",
            "t": "Robert Bunsen explained how they work after visiting Iceland in 1846",
            "k": ["bunsen", "1846"],
            "n": 0
        },
        {
            "id": "kamchatka",
            "tier": "power",
            "t": "Tatyana Ustinova found a valley full of them on Russia’s Kamchatka Peninsula in 1941; a 2007 landslide buried part of it",
            "k": ["kamchatka", "ustinova", "1941"],
            "n": 0
        },
        {
            "id": "waimangu",
            "tier": "power",
            "t": "New Zealand’s Waimangu (“black water”) reportedly erupted up to about 460 meters high from 1900 to 1904, the tallest ever recorded",
            "k": ["waimangu", "black water", "460 meters"],
            "n": 0
        },
        {
            "id": "el-tatio",
            "tier": "power",
            "t": "El Tatio, more than 4,000 meters high in Chile’s Andes, is the largest field of them in the Southern Hemisphere",
            "k": ["el tatio", "chile", "andes"],
            "n": 0
        },
        {
            "id": "grand",
            "tier": "power",
            "t": "Yellowstone’s Grand, a fountain type, is the tallest one whose eruptions can be predicted",
            "k": ["grand", "predicted", "fountain type"],
            "n": 0
        },
        {
            "id": "washburn",
            "tier": "power",
            "t": "The Washburn Expedition named Old Faithful in 1870 for its regular schedule",
            "k": ["washburn", "1870"],
            "n": 0
        },
        {
            "id": "hebgen-lake",
            "tier": "power",
            "t": "The 1959 Hebgen Lake earthquake set off eruptions from many in Yellowstone and changed the timing of others",
            "k": ["hebgen lake", "1959", "earthquake"],
            "n": 0
        },
        {
            "id": "enceladus",
            "tier": "power",
            "t": "NASA’s Cassini saw icy jets spraying from “tiger stripes” on Saturn’s moon Enceladus",
            "k": ["enceladus", "tiger stripes", "cassini"],
            "n": 0
        },
        {
            "id": "triton",
            "tier": "power",
            "t": "Voyager 2 saw dark plumes rising on Neptune’s moon Triton in 1989",
            "k": ["triton", "voyager 2", "1989"],
            "n": 0
        },
        {
            "id": "cold-water",
            "tier": "power",
            "t": "Near Green River, Utah, an old oil-exploration well sprays cold water pushed out by carbon dioxide gas",
            "k": ["green river", "carbon dioxide", "utah"],
            "n": 0
        },
        {
            "id": "caldera",
            "tier": "power",
            "t": "Yellowstone’s are powered by magma beneath a giant supervolcano caldera",
            "k": ["caldera", "supervolcano"],
            "n": 0
        },
        {
            "id": "steamboat-2018",
            "tier": "power",
            "t": "Steamboat began an unusually busy phase in 2018, erupting dozens of times in some years",
            "k": ["2018", "busy phase", "dozens"],
            "n": 0
        },
        {
            "id": "microbes",
            "tier": "power",
            "t": "Heat-loving microbes in their runoff color the ground orange and green",
            "k": ["microbes", "heat-loving"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Not just Old Faithful",
        "body": "Geyser tossups love famous examples, like Old Faithful, Steamboat, Strokkur, and Iceland’s Geysir itself, so players blurt one name when the question wants the whole category. Neighbors trip players up too: an ordinary hot spring doesn’t erupt, a fumarole vents only steam and gas, and a mud pot is a bubbling pool of mud.",
        "fix": "Listen for “these features” or “these hot springs that erupt,” and answer geysers. If the tossup says “this geyser” and every clue points to one place, it wants that one by name. If water shoots into the air, it’s a geyser; if only steam hisses out, it’s a fumarole.",
        "line": "Real answer line: <b><u>Geyser</u></b>s (do not accept “hot springs,” “fumaroles,” or a single geyser such as “Old Faithful”)"
    },
    "tests": {
        "right": [
            "Geysers",
            "geyser",
            "Gyser",
            "Cone geyser",
            "fountain geysers",
            "Yellowstone geysers"
        ],
        "prompt": [],
        "wrong": [
            "Hot springs",
            "Old Faithful",
            "Fumaroles",
            "Volcano",
            "Steamboat Geyser",
            "Geysir",
            "Mud pots",
            "Strokkur"
        ]
    }
}

with open(ROOT / "topics" / "geysers.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("wrote topics/geysers.json")
