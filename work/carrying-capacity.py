import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "carrying-capacity",
    "name": "Carrying capacity",
    "mono": "KC",
    "category": "Biology",
    "qbCategory": "Science · Biology",
    "kicker": "Largest population an environment can support · Symbolized K",
    "dates": "Logistic equation first published 1838",
    "briefing": "Every habitat has limits: only so much food, water, and living space to go around. Carrying capacity, symbolized K, is the largest population of a species that an environment can support over time. When 29 reindeer were left on Alaska’s St. Matthew Island in 1944, they multiplied to about 6,000, ate most of the lichen, and then crashed, a famous example of a population overshooting its limit.",
    "answerHtml": "<b><u>Carrying capacity</u></b> (prompt on <u>K</u>; do not accept “logistic growth,” “limiting factors,” or “exponential growth”)",
    "accept": [
        "carrying capacity",
        "carrying capacities",
        "environmental carrying capacity",
        "ecological carrying capacity"
    ],
    "prompt": [
        "k",
        "k value",
        "maximum population",
        "maximum population size",
        "population limit"
    ],
    "reject": [
        "logistic growth",
        "logistic curve",
        "logistic equation",
        "logistic model",
        "limiting factor",
        "limiting factors",
        "exponential growth",
        "exponential curve",
        "population growth",
        "growth rate",
        "population density",
        "density dependent factors",
        "density dependence",
        "biotic potential",
        "environmental resistance",
        "intrinsic rate of increase",
        "overshoot",
        "zero population growth",
        "maximum sustainable yield",
        "k selection",
        "k selected",
        "r selection",
        "heat capacity",
        "vital capacity",
        "lung capacity",
        "ecological footprint"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Carrying_capacity",
    "qb": {
        "q": "carrying capacity",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "In 1944, the U.S. Coast Guard released 29 reindeer on Alaska’s St. Matthew Island, where the herd grew to about 6,000 by 1963 and ate most of the island’s lichen. Only 42 reindeer were left by 1966, a crash that biologist David Klein blamed on a harsh winter and on the herd overshooting this limit.",
            "r": "It is set by limiting factors like food and space. For 10 points, name this largest population an environment can support over time, symbolized K."
        },
        {
            "p": "Pierre-François Verhulst [“vair-HULST”] modeled human populations in 1838 with an equation in which growth slows down as a population approaches this value. Raymond Pearl and Lowell Reed revived that equation in 1920 by fitting it to United States census counts.",
            "r": "In that logistic equation, growth stops when the population N equals this value. For 10 points, name this largest population an environment can sustain, symbolized K."
        },
        {
            "p": "In their 1967 book _The Theory of Island Biogeography_, Robert MacArthur and E. O. Wilson named a kind of natural selection after this value’s symbol. Species shaped by that kind of selection, such as elephants and whales, have few young, care for them a long time, and keep their numbers near this value.",
            "r": "Species with many young that grow fast are instead called r-selected. For 10 points, name this largest population of a species that an environment can sustain, symbolized K."
        },
        {
            "p": "Liebig’s [“LEE-bigz”] law of the minimum, often pictured as a barrel that can hold water only up to its shortest board, says that the scarcest needed resource limits a population’s growth and sets this value. In a desert, water is often the resource that sets this value.",
            "r": "Food, water, and space are limiting factors that determine it. For 10 points, name this maximum population size, symbolized K, that an environment can support."
        },
        {
            "p": "In simple fishery models, the maximum sustainable yield comes from keeping a fish stock at about half of this value, because a population adds new members fastest at that size. That halfway point is the inflection point of a logistic growth curve.",
            "r": "It is reached when a population’s births and deaths balance. For 10 points, name this largest population an environment can support, symbolized K."
        },
        {
            "p": "Georgy Gause [“GOW-zuh”] grew single-celled _Paramecium_ in test tubes with a fixed daily food supply and found that their numbers rose quickly, then leveled off at this value. He described those experiments in his 1934 book _The Struggle for Existence_.",
            "r": "On a logistic growth graph, this value is drawn as a flat dashed line. For 10 points, name this maximum population an environment can sustain, symbolized K."
        },
        {
            "p": "Joel Cohen’s 1995 book _How Many People Can the Earth Support?_ found that published estimates of this value for humans on Earth vary enormously. Much earlier, in 1798, Thomas Malthus argued that a growing human population would tend to outrun its food supply.",
            "r": "It is set by limiting factors such as food and water. For 10 points, name this maximum population size, symbolized K, that an environment can sustain."
        },
        {
            "p": "Unlike density-independent events such as floods and wildfires, density-dependent factors such as competition, predation, and disease press harder on a population as it grows more crowded, slowing growth as it approaches this value. When births and deaths balance at this value, a population stops growing.",
            "r": "Elephants and other K-selected species keep their numbers near it. For 10 points, name this largest population an environment can support, symbolized K."
        },
        {
            "p": "Because warm water holds less dissolved oxygen, a lake’s value for trout can drop during hot summers. Ranchers and range managers use this term for the number of grazing animals a pasture can feed year after year without being damaged.",
            "r": "It changes whenever food, water, or shelter in a habitat changes. For 10 points, name this maximum population size, symbolized K."
        },
        {
            "p": "The gap between a population’s biotic potential, its growth with no limits, and its real growth is called environmental resistance, the combined effect of all the factors that hold a population at this value. Bacteria with unlimited food and space can instead show J-shaped exponential growth.",
            "r": "In real habitats, growth slows into an S-shaped curve that levels off at this value. For 10 points, name this maximum population, symbolized K."
        },
        {
            "p": "The 1972 report _The Limits to Growth_, written for the Club of Rome, used a computer model called World3 to explore what might happen if the world’s population and economy overshot this limit. Ecologists say a population overshoots when it rises past this value, often followed by a crash.",
            "r": "Limiting factors such as food and space set it. For 10 points, name this largest population an environment can support, symbolized K."
        },
        {
            "p": "Aldo Leopold pointed to mule deer on Arizona’s Kaibab [“KY-bab”] Plateau, whose herd was reported to soar after predators such as wolves and cougars were removed and then crash, as a warning about overshooting this value. Later scientists questioned how accurate the old deer counts were.",
            "r": "It is determined by limiting factors such as food and water. For 10 points, name this largest population an environment can support, symbolized K."
        },
        {
            "p": "Multiplying the exponential growth equation, dN/dt = rN, by a factor of one minus N divided by this value produces the logistic growth equation, in which r is the intrinsic rate of increase. When N is small, that factor is close to one, so growth is nearly exponential.",
            "r": "Growth in that equation drops to zero when N reaches this value. For 10 points, name this maximum population, symbolized K, that an environment can support."
        },
        {
            "p": "In the logistic model, this value is a stable equilibrium: a population above it shrinks, and a population below it grows back toward it. Real populations often overshoot this value and then swing up and down around it instead of settling exactly on it.",
            "r": "It is set by limiting factors like food, water, and shelter. For 10 points, name this largest population that an environment can support, symbolized K."
        },
        {
            "p": "Volunteers who put up nest boxes for eastern bluebirds raise this value for the birds, whose numbers had been limited by a shortage of nesting holes. Destroying or breaking up a species’ habitat has the opposite effect, lowering this value.",
            "r": "Limiting factors such as food, water, and shelter determine it. For 10 points, name this largest population an environment can support, symbolized K."
        }
    ],
    "clues": [
        {
            "id": "definition",
            "tier": "giveaway",
            "t": "The largest population of a species that an environment can support over time",
            "k": ["largest population", "environment", "support"],
            "n": 0
        },
        {
            "id": "symbol-k",
            "tier": "giveaway",
            "t": "Symbolized by the letter K in ecology equations and graphs",
            "k": ["letter k", "symbolized"],
            "n": 0
        },
        {
            "id": "flattens",
            "tier": "giveaway",
            "t": "The level where an S-shaped (logistic) growth curve flattens out",
            "k": ["s-shaped", "logistic", "flattens"],
            "n": 0
        },
        {
            "id": "limiting-factors",
            "tier": "giveaway",
            "t": "Set by limiting factors such as food, water, shelter, and space",
            "k": ["limiting factors"],
            "n": 0
        },
        {
            "id": "logistic-equation",
            "tier": "middle",
            "t": "In the logistic equation, dN/dt = rN(1 − N/K), growth slows to zero as N reaches it",
            "k": ["logistic equation", "slows to zero"],
            "n": 0
        },
        {
            "id": "births-deaths",
            "tier": "middle",
            "t": "At this level, births and deaths balance, so the population stops growing",
            "k": ["births and deaths", "stops growing"],
            "n": 0
        },
        {
            "id": "j-vs-s",
            "tier": "middle",
            "t": "Unlimited resources give J-shaped exponential growth; real populations slow down into an S-shaped curve",
            "k": ["j-shaped", "exponential"],
            "n": 0
        },
        {
            "id": "density-factors",
            "tier": "middle",
            "t": "Density-dependent factors (competition, predation, disease) grow stronger as a population nears it; density-independent ones (floods, fires) don’t",
            "k": ["density-dependent", "density-independent"],
            "n": 0
        },
        {
            "id": "overshoot",
            "tier": "middle",
            "t": "A population that overshoots it often crashes, or swings up and down around it",
            "k": ["overshoots", "crashes"],
            "n": 0
        },
        {
            "id": "k-selection",
            "tier": "middle",
            "t": "K-selected species, like elephants and whales, have few young and stay near it; r-selected species have many young and grow fast",
            "k": ["k-selected", "r-selected"],
            "n": 0
        },
        {
            "id": "st-matthew",
            "tier": "middle",
            "t": "Reindeer left on Alaska’s St. Matthew Island in 1944 grew from 29 to about 6,000, ate the lichen, and crashed to 42 by 1966",
            "k": ["st. matthew island", "reindeer", "lichen"],
            "n": 0
        },
        {
            "id": "rangeland",
            "tier": "middle",
            "t": "Ranchers use the term for the number of grazing animals a pasture can feed without being damaged",
            "k": ["grazing animals", "pasture"],
            "n": 0
        },
        {
            "id": "half-k",
            "tier": "middle",
            "t": "Population growth is fastest at half of it, the inflection point of the S-shaped curve",
            "k": ["inflection point", "half"],
            "n": 0
        },
        {
            "id": "verhulst",
            "tier": "power",
            "t": "Pierre-François Verhulst’s 1838 logistic equation describes growth that levels off at it",
            "k": ["verhulst", "1838"],
            "n": 0
        },
        {
            "id": "pearl-reed",
            "tier": "power",
            "t": "Raymond Pearl and Lowell Reed revived the logistic equation in 1920 by fitting it to U.S. census counts",
            "k": ["pearl", "reed", "1920", "census"],
            "n": 0
        },
        {
            "id": "macarthur-wilson",
            "tier": "power",
            "t": "Robert MacArthur and E. O. Wilson named r- and K-selection in _The Theory of Island Biogeography_ (1967)",
            "k": ["macarthur", "wilson", "island biogeography", "1967"],
            "n": 0
        },
        {
            "id": "klein",
            "tier": "power",
            "t": "David Klein blamed the St. Matthew Island crash on a harsh winter and a herd that had overshot it",
            "k": ["david klein", "harsh winter"],
            "n": 0
        },
        {
            "id": "liebig",
            "tier": "power",
            "t": "Liebig’s law of the minimum, pictured as a barrel that holds water only up to its shortest board: the scarcest resource limits growth",
            "k": ["law of the minimum", "liebig", "barrel"],
            "n": 0
        },
        {
            "id": "msy",
            "tier": "power",
            "t": "In simple fishery models, the maximum sustainable yield comes from keeping a stock at about half of it",
            "k": ["maximum sustainable yield", "fishery"],
            "n": 0
        },
        {
            "id": "gause",
            "tier": "power",
            "t": "Georgy Gause’s _Paramecium_ cultures rose fast, then leveled off; he described them in _The Struggle for Existence_ (1934)",
            "k": ["gause", "paramecium", "struggle for existence"],
            "n": 0
        },
        {
            "id": "malthus",
            "tier": "power",
            "t": "Thomas Malthus argued in 1798 that a growing human population would tend to outrun its food supply",
            "k": ["malthus", "1798", "food supply"],
            "n": 0,
            "rabbit": "Charles Darwin"
        },
        {
            "id": "joel-cohen",
            "tier": "power",
            "t": "Joel Cohen’s 1995 book _How Many People Can the Earth Support?_ found that estimates of it for humans vary enormously",
            "k": ["joel cohen", "1995"],
            "n": 0
        },
        {
            "id": "limits-to-growth",
            "tier": "power",
            "t": "_The Limits to Growth_ (1972), written for the Club of Rome, used the World3 computer model to explore overshoot",
            "k": ["limits to growth", "club of rome", "world3"],
            "n": 0
        },
        {
            "id": "environmental-resistance",
            "tier": "power",
            "t": "Environmental resistance, the sum of all limiting factors, is the gap between biotic potential and real growth",
            "k": ["environmental resistance", "biotic potential"],
            "n": 0
        },
        {
            "id": "kaibab",
            "tier": "power",
            "t": "Aldo Leopold cited Arizona’s Kaibab Plateau deer, reported to soar and crash after predators were removed; later scientists doubted the counts",
            "k": ["kaibab", "aldo leopold"],
            "n": 0
        },
        {
            "id": "stable-equilibrium",
            "tier": "power",
            "t": "In the logistic model it is a stable equilibrium: populations above it shrink, and populations below it grow",
            "k": ["stable equilibrium"],
            "n": 0
        },
        {
            "id": "bluebirds",
            "tier": "power",
            "t": "Nest boxes raised it for eastern bluebirds, which were limited by a shortage of nesting holes; habitat loss lowers it",
            "k": ["nest boxes", "bluebirds", "habitat loss"],
            "n": 0
        }
    ],
    "trap": {
        "title": "The limit, not the curve",
        "body": "Carrying capacity is a number: the population size where growth stops. Logistic growth is the S-shaped pattern a population follows on its way there, and limiting factors, like food and space, are what set the number. Answering “logistic growth,” “limiting factors,” or “exponential growth” for this value is wrong, and the bare letter “K” earns only a prompt.",
        "fix": "Listen for the noun. “This value,” “this quantity,” “this maximum population,” or “symbolized K” means carrying capacity. “This pattern of growth” or “this S-shaped curve” means logistic growth, “this J-shaped growth” means exponential growth, and “these factors” means limiting factors.",
        "line": "Real answer line: <b><u>Carrying capacity</u></b> (prompt on <u>K</u>; do not accept “logistic growth” or “limiting factors”)"
    },
    "tests": {
        "right": [
            "Carrying capacity",
            "carrying capacities",
            "Carying capacity",
            "carrying capcity",
            "Environmental carrying capacity"
        ],
        "prompt": [
            "K",
            "maximum population size"
        ],
        "wrong": [
            "Logistic growth",
            "Limiting factors",
            "Exponential growth",
            "Heat capacity",
            "Biotic potential",
            "K-selection"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
