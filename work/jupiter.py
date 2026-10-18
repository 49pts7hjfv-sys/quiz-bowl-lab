import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "jupiter",
    "name": "Jupiter",
    "mono": "JUP",
    "category": "Astronomy",
    "qbCategory": "Science · Other Science (Astronomy)",
    "kicker": "Largest planet in the solar system · Home of the Great Red Spot",
    "dates": "Known since ancient times; Galilean moons found 1610",
    "briefing": "Jupiter is so huge that all the other planets could fit inside it, and it has more than twice as much mass as all of them put together. Its Great Red Spot is a storm wider than Earth that astronomers have watched for more than 150 years. In 1610, Galileo spotted four moons circling it, the first proof that not everything in the sky goes around Earth.",
    "answerHtml": "<b><u>Jupiter</u></b>",
    "accept": [
        "jupiter",
        "planet jupiter"
    ],
    "prompt": [],
    "reject": [
        "zeus",
        "jove",
        "saturn",
        "uranus",
        "neptune",
        "great red spot",
        "ganymede",
        "europa",
        "io",
        "callisto",
        "juno"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Jupiter",
    "qb": {
        "q": "Jupiter",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "In 1676, Ole Rømer [“ROH-mer”] noticed that eclipses of one of this planet’s moons came earlier or later than expected depending on how far Earth was from this planet, showing that light travels at a finite speed. That moon, Io [“EYE-oh”], is the most volcanically active body in the solar system.",
            "r": "For 10 points, name this largest planet in the solar system, home of the Great Red Spot."
        },
        {
            "p": "Three moons of this planet are locked in a 1:2:4 pattern called the Laplace resonance: the innermost circles four times for each orbit of the outermost. The resulting tidal squeezing heats the innermost moon, Io, and may keep an ocean liquid beneath the ice of Europa.",
            "r": "For 10 points, name this planet whose four largest moons were discovered by Galileo in 1610."
        },
        {
            "p": "While studying Voyager 1 images in 1979, navigation engineer Linda Morabito spotted a plume rising from one of this planet’s moons, the first active volcano ever found beyond Earth. Voyager 1 also discovered this planet’s faint, dusty rings that same year.",
            "r": "For 10 points, name this fifth planet from the Sun, the largest planet in the solar system."
        },
        {
            "p": "In _Sidereus Nuncius_, or _The Starry Messenger_, a scientist called four objects circling this planet the “Medicean Stars” to honor his patrons, the Medici family. Those objects, first spotted in January 1610, proved that not everything in the sky revolves around Earth.",
            "r": "That scientist was Galileo. For 10 points, name this planet, named for the king of the Roman gods."
        },
        {
            "p": "This planet gives off more heat than it receives from the Sun, because it is still slowly shrinking and releasing energy, a process called the Kelvin–Helmholtz mechanism. Deep inside it, crushing pressure turns hydrogen into a liquid metal that produces the strongest magnetic field of any planet.",
            "r": "For 10 points, name this gas giant with a huge storm called the Great Red Spot."
        },
        {
            "p": "Between 1998 and 2000, three white storms on this planet merged into a single storm called Oval BA, which later turned red and was nicknamed “Red Spot Junior.” Its larger cousin is a high-pressure storm that has been shrinking but is still wider than Earth.",
            "r": "For 10 points, name this planet whose Great Red Spot astronomers have watched for more than 150 years."
        },
        {
            "p": "Daniel Kirkwood explained the gaps in the asteroid belt: an asteroid in one of them would circle the Sun, for example, exactly three times for each orbit of this planet, so this planet’s repeated tugs would pull it away. Thousands of Trojan asteroids share this planet’s orbit at two Lagrange points.",
            "r": "For 10 points, name this planet just beyond the asteroid belt, the largest in the solar system."
        },
        {
            "p": "Pioneer 10 made the first flyby of this planet in 1973, and the Galileo spacecraft later orbited it for nearly eight years before plunging into its clouds in 2003. In 1995, Galileo had dropped a probe that parachuted into this planet’s atmosphere.",
            "r": "This planet has more than twice the mass of all the other planets combined. For 10 points, name this largest planet in the solar system."
        },
        {
            "p": "In July 1994, more than 20 pieces of Comet Shoemaker–Levy 9 slammed into this planet, leaving dark scars in its clouds, some about as wide as Earth. This planet’s gravity had torn that comet apart during a close pass two years earlier.",
            "r": "For 10 points, name this gas giant, the fifth planet from the Sun and the largest of all."
        },
        {
            "p": "A NASA probe named for the goddess who could see through the clouds her husband wrapped around himself began orbiting this planet on July 4, 2016. That probe, Juno, found clusters of giant cyclones swirling around this planet’s poles.",
            "r": "For 10 points, name this planet, named for the Roman king of the gods."
        },
        {
            "p": "The fourth movement of Gustav Holst’s _The Planets_ is named for this planet, “the Bringer of Jollity,” and its stately middle tune became the hymn “I Vow to Thee, My Country.” The word “jovial” comes from this planet’s link to good cheer in old astrology.",
            "r": "For 10 points, name this gas giant, the largest planet in the solar system and the fifth from the Sun."
        },
        {
            "p": "This planet’s moon Ganymede [“GAN-ih-meed”] is the only moon known to make its own magnetic field, and it is bigger than the planet Mercury. Another of this planet’s moons, Callisto, is one of the most heavily cratered objects in the solar system.",
            "r": "For 10 points, name this planet whose moon Europa may hide an ocean beneath its icy crust."
        },
        {
            "p": "In 2023, Europe launched a mission called JUICE to study this planet’s icy moons, and in 2024 NASA launched Europa Clipper to learn whether one of them could support life. That moon is thought to hide a salty ocean of liquid water beneath its frozen crust.",
            "r": "For 10 points, name this planet, whose moon Europa was discovered by Galileo along with Io, Ganymede, and Callisto."
        },
        {
            "p": "Because it spins once in just under 10 hours, the fastest rotation of any planet, this planet bulges noticeably at its equator. Its clouds are stretched into light-colored bands called zones and darker bands called belts.",
            "r": "Its Great Red Spot is a storm larger than Earth. For 10 points, name this largest planet in the solar system."
        },
        {
            "p": "Simon Marius, who claimed he had spotted them on his own, gave four of this planet’s moons the names they still carry, all taken from Greek myths. Those four moons were the first objects ever found orbiting a planet other than Earth.",
            "r": "The giant planets are often called “Jovian,” meaning “like this planet.” For 10 points, name this largest planet in the solar system."
        }
    ],
    "clues": [
        {
            "id": "largest-planet",
            "tier": "giveaway",
            "t": "The largest planet in the solar system: a gas giant more than twice as massive as all the other planets combined",
            "k": ["largest planet", "gas giant", "twice as massive"],
            "n": 0
        },
        {
            "id": "fifth-planet",
            "tier": "giveaway",
            "t": "Fifth planet from the Sun, the first one beyond the asteroid belt",
            "k": ["fifth planet", "asteroid belt"],
            "n": 0
        },
        {
            "id": "great-red-spot",
            "tier": "giveaway",
            "t": "Its Great Red Spot is a giant high-pressure storm wider than Earth",
            "k": ["great red spot", "storm"],
            "n": 0,
            "rabbit": "Great Red Spot"
        },
        {
            "id": "galilean-moons",
            "tier": "giveaway",
            "t": "Galileo discovered its four largest moons, Io, Europa, Ganymede, and Callisto, in 1610",
            "k": ["galileo", "1610", "galilean moons"],
            "n": 0,
            "rabbit": "Galileo Galilei"
        },
        {
            "id": "king-of-gods",
            "tier": "giveaway",
            "t": "Named for the king of the Roman gods, the counterpart of the Greek Zeus",
            "k": ["king of the roman gods", "zeus"],
            "n": 0,
            "rabbit": "Zeus"
        },
        {
            "id": "ganymede",
            "tier": "middle",
            "t": "Its moon Ganymede is the largest moon in the solar system, bigger than the planet Mercury, and the only moon known to make its own magnetic field",
            "k": ["ganymede", "largest moon", "mercury"],
            "n": 0,
            "rabbit": "Ganymede"
        },
        {
            "id": "io-volcanoes",
            "tier": "middle",
            "t": "Its moon Io is the most volcanically active body in the solar system",
            "k": ["volcanically active", "io"],
            "n": 0,
            "rabbit": "Io"
        },
        {
            "id": "europa-ocean",
            "tier": "middle",
            "t": "Its moon Europa hides a salty ocean of liquid water under an icy crust, making it a top place to look for life",
            "k": ["europa", "ocean", "icy crust"],
            "n": 0,
            "rabbit": "Europa (moon)"
        },
        {
            "id": "fast-spin",
            "tier": "middle",
            "t": "Spins faster than any other planet: a day lasts just under 10 hours, so it bulges at its equator",
            "k": ["10 hours", "spins faster", "bulges"],
            "n": 0
        },
        {
            "id": "zones-belts",
            "tier": "middle",
            "t": "Its cloud stripes are light-colored zones and darker belts",
            "k": ["zones", "belts"],
            "n": 0
        },
        {
            "id": "shoemaker-levy",
            "tier": "middle",
            "t": "More than 20 pieces of Comet Shoemaker–Levy 9 slammed into it in July 1994",
            "k": ["shoemaker", "levy", "1994"],
            "n": 0,
            "rabbit": "Comets"
        },
        {
            "id": "juno",
            "tier": "middle",
            "t": "NASA’s Juno probe, named for the wife of its namesake god, began orbiting it on July 4, 2016, and found giant cyclones at its poles",
            "k": ["juno", "2016", "cyclones"],
            "n": 0
        },
        {
            "id": "liquid-metal",
            "tier": "middle",
            "t": "Deep inside, crushing pressure turns hydrogen into a liquid metal that creates the strongest magnetic field of any planet",
            "k": ["liquid metal", "magnetic field", "hydrogen"],
            "n": 0,
            "rabbit": "Hydrogen"
        },
        {
            "id": "holst-jollity",
            "tier": "middle",
            "t": "Gustav Holst’s suite _The Planets_ calls it “the Bringer of Jollity”",
            "k": ["holst", "jollity", "the planets"],
            "n": 0
        },
        {
            "id": "jove",
            "tier": "middle",
            "t": "The words “jovial” and “Jovian” (used for the giant planets) come from Jove, another name for its namesake god",
            "k": ["jove", "jovial", "jovian"],
            "n": 0
        },
        {
            "id": "romer",
            "tier": "power",
            "t": "Ole Rømer timed eclipses of its moon Io to show in 1676 that light travels at a finite speed",
            "k": ["eclipses", "1676", "finite speed"],
            "n": 0
        },
        {
            "id": "laplace",
            "tier": "power",
            "t": "Io, Europa, and Ganymede are locked in a 1:2:4 orbital pattern called the Laplace resonance",
            "k": ["laplace resonance", "resonance"],
            "n": 0
        },
        {
            "id": "morabito",
            "tier": "power",
            "t": "Linda Morabito spotted a volcanic plume on Io in Voyager 1 images (1979), the first active volcano found beyond Earth",
            "k": ["morabito", "voyager 1", "1979"],
            "n": 0
        },
        {
            "id": "rings",
            "tier": "power",
            "t": "Voyager 1 discovered its faint, dusty rings in 1979",
            "k": ["dusty rings", "rings"],
            "n": 0
        },
        {
            "id": "medicean",
            "tier": "power",
            "t": "Galileo named its four big moons the “Medicean Stars” for the Medici family in _Sidereus Nuncius_ (_The Starry Messenger_)",
            "k": ["medicean stars", "medici", "sidereus nuncius", "starry messenger"],
            "n": 0
        },
        {
            "id": "marius",
            "tier": "power",
            "t": "Simon Marius claimed he found the four big moons on his own and gave them their names from Greek myths",
            "k": ["simon marius", "marius"],
            "n": 0
        },
        {
            "id": "kelvin-helmholtz",
            "tier": "power",
            "t": "Gives off more heat than it gets from the Sun because it is slowly shrinking (the Kelvin–Helmholtz mechanism)",
            "k": ["more heat", "shrinking", "kelvin"],
            "n": 0
        },
        {
            "id": "oval-ba",
            "tier": "power",
            "t": "Oval BA, nicknamed “Red Spot Junior,” formed when three white storms merged between 1998 and 2000",
            "k": ["oval ba", "red spot junior", "white storms"],
            "n": 0
        },
        {
            "id": "kirkwood",
            "tier": "power",
            "t": "Its repeated tugs clear out the Kirkwood gaps in the asteroid belt",
            "k": ["kirkwood gaps", "kirkwood"],
            "n": 0
        },
        {
            "id": "trojans",
            "tier": "power",
            "t": "Thousands of Trojan asteroids share its orbit at two Lagrange points; NASA’s Lucy probe, launched in 2021, was sent to visit them",
            "k": ["trojan asteroids", "lagrange points", "lucy"],
            "n": 0
        },
        {
            "id": "spacecraft",
            "tier": "power",
            "t": "Pioneer 10 made the first flyby (1973); the Galileo orbiter (1995–2003) dropped a probe into its atmosphere",
            "k": ["pioneer 10", "galileo orbiter", "probe", "1973"],
            "n": 0
        },
        {
            "id": "juice-clipper",
            "tier": "power",
            "t": "Europe’s JUICE (launched 2023) and NASA’s Europa Clipper (launched 2024) were sent to study its icy moons",
            "k": ["juice", "europa clipper", "icy moons"],
            "n": 0
        },
        {
            "id": "callisto",
            "tier": "power",
            "t": "Its moon Callisto is one of the most heavily cratered objects in the solar system",
            "k": ["callisto", "cratered"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Moon clue, planet answer",
        "body": "Many Jupiter tossups lead with clues about its moons: Io’s volcanoes, Europa’s hidden ocean, Ganymede’s magnetic field. Players who recognize the moon blurt out “Io” or “Europa,” but the question asks for the planet. Saturn, the other gas giant with a huge family of moons, is the next most common wrong answer, and Zeus is only the Greek god, not the planet.",
        "fix": "Listen for the noun: “this planet” wants the planet, even if every clue so far was about a moon. Galileo’s four moons, the Great Red Spot, Shoemaker–Levy 9, and the Juno probe mean Jupiter; bright icy rings, Titan, Enceladus, the hexagon, and the Cassini mission mean Saturn.",
        "line": "Real answer line: <b><u>Jupiter</u></b>"
    },
    "tests": {
        "right": [
            "Jupiter",
            "jupiter",
            "Jupitor",
            "Planet Jupiter",
            "the planet Jupiter"
        ],
        "prompt": [],
        "wrong": [
            "Saturn",
            "Zeus",
            "Jove",
            "Great Red Spot",
            "Ganymede",
            "Io"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
