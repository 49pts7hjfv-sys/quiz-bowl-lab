import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "comets",
    "name": "Comets",
    "mono": "CMT",
    "category": "Astronomy",
    "qbCategory": "Science · Other Science (Astronomy)",
    "kicker": "Icy wanderers with glowing tails · Visitors from the edge of the solar system",
    "dates": "Halley’s first predicted return: 1758",
    "briefing": "Comets are “dirty snowballs” of ice, dust, and rock that spend most of their time in the frozen outer solar system. When one swings close to the Sun, its ice turns to gas, puffing up a fuzzy cloud called a coma and long tails that always point away from the Sun. The most famous, Halley’s Comet, returns about every 76 years; it came by in 1986 and is due back in 2061.",
    "answerHtml": "<b><u>Comets</u></b> (accept <u>comet</u>)",
    "accept": [
        "comet",
        "comets"
    ],
    "prompt": [],
    "reject": [
        "asteroid",
        "asteroids",
        "asteroid belt",
        "meteor",
        "meteors",
        "meteoroid",
        "meteoroids",
        "meteorite",
        "meteorites",
        "meteor shower",
        "meteor showers",
        "shooting star",
        "shooting stars",
        "halleys comet",
        "halley comet",
        "comet halley",
        "halley",
        "hale bopp",
        "shoemaker levy",
        "oort cloud",
        "kuiper belt",
        "dwarf planet",
        "centaur",
        "centaurs"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Comet",
    "qb": {
        "q": "comet",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "By showing that one of these objects had no measurable parallax in 1577, Tycho Brahe proved it was farther away than the Moon. That disproved Aristotle’s teaching that these objects were glowing vapors high in Earth’s air.",
            "r": "These icy bodies grow a fuzzy coma and long tails as they near the Sun. For 10 points, name these “dirty snowballs.”"
        },
        {
            "p": "Charles Messier [“MESS-ee-ay”] listed more than 100 fuzzy objects, such as nebulae and star clusters, so that he would not confuse them with these objects, which he spent his career hunting. The name of these objects comes from a Greek word meaning “long-haired.”",
            "r": "For 10 points, name these icy bodies whose glowing tails point away from the Sun."
        },
        {
            "p": "Fred Whipple’s 1950 “icy conglomerate” model explained that each of these objects has a solid nucleus of frozen gases mixed with dust. When one of these bodies nears the Sun, its ice sublimates, turning straight into gas that forms a fuzzy cloud called a coma.",
            "r": "For 10 points, name these “dirty snowballs,” the most famous of which returns about every 76 years."
        },
        {
            "p": "Some of these objects seem to grow an “antitail” that points toward the Sun, which is really a trick of perspective. Each of these objects usually has a curved, yellowish dust tail and a straight, bluish ion tail pushed outward by the solar wind.",
            "r": "For 10 points, name these icy bodies whose tails always point away from the Sun."
        },
        {
            "p": "A European probe named for the painter Giotto [“JOT-oh”], who may have painted one of these objects as the Star of Bethlehem, flew past the most famous of them in 1986. That same object, seen in 1066, months before the Battle of Hastings, appears on the Bayeux Tapestry.",
            "r": "For 10 points, name these icy bodies with glowing tails, including one named for Edmond Halley."
        },
        {
            "p": "In 2014, a lander named Philae bounced across the surface of 67P/Churyumov–Gerasimenko [“choo-RYOO-mof geh-rah-sih-MEN-koh”], becoming the first spacecraft to land on one of these objects. Its mother ship, Rosetta, was named for the stone that helped scholars decode Egyptian hieroglyphs.",
            "r": "For 10 points, name these icy bodies that form a coma and tails near the Sun."
        },
        {
            "p": "On July 4, 2005, NASA’s Deep Impact mission fired a copper impactor into Tempel 1, one of these objects, to blast out material from beneath its surface. Another NASA mission, Stardust, brought dust from one of these objects back to Earth in 2006.",
            "r": "For 10 points, name these icy bodies that develop long tails when they near the Sun."
        },
        {
            "p": "Amateur astronomer Gennady Borisov discovered the first known one of these objects to come from another star system, in 2019. Most of these objects come from two distant reservoirs: the Kuiper Belt and the much farther Oort cloud.",
            "r": "For 10 points, name these icy bodies, nicknamed “dirty snowballs,” that grow tails as they near the Sun."
        },
        {
            "p": "Using Isaac Newton’s laws, an English astronomer showed that the bright objects seen in 1531, 1607, and 1682 were the same one of these bodies, and he predicted its return in 1758. It came back as predicted, years after his death, and was later given the designation 1P.",
            "r": "For 10 points, name these icy bodies, whose most famous example is named for Edmond Halley."
        },
        {
            "p": "Mark Twain was born in 1835, when one of these objects was visible, and he said he expected to die when it came back. He did, in 1910, one day after it passed closest to the Sun.",
            "r": "That object, named for Edmond Halley, returns about every 76 years. For 10 points, name these icy bodies with glowing tails."
        },
        {
            "p": "Dust shed by one of these objects causes both the Orionid meteor shower in October and the Eta Aquariid [“AY-tuh uh-KWAIR-ee-id”] shower in May. The Perseid shower each August comes from the debris of another one, Swift–Tuttle, which returns about every 133 years.",
            "r": "For 10 points, name these “dirty snowballs” whose leftover dust causes many meteor showers."
        },
        {
            "p": "Discovered separately by Alan Hale and Thomas Bopp in 1995, one of these objects stayed visible to the naked eye for about a year and a half, a record. Its coma and two tails glowed brightly in the night sky during 1997.",
            "r": "For 10 points, name these icy bodies, which come from the Kuiper Belt and the Oort cloud."
        },
        {
            "p": "Ernst Öpik [“UH-pik”] and Jan Oort proposed that a vast, round cloud of icy bodies at the far edge of the solar system sends these objects falling toward the Sun on orbits that can take thousands of years. Shorter-period ones often come from the Kuiper Belt instead.",
            "r": "For 10 points, name these “dirty snowballs,” such as Hale–Bopp and the one named for Edmond Halley."
        },
        {
            "p": "In 1992, Jupiter’s gravity tore one of these objects into more than 20 pieces, which smashed into Jupiter two years later. That object, Shoemaker–Levy 9, was named for the three astronomers who discovered it in 1993.",
            "r": "For 10 points, name these icy bodies that form a coma and a tail when they come near the Sun."
        },
        {
            "p": "In 2013, a sungrazing one of these objects named ISON fell apart as it swung close to the Sun. Most of these objects spend nearly all their time far out in the frozen outer solar system, where they are too cold to grow tails.",
            "r": "When they near the Sun, they grow a fuzzy coma and tails that point away from it. For 10 points, name these icy bodies, nicknamed “dirty snowballs.”"
        }
    ],
    "clues": [
        {
            "id": "dirty-snowballs",
            "tier": "giveaway",
            "t": "Icy bodies nicknamed “dirty snowballs,” made of ice, dust, and rock",
            "k": ["dirty snowballs", "icy bodies"],
            "n": 0
        },
        {
            "id": "tails",
            "tier": "giveaway",
            "t": "Near the Sun they grow glowing tails that always point away from the Sun",
            "k": ["tails", "point away"],
            "n": 0
        },
        {
            "id": "halley",
            "tier": "giveaway",
            "t": "The most famous, named for Edmond Halley, returns about every 76 years (it came by in 1986 and is due back in 2061)",
            "k": ["edmond halley", "halley", "76 years", "2061"],
            "n": 0
        },
        {
            "id": "coma-nucleus",
            "tier": "giveaway",
            "t": "The solid center is the nucleus; near the Sun it puffs up a fuzzy cloud of gas and dust called the coma",
            "k": ["nucleus", "coma"],
            "n": 0
        },
        {
            "id": "oort-kuiper",
            "tier": "giveaway",
            "t": "Long-period ones come from the distant Oort cloud; many short-period ones come from the Kuiper Belt",
            "k": ["oort cloud", "kuiper belt"],
            "n": 0,
            "rabbit": "Oort cloud"
        },
        {
            "id": "two-tails",
            "tier": "middle",
            "t": "Usually two tails: a curved, yellowish dust tail and a straight, bluish ion tail pushed by the solar wind",
            "k": ["dust tail", "ion tail", "solar wind"],
            "n": 0
        },
        {
            "id": "sublimation",
            "tier": "middle",
            "t": "Near the Sun their ice sublimates, turning straight from solid to gas",
            "k": ["sublimates", "solid to gas"],
            "n": 0
        },
        {
            "id": "meteor-showers",
            "tier": "middle",
            "t": "Earth passing through their leftover dust causes meteor showers, like the Perseids from Swift–Tuttle",
            "k": ["meteor showers", "perseids", "swift"],
            "n": 0
        },
        {
            "id": "whipple",
            "tier": "middle",
            "t": "Fred Whipple proposed the “dirty snowball” (icy conglomerate) model in 1950",
            "k": ["whipple", "icy conglomerate", "1950"],
            "n": 0
        },
        {
            "id": "halley-prediction",
            "tier": "middle",
            "t": "Edmond Halley used Newton’s laws to show the visitors of 1531, 1607, and 1682 were one object, and predicted its return in 1758",
            "k": ["newton", "1758", "1682"],
            "n": 0,
            "rabbit": "Isaac Newton"
        },
        {
            "id": "mark-twain",
            "tier": "middle",
            "t": "Mark Twain was born in 1835 and died in 1910, both years when the one named for Halley passed close to the Sun",
            "k": ["mark twain", "1835", "1910"],
            "n": 0,
            "rabbit": "Mark Twain"
        },
        {
            "id": "shoemaker-levy",
            "tier": "middle",
            "t": "Shoemaker–Levy 9 was torn apart by Jupiter’s gravity and crashed into Jupiter in 1994",
            "k": ["shoemaker", "levy", "1994"],
            "n": 0,
            "rabbit": "Jupiter"
        },
        {
            "id": "bayeux",
            "tier": "middle",
            "t": "The one named for Halley appears on the Bayeux Tapestry, which shows it in the sky in 1066 before the Battle of Hastings",
            "k": ["bayeux tapestry", "1066", "hastings"],
            "n": 0,
            "rabbit": "Battle of Hastings"
        },
        {
            "id": "long-haired",
            "tier": "middle",
            "t": "Their name comes from a Greek word meaning “long-haired”",
            "k": ["long-haired", "greek"],
            "n": 0
        },
        {
            "id": "tycho-1577",
            "tier": "power",
            "t": "Tycho Brahe found no parallax for the bright one of 1577, proving it lay beyond the Moon, not in Earth’s air as Aristotle had taught",
            "k": ["tycho", "1577", "parallax", "aristotle"],
            "n": 0
        },
        {
            "id": "messier",
            "tier": "power",
            "t": "Charles Messier hunted them and cataloged fuzzy look-alikes such as nebulae so he would not be fooled, creating the Messier catalog",
            "k": ["messier", "catalog"],
            "n": 0
        },
        {
            "id": "rosetta-philae",
            "tier": "power",
            "t": "ESA’s Rosetta orbited 67P/Churyumov–Gerasimenko, and its lander Philae made the first landing on one, in 2014",
            "k": ["rosetta", "philae", "67p", "2014"],
            "n": 0
        },
        {
            "id": "deep-impact",
            "tier": "power",
            "t": "NASA’s Deep Impact fired a copper impactor into Tempel 1 on July 4, 2005",
            "k": ["deep impact", "tempel 1", "copper"],
            "n": 0
        },
        {
            "id": "stardust",
            "tier": "power",
            "t": "NASA’s Stardust caught dust from Wild 2 [“VILT”] in a spongy material called aerogel and returned it to Earth in 2006",
            "k": ["stardust", "wild 2", "aerogel", "2006"],
            "n": 0
        },
        {
            "id": "giotto",
            "tier": "power",
            "t": "ESA’s Giotto probe flew past the one named for Halley in 1986; it was named for the painter who probably showed that same object as the Star of Bethlehem",
            "k": ["giotto", "star of bethlehem", "1986"],
            "n": 0
        },
        {
            "id": "opik-oort",
            "tier": "power",
            "t": "Ernst Öpik (1932) and Jan Oort (1950) proposed a vast, round cloud of icy bodies at the solar system’s edge",
            "k": ["jan oort", "1932", "1950"],
            "n": 0
        },
        {
            "id": "antitail",
            "tier": "power",
            "t": "An “antitail” seems to point toward the Sun, but it is just a trick of perspective",
            "k": ["antitail", "perspective"],
            "n": 0
        },
        {
            "id": "borisov",
            "tier": "power",
            "t": "2I/Borisov, found in 2019 by amateur astronomer Gennady Borisov, was the first known interstellar one",
            "k": ["borisov", "interstellar", "2019"],
            "n": 0
        },
        {
            "id": "periodic-1p",
            "tier": "power",
            "t": "The one named for Halley was the first recognized as periodic, so it is designated 1P",
            "k": ["periodic", "1p"],
            "n": 0
        },
        {
            "id": "hale-bopp",
            "tier": "power",
            "t": "Hale–Bopp (found in 1995, brightest in 1997) stayed visible to the naked eye for a record of about 18 months",
            "k": ["naked eye", "1997", "18 months"],
            "n": 0
        },
        {
            "id": "halley-showers",
            "tier": "power",
            "t": "Dust from the one named for Halley causes the Orionid (October) and Eta Aquariid (May) meteor showers",
            "k": ["orionid", "eta aquariid"],
            "n": 0
        },
        {
            "id": "ison",
            "tier": "power",
            "t": "The sungrazer ISON broke apart near the Sun in 2013",
            "k": ["ison", "sungrazer", "2013"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Comet, asteroid, or meteor?",
        "body": "Comets get mixed up with rocky asteroids and with meteors, the streaks of light made when bits of space dust burn up in Earth’s air. Players also hear “Edmond Halley” and blurt out “Halley’s Comet” when the question wants the whole group. And the Oort cloud and the Kuiper Belt are where comets come from, not the objects themselves.",
        "fix": "A coma, a tail, ice that sublimates, or the nickname “dirty snowball” means comets. Rocky bodies in the belt between Mars and Jupiter are asteroids; a streak of light in the sky is a meteor; a space rock that reaches the ground is a meteorite. If the question says “these objects,” give the general term, not one famous example.",
        "line": "Real answer line: <b><u>Comets</u></b> (accept <u>comet</u>)"
    },
    "tests": {
        "right": [
            "Comets",
            "comet",
            "Comit",
            "a comet",
            "long-period comets"
        ],
        "prompt": [],
        "wrong": [
            "Asteroids",
            "Meteor",
            "Halley's Comet",
            "Oort cloud",
            "Meteorite",
            "Kuiper Belt"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
