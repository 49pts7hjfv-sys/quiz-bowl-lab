import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "pendulums",
    "name": "Pendulums",
    "mono": "PDL",
    "category": "Physics",
    "qbCategory": "Science · Physics",
    "kicker": "A weight swinging from a pivot · Kept time and proved Earth spins",
    "dates": "First pendulum clock built by Christiaan Huygens, 1656",
    "briefing": "A pendulum is just a weight swinging from a string or rod, but it changed the world. Galileo noticed that each swing takes about the same time, wide or narrow, and in 1656 Christiaan Huygens used that idea to build the first pendulum clock, which stayed the most accurate kind of clock until the 1930s. In 1851, Léon Foucault hung a giant pendulum in Paris to prove that Earth rotates.",
    "answerHtml": "<b><u>pendulum</u></b>s (accept specific types like <u>Foucault pendulum</u>s or <u>simple pendulum</u>s; prompt on <u>oscillator</u>s)",
    "accept": [
        "pendulums",
        "pendulum",
        "pendula",
        "simple pendulum",
        "simple pendulums",
        "foucault pendulum",
        "foucault pendulums",
        "foucaults pendulum",
        "physical pendulum",
        "compound pendulum",
        "double pendulum",
        "ballistic pendulum",
        "seconds pendulum",
        "conical pendulum",
        "inverted pendulum"
    ],
    "prompt": [
        "oscillator",
        "oscillators",
        "harmonic oscillator",
        "harmonic oscillators",
        "simple harmonic oscillator"
    ],
    "reject": [
        "simple harmonic motion",
        "harmonic motion",
        "oscillation",
        "oscillations",
        "spring",
        "springs",
        "mass on a spring",
        "hookes law",
        "newtons cradle",
        "pit and the pendulum",
        "precession",
        "resonance"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Pendulum",
    "qb": {
        "q": "pendulum",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "In 1672, Jean Richer [“ree-SHAY”] had to shorten one of these devices in Cayenne, near the equator, to make it keep the same time it kept in Paris, a sign that gravity is slightly weaker there. The time each swing takes depends on the device’s length and on gravity, but not on its mass.",
            "r": "Christiaan Huygens built the first clock regulated by one of these devices. For 10 points, name these swinging weights that keep time in grandfather clocks."
        },
        {
            "p": "Christiaan Huygens [“HOY-gunz”] proved that one of these devices would keep perfect time if its bob moved along a curve called a cycloid, so he guided its string between curved metal “cheeks.” He described his designs in the 1673 book _Horologium Oscillatorium_.",
            "r": "For small swings, the period of one of these devices equals two pi times the square root of its length over g. For 10 points, name these swinging weights."
        },
        {
            "p": "At the North Pole, the direction in which one of these devices swings would turn a full circle in about a day, but at the equator it would not turn at all. In 1851, Léon Foucault [“foo-KOH”] hung a 67-meter-long one from the dome of the Panthéon in Paris to prove that Earth rotates.",
            "r": "For 10 points, name these swinging devices, which Galileo studied after watching a lamp sway in a cathedral, according to a famous story."
        },
        {
            "p": "Henry Kater designed a “reversible” one of these devices that could swing from either of two pivots, letting scientists measure the strength of gravity very precisely. Making one of these devices four times longer doubles the time it takes to complete each swing.",
            "r": "Galileo noticed that wide and narrow swings of these devices take about the same time. For 10 points, name these weights that hang from a pivot and swing back and forth."
        },
        {
            "p": "Benjamin Robins invented a “ballistic” type of these devices that finds a bullet’s speed by measuring how high a heavy wooden block swings after the bullet lodges in it. One of these devices moves fastest at the bottom of its path and stops for an instant at the top of each swing.",
            "r": "The time each one takes per swing depends on its length but not its mass. For 10 points, name these swinging weights, which keep time in grandfather clocks."
        },
        {
            "p": "Hanging one of these devices from the bottom of another creates a system famous for chaos, in which tiny changes in the starting position lead to wildly different motion. A single one of these devices follows simple harmonic motion for small swings, because the sine of a small angle almost equals the angle itself.",
            "r": "These devices keep time in grandfather clocks. For 10 points, name these devices, each made of a bob hanging from a string or rod."
        },
        {
            "p": "A giant steel ball hung near the top of the Taipei 101 skyscraper acts as one of these devices, swinging to reduce the building’s sway in strong winds. Christiaan Huygens noticed that two clocks run by these devices, hung from the same beam, soon fell into a matching rhythm.",
            "r": "For 10 points, name these swinging weights, one of which Léon Foucault used to show that Earth rotates."
        },
        {
            "p": "In the 1790s, French scientists considered defining the meter as the length of one of these devices that takes exactly one second per swing, about 99 centimeters, but they chose a fraction of the distance from the North Pole to the equator instead.",
            "r": "The time each swing takes does not depend on the mass of the bob. For 10 points, name these swinging devices, which regulate grandfather clocks."
        },
        {
            "p": "Balancing a broomstick on your palm and keeping a self-balancing Segway upright are both versions of the “inverted” form of these devices. In an ordinary one of these devices, potential energy is greatest at the top of each swing, and kinetic energy is greatest at the bottom.",
            "r": "For 10 points, name these devices, each a weight on a string or rod that swings back and forth from a fixed point."
        },
        {
            "p": "Vincenzo Viviani [“vee-vee-AH-nee”] wrote that his teacher, while still a student, used his own pulse to time a lamp swaying in the cathedral of Pisa, finding that these devices take nearly the same time per swing whether they swing wide or narrow. That property is called isochronism [“eye-SOCK-ruh-niz-um”].",
            "r": "That teacher was Galileo. For 10 points, name these swinging weights, later used by Christiaan Huygens to build accurate clocks."
        },
        {
            "p": "For a “physical” or “compound” type of these devices, like a swinging rod, the period depends on its moment of inertia and on how far its center of mass sits from the pivot. On the Moon, a simple one of these devices would take about two and a half times as long per swing as on Earth.",
            "r": "Galileo and Christiaan Huygens studied these devices. For 10 points, name these swinging devices, one of which Léon Foucault used to prove that Earth rotates."
        },
        {
            "p": "In the “conical” type of these devices, the bob moves in a horizontal circle, so its string traces out a cone. In an ordinary one, the restoring force pulling the bob back toward the middle equals its weight times the sine of the angle from vertical.",
            "r": "For 10 points, name these swinging weights, found in grandfather clocks, whose period equals two pi times the square root of length divided by g."
        },
        {
            "p": "Isaac Newton filled the hollow bobs of these devices with gold, silver, lead, glass, sand, salt, wood, water, and wheat, and found that all of them swung at the same rate. Air resistance and friction at the pivot slowly shrink the swings of real ones, an effect called damping.",
            "r": "In 1656, Christiaan Huygens used one of these devices to build a far more accurate clock. For 10 points, name these swinging devices, which keep time in grandfather clocks."
        },
        {
            "p": "An invention called the anchor escapement let clocks swing these devices through much smaller arcs, which led to tall “longcase” clocks. Sliding the weight farther up the arm of a wind-up metronome slows its beat, much like lengthening one of these devices.",
            "r": "Galileo and Christiaan Huygens both studied these devices. For 10 points, name these swinging timekeepers found inside grandfather clocks."
        },
        {
            "p": "Christiaan Huygens hoped that clocks run by these devices could help sailors find longitude, but the rolling of ships at sea spoiled their timekeeping. A playground swing pushed in rhythm with its natural frequency goes higher, because the swing acts as one of these devices.",
            "r": "Longer ones take more time per swing. For 10 points, name these weights hanging from a pivot, one of which Léon Foucault used to show that Earth spins."
        }
    ],
    "clues": [
        {
            "id": "definition",
            "tier": "giveaway",
            "t": "A weight called a bob, hanging from a string or rod, that swings back and forth from a fixed pivot",
            "k": ["bob", "swings back and forth", "pivot"],
            "n": 0
        },
        {
            "id": "clocks",
            "tier": "giveaway",
            "t": "Keeps time in grandfather clocks; Christiaan Huygens built the first clock run by one in 1656",
            "k": ["grandfather clocks", "huygens", "1656"],
            "n": 0
        },
        {
            "id": "galileo",
            "tier": "giveaway",
            "t": "Galileo found that each swing takes about the same time; legend says he timed a swaying lamp in Pisa’s cathedral with his pulse",
            "k": ["galileo", "swaying lamp", "pulse"],
            "n": 0,
            "rabbit": "Galileo Galilei"
        },
        {
            "id": "foucault",
            "tier": "giveaway",
            "t": "Léon Foucault hung a huge one from the dome of the Panthéon in Paris (1851) to prove that Earth rotates",
            "k": ["foucault", "earth rotates", "1851"],
            "n": 0
        },
        {
            "id": "length-not-mass",
            "tier": "giveaway",
            "t": "The time for one swing (its period) depends on its length and on gravity, not on the mass of the bob",
            "k": ["length", "not on the mass", "period"],
            "n": 0
        },
        {
            "id": "formula",
            "tier": "middle",
            "t": "For small swings, period = two pi times the square root of (length ÷ g), so four times the length doubles the period",
            "k": ["two pi", "square root", "four times"],
            "n": 0
        },
        {
            "id": "isochronism",
            "tier": "middle",
            "t": "Isochronism: small swings take the same time whether they are wide or narrow",
            "k": ["isochronism", "wide or narrow"],
            "n": 0
        },
        {
            "id": "shm",
            "tier": "middle",
            "t": "Small swings follow simple harmonic motion, because the sine of a small angle almost equals the angle itself",
            "k": ["simple harmonic motion", "small angle"],
            "n": 0
        },
        {
            "id": "energy",
            "tier": "middle",
            "t": "Potential energy is greatest at the top of each swing; kinetic energy and speed are greatest at the bottom",
            "k": ["potential energy", "kinetic energy", "bottom"],
            "n": 0,
            "rabbit": "Potential energy"
        },
        {
            "id": "restoring-force",
            "tier": "middle",
            "t": "The restoring force pulling the bob back toward the middle equals its weight times the sine of the angle from vertical",
            "k": ["restoring force", "sine"],
            "n": 0
        },
        {
            "id": "latitude",
            "tier": "middle",
            "t": "At the North Pole, the direction of a Foucault-style swing turns a full circle in about a day; at the equator it does not turn",
            "k": ["north pole", "equator", "full circle"],
            "n": 0,
            "rabbit": "Precession"
        },
        {
            "id": "damping",
            "tier": "middle",
            "t": "Air resistance and friction at the pivot slowly shrink real swings, an effect called damping",
            "k": ["damping", "air resistance"],
            "n": 0
        },
        {
            "id": "resonance",
            "tier": "middle",
            "t": "A playground swing goes higher when pushed in rhythm with its natural frequency, an example of resonance",
            "k": ["resonance", "playground swing", "natural frequency"],
            "n": 0,
            "rabbit": "Resonance"
        },
        {
            "id": "moon",
            "tier": "middle",
            "t": "On the Moon, with about one-sixth of Earth’s gravity, each swing would take about 2.5 times as long",
            "k": ["moon", "one-sixth"],
            "n": 0
        },
        {
            "id": "cycloid",
            "tier": "power",
            "t": "Huygens proved a bob moving along a cycloid keeps perfect time, guided the string with curved “cheeks,” and wrote _Horologium Oscillatorium_ (1673)",
            "k": ["cycloid", "cheeks", "horologium oscillatorium"],
            "n": 0
        },
        {
            "id": "richer",
            "tier": "power",
            "t": "Jean Richer (1672) had to shorten one in Cayenne, near the equator, a sign that gravity is slightly weaker there",
            "k": ["richer", "cayenne"],
            "n": 0
        },
        {
            "id": "kater",
            "tier": "power",
            "t": "Henry Kater’s “reversible” type swings from either of two pivots to measure gravity precisely",
            "k": ["kater", "reversible", "two pivots"],
            "n": 0
        },
        {
            "id": "ballistic",
            "tier": "power",
            "t": "Benjamin Robins’s “ballistic” type finds a bullet’s speed from how high a struck wooden block swings",
            "k": ["ballistic", "robins", "bullet"],
            "n": 0
        },
        {
            "id": "double-chaos",
            "tier": "power",
            "t": "A “double” type, with one hung from the bottom of another, is a famous example of chaos",
            "k": ["double", "chaos"],
            "n": 0
        },
        {
            "id": "newton-bobs",
            "tier": "power",
            "t": "Isaac Newton filled hollow bobs with gold, wood, wheat, and more; all of them swung at the same rate",
            "k": ["newton", "hollow bobs", "wheat"],
            "n": 0,
            "rabbit": "Isaac Newton"
        },
        {
            "id": "seconds-meter",
            "tier": "power",
            "t": "A “seconds” type (one second per swing) is about 99 centimeters long; 1790s France considered it for defining the meter",
            "k": ["seconds", "99 centimeters", "meter"],
            "n": 0
        },
        {
            "id": "physical",
            "tier": "power",
            "t": "A “physical” or “compound” type, like a swinging rod, has a period set by its moment of inertia",
            "k": ["physical", "compound", "moment of inertia"],
            "n": 0
        },
        {
            "id": "inverted",
            "tier": "power",
            "t": "An upside-down “inverted” type models balancing a broomstick on your palm or keeping a Segway upright",
            "k": ["inverted", "broomstick", "segway"],
            "n": 0
        },
        {
            "id": "conical",
            "tier": "power",
            "t": "A “conical” type’s bob moves in a horizontal circle, so its string traces out a cone",
            "k": ["conical", "horizontal circle", "cone"],
            "n": 0
        },
        {
            "id": "taipei-101",
            "tier": "power",
            "t": "A giant steel ball hung near the top of the Taipei 101 skyscraper is one, swinging to cancel sway from strong winds",
            "k": ["taipei 101", "steel ball", "skyscraper"],
            "n": 0
        },
        {
            "id": "matching-rhythm",
            "tier": "power",
            "t": "Huygens noticed that two clocks of this kind, hung from the same beam, soon fell into a matching rhythm",
            "k": ["matching rhythm", "same beam"],
            "n": 0
        },
        {
            "id": "escapement",
            "tier": "power",
            "t": "The anchor escapement allowed small swings and tall longcase clocks; sliding a metronome’s weight up slows its beat",
            "k": ["anchor escapement", "longcase", "metronome"],
            "n": 0
        },
        {
            "id": "longitude",
            "tier": "power",
            "t": "Huygens hoped clocks of this kind could help sailors find longitude, but the rolling of ships spoiled their timekeeping",
            "k": ["longitude", "sailors", "rolling of ships"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Pendulum or spring?",
        "body": "Pendulums and masses bouncing on springs are the two classic examples of simple harmonic motion, so their clues can sound alike. For small swings, a pendulum’s period depends only on its length and gravity, while a spring’s depends on the mass and on the spring’s stiffness (Hooke’s law). Literature questions on Poe’s “The Pit and the Pendulum” or Umberto Eco’s novel _Foucault’s Pendulum_ want the title, not the device.",
        "fix": "Length, a bob, a pivot, clocks, Galileo, Huygens, or Foucault means a pendulum. A spring constant, stretching, or Hooke’s law means a spring; if the question asks for “this motion,” say simple harmonic motion.",
        "line": "Real answer line: <b><u>pendulum</u></b>s (accept specific types like <u>Foucault pendulum</u>s or <u>simple pendulum</u>s)"
    },
    "tests": {
        "right": [
            "Pendulums",
            "pendulum",
            "Foucault pendulum",
            "Pendelum",
            "simple pendulum"
        ],
        "prompt": [
            "Harmonic oscillator",
            "oscillator"
        ],
        "wrong": [
            "Spring",
            "Simple harmonic motion",
            "Newton's cradle",
            "The Pit and the Pendulum",
            "Oscillation"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
