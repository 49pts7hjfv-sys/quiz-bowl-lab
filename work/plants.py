import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "plants",
    "name": "Plants",
    "mono": "PLT",
    "category": "Biology",
    "qbCategory": "Science · Biology",
    "kicker": "Green organisms that make their own food · The base of most food chains",
    "dates": "On land for more than 400 million years",
    "briefing": "Plants are living things that make their own food. Their green chlorophyll captures sunlight, and photosynthesis turns carbon dioxide and water into sugar while releasing the oxygen we breathe. The kingdom stretches from tiny mosses without true roots to giant sequoias such as General Sherman, the biggest single tree on Earth by volume, and every one of them has stiff cell walls made of cellulose.",
    "answerHtml": "<b><u>Plants</u></b> (accept <u>plant</u> kingdom, <u>Plantae</u>, <u>land plants</u>, or <u>embryophytes</u>; do not accept “fungi” or “algae”)",
    "accept": [
        "plants",
        "plant",
        "plantae",
        "kingdom plantae",
        "plant kingdom",
        "land plants",
        "land plant",
        "embryophytes",
        "embryophyte",
        "embryophyta",
        "green plants",
        "green plant"
    ],
    "prompt": [],
    "reject": [
        "planets",
        "planet",
        "fungi",
        "fungus",
        "algae",
        "alga",
        "animals",
        "animal",
        "protists",
        "protista",
        "trees",
        "tree",
        "flowers",
        "leaves",
        "plankton",
        "phytoplankton"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Plant",
    "qb": {
        "q": "plants",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "Joseph Priestley found that a sprig of mint could “restore” the air inside a sealed jar in which a candle had burned out. Jan Ingenhousz [“IN-gun-howss”] later showed that these organisms refresh air in this way only when sunlight shines on their green parts.",
            "r": "Their green color comes from chlorophyll. For 10 points, name these living things, including mosses and ferns, that make their own food by photosynthesis."
        },
        {
            "p": "Jan Baptist van Helmont grew a willow in a tub of carefully weighed soil for five years, found that the soil had lost almost no weight, and concluded that these organisms build their bodies from water. In fact, the carbon in their bodies comes mainly from carbon dioxide taken in through tiny pores called stomata.",
            "r": "For 10 points, name these organisms that make their own food in chloroplasts and form a kingdom separate from animals and fungi."
        },
        {
            "p": "Matthias Schleiden [“SHLY-den”] concluded in 1838 that all of these organisms are made of cells, and Theodor Schwann soon said the same about animals. Long before that, Robert Hooke named “cells” after looking at thin slices of cork, which comes from the bark of one of these organisms.",
            "r": "Their cells have rigid walls made of cellulose. For 10 points, name this kingdom of organisms that includes trees, grasses, and flowers."
        },
        {
            "p": "Theophrastus [“thee-uh-FRAS-tus”], who took over Aristotle’s school, is often called the “father of botany” for his books about these organisms. Carl Linnaeus later sorted these organisms into classes by counting the stamens and pistils in their flowers.",
            "r": "These organisms are producers, the first link in most food chains. For 10 points, name this kingdom of living things that make their own food from sunlight."
        },
        {
            "p": "Charles Darwin and his son Francis showed that canary grass seedlings bend toward light only when their tips are uncovered. Frits Went later collected the chemical behind that bending, which was named auxin, in tiny blocks of agar.",
            "r": "That bending toward light, called phototropism, helps these organisms catch sunlight for photosynthesis. For 10 points, name these living things, including oaks, ferns, and mosses."
        },
        {
            "p": "Hormones called gibberellins [“jib-uh-REL-inz”] were discovered in Japan by studying rice seedlings that grew strangely tall because of a fungus, a disease called “foolish seedling.” Another hormone, abscisic [“ab-SISS-ik”] acid, makes these organisms close their leaf pores during droughts.",
            "r": "The gas ethylene makes their fruit ripen. For 10 points, name these living things that use chlorophyll to make their own food."
        },
        {
            "p": "Thale cress, a small weed in the mustard family, became the first of these organisms to have its entire genome sequenced, in 2000. Gregor Mendel worked out the basic laws of heredity by breeding thousands of these organisms, all of them peas, in his monastery’s garden.",
            "r": "For 10 points, name this kingdom of organisms that use chlorophyll to capture sunlight, including peas, cress, and corn."
        },
        {
            "p": "_Rafflesia arnoldii_ [“ruh-FLEE-zhuh ar-NOLD-ee-eye”], which has the largest single flower of any of these organisms, has no leaves or stems of its own and steals its food from a vine. In the Namib Desert, _Welwitschia_ [“wel-WITCH-ee-uh”] grows only two leaves during its entire long life.",
            "r": "Most members of this kingdom are green from chlorophyll, which captures sunlight for photosynthesis. For 10 points, name this kingdom of living things that includes trees and flowers."
        },
        {
            "p": "The cells of these organisms trade materials through tiny channels in their walls called plasmodesmata [“plaz-moh-dez-MAH-tuh”]. Their mature cells usually hold a large central vacuole whose water pressure, called turgor pressure, keeps leaves and stems firm.",
            "r": "Their cell walls are made of cellulose. For 10 points, name these organisms whose cells contain chloroplasts for photosynthesis."
        },
        {
            "p": "The closest living relatives of these organisms are freshwater green algae called charophytes [“KAIR-uh-fites”], and these organisms began spreading onto land more than 400 million years ago. The earliest of these organisms on land lacked xylem and phloem, much like modern mosses and liverworts.",
            "r": "For 10 points, name this kingdom of organisms that make food by photosynthesis and include mosses, ferns, and flowering species."
        },
        {
            "p": "The life cycle of these organisms switches between a haploid gametophyte [“guh-MEE-tuh-fite”] stage and a diploid sporophyte [“SPOR-uh-fite”] stage, a pattern called alternation of generations. In mosses the gametophyte is the larger, longer-lived stage, while in ferns the sporophyte is.",
            "r": "Ferns release spores from clusters called sori on the undersides of their fronds. For 10 points, name this kingdom of organisms that make their own food by photosynthesis."
        },
        {
            "p": "In the flowering members of this kingdom, one sperm cell fertilizes an egg while a second sperm helps form a food-storing tissue called endosperm, a process called double fertilization. Conifers and other gymnosperms in this kingdom instead carry “naked” seeds, often on cones.",
            "r": "Many members of this kingdom move water through xylem and sugars through phloem. For 10 points, name this kingdom of organisms that make food through photosynthesis."
        },
        {
            "p": "Pairs of guard cells swell or shrink to open and close tiny pores called stomata [“STOH-muh-tuh”] on the leaves of these organisms. Water that evaporates from those pores in a process called transpiration helps pull more water up through tubes of xylem.",
            "r": "For 10 points, name these living things that take in carbon dioxide and give off oxygen as they make food by photosynthesis."
        },
        {
            "p": "One of these organisms, native only to bogs in the Carolinas, snaps its leaves shut when tiny trigger hairs are touched twice, trapping insects inside. Another one, _Mimosa pudica_, folds up its leaflets within seconds of being touched.",
            "r": "For 10 points, name these organisms, including the Venus flytrap, that make their own food through photosynthesis."
        },
        {
            "p": "Robert Whittaker’s 1969 system of five kingdoms placed these organisms beside animals, fungi, protists, and monerans. Unlike fungi, these organisms build their cell walls from cellulose rather than chitin [“KYE-tin”].",
            "r": "For 10 points, name these producers, which use chlorophyll to make their own food, a kingdom that includes mosses, ferns, and trees."
        }
    ],
    "clues": [
        {
            "id": "kingdom",
            "tier": "giveaway",
            "t": "Form their own kingdom of life, separate from animals, fungi, and protists",
            "k": ["kingdom", "fungi", "protists"],
            "n": 0
        },
        {
            "id": "photosynthesis",
            "tier": "giveaway",
            "t": "Make their own food by photosynthesis, so they are producers at the base of most food chains",
            "k": ["photosynthesis", "producers", "food chains"],
            "n": 0,
            "rabbit": "Photosynthesis"
        },
        {
            "id": "chlorophyll",
            "tier": "giveaway",
            "t": "Green because of chlorophyll, a pigment packed inside chloroplasts",
            "k": ["chlorophyll", "chloroplasts", "pigment"],
            "n": 0,
            "rabbit": "Chloroplasts"
        },
        {
            "id": "cellulose-walls",
            "tier": "giveaway",
            "t": "Their cells have stiff cell walls made of cellulose and usually a large central vacuole",
            "k": ["cellulose", "cell walls", "central vacuole"],
            "n": 0,
            "rabbit": "Cellulose"
        },
        {
            "id": "botany",
            "tier": "giveaway",
            "t": "Studied in botany; the kingdom includes mosses, ferns, conifers, and flowering species",
            "k": ["botany", "mosses", "ferns", "conifers"],
            "n": 0
        },
        {
            "id": "xylem-phloem",
            "tier": "middle",
            "t": "Vascular kinds move water up through xylem and sugar through phloem",
            "k": ["xylem", "phloem", "vascular"],
            "n": 0,
            "rabbit": "Xylem"
        },
        {
            "id": "nonvascular",
            "tier": "middle",
            "t": "Nonvascular bryophytes, like mosses and liverworts, lack xylem and phloem and stay small",
            "k": ["nonvascular", "bryophytes", "liverworts"],
            "n": 0
        },
        {
            "id": "stomata",
            "tier": "middle",
            "t": "Tiny leaf pores called stomata, opened and closed by guard cells, let carbon dioxide in",
            "k": ["stomata", "guard cells"],
            "n": 0
        },
        {
            "id": "transpiration",
            "tier": "middle",
            "t": "Water evaporating from leaves (transpiration) pulls more water up through the xylem",
            "k": ["transpiration", "evaporating"],
            "n": 0
        },
        {
            "id": "seeds",
            "tier": "middle",
            "t": "Gymnosperms, like conifers, have “naked” seeds; flowering angiosperms enclose seeds in fruit and use double fertilization",
            "k": ["gymnosperms", "angiosperms", "naked", "double fertilization"],
            "n": 0,
            "rabbit": "Gymnosperms"
        },
        {
            "id": "alternation",
            "tier": "middle",
            "t": "Alternation of generations: a haploid gametophyte stage alternates with a diploid sporophyte stage",
            "k": ["alternation of generations", "gametophyte", "sporophyte"],
            "n": 0
        },
        {
            "id": "ferns-sori",
            "tier": "middle",
            "t": "Ferns release spores from clusters called sori under their fronds",
            "k": ["sori", "spores", "fronds"],
            "n": 0
        },
        {
            "id": "hormones",
            "tier": "middle",
            "t": "Hormones: auxin causes bending toward light (phototropism), and the gas ethylene ripens fruit",
            "k": ["auxin", "ethylene", "phototropism"],
            "n": 0
        },
        {
            "id": "venus-flytrap",
            "tier": "middle",
            "t": "The Venus flytrap, native to the Carolinas, snaps shut when its trigger hairs are touched twice",
            "k": ["venus flytrap", "trigger hairs", "carolinas"],
            "n": 0
        },
        {
            "id": "mendel-peas",
            "tier": "middle",
            "t": "Gregor Mendel worked out the laws of heredity by breeding thousands of peas",
            "k": ["mendel", "peas", "heredity"],
            "n": 0,
            "rabbit": "Gregor Mendel"
        },
        {
            "id": "priestley",
            "tier": "power",
            "t": "Joseph Priestley found a sprig of mint could “restore” air where a candle had burned out; Jan Ingenhousz showed this needs sunlight",
            "k": ["priestley", "mint", "ingenhousz"],
            "n": 0
        },
        {
            "id": "van-helmont",
            "tier": "power",
            "t": "Jan Baptist van Helmont grew a willow for five years; the soil barely lost weight, so he credited water",
            "k": ["van helmont", "willow", "five years"],
            "n": 0
        },
        {
            "id": "schleiden",
            "tier": "power",
            "t": "Matthias Schleiden proposed in 1838 that all of them are made of cells, a step toward cell theory",
            "k": ["schleiden", "1838", "cell theory"],
            "n": 0
        },
        {
            "id": "theophrastus",
            "tier": "power",
            "t": "Theophrastus, who took over Aristotle’s school, is called the “father of botany”",
            "k": ["theophrastus", "aristotle", "father of botany"],
            "n": 0
        },
        {
            "id": "darwin-went",
            "tier": "power",
            "t": "Charles and Francis Darwin showed canary grass bends toward light sensed at its tip; Frits Went collected auxin in agar blocks",
            "k": ["canary grass", "francis", "frits went", "agar"],
            "n": 0
        },
        {
            "id": "gibberellins",
            "tier": "power",
            "t": "Gibberellins were discovered through rice’s “foolish seedling” disease, which makes seedlings grow too tall",
            "k": ["gibberellins", "foolish seedling", "rice"],
            "n": 0
        },
        {
            "id": "abscisic",
            "tier": "power",
            "t": "Abscisic acid closes their stomata during drought",
            "k": ["abscisic acid", "drought"],
            "n": 0
        },
        {
            "id": "charophytes",
            "tier": "power",
            "t": "Evolved from green algae; their closest living relatives are freshwater charophytes",
            "k": ["charophytes", "green algae"],
            "n": 0
        },
        {
            "id": "plasmodesmata",
            "tier": "power",
            "t": "Neighboring cells trade materials through tiny channels in their walls called plasmodesmata",
            "k": ["plasmodesmata", "channels"],
            "n": 0
        },
        {
            "id": "arabidopsis",
            "tier": "power",
            "t": "Thale cress (_Arabidopsis thaliana_), a mustard-family weed, was the first of them with a fully sequenced genome (2000)",
            "k": ["thale cress", "arabidopsis", "genome"],
            "n": 0
        },
        {
            "id": "rafflesia",
            "tier": "power",
            "t": "_Rafflesia arnoldii_ has the largest single flower and no leaves or stems of its own; it steals food from a vine",
            "k": ["rafflesia", "largest single flower"],
            "n": 0
        },
        {
            "id": "welwitschia",
            "tier": "power",
            "t": "_Welwitschia_ of the Namib Desert grows only two leaves in its whole life",
            "k": ["welwitschia", "namib", "two leaves"],
            "n": 0
        },
        {
            "id": "whittaker",
            "tier": "power",
            "t": "Robert Whittaker’s 1969 five-kingdom system; unlike fungi, their cell walls use cellulose, not chitin",
            "k": ["whittaker", "1969", "chitin"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Fungi are not plants",
        "body": "Mushrooms sprout from soil and stay in one place, so players lump fungi in with this kingdom, but fungi cannot make their own food: they absorb it, and their cell walls are made of chitin, not cellulose. Seaweeds and other algae are another trap; they photosynthesize, but most textbooks group them with the protists.",
        "fix": "Listen for the food clue. Photosynthesis, chlorophyll, cellulose, xylem, or seeds means plants; hyphae, chitin, mushrooms, or decomposing dead matter means fungi. Clues about single-celled or ocean-floating green life usually point to algae.",
        "line": "Real answer line: <b><u>Plants</u></b> (accept <u>Plantae</u> or <u>land plants</u>; do not accept “fungi” or “algae”)"
    },
    "tests": {
        "right": [
            "Plants",
            "plant",
            "Kingdom Plantae",
            "Plantes",
            "land plants"
        ],
        "prompt": [],
        "wrong": [
            "Planets",
            "Fungi",
            "Algae",
            "Animals",
            "Trees"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
