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
    "id": "density",
    "name": "Density",
    "mono": "RHO",
    "category": "Physics",
    "qbCategory": "Science · Physics",
    "kicker": "Mass packed into a given space · Why ice floats and rocks sink",
    "dates": "Archimedes’ crown test, 3rd century BCE (traditional story)",
    "briefing": "Density tells you how much mass is packed into a given space: a brick and a block of foam the same size have very different densities. You find it by dividing an object’s mass by its volume, and anything less dense than water, like a block of wood, floats on it. Water itself is a strange case: it is densest at about 4 °C, and ice is less dense than liquid water, which is why ice cubes float.",
    "answerHtml": "<b><u>density</u></b> (accept <u>mass density</u>; prompt on <u>specific gravity</u>, <u>relative density</u>, or <u>rho</u>; do not accept “mass” or “volume”)",
    "accept": [
        "density",
        "densities",
        "mass density",
        "average density",
        "mean density",
        "volumetric mass density"
    ],
    "prompt": [
        "specific gravity",
        "relative density",
        "rho"
    ],
    "reject": [
        "volume",
        "weight",
        "specific weight",
        "buoyancy",
        "buoyant force",
        "archimedes principle",
        "archimedes",
        "pressure",
        "viscosity",
        "concentration",
        "molarity",
        "molar mass",
        "atomic mass",
        "inertia",
        "specific heat",
        "heat capacity",
        "population density",
        "optical density",
        "charge density",
        "current density",
        "energy density",
        "number density",
        "probability density",
        "linear density",
        "area density",
        "surface density",
        "salinity",
        "surface tension",
        "temperature",
        "momentum",
        "hardness",
        "thickness"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Density",
    "qb": {"q": "density", "found": 0, "tip": TIP},
    "sample": {"n": 0, "note": "no real tossups checked yet"},
    "tossups": [
        {
            "p": "Henry Cavendish’s 1798 experiment, often described as “weighing the world,” found Earth’s average value of this quantity to be about five and a half times that of water. Earth has the highest value of this quantity of any planet in the solar system.",
            "r": "For 10 points, name this quantity, found by dividing an object’s mass by its volume."
        },
        {
            "p": "A Galileo thermometer works because its glass bulbs rise or sink as this property of the liquid around them changes with temperature. Each bulb carries a small tag marked with a temperature.",
            "r": "Of the planets, only Saturn has a lower average value of this property than water. For 10 points, name this property, measured in grams per cubic centimeter."
        },
        {
            "p": "Osmium has the highest value of this property of any element, just ahead of iridium, while lithium has the lowest value of any metal and can even float on water. A block of osmium has about twice the mass of a lead block the same size.",
            "r": "Objects with more of it than water sink. For 10 points, name this property, equal to mass per unit volume."
        },
        {
            "p": "According to a story told by the Roman writer Vitruvius [“vih-TROO-vee-us”], Archimedes [“ar-kih-MEE-deez”] figured out how to test whether King Hiero’s [“HY-er-ohz”] crown was pure gold while stepping into a bath, then ran home shouting “Eureka!”",
            "r": "He realized that the water pushed aside would reveal the crown’s volume. For 10 points, name this property, mass divided by volume, that showed whether the crown was pure gold."
        },
        {
            "p": "Lakes freeze from the top down partly because liquid water reaches its greatest value of this property at about 4 °C, so the water at the bottom of a deep lake stays near that temperature all winter.",
            "r": "Ice floats because it has less of this property than liquid water. For 10 points, name this property, an object’s mass divided by its volume."
        },
        {
            "p": "Submarines dive and surface by flooding or emptying ballast tanks, which changes their overall value of this quantity compared with the seawater around them. Many fish do the same job by adjusting the gas in a swim bladder.",
            "r": "For 10 points, name this quantity whose value for pure water is 1 gram per cubic centimeter."
        },
        {
            "p": "A hydrometer floats higher in liquids that have more of this property, so the mark on its stem at the surface tells the value. Dividing this property of a substance by that of water gives a unitless number called specific gravity.",
            "r": "Things with less of it than water float. For 10 points, name this property calculated as mass divided by volume."
        },
        {
            "p": "An iron or lead cannonball floats on liquid mercury, because mercury has a greater value of this property than either metal. Gold, however, sinks in mercury. Mercury has about 13.5 times as much of this property as water.",
            "r": "For 10 points, name this property, symbolized by the Greek letter rho, which equals mass divided by volume."
        },
        {
            "p": "Very salty water has more of this property than fresh water, which is why swimmers float so easily in the Dead Sea and why a raw egg that sinks in tap water can float in strong salt water.",
            "r": "For 10 points, name this property, which tells whether an object will sink or float in a liquid."
        },
        {
            "p": "In the North Atlantic, cold, salty seawater sinks because it has a high value of this quantity, helping drive a slow, worldwide loop of deep ocean currents called the thermohaline circulation. Antarctic Bottom Water has the highest value of this quantity of any large mass of ocean water.",
            "r": "Warm air rises for the opposite reason. For 10 points, name this quantity, mass per unit volume."
        },
        {
            "p": "A neutron star packs more mass than the Sun into a ball about the size of a city, giving it an enormous value of this quantity. A white dwarf has a smaller but still huge value of it.",
            "r": "For 10 points, name this quantity found by dividing an object’s mass by its volume."
        },
        {
            "p": "A can of regular soda usually sinks in a tank of water while a can of diet soda floats, because the sugar dissolved in regular soda raises this property.",
            "r": "A classroom “tower” stacks honey, water, and oil in layers by this property. For 10 points, name this property, mass divided by volume."
        },
        {
            "p": "Water has roughly 800 times as much of this quantity as air at sea level. At a fixed pressure, heating a gas lowers this quantity, which is why a hot-air balloon rises through the cooler air around it.",
            "r": "For 10 points, name this quantity, an object’s mass per unit volume, often given in grams per cubic centimeter."
        },
        {
            "p": "Hydrogen bonds lock frozen water molecules into an open, six-sided pattern with lots of empty space, so water expands by about nine percent when it freezes and its value of this property drops.",
            "r": "That is why ice floats. For 10 points, name this property, an object’s mass divided by its volume."
        },
        {
            "p": "The kilogram was first based on the mass of one liter of water, so water’s value of this quantity was set at one kilogram per liter. Seawater has slightly more of this quantity than fresh water.",
            "r": "To find this quantity for a rock, measure its volume by how much water it pushes aside, then divide its mass by that volume. For 10 points, name this quantity."
        }
    ],
    "clues": [
        C("mass-volume", "giveaway", "Equals mass divided by volume (ρ = m/V)",
          ["mass divided by volume", "mass", "volume"]),
        C("units", "giveaway", "Often measured in grams per cubic centimeter; pure water has 1 g/cm³",
          ["grams per cubic centimeter", "pure water"]),
        C("float-sink", "giveaway", "Objects with less of it than water float; objects with more sink",
          ["float", "sink"]),
        C("ice-floats", "giveaway", "Ice has less of it than liquid water, so ice floats",
          ["ice floats", "liquid water"], "Ice"),
        C("rho", "giveaway", "Symbolized by the Greek letter rho (ρ)",
          ["rho", "greek letter"]),
        C("four-degrees", "middle", "Liquid water has the most of it at about 4 °C, so the bottom of a deep lake stays near 4 °C in winter",
          ["4 °c", "deep lake", "winter"], "Water"),
        C("archimedes", "middle", "In the traditional story, Archimedes used it to test King Hiero’s gold crown and shouted “Eureka!” in the bath",
          ["archimedes", "crown", "eureka"]),
        C("displacement", "middle", "Find an irregular object’s volume by the water it pushes aside in a graduated cylinder",
          ["graduated cylinder", "pushes aside"]),
        C("saturn", "middle", "Saturn is the only planet with less of it than water; Earth has the most of any planet",
          ["saturn", "earth"], "Saturn"),
        C("osmium", "middle", "Osmium has the highest value of any element, just ahead of iridium",
          ["osmium", "iridium"]),
        C("specific-gravity", "middle", "Specific gravity compares it with water’s value, giving a unitless number",
          ["specific gravity", "unitless"]),
        C("hydrometer", "middle", "A hydrometer floats higher in liquids with more of it",
          ["hydrometer", "floats higher"], "Liquids"),
        C("hot-air", "middle", "Heating a gas lowers it, so hot-air balloons rise",
          ["hot-air balloons", "heating"]),
        C("salt-water", "middle", "Salt water has more of it than fresh water, so people float easily in the Dead Sea",
          ["dead sea", "salt water"]),
        C("cavendish", "power", "Henry Cavendish (1798), “weighing the world,” found Earth’s average value is about 5.5 times water’s",
          ["cavendish", "1798", "weighing the world"]),
        C("lithium", "power", "Lithium has the lowest value of any metal and can float on water",
          ["lithium", "lowest"]),
        C("mercury", "power", "Iron and lead cannonballs float on liquid mercury (about 13.5 times water’s value), but gold sinks in it",
          ["mercury", "cannonballs", "gold"]),
        C("galileo", "power", "A Galileo thermometer’s tagged glass bulbs rise or sink as the liquid’s value changes with temperature",
          ["galileo thermometer", "glass bulbs"]),
        C("submarines", "power", "Submarines flood or empty ballast tanks, and fish adjust swim bladders, to change their overall value",
          ["ballast tanks", "swim bladders", "submarines"]),
        C("thermohaline", "power", "Cold, salty water sinks in the North Atlantic, helping drive the thermohaline circulation",
          ["thermohaline", "north atlantic"], "Ocean currents"),
        C("neutron-star", "power", "A neutron star squeezes more mass than the Sun into a ball about the size of a city",
          ["neutron star", "city"], "Neutron stars"),
        C("soda", "power", "Regular soda cans usually sink in water while diet soda cans float, because of dissolved sugar",
          ["diet soda", "sugar"]),
        C("hydrogen-bonds", "power", "Hydrogen bonds hold ice in an open, six-sided pattern, so water expands about 9% when it freezes",
          ["hydrogen bonds", "six-sided", "expands"], "Hydrogen bonds"),
        C("kilogram", "power", "The kilogram was first based on the mass of one liter of water",
          ["kilogram", "liter"]),
        C("vitruvius", "power", "The crown story was told by the Roman writer Vitruvius",
          ["vitruvius", "roman writer"]),
        C("air-water", "power", "Water has roughly 800 times as much of it as air at sea level",
          ["800 times", "sea level"]),
        C("osmium-lead", "power", "A block of osmium has about twice the mass of a lead block the same size",
          ["twice the mass", "lead block"])
    ],
    "trap": {
        "title": "Not mass, not volume",
        "body": "This quantity is built from two others, mass and volume, and tossups mention both, so players blurt one of them. Mass is how much matter an object has and volume is how much space it takes up; this answer is the ratio between them. Buoyancy, the upward push of a fluid, shows up in the same questions but is a separate answer, and “specific gravity” earns only a prompt.",
        "fix": "Mass divided by volume, grams per cubic centimeter, rho, floating and sinking, and ice floating point to this answer. If the question asks for “this upward force,” say buoyancy instead.",
        "line": "Real answer line: <b><u>density</u></b> (accept <u>mass density</u>; prompt on <u>specific gravity</u>, <u>relative density</u>, or <u>rho</u>; do not accept “mass” or “volume”)"
    },
    "tests": {
        "right": [
            "Density",
            "density",
            "Densty",
            "Mass density",
            "Densities"
        ],
        "prompt": [
            "Specific gravity",
            "Rho"
        ],
        "wrong": [
            "Mass",
            "Volume",
            "Weight",
            "Buoyancy",
            "Population density"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
