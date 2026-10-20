import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TIP = "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."

data = {
    "id": "power-physics",
    "name": "Power (physics)",
    "mono": "PWR",
    "category": "Physics",
    "qbCategory": "Science · Physics",
    "kicker": "How fast work is done · Measured in watts",
    "dates": "Horsepower coined by James Watt, late 1700s; the watt named in 1882",
    "briefing": "Power is how fast work gets done or energy gets used. Two people of the same weight who climb the same stairs do the same work, but the one who runs up uses more power. Power is measured in watts, named for steam-engine pioneer James Watt, who also came up with the horsepower so customers could compare his engines to horses. A 1,200-watt hair dryer uses 1,200 joules of energy every second.",
    "answerHtml": "<b><u>power</u></b> (prompt on <u>P</u>; do not accept “energy” or “work”)",
    "accept": [
        "power",
        "mechanical power",
        "electric power",
        "electrical power",
        "power output",
        "average power",
        "instantaneous power"
    ],
    "prompt": [
        "p",
        "wattage",
        "rate of doing work",
        "rate of work",
        "rate of energy transfer",
        "energy per unit time",
        "work per unit time"
    ],
    "reject": [
        "work",
        "energy",
        "force",
        "watt",
        "watts",
        "kilowatt",
        "kilowatts",
        "kilowatt hour",
        "kilowatt hours",
        "horsepower",
        "joule",
        "joules",
        "voltage",
        "current",
        "electric current",
        "resistance",
        "efficiency",
        "kinetic energy",
        "potential energy",
        "momentum",
        "pressure",
        "intensity",
        "optical power",
        "nuclear power",
        "solar power",
        "wind power",
        "power plant",
        "power station"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Power_(physics)",
    "qb": {
        "q": "power",
        "found": 0,
        "tip": TIP
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "James Watt defined a unit of this quantity as 33,000 foot-pounds of work per minute, based on how hard he estimated a mill horse could work, so that buyers could compare his steam engines to the horses they replaced.",
            "r": "That unit, the horsepower, equals about 746 watts. For 10 points, name this rate at which work is done."
        },
        {
            "p": "In an electric circuit, this quantity equals current times voltage, or current squared times resistance. A hair dryer that draws 10 amperes from a 120-volt outlet uses 1,200 units of this quantity.",
            "r": "For 10 points, name this quantity measured in watts, the rate at which energy is used or transferred."
        },
        {
            "p": "Electric companies send electricity over long distances at very high voltages, because for the same amount of this quantity a higher voltage means a smaller current, so less of this quantity is wasted heating the wires. Transformers raise and lower the voltage for that purpose.",
            "r": "For 10 points, name this quantity, the rate of using or transferring energy, measured in watts."
        },
        {
            "p": "For a car moving at a steady speed, this quantity equals the force pushing the car forward times the car’s velocity. For a spinning motor shaft, this quantity equals the torque times the angular velocity, so gears let a motor trade speed for twisting strength.",
            "r": "For 10 points, name this rate at which work is done, measured in watts."
        },
        {
            "p": "In a common school lab, students find their own value of this quantity by timing a run up a flight of stairs, then dividing their gain in potential energy, mass times g times height, by that time. Running up the stairs gives a larger value of this quantity than walking up them.",
            "r": "For 10 points, name this rate of doing work, measured in watts or in horsepower."
        },
        {
            "p": "A kilowatt-hour is not a unit of this quantity but a unit of energy, equal to using 1,000 units of this quantity for one hour. Electric bills charge for energy, while appliance labels list this quantity.",
            "r": "For 10 points, name this quantity, the rate at which energy is used, measured in watts."
        },
        {
            "p": "A star’s luminosity is its total output of this quantity, which for the Sun is about 3.8 times 10 to the 26th joules every second. At the top of Earth’s atmosphere, sunlight delivers about 1,360 units of this quantity to each square meter, a value called the solar constant.",
            "r": "For 10 points, name this quantity measured in watts, the rate of energy transfer."
        },
        {
            "p": "A resting adult’s body uses energy at a rate of roughly 100 joules per second, about the same as an old light bulb, and a trained cyclist can briefly produce more than ten times that much of this quantity.",
            "r": "For 10 points, name this rate at which work is done or energy is used, measured in watts."
        },
        {
            "p": "Dividing a machine’s useful output of this quantity by its input of this quantity gives its efficiency, which is always less than 100 percent because some energy turns into heat.",
            "r": "Doing the same job in half the time takes twice as much of it. For 10 points, name this rate of doing work."
        },
        {
            "p": "The most extreme lasers reach enormous values of this quantity by squeezing a modest amount of energy into a pulse lasting less than a trillionth of a second. This quantity equals energy divided by time, so a shorter pulse with the same energy gives more of it.",
            "r": "For 10 points, name this quantity, measured in watts, that tells how fast energy is delivered."
        },
        {
            "p": "The intensity of a sound or light wave equals the amount of this quantity it carries per unit area, and the decibel scale compares ratios of this quantity on a logarithmic scale. Doubling the amplitude of a wave multiplies the amount of this quantity it carries by four.",
            "r": "For 10 points, name this rate of energy transfer, measured in watts and symbolized P."
        },
        {
            "p": "James Prescott Joule found that the heat a current produces in a wire each second equals current squared times the wire’s resistance, which is the amount of this quantity turned into heat. That heating is how toasters and electric stoves work.",
            "r": "For 10 points, name this quantity, the rate at which electrical energy is used, measured in watts."
        },
        {
            "p": "John Henry Poynting’s [“POYN-ting’s”] vector gives the direction and amount of this quantity flowing through each square meter of an electromagnetic wave. A solar panel’s rating gives the most of this quantity it can deliver in full sunlight.",
            "r": "For 10 points, name this quantity measured in watts, the rate at which energy is transferred."
        },
        {
            "p": "An old incandescent bulb turns most of the electrical energy it uses into heat rather than light, so an LED bulb that gives the same amount of light needs only about a sixth as much of this quantity.",
            "r": "Bulbs are labeled with this quantity in watts. For 10 points, name this rate of energy use."
        },
        {
            "p": "In 1882, William Siemens [“SEE-menz”] proposed naming a unit of this quantity for the Scottish engineer who improved the steam engine, and that unit later became part of the metric system. That unit equals one joule per second.",
            "r": "For 10 points, name this quantity measured in watts, the rate at which work is done."
        }
    ],
    "clues": [
        {
            "id": "rate-of-work",
            "tier": "giveaway",
            "t": "The rate at which work is done or energy is transferred: work divided by time",
            "k": ["rate", "work divided by time", "energy"],
            "n": 0
        },
        {
            "id": "watts",
            "tier": "giveaway",
            "t": "Measured in watts; one watt is one joule per second",
            "k": ["watts", "joule per second"],
            "n": 0
        },
        {
            "id": "james-watt",
            "tier": "giveaway",
            "t": "Its unit is named for James Watt, the Scottish engineer who improved the steam engine",
            "k": ["james watt", "steam engine"],
            "n": 0
        },
        {
            "id": "faster-more",
            "tier": "giveaway",
            "t": "Doing the same work in less time takes more of it, so running up stairs takes more than walking",
            "k": ["less time", "running up stairs"],
            "n": 0
        },
        {
            "id": "horse-unit",
            "tier": "giveaway",
            "t": "Also measured in a unit named for horses, equal to about 746 watts",
            "k": ["746 watts", "horses"],
            "n": 0
        },
        {
            "id": "current-voltage",
            "tier": "middle",
            "t": "In a circuit, it equals current times voltage (P = IV), or current squared times resistance",
            "k": ["current times voltage", "resistance"],
            "n": 0,
            "rabbit": "Voltage"
        },
        {
            "id": "kilowatt-hour",
            "tier": "middle",
            "t": "A kilowatt-hour is a unit of energy, not of this: 1,000 watts used for one hour",
            "k": ["kilowatt-hour", "1,000 watts"],
            "n": 0,
            "rabbit": "Energy"
        },
        {
            "id": "force-velocity",
            "tier": "middle",
            "t": "For a moving object pushed by a force, it equals force times velocity",
            "k": ["force times velocity", "velocity"],
            "n": 0
        },
        {
            "id": "torque-omega",
            "tier": "middle",
            "t": "For a spinning shaft, it equals torque times angular velocity",
            "k": ["torque times angular velocity", "angular velocity"],
            "n": 0,
            "rabbit": "Torque"
        },
        {
            "id": "efficiency",
            "tier": "middle",
            "t": "Efficiency is useful output divided by input of it, always less than 100 percent",
            "k": ["efficiency", "100 percent"],
            "n": 0
        },
        {
            "id": "stairs-lab",
            "tier": "middle",
            "t": "School lab: time a run up a flight of stairs, then divide mass times g times height by the time",
            "k": ["flight of stairs", "mass times g times height"],
            "n": 0
        },
        {
            "id": "transmission",
            "tier": "middle",
            "t": "Sent over long distances at high voltage, so a smaller current wastes less of it heating the wires; transformers change the voltage",
            "k": ["high voltage", "smaller current", "transformers"],
            "n": 0
        },
        {
            "id": "bulbs",
            "tier": "middle",
            "t": "Light bulbs are labeled in watts; an LED needs only about a sixth as much as an incandescent bulb for the same light",
            "k": ["light bulbs", "incandescent", "led"],
            "n": 0
        },
        {
            "id": "watt-33000",
            "tier": "power",
            "t": "James Watt defined his horse-based unit as 33,000 foot-pounds of work per minute, to sell his steam engines",
            "k": ["33,000 foot-pounds", "foot-pounds"],
            "n": 0
        },
        {
            "id": "siemens-1882",
            "tier": "power",
            "t": "William Siemens proposed naming its unit for James Watt in 1882",
            "k": ["siemens", "1882"],
            "n": 0
        },
        {
            "id": "luminosity",
            "tier": "power",
            "t": "A star’s luminosity is its total output of it; the Sun’s is about 3.8 × 10²⁶ watts",
            "k": ["luminosity", "3.8"],
            "n": 0
        },
        {
            "id": "solar-constant",
            "tier": "power",
            "t": "The solar constant: about 1,360 watts reach each square meter at the top of Earth’s atmosphere",
            "k": ["solar constant", "1,360 watts"],
            "n": 0
        },
        {
            "id": "body-100",
            "tier": "power",
            "t": "A resting adult uses about 100 watts; a trained cyclist can briefly produce more than ten times that",
            "k": ["100 watts", "cyclist"],
            "n": 0
        },
        {
            "id": "lasers",
            "tier": "power",
            "t": "The most extreme lasers reach huge values by squeezing modest energy into pulses shorter than a trillionth of a second",
            "k": ["lasers", "trillionth"],
            "n": 0,
            "rabbit": "Lasers"
        },
        {
            "id": "intensity",
            "tier": "power",
            "t": "A wave’s intensity is the amount it carries per unit area; doubling the amplitude multiplies it by four",
            "k": ["intensity", "per unit area", "amplitude"],
            "n": 0,
            "rabbit": "Waves"
        },
        {
            "id": "decibels",
            "tier": "power",
            "t": "The decibel scale compares ratios of it on a logarithmic scale",
            "k": ["decibel", "logarithmic"],
            "n": 0
        },
        {
            "id": "joule-heating",
            "tier": "power",
            "t": "James Prescott Joule: the heat a current makes in a wire each second equals current squared times resistance",
            "k": ["james prescott joule", "current squared"],
            "n": 0
        },
        {
            "id": "poynting",
            "tier": "power",
            "t": "The Poynting vector gives the amount flowing through each square meter of an electromagnetic wave",
            "k": ["poynting vector", "electromagnetic wave"],
            "n": 0
        },
        {
            "id": "metric-horse",
            "tier": "power",
            "t": "Germany’s PS (Pferdestärke, “horse strength”) is a metric horse-based unit of about 735 watts",
            "k": ["pferdestärke", "735 watts"],
            "n": 0
        },
        {
            "id": "three-gorges",
            "tier": "power",
            "t": "China’s Three Gorges Dam can generate about 22,500 megawatts",
            "k": ["three gorges dam", "megawatts"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Power, not energy or work",
        "body": "Power is how fast energy is used or work is done, so a kilowatt-hour on an electric bill measures energy, not power, and work and energy are separate answer lines whose tossups sound alike. The watt and the horsepower are units, not the quantity, and “electric power” used to mean electricity in general is not the physics idea of a rate.",
        "fix": "Watts, horsepower, P = IV, “work divided by time,” or “how fast” means power. Joules, kilowatt-hours, and “force times distance” mean energy or work. If asked for “this quantity,” say “power,” not “watts.”",
        "line": "Real answer line: <b><u>power</u></b> (prompt on <u>P</u>; do not accept “energy” or “work”)"
    },
    "tests": {
        "right": [
            "Power",
            "power",
            "Powr",
            "Electrical power",
            "Mechanical power",
            "Power output"
        ],
        "prompt": [
            "P",
            "Wattage"
        ],
        "wrong": [
            "Energy",
            "Work",
            "Watts",
            "Horsepower",
            "Kilowatt-hour",
            "Force",
            "Voltage",
            "Current"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
