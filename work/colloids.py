import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "colloids",
    "name": "Colloids",
    "mono": "CLD",
    "category": "Chemistry",
    "qbCategory": "Science · Chemistry",
    "kicker": "Tiny particles spread through another substance · Milk, fog, and gelatin",
    "dates": "Named by Thomas Graham, 1861",
    "briefing": "A colloid is a mixture whose particles are much bigger than most molecules but still too small to see or to settle out, so they stay spread through another substance. Milk, fog, whipped cream, and gelatin are all colloids. Shine a flashlight through one and the beam lights up, because the particles scatter light, a trick called the Tyndall effect. Scottish chemist Thomas Graham named them in 1861 from the Greek word for “glue.”",
    "answerHtml": "<b><u>Colloids</u></b> (accept <u>colloid</u>al dispersions or <u>colloid</u>al suspensions; prompt on heterogeneous <u>mixture</u>s or <u>dispersion</u>s; do not accept “suspension” or “solution” alone)",
    "accept": [
        "colloids",
        "colloid",
        "colloidal",
        "colloidal dispersion",
        "colloidal dispersions",
        "colloidal suspension",
        "colloidal suspensions",
        "colloidal solution",
        "colloidal solutions",
        "colloidal system",
        "colloidal systems",
        "colloidal mixture",
        "colloidal mixtures"
    ],
    "prompt": [
        "dispersion",
        "dispersions",
        "heterogeneous mixture",
        "heterogeneous mixtures",
        "mixture",
        "mixtures"
    ],
    "reject": [
        "homogeneous mixture",
        "homogeneous mixtures",
        "homogenous mixture",
        "emulsion",
        "emulsions",
        "emulsifier",
        "aerosol",
        "aerosols",
        "foam",
        "foams",
        "gel",
        "gels",
        "sol",
        "sols",
        "crystalloid",
        "crystalloids",
        "tyndall effect",
        "brownian motion",
        "micelle",
        "micelles",
        "alloy",
        "alloys",
        "compound",
        "compounds"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Colloid",
    "qb": {
        "q": "colloid",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "Richard Zsigmondy [“ZHIG-mon-dee”] won the 1925 Nobel Prize in Chemistry for studying these mixtures, using an ultramicroscope he helped invent to see light scattered by their particles. That instrument let scientists count particles far too small for an ordinary microscope.",
            "r": "For 10 points, name these mixtures, such as milk, fog, and gelatin, whose particles are too small to settle out but large enough to scatter light."
        },
        {
            "p": "The Svedberg won the 1926 Nobel Prize in Chemistry for studying these mixtures, inventing the ultracentrifuge to make their tiny particles settle. Jean Perrin [“zhahn peh-RAN”] won the Physics Nobel the same year, partly for experiments on how particles in these mixtures settle and jiggle.",
            "r": "That jiggling is called Brownian motion. For 10 points, name these mixtures, like milk and fog, whose particles stay spread out instead of settling."
        },
        {
            "p": "Thomas Graham, who also has a law about how fast gases effuse, named these mixtures in 1861 from the Greek word for “glue.” Graham used membranes to separate them from dissolved salts, a process called dialysis that he pioneered.",
            "r": "For 10 points, name these mixtures, such as mayonnaise and whipped cream, which fall between solutions and suspensions in particle size."
        },
        {
            "p": "DLVO theory explains how stable these mixtures are by weighing van der Waals attraction between their particles against repulsion from the charged layers around them. Adding salt can make their particles clump together, a process called flocculation or coagulation.",
            "r": "For 10 points, name these mixtures, like fog and gelatin, whose particles scatter a beam of light in the Tyndall effect."
        },
        {
            "p": "The Roman Lycurgus [“lye-KUR-gus”] Cup looks green in reflected light and red when lit from behind, because its glass is one of these mixtures, holding tiny particles of gold and silver. In 1857, Michael Faraday made a ruby-red example containing tiny gold particles.",
            "r": "For 10 points, name these mixtures whose particles are too small to settle out, such as milk and fog."
        },
        {
            "p": "The Schulze–Hardy rule says that ions with a higher charge, opposite to that of the particles, are far better at making these mixtures clump together. River deltas form partly because fine clay particles spread through river water clump together when they meet salty seawater.",
            "r": "For 10 points, name these mixtures whose particles, between about 1 and 1,000 nanometers across, scatter light in the Tyndall effect."
        },
        {
            "p": "The zeta potential measures the electric potential near the surface of the particles in these mixtures, and a large value keeps the particles from sticking together. Because those particles carry charge, they drift toward an electrode in an electric field, a process called electrophoresis.",
            "r": "For 10 points, name these mixtures, which include emulsions, foams, and gels, whose particles never settle out."
        },
        {
            "p": "Chemists sort these mixtures into lyophilic [“lye-oh-FIL-ik”] types, whose particles attract the liquid around them, and lyophobic types, whose particles do not. In water treatment, alum is added to make these mixtures of dirt particles clump and sink.",
            "r": "For 10 points, name these mixtures, like milk, whose particles stay spread out instead of settling and make a flashlight beam visible."
        },
        {
            "p": "Above a certain concentration, soap molecules gather into balls called micelles [“my-SELLZ”], forming “association” types of these mixtures. Egg yolk helps make mayonnaise one of these mixtures by keeping drops of oil spread through a watery liquid.",
            "r": "For 10 points, name these mixtures, whose types include emulsions and aerosols, that scatter light in the Tyndall effect."
        },
        {
            "p": "Some of these mixtures are thixotropic [“thik-suh-TROP-ik”], becoming runnier when they are shaken or stirred and thickening again at rest. In a gel, one type of these mixtures, a liquid is trapped inside a network of solid particles or strands.",
            "r": "For 10 points, name these mixtures, including gelatin, whose particles are larger than those in solutions but smaller than those in suspensions."
        },
        {
            "p": "No gas-in-gas type of these mixtures exists, because gases always mix evenly into a solution. Smoke is one of these mixtures with solid particles spread through a gas, while fog spreads liquid droplets through a gas, and both are called aerosols.",
            "r": "For 10 points, name these mixtures, like milk and whipped cream, whose particles do not settle out over time."
        },
        {
            "p": "The random jiggling of particles in these mixtures is named for botanist Robert Brown, who watched tiny bits from pollen grains doing it in water in 1827. Albert Einstein explained that jiggling in 1905 as the result of collisions with moving molecules.",
            "r": "For 10 points, name these mixtures, such as fog and milk, that scatter light in the Tyndall effect."
        },
        {
            "p": "NASA’s Stardust spacecraft caught comet dust in aerogel, a super-light solid made by drying one type of these mixtures. Marshmallows, pumice, and plastic foam cups are “solid foam” examples of these mixtures, with gas bubbles trapped in a solid.",
            "r": "For 10 points, name these mixtures, which also include emulsions like milk and mayonnaise."
        },
        {
            "p": "Unlike the particles in a suspension, the particles in these mixtures pass through ordinary filter paper, but much finer membranes can trap them. Milk is one of these mixtures called an emulsion, and homogenizing it breaks its butterfat into smaller droplets so the cream does not rise.",
            "r": "For 10 points, name these mixtures, like fog and gelatin, that fall between solutions and suspensions in particle size."
        },
        {
            "p": "Each of these mixtures has a dispersed phase spread through a continuous phase called the dispersion medium. Many paints and inks are sols, the type of these mixtures with solid particles in a liquid, while gelatin and jelly are gels.",
            "r": "For 10 points, name these mixtures, like milk and fog, that scatter a beam of light in the Tyndall effect."
        }
    ],
    "clues": [
        {
            "id": "definition",
            "tier": "giveaway",
            "t": "A mixture with tiny particles spread through another substance that never settle out",
            "k": ["mixture", "settle out", "tiny particles"],
            "n": 0
        },
        {
            "id": "examples",
            "tier": "giveaway",
            "t": "Examples include milk, fog, whipped cream, mayonnaise, and gelatin",
            "k": ["milk", "fog", "whipped cream", "gelatin"],
            "n": 0
        },
        {
            "id": "tyndall",
            "tier": "giveaway",
            "t": "Their particles scatter a beam of light, like headlights in fog: the Tyndall effect",
            "k": ["tyndall effect", "tyndall", "scatter"],
            "n": 0
        },
        {
            "id": "in-between",
            "tier": "giveaway",
            "t": "Their particles are bigger than those in a solution but smaller than those in a suspension",
            "k": ["solution", "suspension"],
            "n": 0
        },
        {
            "id": "size",
            "tier": "middle",
            "t": "Particles are about 1 to 1,000 nanometers across",
            "k": ["nanometers", "1,000"],
            "n": 0
        },
        {
            "id": "phases",
            "tier": "middle",
            "t": "Made of a dispersed phase spread through a continuous phase called the dispersion medium",
            "k": ["dispersed phase", "dispersion medium"],
            "n": 0
        },
        {
            "id": "emulsions",
            "tier": "middle",
            "t": "Emulsions are liquid in liquid, like milk and mayonnaise, where egg yolk keeps oil drops spread through water",
            "k": ["emulsions", "mayonnaise", "egg yolk"],
            "n": 0
        },
        {
            "id": "foams",
            "tier": "middle",
            "t": "Foams are gas in liquid (whipped cream, shaving cream); solid foams are gas in solid (marshmallows, pumice)",
            "k": ["foams", "solid foams", "marshmallows", "pumice"],
            "n": 0
        },
        {
            "id": "aerosols",
            "tier": "middle",
            "t": "Aerosols are liquid or solid particles in a gas: fog and clouds (liquid) and smoke (solid)",
            "k": ["aerosols", "smoke", "clouds"],
            "n": 0,
            "rabbit": "Clouds"
        },
        {
            "id": "gels-sols",
            "tier": "middle",
            "t": "Gels trap a liquid in a solid network (gelatin, jelly); sols have solid particles in a liquid (many paints and inks)",
            "k": ["gels", "sols", "jelly", "paints"],
            "n": 0
        },
        {
            "id": "no-gas-gas",
            "tier": "middle",
            "t": "No gas-in-gas type exists, because gases always mix evenly into a solution",
            "k": ["gas-in-gas", "mix evenly"],
            "n": 0
        },
        {
            "id": "brownian",
            "tier": "middle",
            "t": "Their particles jiggle randomly in Brownian motion, first seen by Robert Brown in 1827",
            "k": ["brownian motion", "robert brown", "1827"],
            "n": 0,
            "rabbit": "Brownian motion"
        },
        {
            "id": "graham",
            "tier": "middle",
            "t": "Named in 1861 by Thomas Graham, from the Greek word for “glue”",
            "k": ["thomas graham", "1861", "glue"],
            "n": 0
        },
        {
            "id": "filter-paper",
            "tier": "middle",
            "t": "Their particles pass through ordinary filter paper but can be trapped by much finer membranes",
            "k": ["filter paper", "membranes"],
            "n": 0
        },
        {
            "id": "dialysis",
            "tier": "power",
            "t": "Thomas Graham, of Graham’s law of effusion, pioneered dialysis, using membranes to separate them from dissolved salts",
            "k": ["dialysis", "graham’s law", "effusion"],
            "n": 0
        },
        {
            "id": "zsigmondy",
            "tier": "power",
            "t": "Richard Zsigmondy helped invent the ultramicroscope and won the 1925 Nobel Prize in Chemistry for studying them",
            "k": ["zsigmondy", "ultramicroscope", "1925"],
            "n": 0
        },
        {
            "id": "svedberg-perrin",
            "tier": "power",
            "t": "1926: The Svedberg (Chemistry Nobel; invented the ultracentrifuge) and Jean Perrin (Physics Nobel) were honored for studying them",
            "k": ["svedberg", "ultracentrifuge", "perrin", "1926"],
            "n": 0
        },
        {
            "id": "einstein",
            "tier": "power",
            "t": "Albert Einstein explained Brownian motion in 1905 as the result of collisions with moving molecules",
            "k": ["einstein", "1905", "collisions"],
            "n": 0,
            "rabbit": "Albert Einstein"
        },
        {
            "id": "dlvo",
            "tier": "power",
            "t": "DLVO theory weighs van der Waals attraction against electric repulsion to explain how stable they are",
            "k": ["dlvo", "van der waals", "repulsion"],
            "n": 0,
            "rabbit": "Van der Waals forces"
        },
        {
            "id": "flocculation",
            "tier": "power",
            "t": "Adding salt can make the particles clump together, called coagulation or flocculation",
            "k": ["coagulation", "flocculation", "clump"],
            "n": 0
        },
        {
            "id": "schulze-hardy",
            "tier": "power",
            "t": "Schulze–Hardy rule: oppositely charged ions with higher charges clump the particles far more effectively",
            "k": ["schulze–hardy", "higher charges"],
            "n": 0
        },
        {
            "id": "alum-deltas",
            "tier": "power",
            "t": "Alum clumps dirt particles in water treatment; river clay clumping in salty seawater helps form deltas",
            "k": ["alum", "deltas", "seawater"],
            "n": 0
        },
        {
            "id": "zeta-electrophoresis",
            "tier": "power",
            "t": "Zeta potential measures the electric potential near their charged particles, which drift toward an electrode in electrophoresis",
            "k": ["zeta potential", "electrophoresis", "electrode"],
            "n": 0
        },
        {
            "id": "lyophilic",
            "tier": "power",
            "t": "Lyophilic types have particles that attract the surrounding liquid; lyophobic types do not",
            "k": ["lyophilic", "lyophobic"],
            "n": 0
        },
        {
            "id": "micelles",
            "tier": "power",
            "t": "Above a certain concentration, soap molecules form micelles, making “association” types",
            "k": ["micelles", "soap", "association"],
            "n": 0
        },
        {
            "id": "thixotropic",
            "tier": "power",
            "t": "Thixotropic ones get runnier when shaken or stirred and thicken again at rest",
            "k": ["thixotropic", "shaken"],
            "n": 0
        },
        {
            "id": "gold-glass",
            "tier": "power",
            "t": "Gold and silver particles make the Roman Lycurgus Cup look green or red; Michael Faraday made a ruby-red gold sample in 1857",
            "k": ["lycurgus cup", "lycurgus", "faraday", "ruby-red"],
            "n": 0,
            "rabbit": "Michael Faraday"
        },
        {
            "id": "aerogel",
            "tier": "power",
            "t": "NASA’s Stardust probe caught comet dust in aerogel, a super-light solid made by drying a gel",
            "k": ["aerogel", "stardust"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Not solution or suspension",
        "body": "These mixtures are defined by particle size, so tossups about them often describe solutions and suspensions too. In a solution, like salt water, the particles are single molecules or ions and a light beam passes through unseen; in a suspension, like muddy water, the particles are big enough to settle out or be filtered. Players also blurt one type, like “emulsion” or “aerosol,” when the question wants the whole family.",
        "fix": "Settles out or filters out means suspension; perfectly clear with no visible beam means solution; scatters a beam (the Tyndall effect) but never settles means this answer. Listen for “these mixtures” and give the general name unless the question clearly asks for one type.",
        "line": "Real answer line: <b><u>Colloids</u></b> (accept <u>colloid</u>al dispersions or <u>colloid</u>al suspensions; prompt on heterogeneous <u>mixture</u>s or <u>dispersion</u>s; do not accept “suspension” or “solution” alone)"
    },
    "tests": {
        "right": [
            "Colloids",
            "colloid",
            "Coloids",
            "colloidal suspension",
            "Colloidal dispersion",
            "colloidal solution"
        ],
        "prompt": [
            "Dispersion",
            "Heterogeneous mixture"
        ],
        "wrong": [
            "Suspension",
            "Solution",
            "Emulsion",
            "Aerosol",
            "Tyndall effect",
            "Homogeneous mixture",
            "Crystalloid"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
