import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "luminosity",
    "name": "Luminosity",
    "mono": "LUM",
    "category": "Astronomy",
    "qbCategory": "Science · Other Science (Astronomy)",
    "kicker": "A star’s total power output · How bright it truly is, not how bright it looks",
    "dates": "Leavitt’s law 1912; H–R diagram c. 1911–1913",
    "briefing": "Luminosity is the total amount of energy a star gives off every second: its true power output. The Sun’s luminosity is about 380 trillion trillion watts. A star can look faint just because it is far away, so astronomers keep luminosity separate from apparent brightness, which depends on distance. Stars whose luminosity is known, like Cepheid variables, work as “standard candles” for measuring the universe.",
    "answerHtml": "<b><u>Luminosity</u></b> (prompt on <u>brightness</u> or <u>power</u>; do not accept “apparent brightness” or “magnitude”)",
    "accept": [
        "luminosity",
        "luminosities"
    ],
    "prompt": [
        "brightness",
        "absolute brightness",
        "intrinsic brightness",
        "true brightness",
        "power",
        "power output",
        "total power",
        "total power output",
        "energy output",
        "radiant power"
    ],
    "reject": [
        "apparent brightness",
        "apparent magnitude",
        "absolute magnitude",
        "magnitude",
        "flux",
        "luminance",
        "luminous intensity",
        "luminous flux",
        "luminescence",
        "irradiance",
        "solar constant"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Luminosity",
    "qb": {
        "q": "luminosity",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "If a star’s surface temperature doubles while its size stays the same, this quantity becomes 16 times larger, because the Stefan–Boltzmann law says it grows with the fourth power of temperature. It also grows with the square of a star’s radius.",
            "r": "For 10 points, name this quantity, the total amount of energy a star gives off every second."
        },
        {
            "p": "While measuring stars in the Small Magellanic Cloud, Henrietta Swan Leavitt found that Cepheid [“SEF-ee-id”] variables that take longer to brighten and dim have greater values of this quantity. Her 1912 discovery later let Edwin Hubble show that the Andromeda “nebula” is a separate galaxy.",
            "r": "For 10 points, name this quantity, a star’s total power output, often given in units of the Sun’s."
        },
        {
            "p": "In the Morgan–Keenan system, Roman numerals give a star’s “class” named for this quantity, from I for supergiants down to V for main-sequence dwarfs. The V at the end of the Sun’s label, G2V, comes from that scheme.",
            "r": "For 10 points, name this quantity, the total energy a star gives off per second, measured in watts."
        },
        {
            "p": "Arthur Eddington found a limit on this quantity: above it, the outward push of a star’s own light, called radiation pressure, becomes stronger than the star’s gravity and drives gas away from the star.",
            "r": "For 10 points, name this quantity, the total power given off by a star or another glowing object, measured in watts."
        },
        {
            "p": "For main-sequence stars, this quantity rises roughly as mass to the 3.5 power, so a star ten times as massive as the Sun has thousands of times the Sun’s value, while a star with half the Sun’s mass has less than a tenth of it.",
            "r": "That is why the most massive stars burn out in only a few million years. For 10 points, name this measure of a star’s total power output."
        },
        {
            "p": "Carl Sagan and George Mullen pointed out a puzzle: early in Earth’s history, the Sun had only about 70 percent as much of this quantity as it has in modern times, yet young Earth still had liquid water. That puzzle is called the faint young Sun paradox.",
            "r": "For 10 points, name this quantity, the total energy the Sun or another star gives off each second."
        },
        {
            "p": "Dividing this quantity by 4π times the square of a star’s distance gives the flux that we measure on Earth, a rule called the inverse-square law. Astronomers who know both the flux and this quantity for a star can work out how far away it is.",
            "r": "Because of that rule, a powerful star can still look faint if it is far away. For 10 points, name this quantity, a star’s true total power output."
        },
        {
            "p": "In 1998, two teams compared the known peak value of this quantity for Type Ia supernovae with how faint those explosions looked, and discovered that the universe’s expansion is speeding up. Objects with a known value of this quantity are called standard candles.",
            "r": "For 10 points, name this measure of the total energy an object gives off per second."
        },
        {
            "p": "Multiplying the solar constant, about 1,361 watts per square meter, by 4π times the square of Earth’s distance from the Sun gives the Sun’s value of this quantity, about 3.8 × 10²⁶ watts.",
            "r": "Astronomers often give it for other stars in units of the Sun’s value. For 10 points, name this quantity, a star’s total power output."
        },
        {
            "p": "Many white dwarfs are hotter than the Sun but have far less of this quantity because they are so small, while cool red giants have much more of it because they are so huge. The red supergiant Betelgeuse [“BET-ul-jooz”] has an enormous value of this quantity despite its cool surface.",
            "r": "Ejnar Hertzsprung and Henry Norris Russell plotted it against temperature. For 10 points, name this total power output of a star."
        },
        {
            "p": "A star’s absolute magnitude, which is how bright it would look from 10 parsecs away, is a backward, logarithmic stand-in for this quantity: a star whose absolute magnitude is five lower has 100 times more of it.",
            "r": "For 10 points, name this quantity, the total energy a star gives off each second, measured in watts."
        },
        {
            "p": "Astronomers call this quantity “bolometric” when it counts energy at every wavelength, a term that comes from the bolometer, a heat-measuring device invented by Samuel Langley. Visible light makes up only part of the Sun’s total.",
            "r": "For 10 points, name this quantity, a star’s total power output, which is often compared to the Sun’s."
        },
        {
            "p": "Sirius is the brightest star in our night sky mostly because it is only about 8.6 light-years away; it has only about 25 times the Sun’s value of this quantity. Rigel [“RY-jul”] looks fainter, but it has more than a thousand times as much of this quantity as Sirius.",
            "r": "For 10 points, name this quantity, a star’s true power output, as opposed to how bright it looks from Earth."
        },
        {
            "p": "The distance from a star to its habitable zone, where a planet could have liquid water, grows with the square root of this quantity. Red dwarfs have so little of it that their habitable zones lie closer in than Mercury’s orbit around the Sun.",
            "r": "For 10 points, name this measure of the total energy a star gives off per second."
        },
        {
            "p": "Quasars, which are powered by gas falling into supermassive black holes, have some of the highest values of this quantity in the universe, often more than all the stars in their home galaxies put together, even though that glow comes from a region about the size of our solar system.",
            "r": "For 10 points, name this quantity, the total power an object gives off, often measured in watts."
        }
    ],
    "clues": [
        {
            "id": "total-power",
            "tier": "giveaway",
            "t": "The total amount of energy a star gives off every second: its true power output",
            "k": [
                "total amount of energy",
                "power output",
                "every second"
            ],
            "n": 0
        },
        {
            "id": "watts-solar",
            "tier": "giveaway",
            "t": "Measured in watts, the unit of power, or in units of the Sun’s value",
            "k": [
                "watts",
                "units of the sun’s value"
            ],
            "n": 0
        },
        {
            "id": "hr-diagram",
            "tier": "giveaway",
            "t": "Plotted on the vertical axis of the Hertzsprung–Russell (H–R) diagram, against surface temperature",
            "k": [
                "vertical axis",
                "hertzsprung–russell",
                "h–r diagram"
            ],
            "n": 0,
            "rabbit": "Hertzsprung–Russell diagram"
        },
        {
            "id": "not-apparent",
            "tier": "giveaway",
            "t": "Not the same as apparent brightness: a star can look faint just because it is far away",
            "k": [
                "apparent brightness",
                "far away"
            ],
            "n": 0
        },
        {
            "id": "stefan-boltzmann",
            "tier": "middle",
            "t": "Stefan–Boltzmann law: it grows with a star’s radius squared and its temperature to the fourth power (L = 4πR²σT⁴)",
            "k": [
                "stefan–boltzmann",
                "radius squared",
                "fourth power"
            ],
            "n": 0
        },
        {
            "id": "inverse-square",
            "tier": "middle",
            "t": "Flux (apparent brightness) equals it divided by 4π times the distance squared: the inverse-square law",
            "k": [
                "inverse-square law",
                "flux",
                "distance squared"
            ],
            "n": 0
        },
        {
            "id": "leavitt",
            "tier": "middle",
            "t": "Henrietta Swan Leavitt (1912): Cepheid variables that take longer to pulse have greater values (Leavitt’s law)",
            "k": [
                "leavitt",
                "cepheid",
                "1912"
            ],
            "n": 0,
            "rabbit": "Cepheid variables"
        },
        {
            "id": "standard-candles",
            "tier": "middle",
            "t": "Objects whose value is known, like Cepheid variables and Type Ia supernovae, are “standard candles” for measuring distances",
            "k": [
                "standard candles",
                "type ia"
            ],
            "n": 0,
            "rabbit": "Supernovae"
        },
        {
            "id": "absolute-magnitude",
            "tier": "middle",
            "t": "Absolute magnitude, how bright a star would look from 10 parsecs away, is a backward, logarithmic stand-in for it",
            "k": [
                "absolute magnitude",
                "10 parsecs",
                "logarithmic"
            ],
            "n": 0
        },
        {
            "id": "main-sequence",
            "tier": "middle",
            "t": "Along the main sequence it rises with mass, so hot, blue, massive stars give off the most",
            "k": [
                "main sequence",
                "massive stars"
            ],
            "n": 0,
            "rabbit": "Main sequence"
        },
        {
            "id": "giants-dwarfs",
            "tier": "middle",
            "t": "Size matters: cool red giants have high values because they are huge, while hot white dwarfs are dim because they are tiny",
            "k": [
                "red giants",
                "white dwarfs",
                "size matters"
            ],
            "n": 0,
            "rabbit": "White dwarfs"
        },
        {
            "id": "sirius",
            "tier": "middle",
            "t": "Sirius looks brightest at night mostly because it is close (about 8.6 light-years), but it has only about 25 times the Sun’s value",
            "k": [
                "sirius",
                "8.6 light-years",
                "25 times"
            ],
            "n": 0
        },
        {
            "id": "morgan-keenan",
            "tier": "power",
            "t": "Morgan–Keenan classes named for it use Roman numerals: I = supergiants, III = giants, V = main-sequence dwarfs (the Sun is G2V)",
            "k": [
                "morgan–keenan",
                "roman numerals",
                "g2v"
            ],
            "n": 0
        },
        {
            "id": "mass-power",
            "tier": "power",
            "t": "For main-sequence stars it rises roughly as mass to the 3.5 power",
            "k": [
                "3.5 power",
                "mass"
            ],
            "n": 0
        },
        {
            "id": "lifetimes",
            "tier": "power",
            "t": "Stars with high values burn out fast: the most massive last only a few million years",
            "k": [
                "burn out",
                "few million years"
            ],
            "n": 0
        },
        {
            "id": "eddington",
            "tier": "power",
            "t": "The Eddington limit: above it, the push of a star’s own light (radiation pressure) beats its gravity",
            "k": [
                "eddington",
                "radiation pressure"
            ],
            "n": 0
        },
        {
            "id": "faint-young-sun",
            "tier": "power",
            "t": "Faint young Sun paradox (Carl Sagan and George Mullen, 1972): the early Sun had only about 70 percent of its modern value",
            "k": [
                "faint young sun",
                "sagan",
                "70 percent"
            ],
            "n": 0
        },
        {
            "id": "solar-constant",
            "tier": "power",
            "t": "The solar constant (about 1,361 watts per square meter) times 4π times Earth’s distance squared gives the Sun’s value, about 3.8 × 10²⁶ watts",
            "k": [
                "solar constant",
                "1,361",
                "3.8"
            ],
            "n": 0
        },
        {
            "id": "bolometric",
            "tier": "power",
            "t": "“Bolometric” means counted over all wavelengths, after the bolometer, a heat-measuring device invented by Samuel Langley",
            "k": [
                "bolometric",
                "bolometer",
                "langley"
            ],
            "n": 0
        },
        {
            "id": "type-ia-1998",
            "tier": "power",
            "t": "In 1998, Type Ia supernovae used as standard candles showed that the universe’s expansion is speeding up",
            "k": [
                "1998",
                "speeding up"
            ],
            "n": 0
        },
        {
            "id": "habitable-zone",
            "tier": "power",
            "t": "The distance to a star’s habitable zone grows with the square root of this value; red dwarfs’ habitable zones are closer to them than Mercury is to the Sun",
            "k": [
                "habitable zone",
                "square root",
                "red dwarfs"
            ],
            "n": 0
        },
        {
            "id": "betelgeuse-rigel",
            "tier": "power",
            "t": "Betelgeuse (a red supergiant) and Rigel give off enormous amounts; Rigel looks fainter than Sirius but gives off over a thousand times as much",
            "k": [
                "betelgeuse",
                "rigel",
                "thousand times"
            ],
            "n": 0
        },
        {
            "id": "quasars",
            "tier": "power",
            "t": "Quasars, powered by supermassive black holes, can give off more than all the stars in their home galaxies combined",
            "k": [
                "quasars",
                "home galaxies"
            ],
            "n": 0,
            "rabbit": "Quasars"
        },
        {
            "id": "hertzsprung-russell",
            "tier": "power",
            "t": "Ejnar Hertzsprung and Henry Norris Russell first plotted it against temperature (about 1911–1913)",
            "k": [
                "ejnar hertzsprung",
                "henry norris russell"
            ],
            "n": 0
        },
        {
            "id": "hubble-andromeda",
            "tier": "power",
            "t": "Edwin Hubble used Leavitt’s Cepheids in the 1920s to show that the Andromeda “nebula” is a separate galaxy",
            "k": [
                "edwin hubble",
                "andromeda"
            ],
            "n": 0,
            "rabbit": "Edwin Hubble"
        }
    ],
    "trap": {
        "title": "True power or apparent brightness?",
        "body": "Luminosity is a star’s true power output, but how bright a star looks from Earth, its apparent brightness or flux, also depends on how far away it is. Absolute magnitude and apparent magnitude are different quantities that rate brightness on a backward, logarithmic scale. Players who hear “bright” clues often blurt out “brightness” or “magnitude” instead of the exact term.",
        "fix": "Watts, units of the Sun’s output, the Stefan–Boltzmann law, Leavitt’s Cepheids, the Eddington limit, and “total energy per second” all mean luminosity. “As seen from Earth,” “divided by distance squared,” or “watts per square meter” mean flux; a number on a scale where lower means brighter is a magnitude.",
        "line": "Real answer line: <b><u>Luminosity</u></b> (prompt on <u>brightness</u> or <u>power</u>; do not accept “apparent brightness” or “magnitude”)"
    },
    "tests": {
        "right": [
            "Luminosity",
            "luminosity",
            "Luminocity",
            "Stellar luminosity",
            "Bolometric luminosity"
        ],
        "prompt": [
            "Brightness",
            "Power",
            "Absolute brightness"
        ],
        "wrong": [
            "Apparent brightness",
            "Absolute magnitude",
            "Apparent magnitude",
            "Flux",
            "Luminance",
            "Temperature"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
