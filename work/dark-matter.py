import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "dark-matter",
    "name": "Dark matter",
    "mono": "DM",
    "category": "Astronomy",
    "qbCategory": "Science · Other Science (Astronomy)",
    "kicker": "Invisible mass that holds galaxies together · Detected only by its gravity",
    "dates": "Proposed by Fritz Zwicky, 1933",
    "briefing": "Most of the matter in the universe is invisible dark matter: it gives off no light, yet its gravity holds galaxies and galaxy clusters together. In 1933 Fritz Zwicky noticed that galaxies in the Coma Cluster moved too fast to be held by their stars alone, and in the 1970s Vera Rubin showed that stars at the edges of galaxies orbit surprisingly fast. What it is actually made of remains one of science’s biggest mysteries.",
    "answerHtml": "<b><u>Dark matter</u></b> (accept <u>cold dark matter</u>; do not accept “dark energy”)",
    "accept": [
        "dark matter",
        "cold dark matter"
    ],
    "prompt": [],
    "reject": [
        "dark energy",
        "antimatter",
        "anti matter",
        "black hole",
        "black holes",
        "baryonic matter",
        "ordinary matter",
        "normal matter",
        "wimp",
        "wimps",
        "macho",
        "machos",
        "axion",
        "axions",
        "neutrino",
        "neutrinos",
        "mond",
        "modified newtonian dynamics",
        "gravitational lensing",
        "cosmological constant",
        "quintessence",
        "dark flow"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Dark_matter",
    "qb": {
        "q": "dark matter",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "In 1933, Fritz Zwicky [“TSVIK-ee”] applied the virial theorem to the Coma Cluster and found that its galaxies were moving far too fast to be held together by the gravity of their visible stars alone. He concluded that the cluster must contain huge amounts of unseen mass.",
            "r": "For 10 points, name this invisible substance that makes up most of the matter in the universe and is detected only by its gravity."
        },
        {
            "p": "Vera Rubin and Kent Ford measured how fast stars and gas clouds orbit in the Andromeda Galaxy and found that those far from its center move about as fast as those near it. Those flat rotation curves suggested that galaxies are wrapped in halos of unseen mass.",
            "r": "For 10 points, name this invisible form of matter that gives off no light but has gravity."
        },
        {
            "p": "When two galaxy clusters smashed together to form the Bullet Cluster, X-ray telescopes showed their hot gas piling up in the middle, but gravitational lensing showed that most of their mass had passed right through. That 2006 result was hailed as direct evidence for this substance.",
            "r": "For 10 points, name this mysterious, invisible matter that neither gives off nor absorbs light but still has gravity."
        },
        {
            "p": "Frank Wilczek [“WIL-chek”] named a hypothetical particle after a brand of laundry detergent, and that particle, the axion, is one proposed explanation for this substance. Another candidate is a class of weakly interacting massive particles, or WIMPs.",
            "r": "For 10 points, name this invisible matter that holds galaxies together with its gravity."
        },
        {
            "p": "Mordehai Milgrom’s theory called MOND, short for Modified Newtonian Dynamics, tries to explain why galaxies spin so fast without needing this substance, by changing the law of gravity instead. Most astronomers favor this substance as the explanation.",
            "r": "For 10 points, name this invisible matter, first proposed by Fritz Zwicky after he studied the Coma Cluster."
        },
        {
            "p": "Deep in a former gold mine in South Dakota, the LUX-ZEPLIN experiment uses tons of liquid xenon to try to catch a rare collision between an atom and a particle of this substance. Such underground experiments are shielded from cosmic rays by thousands of feet of rock.",
            "r": "For 10 points, name this unseen substance that makes up most of the matter in the universe."
        },
        {
            "p": "Surveys that watched for stars briefly brightening by gravitational lensing tested whether this substance is made of MACHOs, or massive compact halo objects, such as brown dwarfs. Those surveys found too few MACHOs to explain most of it.",
            "r": "For 10 points, name this invisible material whose gravity holds galaxies and galaxy clusters together."
        },
        {
            "p": "Some supersymmetry theories predict a stable particle called the neutralino, which could make up this substance. Because this substance is thought to be mostly “cold,” or slow-moving, the standard model of cosmology is called Lambda-CDM.",
            "r": "For 10 points, name this mysterious, invisible substance that makes up about 85 percent of the matter in the universe."
        },
        {
            "p": "Tiny ripples in the cosmic microwave background measured by the WMAP and Planck spacecraft revealed that this substance outweighs ordinary matter by about five to one. Its gravity helped pull ordinary gas together into the first galaxies.",
            "r": "For 10 points, name this invisible matter, whose existence was first suggested by Fritz Zwicky."
        },
        {
            "p": "Neutrinos were once proposed as a “hot,” fast-moving form of this substance, but they are too light and too fast to explain how galaxies formed. This substance does not interact with light at all, so no telescope can see it directly.",
            "r": "For 10 points, name this substance, detected only through its gravity, that Vera Rubin found evidence for in spinning galaxies."
        },
        {
            "p": "In 2023, Europe launched the Euclid space telescope to map where this substance lies across billions of light-years, by measuring how its gravity slightly warps the shapes of distant galaxies. Astronomers think most galaxies sit inside a huge halo of it.",
            "r": "For 10 points, name this invisible matter that gives off no light but makes up most of the mass of galaxies."
        },
        {
            "p": "A large observatory in Chile is named for the astronomer whose studies of spinning galaxies provided key evidence for this substance. That astronomer, Vera Rubin, found that stars at the outer edges of spiral galaxies orbit surprisingly fast.",
            "r": "For 10 points, name this invisible form of matter, which makes up most of the matter in the universe."
        },
        {
            "p": "Some scientists have suggested that this substance could be made of primordial black holes formed in the first moments after the Big Bang, while others have searched for its particles in collisions at the Large Hadron Collider.",
            "r": "For 10 points, name this invisible matter, which, unlike ordinary matter, gives off no light."
        },
        {
            "p": "The Milky Way’s visible disk of stars sits inside a much larger, roughly round cloud, or halo, made mostly of this substance. This substance can be mapped by gravitational lensing, because its gravity bends light from more distant galaxies.",
            "r": "For 10 points, name this mysterious, invisible substance that gives off no light."
        },
        {
            "p": "Astronomers estimate that about 5 percent of the universe’s mass and energy is ordinary matter, about 68 percent is a mysterious energy that speeds up its expansion, and about 27 percent is this substance.",
            "r": "Its gravity holds galaxies and galaxy clusters together. For 10 points, name this invisible substance that gives off no light."
        }
    ],
    "clues": [
        {
            "id": "invisible-gravity",
            "tier": "giveaway",
            "t": "Invisible matter that gives off no light; it is detected only through its gravity",
            "k": ["invisible", "no light", "gravity"],
            "n": 0
        },
        {
            "id": "most-of-matter",
            "tier": "giveaway",
            "t": "Makes up most of the matter in the universe, about 85 percent",
            "k": ["most of the matter", "85 percent"],
            "n": 0
        },
        {
            "id": "zwicky",
            "tier": "giveaway",
            "t": "Fritz Zwicky proposed it in 1933 after galaxies in the Coma Cluster moved too fast",
            "k": ["zwicky", "coma cluster", "1933"],
            "n": 0
        },
        {
            "id": "vera-rubin",
            "tier": "giveaway",
            "t": "In the 1970s, Vera Rubin and Kent Ford found that stars far from galaxies’ centers orbit surprisingly fast",
            "k": ["vera rubin", "kent ford", "rubin"],
            "n": 0,
            "rabbit": "Vera Rubin"
        },
        {
            "id": "holds-galaxies",
            "tier": "giveaway",
            "t": "Its extra gravity holds galaxies and galaxy clusters together",
            "k": ["galaxy clusters", "extra gravity"],
            "n": 0
        },
        {
            "id": "rotation-curves",
            "tier": "middle",
            "t": "Galaxies’ “flat rotation curves” (outer stars orbiting about as fast as inner ones) are a key sign of it",
            "k": ["flat rotation curves", "rotation curves"],
            "n": 0
        },
        {
            "id": "halo",
            "tier": "middle",
            "t": "Most galaxies, including the Milky Way, sit inside a huge, roughly round halo of it",
            "k": ["halo", "milky way"],
            "n": 0
        },
        {
            "id": "lensing",
            "tier": "middle",
            "t": "Astronomers map it with gravitational lensing, since its gravity bends light from more distant galaxies",
            "k": ["gravitational lensing", "bends light"],
            "n": 0,
            "rabbit": "Gravitational lensing"
        },
        {
            "id": "bullet-cluster",
            "tier": "middle",
            "t": "In the Bullet Cluster (2006), lensing showed that most of two colliding clusters’ mass had moved apart from their X-ray-glowing hot gas",
            "k": ["bullet cluster", "colliding", "hot gas"],
            "n": 0
        },
        {
            "id": "wimps",
            "tier": "middle",
            "t": "A leading candidate: WIMPs, or weakly interacting massive particles",
            "k": ["wimps", "weakly interacting"],
            "n": 0
        },
        {
            "id": "machos",
            "tier": "middle",
            "t": "MACHOs (massive compact halo objects) such as brown dwarfs were tested, but there are too few of them to explain it",
            "k": ["machos", "compact halo", "brown dwarfs"],
            "n": 0
        },
        {
            "id": "cold",
            "tier": "middle",
            "t": "The standard Lambda-CDM model of cosmology says most of it is “cold,” or slow-moving",
            "k": ["lambda-cdm", "cold", "slow-moving"],
            "n": 0
        },
        {
            "id": "euclid",
            "tier": "middle",
            "t": "Europe’s Euclid space telescope (launched 2023) maps it by how its gravity warps the shapes of distant galaxies",
            "k": ["euclid", "2023"],
            "n": 0,
            "rabbit": "Euclid"
        },
        {
            "id": "hot-neutrinos",
            "tier": "middle",
            "t": "Neutrinos are a “hot,” fast-moving form of it, but they are too light and fast to be most of it",
            "k": ["neutrinos", "hot"],
            "n": 0,
            "rabbit": "Neutrinos"
        },
        {
            "id": "virial",
            "tier": "power",
            "t": "Zwicky used the virial theorem, which links the motions inside a cluster to its total mass",
            "k": ["virial theorem", "virial"],
            "n": 0
        },
        {
            "id": "andromeda",
            "tier": "power",
            "t": "Rubin and Ford first measured the spin of the Andromeda Galaxy",
            "k": ["andromeda"],
            "n": 0,
            "rabbit": "Andromeda Galaxy"
        },
        {
            "id": "axions",
            "tier": "power",
            "t": "Another candidate, the axion, was named by Frank Wilczek after a laundry detergent",
            "k": ["axion", "wilczek", "laundry detergent"],
            "n": 0
        },
        {
            "id": "mond",
            "tier": "power",
            "t": "Mordehai Milgrom’s MOND (Modified Newtonian Dynamics) tries to explain fast-spinning galaxies by changing gravity instead",
            "k": ["mond", "milgrom", "modified newtonian dynamics"],
            "n": 0
        },
        {
            "id": "lux-zeplin",
            "tier": "power",
            "t": "Underground detectors filled with liquid xenon, like LUX-ZEPLIN in a former South Dakota gold mine, hunt for its particles",
            "k": ["xenon", "lux-zeplin", "south dakota"],
            "n": 0
        },
        {
            "id": "cmb",
            "tier": "power",
            "t": "The cosmic microwave background, measured by WMAP and Planck, shows it outweighs ordinary matter about five to one",
            "k": ["cosmic microwave background", "wmap", "planck", "five to one"],
            "n": 0,
            "rabbit": "Cosmic microwave background"
        },
        {
            "id": "neutralino",
            "tier": "power",
            "t": "Some supersymmetry theories predict a WIMP called the neutralino",
            "k": ["neutralino", "supersymmetry"],
            "n": 0
        },
        {
            "id": "rubin-observatory",
            "tier": "power",
            "t": "The Vera C. Rubin Observatory in Chile honors the astronomer whose spinning-galaxy studies supported it",
            "k": ["chile", "observatory"],
            "n": 0
        },
        {
            "id": "lhc",
            "tier": "power",
            "t": "Physicists have searched for its particles in collisions at the Large Hadron Collider",
            "k": ["large hadron collider", "collisions"],
            "n": 0
        },
        {
            "id": "primordial-black-holes",
            "tier": "power",
            "t": "Primordial black holes from the first moments after the Big Bang are another proposed candidate",
            "k": ["primordial black holes", "big bang"],
            "n": 0
        },
        {
            "id": "first-galaxies",
            "tier": "power",
            "t": "Its gravity helped pull gas together into the first galaxies",
            "k": ["first galaxies"],
            "n": 0
        },
        {
            "id": "cosmic-budget",
            "tier": "power",
            "t": "Of the universe’s mass and energy, about 5 percent is ordinary matter, about 68 percent is a mysterious energy that speeds up expansion, and about 27 percent is this",
            "k": ["27 percent", "68 percent"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Matter, not energy",
        "body": "Dark matter and dark energy sound alike but do opposite jobs: dark matter’s gravity pulls galaxies together, while dark energy speeds up the expansion of the whole universe. Answering “dark energy” is wrong. Antimatter is a third mix-up: it is made of particles like positrons, which physicists can make in laboratories.",
        "fix": "Zwicky, Vera Rubin, rotation curves, halos, lensing, the Bullet Cluster, WIMPs, and axions mean dark matter. Type Ia supernovae, the speeding-up of the universe’s expansion, and the cosmological constant mean dark energy.",
        "line": "Real answer line: <b><u>Dark matter</u></b> (accept <u>cold dark matter</u>; do not accept “dark energy”)"
    },
    "tests": {
        "right": [
            "Dark matter",
            "dark mater",
            "Cold dark matter",
            "darkmatter",
            "the dark matter"
        ],
        "prompt": [],
        "wrong": [
            "Dark energy",
            "Antimatter",
            "Black holes",
            "WIMPs",
            "Neutrinos",
            "MOND"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
