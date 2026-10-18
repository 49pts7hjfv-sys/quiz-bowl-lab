import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "ideal-gas-law",
    "name": "Ideal gas law",
    "mono": "IGL",
    "category": "Chemistry",
    "qbCategory": "Science · Chemistry",
    "kicker": "PV = nRT · How a gas’s pressure, volume, and temperature are linked",
    "dates": "First stated by Émile Clapeyron, 1834",
    "briefing": "The ideal gas law ties together four things you can measure about a gas: its pressure, its volume, its temperature, and how many moles of it there are. Written PV = nRT, it combines older laws discovered by Robert Boyle, Jacques Charles, and Amedeo Avogadro. It describes an imaginary “ideal” gas whose particles take up no space and never attract one another, yet real gases such as air follow it closely under everyday conditions.",
    "answerHtml": "<b><u>Ideal gas</u></b> law (accept <u>PV = nRT</u> or <u>ideal gas</u> equation; prompt on <u>gas law</u>)",
    "accept": [
        "ideal gas law",
        "ideal gas laws",
        "ideal gas",
        "ideal gases",
        "ideal gas equation",
        "pv nrt",
        "pv equals nrt",
        "perfect gas law",
        "perfect gas",
        "general gas equation"
    ],
    "prompt": [
        "gas law",
        "gas laws",
        "gas equation",
        "equation of state"
    ],
    "reject": [
        "boyles law",
        "boyle law",
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
        "grahams law",
        "henrys law",
        "raoults law",
        "combined gas law",
        "van der waals equation",
        "van der waals",
        "real gas",
        "real gases",
        "real gas law",
        "gas constant",
        "ideal gas constant",
        "universal gas constant",
        "boltzmann constant",
        "avogadros number",
        "kinetic molecular theory",
        "kinetic theory",
        "kinetic theory of gases",
        "clausius clapeyron equation",
        "clausius clapeyron",
        "virial equation",
        "compressibility factor",
        "ideal solution",
        "noble gas",
        "noble gases",
        "first law of thermodynamics"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Ideal_gas_law",
    "qb": {
        "q": "ideal gas",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "For a gas that obeys this law exactly, the molar heat capacity at constant pressure minus the molar heat capacity at constant volume equals this law’s constant, a result called Mayer’s relation. Such a gas does not change temperature when it expands freely into a vacuum.",
            "r": "For 10 points, name this law relating a gas’s pressure, volume, temperature, and number of moles."
        },
        {
            "p": "Émile Clapeyron [“klah-pay-RAWN”] first stated this law in 1834 by combining earlier laws named for Robert Boyle and Jacques Charles. In its modern form, this law also includes Avogadro’s law through a term for the number of moles.",
            "r": "For 10 points, name this law often summarized as pressure times volume equals moles times R times temperature."
        },
        {
            "p": "Johannes van der Waals won the 1910 Nobel Prize in Physics for an equation that corrects this law, using one constant for the attractions between molecules and another for the space the molecules take up.",
            "r": "Real gases obey this law poorly at high pressures and low temperatures. For 10 points, name this law relating pressure, volume, moles, and temperature."
        },
        {
            "p": "A gas’s compressibility factor compares its actual pressure-volume product with the value this law predicts, and it equals exactly 1 for a gas that obeys this law. At a temperature called the Boyle temperature, a real gas follows this law well over a wide range of pressures.",
            "r": "For 10 points, name this equation of state that combines Boyle’s law, Charles’s law, and Avogadro’s law."
        },
        {
            "p": "Writing this law in terms of the number of molecules instead of moles replaces its usual constant with the Boltzmann constant. That usual constant, about 8.314 joules per mole per kelvin, is called the gas constant and is written R.",
            "r": "For 10 points, name this law that relates the pressure, volume, temperature, and amount of a gas."
        },
        {
            "p": "The kinetic molecular theory explains this law by assuming that gas particles take up no volume, never attract or repel one another, and bounce off each other in perfectly elastic collisions. Real gases follow this law best at high temperatures and low pressures.",
            "r": "For 10 points, name this gas law, written with the letters P, V, n, R, and T."
        },
        {
            "p": "Rearranging this law shows that a gas’s density depends on its molar mass, so chemists can find an unknown gas’s molar mass by measuring its density. This law predicts that one mole of any gas at 0 degrees Celsius and 1 atmosphere fills about 22.4 liters.",
            "r": "For 10 points, name this law, which combines the simpler gas laws into one equation with the constant R."
        },
        {
            "p": "Daniel Bernoulli’s 1738 book _Hydrodynamica_ explained gas pressure as the result of countless tiny particles hitting the walls of their container, an early step toward explaining this law. In this law, temperature must be measured in kelvins, starting from absolute zero.",
            "r": "For 10 points, name this law that combines Boyle’s law and Charles’s law with Avogadro’s law."
        },
        {
            "p": "The internal energy of a gas that perfectly obeys this law depends only on its temperature, so such a gas would show no Joule–Thomson effect, the temperature change of a gas forced through a valve. Real gases differ from this law because their molecules attract one another and take up space.",
            "r": "For 10 points, name this law, which states that pressure times volume equals moles times the gas constant times temperature."
        },
        {
            "p": "For a reversible adiabatic process, a gas obeying this law keeps the product of its pressure and its volume raised to the power gamma constant, where gamma is the ratio of its heat capacities. At constant temperature, this law reduces to Boyle’s law.",
            "r": "For 10 points, name this gas law that relates pressure, volume, temperature, and the number of moles."
        },
        {
            "p": "Guillaume Amontons [“ah-mohn-TOHN”] noticed long before Gay-Lussac that a gas’s pressure rises with its temperature when its volume is held fixed, a rule built into this law. According to this law, heating the air inside a hot-air balloon makes that air less dense, so the balloon rises.",
            "r": "For 10 points, name this law relating pressure, volume, temperature, and the number of moles of a gas."
        },
        {
            "p": "Constant-volume gas thermometers rely on this law, and extending straight-line graphs of a gas’s volume against its temperature down to zero volume points to absolute zero, about −273 degrees Celsius. In 1802, Joseph Louis Gay-Lussac published measurements showing that different gases expand by the same fraction when heated, a finding built into this law.",
            "r": "For 10 points, name this gas law, in which temperature must be measured in kelvins rather than degrees Celsius."
        },
        {
            "p": "The virial [“VEER-ee-ul”] equation of state adds a series of correction terms to this law, which is the first term of that series. Since 2019, this law’s constant has had an exact value, because the Avogadro and Boltzmann constants were fixed exactly.",
            "r": "For 10 points, name this law, whose constant R is about 0.0821 liter-atmospheres per mole per kelvin."
        },
        {
            "p": "Dalton’s law of partial pressures can be derived from this law for mixtures of gases, since each gas pushes in proportion to its number of moles. No real gas obeys this law perfectly, because real molecules have size and attract one another, though helium comes very close.",
            "r": "Its constant, R, is called the gas constant. For 10 points, name this law relating a gas’s pressure, volume, temperature, and amount."
        },
        {
            "p": "In a gas that obeys this law, the average translational kinetic energy of a molecule is three-halves times the Boltzmann constant times the temperature. At constant pressure, this law says that doubling a gas’s kelvin temperature doubles its volume.",
            "r": "Chemists use it to relate a gas’s pressure, volume, and temperature. For 10 points, name this law that combines Boyle’s, Charles’s, and Avogadro’s laws."
        }
    ],
    "clues": [
        {
            "id": "formula",
            "tier": "giveaway",
            "t": "Pressure times volume equals moles times the gas constant R times temperature",
            "k": ["temperature", "pressure", "volume", "moles"],
            "n": 0
        },
        {
            "id": "combines",
            "tier": "giveaway",
            "t": "Combines Boyle’s law, Charles’s law, and Avogadro’s law (plus Gay-Lussac’s law)",
            "k": ["combines", "boyle", "charles", "avogadro"],
            "n": 0,
            "rabbit": "Boyle’s law"
        },
        {
            "id": "kelvins",
            "tier": "giveaway",
            "t": "Temperature must be measured in kelvins, starting from absolute zero",
            "k": ["kelvins", "absolute zero"],
            "n": 0,
            "rabbit": "Absolute zero"
        },
        {
            "id": "constant-r",
            "tier": "giveaway",
            "t": "Its constant R is about 8.314 joules per mole per kelvin, or 0.0821 liter-atmospheres per mole per kelvin",
            "k": ["8.314", "0.0821", "constant r"],
            "n": 0,
            "rabbit": "Gas constant"
        },
        {
            "id": "hypothetical",
            "tier": "giveaway",
            "t": "Describes a hypothetical gas whose particles take up no space and never attract one another",
            "k": ["hypothetical", "no space", "never attract"],
            "n": 0
        },
        {
            "id": "real-gases",
            "tier": "middle",
            "t": "Real gases follow it best at high temperature and low pressure and stray from it at high pressure and low temperature",
            "k": ["high temperature", "low pressure", "stray"],
            "n": 0
        },
        {
            "id": "van-der-waals",
            "tier": "middle",
            "t": "Johannes van der Waals corrected it with one constant for attractions and one for molecule size (1910 Nobel Prize in Physics)",
            "k": ["van der waals", "attractions", "1910"],
            "n": 0,
            "rabbit": "Van der Waals forces"
        },
        {
            "id": "kmt",
            "tier": "middle",
            "t": "Kinetic molecular theory explains it: tiny particles in random motion with perfectly elastic collisions",
            "k": ["kinetic molecular theory", "elastic collisions"],
            "n": 0
        },
        {
            "id": "molar-volume",
            "tier": "middle",
            "t": "One mole of gas at 0 degrees Celsius and 1 atmosphere fills about 22.4 liters",
            "k": ["22.4 liters", "one mole"],
            "n": 0,
            "rabbit": "Avogadro’s number"
        },
        {
            "id": "boltzmann",
            "tier": "middle",
            "t": "Written for molecules instead of moles, its constant becomes the Boltzmann constant",
            "k": ["boltzmann constant", "molecules"],
            "n": 0
        },
        {
            "id": "clapeyron",
            "tier": "middle",
            "t": "Émile Clapeyron first stated it in 1834, combining Boyle’s and Charles’s laws",
            "k": ["clapeyron", "1834"],
            "n": 0
        },
        {
            "id": "density",
            "tier": "middle",
            "t": "Rearranged, it lets chemists find a gas’s molar mass from its density",
            "k": ["molar mass", "density"],
            "n": 0
        },
        {
            "id": "balloon",
            "tier": "middle",
            "t": "Heated air at constant pressure becomes less dense, so hot-air balloons rise",
            "k": ["hot-air balloons", "less dense"],
            "n": 0
        },
        {
            "id": "dalton",
            "tier": "middle",
            "t": "Dalton’s law of partial pressures can be derived from it for gas mixtures",
            "k": ["partial pressures", "dalton"],
            "n": 0
        },
        {
            "id": "compressibility",
            "tier": "power",
            "t": "The compressibility factor compares a gas’s actual pressure-volume product with its prediction; it equals exactly 1 for a gas that obeys it",
            "k": ["compressibility factor", "exactly 1"],
            "n": 0
        },
        {
            "id": "boyle-temperature",
            "tier": "power",
            "t": "At the Boyle temperature, a real gas obeys it well over a wide range of pressures",
            "k": ["boyle temperature", "wide range"],
            "n": 0
        },
        {
            "id": "virial",
            "tier": "power",
            "t": "It is the simplest equation of state; the virial equation adds a series of correction terms to it",
            "k": ["virial", "equation of state", "correction terms"],
            "n": 0
        },
        {
            "id": "mayer",
            "tier": "power",
            "t": "Mayer’s relation: a gas’s molar heat capacities at constant pressure and at constant volume differ by its constant R",
            "k": ["mayer", "heat capacities"],
            "n": 0
        },
        {
            "id": "free-expansion",
            "tier": "power",
            "t": "Its internal energy depends only on temperature, so it shows no temperature change expanding into a vacuum and no Joule–Thomson effect",
            "k": ["internal energy", "joule–thomson", "vacuum"],
            "n": 0
        },
        {
            "id": "adiabatic",
            "tier": "power",
            "t": "In a reversible adiabatic process, pressure times volume raised to the power gamma stays constant",
            "k": ["adiabatic", "gamma"],
            "n": 0
        },
        {
            "id": "bernoulli",
            "tier": "power",
            "t": "Daniel Bernoulli’s 1738 _Hydrodynamica_ explained gas pressure as particles hitting the walls of their container",
            "k": ["bernoulli", "hydrodynamica", "1738"],
            "n": 0
        },
        {
            "id": "amontons",
            "tier": "power",
            "t": "Guillaume Amontons noticed long before Gay-Lussac that pressure rises with temperature at a fixed volume",
            "k": ["amontons", "fixed volume"],
            "n": 0
        },
        {
            "id": "gay-lussac",
            "tier": "power",
            "t": "In 1802, Joseph Louis Gay-Lussac showed that different gases expand by the same fraction when heated",
            "k": ["gay-lussac", "1802", "same fraction"],
            "n": 0
        },
        {
            "id": "gas-thermometer",
            "tier": "power",
            "t": "Constant-volume gas thermometers rely on it; extending volume-temperature lines to zero volume points to absolute zero, about −273 degrees Celsius",
            "k": ["gas thermometers", "−273"],
            "n": 0
        },
        {
            "id": "kinetic-energy",
            "tier": "power",
            "t": "A molecule’s average translational kinetic energy is three-halves the Boltzmann constant times the temperature",
            "k": ["three-halves", "kinetic energy"],
            "n": 0,
            "rabbit": "Kinetic Energy"
        },
        {
            "id": "exact-r",
            "tier": "power",
            "t": "Since 2019, its constant R has an exact value, because the Avogadro and Boltzmann constants were fixed",
            "k": ["2019", "exact value"],
            "n": 0
        },
        {
            "id": "helium-closest",
            "tier": "power",
            "t": "No real gas obeys it perfectly, but helium comes very close",
            "k": ["helium", "perfectly"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Whole law, not a piece",
        "body": "This law is built from simpler gas laws, so its clues often mention Boyle’s law (pressure and volume), Charles’s law (volume and temperature), or Avogadro’s law (volume and moles). Those are separate answer lines, and so is the gas constant, R, which is only one part of this equation. The combined gas law is a trap too: it links pressure, volume, and temperature but leaves out the number of moles.",
        "fix": "If the clues include all four quantities, the constant R, real-gas corrections like van der Waals’s, or the kinetic molecular theory’s assumptions, answer with the full law. A few tossups ask for the imaginary gas itself, the “ideal gas,” which is also accepted.",
        "line": "Real answer line: <b><u>Ideal gas</u></b> law (accept <u>PV = nRT</u>; prompt on <u>gas law</u>)"
    },
    "tests": {
        "right": [
            "Ideal gas law",
            "PV = nRT",
            "ideal gas",
            "Ideal gas equation",
            "idael gas law",
            "pv=nrt"
        ],
        "prompt": [
            "Gas law"
        ],
        "wrong": [
            "Boyle’s law",
            "Combined gas law",
            "Gas constant",
            "Van der Waals equation",
            "Real gas",
            "Charles’s law",
            "Kinetic molecular theory"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
