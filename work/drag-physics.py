import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TIP = "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."


def C(cid, tier, t, k, rabbit=None):
    d = {"id": cid, "tier": tier, "t": t, "k": k, "n": 0}
    if rabbit:
        d["rabbit"] = rabbit
    return d


data = {
    "id": "drag-physics",
    "name": "Drag (physics)",
    "mono": "DRG",
    "category": "Physics",
    "qbCategory": "Science · Physics",
    "kicker": "The force that resists motion through air or water · Why parachutes work",
    "dates": "Studied in Isaac Newton’s _Principia_, 1687",
    "briefing": "Drag is the force that pushes back on anything moving through air or water, from a cyclist to a swimmer to a jumbo jet. It grows quickly with speed, which is why a falling skydiver eventually stops speeding up at a steady terminal velocity, and why a parachute, with its huge area, slows the fall to a gentle landing. Engineers fight drag by giving cars, planes, and racing bikes smooth, streamlined shapes.",
    "answerHtml": "<b><u>drag</u></b> (accept <u>drag force</u>, <u>air resistance</u>, or <u>fluid resistance</u>; do not accept “friction” or “lift”)",
    "accept": [
        "drag",
        "drag force",
        "drag forces",
        "aerodynamic drag",
        "air drag",
        "fluid drag",
        "hydrodynamic drag",
        "air resistance",
        "water resistance",
        "fluid resistance",
        "drag physics"
    ],
    "prompt": [
        "resistance",
        "resistive force",
        "resistive forces",
        "retarding force"
    ],
    "reject": [
        "friction",
        "frictional force",
        "friction force",
        "kinetic friction",
        "static friction",
        "rolling friction",
        "lift",
        "lift force",
        "thrust",
        "weight",
        "gravity",
        "buoyancy",
        "buoyant force",
        "viscosity",
        "terminal velocity",
        "terminal speed",
        "turbulence",
        "tension",
        "normal force",
        "inertia",
        "momentum",
        "pressure",
        "air pressure",
        "bernoullis principle",
        "magnus effect",
        "drag coefficient",
        "coefficient of drag",
        "drag equation",
        "electrical resistance",
        "resistor",
        "impedance",
        "surface tension",
        "stokes law",
        "reynolds number"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Drag_(physics)",
    "qb": {"q": "drag", "found": 0, "tip": TIP},
    "sample": {"n": 0, "note": "no real tossups checked yet"},
    "tossups": [
        {
            "p": "Golf balls have dimples because the dimples help the air flowing past cling to the ball longer, shrinking the low-pressure wake behind it and so reducing this force. Swimmers shave and wear slick suits to reduce this force in water.",
            "r": "For 10 points, name this force that resists the motion of an object through a fluid such as air or water."
        },
        {
            "p": "Stokes’ law says that for a tiny sphere moving slowly through a fluid, this force equals six pi times the fluid’s viscosity times the sphere’s radius and speed. Robert Millikan used that law to find the sizes of his charged droplets.",
            "r": "For 10 points, name this force that opposes motion through a fluid and makes falling objects reach terminal velocity."
        },
        {
            "p": "Car designers test models in wind tunnels to lower this force’s namesake coefficient. At highway speeds, this force roughly quadruples whenever a car’s speed doubles, so on the highway it uses up much of a car’s fuel.",
            "r": "Parachutes use it to slow a fall. For 10 points, name this force that streamlined shapes are designed to reduce."
        },
        {
            "p": "A skydiver who tucks into a head-down dive can fall much faster than one falling belly-down, because the smaller area facing the air cuts this force. Belly-down skydivers stop speeding up at roughly 200 kilometers per hour.",
            "r": "When this force balances a falling object’s weight, the object reaches terminal velocity. For 10 points, name this force."
        },
        {
            "p": "Isaac Newton studied this force in Book II of his _Principia_, arguing that for many objects moving through air or water it grows roughly with the square of their speed. He measured it by watching how quickly swinging pendulums slowed down.",
            "r": "For 10 points, name this force that acts on a moving object opposite to its motion through a fluid."
        },
        {
            "p": "Racing cyclists ride in tight lines so that riders behind can tuck into the leader’s wake, where this force is much weaker, a trick called drafting. Race car drivers use the same trick at high speed.",
            "r": "Streamlined shapes reduce it. For 10 points, name this force that resists objects moving through air."
        },
        {
            "p": "In 1971, Apollo 15 astronaut David Scott dropped a hammer and a falcon feather on the Moon, and they hit the ground together, because the Moon has almost no air to cause this force.",
            "r": "On Earth, this force makes a feather fall slowly. For 10 points, name this force that resists motion through air."
        },
        {
            "p": "Spinning maple seeds and fluffy dandelion seeds take advantage of this force to fall slowly, so the wind can carry them far from the parent plant. A flat sheet of paper falls slowly, but the same sheet crumpled into a ball falls fast, because crumpling reduces this force.",
            "r": "For 10 points, name this force that a parachute uses to slow a falling skydiver."
        },
        {
            "p": "Thin traces of air in low Earth orbit slowly pull the International Space Station lower through this force, so it has to be boosted back up from time to time by rocket thrusters.",
            "r": "Returning spacecraft use this force to slow down in the atmosphere. For 10 points, name this force that resists motion through air."
        },
        {
            "p": "The Reynolds number compares a fluid’s inertia to its viscosity. At low Reynolds numbers, such as for a bacterium swimming, this force grows in direct proportion to speed, but for a fast-moving car it grows with the square of speed.",
            "r": "Teardrop-shaped, streamlined bodies reduce this force. For 10 points, name this force that resists motion through a fluid."
        },
        {
            "p": "Downhill skiers crouch into a tight “tuck” position and speed skaters wear smooth, hooded suits to reduce this force, which grows quickly as they go faster. Cyclists in time trials wear pointed, teardrop-shaped helmets for the same reason.",
            "r": "For 10 points, name this force that a streamlined shape helps reduce, which acts opposite to an object’s motion through air."
        },
        {
            "p": "Europe’s Huygens [“HOY-gunz”] probe floated down through the thick, hazy air of Saturn’s moon Titan for more than two hours in 2005, slowed by parachutes that relied on this force.",
            "r": "For 10 points, name this force, which grows with an object’s speed and with the area it presents to the air."
        },
        {
            "p": "Airplane wings produce an “induced” type of this force as a side effect of making lift, and many airliners have upturned winglets at their wingtips to reduce it. That type is strongest when a plane flies slowly, as during takeoff and landing.",
            "r": "Of the four forces on a flying airplane, this one opposes thrust. For 10 points, name this force."
        },
        {
            "p": "Gustave Eiffel studied this force by dropping objects from his famous tower in Paris, and he later built wind tunnels to measure it on models of airplane wings. He published his results in the early 1900s.",
            "r": "Parachutes increase it. For 10 points, name this force that resists the motion of a falling object through the air."
        },
        {
            "p": "A diving peregrine falcon pulls its wings tight against its body to cut this force, letting it reach speeds of more than 300 kilometers per hour. Tuna and dolphins have torpedo-shaped bodies to reduce this force as they swim.",
            "r": "It grows as an object moves faster through air or water. For 10 points, name this force that parachutes are designed to increase."
        }
    ],
    "clues": [
        C("definition", "giveaway", "A force that resists an object’s motion through a fluid, such as air or water",
          ["fluid", "resists", "air or water"]),
        C("terminal-velocity", "giveaway", "When it balances a falling object’s weight, the object stops speeding up: terminal velocity",
          ["terminal velocity", "balances"], "Velocity"),
        C("parachute", "giveaway", "Parachutes use their large area to increase it and slow a fall",
          ["parachutes", "large area"]),
        C("streamlining", "giveaway", "Streamlined, teardrop shapes, as on cars, planes, and fish, reduce it",
          ["streamlined", "teardrop"]),
        C("airplane-forces", "giveaway", "One of the four forces on a flying airplane; it opposes thrust, while lift opposes weight",
          ["four forces", "thrust", "airplane"]),
        C("speed-squared", "middle", "At highway speeds it roughly quadruples when speed doubles (it grows with the square of speed)",
          ["quadruples", "square of speed"]),
        C("coefficient", "middle", "Engineers calculate it with a namesake equation that uses its coefficient, measured in wind tunnels",
          ["coefficient", "wind tunnels", "equation"]),
        C("area-shape", "middle", "It depends on the fluid, the object’s speed, its shape, and the area facing the flow",
          ["area", "shape"]),
        C("moon-feather", "middle", "On the Moon in 1971, Apollo 15’s David Scott dropped a hammer and a feather that fell together, since there is almost no air",
          ["hammer", "feather", "apollo 15"], "Gravity"),
        C("drafting", "middle", "Drafting: cyclists and race cars ride in a leader’s wake, where it is weaker",
          ["drafting", "wake"]),
        C("skydiver", "middle", "A belly-down skydiver stops speeding up at roughly 200 km/h; a head-down dive cuts it and falls faster",
          ["skydiver", "belly-down", "head-down"]),
        C("not-friction", "middle", "Sometimes called fluid friction, but a separate answer from sliding friction between solid surfaces",
          ["sliding friction", "fluid friction"], "Friction"),
        C("dimples", "power", "Golf ball dimples shrink the low-pressure wake behind the ball, reducing it",
          ["dimples", "golf ball", "wake"]),
        C("stokes", "power", "Stokes’ law: for a tiny, slow sphere it equals 6π × viscosity × radius × speed (used by Millikan)",
          ["stokes’ law", "viscosity", "sphere"], "Viscosity"),
        C("reynolds", "power", "The Reynolds number compares inertia to viscosity; at low values it grows in proportion to speed, at high values with speed squared",
          ["reynolds number", "proportion"]),
        C("newton-principia", "power", "Isaac Newton studied it in Book II of his _Principia_, watching how swinging pendulums slowed",
          ["principia", "book ii", "pendulums"], "Isaac Newton"),
        C("seeds", "power", "Spinning maple seeds and fluffy dandelion seeds use it to fall slowly and drift far",
          ["maple", "dandelion", "seeds"]),
        C("iss", "power", "Thin air in low orbit slowly pulls the International Space Station lower, so it must be boosted back up",
          ["international space station", "low orbit", "boosted"]),
        C("huygens", "power", "Huygens’s parachutes slowed it through Titan’s thick air for more than two hours in 2005",
          ["huygens", "titan", "2005"], "Titan (moon)"),
        C("induced", "power", "Wings make an “induced” type as a side effect of lift; winglets reduce it, and it is strongest at low speeds",
          ["induced", "winglets", "lift"]),
        C("eiffel", "power", "Gustave Eiffel dropped objects from his tower and built wind tunnels to measure it",
          ["eiffel", "tower"]),
        C("skiers", "power", "Downhill skiers tuck, speed skaters wear smooth suits, and cyclists wear teardrop helmets to reduce it",
          ["skiers", "tuck", "speed skaters"]),
        C("falcon", "power", "A diving peregrine falcon pulls in its wings to cut it, passing 300 km/h",
          ["peregrine falcon", "300"]),
        C("swimmers", "power", "Swimmers shave and wear slick suits to reduce it in water; tuna and dolphins are torpedo-shaped",
          ["swimmers", "slick suits", "torpedo-shaped"]),
        C("paper", "power", "Flat paper falls slowly but crumpled paper falls fast, because crumpling reduces it",
          ["crumpled", "paper"])
    ],
    "trap": {
        "title": "Not friction, not lift",
        "body": "This force is sometimes called “fluid friction,” but quiz bowl treats it as a separate answer from friction between two solid surfaces, and this page does not accept “friction.” On airplanes it is one of four forces, so players blurt “lift,” which pushes a plane up, or “thrust,” which pushes it forward. And “terminal velocity” is a speed, not a force.",
        "fix": "Air or water, parachutes, streamlining, wind tunnels, and speed squared point to this force; sliding surfaces, lubricants, and the coefficient mu times the normal force point to friction. On an airplane, the force that opposes thrust is this one, while lift opposes weight.",
        "line": "Real answer line: <b><u>drag</u></b> (accept <u>drag force</u>, <u>air resistance</u>, or <u>fluid resistance</u>; do not accept “friction” or “lift”)"
    },
    "tests": {
        "right": [
            "Drag",
            "Drag force",
            "Air resistance",
            "Drag (physics)",
            "Air resistence"
        ],
        "prompt": [
            "Resistance",
            "Resistive force"
        ],
        "wrong": [
            "Friction",
            "Lift",
            "Terminal velocity",
            "Viscosity",
            "Thrust"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
