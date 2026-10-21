import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TIP = "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."

data = {
    "id": "oort-cloud",
    "name": "Oort cloud",
    "mono": "OCL",
    "category": "Astronomy",
    "qbCategory": "Science · Other Science (Astronomy)",
    "kicker": "Distant shell of icy bodies around the Sun · Home of long-period comets",
    "dates": "Proposed by Öpik (1932) and Oort (1950)",
    "briefing": "Far beyond Pluto, a giant shell of icy bodies may surround the whole solar system: the Oort cloud. No telescope has ever seen it directly, but astronomers think it holds billions or even trillions of frozen comet nuclei, stretching out perhaps 100,000 times as far from the Sun as Earth is. Every so often, a passing star or the pull of the Milky Way nudges one inward, and it becomes a long-period comet swooping past the Sun.",
    "answerHtml": "<b><u>Oort cloud</u></b> (accept <u>Öpik–Oort cloud</u>; prompt on <u>Oort</u> alone or <u>Hills cloud</u>; do not accept “Kuiper belt,” “asteroid belt,” or “scattered disk”)",
    "accept": [
        "oort cloud",
        "opik oort cloud",
        "oort opik cloud"
    ],
    "prompt": [
        "oort",
        "hills cloud"
    ],
    "reject": [
        "kuiper belt",
        "edgeworth kuiper belt",
        "kuiper",
        "asteroid belt",
        "main belt",
        "scattered disk",
        "scattered disc",
        "comet",
        "comets",
        "long period comet",
        "long period comets",
        "sedna",
        "heliosphere",
        "heliopause",
        "termination shock",
        "van allen belt",
        "van allen belts",
        "jan oort",
        "kuiper cliff",
        "nemesis"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Oort_cloud",
    "qb": {
        "q": "Oort cloud",
        "found": 0,
        "tip": TIP
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "In 1932, the Estonian astronomer Ernst Öpik [“UH-pik”] suggested that comets could come from a distant swarm of icy bodies only loosely held by the Sun’s gravity. A Dutch astronomer proposed a similar idea in 1950 to explain where comets with very long orbits come from.",
            "r": "That astronomer was Jan Oort. For 10 points, name this distant, roughly spherical cloud of icy bodies."
        },
        {
            "p": "A 1950 paper pointed out that comets with very long orbits fall in from every direction, not just along the flat plane of the planets, and that many of their orbits stretch out to tens of thousands of times Earth’s distance from the Sun.",
            "r": "That paper proposed this vast reservoir of comets. For 10 points, name this distant shell of icy bodies, named for a Dutch astronomer."
        },
        {
            "p": "In 1981, Jack Hills proposed that this region has a denser, doughnut-shaped inner part, which is sometimes called the Hills cloud. The discoverers of Sedna, found in 2003, suggested that it might be the first known member of that inner part.",
            "r": "For 10 points, name this distant shell of icy bodies thought to be the source of long-period comets."
        },
        {
            "p": "NASA estimates that Voyager 1, launched in 1977, will take about 300 years to reach the inner edge of this region and possibly 30,000 years to fly all the way through it.",
            "r": "For 10 points, name this vast cloud of icy bodies at the outer edge of the solar system, the source of long-period comets."
        },
        {
            "p": "Objects in this region are held so weakly by the Sun that the tidal pull of the Milky Way itself, along with the gravity of passing stars and giant gas clouds, can nudge them onto orbits that carry them toward the Sun.",
            "r": "They then become long-period comets. For 10 points, name this distant shell of icy bodies surrounding the solar system."
        },
        {
            "p": "Measurements from the Gaia spacecraft show that Gliese 710, a dim orange star with a bit more than half the Sun’s mass, should pass through this region in about 1.3 million years, possibly sending a shower of comets toward the inner solar system.",
            "r": "For 10 points, name this distant cloud of icy bodies, which has never been seen directly."
        },
        {
            "p": "In 1984, some scientists proposed that a dim companion star of the Sun, nicknamed Nemesis, swings through this region about every 26 million years, stirring up comet showers that cause mass extinctions. Sky surveys such as NASA’s WISE found no such star.",
            "r": "For 10 points, name this distant cloud of icy bodies, the source of long-period comets."
        },
        {
            "p": "Most objects in this region probably formed much closer to the Sun, among the giant planets, until close encounters with Jupiter, Saturn, Uranus, and Neptune flung them far outward early in the solar system’s history.",
            "r": "For 10 points, name this distant shell of icy bodies, named for the Dutch astronomer Jan Oort."
        },
        {
            "p": "No object in this region has ever been seen in place, because its icy bodies are small, dark, and extremely far away. Its inner edge may lie a few thousand times farther from the Sun than Earth does.",
            "r": "For 10 points, name this hypothetical cloud of icy bodies, the home of long-period comets."
        },
        {
            "p": "Comet Hale–Bopp, which stayed visible to the naked eye for about a year and a half, and Comet Hyakutake [“hyah-koo-TAH-keh”], which swept close to Earth in 1996, probably both began their journeys in this region.",
            "r": "Such long-period comets fall in from this region when something disturbs their orbits. For 10 points, name this distant cloud of icy bodies."
        },
        {
            "p": "The Dutch astronomer this region is named for also gave his name to two constants that describe how the Milky Way rotates, and his work helped show that the Sun lies far from the galaxy’s center.",
            "r": "For 10 points, name this distant cloud of icy bodies that sends long-period comets toward the Sun."
        },
        {
            "p": "Astronomers call comets making their first trip in from this region “dynamically new,” and their ice has never been warmed much by the Sun. One such comet, ISON, broke apart in 2013 as it swung extremely close to the Sun.",
            "r": "Such comets have orbits lasting thousands or even millions of years. For 10 points, name this distant reservoir of comets that surrounds the solar system."
        },
        {
            "p": "The outer edge of this region may mark roughly where the Sun’s gravity stops being stronger than the pull of other stars and the rest of the galaxy. That makes this region far larger than the heliosphere, the bubble of solar wind that Voyager 1 left in 2012.",
            "r": "For 10 points, name this roughly spherical cloud of icy bodies, often described as the outer edge of the solar system."
        },
        {
            "p": "Some estimates place the outer edge of this region about 100,000 times as far from the Sun as Earth is, so far that sunlight would need more than a year and a half to get there.",
            "r": "For 10 points, name this distant, roughly spherical cloud of icy bodies, named for the astronomer Jan Oort."
        },
        {
            "p": "About 70,000 years ago, a dim red dwarf later named Scholz’s [“SHOLTS-iz”] Star and its brown dwarf partner probably passed through the outer part of this region, the closest flyby of a star then known when astronomers announced it in 2015.",
            "r": "For 10 points, name this distant cloud of icy bodies, the source of long-period comets."
        }
    ],
    "clues": [
        {
            "id": "long-period",
            "tier": "giveaway",
            "t": "Thought to be the source of long-period comets, which take more than about 200 years to orbit the Sun",
            "k": ["long-period comets", "200 years"],
            "n": 0,
            "rabbit": "Comets"
        },
        {
            "id": "spherical-shell",
            "tier": "giveaway",
            "t": "A huge, roughly spherical shell of icy bodies surrounding the solar system",
            "k": ["spherical shell", "icy bodies"],
            "n": 0
        },
        {
            "id": "jan-oort",
            "tier": "giveaway",
            "t": "Named for the Dutch astronomer Jan Oort, who proposed it in 1950",
            "k": ["dutch", "1950"],
            "n": 0
        },
        {
            "id": "never-seen",
            "tier": "giveaway",
            "t": "Hypothetical: no object in it has ever been observed directly",
            "k": ["hypothetical", "observed directly"],
            "n": 0
        },
        {
            "id": "beyond-kuiper",
            "tier": "giveaway",
            "t": "Lies far beyond Pluto and the Kuiper belt",
            "k": ["kuiper belt", "pluto"],
            "n": 0,
            "rabbit": "Kuiper Belt"
        },
        {
            "id": "opik",
            "tier": "middle",
            "t": "The Estonian astronomer Ernst Öpik suggested a similar reservoir in 1932, so his name is sometimes added to its name",
            "k": ["öpik", "1932", "estonian"],
            "n": 0
        },
        {
            "id": "distance",
            "tier": "middle",
            "t": "Estimates put its inner edge at a few thousand AU and its outer edge at about 100,000 AU or more",
            "k": ["100,000 au", "few thousand"],
            "n": 0
        },
        {
            "id": "nudges",
            "tier": "middle",
            "t": "Passing stars, giant gas clouds, and the Milky Way’s tidal pull nudge its objects toward the Sun",
            "k": ["passing stars", "tidal pull", "milky way"],
            "n": 0
        },
        {
            "id": "voyager",
            "tier": "middle",
            "t": "Voyager 1 will take about 300 years to reach its inner edge and possibly 30,000 years to cross it",
            "k": ["voyager 1", "300 years", "30,000 years"],
            "n": 0
        },
        {
            "id": "all-directions",
            "tier": "middle",
            "t": "Long-period comets fall in from all directions, a clue that their source is round, not flat",
            "k": ["all directions", "round"],
            "n": 0
        },
        {
            "id": "flung-outward",
            "tier": "middle",
            "t": "Its objects probably formed near the giant planets and were flung outward by their gravity",
            "k": ["giant planets", "flung outward"],
            "n": 0
        },
        {
            "id": "famous-comets",
            "tier": "middle",
            "t": "Long-period comets such as Hale–Bopp and Hyakutake probably began their journeys there",
            "k": ["hale–bopp", "hyakutake"],
            "n": 0
        },
        {
            "id": "billions",
            "tier": "middle",
            "t": "May hold billions or even trillions of icy objects",
            "k": ["trillions", "billions"],
            "n": 0
        },
        {
            "id": "heliosphere",
            "tier": "middle",
            "t": "Lies far beyond the heliosphere, the bubble of solar wind that Voyager 1 left in 2012",
            "k": ["heliosphere", "2012", "solar wind"],
            "n": 0
        },
        {
            "id": "hills",
            "tier": "power",
            "t": "Jack Hills (1981) proposed a denser, doughnut-shaped inner part, sometimes called the Hills cloud",
            "k": ["jack hills", "1981", "doughnut-shaped"],
            "n": 0
        },
        {
            "id": "sedna",
            "tier": "power",
            "t": "Sedna’s discoverers (2003) suggested that it might be the first known member of the inner part",
            "k": ["sedna", "2003"],
            "n": 0
        },
        {
            "id": "nemesis",
            "tier": "power",
            "t": "The 1984 “Nemesis” idea: an unseen companion star stirs up comet showers every 26 million years; WISE found no such star",
            "k": ["nemesis", "26 million years", "wise"],
            "n": 0
        },
        {
            "id": "gliese-710",
            "tier": "power",
            "t": "Gaia data show that the star Gliese 710 should pass through it in about 1.3 million years",
            "k": ["gliese 710", "1.3 million years", "gaia"],
            "n": 0
        },
        {
            "id": "oort-evidence",
            "tier": "power",
            "t": "Oort noticed that many long-period comets have orbits reaching out tens of thousands of AU",
            "k": ["tens of thousands", "orbits"],
            "n": 0
        },
        {
            "id": "dynamically-new",
            "tier": "power",
            "t": "Comets on their first trip in are called “dynamically new”; ISON (2013) was one, and it broke apart near the Sun",
            "k": ["dynamically new", "ison", "2013"],
            "n": 0
        },
        {
            "id": "oort-constants",
            "tier": "power",
            "t": "Its namesake also names two constants describing how the Milky Way rotates",
            "k": ["constants", "rotates"],
            "n": 0
        },
        {
            "id": "light-travel",
            "tier": "power",
            "t": "If its outer edge is 100,000 AU away, sunlight would need more than a year and a half to get there",
            "k": ["sunlight", "year and a half"],
            "n": 0
        },
        {
            "id": "sun-gravity-edge",
            "tier": "power",
            "t": "Its outer edge may mark roughly where the Sun’s gravity stops beating the pull of other stars",
            "k": ["sun’s gravity", "other stars"],
            "n": 0
        },
        {
            "id": "scholz",
            "tier": "power",
            "t": "Scholz’s Star and its brown dwarf partner probably passed through its outer part about 70,000 years ago",
            "k": ["scholz", "70,000 years", "brown dwarf"],
            "n": 0
        },
        {
            "id": "comet-showers",
            "tier": "power",
            "t": "A close-passing star could send a “comet shower” toward the inner solar system",
            "k": ["comet shower", "close-passing"],
            "n": 0
        },
        {
            "id": "interstellar",
            "tier": "power",
            "t": "Oort also noticed that no comets seemed to arrive from interstellar space",
            "k": ["interstellar space"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Cloud or belt?",
        "body": "The solar system has two icy reservoirs, and they sound alike. The Kuiper belt is a flat, doughnut-shaped ring just beyond Neptune that holds Pluto and sends in many short-period comets; the Oort cloud is a far more distant, roughly round shell that has never been seen directly and sends in long-period comets. Players also confuse both with the rocky asteroid belt between Mars and Jupiter.",
        "fix": "Ernst Öpik, Jan Oort, a round shell, the Milky Way’s tidal pull, Gliese 710, or comets that take thousands of years to orbit mean the Oort cloud. Pluto, Arrokoth, New Horizons, or plutinos mean the Kuiper belt. Saying only “Oort” earns a prompt, so add “cloud.”",
        "line": "Real answer line: <b><u>Oort cloud</u></b> (accept <u>Öpik–Oort cloud</u>; prompt on <u>Oort</u>; do not accept “Kuiper belt”)"
    },
    "tests": {
        "right": [
            "Oort cloud",
            "oort cloud",
            "Oort clowd",
            "Öpik–Oort cloud",
            "the Oort cloud",
            "inner Oort cloud"
        ],
        "prompt": [
            "Oort",
            "Hills cloud"
        ],
        "wrong": [
            "Kuiper belt",
            "Asteroid belt",
            "Scattered disk",
            "Comets",
            "Sedna",
            "Heliopause"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
