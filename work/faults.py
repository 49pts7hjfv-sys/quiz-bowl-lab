import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "faults",
    "name": "Faults",
    "mono": "FLT",
    "category": "Earth Science",
    "qbCategory": "Science · Other Science (Earth Science)",
    "kicker": "Breaks in the crust where rock slips past rock · Where earthquakes start",
    "dates": "Elastic rebound theory: Harry Fielding Reid, 1910",
    "briefing": "Faults are breaks in Earth’s crust where the rock on one side has moved past the rock on the other, sometimes by a few centimeters and sometimes by many kilometers over millions of years. When stress builds up along a stuck fault and the rock suddenly lurches, the ground shakes in an earthquake. California’s San Andreas Fault, where two tectonic plates grind sideways past each other, caused the great San Francisco earthquake of 1906.",
    "answerHtml": "<b><u>Faults</u></b> (accept <u>fault</u> lines or <u>fault</u> zones; accept specific types such as normal, reverse, thrust, or strike-slip <u>faults</u>; prompt on fractures or cracks; do not accept “earthquakes” or a single named example like “San Andreas Fault”)",
    "accept": [
        "faults",
        "fault",
        "fault line",
        "fault lines",
        "fault zone",
        "fault zones",
        "faulting",
        "geologic fault",
        "geologic faults",
        "geological fault",
        "geological faults",
        "fault plane",
        "fault planes",
        "normal fault",
        "normal faults",
        "reverse fault",
        "reverse faults",
        "thrust fault",
        "thrust faults",
        "strike slip fault",
        "strike slip faults",
        "transform fault",
        "transform faults",
        "dip slip fault",
        "dip slip faults",
        "oblique slip fault",
        "oblique slip faults"
    ],
    "prompt": [
        "fracture",
        "fractures",
        "rock fracture",
        "rock fractures",
        "crack",
        "cracks",
        "cracks in the crust",
        "break",
        "breaks",
        "rupture",
        "ruptures",
        "thrust",
        "thrusts",
        "overthrust",
        "strike slip",
        "transform boundary",
        "transform boundaries",
        "transform plate boundary",
        "transform plate boundaries"
    ],
    "reject": [
        "earthquake",
        "earthquakes",
        "quake",
        "quakes",
        "seismic waves",
        "epicenter",
        "hypocenter",
        "focus",
        "san andreas",
        "san andreas fault",
        "hayward fault",
        "north anatolian fault",
        "hanging wall",
        "footwall",
        "foot wall",
        "fault scarp",
        "fault scarps",
        "scarp",
        "fault block mountain",
        "fault block mountains",
        "joint",
        "joints",
        "fold",
        "folds",
        "folding",
        "anticline",
        "syncline",
        "fissure",
        "fissures",
        "rift",
        "rift valley",
        "graben",
        "grabens",
        "horst",
        "horsts",
        "slickensides",
        "plate tectonics",
        "tectonic plates",
        "plate boundary",
        "plate boundaries",
        "subduction",
        "subduction zone",
        "seafloor spreading",
        "volcano",
        "volcanoes",
        "faust",
        "fasting",
        "the fault in our stars",
        "fault in our stars"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Fault_(geology)",
    "qb": {
        "q": "fault",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "Miners gave the two sides of these features their names: they could hang lanterns from the block above a slanted one while standing on the block below it. In one kind of these features, that upper block slides downward as the crust is stretched apart.",
            "r": "That kind is called normal, and the two blocks are called the hanging wall and the footwall. For 10 points, name these breaks in Earth’s crust along which blocks of rock move."
        },
        {
            "p": "Polished, grooved surfaces called slickensides form where rock grinds against rock along these features, and their scratches show which way the rock slid. Crushed, powdery rock called gouge often fills the zones along them.",
            "r": "Earthquakes begin when rock suddenly slips along one. For 10 points, name these fractures in Earth’s crust, whose main types are normal, reverse, and strike-slip."
        },
        {
            "p": "Geologists describe the position of one of these features with two measurements: its strike, the compass direction of the line where it meets level ground, and its dip, the angle at which it slants downward. The dip-slip kinds of these features move up or down along that slant.",
            "r": "Strike-slip kinds move sideways instead. For 10 points, name these breaks in rock, such as California’s San Andreas, along which earthquakes happen."
        },
        {
            "p": "After studying the 1906 San Francisco earthquake, Harry Fielding Reid proposed elastic rebound theory, which says rock on both sides of one of these features slowly bends as stress builds, then snaps back when the rock suddenly slips.",
            "r": "That 1906 earthquake struck along the San Andreas. For 10 points, name these fractures in Earth’s crust where blocks of rock move past each other."
        },
        {
            "p": "By the principle of cross-cutting relationships, one of these features must be younger than any rock layers it slices through. Matching layers on opposite sides of one of these features often sit at different heights, because the rock has shifted along it.",
            "r": "For 10 points, name these breaks in Earth’s crust, which come in normal, reverse, and strike-slip types."
        },
        {
            "p": "In Montana’s Glacier National Park, a huge slab of ancient rock slid over much younger rock along the Lewis Overthrust, and Chief Mountain is a lone leftover piece of that slab. That overthrust formed as the crust was squeezed and one block was shoved up and over another.",
            "r": "Low-angle reverse types like it are called thrusts. For 10 points, name these breaks in Earth’s crust along which rock slips during earthquakes."
        },
        {
            "p": "Because moderate earthquakes had struck Parkfield, California, about every 22 years, scientists predicted another one there by 1993, but it did not arrive until 2004. Parkfield sits on the most famous of these features in the United States.",
            "r": "That feature, the San Andreas, marks where two plates slide past each other. For 10 points, name these breaks in Earth’s crust where earthquakes occur."
        },
        {
            "p": "The University of California’s football stadium in Berkeley was built right across the Hayward example of these features, which slowly creeps and pulls curbs and walls out of line. The Hayward example also produced a large earthquake in 1868.",
            "r": "California’s most famous example is the San Andreas. For 10 points, name these cracks in Earth’s crust along which blocks of rock slip."
        },
        {
            "p": "The 1994 Northridge earthquake near Los Angeles struck on a “blind” one of these features, which lies buried and never breaks the ground surface. It was a thrust, a kind of these features that forms where the crust is squeezed together.",
            "r": "Other kinds include normal and strike-slip. For 10 points, name these fractures along which rocks move, causing earthquakes."
        },
        {
            "p": "Nevada’s Basin and Range region is a series of raised blocks called horsts and dropped blocks called grabens [“GRAH-bunz”], created as the crust stretched apart along these features. Wyoming’s Teton Range rose along one of them at its eastern edge.",
            "r": "Those are the normal type, in which the hanging wall drops down. For 10 points, name these breaks in rock along which earthquakes happen."
        },
        {
            "p": "Turkey’s North Anatolian example of these features has produced a series of major earthquakes, including one near Izmit [“IZ-mit”] in 1999. Its two sides slide horizontally past each other, with the far side moving to the right, so geologists call it right-lateral.",
            "r": "California’s San Andreas is also a right-lateral, strike-slip example. For 10 points, name these fractures in Earth’s crust where rock slips during earthquakes."
        },
        {
            "p": "Wallace Creek, on California’s Carrizo [“kuh-REE-zoh”] Plain, takes a sharp sideways jog where it crosses one of these features, because the ground has shifted along it over thousands of years. Low spots along such features can fill with water to form sag ponds.",
            "r": "For 10 points, name these breaks in Earth’s crust, such as the San Andreas, which come in normal, reverse, and strike-slip types."
        },
        {
            "p": "In 1965, J. Tuzo Wilson named the transform type of these features, which offset mid-ocean ridges into staggered segments. Where a transform type cuts across land, as in California, its two sides slide horizontally past each other.",
            "r": "Earthquakes strike when rock lurches along these features. For 10 points, name these fractures, including the San Andreas, along which blocks of rock move."
        },
        {
            "p": "Engineers set the Trans-Alaska Pipeline on sliding supports where it crosses the Denali example of these features, so when a magnitude 7.9 earthquake shifted the ground there in 2002, the pipeline did not break.",
            "r": "That quake moved the ground mostly sideways. For 10 points, name these breaks in Earth’s crust, whose types include normal, reverse, and strike-slip, along which earthquakes happen."
        },
        {
            "p": "Tension, which pulls the crust apart, makes the hanging wall of one of these features slide down, while compression pushes the hanging wall up compared with the footwall. Shear stress makes the two blocks slide sideways past each other instead.",
            "r": "Those motions define the normal, reverse, and strike-slip types. For 10 points, name these breaks in Earth’s crust, such as the San Andreas, where earthquakes start."
        }
    ],
    "clues": [
        {
            "id": "breaks-in-crust",
            "tier": "giveaway",
            "t": "Breaks in Earth’s crust where blocks of rock have moved past each other",
            "k": ["breaks", "blocks of rock", "crust"],
            "n": 0
        },
        {
            "id": "earthquakes",
            "tier": "giveaway",
            "t": "Earthquakes happen when stress builds up and the rock along one suddenly slips",
            "k": ["earthquakes", "slips", "stress"],
            "n": 0,
            "rabbit": "Earthquakes"
        },
        {
            "id": "three-types",
            "tier": "giveaway",
            "t": "Three main types: normal, reverse, and strike-slip",
            "k": ["normal", "reverse", "strike-slip"],
            "n": 0
        },
        {
            "id": "san-andreas",
            "tier": "giveaway",
            "t": "California’s San Andreas is the most famous example, where the Pacific and North American plates slide past each other",
            "k": ["san andreas", "california", "pacific"],
            "n": 0,
            "rabbit": "Plate tectonics"
        },
        {
            "id": "hanging-footwall",
            "tier": "middle",
            "t": "The block above a slanted one is the hanging wall; the block below it is the footwall",
            "k": ["hanging wall", "footwall"],
            "n": 0
        },
        {
            "id": "normal-tension",
            "tier": "middle",
            "t": "Normal type: tension stretches the crust apart and the hanging wall slides down",
            "k": ["tension", "slides down", "normal"],
            "n": 0
        },
        {
            "id": "reverse-compression",
            "tier": "middle",
            "t": "Reverse type: compression squeezes the crust and pushes the hanging wall up",
            "k": ["compression", "squeezes", "reverse"],
            "n": 0
        },
        {
            "id": "thrust",
            "tier": "middle",
            "t": "A thrust is a low-angle reverse type that can shove older rock on top of younger rock",
            "k": ["thrust", "low-angle", "older rock"],
            "n": 0
        },
        {
            "id": "strike-slip-shear",
            "tier": "middle",
            "t": "Strike-slip type: shear stress makes the blocks slide horizontally; the San Andreas is right-lateral",
            "k": ["shear", "horizontally", "right-lateral"],
            "n": 0
        },
        {
            "id": "elastic-rebound",
            "tier": "middle",
            "t": "Elastic rebound theory: rock on both sides bends as stress builds, then snaps back when it slips",
            "k": ["elastic rebound", "snaps back"],
            "n": 0
        },
        {
            "id": "horst-graben",
            "tier": "middle",
            "t": "Normal ones stretch the land into raised horsts and dropped grabens, as in Nevada’s Basin and Range",
            "k": ["horsts", "grabens", "basin and range"],
            "n": 0
        },
        {
            "id": "transform",
            "tier": "middle",
            "t": "Transform types offset mid-ocean ridges and form transform plate boundaries",
            "k": ["transform", "mid-ocean ridges"],
            "n": 0,
            "rabbit": "Seafloor spreading"
        },
        {
            "id": "scarp",
            "tier": "middle",
            "t": "Where one breaks the ground surface, it can leave a step-like cliff called a scarp",
            "k": ["scarp", "cliff"],
            "n": 0
        },
        {
            "id": "miners-lanterns",
            "tier": "power",
            "t": "Miners named the two walls: they hung lanterns on the hanging wall and stood on the footwall",
            "k": ["miners", "lanterns"],
            "n": 0
        },
        {
            "id": "slickensides",
            "tier": "power",
            "t": "Polished, grooved slickensides show which way the rock slid; crushed rock called gouge fills the zone",
            "k": ["slickensides", "gouge", "grooved"],
            "n": 0
        },
        {
            "id": "strike-dip",
            "tier": "power",
            "t": "Position given by strike (compass direction along level ground) and dip (the angle it slants down)",
            "k": ["strike", "dip", "compass direction"],
            "n": 0
        },
        {
            "id": "cross-cutting",
            "tier": "power",
            "t": "Cross-cutting relationships: one is younger than any rock layers it cuts through",
            "k": ["cross-cutting", "younger"],
            "n": 0
        },
        {
            "id": "reid-1906",
            "tier": "power",
            "t": "Harry Fielding Reid proposed elastic rebound theory after studying the 1906 San Francisco earthquake",
            "k": ["harry fielding reid", "reid", "1906"],
            "n": 0
        },
        {
            "id": "parkfield",
            "tier": "power",
            "t": "Parkfield, California, on the San Andreas: a quake predicted by 1993 finally came in 2004",
            "k": ["parkfield", "1993", "2004"],
            "n": 0
        },
        {
            "id": "lewis-overthrust",
            "tier": "power",
            "t": "The Lewis Overthrust in Glacier National Park slid ancient rock over younger rock; Chief Mountain is a leftover piece",
            "k": ["lewis overthrust", "chief mountain", "glacier national park"],
            "n": 0
        },
        {
            "id": "northridge",
            "tier": "power",
            "t": "The 1994 Northridge earthquake struck on a buried “blind” thrust",
            "k": ["northridge", "blind", "1994"],
            "n": 0
        },
        {
            "id": "hayward",
            "tier": "power",
            "t": "The Hayward example creeps beneath the University of California’s football stadium in Berkeley and caused an 1868 earthquake",
            "k": ["hayward", "berkeley", "creeps", "1868"],
            "n": 0
        },
        {
            "id": "north-anatolian",
            "tier": "power",
            "t": "Turkey’s North Anatolian is a right-lateral strike-slip example that caused the 1999 Izmit earthquake",
            "k": ["north anatolian", "izmit", "turkey"],
            "n": 0
        },
        {
            "id": "wallace-creek",
            "tier": "power",
            "t": "Wallace Creek on the Carrizo Plain jogs sideways across the San Andreas; sag ponds fill low spots along such breaks",
            "k": ["wallace creek", "sag ponds", "carrizo plain"],
            "n": 0
        },
        {
            "id": "wilson-1965",
            "tier": "power",
            "t": "J. Tuzo Wilson named the transform type in 1965",
            "k": ["tuzo wilson", "1965"],
            "n": 0
        },
        {
            "id": "denali-pipeline",
            "tier": "power",
            "t": "The Trans-Alaska Pipeline crosses the Denali example on sliding supports and survived a 2002 earthquake there",
            "k": ["denali", "trans-alaska pipeline", "2002"],
            "n": 0
        },
        {
            "id": "tetons",
            "tier": "power",
            "t": "Wyoming’s Teton Range rose along a normal one at its eastern edge",
            "k": ["teton range", "wyoming"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Fault or earthquake?",
        "body": "Fault tossups are packed with earthquake clues, like elastic rebound, the 1906 San Francisco quake, and Parkfield, so players blurt out “earthquakes,” which names the shaking, not the crack in the rock. Others name one famous example, like the San Andreas, or one part, like the hanging wall, when the question wants the whole category.",
        "fix": "Listen for “these features,” “these breaks,” or “these fractures,” and answer faults. Naming a type, such as normal, thrust, or strike-slip faults, is fine, and “fractures” alone earns a prompt. Save “earthquakes” for questions about the shaking and its waves.",
        "line": "Real answer line: <b><u>Faults</u></b> (accept <u>fault</u> lines or specific types such as strike-slip faults; prompt on fractures; do not accept “earthquakes” or “San Andreas Fault”)"
    },
    "tests": {
        "right": [
            "Faults",
            "fault",
            "Fault lines",
            "Strike-slip fault",
            "Normal faults",
            "Falts"
        ],
        "prompt": [
            "Fractures",
            "Cracks",
            "Transform boundary"
        ],
        "wrong": [
            "Earthquakes",
            "San Andreas Fault",
            "Hanging wall",
            "Joints",
            "Folds",
            "The Fault in Our Stars",
            "Subduction"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
