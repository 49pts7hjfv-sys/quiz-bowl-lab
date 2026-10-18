import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "boyles-law",
    "name": "Boyle’s law",
    "mono": "BYL",
    "category": "Chemistry",
    "qbCategory": "Science · Chemistry",
    "kicker": "Squeeze a gas and its pressure rises · PV stays constant at fixed temperature",
    "dates": "Published by Robert Boyle, 1662",
    "briefing": "Push a syringe’s plunger while blocking its tip, and the trapped air pushes back harder the more you squeeze it. Robert Boyle measured this in 1662: at a constant temperature, a gas’s pressure and volume are inversely proportional, so halving the volume doubles the pressure. Written PV = k, Boyle’s law explains why your lungs fill when your diaphragm moves down and why a sealed bag of chips puffs up on a mountaintop.",
    "answerHtml": "<b><u>Boyle’s law</u></b> (accept <u>Boyle–Mariotte law</u> or <u>Mariotte’s law</u>; prompt on <u>Boyle</u> alone)",
    "accept": [
        "boyles law",
        "boyle law",
        "boyles gas law",
        "boyle mariotte law",
        "boyle mariottes law",
        "boyles mariottes law",
        "boyles and mariottes law",
        "mariottes law",
        "mariotte law",
        "mariottes gas law",
        "pv k",
        "pv equals k",
        "p1v1 p2v2",
        "p1v1 equals p2v2",
        "p1 v1 p2 v2"
    ],
    "prompt": [
        "boyle",
        "boyles",
        "robert boyle",
        "mariotte",
        "edme mariotte",
        "gas law",
        "gas laws",
        "pressure volume law"
    ],
    "reject": [
        "charles law",
        "charless law",
        "gay lussacs law",
        "gay lussac law",
        "amontons law",
        "amontonss law",
        "avogadros law",
        "avogadro law",
        "daltons law",
        "dalton law",
        "henrys law",
        "henry law",
        "grahams law",
        "combined gas law",
        "ideal gas law",
        "ideal gas",
        "pv nrt",
        "hookes law",
        "pascals law",
        "pascals principle",
        "bernoullis principle",
        "boyle temperature",
        "boyles temperature",
        "kinetic molecular theory",
        "gas constant"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Boyle%27s_law",
    "qb": {
        "q": "Boyle",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "Richard Towneley and Henry Power noticed this relationship in the early 1660s, before its namesake confirmed it with careful measurements. Its namesake published it in 1662, in a defense of his work against the Jesuit critic Franciscus Linus.",
            "r": "Doubling the pressure on a gas obeying this law halves its volume. For 10 points, name this law that relates a gas’s pressure and volume at constant temperature."
        },
        {
            "p": "A French physicist who also discovered the blind spot in the human eye found this law on his own in 1676, so in France it is often called by his name. This law describes an isothermal process, one in which the temperature stays the same.",
            "r": "It says that a gas’s pressure times its volume stays constant. For 10 points, name this gas law named for an Irish-born chemist of the 1600s."
        },
        {
            "p": "At a temperature named for this law’s discoverer, a real gas obeys this law over a wide range of pressures, because the effects of its molecules’ attractions and their sizes cancel out. Real gases break this law at very high pressures.",
            "r": "This law says that halving a gas’s volume doubles its pressure if the temperature stays fixed. For 10 points, name this law relating pressure and volume."
        },
        {
            "p": "In his 1738 book _Hydrodynamica_, Daniel Bernoulli derived this law by imagining gas particles bouncing off the walls of their container. In the kinetic theory of gases, this law holds because squeezing a gas into a smaller space makes its particles hit the walls more often.",
            "r": "For 10 points, name this law which states that, at constant temperature, the pressure of a gas is inversely proportional to its volume."
        },
        {
            "p": "Plotting a gas’s pressure against one over its volume gives a straight line through the origin for a gas obeying this law, while plotting pressure against volume gives a curve called a hyperbola. Each such curve, drawn for one temperature, is called an isotherm.",
            "r": "For 10 points, name this gas law summed up by saying that pressure times volume stays the same."
        },
        {
            "p": "Robert Hooke built the air pump that this law’s namesake used in his experiments on air, and Hooke later gave his own name to a law about springs. Breathing follows this law: when the diaphragm moves down, the chest cavity gets bigger, so the pressure inside the lungs drops.",
            "r": "Air then rushes in to fill the lungs. For 10 points, name this law relating a gas’s pressure and volume."
        },
        {
            "p": "A balloon filled with air 10 meters underwater roughly doubles in volume by the time it reaches the surface, because the pressure at that depth is about twice the pressure at the surface. Weather balloons swell as they rise for a similar reason, since the air pressure around them keeps falling.",
            "r": "Scuba divers are taught never to hold their breath while rising. For 10 points, name this law relating a gas’s pressure and volume."
        },
        {
            "p": "A marshmallow sealed inside a syringe swells up when the plunger is pulled back, because lowering the pressure lets the tiny pockets of air inside it expand. A sealed bag of chips puffs up at high altitude for the same reason.",
            "r": "For 10 points, name this law stating that a gas’s volume rises as its pressure falls, if its temperature stays constant."
        },
        {
            "p": "This law’s namesake was born at Lismore Castle in Ireland, a son of the Earl of Cork. He wrote _The Sceptical Chymist_ in 1661 and helped found the Royal Society.",
            "r": "For 10 points, name this law which says that a gas’s pressure and volume are inversely proportional at constant temperature."
        },
        {
            "p": "Thomas Hobbes, the author of _Leviathan_, attacked the air-pump experiments that this law’s namesake used to study air. This law can be joined with Charles’s law and Gay-Lussac’s law to form the combined gas law.",
            "r": "For 10 points, name this law which says that squeezing a gas into a smaller space raises its pressure, as long as its temperature stays the same."
        },
        {
            "p": "If a gas obeying this law at 1 atmosphere is squeezed from 6 liters down to 2 liters, its pressure rises to 3 atmospheres. This law works only when both the temperature and the amount of gas stay fixed.",
            "r": "For 10 points, name this gas law often written as P-one V-one equals P-two V-two."
        },
        {
            "p": "This law’s namesake described the “spring of the air,” its push back against being squeezed, in a 1660 book of experiments made with an air pump. For a later edition, he trapped air in the sealed short arm of a J-shaped tube and compressed it by pouring mercury into the long arm.",
            "r": "This law says that a gas’s pressure rises as its volume shrinks. For 10 points, name this law relating the pressure and volume of a gas at constant temperature."
        },
        {
            "p": "For a gas that perfectly obeys this law, a graph of pressure times volume against pressure is a flat, horizontal line. Real gases curve away from that line at high pressures, because their molecules take up space and attract one another.",
            "r": "This law says that pressure and volume are inversely proportional. For 10 points, name this gas law that holds at constant temperature."
        },
        {
            "p": "Squeezing a sealed plastic bottle makes a small toy called a Cartesian diver sink, because the higher pressure shrinks the air bubble trapped inside the diver. Letting go lets the bubble expand again, so the diver floats back up.",
            "r": "For 10 points, name this law stating that, at constant temperature, a gas’s volume shrinks as the pressure on it rises."
        },
        {
            "p": "Émile Clapeyron [“klah-pay-RAWN”] combined this law with Charles’s law in 1834 to state the ideal gas law. Real gases follow this law best at low pressures and high temperatures, where their molecules are far apart and barely attract one another.",
            "r": "At constant temperature, the ideal gas law reduces to this law. For 10 points, name this law relating a gas’s pressure and volume."
        }
    ],
    "clues": [
        {
            "id": "inverse",
            "tier": "giveaway",
            "t": "At constant temperature, a gas’s pressure and volume are inversely proportional",
            "k": ["inversely proportional", "pressure", "volume"],
            "n": 0
        },
        {
            "id": "formula",
            "tier": "giveaway",
            "t": "Pressure times volume stays constant: P₁V₁ = P₂V₂",
            "k": ["pressure times volume", "constant"],
            "n": 0
        },
        {
            "id": "doubling",
            "tier": "giveaway",
            "t": "Double the pressure on a gas and its volume is cut in half",
            "k": ["double", "half"],
            "n": 0
        },
        {
            "id": "namesake",
            "tier": "giveaway",
            "t": "Named for an Irish-born chemist of the 1600s, often called a father of modern chemistry",
            "k": ["irish-born", "father of modern chemistry", "1600s"],
            "n": 0
        },
        {
            "id": "isothermal",
            "tier": "middle",
            "t": "Describes an isothermal process: the temperature and the amount of gas stay fixed",
            "k": ["isothermal", "amount of gas"],
            "n": 0
        },
        {
            "id": "kinetic",
            "tier": "middle",
            "t": "Kinetic theory: in a smaller space, gas particles hit the walls more often, so the pressure rises",
            "k": ["kinetic theory", "walls", "more often"],
            "n": 0
        },
        {
            "id": "breathing",
            "tier": "middle",
            "t": "Breathing: the diaphragm moves down, the chest gets bigger, the pressure in the lungs drops, and air flows in",
            "k": ["diaphragm", "breathing", "lungs"],
            "n": 0
        },
        {
            "id": "syringe",
            "tier": "middle",
            "t": "Pulling back a syringe’s plunger makes more room, lowering the pressure so liquid is drawn in",
            "k": ["syringe", "plunger"],
            "n": 0
        },
        {
            "id": "scuba",
            "tier": "middle",
            "t": "Air from 10 meters underwater about doubles in volume at the surface, so scuba divers must never hold their breath while rising",
            "k": ["scuba", "10 meters", "hold their breath"],
            "n": 0
        },
        {
            "id": "chips",
            "tier": "middle",
            "t": "A sealed bag of chips puffs up at high altitude; a marshmallow in a syringe swells when the plunger is pulled back",
            "k": ["bag of chips", "marshmallow", "altitude"],
            "n": 0
        },
        {
            "id": "combined",
            "tier": "middle",
            "t": "Joined with Charles’s and Gay-Lussac’s laws in the combined gas law; the ideal gas law reduces to it at constant temperature",
            "k": ["combined gas law", "charles", "ideal gas law"],
            "n": 0,
            "rabbit": "Ideal gas law"
        },
        {
            "id": "graphs",
            "tier": "middle",
            "t": "Pressure plotted against volume is a curve called a hyperbola; pressure against one over volume is a straight line",
            "k": ["hyperbola", "straight line"],
            "n": 0
        },
        {
            "id": "cartesian",
            "tier": "middle",
            "t": "Squeezing a bottle makes a Cartesian diver sink by shrinking its air bubble",
            "k": ["cartesian diver", "squeezing", "bubble"],
            "n": 0
        },
        {
            "id": "towneley",
            "tier": "power",
            "t": "Richard Towneley and Henry Power noticed the relationship first, in the early 1660s",
            "k": ["towneley", "henry power"],
            "n": 0
        },
        {
            "id": "linus",
            "tier": "power",
            "t": "Its namesake published it in 1662, defending his work against the Jesuit critic Franciscus Linus",
            "k": ["1662", "linus", "jesuit"],
            "n": 0
        },
        {
            "id": "spring-of-air",
            "tier": "power",
            "t": "His 1660 book of air-pump experiments described the “spring of the air”",
            "k": ["spring of the air", "1660"],
            "n": 0
        },
        {
            "id": "j-tube",
            "tier": "power",
            "t": "Its namesake poured mercury into a J-shaped tube to squeeze a pocket of trapped air",
            "k": ["j-shaped", "mercury", "trapped air"],
            "n": 0
        },
        {
            "id": "hooke",
            "tier": "power",
            "t": "Robert Hooke, who later named a law about springs, built the air pump",
            "k": ["hooke", "air pump"],
            "n": 0,
            "rabbit": "Hooke’s law"
        },
        {
            "id": "mariotte",
            "tier": "power",
            "t": "Edme Mariotte, who also discovered the eye’s blind spot, found it independently in 1676",
            "k": ["mariotte", "blind spot", "1676"],
            "n": 0
        },
        {
            "id": "named-temperature",
            "tier": "power",
            "t": "At a temperature named for its discoverer, a real gas obeys it over a wide range of pressures",
            "k": ["temperature named", "real gas"],
            "n": 0
        },
        {
            "id": "bernoulli",
            "tier": "power",
            "t": "Daniel Bernoulli derived it in _Hydrodynamica_ (1738) from particles hitting the walls of their container",
            "k": ["bernoulli", "hydrodynamica", "1738"],
            "n": 0
        },
        {
            "id": "flat-line",
            "tier": "power",
            "t": "Pressure times volume plotted against pressure is a flat line for an ideal gas; real gases curve away at high pressure",
            "k": ["flat line", "high pressure"],
            "n": 0
        },
        {
            "id": "sceptical",
            "tier": "power",
            "t": "Its namesake wrote _The Sceptical Chymist_ (1661) and helped found the Royal Society",
            "k": ["sceptical chymist", "royal society", "1661"],
            "n": 0
        },
        {
            "id": "lismore",
            "tier": "power",
            "t": "Its namesake was born at Lismore Castle in Ireland, a son of the Earl of Cork",
            "k": ["lismore", "earl of cork"],
            "n": 0
        },
        {
            "id": "hobbes",
            "tier": "power",
            "t": "Thomas Hobbes, author of _Leviathan_, attacked its namesake’s air-pump experiments",
            "k": ["hobbes", "leviathan"],
            "n": 0
        },
        {
            "id": "clapeyron",
            "tier": "power",
            "t": "Émile Clapeyron combined it with Charles’s law in 1834 to state the ideal gas law",
            "k": ["clapeyron", "1834"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Pressure and volume only",
        "body": "Gas-law tossups blur together: Charles’s law links volume and temperature, Gay-Lussac’s law links pressure and temperature, and the ideal gas law ties everything together as PV = nRT. This law is the one where the temperature stays fixed while pressure and volume trade off. Hearing “Robert Hooke” in an early clue can also lure a wrong buzz of “Hooke’s law,” which is about springs.",
        "fix": "Ask which quantity is held constant. Constant temperature, with pressure and volume moving in opposite directions, means this law; constant pressure means Charles’s law; constant volume means Gay-Lussac’s law. Saying just “Boyle” earns a prompt, so add “law.”",
        "line": "Real answer line: <b><u>Boyle’s law</u></b> (accept <u>Boyle–Mariotte law</u> or <u>Mariotte’s law</u>; prompt on <u>Boyle</u>)"
    },
    "tests": {
        "right": [
            "Boyle’s law",
            "Boyle's Law",
            "boyels law",
            "Mariotte’s law",
            "Boyle-Mariotte law",
            "PV = k"
        ],
        "prompt": [
            "Boyle",
            "Robert Boyle"
        ],
        "wrong": [
            "Charles’s law",
            "Ideal gas law",
            "Gay-Lussac’s law",
            "Henry’s law",
            "Combined gas law",
            "Hooke’s law"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
