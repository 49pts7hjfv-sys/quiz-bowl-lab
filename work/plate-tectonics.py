import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "plate-tectonics",
    "name": "Plate tectonics",
    "mono": "PT",
    "category": "Earth Science",
    "qbCategory": "Science · Other Science (Earth Science)",
    "kicker": "Theory of Earth’s moving outer shell · Explains earthquakes and volcanoes",
    "dates": "Accepted in the late 1960s",
    "briefing": "Earth’s rigid outer shell is cracked into a dozen or so giant plates that creep a few centimeters a year, about as fast as your fingernails grow. Plate tectonics, the theory that tied together Alfred Wegener’s continental drift and Harry Hess’s seafloor spreading in the 1960s, explains why most earthquakes and volcanoes strike where plates meet, and how India crashed into Asia to raise the Himalayas.",
    "answerHtml": "<b><u>Plate tectonics</u></b> (accept <u>tectonic plates</u> or <u>plate tectonic</u> theory; prompt on <u>continental drift</u> or <u>plates</u>; do not accept “seafloor spreading”)",
    "accept": [
        "plate tectonics",
        "plate tectonic",
        "plate tectonic theory",
        "theory of plate tectonics",
        "tectonic plates",
        "tectonic plate",
        "tectonic plate theory",
        "lithospheric plates",
        "lithospheric plate",
        "crustal plates"
    ],
    "prompt": [
        "continental drift",
        "theory of continental drift",
        "plates",
        "tectonics",
        "plate motion",
        "plate motions",
        "plate movement",
        "plate movements",
        "plate theory"
    ],
    "reject": [
        "seafloor spreading",
        "sea floor spreading",
        "ocean floor spreading",
        "subduction",
        "convection",
        "mantle convection",
        "convection currents",
        "pangaea",
        "pangea",
        "earthquake",
        "earthquakes",
        "volcano",
        "volcanoes",
        "fault",
        "faults",
        "isostasy",
        "orogeny",
        "lithosphere",
        "asthenosphere",
        "mantle",
        "mid ocean ridge",
        "mid ocean ridges",
        "hotspot",
        "hotspots",
        "hot spot",
        "ring of fire",
        "genetic drift"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Plate_tectonics",
    "qb": {
        "q": "plate tectonics",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "Dan McKenzie and Robert Parker helped launch this theory with a 1967 paper on the North Pacific, and W. Jason Morgan independently published a similar model the next year. Those papers showed that rigid pieces of Earth’s surface could move across a sphere without bending.",
            "r": "This theory explains why earthquakes and volcanoes line the Pacific Ring of Fire. For 10 points, name this theory that says Earth’s outer shell is broken into large moving pieces."
        },
        {
            "p": "J. Tuzo Wilson identified a new class of faults, called transform faults, that offset mid-ocean ridges, and a cycle in which oceans repeatedly open and close is named for him. Wilson also proposed that a fixed hotspot built the Hawaiian Islands.",
            "r": "California’s San Andreas Fault is a transform boundary in this theory. For 10 points, name this theory that says Earth’s lithosphere is split into large pieces that slowly move."
        },
        {
            "p": "In 1968, Xavier Le Pichon [“luh pee-SHOHN”] used seafloor data to divide the globe into six huge pieces under this theory. In this theory, the motion of each piece across Earth’s curved surface can be described as a rotation around a point called its Euler [“OY-ler”] pole.",
            "r": "The largest piece in this theory lies almost entirely beneath the Pacific Ocean. For 10 points, name this theory that says Earth’s rigid outer shell is broken into large, moving pieces."
        },
        {
            "p": "Geologists use a theorem by the mathematician Leonhard Euler [“OY-ler”] to describe motion in this theory, in which each moving piece rotates around its own Euler pole. GPS receivers anchored in solid rock can measure that motion directly.",
            "r": "Pieces in this theory move only a few centimeters a year, about as fast as fingernails grow. For 10 points, name this theory of Earth’s slowly moving outer shell."
        },
        {
            "p": "The Afar [“AH-far”] region of Ethiopia sits on a triple junction, a point where three of the rigid pieces described by this theory meet. Nearby, the Red Sea and the Gulf of Aden are widening as Arabia pulls away from Africa.",
            "r": "The East African Rift is slowly splitting Africa at a divergent boundary in this theory. For 10 points, name this theory that explains how Earth’s outer shell moves in large pieces."
        },
        {
            "p": "Wadati–Benioff zones, slanting bands of earthquakes that reach hundreds of kilometers deep, trace cold slabs of seafloor sinking into the mantle in this theory. Such zones dip beneath curving chains of volcanic islands, such as Japan and the Aleutians.",
            "r": "In this theory, subduction at convergent boundaries creates deep trenches like the Mariana Trench. For 10 points, name this theory that says Earth’s outer shell is broken into large moving pieces."
        },
        {
            "p": "Many geologists think “slab pull,” the tug of old, cold seafloor sinking at trenches, is the strongest force driving motion in this theory, with help from “ridge push” at mid-ocean ridges. Because old seafloor sinks back into the mantle, almost no ocean floor is older than about 200 million years.",
            "r": "Heat escaping from Earth’s interior also drives slow convection in the mantle. For 10 points, name this theory of Earth’s moving outer shell."
        },
        {
            "p": "The second word in this theory’s name comes from a Greek word for “builder,” since it explains how features like mountain ranges and ocean basins are built. In this theory, dense oceanic crust sinks beneath lighter continental crust where the two collide.",
            "r": "This theory combined Alfred Wegener’s continental drift with Harry Hess’s seafloor spreading. For 10 points, name this 1960s theory of Earth’s moving outer shell."
        },
        {
            "p": "Earth is the only planet known to show the process described by this theory, which helps recycle carbon between the air and Earth’s rocks over millions of years. Venus, by contrast, seems to have a single unbroken outer shell.",
            "r": "The Pacific Ring of Fire traces boundaries described by this theory. For 10 points, name this theory that says Earth’s outer shell is broken into large, slowly moving pieces."
        },
        {
            "p": "Decades before this theory was accepted, British geologist Arthur Holmes suggested in the late 1920s that slow convection currents in the mantle could drag continents apart. Holmes also helped pioneer the use of radioactivity to measure the ages of rocks.",
            "r": "This theory grew out of Alfred Wegener’s older idea of continental drift. For 10 points, name this theory in which rigid pieces of the lithosphere ride on the soft asthenosphere."
        },
        {
            "p": "Volcanic islands get steadily older toward the northwest along the Hawaiian chain, because the Pacific seafloor has carried them away from a hotspot in the motion described by this theory. A sharp bend in that chain is usually explained as a change in the seafloor’s direction of motion.",
            "r": "Hotspots are unusual, since most volcanoes form along boundaries in this theory. For 10 points, name this theory of Earth’s moving outer shell."
        },
        {
            "p": "Curving chains of volcanic islands, like the Aleutians and the Mariana Islands, form in this theory where one piece of ocean floor dives beneath another. The Andes formed instead where ocean floor sinks beneath the edge of a continent.",
            "r": "That sinking, called subduction, also carves deep ocean trenches. For 10 points, name this theory that says Earth’s rigid outer shell is broken into large, moving pieces."
        },
        {
            "p": "Scuba divers in Iceland’s Silfra fissure swim through a crack between the North American and Eurasian pieces of Earth’s outer shell in this theory. Volcanoes in Iceland erupt partly because the island sits right on that spreading boundary.",
            "r": "The Mid-Atlantic Ridge is a divergent boundary in this theory. For 10 points, name this theory in which rigid pieces of Earth’s outer shell glide over the asthenosphere."
        },
        {
            "p": "The small Juan de Fuca piece of seafloor sinking beneath the Pacific Northwest feeds the Cascade volcanoes, including Mount St. Helens, in this theory. That same sinking zone set off a giant earthquake in the year 1700 that sent a tsunami all the way to Japan.",
            "r": "California’s San Andreas Fault marks a transform boundary in this theory. For 10 points, name this theory that says Earth’s outer shell is split into large, slowly moving pieces."
        },
        {
            "p": "This theory explains how India drifted north and slammed into Asia, crumpling rock into the Himalayas, which is why fossils of sea creatures lie near the top of Mount Everest. It also explains why the coasts of South America and Africa fit together like puzzle pieces.",
            "r": "This theory combined continental drift with seafloor spreading. For 10 points, name this theory that says Earth’s rigid outer shell is broken into large moving pieces."
        }
    ],
    "clues": [
        {
            "id": "outer-shell",
            "tier": "giveaway",
            "t": "The theory that Earth’s rigid outer shell, the lithosphere, is broken into large pieces that slowly move",
            "k": ["lithosphere", "outer shell", "slowly move"],
            "n": 0
        },
        {
            "id": "three-boundaries",
            "tier": "giveaway",
            "t": "Its pieces meet at three kinds of boundaries: divergent (pulling apart), convergent (pushing together), and transform (sliding past)",
            "k": ["divergent", "convergent", "transform"],
            "n": 0
        },
        {
            "id": "quakes-volcanoes",
            "tier": "giveaway",
            "t": "Explains why most earthquakes, volcanoes, and mountain ranges form along the boundaries between its pieces",
            "k": ["earthquakes", "volcanoes", "boundaries"],
            "n": 0,
            "rabbit": "Earthquakes"
        },
        {
            "id": "wegener-hess",
            "tier": "giveaway",
            "t": "Grew in the 1960s out of Alfred Wegener’s continental drift and Harry Hess’s seafloor spreading",
            "k": ["continental drift", "wegener", "seafloor spreading", "1960s"],
            "n": 0,
            "rabbit": "Seafloor spreading"
        },
        {
            "id": "asthenosphere",
            "tier": "giveaway",
            "t": "Its rigid pieces ride on the soft, slowly flowing asthenosphere of the upper mantle",
            "k": ["asthenosphere"],
            "n": 0,
            "rabbit": "Asthenosphere"
        },
        {
            "id": "divergent-examples",
            "tier": "middle",
            "t": "Divergent examples include the Mid-Atlantic Ridge and the East African Rift, where new crust forms as pieces pull apart",
            "k": ["mid-atlantic ridge", "east african rift", "pull apart"],
            "n": 0
        },
        {
            "id": "subduction-trenches",
            "tier": "middle",
            "t": "At convergent boundaries, denser ocean floor sinks in subduction, forming deep trenches like the Mariana Trench and ranges like the Andes",
            "k": ["subduction", "mariana trench", "andes", "trenches"],
            "n": 0,
            "rabbit": "Subduction"
        },
        {
            "id": "himalayas",
            "tier": "middle",
            "t": "India slammed into Asia and raised the Himalayas, which is why fossils of sea creatures lie near Mount Everest’s summit",
            "k": ["himalayas", "india", "everest"],
            "n": 0
        },
        {
            "id": "san-andreas",
            "tier": "middle",
            "t": "California’s San Andreas Fault is a transform boundary, where two pieces slide past each other",
            "k": ["san andreas", "slide past"],
            "n": 0,
            "rabbit": "Faults"
        },
        {
            "id": "ring-of-fire",
            "tier": "middle",
            "t": "The Pacific Ring of Fire traces the boundaries around the Pacific Ocean, where many earthquakes and volcanoes strike",
            "k": ["ring of fire", "pacific"],
            "n": 0,
            "rabbit": "Volcanoes"
        },
        {
            "id": "speed-gps",
            "tier": "middle",
            "t": "Its pieces move a few centimeters a year, about as fast as fingernails grow, and GPS can measure the motion",
            "k": ["centimeters", "fingernails", "gps"],
            "n": 0
        },
        {
            "id": "convection",
            "tier": "middle",
            "t": "Heat escaping from Earth’s interior drives slow convection in the mantle beneath the moving pieces",
            "k": ["convection", "mantle"],
            "n": 0,
            "rabbit": "Mantle"
        },
        {
            "id": "hotspots",
            "tier": "middle",
            "t": "Hotspots, like the one under Hawaii, are an exception: they make volcanoes far from any boundary",
            "k": ["hotspots", "hotspot", "hawaii"],
            "n": 0
        },
        {
            "id": "pacific-largest",
            "tier": "middle",
            "t": "Its largest piece lies almost entirely beneath the Pacific Ocean",
            "k": ["largest", "pacific ocean"],
            "n": 0
        },
        {
            "id": "mckenzie-morgan",
            "tier": "power",
            "t": "Dan McKenzie and Robert Parker (1967) and W. Jason Morgan (1968) showed rigid pieces of Earth’s surface moving across a sphere",
            "k": ["mckenzie", "parker", "jason morgan", "sphere"],
            "n": 0
        },
        {
            "id": "tuzo-wilson",
            "tier": "power",
            "t": "J. Tuzo Wilson named transform faults, proposed the Hawaiian hotspot, and gave his name to the Wilson cycle of oceans opening and closing",
            "k": ["tuzo wilson", "wilson cycle", "transform faults"],
            "n": 0
        },
        {
            "id": "le-pichon",
            "tier": "power",
            "t": "Xavier Le Pichon’s 1968 model divided the globe into six huge pieces",
            "k": ["le pichon", "six huge pieces"],
            "n": 0
        },
        {
            "id": "euler-poles",
            "tier": "power",
            "t": "Each piece’s motion across the sphere is a rotation around its own Euler [“OY-ler”] pole, from a theorem by Leonhard Euler",
            "k": ["euler pole", "euler", "rotation"],
            "n": 0
        },
        {
            "id": "triple-junction",
            "tier": "power",
            "t": "Three pieces meet at a triple junction, like the one in Ethiopia’s Afar region, where the Red Sea and Gulf of Aden are opening",
            "k": ["triple junction", "afar", "red sea"],
            "n": 0
        },
        {
            "id": "wadati-benioff",
            "tier": "power",
            "t": "Wadati–Benioff zones are slanting bands of deep earthquakes along slabs of seafloor sinking into the mantle",
            "k": ["wadati", "benioff", "slanting"],
            "n": 0
        },
        {
            "id": "slab-pull",
            "tier": "power",
            "t": "“Slab pull,” the tug of old seafloor sinking at trenches, is thought to be its strongest driving force, helped by “ridge push”",
            "k": ["slab pull", "ridge push"],
            "n": 0
        },
        {
            "id": "greek-builder",
            "tier": "power",
            "t": "The second word of its name comes from a Greek word for “builder”",
            "k": ["greek", "builder"],
            "n": 0
        },
        {
            "id": "only-earth",
            "tier": "power",
            "t": "Earth is the only planet known to have it; Venus seems to have one unbroken outer shell",
            "k": ["only planet", "venus"],
            "n": 0
        },
        {
            "id": "holmes",
            "tier": "power",
            "t": "Arthur Holmes suggested in the late 1920s that mantle convection could carry continents; he also pioneered dating rocks with radioactivity",
            "k": ["arthur holmes", "holmes", "radioactivity"],
            "n": 0
        },
        {
            "id": "hawaiian-chain",
            "tier": "power",
            "t": "The Hawaiian chain gets older toward the northwest as the Pacific seafloor slides over a hotspot; a sharp bend is usually explained as a change in direction",
            "k": ["northwest", "sharp bend", "hawaiian chain"],
            "n": 0
        },
        {
            "id": "island-arcs",
            "tier": "power",
            "t": "Where ocean floor dives beneath ocean floor, curving island arcs form, like the Aleutians and the Mariana Islands",
            "k": ["island arcs", "aleutians", "mariana islands"],
            "n": 0
        },
        {
            "id": "silfra",
            "tier": "power",
            "t": "Divers in Iceland’s Silfra fissure swim through a crack between the North American and Eurasian pieces",
            "k": ["silfra", "iceland", "eurasian"],
            "n": 0
        },
        {
            "id": "juan-de-fuca",
            "tier": "power",
            "t": "The small Juan de Fuca piece sinks beneath the Pacific Northwest, feeding the Cascade volcanoes and setting off a giant earthquake in 1700",
            "k": ["juan de fuca", "cascade", "1700"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Drift, spreading, or plates?",
        "body": "Three answer lines tell one story. Continental drift was Alfred Wegener’s 1912 idea that the continents move, which most scientists rejected because he could not explain how. Seafloor spreading, Harry Hess’s idea from the early 1960s, showed how new ocean crust forms at mid-ocean ridges, and plate tectonics tied both together into one theory of a moving, broken outer shell.",
        "fix": "Wegener, Pangaea, matching fossils, and puzzle-piece coastlines point to continental drift, which earns only a prompt here. Hess, magnetic stripes, and new crust at mid-ocean ridges mean seafloor spreading, which is wrong. Three kinds of boundaries, slab pull, J. Tuzo Wilson, or McKenzie and Parker mean plate tectonics.",
        "line": "Real answer line: <b><u>Plate tectonics</u></b> (accept tectonic plates; prompt on continental drift; do not accept “seafloor spreading”)"
    },
    "tests": {
        "right": ["Plate tectonics", "tectonic plates", "plate tectonic theory", "plate techtonics", "Theory of plate tectonics"],
        "prompt": ["Continental drift", "plates"],
        "wrong": ["Seafloor spreading", "Subduction", "Pangaea", "Convection currents", "Earthquakes"]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
