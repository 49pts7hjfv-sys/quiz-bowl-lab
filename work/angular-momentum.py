import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "angular-momentum",
    "name": "Angular momentum",
    "mono": "L",
    "category": "Physics",
    "qbCategory": "Science · Physics",
    "kicker": "Rotation’s conserved quantity · Why skaters spin faster with arms in",
    "dates": "Kepler’s second law (1609) reflects its conservation",
    "briefing": "Angular momentum is the spinning version of momentum. It grows with an object’s mass, with how far that mass sits from the center, and with how fast the object turns. When no outside twist, or torque, acts on a system, its angular momentum stays the same, which is why a figure skater spins faster when she pulls in her arms. The same rule makes collapsing stars spin up and helps a spinning top stay upright.",
    "answerHtml": "<b><u>Angular momentum</u></b> (prompt on <u>L</u>; do not accept “linear momentum” or just “momentum”)",
    "accept": [
        "angular momentum",
        "angular momenta",
        "conservation of angular momentum",
        "law of conservation of angular momentum",
        "rotational momentum",
        "moment of momentum"
    ],
    "prompt": [
        "l"
    ],
    "reject": [
        "linear momentum",
        "torque",
        "moment of inertia",
        "rotational inertia",
        "angular velocity",
        "angular acceleration",
        "angular displacement",
        "angular impulse",
        "impulse",
        "precession",
        "spin"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Angular_momentum",
    "qb": {
        "q": "angular momentum",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "Emmy Noether’s [“NUR-terz”] theorem links the conservation of this quantity to the fact that the laws of physics work the same no matter which direction a system faces. The net torque on an object equals the rate at which this quantity changes over time.",
            "r": "A figure skater who pulls in her arms spins faster because this quantity is conserved. For 10 points, name this rotational quantity, equal to moment of inertia times angular velocity."
        },
        {
            "p": "In his 1913 model of the hydrogen atom, Niels Bohr assumed that the electron’s value of this quantity in each allowed orbit is a whole-number multiple of Planck’s constant divided by two pi. This quantity is a vector that points along the axis of rotation, following the right-hand rule.",
            "r": "For 10 points, name this quantity that a spinning object keeps constant unless an outside torque acts on it."
        },
        {
            "p": "In 1922, Otto Stern and Walther Gerlach [“GAIR-lahk”] sent silver atoms through an uneven magnetic field and saw the beam split in two, showing that this quantity can only line up in certain directions. The built-in form of this quantity carried by an electron is called spin.",
            "r": "Gymnasts tuck their bodies to flip faster because this quantity is conserved. For 10 points, name this rotational quantity, symbolized L."
        },
        {
            "p": "Kepler’s second law, which says a planet sweeps out equal areas in equal times, is really a consequence of the conservation of this quantity. Because this quantity stays fixed, a comet moves fastest when it swings closest to the Sun.",
            "r": "For 10 points, name this quantity, which equals moment of inertia times angular velocity and is symbolized L."
        },
        {
            "p": "Tides slowly transfer this quantity from Earth’s spin to the Moon’s orbit, which is why Earth’s days are getting longer and the Moon drifts about four centimeters farther away each year. A spinning top or gyroscope resists tipping over because of this quantity.",
            "r": "Ice skaters spin faster when they pull in their arms because it is conserved. For 10 points, name this rotational quantity, symbolized L."
        },
        {
            "p": "The Sun holds more than 99 percent of the Solar System’s mass but only a tiny share of this quantity, most of which is carried by Jupiter’s orbit. A cloud of gas collapsing to form a star spins faster and flattens into a disk because this quantity is conserved.",
            "r": "For 10 points, name this rotational quantity, symbolized L, that equals moment of inertia times angular velocity."
        },
        {
            "p": "When a giant star’s core collapses into a neutron star only about 20 kilometers across, conservation of this quantity makes the tiny star spin many times per second. A diver who tucks into a ball flips faster for the same reason.",
            "r": "It is symbolized L. For 10 points, name this quantity, the product of moment of inertia and angular velocity."
        },
        {
            "p": "This quantity has the same units as Planck’s constant, joule-seconds, which can also be written as kilogram meters squared per second. For a point mass, this quantity equals the cross product of its position vector with its mass times velocity.",
            "r": "For 10 points, name this quantity that explains why ice skaters spin faster when they pull in their arms."
        },
        {
            "p": "The azimuthal quantum number, written as a lowercase l, sets the size of an electron’s orbital value of this quantity and decides whether its orbital is s, p, d, or f. A helicopter needs a tail rotor because its body would otherwise spin opposite the main rotor to conserve this quantity.",
            "r": "Figure skaters spin faster by pulling in their arms because it is conserved. For 10 points, name this rotational quantity, symbolized L."
        },
        {
            "p": "Clebsch–Gordan [“KLEPSH GOR-dahn”] coefficients are used in quantum mechanics when two sources of this quantity, such as an electron’s orbit and its spin, are added together. A person sitting on a swivel stool who flips over a spinning bicycle wheel starts turning because this quantity is conserved.",
            "r": "For 10 points, name this rotational quantity, equal to moment of inertia times angular velocity."
        },
        {
            "p": "Gravity’s torque on a tilted spinning top changes the direction of this quantity instead of knocking the top over, so the top’s axis slowly circles in a motion called precession. A football thrown in a tight spiral flies steadily because of this quantity.",
            "r": "For 10 points, name this quantity, symbolized L, that a figure skater conserves while spinning."
        },
        {
            "p": "A falling cat can twist around to land on its feet even though its total of this quantity stays zero, by changing its body’s shape. A spacecraft can turn itself by spinning a reaction wheel the opposite way, since the total of this quantity must stay the same.",
            "r": "For 10 points, name this rotational quantity, symbolized L, that stays constant when no outside torque acts on a system."
        },
        {
            "p": "In the Einstein–de Haas effect, magnetizing a hanging iron cylinder makes it start to rotate, showing that the magnetism of electrons is tied to this quantity. In the absence of outside torques, this quantity is conserved.",
            "r": "For 10 points, name this quantity whose conservation explains Kepler’s second law and why spinning skaters speed up."
        },
        {
            "p": "Multiplying a torque by the time it acts gives the change in this quantity, an amount called angular impulse. For a rigid body turning about a fixed axis, this quantity equals the moment of inertia times the angular velocity.",
            "r": "Its conservation makes a figure skater spin faster when she pulls in her arms. For 10 points, name this quantity, symbolized L."
        },
        {
            "p": "The no-hair theorem says a black hole can be described completely by just three numbers: its mass, its electric charge, and this quantity. A rotating Kerr black hole has some of this quantity, while a Schwarzschild [“SHVARTS-shilt”] black hole has none.",
            "r": "For 10 points, name this quantity, symbolized L, which a spinning ice skater conserves."
        }
    ],
    "clues": [
        {
            "id": "skater",
            "tier": "giveaway",
            "t": "A figure skater spins faster when she pulls in her arms, because it stays constant",
            "k": ["figure skater", "pulls in", "arms"],
            "n": 0
        },
        {
            "id": "formula",
            "tier": "giveaway",
            "t": "Equals moment of inertia (I) times angular velocity (omega): L = Iω",
            "k": ["moment of inertia", "inertia", "omega"],
            "n": 0
        },
        {
            "id": "rotational-counterpart",
            "tier": "giveaway",
            "t": "Symbolized L; the rotational counterpart of mass times velocity",
            "k": ["rotational counterpart", "symbolized"],
            "n": 0,
            "rabbit": "Momentum"
        },
        {
            "id": "no-torque",
            "tier": "giveaway",
            "t": "Conserved whenever no net outside torque acts on a system",
            "k": ["torque", "conserved"],
            "n": 0,
            "rabbit": "Torque"
        },
        {
            "id": "torque-rate",
            "tier": "middle",
            "t": "Net torque equals its rate of change over time",
            "k": ["rate of change", "net torque"],
            "n": 0
        },
        {
            "id": "kepler",
            "tier": "middle",
            "t": "Its conservation explains Kepler’s second law (equal areas in equal times), so a comet moves fastest near the Sun",
            "k": ["kepler", "equal areas", "comet"],
            "n": 0,
            "rabbit": "Johannes Kepler"
        },
        {
            "id": "neutron-star",
            "tier": "middle",
            "t": "A collapsing star core becomes a fast-spinning neutron star (pulsar) because it is conserved",
            "k": ["neutron star", "pulsar", "collapsing"],
            "n": 0,
            "rabbit": "Neutron stars"
        },
        {
            "id": "vector",
            "tier": "middle",
            "t": "A vector pointing along the axis of rotation, found with the right-hand rule",
            "k": ["right-hand rule", "axis of rotation", "vector"],
            "n": 0
        },
        {
            "id": "gyroscope",
            "tier": "middle",
            "t": "Keeps spinning tops and gyroscopes from tipping; gravity’s torque makes them precess instead",
            "k": ["gyroscopes", "precess", "spinning tops"],
            "n": 0,
            "rabbit": "Precession"
        },
        {
            "id": "cross-product",
            "tier": "middle",
            "t": "For a point mass, the cross product of position and mass times velocity: L = r × p",
            "k": ["cross product", "position"],
            "n": 0
        },
        {
            "id": "diver",
            "tier": "middle",
            "t": "Divers and gymnasts tuck into a ball to flip faster",
            "k": ["divers", "gymnasts", "tuck"],
            "n": 0
        },
        {
            "id": "helicopter",
            "tier": "middle",
            "t": "A helicopter’s tail rotor keeps the body from spinning opposite the main rotor",
            "k": ["helicopter", "tail rotor"],
            "n": 0
        },
        {
            "id": "bicycle-wheel",
            "tier": "middle",
            "t": "Flipping a spinning bicycle wheel while sitting on a swivel stool makes you start turning",
            "k": ["bicycle wheel", "swivel stool"],
            "n": 0
        },
        {
            "id": "noether",
            "tier": "power",
            "t": "Emmy Noether’s theorem: its conservation comes from the laws of physics being the same in every direction",
            "k": ["noether", "every direction"],
            "n": 0
        },
        {
            "id": "bohr",
            "tier": "power",
            "t": "Niels Bohr’s 1913 model: an electron’s value is a whole-number multiple of h-bar (Planck’s constant over 2π)",
            "k": ["bohr", "1913", "h-bar"],
            "n": 0,
            "rabbit": "Niels Bohr"
        },
        {
            "id": "stern-gerlach",
            "tier": "power",
            "t": "Stern–Gerlach experiment (1922): a beam of silver atoms split in two, showing it can only line up in certain directions",
            "k": ["stern", "gerlach", "silver atoms", "1922"],
            "n": 0
        },
        {
            "id": "units",
            "tier": "power",
            "t": "Measured in joule-seconds (kilogram meters squared per second), the same units as Planck’s constant",
            "k": ["joule-seconds", "planck’s constant"],
            "n": 0
        },
        {
            "id": "spin",
            "tier": "power",
            "t": "Spin is the built-in (intrinsic) form carried by particles such as electrons",
            "k": ["intrinsic", "spin"],
            "n": 0,
            "rabbit": "Spin (physics)"
        },
        {
            "id": "moon-tides",
            "tier": "power",
            "t": "Tides move it from Earth’s spin to the Moon’s orbit: days get longer and the Moon drifts about 4 cm farther away each year",
            "k": ["tides", "moon", "days get longer"],
            "n": 0
        },
        {
            "id": "jupiter",
            "tier": "power",
            "t": "The Sun has over 99% of the Solar System’s mass but little of this; Jupiter’s orbit carries most of it",
            "k": ["jupiter", "solar system"],
            "n": 0
        },
        {
            "id": "azimuthal",
            "tier": "power",
            "t": "The azimuthal quantum number l sets an electron’s orbital value and whether the orbital is s, p, d, or f",
            "k": ["azimuthal", "quantum number"],
            "n": 0
        },
        {
            "id": "clebsch-gordan",
            "tier": "power",
            "t": "Clebsch–Gordan coefficients add two sources of it (such as orbit and spin) in quantum mechanics",
            "k": ["clebsch", "gordan", "coefficients"],
            "n": 0
        },
        {
            "id": "falling-cat",
            "tier": "power",
            "t": "A falling cat rights itself with a total of zero by changing its body’s shape",
            "k": ["falling cat", "zero"],
            "n": 0
        },
        {
            "id": "reaction-wheel",
            "tier": "power",
            "t": "Spacecraft turn by spinning reaction wheels the opposite way",
            "k": ["reaction wheels", "spacecraft"],
            "n": 0
        },
        {
            "id": "einstein-de-haas",
            "tier": "power",
            "t": "Einstein–de Haas effect: magnetizing a hanging iron cylinder makes it rotate",
            "k": ["einstein", "de haas", "iron cylinder"],
            "n": 0
        },
        {
            "id": "no-hair",
            "tier": "power",
            "t": "No-hair theorem: a black hole is described by its mass, charge, and this; Kerr black holes have some, Schwarzschild ones none",
            "k": ["no-hair", "kerr", "black hole"],
            "n": 0,
            "rabbit": "Black Holes"
        },
        {
            "id": "angular-impulse",
            "tier": "power",
            "t": "Torque multiplied by the time it acts gives its change, called angular impulse",
            "k": ["impulse", "torque multiplied"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Angular, not linear",
        "body": "Angular momentum (the spinning kind) and plain momentum (mass times velocity) are separate answer lines, and torque and moment of inertia show up in the same formulas. Saying just “momentum” is not enough here: say the whole answer, “angular momentum.” Noether’s theorem trips people up too: rotation symmetry gives angular momentum, while sameness everywhere in space gives ordinary momentum.",
        "fix": "Spinning, orbiting, skaters pulling in their arms, Kepler’s equal areas, L, Iω, and h-bar mean angular momentum. Collisions, p = mv, impulse, and rockets mean ordinary (linear) momentum. A twisting force is torque; resistance to starting a spin is moment of inertia.",
        "line": "Real answer line: <b><u>Angular momentum</u></b> (prompt on <u>L</u>; do not accept “linear momentum”)"
    },
    "tests": {
        "right": [
            "Angular momentum",
            "angular momentum",
            "Angular momentem",
            "Conservation of angular momentum",
            "Rotational momentum",
            "the angular momentum"
        ],
        "prompt": [
            "L"
        ],
        "wrong": [
            "Momentum",
            "Linear momentum",
            "Torque",
            "Moment of inertia",
            "Angular velocity",
            "Spin"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
