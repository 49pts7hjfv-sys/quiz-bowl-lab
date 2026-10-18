import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "asthenosphere",
    "name": "Asthenosphere",
    "mono": "AST",
    "category": "Earth Science",
    "qbCategory": "Science · Other Science (Earth Science)",
    "kicker": "Soft, slowly flowing layer of the upper mantle · Earth’s plates ride on it",
    "dates": "Named in 1914",
    "briefing": "Earth’s rigid plates don’t sit on rock that stays put: they glide over the asthenosphere, a hot layer of the upper mantle that is solid but soft enough to flow very slowly, a little like Silly Putty. Its name comes from a Greek word meaning “weak.” Seismic waves slow down as they pass through it, and its slow flow lets land rise back up after the weight of ice-age glaciers melts away.",
    "answerHtml": "<b><u>Asthenosphere</u></b> (prompt on <u>upper mantle</u>, <u>mantle</u>, or <u>low-velocity zone</u>; do not accept “lithosphere” or “mesosphere”)",
    "accept": [
        "asthenosphere",
        "the asthenosphere",
        "earths asthenosphere"
    ],
    "prompt": [
        "upper mantle",
        "the upper mantle",
        "mantle",
        "the mantle",
        "earths mantle",
        "low velocity zone"
    ],
    "reject": [
        "lithosphere",
        "mesosphere",
        "lower mantle",
        "crust",
        "earths crust",
        "core",
        "earths core",
        "outer core",
        "inner core",
        "mohorovicic discontinuity",
        "moho",
        "transition zone",
        "lithosphere asthenosphere boundary",
        "stratosphere",
        "troposphere",
        "ionosphere",
        "thermosphere",
        "atmosphere",
        "hydrosphere",
        "biosphere",
        "magma",
        "plate tectonics",
        "tectonic plates"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Asthenosphere",
    "qb": {
        "q": "asthenosphere",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "Geologist Joseph Barrell named this layer in 1914 in a series of papers on the strength of Earth’s crust, arguing that a strong outer shell must rest on something much weaker. Rock from this layer partly melts as it rises beneath mid-ocean ridges.",
            "r": "Its name comes from a Greek word meaning “weak.” For 10 points, name this soft, slowly flowing layer of the upper mantle that lies just beneath the lithosphere."
        },
        {
            "p": "Clarence Dutton coined the word isostasy for the balance in which Earth’s rigid outer shell rests on this layer, like a block of wood floating in water. The heavy volcanoes of Hawaii press the seafloor down into this layer, so the islands slowly sink.",
            "r": "Earth’s tectonic plates glide over this layer. For 10 points, name this soft, flowing region of the upper mantle."
        },
        {
            "p": "Olivine crystals in this layer tend to line up with the direction in which the seafloor above it is moving, so seismic waves race through it faster in some directions than in others, an effect called seismic anisotropy [“an-eye-SOT-ruh-pee”].",
            "r": "Seismic waves also slow down in this layer’s low-velocity zone. For 10 points, name this weak, plastic layer of the upper mantle beneath the lithosphere."
        },
        {
            "p": "Beneath mid-ocean ridges, hot rock from this layer rises and partly melts as the pressure on it drops, producing the magma that hardens into new seafloor. This layer comes closest to Earth’s surface under those ridges.",
            "r": "Slow convection currents in this layer help carry the plates along. For 10 points, name this soft, flowing layer of the upper mantle."
        },
        {
            "p": "This layer’s upper boundary is set mainly by temperature rather than by any change in rock type: above it, cooler rock is stiff and strong, while below it, hotter rock of the same kind turns soft enough to flow.",
            "r": "That stiff rock above, together with the crust, forms the lithosphere. For 10 points, name this layer of the upper mantle on which tectonic plates move."
        },
        {
            "p": "Unlike the crust and the mantle, which are defined by what they are made of, this layer is defined by how its rock behaves, making it a “mechanical” layer of Earth along with the lithosphere above it.",
            "r": "Some textbooks call the stiffer rock beneath it the mesosphere. For 10 points, name this soft, plastic layer of the upper mantle."
        },
        {
            "p": "Like the rest of the upper mantle, this layer is made mostly of peridotite [“puh-RID-uh-tite”], a dense, green, olivine-rich rock. The same rock makes up the stiffer bottom of the lithosphere above it, but there it is cooler and stronger.",
            "r": "A tiny fraction of this layer’s rock may be melted. For 10 points, name this weak layer of the upper mantle that tectonic plates ride on."
        },
        {
            "p": "As ocean floor moves away from a ridge and cools, rock from the top of this layer stiffens and joins the lithosphere, so the oldest seafloor has the thickest lithosphere. That cooling also makes old seafloor sit deeper than young seafloor.",
            "r": "Its name comes from a Greek word for “weak.” For 10 points, name this soft, slowly flowing layer of the upper mantle."
        },
        {
            "p": "Ordinary earthquakes rarely start in this layer, because its hot rock bends and flows instead of snapping. The deep earthquakes that do strike at its depths happen inside cold slabs of ocean floor sinking down through it.",
            "r": "Rock in this layer is often compared to Silly Putty or warm tar. For 10 points, name this plastic layer of the upper mantle beneath the lithosphere."
        },
        {
            "p": "Land around the Gulf of Bothnia, between Sweden and Finland, is still rising almost a centimeter a year, because rock in this layer is slowly flowing back after the weight of an ice-age ice sheet melted away.",
            "r": "Land around Canada’s Hudson Bay is rising for the same reason. For 10 points, name this soft, flowing layer of the upper mantle."
        },
        {
            "p": "The ancient shorelines of Utah’s Lake Bonneville bulge upward near the middle of the old lake, because the land rose as rock in this layer crept back after the water drained. Grove Karl Gilbert studied those bent shorelines.",
            "r": "The rigid lithosphere floats on this layer in a balance called isostasy. For 10 points, name this layer of the upper mantle."
        },
        {
            "p": "The enormous weight of Hawaii’s volcanoes bends the seafloor down into this layer, so the islands slowly sink and a moat-like trough surrounds them. That bending is possible because rock in this layer slowly gives way beneath them.",
            "r": "Earth’s tectonic plates glide over this layer. For 10 points, name this soft region of the upper mantle beneath the lithosphere."
        },
        {
            "p": "Seismic S-waves slow down sharply in the upper part of this layer, called the low-velocity zone, a sign that its rock is hot, soft, and possibly very slightly melted. Its top lies roughly 100 kilometers down, and deeper beneath old continents.",
            "r": "Tectonic plates slide over it. For 10 points, name this layer whose name comes from the Greek word for “weak.”"
        },
        {
            "p": "Some textbooks divide Earth by stiffness into the lithosphere, this layer, and a stronger zone below it called the mesosphere, which shares its name with a layer of the atmosphere. Hot plumes of rock push up through this layer beneath hotspots like Iceland.",
            "r": "Slow convection currents in this layer help move the plates above. For 10 points, name this soft, plastic layer of the upper mantle."
        },
        {
            "p": "Rock in this layer is solid, but it is so hot that over thousands of years it flows like Silly Putty or warm tar, bending instead of breaking. Geologists call rock that behaves this way plastic or ductile.",
            "r": "Earth’s rigid lithosphere rides on top of it. For 10 points, name this soft layer of the upper mantle, whose name comes from the Greek for “weak.”"
        }
    ],
    "clues": [
        {
            "id": "soft-layer",
            "tier": "giveaway",
            "t": "A hot, soft layer of the upper mantle that is solid but flows very slowly",
            "k": ["upper mantle", "flows", "soft"],
            "n": 0,
            "rabbit": "Mantle"
        },
        {
            "id": "below-lithosphere",
            "tier": "giveaway",
            "t": "Lies just beneath the rigid lithosphere, which is the crust plus the stiff top of the mantle",
            "k": ["lithosphere", "rigid"],
            "n": 0
        },
        {
            "id": "plates-ride",
            "tier": "giveaway",
            "t": "Earth’s tectonic plates glide over it",
            "k": ["tectonic plates", "glide"],
            "n": 0,
            "rabbit": "Plate tectonics"
        },
        {
            "id": "greek-weak",
            "tier": "giveaway",
            "t": "Its name comes from a Greek word meaning “weak” or “without strength”",
            "k": ["greek", "weak"],
            "n": 0
        },
        {
            "id": "plastic-putty",
            "tier": "middle",
            "t": "Its rock is plastic, or ductile: it bends and flows instead of breaking, and is often compared to Silly Putty or warm tar",
            "k": ["plastic", "ductile", "silly putty"],
            "n": 0
        },
        {
            "id": "convection",
            "tier": "middle",
            "t": "Slow convection currents in it help carry the plates along",
            "k": ["convection"],
            "n": 0
        },
        {
            "id": "low-velocity",
            "tier": "middle",
            "t": "Seismic waves, especially S-waves, slow down in its upper part, the low-velocity zone",
            "k": ["low-velocity zone", "s-waves"],
            "n": 0
        },
        {
            "id": "partial-melt",
            "tier": "middle",
            "t": "Nearly all of its rock is solid, but a tiny fraction may be melted, which helps make it weak",
            "k": ["melted", "tiny fraction"],
            "n": 0
        },
        {
            "id": "mesosphere",
            "tier": "middle",
            "t": "Some textbooks call the stiffer rock below it the mesosphere, the same name as a layer of the atmosphere",
            "k": ["mesosphere", "stiffer"],
            "n": 0
        },
        {
            "id": "isostasy",
            "tier": "middle",
            "t": "The lithosphere floats on it in a balance called isostasy, like a block of wood floating in water",
            "k": ["isostasy", "floats"],
            "n": 0
        },
        {
            "id": "rebound",
            "tier": "middle",
            "t": "Its slow flow lets land rise back up after ice-age ice sheets melt, as around Canada’s Hudson Bay",
            "k": ["hudson bay", "ice sheets", "rise"],
            "n": 0,
            "rabbit": "Glaciers"
        },
        {
            "id": "depth",
            "tier": "middle",
            "t": "Its top lies roughly 100 kilometers down: shallower under mid-ocean ridges and deeper under old continents",
            "k": ["100 kilometers", "old continents"],
            "n": 0
        },
        {
            "id": "plumes",
            "tier": "middle",
            "t": "Hot plumes of rock rising through the mantle push up through it beneath hotspots like Iceland and Hawaii",
            "k": ["plumes", "hotspots"],
            "n": 0
        },
        {
            "id": "barrell",
            "tier": "power",
            "t": "Named in 1914 by geologist Joseph Barrell, in papers on the strength of Earth’s crust",
            "k": ["joseph barrell", "barrell", "1914"],
            "n": 0
        },
        {
            "id": "dutton",
            "tier": "power",
            "t": "Clarence Dutton coined the word “isostasy” for the floating balance of the rigid shell above it",
            "k": ["clarence dutton", "dutton"],
            "n": 0
        },
        {
            "id": "anisotropy",
            "tier": "power",
            "t": "Its olivine crystals line up with the direction the seafloor above is moving, so seismic waves travel faster in some directions: seismic anisotropy",
            "k": ["anisotropy", "olivine crystals", "line up"],
            "n": 0
        },
        {
            "id": "decompression",
            "tier": "power",
            "t": "Beneath mid-ocean ridges, its rock rises and partly melts as the pressure drops, making the magma for new seafloor",
            "k": ["mid-ocean ridges", "partly melts", "pressure"],
            "n": 0,
            "rabbit": "Seafloor spreading"
        },
        {
            "id": "temperature-boundary",
            "tier": "power",
            "t": "Its top boundary is set by temperature, not rock type: the same rock is stiff when cooler above and soft when hotter below",
            "k": ["temperature", "rock type"],
            "n": 0
        },
        {
            "id": "mechanical",
            "tier": "power",
            "t": "A “mechanical” layer, defined by how its rock behaves, unlike the crust and mantle, which are defined by what they are made of",
            "k": ["mechanical", "behaves"],
            "n": 0
        },
        {
            "id": "peridotite",
            "tier": "power",
            "t": "Made mostly of peridotite [“puh-RID-uh-tite”], a dense, green, olivine-rich rock",
            "k": ["peridotite", "olivine"],
            "n": 0,
            "rabbit": "Olivine"
        },
        {
            "id": "thickening",
            "tier": "power",
            "t": "As seafloor ages and cools, rock from its top stiffens and joins the lithosphere, so the oldest seafloor has the thickest lithosphere",
            "k": ["oldest seafloor", "thickest", "cools"],
            "n": 0
        },
        {
            "id": "quakes",
            "tier": "power",
            "t": "Ordinary earthquakes rarely start in it because its rock bends instead of snapping; deep quakes strike only inside cold sinking slabs",
            "k": ["earthquakes", "slabs", "snapping"],
            "n": 0,
            "rabbit": "Earthquakes"
        },
        {
            "id": "bothnia",
            "tier": "power",
            "t": "Land around the Gulf of Bothnia, between Sweden and Finland, is still rising almost a centimeter a year as rock in it flows back",
            "k": ["gulf of bothnia", "bothnia", "centimeter"],
            "n": 0
        },
        {
            "id": "bonneville",
            "tier": "power",
            "t": "Utah’s ancient Lake Bonneville shorelines, studied by G. K. Gilbert, bulge upward where the land rose after the lake drained",
            "k": ["lake bonneville", "bonneville", "gilbert"],
            "n": 0
        },
        {
            "id": "hawaii-sinking",
            "tier": "power",
            "t": "Hawaii’s heavy volcanoes bend the seafloor down into it, so the islands slowly sink inside a moat-like trough",
            "k": ["hawaii", "moat", "sink"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Asthenosphere or lithosphere?",
        "body": "Both names end in “-sphere,” and the two layers sit right on top of each other. The lithosphere is the rigid outer shell (the crust plus the stiff top of the mantle) that is broken into tectonic plates, while the asthenosphere is the soft, slowly flowing layer just beneath it that the plates ride on. Players also answer “mantle,” which is too broad, because the asthenosphere is only one part of the upper mantle.",
        "fix": "Rigid, brittle, broken into plates, or includes the crust means lithosphere. Soft, plastic, flowing, Greek for “weak,” the low-velocity zone, or the layer the plates glide on means asthenosphere. “Upper mantle” or “mantle” earns only a prompt, and the mesosphere is the stiffer zone below it (or a layer of the atmosphere).",
        "line": "Real answer line: <b><u>Asthenosphere</u></b> (prompt on upper mantle or mantle; do not accept “lithosphere” or “mesosphere”)"
    },
    "tests": {
        "right": ["Asthenosphere", "the asthenosphere", "Asthenosfere", "astenosphere"],
        "prompt": ["Upper mantle", "Mantle"],
        "wrong": ["Lithosphere", "Mesosphere", "Lower mantle", "Crust", "Outer core", "Stratosphere"]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
