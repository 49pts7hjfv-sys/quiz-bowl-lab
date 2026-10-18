import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "salinity",
    "name": "Salinity",
    "mono": "SAL",
    "category": "Earth Science",
    "qbCategory": "Science · Other Science (Earth Science)",
    "kicker": "How salty water is · The ocean averages about 35 parts per thousand",
    "dates": "Ocean average: about 35 parts per thousand",
    "briefing": "Salinity measures how much salt is dissolved in water. A kilogram of average seawater holds about 35 grams of dissolved salts, mostly sodium and chloride, which works out to about 3.5 percent. Evaporation makes water saltier and rain makes it fresher, and in the Dead Sea, nearly ten times saltier than the ocean, swimmers bob like corks.",
    "answerHtml": "<b><u>Salinity</u></b> (accept <u>saltiness</u>, <u>salt content</u>, or <u>salt concentration</u>; prompt on <u>salt</u>; do not accept “density” or “salinization”)",
    "accept": [
        "salinity",
        "salinities",
        "saltiness",
        "salt content",
        "salt concentration",
        "salt concentrations",
        "concentration of salt",
        "ocean salinity",
        "seawater salinity",
        "sea surface salinity",
        "water salinity",
        "practical salinity",
        "absolute salinity"
    ],
    "prompt": [
        "salt",
        "salts",
        "dissolved salt",
        "dissolved salts",
        "dissolved solids",
        "total dissolved solids"
    ],
    "reject": [
        "salinization",
        "salination",
        "density",
        "seawater density",
        "temperature",
        "chlorinity",
        "halocline",
        "haloclines",
        "thermocline",
        "pycnocline",
        "isohaline",
        "isohalines",
        "thermohaline circulation",
        "brackish",
        "brackish water",
        "brine",
        "salt water",
        "saltwater",
        "sodium chloride",
        "sodium",
        "chloride",
        "halite",
        "osmosis",
        "conductivity",
        "solubility",
        "dead sea",
        "salinometer"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Salinity",
    "qb": {
        "q": "salinity",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "Johan Georg Forchhammer and Alexander Marcet found that the main dissolved substances in seawater keep nearly the same ratios to one another everywhere, even though this property changes from place to place. That rule is called the principle of constant proportions.",
            "r": "For 10 points, name this measure of how much salt is dissolved in water, which averages about 35 parts per thousand in the ocean."
        },
        {
            "p": "William Dittmar analyzed seawater samples collected on the voyage of HMS _Challenger_ and confirmed that sodium, chloride, and other ions keep fixed ratios even when this property changes. Chloride makes up more than half of the dissolved material this property measures.",
            "r": "For 10 points, name this property of seawater, the amount of salt in it, which goes up when water evaporates."
        },
        {
            "p": "Since 1978, oceanographers have reported this property on a unitless “practical” scale based on how well seawater conducts electricity compared with a standard solution of potassium chloride. Instruments called CTDs measure conductivity, temperature, and depth to find it.",
            "r": "For 10 points, name this property of water, the amount of dissolved salt it contains."
        },
        {
            "p": "Before electronic sensors, oceanographers found this property by first measuring chlorinity, adding silver nitrate to seawater to see how much chloride it held. The Danish physicist Martin Knudsen helped set up that method around 1900.",
            "r": "For 10 points, name this property, which averages about 35 parts per thousand in the open ocean."
        },
        {
            "p": "NASA’s Aquarius instrument, launched in 2011 aboard an Argentine satellite, mapped this property across the sea surface by sensing faint microwaves given off by the water. Europe’s SMOS satellite also measures this property from orbit.",
            "r": "For 10 points, name this property of seawater, which rises when water evaporates and leaves its salt behind."
        },
        {
            "p": "Thousands of drifting robots called Argo floats sink as deep as 2,000 meters and then rise, recording temperature and this property along the way. Together, those two measurements let scientists work out the density of the water.",
            "r": "For 10 points, name this measure of how salty water is, usually given in parts per thousand."
        },
        {
            "p": "Because evaporation removes more water than rivers and rain add, the Mediterranean Sea is higher in this property than the Atlantic, so its dense water spills out beneath the Atlantic water flowing in at the Strait of Gibraltar.",
            "r": "For 10 points, name this measure of the dissolved salt in seawater, which averages about 35 parts per thousand."
        },
        {
            "p": "In 1715, Edmond Halley suggested that the age of Earth could be estimated by measuring how fast this property of lakes and the ocean goes up. John Joly later tried that idea using the sodium carried to the sea by rivers, but his answer was far too young.",
            "r": "For 10 points, name this measure of how much salt is dissolved in water, which evaporation raises and rain lowers."
        },
        {
            "p": "Euryhaline animals, like salmon and bull sharks, can survive big changes in this property, while stenohaline animals cannot. Bull sharks have been found far up freshwater rivers like the Mississippi, and salmon move between salty oceans and freshwater rivers during their lives.",
            "r": "For 10 points, name this property of water, which in the open ocean averages about 35 parts per thousand."
        },
        {
            "p": "In a salt-wedge estuary, like the mouth of the Mississippi River, dense seawater slides upstream beneath the river’s fresh water, so this property is much higher near the bottom. Water with an in-between value of this property is called brackish.",
            "r": "For 10 points, name this measure of how much salt is dissolved in water."
        },
        {
            "p": "When sea ice forms in Antarctica’s Weddell Sea, it leaves most of its salt behind in the water below, a process called brine rejection that raises this property. That cold, dense water sinks to form Antarctic Bottom Water.",
            "r": "For 10 points, name this property of seawater that, along with temperature, controls its density and drives the thermohaline circulation."
        },
        {
            "p": "A layer of the ocean where this property changes quickly with depth is called a halocline, and lines on a map that connect places with equal values of this property are called isohalines.",
            "r": "Evaporation raises it, and rain lowers it. For 10 points, name this measure of the salt dissolved in seawater."
        },
        {
            "p": "In the open ocean, this property is highest at the sea surface in the subtropics, about 20 to 30 degrees from the equator, where dry air lets evaporation outpace rainfall. It is lower near the rainy equator and near melting polar ice.",
            "r": "For 10 points, name this measure of how salty seawater is, which averages about 35 parts per thousand."
        },
        {
            "p": "Raising this property lowers the temperature at which water freezes, so ocean water stays liquid a little below 0 °C. Raising it also makes water conduct electricity better, which is how most modern instruments measure it.",
            "r": "The Dead Sea’s value is nearly ten times the ocean’s. For 10 points, name this measure of how salty water is."
        },
        {
            "p": "Rivers slowly add to this property of the ocean by carrying in ions weathered out of rocks on land, and gases from volcanoes add chloride. Sodium and chloride ions make up most of the dissolved material that this property measures.",
            "r": "For 10 points, name this measure of the salt in seawater, which averages about 35 parts per thousand."
        }
    ],
    "clues": [
        {
            "id": "dissolved-salt",
            "tier": "giveaway",
            "t": "The amount of salt dissolved in water",
            "k": ["dissolved", "salt"],
            "n": 0
        },
        {
            "id": "ppt-35",
            "tier": "giveaway",
            "t": "Seawater averages about 35 parts per thousand, or about 3.5 percent",
            "k": ["35 parts per thousand", "3.5 percent"],
            "n": 0
        },
        {
            "id": "evaporation-rain",
            "tier": "giveaway",
            "t": "Raised by evaporation and by sea ice forming; lowered by rain, rivers, and melting ice",
            "k": ["evaporation", "rain", "melting ice"],
            "n": 0
        },
        {
            "id": "dead-sea",
            "tier": "giveaway",
            "t": "The Dead Sea’s value is nearly ten times the ocean’s, so swimmers float easily",
            "k": ["dead sea", "float"],
            "n": 0
        },
        {
            "id": "thermohaline",
            "tier": "giveaway",
            "t": "Along with temperature, it controls seawater density and drives the thermohaline circulation",
            "k": ["thermohaline", "density", "temperature"],
            "n": 0,
            "rabbit": "Ocean currents"
        },
        {
            "id": "halocline",
            "tier": "middle",
            "t": "A layer of the ocean where it changes quickly with depth is called a halocline",
            "k": ["halocline"],
            "n": 0
        },
        {
            "id": "isohalines",
            "tier": "middle",
            "t": "Map lines connecting places with equal values are called isohalines",
            "k": ["isohalines"],
            "n": 0
        },
        {
            "id": "chloride-sodium",
            "tier": "middle",
            "t": "Chloride and sodium ions make up most of the dissolved material; chloride alone is more than half",
            "k": ["chloride", "sodium"],
            "n": 0,
            "rabbit": "Sodium"
        },
        {
            "id": "conductivity",
            "tier": "middle",
            "t": "Saltier water conducts electricity better, so CTD instruments find it from conductivity, temperature, and depth",
            "k": ["conductivity", "ctd"],
            "n": 0
        },
        {
            "id": "brackish",
            "tier": "middle",
            "t": "Water with an in-between value, as in many estuaries, is called brackish",
            "k": ["brackish", "estuaries"],
            "n": 0
        },
        {
            "id": "brine-rejection",
            "tier": "middle",
            "t": "Brine rejection: forming sea ice leaves its salt behind, so the water below gets saltier and denser",
            "k": ["brine rejection", "sea ice"],
            "n": 0
        },
        {
            "id": "subtropics",
            "tier": "middle",
            "t": "Highest at the sea surface in the subtropics, where evaporation beats rainfall; lower at the rainy equator",
            "k": ["subtropics", "equator"],
            "n": 0
        },
        {
            "id": "freezing-point",
            "tier": "middle",
            "t": "Raising it lowers the freezing point, so ocean water stays liquid a little below 0 °C",
            "k": ["freezing point"],
            "n": 0
        },
        {
            "id": "constant-proportions",
            "tier": "power",
            "t": "Forchhammer’s and Marcet’s principle of constant proportions: the main dissolved ions keep the same ratios everywhere",
            "k": ["constant proportions", "forchhammer", "marcet"],
            "n": 0
        },
        {
            "id": "dittmar",
            "tier": "power",
            "t": "William Dittmar confirmed those fixed ratios using seawater samples from the voyage of HMS _Challenger_",
            "k": ["dittmar", "challenger"],
            "n": 0
        },
        {
            "id": "practical-scale",
            "tier": "power",
            "t": "Since 1978, reported on a unitless “practical” scale based on conductivity compared with a potassium chloride standard",
            "k": ["potassium chloride", "1978", "practical"],
            "n": 0
        },
        {
            "id": "chlorinity",
            "tier": "power",
            "t": "The older method measured chlorinity by adding silver nitrate; Martin Knudsen helped set it up around 1900",
            "k": ["chlorinity", "silver nitrate", "knudsen"],
            "n": 0
        },
        {
            "id": "aquarius-smos",
            "tier": "power",
            "t": "NASA’s Aquarius (launched in 2011 on an Argentine satellite) and Europe’s SMOS satellite mapped it from space",
            "k": ["aquarius", "smos"],
            "n": 0
        },
        {
            "id": "argo",
            "tier": "power",
            "t": "Argo floats dive as deep as 2,000 meters, recording it and temperature",
            "k": ["argo floats", "2,000 meters"],
            "n": 0
        },
        {
            "id": "gibraltar",
            "tier": "power",
            "t": "The Mediterranean’s higher value makes its dense water spill out beneath incoming Atlantic water at the Strait of Gibraltar",
            "k": ["mediterranean", "gibraltar"],
            "n": 0
        },
        {
            "id": "halley-joly",
            "tier": "power",
            "t": "Edmond Halley (1715) proposed timing its rise to find Earth’s age; John Joly later tried it with sodium",
            "k": ["halley", "joly", "1715"],
            "n": 0
        },
        {
            "id": "euryhaline",
            "tier": "power",
            "t": "Euryhaline animals like salmon and bull sharks handle big changes in it; stenohaline animals cannot",
            "k": ["euryhaline", "stenohaline", "bull sharks"],
            "n": 0
        },
        {
            "id": "salt-wedge",
            "tier": "power",
            "t": "In a salt-wedge estuary, like the Mississippi River’s mouth, dense seawater slides upstream beneath fresh river water",
            "k": ["salt-wedge", "mississippi"],
            "n": 0,
            "rabbit": "Mississippi River"
        },
        {
            "id": "antarctic-bottom-water",
            "tier": "power",
            "t": "In Antarctica’s Weddell Sea, brine rejection makes the cold, dense Antarctic Bottom Water",
            "k": ["weddell sea", "antarctic bottom water"],
            "n": 0
        },
        {
            "id": "sources",
            "tier": "power",
            "t": "Rivers add ions weathered out of rocks on land, and volcanic gases add chloride",
            "k": ["weathered", "volcanic gases"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Saltiness, not density",
        "body": "Thermohaline-circulation tossups describe cold, salty water sinking, so players blurt out “density,” which depends on both temperature and this property and is a different answer. A halocline is only a layer where this property changes quickly, and “salinization” means salt building up in soil. Saying just “salt” earns a prompt.",
        "fix": "Parts per thousand, PSU, conductivity sensors, evaporation raising it, and the Dead Sea mean salinity. Mass per volume or kilograms per cubic meter mean density, and a layer of fast change means halocline (salt) or thermocline (temperature).",
        "line": "Real answer line: <b><u>Salinity</u></b> (accept saltiness or salt content; prompt on salt; do not accept “density”)"
    },
    "tests": {
        "right": [
            "Salinity",
            "saltiness",
            "Salt content",
            "Salinty",
            "Ocean salinity"
        ],
        "prompt": [
            "Salt",
            "Dissolved salts"
        ],
        "wrong": [
            "Density",
            "Salinization",
            "Temperature",
            "Halocline",
            "Brackish water",
            "Sodium chloride"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
