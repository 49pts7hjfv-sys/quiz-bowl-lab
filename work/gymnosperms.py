import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "gymnosperms",
    "name": "Gymnosperms",
    "mono": "GYM",
    "category": "Biology",
    "qbCategory": "Science · Biology",
    "kicker": "“Naked seed” plants · Conifers, cycads, ginkgos, and gnetophytes",
    "dates": "First appeared more than 300 million years ago",
    "briefing": "Gymnosperms are seed plants whose seeds sit out in the open, usually on the scales of a cone, instead of being wrapped inside a fruit; their name means “naked seed” in Greek. The group includes pines, spruces, and other conifers, plus palm-like cycads, the fan-leaved ginkgo, and unusual gnetophytes such as the two-leaved desert plant _Welwitschia_. They ruled forests in the age of the dinosaurs, and the tallest known tree and the biggest single tree are both conifers.",
    "answerHtml": "<b><u>Gymnosperms</u></b> (accept <u>gymnosperm</u> or <u>Gymnospermae</u>; prompt on <u>seed plants</u>; do not accept “conifers” or “angiosperms”)",
    "accept": [
        "gymnosperms",
        "gymnosperm",
        "gymnospermae"
    ],
    "prompt": [
        "seed plants",
        "seed plant",
        "spermatophytes",
        "spermatophyta"
    ],
    "reject": [
        "angiosperms",
        "angiosperm",
        "flowering plants",
        "flowering plant",
        "conifers",
        "conifer",
        "coniferophyta",
        "pinophyta",
        "cycads",
        "cycad",
        "ginkgo",
        "ginkgos",
        "ginkgo biloba",
        "gnetophytes",
        "gnetophyta",
        "ferns",
        "fern",
        "mosses",
        "bryophytes",
        "pteridophytes",
        "seedless vascular plants",
        "vascular plants",
        "pine trees",
        "pine tree",
        "pines",
        "cones",
        "pine cones",
        "pinecones",
        "evergreens",
        "evergreen trees",
        "softwoods",
        "monocots",
        "dicots"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Gymnosperm",
    "qb": {
        "q": "gymnosperms",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "_Welwitschia_ [“wel-WITCH-ee-uh”], a desert plant that grows only two leaves in its whole life, belongs to a small division of this group called the gnetophytes [“NEE-toh-fyts”]. Unlike the rest of this group, gnetophytes have water-carrying vessels in their xylem, like flowering plants.",
            "r": "For 10 points, name this group of seed plants, including pines and other conifers, whose seeds are not enclosed in fruit."
        },
        {
            "p": "Unlike flowering plants, these plants never form a triploid endosperm; instead, the food stored in their seeds is haploid tissue from the female gametophyte. Many of them catch pollen on a sticky “pollination drop” that oozes from the tiny opening of each ovule.",
            "r": "For 10 points, name this group of seed plants, which includes cycads and conifers, whose name means “naked seed.”"
        },
        {
            "p": "_Ginkgo biloba_ [“GINK-oh by-LOH-buh”], the only living species in its division of this group, has fan-shaped leaves, and its female trees make seeds with a fleshy coat that smells like rancid butter. Ginkgos and cycads in this group still make swimming sperm.",
            "r": "For 10 points, name this group of seed plants, which also includes conifers, whose seeds are not enclosed in a fruit."
        },
        {
            "p": "The sago palm is not a true palm but a cycad, a member of this group. Cycads grow special coral-shaped roots that house nitrogen-fixing cyanobacteria, and they were common in the age of the dinosaurs.",
            "r": "For 10 points, name this group of seed plants, including pines and spruces, that often carry their seeds on cones."
        },
        {
            "p": "In pines, members of this group, fertilization happens more than a year after a pollen grain lands on a seed cone, and the seeds can take about two years to mature. Pine pollen grains have two air sacs that help them ride the wind.",
            "r": "For 10 points, name this group of plants, which includes conifers, cycads, and the ginkgo, that do not enclose their seeds in fruit."
        },
        {
            "p": "Lodgepole pines and jack pines in this group make serotinous [“seh-ROT-ih-nus”] cones, which stay sealed with resin until the heat of a forest fire opens them. Amber is fossilized resin, and much of it came from trees in this group.",
            "r": "For 10 points, name this group of “naked seed” plants that includes pines, firs, and spruces."
        },
        {
            "p": "A coast redwood named Hyperion, the tallest known living tree, belongs to this group, as does a Great Basin bristlecone pine called Methuselah, one of the oldest known living trees. So does General Sherman, a giant sequoia in California that is the biggest known single tree by volume.",
            "r": "For 10 points, name this group of seed plants, including conifers, whose seeds are not enclosed in an ovary."
        },
        {
            "p": "The cancer drug paclitaxel [“pak-lih-TAK-sul”], sold as Taxol, was first found in the bark of the Pacific yew, a tree in this group. Unlike pines, yews do not make woody seed cones; instead, each seed sits in a fleshy red cup called an aril.",
            "r": "Most members of this group are evergreen. For 10 points, name this group of seed plants that also includes pines and other conifers."
        },
        {
            "p": "The dawn redwood was known only from fossils until living trees were found in China in the 1940s, and the Wollemi [“WALL-uh-my”] pine was discovered in an Australian canyon in 1994. Both are “living fossils” from this ancient group of plants.",
            "r": "This group dominated forests during the age of the dinosaurs. For 10 points, name this group of plants with “naked” seeds, including conifers."
        },
        {
            "p": "The leaves of many members of this group are narrow needles with a thick waxy cuticle and stomata sunk into pits, adaptations that help them keep water through winters when the soil is frozen.",
            "r": "Members of this group dominate the taiga across Canada and Russia. For 10 points, name this group of seed plants, which includes pines, spruces, and firs."
        },
        {
            "p": "The wood of most members of this group, called softwood, is made almost entirely of water-carrying tracheids [“TRAY-kee-idz”] rather than the wide vessels of hardwoods. Their phloem uses sieve cells helped by Strasburger [“SHTRAHS-boor-ger”] cells instead of companion cells.",
            "r": "Pine resin from this group can be made into turpentine. For 10 points, name this group of plants whose seeds develop on the scales of cones."
        },
        {
            "p": "Each scale of a pine’s seed cone carries two ovules, and pollen enters each ovule through a tiny opening called the micropyle [“MY-kroh-pyle”]. When the cone dries and opens, its seeds, many with a papery wing, flutter away on the wind.",
            "r": "For 10 points, name this group of seed plants, including conifers, whose seeds are not enclosed in fruit."
        },
        {
            "p": "Larches, bald cypresses, and dawn redwoods are unusual members of this group because they are deciduous, dropping all their needles every fall. Bald cypresses growing in swamps send up woody bumps called “knees” around their trunks.",
            "r": "Most other members of this group, such as pines, stay green all year. For 10 points, name this group of plants whose seeds are not enclosed in fruit."
        },
        {
            "p": "Ginkgophyta [“gink-GOFF-ih-tuh”], which has just one living species, is one of this group’s four living divisions, along with the cycads and the gnetophytes. This group appeared more than 300 million years ago, long before flowering plants, and dominated the world’s forests during the Mesozoic Era.",
            "r": "The fourth division is the conifers. For 10 points, name this group of seed plants whose name means “naked seed.”"
        },
        {
            "p": "_Gnetum_, a tropical member of this group, has broad leaves that look like those of flowering plants. In the same group, the “berries” of junipers are really tiny cones whose scales have turned fleshy and fused together, and the edible “nuts” of piñon [“PIN-yohn”] pines are actually seeds.",
            "r": "This group also includes the spruces and firs often used as Christmas trees. For 10 points, name this group of seed plants that carry seeds on cones rather than in fruit."
        }
    ],
    "clues": [
        {
            "id": "naked-seed",
            "tier": "giveaway",
            "t": "Seed plants whose seeds are not enclosed in a fruit; the name means “naked seed” in Greek",
            "k": ["naked seed", "greek", "fruit"],
            "n": 0
        },
        {
            "id": "cones",
            "tier": "giveaway",
            "t": "Many carry their seeds on the scales of cones",
            "k": ["cones", "scales"],
            "n": 0
        },
        {
            "id": "conifers",
            "tier": "giveaway",
            "t": "Include conifers such as pines, spruces, firs (popular Christmas trees), cedars, and redwoods",
            "k": ["conifers", "pines", "spruces", "christmas trees"],
            "n": 0,
            "rabbit": "Trees"
        },
        {
            "id": "vs-angiosperms",
            "tier": "giveaway",
            "t": "Their flowering relatives, the angiosperms, enclose seeds inside an ovary that becomes a fruit",
            "k": ["angiosperms", "ovary"],
            "n": 0,
            "rabbit": "Flowers"
        },
        {
            "id": "evergreen",
            "tier": "giveaway",
            "t": "Most are evergreen, keeping needle- or scale-shaped leaves all year",
            "k": ["evergreen", "needle"],
            "n": 0,
            "rabbit": "Leaves"
        },
        {
            "id": "four-groups",
            "tier": "middle",
            "t": "Four living groups: conifers, cycads, the ginkgo, and gnetophytes",
            "k": ["four living groups", "cycads", "ginkgo", "gnetophytes"],
            "n": 0
        },
        {
            "id": "wind-pollinated",
            "tier": "middle",
            "t": "Most are pollinated by wind; pine pollen grains have two air sacs that help them float",
            "k": ["wind", "air sacs"],
            "n": 0,
            "rabbit": "Pollen"
        },
        {
            "id": "softwood",
            "tier": "middle",
            "t": "Conifer wood, called softwood, is made mostly of tracheids, not wide vessels; pine resin is distilled into turpentine",
            "k": ["softwood", "tracheids", "turpentine"],
            "n": 0,
            "rabbit": "Xylem"
        },
        {
            "id": "taiga",
            "tier": "middle",
            "t": "Conifers dominate the taiga, or boreal forest, across Canada, Scandinavia, and Russia",
            "k": ["taiga", "boreal forest"],
            "n": 0,
            "rabbit": "Tundra"
        },
        {
            "id": "needles",
            "tier": "middle",
            "t": "Needles with a thick waxy cuticle and sunken stomata help them keep water through frozen winters",
            "k": ["waxy cuticle", "sunken stomata", "needles"],
            "n": 0
        },
        {
            "id": "ginkgo",
            "tier": "middle",
            "t": "_Ginkgo biloba_, a “living fossil” with fan-shaped leaves, is the only living species in its division; female trees make smelly seeds",
            "k": ["ginkgo biloba", "living fossil", "fan-shaped"],
            "n": 0
        },
        {
            "id": "dinosaur-age",
            "tier": "middle",
            "t": "Appeared more than 300 million years ago and dominated forests in the age of the dinosaurs, the Mesozoic Era",
            "k": ["dinosaurs", "mesozoic", "300 million"],
            "n": 0
        },
        {
            "id": "gnetophytes",
            "tier": "power",
            "t": "Gnetophytes (_Gnetum_, _Ephedra_, and _Welwitschia_) are the only ones with xylem vessels; _Gnetum_ has broad leaves like a flowering plant’s",
            "k": ["gnetophytes", "vessels", "gnetum"],
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
            "id": "haploid-food",
            "tier": "power",
            "t": "No triploid endosperm: the food in their seeds is haploid tissue from the female gametophyte",
            "k": ["female gametophyte", "haploid", "endosperm"],
            "n": 0
        },
        {
            "id": "pollination-drop",
            "tier": "power",
            "t": "Many catch pollen on a sticky pollination drop at the micropyle, the opening of each ovule; each pine cone scale holds two ovules",
            "k": ["pollination drop", "micropyle", "two ovules"],
            "n": 0
        },
        {
            "id": "swimming-sperm",
            "tier": "power",
            "t": "Cycads and the ginkgo still make swimming sperm",
            "k": ["swimming sperm"],
            "n": 0
        },
        {
            "id": "cycads",
            "tier": "power",
            "t": "Cycads such as the sago palm look like palms; their coral-shaped (coralloid) roots house nitrogen-fixing cyanobacteria",
            "k": ["sago palm", "coralloid", "cyanobacteria"],
            "n": 0
        },
        {
            "id": "pine-timing",
            "tier": "power",
            "t": "In pines, fertilization comes more than a year after pollination, and seeds take about two years to mature",
            "k": ["more than a year", "two years"],
            "n": 0
        },
        {
            "id": "serotinous",
            "tier": "power",
            "t": "Lodgepole and jack pines make serotinous cones that stay sealed with resin until a fire opens them; fossilized resin is amber",
            "k": ["serotinous", "lodgepole", "amber"],
            "n": 0
        },
        {
            "id": "record-trees",
            "tier": "power",
            "t": "Record trees: Hyperion, a coast redwood (tallest known); General Sherman, a giant sequoia (biggest by volume); Methuselah, a bristlecone pine (among the oldest)",
            "k": ["hyperion", "general sherman", "methuselah", "bristlecone"],
            "n": 0
        },
        {
            "id": "yew-taxol",
            "tier": "power",
            "t": "The Pacific yew, whose seeds sit in red fleshy arils instead of cones, gave the cancer drug Taxol (paclitaxel)",
            "k": ["pacific yew", "taxol", "arils", "paclitaxel"],
            "n": 0
        },
        {
            "id": "living-fossils",
            "tier": "power",
            "t": "The dawn redwood (found alive in China in the 1940s) and the Wollemi pine (found in Australia in 1994) are “living fossils”",
            "k": ["dawn redwood", "wollemi", "1994"],
            "n": 0
        },
        {
            "id": "deciduous-conifers",
            "tier": "power",
            "t": "Larches, bald cypresses, and dawn redwoods are deciduous, dropping their needles every fall; bald cypresses grow woody “knees”",
            "k": ["deciduous", "larches", "bald cypresses", "knees"],
            "n": 0
        },
        {
            "id": "strasburger-cells",
            "tier": "power",
            "t": "Their phloem uses sieve cells helped by Strasburger cells instead of companion cells",
            "k": ["strasburger", "sieve cells"],
            "n": 0,
            "rabbit": "Phloem"
        },
        {
            "id": "juniper-pinon",
            "tier": "power",
            "t": "Juniper “berries” are really fleshy cones, and the “nuts” of piñon pines are really seeds",
            "k": ["juniper", "piñon", "berries"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Not just conifers",
        "body": "Most tossups on this group mention pines, spruces, and cones, so players blurt “conifers.” But conifers are only one of four living divisions: cycads, the ginkgo, and gnetophytes like _Welwitschia_ belong to this group too, so the narrower answer is wrong when the question asks for the whole group. The opposite trap is “angiosperms,” the flowering plants that enclose their seeds in fruit.",
        "fix": "“This group of seed plants,” “naked seeds,” or a mix of cycads, ginkgos, and pines means gymnosperms. Say conifers only for “these cone-bearing trees” when every clue stays on pines and their relatives. Fruit, flowers, or double fertilization mean angiosperms.",
        "line": "Real answer line: <b><u>Gymnosperms</u></b> (accept <u>Gymnospermae</u>; prompt on <u>seed plants</u>; do not accept “conifers” or “angiosperms”)"
    },
    "tests": {
        "right": [
            "Gymnosperms",
            "gymnosperm",
            "Gymnosperns",
            "the gymnosperms",
            "Gymnospermae"
        ],
        "prompt": [
            "Seed plants",
            "Spermatophytes"
        ],
        "wrong": [
            "Angiosperms",
            "Conifers",
            "Cycads",
            "Flowering plants",
            "Ferns",
            "Pine trees"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
