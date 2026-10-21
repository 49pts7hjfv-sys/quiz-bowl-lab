import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TIP = "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."

data = {
    "id": "nebulae",
    "name": "Nebulae",
    "mono": "NEB",
    "category": "Astronomy",
    "qbCategory": "Science · Other Science (Astronomy)",
    "kicker": "Glowing clouds of gas and dust · Where stars are born and where they die",
    "dates": "First photographed in 1880 (in Orion’s sword)",
    "briefing": "A nebula is a cloud of gas and dust floating between the stars, and its name is Latin for “mist.” Some glow red like giant neon signs, some shine blue by reflecting starlight, and some are dark blotches that block the stars behind them. Nebulae are where stars are born, like the Orion Nebula in Orion’s sword, and they are also what dying stars leave behind.",
    "answerHtml": "<b><u>nebula</u></b>e (accept <u>nebula</u> or <u>nebula</u>s; accept specific types such as <u>emission nebula</u>e or <u>planetary nebula</u>e; prompt on <u>interstellar cloud</u>s or <u>molecular cloud</u>s; do not accept “galaxies” or a single named nebula such as the “Crab Nebula”)",
    "accept": [
        "nebula",
        "nebulae",
        "nebulas",
        "emission nebula",
        "emission nebulae",
        "reflection nebula",
        "reflection nebulae",
        "dark nebula",
        "dark nebulae",
        "planetary nebula",
        "planetary nebulae",
        "diffuse nebula",
        "diffuse nebulae",
        "interstellar nebula",
        "interstellar nebulae"
    ],
    "prompt": [
        "interstellar cloud",
        "interstellar clouds",
        "molecular cloud",
        "molecular clouds",
        "gas cloud",
        "gas clouds",
        "dust cloud",
        "dust clouds",
        "cloud of gas and dust",
        "clouds of gas and dust",
        "clouds",
        "cloud",
        "stellar nursery",
        "stellar nurseries",
        "h ii region",
        "h ii regions",
        "hii region",
        "hii regions"
    ],
    "reject": [
        "galaxy",
        "galaxies",
        "spiral nebula",
        "spiral nebulae",
        "extragalactic nebula",
        "extragalactic nebulae",
        "andromeda nebula",
        "great andromeda nebula",
        "star cluster",
        "star clusters",
        "cluster",
        "clusters",
        "globular cluster",
        "globular clusters",
        "open cluster",
        "open clusters",
        "crab nebula",
        "orion nebula",
        "great orion nebula",
        "horsehead nebula",
        "ring nebula",
        "southern ring nebula",
        "eagle nebula",
        "helix nebula",
        "cats eye nebula",
        "lagoon nebula",
        "trifid nebula",
        "carina nebula",
        "tarantula nebula",
        "veil nebula",
        "dumbbell nebula",
        "solar nebula",
        "pillars of creation",
        "comet",
        "comets",
        "supernova",
        "supernovae",
        "quasar",
        "quasars",
        "constellation",
        "constellations",
        "black hole",
        "black holes",
        "stars"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Nebula",
    "qb": {
        "q": "nebulae",
        "found": 0,
        "tip": TIP
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "In 1864, William Huggins pointed a spectroscope at the Cat’s Eye in the constellation Draco and saw a few bright lines instead of a full rainbow of colors. That proved the object was a glowing gas, not a swarm of distant stars.",
            "r": "It is a planetary example of these objects. For 10 points, name these clouds of gas and dust in space."
        },
        {
            "p": "A bright green line in the light of many of these objects was once blamed on an unknown element nicknamed “nebulium.” In 1927, Ira Bowen showed that the line actually comes from oxygen atoms missing two electrons, glowing in extremely thin gas.",
            "r": "For 10 points, name these glowing clouds of gas and dust, such as M42 in Orion’s sword."
        },
        {
            "p": "William Herschel named one type of these objects for their round, greenish disks, which reminded him of planets like Uranus, which he had discovered. That type, which includes M57 in Lyra, actually forms when a dying Sun-like star puffs off its outer layers.",
            "r": "For 10 points, name these clouds of gas and dust, whose planetary type has nothing to do with planets."
        },
        {
            "p": "Williamina Fleming spotted the dark shape later nicknamed the Horsehead on a photographic plate at Harvard in 1888. Cataloged as Barnard 33, that dark cloud of dust stands out against glowing red gas near the belt of Orion.",
            "r": "For 10 points, name these clouds of gas and dust, which come in emission, reflection, and dark types."
        },
        {
            "p": "J. L. E. Dreyer’s New General Catalogue of 1888 listed nearly 8,000 of these objects and star clusters. Until the 1920s, the word for these objects also covered the fuzzy spirals that Edwin Hubble showed were separate galaxies.",
            "r": "For 10 points, name these clouds of gas and dust in space, whose name is Latin for “mist.”"
        },
        {
            "p": "The Pleiades star cluster is wrapped in a blue haze of dust that scatters its stars’ light, one example of these objects. Other examples glow pinkish red as ultraviolet light from hot young stars makes their hydrogen shine.",
            "r": "Those are the reflection and emission kinds. For 10 points, name these clouds of gas and dust between the stars."
        },
        {
            "p": "Edward Emerson Barnard photographed and cataloged hundreds of dark patches along the Milky Way, which turned out to be dense clouds blocking the light of stars behind them. The Coalsack, near the Southern Cross, is another dark example of these objects.",
            "r": "For 10 points, name these clouds of gas and dust, which also come in glowing emission types."
        },
        {
            "p": "Charles Messier [“MESS-ee-ay”] listed more than 100 fuzzy patches so that he would not mistake them for comets. Many of his entries, including M8, M16, M20, M42, and M57, are these objects, and his very first entry, M1, is the wreck of a star seen exploding in 1054.",
            "r": "For 10 points, name these clouds of gas and dust, such as the one in Orion’s sword."
        },
        {
            "p": "Dark lanes of dust split M20 in Sagittarius into three lobes, giving it the name Trifid, and it mixes glowing red, reflecting blue, and dark parts in a single object. Nearby lies M8, the Lagoon, another of these objects that can be seen with binoculars.",
            "r": "For 10 points, name these interstellar clouds of gas and dust, which come in emission, reflection, and dark types."
        },
        {
            "p": "Two of the James Webb Space Telescope’s first images, released in July 2022, showed these objects: the “Cosmic Cliffs” in Carina and a glowing shell of gas, called the Southern Ring, around a dying star.",
            "r": "For 10 points, name these clouds of gas and dust in space, whose name comes from the Latin for “mist” or “cloud.”"
        },
        {
            "p": "In 1880, Henry Draper, a New York doctor and amateur astronomer, took the first photograph ever made of one of these objects. The cloud he photographed is lit by four bright young stars called the Trapezium.",
            "r": "That cloud, M42, is the fuzzy middle “star” of Orion’s sword. For 10 points, name these glowing clouds of gas and dust."
        },
        {
            "p": "The Pillars of Creation are towering columns of cold gas and dust inside M16, the Eagle, one of these objects in the constellation Serpens. Hubble photographed the pillars in 1995, and Webb photographed them again in 2022.",
            "r": "For 10 points, name these clouds of gas and dust where new stars are born."
        },
        {
            "p": "The Veil, a set of delicate glowing filaments in Cygnus, and the first object in Charles Messier’s catalog, in Taurus, both formed from stars that exploded as supernovae, so both count as these objects.",
            "r": "For 10 points, name these clouds of gas and dust, which also come in planetary, emission, reflection, and dark types."
        },
        {
            "p": "The Tarantula, in the Large Magellanic Cloud, is the largest and brightest star-forming one of these objects in the Local Group of galaxies. In our own galaxy, a huge one in Carina surrounds Eta Carinae, a giant star that brightened dramatically in the 1840s.",
            "r": "For 10 points, name these clouds of gas and dust in space, some of which are stellar nurseries."
        },
        {
            "p": "In the 1700s, Immanuel Kant and later Pierre-Simon Laplace [“lah-PLAHSS”] proposed that the Sun and planets formed from a slowly spinning, flattening one of these objects. Modern ideas about how the solar system formed still build on their hypothesis.",
            "r": "Many of these objects are called stellar nurseries. For 10 points, name these clouds of gas and dust."
        }
    ],
    "clues": [
        {
            "id": "clouds",
            "tier": "giveaway",
            "t": "Clouds of gas (mostly hydrogen and helium) and dust in the space between stars",
            "k": ["clouds of gas", "dust", "hydrogen"],
            "n": 0
        },
        {
            "id": "latin-mist",
            "tier": "giveaway",
            "t": "Their name is Latin for “mist” or “cloud”",
            "k": ["latin", "mist"],
            "n": 0
        },
        {
            "id": "orion-m42",
            "tier": "giveaway",
            "t": "M42, the fuzzy middle “star” of Orion’s sword, is a famous one you can see without a telescope",
            "k": ["m42", "orion", "sword"],
            "n": 0,
            "rabbit": "Orion"
        },
        {
            "id": "nurseries",
            "tier": "giveaway",
            "t": "Stars are born inside many of them, so they are called stellar nurseries; dying stars also make them",
            "k": ["stellar nurseries", "dying stars"],
            "n": 0,
            "rabbit": "Star formation"
        },
        {
            "id": "types",
            "tier": "giveaway",
            "t": "Main types: emission (glowing red), reflection (blue), dark, and planetary",
            "k": ["emission", "reflection", "planetary"],
            "n": 0
        },
        {
            "id": "planetary-type",
            "tier": "middle",
            "t": "The planetary type is a shell of gas puffed off by a dying Sun-like star, like the Ring (M57) in Lyra; it has nothing to do with planets",
            "k": ["planetary type", "m57", "lyra"],
            "n": 0,
            "rabbit": "White dwarfs"
        },
        {
            "id": "herschel-planetary",
            "tier": "middle",
            "t": "William Herschel named the planetary type because their round disks looked like planets such as Uranus",
            "k": ["herschel", "uranus"],
            "n": 0
        },
        {
            "id": "emission-red",
            "tier": "middle",
            "t": "Emission types glow pinkish red because ultraviolet light from hot young stars makes their hydrogen shine",
            "k": ["pinkish red", "ultraviolet"],
            "n": 0,
            "rabbit": "Hydrogen"
        },
        {
            "id": "reflection-blue",
            "tier": "middle",
            "t": "Reflection types look blue because dust scatters starlight, as around the Pleiades",
            "k": ["scatters", "pleiades", "blue"],
            "n": 0
        },
        {
            "id": "horsehead",
            "tier": "middle",
            "t": "The dark Horsehead stands out against glowing red gas near Orion’s belt",
            "k": ["horsehead", "belt"],
            "n": 0
        },
        {
            "id": "messier",
            "tier": "middle",
            "t": "Charles Messier listed many of them among the fuzzy objects that he did not want to confuse with comets",
            "k": ["messier", "comets"],
            "n": 0,
            "rabbit": "Comets"
        },
        {
            "id": "pillars",
            "tier": "middle",
            "t": "The Pillars of Creation are in M16, the Eagle, photographed by Hubble (1995) and Webb (2022)",
            "k": ["pillars of creation", "eagle", "m16"],
            "n": 0
        },
        {
            "id": "galaxies-old-name",
            "tier": "middle",
            "t": "Their name was once used for galaxies too, like the spiral in Andromeda, until Edwin Hubble’s work in the 1920s",
            "k": ["galaxies", "andromeda", "edwin hubble"],
            "n": 0,
            "rabbit": "Galaxies"
        },
        {
            "id": "remnants",
            "tier": "middle",
            "t": "Exploded stars leave glowing remnants, like M1 in Taurus (from 1054) and the Veil in Cygnus",
            "k": ["remnants", "veil", "cygnus"],
            "n": 0,
            "rabbit": "Crab Nebula"
        },
        {
            "id": "draper",
            "tier": "middle",
            "t": "Henry Draper took the first photograph of one, M42, in 1880",
            "k": ["draper", "1880", "photograph"],
            "n": 0
        },
        {
            "id": "huggins",
            "tier": "power",
            "t": "William Huggins’s 1864 spectrum of the Cat’s Eye showed a few bright lines, proving that it was glowing gas, not stars",
            "k": ["huggins", "1864", "spectrum"],
            "n": 0
        },
        {
            "id": "nebulium",
            "tier": "power",
            "t": "A green line once blamed on a new element, “nebulium,” was traced by Ira Bowen in 1927 to oxygen missing two electrons",
            "k": ["nebulium", "ira bowen", "oxygen"],
            "n": 0
        },
        {
            "id": "forbidden",
            "tier": "power",
            "t": "Bowen’s “forbidden lines” can form only in extremely thin gas",
            "k": ["forbidden lines", "thin gas"],
            "n": 0
        },
        {
            "id": "fleming",
            "tier": "power",
            "t": "Williamina Fleming discovered the Horsehead on a Harvard photographic plate in 1888",
            "k": ["williamina fleming", "1888"],
            "n": 0
        },
        {
            "id": "barnard",
            "tier": "power",
            "t": "E. E. Barnard cataloged hundreds of dark ones; the Horsehead is Barnard 33",
            "k": ["barnard 33", "barnard"],
            "n": 0
        },
        {
            "id": "coalsack",
            "tier": "power",
            "t": "The Coalsack, near the Southern Cross, is a dark one",
            "k": ["coalsack", "southern cross"],
            "n": 0
        },
        {
            "id": "dreyer",
            "tier": "power",
            "t": "J. L. E. Dreyer’s New General Catalogue (1888) listed thousands of them along with star clusters",
            "k": ["dreyer", "new general catalogue"],
            "n": 0
        },
        {
            "id": "trifid",
            "tier": "power",
            "t": "M20, the Trifid in Sagittarius, mixes emission, reflection, and dark parts and is split into three lobes by dust lanes",
            "k": ["trifid", "m20", "three lobes"],
            "n": 0
        },
        {
            "id": "lagoon",
            "tier": "power",
            "t": "M8, the Lagoon in Sagittarius, can be seen with binoculars",
            "k": ["lagoon", "binoculars"],
            "n": 0
        },
        {
            "id": "webb-2022",
            "tier": "power",
            "t": "Webb’s first images (July 2022) included the “Cosmic Cliffs” in Carina and the Southern Ring",
            "k": ["cosmic cliffs", "southern ring"],
            "n": 0
        },
        {
            "id": "tarantula",
            "tier": "power",
            "t": "The Tarantula in the Large Magellanic Cloud is the largest and brightest star-forming one in the Local Group",
            "k": ["tarantula", "large magellanic cloud"],
            "n": 0
        },
        {
            "id": "eta-carinae",
            "tier": "power",
            "t": "The giant one in Carina surrounds Eta Carinae, a star that brightened dramatically in the 1840s",
            "k": ["eta carinae", "1840s"],
            "n": 0
        },
        {
            "id": "kant-laplace",
            "tier": "power",
            "t": "Immanuel Kant and Pierre-Simon Laplace proposed that the solar system formed from a spinning, flattening one",
            "k": ["kant", "laplace"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Clouds or galaxies?",
        "body": "For centuries, “nebula” meant any fuzzy patch seen through a telescope, so Messier’s list mixes true gas clouds with star clusters and galaxies, and the Andromeda Galaxy was long called the Andromeda “Nebula.” Players also answer with one famous example, like the Orion or Crab Nebula, when the question asks for “these objects.”",
        "fix": "“These clouds of gas and dust,” with emission, reflection, dark, or planetary types, means nebulae. Hubble, Cepheids, redshifts, or spiral arms of stars mean galaxies; a tight group of stars is a star cluster. If every clue describes one object with its own Messier number, name that object.",
        "line": "Real answer line: <b><u>nebula</u></b>e (accept <u>nebula</u>; accept specific types such as <u>planetary nebula</u>e)"
    },
    "tests": {
        "right": [
            "Nebulae",
            "nebula",
            "Nebulas",
            "Nebulea",
            "planetary nebulae",
            "emission nebula"
        ],
        "prompt": [
            "interstellar clouds",
            "molecular clouds"
        ],
        "wrong": [
            "Galaxies",
            "Crab Nebula",
            "Star clusters",
            "Orion Nebula",
            "Spiral nebulae",
            "Comets",
            "Oort cloud"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
