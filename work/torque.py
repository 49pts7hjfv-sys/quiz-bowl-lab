import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TIP = "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."

data = {
    "id": "torque",
    "name": "Torque",
    "mono": "TAU",
    "category": "Physics",
    "qbCategory": "Science · Physics",
    "kicker": "The twisting effect of a force · Force times lever arm",
    "dates": "Law of the lever described by Archimedes, 3rd century BCE",
    "briefing": "Torque is the twisting effect of a force: it’s what turns a doorknob, a wrench, or a bicycle pedal. How much torque you get depends on how hard you push and how far from the pivot you push, which is why a long wrench loosens a stubborn bolt and why door handles sit far from the hinges. Torque is to spinning what force is to straight-line motion: it changes how fast things rotate.",
    "answerHtml": "<b><u>torque</u></b> (accept <u>moment of force</u>; prompt on <u>moment</u>, <u>tau</u>, or <u>twisting force</u>; do not accept “angular momentum”)",
    "accept": [
        "torque",
        "torques",
        "net torque",
        "moment of force",
        "moment of a force",
        "moments of force",
        "the moment of force"
    ],
    "prompt": [
        "moment",
        "moments",
        "tau",
        "twisting force",
        "turning force",
        "rotational force",
        "turning effect",
        "twist"
    ],
    "reject": [
        "angular momentum",
        "momentum",
        "moment of inertia",
        "rotational inertia",
        "inertia",
        "angular acceleration",
        "angular velocity",
        "angular impulse",
        "impulse",
        "work",
        "energy",
        "power",
        "horsepower",
        "lever",
        "levers",
        "fulcrum",
        "couple",
        "precession",
        "torsion",
        "tension",
        "newton meter",
        "newton meters",
        "pressure",
        "centripetal force",
        "centrifugal force",
        "friction"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Torque",
    "qb": {
        "q": "torque",
        "found": 0,
        "tip": TIP
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "This quantity’s name comes from a Latin word meaning “to twist.” This quantity is a vector that points along the axis of rotation, in a direction found with the right-hand rule, and it equals the cross product of the position vector from the pivot and the force.",
            "r": "For 10 points, name this rotational equivalent of force, measured in newton-meters."
        },
        {
            "p": "Archimedes’ [“ar-kih-MEE-deez’s”] law of the lever is really a rule about balancing this quantity, and he supposedly boasted, “Give me a place to stand, and I will move the Earth.” On a balanced seesaw, a heavier child must sit closer to the pivot so that both sides have equal amounts of this quantity.",
            "r": "For 10 points, name this twisting effect of a force, equal to the force times the lever arm."
        },
        {
            "p": "In 1785, Charles-Augustin de Coulomb [“KOO-lohm”] measured electric forces with a torsion balance, using the fact that the amount of this quantity needed to twist a thin wire depends on the angle of the twist. Henry Cavendish later used a similar balance to measure the pull of gravity between lead balls.",
            "r": "For 10 points, name this rotational effect of a force, symbolized by the Greek letter tau."
        },
        {
            "p": "A loop of wire carrying an electric current in a magnetic field feels this quantity, which is what makes an electric motor spin. Earth’s magnetic field exerts this quantity on a compass needle, turning the needle until it points north.",
            "r": "For 10 points, name this twisting effect of a force, measured in newton-meters."
        },
        {
            "p": "A car engine’s power equals this quantity multiplied by how fast the crankshaft spins, which is why engine specs list both horsepower and this quantity, often in pound-feet. Low gears on a bicycle let a rider deliver more of this quantity to the rear wheel for the same push on the pedals.",
            "r": "For 10 points, name this rotational equivalent of force, equal to force times lever arm."
        },
        {
            "p": "In the rotational version of Newton’s second law, the net amount of this quantity equals moment of inertia times angular acceleration. A wheel speeds up or slows down its spin only when a net amount of this quantity acts on it.",
            "r": "For 10 points, name this twisting effect of a force, symbolized by the Greek letter tau."
        },
        {
            "p": "The net amount of this quantity on a system equals the rate at which its angular momentum changes, so angular momentum is conserved when this quantity is zero. On a tilted spinning top, gravity’s amount of this quantity makes the top precess instead of falling over.",
            "r": "For 10 points, name this rotational effect of a force, measured in newton-meters."
        },
        {
            "p": "Alexander Calder’s hanging mobiles stay level because, at every pivot, this quantity from the pieces on one side balances this quantity from the pieces on the other side. An object is in static equilibrium only when both the net force and the net amount of this quantity on it are zero.",
            "r": "For 10 points, name this twisting effect of a force, equal to force times lever arm."
        },
        {
            "p": "A tall box tips over once its center of gravity moves past the edge of its base, because gravity then produces this quantity that turns the box over instead of back upright. Objects with wide bases and low centers of gravity are harder to tip over for the same reason.",
            "r": "For 10 points, name this rotational effect of a force, symbolized by the Greek letter tau."
        },
        {
            "p": "Mechanics use a special wrench that clicks when it reaches a set amount of this quantity, so that bolts such as a car’s lug nuts are tightened just right. That tool is named for this quantity.",
            "r": "A longer wrench gives more of it for the same push. For 10 points, name this twisting effect of a force."
        },
        {
            "p": "Multiplying this quantity by the angle that an object turns through, measured in radians, gives the work done on the object. This quantity has the same units as energy, newton-meters, but those units are not called joules when they measure this quantity.",
            "r": "For 10 points, name this rotational equivalent of force, symbolized by the Greek letter tau."
        },
        {
            "p": "Two equal and opposite forces that do not act along the same line, called a couple, produce this quantity without pushing an object in any direction. Turning a steering wheel with your hands on opposite sides creates such a couple.",
            "r": "For 10 points, name this twisting effect of a force, measured in newton-meters."
        },
        {
            "p": "Many cars with automatic transmissions use a fluid-filled “converter” named for this quantity to connect the engine to the wheels. Electric motors can deliver their greatest amount of this quantity even when they are barely turning, which helps electric cars speed up quickly from a stop.",
            "r": "For 10 points, name this rotational effect of a force, equal to force times lever arm."
        },
        {
            "p": "When you hold a weight in your hand, your biceps pulls on your forearm only a few centimeters from the elbow, so it must pull much harder than the weight to make enough of this quantity. In that case, the forearm acts as a third-class lever.",
            "r": "For 10 points, name this twisting effect of a force, which is why door handles are placed far from the hinges."
        },
        {
            "p": "Pushing straight toward a door’s hinges produces none of this quantity, because this quantity depends on the sine of the angle between the force and the lever arm. Its size equals the force times the perpendicular distance from the pivot to the line of the force.",
            "r": "For 10 points, name this rotational effect of a force, symbolized by the Greek letter tau."
        }
    ],
    "clues": [
        {
            "id": "twisting",
            "tier": "giveaway",
            "t": "The twisting or turning effect of a force; the rotational equivalent of force",
            "k": ["twisting", "rotational equivalent"],
            "n": 0
        },
        {
            "id": "force-times-arm",
            "tier": "giveaway",
            "t": "Equals the force times the lever arm, the distance from the pivot",
            "k": ["lever arm", "pivot"],
            "n": 0
        },
        {
            "id": "units-tau",
            "tier": "giveaway",
            "t": "Measured in newton-meters and symbolized by the Greek letter tau",
            "k": ["newton-meters", "greek letter tau", "tau"],
            "n": 0
        },
        {
            "id": "wrench-door",
            "tier": "giveaway",
            "t": "A longer wrench, or a door handle far from the hinges, gives more of it for the same push",
            "k": ["longer wrench", "door handle", "hinges"],
            "n": 0
        },
        {
            "id": "seesaw",
            "tier": "middle",
            "t": "On a balanced seesaw, a heavier child sits closer to the pivot so both sides have equal amounts",
            "k": ["seesaw", "heavier child"],
            "n": 0
        },
        {
            "id": "i-alpha",
            "tier": "middle",
            "t": "Newton’s second law for rotation: the net amount equals moment of inertia times angular acceleration",
            "k": ["moment of inertia", "angular acceleration"],
            "n": 0,
            "rabbit": "Inertia"
        },
        {
            "id": "angular-momentum",
            "tier": "middle",
            "t": "The net amount equals the rate of change of angular momentum; with none, angular momentum is conserved",
            "k": ["angular momentum", "rate of change"],
            "n": 0,
            "rabbit": "Angular momentum"
        },
        {
            "id": "equilibrium",
            "tier": "middle",
            "t": "Static equilibrium needs both zero net force and zero net amount of it",
            "k": ["static equilibrium", "zero net force"],
            "n": 0
        },
        {
            "id": "cross-product",
            "tier": "middle",
            "t": "A vector: the cross product of position and force (r × F), pointing along the axis by the right-hand rule",
            "k": ["cross product", "right-hand rule"],
            "n": 0
        },
        {
            "id": "right-angles",
            "tier": "middle",
            "t": "Greatest when the force is at right angles to the lever arm; pushing straight toward the hinges gives none (it depends on the sine of the angle)",
            "k": ["right angles", "straight toward", "sine"],
            "n": 0
        },
        {
            "id": "motor-compass",
            "tier": "middle",
            "t": "A current loop in a magnetic field feels it, which spins electric motors; it also turns compass needles north",
            "k": ["electric motors", "compass needles", "current loop"],
            "n": 0,
            "rabbit": "Magnetic fields"
        },
        {
            "id": "engine-power",
            "tier": "middle",
            "t": "An engine’s power equals it times how fast the engine spins (angular velocity); engines are rated in pound-feet",
            "k": ["pound-feet", "angular velocity", "power"],
            "n": 0,
            "rabbit": "Power (physics)"
        },
        {
            "id": "precession",
            "tier": "middle",
            "t": "Gravity’s amount of it on a tilted spinning top makes the top precess instead of falling",
            "k": ["precess", "spinning top"],
            "n": 0,
            "rabbit": "Precession"
        },
        {
            "id": "latin",
            "tier": "power",
            "t": "Its name comes from a Latin word meaning “to twist”",
            "k": ["latin", "to twist"],
            "n": 0
        },
        {
            "id": "archimedes",
            "tier": "power",
            "t": "Archimedes’ law of the lever balances it; he supposedly said, “Give me a place to stand, and I will move the Earth”",
            "k": ["archimedes", "place to stand", "law of the lever"],
            "n": 0
        },
        {
            "id": "coulomb",
            "tier": "power",
            "t": "Charles-Augustin de Coulomb’s torsion balance (1785) measured electric forces from the twist of a thin wire",
            "k": ["coulomb", "torsion balance", "1785"],
            "n": 0,
            "rabbit": "Coulomb’s law"
        },
        {
            "id": "cavendish",
            "tier": "power",
            "t": "Henry Cavendish used a similar torsion balance to measure the pull of gravity between lead balls",
            "k": ["cavendish", "lead balls"],
            "n": 0,
            "rabbit": "Gravity"
        },
        {
            "id": "calder",
            "tier": "power",
            "t": "Alexander Calder’s mobiles stay level because the amounts on both sides of each pivot balance",
            "k": ["calder", "mobiles"],
            "n": 0
        },
        {
            "id": "tipping",
            "tier": "power",
            "t": "A box tips over once its center of gravity moves past the edge of its base",
            "k": ["center of gravity", "tips over"],
            "n": 0
        },
        {
            "id": "wrench-tool",
            "tier": "power",
            "t": "A clicking wrench named for it tightens bolts, such as a car’s lug nuts, to a set amount",
            "k": ["lug nuts", "clicking wrench"],
            "n": 0
        },
        {
            "id": "work-angle",
            "tier": "power",
            "t": "It times the angle turned (in radians) equals the work done",
            "k": ["radians", "work done"],
            "n": 0
        },
        {
            "id": "not-joules",
            "tier": "power",
            "t": "It shares units with energy (newton-meters), but those units are not called joules when they measure it",
            "k": ["joules", "energy"],
            "n": 0
        },
        {
            "id": "couple",
            "tier": "power",
            "t": "A couple: two equal, opposite forces not along the same line, like two hands turning a steering wheel",
            "k": ["couple", "steering wheel"],
            "n": 0
        },
        {
            "id": "converter",
            "tier": "power",
            "t": "A fluid-filled “converter” named for it connects the engine to the wheels in many automatic transmissions",
            "k": ["automatic transmissions", "converter"],
            "n": 0
        },
        {
            "id": "electric-cars",
            "tier": "power",
            "t": "Electric motors give their greatest amount even when barely turning, so electric cars speed up quickly from a stop",
            "k": ["electric cars", "barely turning"],
            "n": 0
        },
        {
            "id": "biceps",
            "tier": "power",
            "t": "The biceps pulls on the forearm a few centimeters from the elbow (a third-class lever), so it pulls much harder than the weight held",
            "k": ["biceps", "third-class lever", "elbow"],
            "n": 0
        },
        {
            "id": "bicycle-gears",
            "tier": "power",
            "t": "Low gears on a bicycle deliver more of it to the rear wheel for the same push on the pedals",
            "k": ["low gears", "bicycle"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Torque or angular momentum?",
        "body": "Torque, angular momentum, and moment of inertia all show up in the same spinning-object tossups. Torque is the twist that changes a spin, angular momentum is the amount of spin, and moment of inertia is how hard an object is to spin up. Saying just “moment” or “twisting force” earns only a prompt.",
        "fix": "Wrenches, levers, seesaws, newton-meters, r × F, tau, and “force times lever arm” mean torque. Iω, spinning skaters, and Kepler’s equal areas mean angular momentum; mass spread far from the axis means moment of inertia.",
        "line": "Real answer line: <b><u>torque</u></b> (accept <u>moment of force</u>; prompt on <u>moment</u>, <u>tau</u>, or <u>twisting force</u>; do not accept “angular momentum”)"
    },
    "tests": {
        "right": [
            "Torque",
            "torque",
            "Torqe",
            "Moment of force",
            "Net torque"
        ],
        "prompt": [
            "Moment",
            "Tau",
            "Twisting force"
        ],
        "wrong": [
            "Angular momentum",
            "Moment of inertia",
            "Force",
            "Work",
            "Angular acceleration",
            "Lever arm",
            "Precession"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
