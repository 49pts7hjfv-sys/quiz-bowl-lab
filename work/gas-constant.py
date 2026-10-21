import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TIP = "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."

LINE = "<b><u>Gas constant</u></b> (accept <u>R</u>, ideal <u>gas constant</u>, universal <u>gas constant</u>, or molar <u>gas constant</u>; do not accept “Boltzmann constant” or “Avogadro’s number”)"

data = {
    "id": "gas-constant",
    "name": "Gas constant",
    "mono": "R",
    "category": "Chemistry",
    "qbCategory": "Science · Chemistry",
    "kicker": "The R in PV = nRT · About 8.314 joules per mole per kelvin",
    "dates": "Exact value fixed in 2019",
    "briefing": "The gas constant, written R, is the number that makes the ideal gas law work: pressure times volume equals moles times R times temperature. It equals about 8.314 joules per mole per kelvin, or about 0.0821 liter-atmospheres per mole per kelvin, and it is really Boltzmann’s constant scaled up to a whole mole. R also turns up in equations for reaction rates, battery voltages, and chemical equilibrium.",
    "answerHtml": LINE,
    "accept": [
        "gas constant",
        "the gas constant",
        "ideal gas constant",
        "the ideal gas constant",
        "universal gas constant",
        "molar gas constant",
        "r",
        "gas constant r",
        "constant r",
        "r constant"
    ],
    "prompt": [],
    "reject": [
        "boltzmann constant",
        "boltzmanns constant",
        "boltzmann",
        "k",
        "kb",
        "k sub b",
        "avogadros number",
        "avogadros constant",
        "avogadro constant",
        "avogadro number",
        "avogadro",
        "na",
        "faraday constant",
        "faradays constant",
        "faraday",
        "planck constant",
        "plancks constant",
        "rydberg constant",
        "rydberg",
        "gravitational constant",
        "universal gravitational constant",
        "coulomb constant",
        "coulombs constant",
        "stefan boltzmann constant",
        "equilibrium constant",
        "rate constant",
        "dielectric constant",
        "ideal gas law",
        "gas law",
        "gas laws",
        "pv nrt",
        "pv equals nrt",
        "boyles law",
        "charles law",
        "combined gas law",
        "van der waals constant",
        "van der waals constants",
        "molar volume",
        "speed of light",
        "c"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Gas_constant",
    "qb": {"q": "gas constant", "found": 0, "tip": TIP},
    "sample": {"n": 0, "note": "no real tossups checked yet"},
    "tossups": [
        {
            "p": "The law of Dulong [“doo-LONG”] and Petit [“puh-TEE”] says that the molar heat capacity of many solid elements is about three times this constant, roughly 25 joules per mole per kelvin. For an ideal monatomic gas, the molar heat capacity at constant volume is three-halves of this constant.",
            "r": "For 10 points, name this constant, about 8.314 joules per mole per kelvin, which appears in the ideal gas law."
        },
        {
            "p": "Mayer’s relation says that for an ideal gas, the molar heat capacity at constant pressure is larger than the one at constant volume by exactly this constant. This constant has the same units as molar entropy: joules per mole per kelvin.",
            "r": "Dividing this constant by Avogadro’s number gives the Boltzmann constant. For 10 points, name this constant in the ideal gas law."
        },
        {
            "p": "In the Nernst equation, this constant times the temperature, divided by Faraday’s constant, gives a voltage of about 25.7 millivolts at 25 degrees Celsius. That combination tells how a cell’s voltage changes as the concentrations of its chemicals change.",
            "r": "For 10 points, name this constant, equal to about 8.314 joules per mole per kelvin, which also appears in the ideal gas law."
        },
        {
            "p": "The standard Gibbs free energy change of a reaction equals the negative of this constant times the absolute temperature times the natural logarithm of the equilibrium constant. This constant also links the equilibrium constants written with pressures and with concentrations.",
            "r": "For 10 points, name this constant, about 0.0821 liter-atmospheres per mole per kelvin, which appears in the ideal gas law."
        },
        {
            "p": "On an Arrhenius [“ar-RAY-nee-us”] plot, the natural log of a rate constant is graphed against one over the absolute temperature, giving a line whose slope is the negative of the activation energy divided by this constant.",
            "r": "Multiplying this constant by temperature and moles gives pressure times volume for an ideal gas. For 10 points, name this constant."
        },
        {
            "p": "Jacobus van ’t Hoff [“vahnt HOFF”], winner of the first Nobel Prize in Chemistry, showed that osmotic pressure equals a solution’s molarity times this constant times the absolute temperature, the same form as a law for gases.",
            "r": "That gas law, first stated by Émile Clapeyron in 1834, also uses this constant. For 10 points, name this constant, about 8.314 joules per mole per kelvin."
        },
        {
            "p": "The root-mean-square speed of gas molecules is the square root of a fraction: three times this constant times the temperature, divided by the molar mass. That formula shows why light helium atoms move much faster than heavy xenon atoms at the same temperature.",
            "r": "It is about 8.314 joules per mole per kelvin. For 10 points, name this constant, which equals Avogadro’s number times the Boltzmann constant."
        },
        {
            "p": "Meteorologists divide this constant by the molar mass of dry air to get a “specific” version, about 287 joules per kilogram per kelvin, for that air. Engineers use similar versions for each individual gas, such as helium or carbon dioxide.",
            "r": "For 10 points, name this universal constant, about 8.314 joules per mole per kelvin, from the ideal gas law."
        },
        {
            "p": "When an ideal gas expands reversibly at constant temperature, the work it does equals the number of moles times this constant times the temperature times the natural log of the ratio of the final volume to the starting volume.",
            "r": "It equals about 8.314 joules per mole per kelvin. For 10 points, name this constant that appears in the ideal gas law."
        },
        {
            "p": "Since the 2019 redefinition of SI units, this constant has had an exact value, because it is the product of two constants that were fixed exactly: Avogadro’s number and the Boltzmann constant.",
            "r": "For 10 points, name this constant that appears in the ideal gas law, written pressure times volume equals moles times this constant times temperature."
        },
        {
            "p": "The Clausius–Clapeyron [“KLOW-zee-us kla-pay-ROHN”] equation, which predicts how a liquid’s vapor pressure rises with temperature, divides the heat of vaporization by this constant. A plot of the natural log of vapor pressure against one over temperature has a slope equal to the negative of that ratio.",
            "r": "For 10 points, name this constant, about 8.314 joules per mole per kelvin, which also appears in the ideal gas law."
        },
        {
            "p": "Johannes van der Waals’s equation for real gases adds a constant a for attractions between molecules and a constant b for the space the molecules themselves take up, but it still multiplies moles and temperature by this third constant.",
            "r": "Because it is the same for every ideal gas, this constant is often called “universal.” For 10 points, name this constant, about 8.314 joules per mole per kelvin."
        },
        {
            "p": "Using this constant, chemists calculate that one mole of any ideal gas at 0 °C and 1 atmosphere fills about 22.4 liters. Rearranging the same law lets chemists find a gas’s molar mass from its density.",
            "r": "It appears in the ideal gas law. For 10 points, name this constant, about 0.0821 liter-atmospheres per mole per kelvin."
        },
        {
            "p": "For a fixed amount of gas, pressure times volume divided by absolute temperature stays the same, a rule called the combined gas law; that ratio equals the number of moles times this constant. Temperatures must be in kelvins when this constant is used.",
            "r": "It appears in the ideal gas law. For 10 points, name this constant, about 8.314 joules per mole per kelvin."
        },
        {
            "p": "This constant has the same number in joules per mole per kelvin as in kilopascal-liters per mole per kelvin, because one kilopascal times one liter equals exactly one joule. In calories, it is close to 2 per mole per kelvin.",
            "r": "In liter-atmospheres per mole per kelvin, it is about 0.0821. For 10 points, name this constant from the ideal gas law."
        }
    ],
    "clues": [
        {
            "id": "ideal-gas-law",
            "tier": "giveaway",
            "t": "The constant in the ideal gas law: pressure times volume equals moles times it times temperature",
            "k": ["ideal gas law", "pressure", "volume"],
            "n": 0,
            "rabbit": "Ideal gas law"
        },
        {
            "id": "value-joules",
            "tier": "giveaway",
            "t": "About 8.314 joules per mole per kelvin",
            "k": ["8.314", "joules"],
            "n": 0
        },
        {
            "id": "value-liter-atm",
            "tier": "giveaway",
            "t": "About 0.0821 liter-atmospheres per mole per kelvin",
            "k": ["0.0821", "liter-atmospheres"],
            "n": 0
        },
        {
            "id": "boltzmann",
            "tier": "giveaway",
            "t": "Equals Avogadro’s number times the Boltzmann constant; written per molecule instead of per mole, it becomes the Boltzmann constant",
            "k": ["avogadro", "boltzmann", "per molecule"],
            "n": 0,
            "rabbit": "Avogadro’s number"
        },
        {
            "id": "kelvins",
            "tier": "giveaway",
            "t": "Temperatures must be in kelvins when it is used",
            "k": ["kelvins"],
            "n": 0
        },
        {
            "id": "units",
            "tier": "middle",
            "t": "Its units, joules per mole per kelvin, are the same as those of molar entropy and molar heat capacity",
            "k": ["molar entropy", "heat capacity"],
            "n": 0
        },
        {
            "id": "arrhenius",
            "tier": "middle",
            "t": "An Arrhenius plot of ln k against 1/T has a slope equal to minus the activation energy divided by it",
            "k": ["arrhenius", "activation energy", "slope"],
            "n": 0,
            "rabbit": "Activation energy"
        },
        {
            "id": "gibbs",
            "tier": "middle",
            "t": "The standard Gibbs free energy change equals minus it times temperature times the natural log of the equilibrium constant",
            "k": ["gibbs", "natural log", "equilibrium constant"],
            "n": 0,
            "rabbit": "Chemical equilibrium"
        },
        {
            "id": "nernst",
            "tier": "middle",
            "t": "In the Nernst equation, it times temperature divided by Faraday’s constant is about 25.7 millivolts at 25 °C",
            "k": ["nernst", "faraday", "millivolts"],
            "n": 0
        },
        {
            "id": "molar-volume",
            "tier": "middle",
            "t": "Using it, one mole of ideal gas at 0 °C and 1 atmosphere fills about 22.4 liters",
            "k": ["22.4 liters", "one mole"],
            "n": 0
        },
        {
            "id": "combined",
            "tier": "middle",
            "t": "In the combined gas law, pressure times volume divided by temperature equals moles times it",
            "k": ["combined gas law"],
            "n": 0
        },
        {
            "id": "mayer",
            "tier": "middle",
            "t": "Mayer’s relation: an ideal gas’s molar heat capacity at constant pressure exceeds the one at constant volume by exactly this amount",
            "k": ["mayer", "constant pressure", "constant volume"],
            "n": 0
        },
        {
            "id": "osmotic",
            "tier": "middle",
            "t": "Van ’t Hoff, winner of the first Chemistry Nobel (1901): osmotic pressure equals molarity times it times temperature",
            "k": ["osmotic pressure", "van ’t hoff", "molarity"],
            "n": 0
        },
        {
            "id": "van-der-waals",
            "tier": "middle",
            "t": "Van der Waals’s real-gas equation adds constants a (attractions) and b (molecule size) but keeps it",
            "k": ["van der waals", "real-gas", "attractions"],
            "n": 0
        },
        {
            "id": "dulong-petit",
            "tier": "power",
            "t": "Dulong–Petit law: many solid elements have a molar heat capacity of about three times it, roughly 25 joules per mole per kelvin",
            "k": ["dulong", "petit", "three times"],
            "n": 0
        },
        {
            "id": "monatomic",
            "tier": "power",
            "t": "An ideal monatomic gas has a molar heat capacity at constant volume of three-halves of it",
            "k": ["monatomic", "three-halves"],
            "n": 0
        },
        {
            "id": "rms-speed",
            "tier": "power",
            "t": "Root-mean-square speed is the square root of 3 times it times temperature, divided by molar mass, so light helium outpaces xenon",
            "k": ["root-mean-square", "helium", "xenon"],
            "n": 0
        },
        {
            "id": "specific-air",
            "tier": "power",
            "t": "Divided by the molar mass of dry air, it gives a “specific” version for air of about 287 joules per kilogram per kelvin",
            "k": ["specific", "dry air", "287"],
            "n": 0
        },
        {
            "id": "isothermal-work",
            "tier": "power",
            "t": "When an ideal gas expands reversibly at constant temperature, its work equals moles times it times temperature times the natural log of the volume ratio",
            "k": ["reversibly", "volume ratio", "work"],
            "n": 0
        },
        {
            "id": "si-2019",
            "tier": "power",
            "t": "Exact since the 2019 SI redefinition, because Avogadro’s number and the Boltzmann constant were fixed exactly",
            "k": ["2019", "redefinition", "exact"],
            "n": 0
        },
        {
            "id": "clausius-clapeyron",
            "tier": "power",
            "t": "The Clausius–Clapeyron equation divides the heat of vaporization by it to predict how vapor pressure rises with temperature",
            "k": ["clausius", "vapor pressure", "heat of vaporization"],
            "n": 0,
            "rabbit": "Vapor pressure"
        },
        {
            "id": "kilopascal-liters",
            "tier": "power",
            "t": "Same number in joules and in kilopascal-liters per mole per kelvin, since one kilopascal-liter is one joule; in calories, about 1.987",
            "k": ["kilopascal", "calories", "1.987"],
            "n": 0
        },
        {
            "id": "clapeyron-1834",
            "tier": "power",
            "t": "Émile Clapeyron first stated the ideal gas law, which uses it, in 1834",
            "k": ["clapeyron", "1834"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Not Boltzmann or Avogadro",
        "body": "Three constants are tied together here: this one equals Avogadro’s number times the Boltzmann constant. The Boltzmann constant, about 1.38 × 10⁻²³ joules per kelvin, does the same job for a single molecule, so answering with it is wrong. The ideal gas law is also a separate answer from the constant inside it.",
        "fix": "“Per mole,” 8.314, 0.0821, and the ideal gas law mean the gas constant, R. “Per molecule” or “per particle,” 1.38 × 10⁻²³, and Boltzmann’s tombstone mean the Boltzmann constant; 6.02 × 10²³ means Avogadro’s number. If the question asks for “this law” or “this equation,” say the ideal gas law instead.",
        "line": "Real answer line: " + LINE
    },
    "tests": {
        "right": [
            "Gas constant",
            "R",
            "ideal gas constant",
            "universal gas constant",
            "the gas constant R",
            "Gas constnat"
        ],
        "prompt": [],
        "wrong": [
            "Boltzmann constant",
            "Avogadro's number",
            "Ideal gas law",
            "Faraday constant",
            "Planck's constant",
            "Rate constant",
            "Equilibrium constant",
            "Rydberg constant"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
