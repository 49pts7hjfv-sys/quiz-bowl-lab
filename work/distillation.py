import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "distillation",
    "name": "Distillation",
    "mono": "DST",
    "category": "Chemistry",
    "qbCategory": "Science · Chemistry",
    "kicker": "Separation technique · Boiling a mixture, then condensing the vapor",
    "dates": "Used since ancient times",
    "briefing": "Distillation separates the parts of a liquid mixture by boiling it and then cooling the vapor back into a liquid in a separate container. Because each substance boils at its own temperature, the ones with lower boiling points escape first. Oil refineries use giant towers to split crude oil into gasoline, jet fuel, and diesel, and some dry countries use distillation to turn seawater into fresh drinking water.",
    "answerHtml": "<b><u>Distillation</u></b> (accept <u>distilling</u>; accept specific types such as <u>fractional distillation</u> or <u>steam distillation</u>; prompt on <u>fractionation</u>)",
    "accept": [
        "distillation",
        "distillations",
        "distilling",
        "fractional distillation",
        "simple distillation",
        "steam distillation",
        "vacuum distillation"
    ],
    "prompt": [
        "fractionation"
    ],
    "reject": [
        "evaporation",
        "evaporating",
        "condensation",
        "boiling",
        "vaporization",
        "sublimation",
        "filtration",
        "chromatography",
        "crystallization",
        "decantation",
        "centrifugation",
        "desalination",
        "distilled water",
        "distillery",
        "distillate",
        "instillation",
        "titration",
        "extraction",
        "solvent extraction",
        "fermentation",
        "reverse osmosis",
        "osmosis",
        "cracking",
        "reflux",
        "boiling point",
        "vapor pressure",
        "condenser",
        "separation"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Distillation",
    "qb": {
        "q": "distillation",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "The McCabe–Thiele method uses a graph to estimate how many theoretical plates a column needs to carry out this process. Each theoretical plate stands for one stage in which vapor and liquid reach equilibrium with each other.",
            "r": "For 10 points, name this technique that separates liquids by boiling a mixture and condensing the vapor."
        },
        {
            "p": "The alchemist Maria the Jewess is credited with inventing the tribikos, a three-armed device for this process, as well as the water bath now called a bain-marie [“ban-muh-REE”]. Alchemists in Roman-era Egypt wrote some of the earliest descriptions of equipment for this process.",
            "r": "For 10 points, name this ancient technique that separates liquids by boiling a mixture and cooling the vapor."
        },
        {
            "p": "In a Liebig [“LEE-big”] condenser used for this process, cold water enters the outer jacket at the bottom and leaves at the top, flowing opposite to the hot vapor. The thermometer for this process is placed with its bulb level with the side arm, so it measures the temperature of the vapor.",
            "r": "The purified liquid drips into a receiving flask. For 10 points, name this lab technique that separates a liquid mixture using differences in boiling points."
        },
        {
            "p": "A Vigreux [“vee-GRUH”] column, a glass tube with many inward-pointing dents, is used in the fractional form of this process, giving rising vapor more surfaces on which to condense and boil again. Each time the vapor condenses and boils again, it becomes richer in the liquid with the lower boiling point.",
            "r": "Oil refineries use tall towers for this process to separate crude oil into gasoline, kerosene, and diesel. For 10 points, name this technique that separates liquids by their boiling points."
        },
        {
            "p": "Carl von Linde built machines that turned air into a liquid, which could then be separated into nitrogen, argon, and oxygen by the fractional form of this process. Nitrogen comes off first in that separation because it boils at the lowest temperature of the three.",
            "r": "For 10 points, name this process that separates a mixture by boiling it and condensing the vapors."
        },
        {
            "p": "Perfume makers use the “steam” form of this process to pull fragrant essential oils out of plants like lavender, because steam carries the oils over at temperatures below their normal boiling points. Lowering the pressure in the “vacuum” form of this process lets heat-sensitive substances boil at lower temperatures.",
            "r": "For 10 points, name this technique that separates the parts of a liquid mixture by boiling it and condensing the vapor."
        },
        {
            "p": "A rotary evaporator quickly removes solvents from a sample using a low-pressure version of this process, spinning the flask to spread the liquid into a thin film. Boiling chips are often added before this process to prevent violent bursts of boiling called bumping.",
            "r": "For 10 points, name this process in which a mixture is boiled and its vapor is cooled in a condenser."
        },
        {
            "p": "Raoult’s [“rah-OOLZ”] law helps explain why the vapor above a boiling mixture is richer in its more volatile liquid, the key idea behind this process. Repeating this process on the collected liquid can make it purer each time.",
            "r": "For 10 points, name this separation technique based on differences in boiling points, which uses a condenser to turn vapor back into liquid."
        },
        {
            "p": "In a refinery tower used for this process, small molecules such as propane rise to the top, while thick, heavy leftovers like asphalt stay near the bottom. Gasoline, kerosene, and diesel are drawn off as separate fractions at different heights in between.",
            "r": "For 10 points, name this process that uses differences in boiling points to separate crude oil and other liquid mixtures."
        },
        {
            "p": "Multi-stage flash plants in the Middle East turn seawater into fresh water using this process, which leaves the salt behind. A simple solar version of this process lets sunlight evaporate water under a plastic sheet, where the vapor condenses and drips into a cup.",
            "r": "For 10 points, name this purification process in which a liquid is boiled and its vapor is condensed and collected."
        },
        {
            "p": "A Dean–Stark trap uses this process to pull water out of a reaction as it forms, with help from a solvent like toluene that boils off together with the water. In the lab version of this process, vapor travels from a heated flask through a condenser into a receiving flask.",
            "r": "Crude oil is separated into fuels by this technique. For 10 points, name this separation technique based on differences in boiling points."
        },
        {
            "p": "Medieval chemists in the Islamic world used a device called the alembic to perform this process and make rose water. The alembic’s heated pot held the mixture, while its head caught the rising vapor and sent it down a spout. The word “alembic” comes from Arabic, which took it from Greek.",
            "r": "This technique uses a condenser to turn vapor back into a liquid. For 10 points, name this technique that separates the parts of a liquid mixture by boiling and condensing."
        },
        {
            "p": "Ethanol cannot be completely separated from water by this process, because the two form a constant-boiling mixture called an azeotrope [“ay-ZEE-uh-trope”], whose vapor has the same makeup as the liquid. To get pure ethanol, chemists can add a third liquid, such as benzene, that changes how the mixture boils.",
            "r": "Lab glassware for this process includes a heated flask, a condenser, and a receiving flask. For 10 points, name this technique for separating liquids by boiling point."
        },
        {
            "p": "The simple form of this process works well when two liquids have very different boiling points, but the fractional form is needed when their boiling points are close together. Water purified by this process is used in car batteries and science labs.",
            "r": "For 10 points, name this technique that purifies liquids by boiling them and condensing the vapor."
        },
        {
            "p": "Unlike refluxing, in which condensed vapor drips back into the boiling flask, this process collects the condensed vapor in a separate container. Large columns for this process send part of the condensed liquid back down the column to improve the separation.",
            "r": "For 10 points, name this technique used to purify water, separate crude oil, and isolate essential oils by boiling and condensing."
        }
    ],
    "clues": [
        {
            "id": "definition",
            "tier": "giveaway",
            "t": "Separates a liquid mixture by boiling it and condensing the vapor in a separate container",
            "k": ["boiling", "condensing", "separate container"],
            "n": 0
        },
        {
            "id": "boiling-points",
            "tier": "giveaway",
            "t": "Works because each substance has its own boiling point; lower-boiling liquids come off first",
            "k": ["boiling point", "lower-boiling"],
            "n": 0,
            "rabbit": "Boiling point"
        },
        {
            "id": "crude-oil",
            "tier": "giveaway",
            "t": "Oil refineries use tall towers to split crude oil into gasoline, kerosene, and diesel",
            "k": ["crude oil", "refineries", "gasoline"],
            "n": 0
        },
        {
            "id": "seawater",
            "tier": "giveaway",
            "t": "Turns seawater into fresh drinking water by leaving the salt behind",
            "k": ["seawater", "salt", "drinking water"],
            "n": 0
        },
        {
            "id": "condenser",
            "tier": "giveaway",
            "t": "A condenser cools the vapor back into a liquid, which drips into a receiving flask",
            "k": ["condenser", "receiving flask"],
            "n": 0
        },
        {
            "id": "fractional",
            "tier": "middle",
            "t": "The fractional form uses a column for liquids with close boiling points; the vapor condenses and boils again many times",
            "k": ["fractional", "column", "close boiling points"],
            "n": 0
        },
        {
            "id": "simple",
            "tier": "middle",
            "t": "The simple form works when the liquids’ boiling points are far apart",
            "k": ["simple form", "far apart"],
            "n": 0
        },
        {
            "id": "liebig",
            "tier": "middle",
            "t": "Liebig condenser: cold water flows into the jacket at the bottom and out the top, opposite the vapor",
            "k": ["liebig", "jacket", "cold water"],
            "n": 0
        },
        {
            "id": "thermometer",
            "tier": "middle",
            "t": "The thermometer bulb sits level with the side arm to read the vapor’s temperature",
            "k": ["thermometer", "side arm"],
            "n": 0
        },
        {
            "id": "boiling-chips",
            "tier": "middle",
            "t": "Boiling chips prevent violent bursts of boiling called bumping",
            "k": ["boiling chips", "bumping"],
            "n": 0
        },
        {
            "id": "steam",
            "tier": "middle",
            "t": "The steam form pulls essential oils out of plants like lavender for perfumes",
            "k": ["steam", "essential oils", "lavender"],
            "n": 0
        },
        {
            "id": "vacuum",
            "tier": "middle",
            "t": "The vacuum form lowers the pressure so heat-sensitive substances boil at lower temperatures",
            "k": ["vacuum", "heat-sensitive", "pressure"],
            "n": 0
        },
        {
            "id": "liquid-air",
            "tier": "middle",
            "t": "Liquid air is separated into nitrogen, argon, and oxygen this way; nitrogen boils off first",
            "k": ["liquid air", "nitrogen", "argon"],
            "n": 0
        },
        {
            "id": "refinery-tower",
            "tier": "middle",
            "t": "In a refinery tower, gases like propane exit at the top and asphalt stays at the bottom",
            "k": ["propane", "asphalt", "refinery tower"],
            "n": 0
        },
        {
            "id": "pure-water",
            "tier": "middle",
            "t": "Water purified this way is used in car batteries and science labs",
            "k": ["car batteries", "purified", "labs"],
            "n": 0
        },
        {
            "id": "azeotrope",
            "tier": "power",
            "t": "Azeotropes, like ethanol and water, boil with a vapor that has the same makeup as the liquid, so they cannot be fully separated",
            "k": ["azeotropes", "azeotrope", "ethanol"],
            "n": 0
        },
        {
            "id": "benzene",
            "tier": "power",
            "t": "Adding a third liquid, such as benzene, helps make pure ethanol",
            "k": ["benzene", "third liquid", "pure ethanol"],
            "n": 0
        },
        {
            "id": "raoult",
            "tier": "power",
            "t": "Raoult’s law explains why the vapor is richer in the more volatile liquid",
            "k": ["raoult", "volatile"],
            "n": 0,
            "rabbit": "Vapor pressure"
        },
        {
            "id": "mccabe-thiele",
            "tier": "power",
            "t": "The McCabe–Thiele method is a graph for finding how many theoretical plates a column needs",
            "k": ["mccabe–thiele", "theoretical plates"],
            "n": 0
        },
        {
            "id": "vigreux",
            "tier": "power",
            "t": "A Vigreux column has inward-pointing glass dents that give the vapor more surfaces",
            "k": ["vigreux", "dents"],
            "n": 0
        },
        {
            "id": "maria",
            "tier": "power",
            "t": "Maria the Jewess is credited with the three-armed tribikos and the bain-marie water bath",
            "k": ["maria the jewess", "tribikos", "bain-marie"],
            "n": 0
        },
        {
            "id": "alembic",
            "tier": "power",
            "t": "Medieval chemists in the Islamic world made rose water with the alembic, a word that came from Greek through Arabic",
            "k": ["alembic", "rose water", "arabic"],
            "n": 0
        },
        {
            "id": "linde",
            "tier": "power",
            "t": "Carl von Linde built machines that turned air into a liquid so it could be separated",
            "k": ["linde", "air into a liquid"],
            "n": 0
        },
        {
            "id": "rotary",
            "tier": "power",
            "t": "A rotary evaporator removes solvents with a spinning, low-pressure version",
            "k": ["rotary evaporator", "spinning"],
            "n": 0
        },
        {
            "id": "dean-stark",
            "tier": "power",
            "t": "A Dean–Stark trap removes water from a reaction with help from toluene",
            "k": ["dean–stark", "toluene"],
            "n": 0
        },
        {
            "id": "multi-stage",
            "tier": "power",
            "t": "Multi-stage flash plants in the Middle East make fresh water; a simple solar version drips water from a plastic sheet into a cup",
            "k": ["multi-stage flash", "middle east", "solar"],
            "n": 0
        },
        {
            "id": "reflux",
            "tier": "power",
            "t": "Unlike refluxing, where condensed vapor drips back into the flask, it collects the liquid separately; big columns send some liquid back down",
            "k": ["refluxing", "reflux", "separately"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Whole process, not one step",
        "body": "Tossups on this technique are full of its steps, like boiling, vaporizing, and condensing, so players blurt “evaporation” or “condensation.” Those are only parts of the process, and evaporation alone lets the vapor escape instead of collecting it. Other separation methods are traps too: filtration pours a mixture through filter paper, and chromatography separates substances as a solvent carries them along paper or through a column.",
        "fix": "If the clues involve boiling points, condensers, fractions of crude oil, or azeotropes, answer distillation; specific types such as “fractional” or “steam” distillation are also accepted. Filter paper means filtration, and spots moving up paper means chromatography.",
        "line": "Real answer line: <b><u>Distillation</u></b> (accept <u>fractional distillation</u> and other specific types; prompt on <u>fractionation</u>)"
    },
    "tests": {
        "right": [
            "Distillation",
            "fractional distillation",
            "Distilation",
            "steam distillation",
            "distilling"
        ],
        "prompt": [
            "Fractionation"
        ],
        "wrong": [
            "Evaporation",
            "Condensation",
            "Filtration",
            "Chromatography",
            "Distilled water",
            "Boiling",
            "Instillation"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
