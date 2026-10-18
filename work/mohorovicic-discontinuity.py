import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "mohorovicic-discontinuity",
    "name": "Mohorovičić discontinuity",
    "mono": "MOH",
    "category": "Earth Science",
    "qbCategory": "Science · Other Science (Earth Science)",
    "kicker": "Boundary between Earth’s crust and mantle · Found by seismology in 1909",
    "dates": "Discovered 1909",
    "briefing": "In 1909, the Croatian scientist Andrija Mohorovičić noticed that waves from an earthquake near Zagreb reached faraway stations sooner than expected, as if they had sped up underground. He had found the boundary where Earth’s crust ends and the denser mantle begins, now called the Mohorovičić discontinuity, or “Moho.” It lies only about 5 to 10 kilometers below the ocean floor but much deeper under the continents.",
    "answerHtml": "<b><u>Mohorovičić discontinuity</u></b> (accept <u>Moho</u> or <u>crust–mantle boundary</u>; prompt on <u>discontinuity</u> or <u>boundary</u>; do not accept “Gutenberg discontinuity,” “Conrad discontinuity,” or “Mohs scale”)",
    "accept": [
        "mohorovicic discontinuity",
        "mohorovicic",
        "moho",
        "moho discontinuity",
        "mohorovicic boundary",
        "moho boundary",
        "crust mantle boundary",
        "crust mantle discontinuity",
        "boundary between the crust and mantle",
        "boundary between the crust and the mantle"
    ],
    "prompt": [
        "discontinuity",
        "seismic discontinuity",
        "boundary",
        "seismic boundary"
    ],
    "reject": [
        "gutenberg discontinuity",
        "gutenberg",
        "lehmann discontinuity",
        "lehmann",
        "conrad discontinuity",
        "conrad",
        "repetti discontinuity",
        "core mantle boundary",
        "lithosphere",
        "asthenosphere",
        "low velocity zone",
        "transition zone",
        "d double prime",
        "shadow zone",
        "mohs",
        "mohs scale",
        "mohs hardness scale",
        "mohole",
        "project mohole",
        "kola superdeep borehole",
        "moon",
        "the moon"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Mohorovi%C4%8Di%C4%87_discontinuity",
    "qb": {
        "q": "Mohorovicic",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "Novelist John Steinbeck wrote a _Life_ magazine article about a 1961 test drilling for a project that hoped to bore through the ocean floor all the way to this boundary. Congress canceled that project, Project Mohole, in 1966.",
            "r": "Seismic waves speed up as they cross this boundary. For 10 points, name this boundary between Earth’s crust and mantle, discovered by a Croatian seismologist in 1909."
        },
        {
            "p": "Walter Munk and Harry Hess belonged to a joke-named group, the American Miscellaneous Society, that proposed drilling down to this boundary in 1957. Their project’s name combined this boundary’s nickname with the word “hole.”",
            "r": "This boundary lies only about 5 to 10 kilometers below the ocean floor. For 10 points, name this boundary between Earth’s crust and mantle."
        },
        {
            "p": "In 1961, the drilling barge CUSS I bored test holes into the Pacific seafloor off Mexico’s Guadalupe Island, the first step of a failed attempt to reach this boundary. Those holes passed through seafloor mud and into hard basalt.",
            "r": "Below this boundary lies dense, olivine-rich peridotite. For 10 points, name this boundary where Earth’s crust ends and the mantle begins."
        },
        {
            "p": "Drillers trying to reach this boundary in 1961 pioneered dynamic positioning, using propellers instead of anchors to hold a ship steady over deep water. Japan’s drilling ship Chikyu, which holds itself in place the same way, was built with the goal of drilling through this boundary.",
            "r": "This boundary is much deeper beneath continents than beneath the ocean floor. For 10 points, name this boundary between Earth’s crust and mantle."
        },
        {
            "p": "In Oman’s Samail ophiolite, a huge slice of ancient seafloor shoved up onto land, geologists can walk across this boundary, stepping from gabbro onto peridotite. Such exposures are rare, because this boundary is usually buried kilometers deep.",
            "r": "Seismic waves speed up as they cross this boundary from the crust into the mantle. For 10 points, name this boundary discovered in 1909 by a Croatian scientist."
        },
        {
            "p": "Japan’s deep-sea drilling ship Chikyu, whose name means “Earth,” was designed with the goal of drilling all the way down to this boundary beneath the seafloor. No drill has ever reached this boundary.",
            "r": "Below this boundary, P-waves jump to about 8 kilometers per second. For 10 points, name this boundary between Earth’s crust and mantle."
        },
        {
            "p": "Seismologists call P-waves that race along just beneath this boundary head waves and label them Pn. At faraway stations, those waves arrive before waves that take the shorter route through the rock above it.",
            "r": "This boundary separates the crust from the mantle beneath it. For 10 points, name this boundary, which has a four-letter nickname."
        },
        {
            "p": "This boundary lies deepest beneath Tibet and the Himalayas, around 70 kilometers down, because tall mountains are held up by deep roots of light rock, much as most of an iceberg hides underwater.",
            "r": "Beneath the ocean floor, it lies only about 5 to 10 kilometers down. For 10 points, name this boundary between Earth’s crust and mantle."
        },
        {
            "p": "Seismometers left on the Moon by Apollo astronauts detected a lunar version of this boundary a few dozen kilometers below the surface. On Earth, the rock gabbro often lies just above this boundary beneath the oceans.",
            "r": "Seismic waves speed up sharply as they cross this boundary. For 10 points, name this boundary between Earth’s crust and mantle, discovered in 1909."
        },
        {
            "p": "Geologists distinguish a “seismic” version of this boundary, defined by a jump in the speed of earthquake waves, from a “petrologic” version, defined by a change in rock type. The two versions do not always line up exactly.",
            "r": "Below this boundary lies dense, olivine-rich peridotite. For 10 points, name this boundary where Earth’s crust ends and the mantle begins."
        },
        {
            "p": "This boundary’s discoverer was also a meteorologist who directed the weather observatory in Zagreb and equipped it with seismographs. He found this boundary by studying records of an October 1909 earthquake in the nearby Kupa Valley.",
            "r": "Seismic waves speed up as they cross this boundary. For 10 points, name this boundary between Earth’s crust and mantle, named for a Croatian scientist."
        },
        {
            "p": "The Soviet Union’s Kola Superdeep Borehole reached more than 12 kilometers down, making it the deepest hole ever drilled, yet it never came close to this boundary, which lies much deeper beneath continents.",
            "r": "Beneath the ocean floor, this boundary lies only about 5 to 10 kilometers down. For 10 points, name this boundary between Earth’s crust and mantle."
        },
        {
            "p": "Records of an October 1909 earthquake in Croatia’s Kupa Valley showed two sets of waves reaching distant stations: slower ones that had stayed in the shallow rock above this boundary, and faster ones that had dipped below it.",
            "r": "It is named for the Croatian seismologist who found it. For 10 points, name this boundary between Earth’s crust and mantle."
        },
        {
            "p": "P-waves speed up from roughly 6 or 7 kilometers per second to about 8 when they cross this boundary, a jump that reveals denser rock below. That denser rock is mostly olivine-rich peridotite.",
            "r": "This boundary lies much deeper beneath continents than beneath the ocean floor. For 10 points, name this boundary between Earth’s crust and mantle."
        },
        {
            "p": "This boundary lies within the rigid lithosphere rather than at its base, so moving plates carry it along with them. Granite and basalt are common just above this boundary, while dense, olivine-rich peridotite lies just below it.",
            "r": "Seismic waves speed up as they cross it. For 10 points, name this boundary between Earth’s crust and mantle, discovered by a Croatian seismologist in 1909."
        }
    ],
    "clues": [
        {
            "id": "crust-mantle",
            "tier": "giveaway",
            "t": "The boundary between Earth’s crust and the mantle beneath it",
            "k": ["crust", "mantle", "boundary"],
            "n": 0,
            "rabbit": "Mantle"
        },
        {
            "id": "croatian-1909",
            "tier": "giveaway",
            "t": "Discovered in 1909 by the Croatian seismologist it is named after",
            "k": ["croatian", "1909", "seismologist"],
            "n": 0
        },
        {
            "id": "speed-jump",
            "tier": "giveaway",
            "t": "Seismic waves speed up sharply as they cross it from the crust into denser mantle rock",
            "k": ["seismic waves", "speed up", "denser"],
            "n": 0
        },
        {
            "id": "nickname",
            "tier": "giveaway",
            "t": "Usually called by a four-letter nickname made from the start of its discoverer’s last name",
            "k": ["four-letter", "nickname"],
            "n": 0
        },
        {
            "id": "kupa-quake",
            "tier": "middle",
            "t": "Found from records of an October 1909 earthquake in Croatia’s Kupa Valley, near Zagreb",
            "k": ["kupa", "zagreb", "earthquake"],
            "n": 0
        },
        {
            "id": "two-sets",
            "tier": "middle",
            "t": "Distant stations recorded two sets of waves: slower ones through the crust and faster ones that dipped below it",
            "k": ["two sets", "faster", "slower"],
            "n": 0
        },
        {
            "id": "eight-kps",
            "tier": "middle",
            "t": "P-waves jump from roughly 6 or 7 to about 8 kilometers per second below it",
            "k": ["kilometers per second", "p-waves"],
            "n": 0
        },
        {
            "id": "ocean-vs-continent",
            "tier": "middle",
            "t": "Only about 5 to 10 kilometers below the ocean floor, but around 35 kilometers down beneath most continents",
            "k": ["ocean floor", "continents", "35 kilometers"],
            "n": 0
        },
        {
            "id": "mountain-roots",
            "tier": "middle",
            "t": "Dips deepest beneath tall mountains, which rest on thick roots of crust, the way most of an iceberg hides underwater",
            "k": ["mountains", "roots", "iceberg"],
            "n": 0
        },
        {
            "id": "peridotite",
            "tier": "middle",
            "t": "Crustal rocks like granite, basalt, and gabbro lie above it; dense, olivine-rich peridotite lies below it",
            "k": ["peridotite", "olivine", "gabbro"],
            "n": 0,
            "rabbit": "Olivine"
        },
        {
            "id": "lithosphere",
            "tier": "middle",
            "t": "Lies inside the rigid lithosphere, which includes both the crust and the topmost mantle",
            "k": ["lithosphere", "topmost"],
            "n": 0,
            "rabbit": "Asthenosphere"
        },
        {
            "id": "project-mohole",
            "tier": "middle",
            "t": "Project Mohole tried to drill through the ocean floor to reach it until Congress canceled the project in 1966",
            "k": ["project mohole", "congress", "1966"],
            "n": 0
        },
        {
            "id": "kola",
            "tier": "middle",
            "t": "The Soviet Kola Superdeep Borehole, more than 12 kilometers deep, never came close to it",
            "k": ["kola", "superdeep", "borehole"],
            "n": 0
        },
        {
            "id": "steinbeck",
            "tier": "power",
            "t": "John Steinbeck wrote about Project Mohole’s 1961 test drilling for _Life_ magazine",
            "k": ["steinbeck", "life magazine"],
            "n": 0
        },
        {
            "id": "amsoc",
            "tier": "power",
            "t": "The joke-named American Miscellaneous Society, including Walter Munk and Harry Hess, proposed drilling to it in 1957",
            "k": ["american miscellaneous society", "walter munk", "harry hess"],
            "n": 0,
            "rabbit": "Seafloor spreading"
        },
        {
            "id": "guadalupe",
            "tier": "power",
            "t": "In 1961, the drilling barge CUSS I bored test holes off Mexico’s Guadalupe Island, passing through seafloor mud into basalt",
            "k": ["guadalupe island", "cuss i", "barge"],
            "n": 0
        },
        {
            "id": "dynamic-positioning",
            "tier": "power",
            "t": "The 1961 drilling pioneered dynamic positioning: propellers, not anchors, held the ship steady over deep water",
            "k": ["dynamic positioning", "propellers", "anchors"],
            "n": 0
        },
        {
            "id": "oman",
            "tier": "power",
            "t": "In Oman’s Samail ophiolite, a slice of old seafloor shoved onto land, geologists can walk across it",
            "k": ["oman", "samail", "ophiolite"],
            "n": 0
        },
        {
            "id": "chikyu",
            "tier": "power",
            "t": "Japan’s drilling ship Chikyu (“Earth”) was designed with the goal of drilling through it; no drill has ever reached it",
            "k": ["chikyu", "japan"],
            "n": 0
        },
        {
            "id": "head-waves",
            "tier": "power",
            "t": "P-waves racing just beneath it are called head waves and labeled Pn; they reach faraway stations first",
            "k": ["head waves", "pn"],
            "n": 0
        },
        {
            "id": "moon",
            "tier": "power",
            "t": "Seismometers left by Apollo astronauts found a lunar version a few dozen kilometers below the Moon’s surface",
            "k": ["apollo", "lunar", "seismometers"],
            "n": 0
        },
        {
            "id": "petrologic",
            "tier": "power",
            "t": "A “seismic” version is defined by wave speed and a “petrologic” version by rock type; the two do not always line up",
            "k": ["petrologic", "seismic"],
            "n": 0
        },
        {
            "id": "observatory",
            "tier": "power",
            "t": "Its discoverer was also a meteorologist who directed Zagreb’s weather observatory and equipped it with seismographs",
            "k": ["meteorologist", "observatory", "seismographs"],
            "n": 0
        },
        {
            "id": "tibet",
            "tier": "power",
            "t": "Deepest of all beneath Tibet and the Himalayas, around 70 kilometers down, where the crust is about twice its usual thickness",
            "k": ["tibet", "himalayas", "70 kilometers"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Which boundary is which?",
        "body": "Earth’s interior has several named boundaries, and quiz bowl asks about each one. The Mohorovičić discontinuity (Moho) separates the crust from the mantle, the Gutenberg discontinuity separates the mantle from the outer core about 2,900 kilometers down, and the Conrad discontinuity lies inside the continental crust. Players also mix up the Moho with the Mohs hardness scale, which ranks minerals and has nothing to do with Earth’s layers.",
        "fix": "Crust above and mantle below, 1909, a Croatian scientist, Project Mohole, or waves jumping to about 8 kilometers per second mean the Moho. The core, the S-wave shadow zone, or about 2,900 kilometers down mean the Gutenberg discontinuity. Saying only “discontinuity” earns a prompt.",
        "line": "Real answer line: <b><u>Mohorovičić discontinuity</u></b> (accept <u>Moho</u>; prompt on discontinuity; do not accept “Gutenberg discontinuity”)"
    },
    "tests": {
        "right": ["Mohorovičić discontinuity", "Moho", "the Moho", "Mohorovicic discontinuity", "Mohorovicic discontinuty", "crust-mantle boundary"],
        "prompt": ["discontinuity", "boundary"],
        "wrong": ["Gutenberg discontinuity", "Lehmann discontinuity", "Mantle", "Crust", "Mohs scale", "Project Mohole", "Lithosphere"]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
