import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "echinoderms",
    "name": "Echinoderms",
    "mono": "ECH",
    "category": "Biology",
    "qbCategory": "Science · Biology",
    "kicker": "Spiny-skinned sea animals · Sea stars, sea urchins, and sand dollars",
    "dates": "About 7,000 living species, all in the sea",
    "briefing": "Echinoderms are spiny-skinned sea animals such as sea stars, sea urchins, sand dollars, and sea cucumbers. Most adults are built in five matching parts around a central mouth, and they creep along on hundreds of tiny tube feet powered by water pumped through canals inside their bodies. A sea star can even push its stomach out of its mouth to digest a clam outside its body, and it can regrow a lost arm.",
    "answerHtml": "<b><u>Echinoderms</u></b> (accept <u>Echinodermata</u>; do not accept a single member such as “starfish”)",
    "accept": [
        "echinoderms",
        "echinoderm",
        "echinodermata",
        "phylum echinodermata"
    ],
    "prompt": [],
    "reject": [
        "cnidarians",
        "cnidarian",
        "cnidaria",
        "mollusks",
        "mollusk",
        "molluscs",
        "mollusca",
        "arthropods",
        "arthropoda",
        "chordates",
        "chordata",
        "hemichordates",
        "deuterostomes",
        "sponges",
        "porifera",
        "annelids",
        "crustaceans",
        "jellyfish",
        "corals",
        "starfish",
        "sea star",
        "sea stars",
        "sea urchin",
        "sea urchins",
        "sand dollar",
        "sand dollars",
        "sea cucumber",
        "sea cucumbers",
        "brittle stars",
        "sea lilies",
        "crinoids",
        "asteroidea",
        "echinoidea",
        "echinoids"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Echinoderm",
    "qb": {
        "q": "echinoderm",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "Some members of this phylum chew with a five-toothed jaw structure called Aristotle’s lantern, named for the Greek thinker who described it. Members of this phylum have an internal skeleton made of small plates of calcium carbonate called ossicles [“OSS-ih-kulz”].",
            "r": "For 10 points, name this phylum of spiny-skinned sea animals that includes sea urchins and sea stars."
        },
        {
            "p": "Water enters a network of canals inside members of this phylum through a sieve-like plate called the madreporite [“MAD-ruh-por-ite”]. Muscular bulbs called ampullae [“am-PULL-ee”] squeeze that water into the tube feet, stretching them out so the animal can creep along or grip a rock.",
            "r": "That network is the water vascular system. For 10 points, name this phylum whose members include starfish and sea urchins."
        },
        {
            "p": "Ecologist Robert Paine coined the term “keystone species” after he removed a predator from this phylum, Pisaster ochraceus, from tide pools in Washington State and watched mussels crowd out other species. Another member of this phylum, the crown-of-thorns, has wiped out large areas of coral on the Great Barrier Reef.",
            "r": "For 10 points, name this phylum of tube-footed sea animals that includes the sea stars and sand dollars."
        },
        {
            "p": "In the 1870s, Oscar Hertwig first saw the nucleus of a sperm cell fuse with the nucleus of an egg by studying eggs of a member of this phylum. Like chordates, members of this phylum are deuterostomes: an early embryo’s first opening becomes the anus, not the mouth.",
            "r": "These animals move on tube feet. For 10 points, name this phylum that includes sea urchins, sand dollars, and sea stars."
        },
        {
            "p": "Beginning in 2013, a wasting disease killed millions of members of this phylum along the Pacific coast of North America, and the sunflower species was later listed as critically endangered. Some members of this phylum eat clams by prying their shells apart and pushing their own stomachs inside to digest the clam.",
            "r": "These animals have tube feet and five-part bodies. For 10 points, name this phylum whose members include sea stars and sea urchins."
        },
        {
            "p": "When attacked, some members of this phylum shoot out sticky threads called Cuvierian tubules, while others can expel some of their internal organs and later regrow them. Those soft, sausage-shaped members of this phylum are dried and eaten as a delicacy called trepang [“trih-PANG”].",
            "r": "Those animals are sea cucumbers. For 10 points, name this phylum that also includes sea stars and sand dollars."
        },
        {
            "p": "Swimming larvae of members of this phylum, such as the bipinnaria [“bye-pih-NAIR-ee-uh”] and the pluteus [“PLOO-tee-us”], are bilaterally symmetrical, but they change into adults whose bodies are built in five matching parts around a central mouth.",
            "r": "For 10 points, name this phylum of spiny-skinned animals that includes sea stars, sea urchins, and sand dollars."
        },
        {
            "p": "Members of this phylum can quickly stiffen or loosen a special “catch” connective tissue, which lets some of them lock their spines in place. Members of this phylum have no brain; instead, a ring of nerves around the mouth connects to nerves that run out into each section of the body.",
            "r": "For 10 points, name this phylum of marine invertebrates that move on tube feet and include the sea urchins."
        },
        {
            "p": "Stalked members of this phylum called sea lilies look like flowers, and pieces of their fossil stems are common in ancient limestone. Their stalkless relatives, the feather stars, can swim by waving their arms, and both groups are called crinoids [“KRY-noyds”].",
            "r": "Brittle stars belong to another class of this phylum. For 10 points, name this phylum of spiny-skinned animals that includes sea stars."
        },
        {
            "p": "Tiny pincers called pedicellariae [“ped-ih-suh-LAIR-ee-ee”] help keep the skin of some members of this phylum clean. Some members of this phylum sense light with a simple eyespot at the tip of each arm, and they can regrow arms that have been lost.",
            "r": "For 10 points, name this phylum whose members, including starfish, creep along on hundreds of tube feet."
        },
        {
            "p": "Where sea otters have been hunted out, grazing members of this phylum can multiply and strip kelp forests down to bare rock, leaving areas called “barrens.” Flattened, burrowing members of this phylum leave behind white skeletons, called tests, that often wash up on sandy beaches.",
            "r": "Those flat animals are sand dollars. For 10 points, name this phylum that also includes sea stars and sea urchins."
        },
        {
            "p": "Each skeletal plate of a member of this phylum acts like a single crystal of the mineral calcite, with a spongy, hole-filled structure called stereom. Among invertebrates, members of this phylum are some of the closest relatives of chordates, since both groups are deuterostomes.",
            "r": "These animals move on tube feet. For 10 points, name this phylum of spiny-skinned animals, including sea urchins and starfish."
        },
        {
            "p": "The classes Asteroidea [“ass-tuh-ROY-dee-uh”], Ophiuroidea [“oh-fee-yuh-ROY-dee-uh”], and Holothuroidea [“hol-uh-thyoo-ROY-dee-uh”] belong to this phylum. Members of the class Ophiuroidea, called brittle stars, wave long, thin arms that can break off and grow back, and like other members of this phylum, they move using tube feet.",
            "r": "For 10 points, name this phylum of “spiny-skinned” sea animals that includes sea urchins and sand dollars."
        },
        {
            "p": "A cardiac stomach that some members of this phylum push out through the mouth onto their prey works together with a pyloric stomach linked to digestive glands in each of their arms. This lets them eat clams far bigger than their mouths.",
            "r": "These animals move with tube feet powered by a water vascular system. For 10 points, name this phylum of sea animals that includes the starfish."
        },
        {
            "p": "Basket stars, close relatives of the brittle stars in this phylum, catch tiny drifting animals with arms that branch again and again into tangled curls. Most adult members of this phylum have five-part radial symmetry, though their larvae are bilaterally symmetrical.",
            "r": "For 10 points, name this phylum, whose name means “spiny skin,” that includes sea stars and sea urchins."
        }
    ],
    "clues": [
        {
            "id": "members",
            "tier": "giveaway",
            "t": "Phylum of sea animals including sea stars (starfish), sea urchins, sand dollars, and sea cucumbers",
            "k": ["sea stars", "starfish", "sea urchins", "sand dollars", "sea cucumbers"],
            "n": 0
        },
        {
            "id": "spiny-skin",
            "tier": "giveaway",
            "t": "Its name comes from Greek words meaning “spiny skin”",
            "k": ["spiny skin", "greek"],
            "n": 0
        },
        {
            "id": "tube-feet",
            "tier": "giveaway",
            "t": "Creep along and grip rocks with hundreds of small tube feet",
            "k": ["tube feet", "grip"],
            "n": 0
        },
        {
            "id": "five-part",
            "tier": "giveaway",
            "t": "Adults usually have five-part (pentaradial) symmetry around a central mouth",
            "k": ["five-part", "pentaradial", "symmetry"],
            "n": 0
        },
        {
            "id": "all-marine",
            "tier": "giveaway",
            "t": "Every species lives in the sea; none live in fresh water or on land",
            "k": ["fresh water", "sea"],
            "n": 0
        },
        {
            "id": "water-vascular",
            "tier": "middle",
            "t": "A water vascular system of water-filled canals powers the tube feet",
            "k": ["water vascular system", "canals"],
            "n": 0
        },
        {
            "id": "endoskeleton",
            "tier": "middle",
            "t": "An internal skeleton (endoskeleton) of calcium carbonate plates called ossicles sits just under the skin",
            "k": ["endoskeleton", "ossicles", "calcium carbonate"],
            "n": 0
        },
        {
            "id": "larvae",
            "tier": "middle",
            "t": "Their swimming larvae have bilateral symmetry; only the adults switch to five-part symmetry",
            "k": ["larvae", "bilateral"],
            "n": 0
        },
        {
            "id": "deuterostomes",
            "tier": "middle",
            "t": "Deuterostomes, like chordates: an embryo’s first opening becomes the anus, not the mouth",
            "k": ["deuterostomes", "chordates"],
            "n": 0,
            "rabbit": "Chordates"
        },
        {
            "id": "stomach",
            "tier": "middle",
            "t": "Sea stars push their cardiac stomach out through the mouth to digest clams and mussels outside the body; a second, pyloric stomach stays inside",
            "k": ["cardiac stomach", "pyloric", "clams"],
            "n": 0
        },
        {
            "id": "regrow-eyespot",
            "tier": "middle",
            "t": "Sea stars can regrow lost arms, and each arm tip has a simple eyespot",
            "k": ["regrow", "eyespot"],
            "n": 0
        },
        {
            "id": "no-brain",
            "tier": "middle",
            "t": "No brain: a ring of nerves around the mouth links to nerves running out into each body section",
            "k": ["ring of nerves", "no brain"],
            "n": 0
        },
        {
            "id": "crown-of-thorns",
            "tier": "middle",
            "t": "The coral-eating crown-of-thorns starfish has wiped out large areas of the Great Barrier Reef",
            "k": ["crown-of-thorns", "great barrier reef"],
            "n": 0,
            "rabbit": "Coral reefs"
        },
        {
            "id": "sea-cucumber-defense",
            "tier": "middle",
            "t": "Sea cucumbers can expel some of their internal organs to escape predators, then regrow them",
            "k": ["expel", "internal organs"],
            "n": 0
        },
        {
            "id": "sand-dollar-tests",
            "tier": "middle",
            "t": "Sand dollars are flat, burrowing relatives of sea urchins; their skeletons are called tests",
            "k": ["tests", "burrowing"],
            "n": 0
        },
        {
            "id": "aristotles-lantern",
            "tier": "power",
            "t": "Sea urchins chew with a five-toothed jaw structure called Aristotle’s lantern",
            "k": ["aristotle", "lantern", "five-toothed"],
            "n": 0
        },
        {
            "id": "madreporite",
            "tier": "power",
            "t": "Water enters through a sieve plate called the madreporite; bulb-shaped ampullae squeeze it into the tube feet",
            "k": ["madreporite", "ampullae", "sieve plate"],
            "n": 0
        },
        {
            "id": "pedicellariae",
            "tier": "power",
            "t": "Tiny pincers called pedicellariae help keep the skin of sea stars and sea urchins clean",
            "k": ["pedicellariae", "pincers"],
            "n": 0
        },
        {
            "id": "catch-tissue",
            "tier": "power",
            "t": "“Catch” connective tissue can quickly stiffen or loosen, locking a sea urchin’s spines in place",
            "k": ["connective tissue", "catch", "spines"],
            "n": 0
        },
        {
            "id": "larva-names",
            "tier": "power",
            "t": "Their larvae have names like bipinnaria (sea stars) and pluteus (sea urchins)",
            "k": ["bipinnaria", "pluteus"],
            "n": 0
        },
        {
            "id": "paine-keystone",
            "tier": "power",
            "t": "Robert Paine coined “keystone species” after removing the sea star Pisaster from Washington tide pools, letting mussels take over",
            "k": ["keystone species", "robert paine", "pisaster"],
            "n": 0,
            "rabbit": "Predation"
        },
        {
            "id": "hertwig",
            "tier": "power",
            "t": "In the 1870s, Oscar Hertwig first saw sperm and egg nuclei fuse in sea urchin eggs; sea urchins became classic model organisms",
            "k": ["oscar hertwig", "hertwig", "model organisms"],
            "n": 0
        },
        {
            "id": "wasting-disease",
            "tier": "power",
            "t": "Sea star wasting disease, starting in 2013, killed millions on North America’s Pacific coast; the sunflower sea star became critically endangered",
            "k": ["wasting disease", "sunflower", "2013"],
            "n": 0
        },
        {
            "id": "classes",
            "tier": "power",
            "t": "Its classes include Asteroidea (sea stars), Ophiuroidea (brittle stars and basket stars), Holothuroidea (sea cucumbers), and Crinoidea (sea lilies)",
            "k": ["asteroidea", "ophiuroidea", "holothuroidea", "crinoidea"],
            "n": 0
        },
        {
            "id": "cuvierian-trepang",
            "tier": "power",
            "t": "Some sea cucumbers shoot sticky Cuvierian tubules at attackers; dried sea cucumbers are eaten as a delicacy called trepang",
            "k": ["cuvierian", "trepang", "sticky"],
            "n": 0
        },
        {
            "id": "sea-lilies",
            "tier": "power",
            "t": "Stalked sea lilies look like flowers; their fossil stems are common in ancient limestone, and swimming feather stars are their relatives",
            "k": ["sea lilies", "limestone", "feather stars"],
            "n": 0
        },
        {
            "id": "stereom",
            "tier": "power",
            "t": "Each skeletal plate acts like a single calcite crystal with a spongy, hole-filled structure called stereom",
            "k": ["stereom", "calcite", "single calcite crystal"],
            "n": 0
        },
        {
            "id": "urchin-barrens",
            "tier": "power",
            "t": "Without sea otters to eat them, sea urchins can strip kelp forests into bare “urchin barrens”",
            "k": ["sea otters", "kelp", "barrens"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Phylum, not starfish",
        "body": "Most clues describe one famous member, like a sea urchin’s Aristotle’s lantern or a sea star pushing out its stomach, so players blurt “starfish” or “sea urchin.” But the question wants the whole phylum, and naming one animal is wrong. Cnidarians are the other trap: jellyfish, corals, and sea anemones are also radially symmetrical sea animals, but they have stinging cells instead of tube feet and spiny skeletal plates.",
        "fix": "Listen for “this phylum” or “these animals” and give the group’s name. Tube feet, a water vascular system, five-part symmetry, and “spiny skin” mean echinoderms; stinging cells, jellies, and polyps mean cnidarians.",
        "line": "Real answer line: <b><u>Echinoderms</u></b> (accept <u>Echinodermata</u>; do not accept a single member such as “starfish”)"
    },
    "tests": {
        "right": [
            "Echinoderms",
            "echinoderm",
            "Echinodermata",
            "Echinoderns",
            "Phylum Echinodermata"
        ],
        "prompt": [],
        "wrong": [
            "Cnidarians",
            "Mollusks",
            "Starfish",
            "Sea urchins",
            "Chordates",
            "Arthropods"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
