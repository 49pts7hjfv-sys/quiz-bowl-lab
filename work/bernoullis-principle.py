import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "bernoullis-principle",
    "name": "Bernoulli’s principle",
    "mono": "BER",
    "category": "Physics",
    "qbCategory": "Science · Physics",
    "kicker": "Faster flow means lower pressure · A key idea behind airplane lift",
    "dates": "Published by Daniel Bernoulli in 1738",
    "briefing": "Bernoulli’s principle says that when a fluid such as air or water speeds up, its pressure drops. The Swiss scientist Daniel Bernoulli published the idea in his 1738 book _Hydrodynamica_. It helps explain how airplane wings get lift, how perfume sprayers pull up liquid, and why a ping-pong ball can float in the stream from a hair dryer.",
    "answerHtml": "<b><u>Bernoulli’s principle</u></b> (accept <u>Bernoulli’s equation</u>, <u>Bernoulli’s law</u>, or <u>Bernoulli effect</u>; prompt on <u>Bernoulli</u>; do not accept “Venturi effect”)",
    "accept": [
        "bernoullis principle",
        "bernoulli principle",
        "bernoullis equation",
        "bernoulli equation",
        "bernoullis law",
        "bernoulli law",
        "bernoulli effect",
        "bernoullis effect",
        "bernoullis theorem",
        "bernoulli theorem",
        "principle of bernoulli"
    ],
    "prompt": [
        "bernoulli",
        "daniel bernoulli"
    ],
    "reject": [
        "venturi effect",
        "venturi",
        "pascals principle",
        "pascals law",
        "pascal principle",
        "archimedes principle",
        "archimedes",
        "buoyancy",
        "magnus effect",
        "coanda effect",
        "torricellis law",
        "continuity equation",
        "equation of continuity",
        "navier stokes equations",
        "bernoulli numbers",
        "bernoulli distribution",
        "bernoulli trial",
        "lift",
        "drag",
        "pressure",
        "boyles law"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Bernoulli%27s_principle",
    "qb": {
        "q": "Bernoulli",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "The 1738 book that introduced this principle, _Hydrodynamica_, also argued that a gas pushes on its container because countless tiny particles keep hitting the walls, an early version of the kinetic theory of gases. That book’s author came from a famous family of mathematicians.",
            "r": "For 10 points, name this principle stating that a fluid’s pressure drops as its speed increases."
        },
        {
            "p": "Leonhard Euler [“OY-ler”] wrote this principle’s equation in its modern form, which applies along a streamline in a steady, incompressible flow with no viscosity. That equation says pressure plus one-half density times speed squared plus density times g times height stays constant.",
            "r": "For 10 points, name this rule of fluid dynamics, which says that faster-moving fluids have lower pressure."
        },
        {
            "p": "This principle’s namesake had a bitter rivalry with his own father, Johann, who wrote a competing book called _Hydraulica_ and dated it earlier than his son’s. The son’s book, _Hydrodynamica_, came out in 1738.",
            "r": "It helps explain airplane lift. For 10 points, name this principle stating that when a fluid flows faster, its pressure falls."
        },
        {
            "p": "The “equal transit time” fallacy is a popular but wrong argument based on this principle, which claims that air flowing over the top of an airfoil must meet the air from below at the back edge. In reality, the air over the top arrives first.",
            "r": "For 10 points, name this principle of fluids, which helps explain airplane lift by linking faster flow to lower pressure."
        },
        {
            "p": "In the 1730s, Henri Pitot [“PEE-toh”] invented a tube to measure the speed of river water. Airplanes use such tubes, along with this principle, to find their airspeed by comparing the pressure of air rammed to a stop in the tube with that of the air flowing past.",
            "r": "Perfume sprayers also rely on it. For 10 points, name this principle stating that faster-moving fluids exert less pressure."
        },
        {
            "p": "A law named for Evangelista Torricelli [“tor-ih-CHEL-ee”] says that water leaks from a hole in a tank at the speed it would reach falling from the water’s surface, and it can be derived from this principle. This principle is really conservation of energy for a moving fluid.",
            "r": "For 10 points, name this principle stating that a fluid’s pressure drops when its speed increases."
        },
        {
            "p": "A Venturi meter uses this principle to find a liquid’s speed by comparing the pressure in a wide part of a pipe with that in a narrow throat, where the liquid moves faster. A carburetor uses the same effect to pull fuel into a stream of air.",
            "r": "For 10 points, name this principle, published in 1738, which says that faster fluids have lower pressure."
        },
        {
            "p": "A 1911 collision between the warship HMS _Hawke_ and the ocean liner _Olympic_, sister ship of the _Titanic_, was blamed on suction explained by this principle. Two ships sailing close together can be pulled toward each other for the same reason.",
            "r": "For 10 points, name this principle stating that fast-moving fluids, like the water squeezed between the ships, have lower pressure."
        },
        {
            "p": "Engineers often write this principle in terms of “head,” saying that pressure head, velocity head, and elevation head add up to a constant total for an ideal fluid. The principle holds exactly only for a fluid with no viscosity that cannot be compressed.",
            "r": "Perfume atomizers use it to draw liquid up a thin tube. For 10 points, name this principle linking faster fluid speed to lower pressure."
        },
        {
            "p": "A water aspirator in a chemistry lab uses this principle, pulling air out of a flask with a fast jet of water. Race cars carry upside-down wings so that this principle presses them onto the track, a push called downforce.",
            "r": "For 10 points, name this principle that explains how airplane wings get lift, because faster-moving air has lower pressure."
        },
        {
            "p": "This principle is often used with the continuity equation, which says that a fluid in a pipe speeds up wherever the pipe gets narrower, since area times speed stays the same. Blowing between two empty soda cans makes them roll toward each other because of this principle.",
            "r": "It helps explain how airplanes fly. For 10 points, name this principle that says faster-moving fluids exert less pressure."
        },
        {
            "p": "Blowing hard through an upside-down funnel can hold a ping-pong ball inside instead of pushing it out, and a ping-pong ball can hover in the stream of a hair dryer; both tricks are classroom demonstrations of this principle.",
            "r": "For 10 points, name this principle of fluid flow, published by a Swiss scientist in 1738, which helps explain airplane lift."
        },
        {
            "p": "In this principle’s equation, one-half times density times speed squared is called dynamic pressure; adding it to the static pressure gives the total, or stagnation, pressure. Because of this principle, strong hurricane winds racing over a roof can help lift it off a house.",
            "r": "Wind blowing across a chimney top helps draw smoke up for the same reason. For 10 points, name this principle linking faster fluid flow to lower pressure."
        },
        {
            "p": "In a Bunsen burner, gas rushing out of a narrow jet pulls air in through holes near the bottom of the barrel, thanks to this principle. Many airbrushes use a fast stream of air to pull paint up from a cup in a similar way.",
            "r": "This principle is named for a Swiss scientist. For 10 points, name this principle stating that faster-moving fluids have lower pressure."
        },
        {
            "p": "This principle’s namesake, who trained as a doctor, later used mathematics to argue that inoculating people against smallpox would save lives. He described this principle in his 1738 book _Hydrodynamica_, and his father and uncle were also famous mathematicians.",
            "r": "For 10 points, name this principle, which says that when a fluid speeds up, its pressure drops."
        }
    ],
    "clues": [
        {
            "id": "statement",
            "tier": "giveaway",
            "t": "When a fluid such as air or water speeds up, its pressure drops",
            "k": ["speeds up", "pressure drops", "fluid"],
            "n": 0
        },
        {
            "id": "lift",
            "tier": "giveaway",
            "t": "Helps explain how airplane wings get lift: faster air over the curved top has lower pressure",
            "k": ["airplane wings", "lift", "curved top"],
            "n": 0
        },
        {
            "id": "swiss-namesake",
            "tier": "giveaway",
            "t": "Named for a Swiss scientist",
            "k": ["swiss scientist", "swiss"],
            "n": 0
        },
        {
            "id": "hydrodynamica",
            "tier": "middle",
            "t": "Its namesake published it in his 1738 book _Hydrodynamica_",
            "k": ["hydrodynamica", "1738"],
            "n": 0
        },
        {
            "id": "energy",
            "tier": "middle",
            "t": "It is conservation of energy for a moving fluid",
            "k": ["conservation of energy", "moving fluid"],
            "n": 0,
            "rabbit": "Energy"
        },
        {
            "id": "equation",
            "tier": "middle",
            "t": "Its equation: pressure + ½ × density × speed² + density × g × height stays constant along a streamline",
            "k": ["streamline", "density", "constant"],
            "n": 0
        },
        {
            "id": "ideal-fluid",
            "tier": "middle",
            "t": "Holds exactly only for steady flow of a fluid with no viscosity that cannot be compressed",
            "k": ["viscosity", "steady flow", "compressed"],
            "n": 0,
            "rabbit": "Viscosity"
        },
        {
            "id": "atomizers",
            "tier": "middle",
            "t": "Perfume atomizers use it: air rushing across the top of a thin tube draws liquid up and sprays it as a mist",
            "k": ["atomizers", "thin tube", "perfume"],
            "n": 0
        },
        {
            "id": "venturi",
            "tier": "middle",
            "t": "Venturi effect: a fluid speeds up and its pressure drops in a narrow part of a pipe; Venturi meters and carburetors use it",
            "k": ["venturi", "carburetors", "narrow"],
            "n": 0,
            "rabbit": "Venturi effect"
        },
        {
            "id": "ships",
            "tier": "middle",
            "t": "Two ships sailing close together can be pulled toward each other",
            "k": ["two ships", "pulled"],
            "n": 0
        },
        {
            "id": "ping-pong",
            "tier": "middle",
            "t": "A ping-pong ball hovers in a hair dryer’s stream and stays inside an upside-down funnel when you blow through it",
            "k": ["ping-pong ball", "hair dryer", "funnel"],
            "n": 0
        },
        {
            "id": "soda-cans",
            "tier": "middle",
            "t": "Blowing between two empty soda cans makes them roll toward each other",
            "k": ["soda cans", "roll"],
            "n": 0
        },
        {
            "id": "roofs",
            "tier": "middle",
            "t": "Hurricane winds racing over a roof can help lift it off; wind across a chimney top helps draw smoke up",
            "k": ["hurricane", "roof", "chimney"],
            "n": 0
        },
        {
            "id": "downforce",
            "tier": "power",
            "t": "Race cars use upside-down wings that press them onto the track, a push called downforce",
            "k": ["downforce", "upside-down wings", "race cars"],
            "n": 0
        },
        {
            "id": "kinetic-theory",
            "tier": "power",
            "t": "_Hydrodynamica_ also explained gas pressure as countless tiny particles hitting a container’s walls, an early kinetic theory of gases",
            "k": ["kinetic theory", "gas pressure", "particles"],
            "n": 0
        },
        {
            "id": "euler",
            "tier": "power",
            "t": "Leonhard Euler wrote its equation in its modern form",
            "k": ["leonhard euler", "modern form"],
            "n": 0,
            "rabbit": "Leonhard Euler"
        },
        {
            "id": "hydraulica",
            "tier": "power",
            "t": "Its namesake’s father, Johann, wrote a rival book, _Hydraulica_, and dated it earlier than his son’s; his uncle was also a famous mathematician",
            "k": ["hydraulica", "johann", "rival"],
            "n": 0
        },
        {
            "id": "equal-transit",
            "tier": "power",
            "t": "The “equal transit time” fallacy wrongly says air over an airfoil’s top must meet the air from below at the back edge; the top air arrives first",
            "k": ["equal transit time", "fallacy", "airfoil"],
            "n": 0
        },
        {
            "id": "pitot",
            "tier": "power",
            "t": "Henri Pitot’s tube (1730s) measured the speed of river water; airplanes use such tubes to find their airspeed",
            "k": ["pitot", "airspeed", "1730s"],
            "n": 0
        },
        {
            "id": "torricelli",
            "tier": "power",
            "t": "Torricelli’s law for the speed of water leaking from a hole in a tank can be derived from it",
            "k": ["torricelli", "leaking", "tank"],
            "n": 0
        },
        {
            "id": "head",
            "tier": "power",
            "t": "Engineers write it as pressure head plus velocity head plus elevation head equals a constant total",
            "k": ["pressure head", "velocity head", "elevation head"],
            "n": 0
        },
        {
            "id": "olympic-hawke",
            "tier": "power",
            "t": "A 1911 collision between HMS _Hawke_ and the liner _Olympic_, the _Titanic_’s sister ship, was blamed on suction it explains",
            "k": ["hawke", "olympic", "1911", "titanic"],
            "n": 0
        },
        {
            "id": "aspirator",
            "tier": "power",
            "t": "A lab water aspirator uses a fast jet of water to pull air out of a flask",
            "k": ["aspirator", "flask", "jet of water"],
            "n": 0
        },
        {
            "id": "continuity",
            "tier": "power",
            "t": "Often paired with the continuity equation: area times speed stays the same, so a fluid speeds up in a narrower pipe",
            "k": ["continuity equation", "area times speed", "narrower"],
            "n": 0
        },
        {
            "id": "dynamic-pressure",
            "tier": "power",
            "t": "One-half × density × speed² is the dynamic pressure; adding the static pressure gives the stagnation pressure",
            "k": ["dynamic pressure", "stagnation", "static pressure"],
            "n": 0,
            "rabbit": "Pressure"
        },
        {
            "id": "bunsen",
            "tier": "power",
            "t": "A Bunsen burner’s gas jet pulls air in through holes near the bottom of the barrel; many airbrushes pull up paint the same way",
            "k": ["bunsen burner", "airbrushes", "holes"],
            "n": 0
        },
        {
            "id": "smallpox",
            "tier": "power",
            "t": "Its namesake trained as a doctor and used mathematics to argue that smallpox inoculation would save lives",
            "k": ["smallpox", "inoculation", "doctor"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Not Pascal or Venturi",
        "body": "Several fluid answer lines sound alike. Pascal’s principle says pressure applied to a trapped fluid spreads equally in all directions, as in hydraulic lifts, and Archimedes’ principle is about buoyancy and floating. The Venturi effect is a special case of this principle in a narrowing pipe, and the Magnus effect is what curves a spinning ball, so real answer lines may refuse those names.",
        "fix": "Speed and pressure trading off, wings, sprayers, Pitot tubes, or _Hydrodynamica_ mean this principle. Hydraulic jacks and brakes mean Pascal; floating and displaced water mean Archimedes; a spinning, curving ball means the Magnus effect; and saying just “Bernoulli” earns only a prompt.",
        "line": "Real answer line: <b><u>Bernoulli’s principle</u></b> (accept <u>Bernoulli’s equation</u>, <u>Bernoulli’s law</u>, or <u>Bernoulli effect</u>; prompt on <u>Bernoulli</u>; do not accept “Venturi effect”)"
    },
    "tests": {
        "right": [
            "Bernoulli's principle",
            "Bernoulli principle",
            "Bernoulli's equation",
            "Bernoulli effect",
            "Bernouli's principle"
        ],
        "prompt": [
            "Bernoulli",
            "Daniel Bernoulli"
        ],
        "wrong": [
            "Venturi effect",
            "Pascal's principle",
            "Archimedes' principle",
            "Magnus effect",
            "Bernoulli numbers"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
