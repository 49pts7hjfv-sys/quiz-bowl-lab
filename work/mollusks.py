import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "mollusks",
    "name": "Mollusks",
    "mono": "MOL",
    "category": "Biology",
    "qbCategory": "Science · Biology",
    "kicker": "Soft-bodied invertebrates · Snails, clams, squids, and octopuses",
    "dates": "Second-largest animal phylum, after arthropods",
    "briefing": "Mollusks are soft-bodied animals, and many of them build hard shells to protect themselves: snails, clams, oysters, and scallops all belong to this huge group. Octopuses and squids are mollusks too, and they are among the smartest invertebrates on Earth, able to change color in a flash and squirt ink to escape. Most mollusks share a muscular foot and a skin-like mantle that makes the shell, and many scrape up food with a rough, toothy tongue called a radula.",
    "answerHtml": "<b><u>Mollusks</u></b> (accept <u>Mollusca</u> or <u>molluscs</u>; do not accept a single class such as “cephalopods”)",
    "accept": [
        "mollusks",
        "mollusk",
        "molluscs",
        "mollusc",
        "mollusca",
        "phylum mollusca"
    ],
    "prompt": [],
    "reject": [
        "echinoderms",
        "echinoderm",
        "echinodermata",
        "cnidarians",
        "cnidaria",
        "arthropods",
        "arthropoda",
        "annelids",
        "annelida",
        "crustaceans",
        "brachiopods",
        "brachiopoda",
        "nematodes",
        "sponges",
        "chordates",
        "cephalopods",
        "cephalopoda",
        "gastropods",
        "gastropoda",
        "bivalves",
        "bivalvia",
        "octopus",
        "octopuses",
        "squid",
        "squids",
        "snails",
        "snail",
        "slugs",
        "clams",
        "clam",
        "oysters",
        "mussels",
        "shellfish"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Mollusca",
    "qb": {
        "q": "mollusk",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "Alan Hodgkin and Andrew Huxley shared a 1963 Nobel Prize for explaining nerve impulses, using a giant nerve fiber from one member of this phylum. Another member of this phylum, the sea hare Aplysia, helped Eric Kandel study how memories form.",
            "r": "Members of this phylum include squids and snails. For 10 points, name this phylum of soft-bodied animals."
        },
        {
            "p": "The Phoenicians crushed huge numbers of murex, members of this phylum, to make Tyrian purple, a dye so costly that it became the color of royalty. Many members of this phylum scrape up food with a radula [“RAJ-uh-luh”], a ribbon-like tongue covered with tiny teeth.",
            "r": "Most of its members have a muscular foot and a mantle. For 10 points, name this phylum that includes snails, clams, and octopuses."
        },
        {
            "p": "As they develop, some members of this phylum twist their bodies 180 degrees in a process called torsion, which moves the mantle cavity and anus up over the head. Those members, the gastropods, are the largest class of this phylum.",
            "r": "For 10 points, name this phylum of soft-bodied animals that includes snails, slugs, and octopuses."
        },
        {
            "p": "Chitons [“KY-tunz”], members of this phylum covered by eight overlapping shell plates, have teeth capped with the iron mineral magnetite. Bivalves are the only major class of this phylum that has no radula, the toothy, ribbon-like tongue that others use to scrape up food.",
            "r": "Its name comes from a Latin word meaning “soft.” For 10 points, name this phylum that includes octopuses and snails."
        },
        {
            "p": "Engineer Marc Brunel based his tunneling shield for the Thames Tunnel on the shipworm, a wood-boring member of this phylum that damaged wooden ships for centuries. Clams, oysters, and mussels are members of this phylum with two hinged shells.",
            "r": "For 10 points, name this phylum of soft-bodied animals that also includes squids and snails."
        },
        {
            "p": "Scallops, members of this phylum, can have up to 200 tiny eyes along the edge of their mantle, and each eye focuses light mainly with a curved mirror at its back. Like other bivalves in this phylum, scallops filter food from the water with their gills.",
            "r": "For 10 points, name this phylum of soft-bodied animals that also includes snails, slugs, and squids."
        },
        {
            "p": "The blood of some members of this phylum is blue because it carries oxygen with hemocyanin [“hee-moh-SY-uh-nin”], a protein that uses copper instead of iron, and the octopus pumps that blood with three hearts. Unlike most members of this phylum, cephalopods have a closed circulatory system.",
            "r": "Its members have a mantle and often a shell. For 10 points, name this phylum that includes octopuses, squids, and snails."
        },
        {
            "p": "Extinct members of this phylum called ammonites are common index fossils, and their living relative, the chambered nautilus, controls its buoyancy with a tube called the siphuncle [“SY-fung-kul”]. Cephalopods in this phylum shoot water out of a siphon to jet away from danger.",
            "r": "Gastropods and bivalves belong to it too. For 10 points, name this phylum that includes octopuses, snails, and clams."
        },
        {
            "p": "Like annelid worms, many members of this phylum begin life as a tiny swimming larva called a trochophore [“TROCK-uh-for”], and some then pass through a second larval stage called a veliger [“VEL-uh-jer”]. Members of this phylum have a mantle that can build a shell of calcium carbonate.",
            "r": "Clams and oysters belong to it. For 10 points, name this phylum of soft-bodied animals that includes squids and snails."
        },
        {
            "p": "Some members of the genus Conus in this phylum hunt fish by firing harpoon-like, venom-filled teeth, and a painkiller called ziconotide was developed from that venom. Gastropods, the largest class of this phylum, glide along on a single muscular foot.",
            "r": "Its members include slugs, clams, and octopuses. For 10 points, name this phylum of soft-bodied invertebrates."
        },
        {
            "p": "Some brightly colored sea slugs in this phylum, called nudibranchs [“NOO-dih-branks”], store the stinging cells of the sea anemones and other cnidarians they eat and use them for their own defense. Members of this phylum, from slugs to squids, have a fold of tissue called the mantle.",
            "r": "Its members have a muscular foot. For 10 points, name this phylum of soft-bodied invertebrates that includes snails and clams."
        },
        {
            "p": "In 1893, Kokichi Mikimoto produced the first cultured pearls by placing an irritant inside oysters, which coated it with layers of nacre [“NAY-ker”], or mother-of-pearl. Oysters belong to the class of this phylum called bivalves, which have two hinged shells.",
            "r": "For 10 points, name this phylum of soft-bodied animals that includes clams, snails, and octopuses."
        },
        {
            "p": "Pet birds are often given cuttlebones, the internal shells of some members of this phylum, and the ink of those same animals gave its name to the reddish-brown color sepia. Octopuses and squids in this phylum change color using skin cells called chromatophores [“kroh-MAT-uh-forz”].",
            "r": "This phylum also includes snails, slugs, and clams. For 10 points, name this second-largest animal phylum, after the arthropods."
        },
        {
            "p": "Zebra mussels, invasive members of this phylum that reached the Great Lakes in the late 1980s in ships’ ballast water, clog water intake pipes and crowd out native species. Members of this phylum called bivalves have two hinged shells held shut by strong adductor muscles.",
            "r": "Squids and snails are members too. For 10 points, name this phylum of soft-bodied animals."
        },
        {
            "p": "The colossal squid, the heaviest known invertebrate and a member of this phylum, has the largest eyes of any animal. The study of animals in this phylum is called malacology, while the study of their shells is called conchology [“kong-KOL-uh-jee”].",
            "r": "For 10 points, name this phylum of soft-bodied animals that includes octopuses, snails, and clams."
        }
    ],
    "clues": [
        {
            "id": "members",
            "tier": "giveaway",
            "t": "Phylum including snails, slugs, clams, oysters, squids, and octopuses",
            "k": ["snails", "clams", "squids", "octopuses"],
            "n": 0
        },
        {
            "id": "soft",
            "tier": "giveaway",
            "t": "Its name comes from a Latin word meaning “soft”",
            "k": ["soft", "latin"],
            "n": 0
        },
        {
            "id": "body-plan",
            "tier": "giveaway",
            "t": "Body plan: a muscular foot, a mass of internal organs, and a fold of tissue called the mantle",
            "k": ["muscular foot", "mantle"],
            "n": 0
        },
        {
            "id": "shell",
            "tier": "giveaway",
            "t": "Many have a hard shell of calcium carbonate made by the mantle",
            "k": ["shell", "calcium carbonate"],
            "n": 0
        },
        {
            "id": "second-largest",
            "tier": "giveaway",
            "t": "The second-largest animal phylum, after the arthropods",
            "k": ["second-largest", "arthropods"],
            "n": 0
        },
        {
            "id": "radula",
            "tier": "middle",
            "t": "Most scrape up food with a radula, a ribbon-like tongue covered with tiny teeth; bivalves have none",
            "k": ["radula", "teeth"],
            "n": 0
        },
        {
            "id": "classes",
            "tier": "middle",
            "t": "Main classes: gastropods (snails and slugs, the largest class), bivalves (clams and oysters), and cephalopods (squids and octopuses)",
            "k": ["gastropods", "bivalves", "cephalopods"],
            "n": 0
        },
        {
            "id": "bivalves",
            "tier": "middle",
            "t": "Bivalves have two hinged shells held shut by adductor muscles and filter food with their gills",
            "k": ["hinged", "adductor", "gills"],
            "n": 0
        },
        {
            "id": "cephalopods",
            "tier": "middle",
            "t": "Cephalopods are the smartest invertebrates; they jet away by squirting water out of a siphon",
            "k": ["siphon", "smartest", "jet"],
            "n": 0
        },
        {
            "id": "ink-color",
            "tier": "middle",
            "t": "Octopuses (eight arms) and squids (eight arms plus two tentacles) squirt ink and change color with chromatophores",
            "k": ["chromatophores", "ink", "tentacles"],
            "n": 0
        },
        {
            "id": "hemocyanin",
            "tier": "middle",
            "t": "Octopuses have three hearts and blue blood carrying copper-based hemocyanin; cephalopods have closed circulation, while most others have open circulation",
            "k": ["hemocyanin", "three hearts", "copper"],
            "n": 0
        },
        {
            "id": "pearls",
            "tier": "middle",
            "t": "Oysters make pearls by coating an irritant with nacre (mother-of-pearl); Kokichi Mikimoto first cultured pearls in 1893",
            "k": ["pearls", "nacre", "mikimoto"],
            "n": 0
        },
        {
            "id": "malacology",
            "tier": "middle",
            "t": "Malacology is the study of these animals; conchology is the study of their shells",
            "k": ["malacology", "conchology"],
            "n": 0
        },
        {
            "id": "torsion",
            "tier": "power",
            "t": "Gastropods twist 180 degrees as they develop (torsion), moving the mantle cavity over the head",
            "k": ["torsion", "180 degrees"],
            "n": 0
        },
        {
            "id": "trochophore",
            "tier": "power",
            "t": "Many start life as a trochophore larva, like annelid worms, and some then become veligers",
            "k": ["trochophore", "veligers", "annelid"],
            "n": 0
        },
        {
            "id": "chitons",
            "tier": "power",
            "t": "Chitons have eight overlapping shell plates and teeth capped with the iron mineral magnetite",
            "k": ["chitons", "magnetite", "eight overlapping"],
            "n": 0
        },
        {
            "id": "squid-axon",
            "tier": "power",
            "t": "Alan Hodgkin and Andrew Huxley used the squid’s giant nerve fiber (axon) to explain nerve impulses, winning a 1963 Nobel Prize",
            "k": ["hodgkin", "huxley", "giant nerve fiber"],
            "n": 0,
            "rabbit": "Neurons"
        },
        {
            "id": "aplysia",
            "tier": "power",
            "t": "Eric Kandel studied how memories form in the sea hare Aplysia (2000 Nobel Prize)",
            "k": ["kandel", "aplysia", "memories"],
            "n": 0
        },
        {
            "id": "tyrian-purple",
            "tier": "power",
            "t": "The Phoenicians made Tyrian purple, the royal dye, from murex sea snails",
            "k": ["tyrian purple", "murex", "phoenicians"],
            "n": 0
        },
        {
            "id": "shipworm",
            "tier": "power",
            "t": "Wood-boring shipworms inspired Marc Brunel’s tunneling shield for the Thames Tunnel",
            "k": ["shipworms", "marc brunel", "thames tunnel"],
            "n": 0
        },
        {
            "id": "scallop-eyes",
            "tier": "power",
            "t": "Scallops can have up to 200 eyes, each focusing light mainly with a curved mirror at its back",
            "k": ["scallops", "curved mirror", "200"],
            "n": 0
        },
        {
            "id": "nautilus",
            "tier": "power",
            "t": "The chambered nautilus controls buoyancy with a tube called the siphuncle; extinct ammonites are index fossils",
            "k": ["nautilus", "siphuncle", "ammonites"],
            "n": 0
        },
        {
            "id": "cone-snails",
            "tier": "power",
            "t": "Some cone snails (genus Conus) harpoon fish with venom; the painkiller ziconotide was developed from it",
            "k": ["conus", "ziconotide", "venom"],
            "n": 0
        },
        {
            "id": "nudibranchs",
            "tier": "power",
            "t": "Nudibranchs (sea slugs) store the stinging cells of the cnidarians they eat",
            "k": ["nudibranchs", "stinging cells"],
            "n": 0,
            "rabbit": "Cnidarians"
        },
        {
            "id": "cuttlefish",
            "tier": "power",
            "t": "Cuttlefish have an internal cuttlebone; their ink gave its name to the color sepia",
            "k": ["cuttlebone", "sepia"],
            "n": 0
        },
        {
            "id": "zebra-mussels",
            "tier": "power",
            "t": "Invasive zebra mussels reached the Great Lakes in the late 1980s in ships’ ballast water",
            "k": ["zebra mussels", "ballast", "great lakes"],
            "n": 0
        },
        {
            "id": "colossal-squid",
            "tier": "power",
            "t": "The colossal squid is the heaviest known invertebrate and has the largest eyes of any animal",
            "k": ["colossal squid", "heaviest", "largest eyes"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Phylum, not class",
        "body": "Many clues describe just one class, like cephalopods for octopuses and squids, gastropods for snails, or bivalves for clams, and some tossups ask for those classes instead, so listen for “this phylum” versus “this class.” Brachiopods are the other trap: these “lamp shells” have two shells and look like clams, but they belong to a completely different phylum.",
        "fix": "If the question asks for the phylum, or mixes clues about snails, clams, and squids, say mollusks. Arms, ink, and jet propulsion alone may mean cephalopods; two shells on the top and bottom (instead of left and right) mean brachiopods.",
        "line": "Real answer line: <b><u>Mollusks</u></b> (accept <u>Mollusca</u> or <u>molluscs</u>; do not accept a single class such as “cephalopods”)"
    },
    "tests": {
        "right": [
            "Mollusks",
            "mollusk",
            "Molluscs",
            "Mollusca",
            "Molusks"
        ],
        "prompt": [],
        "wrong": [
            "Echinoderms",
            "Arthropods",
            "Cephalopods",
            "Octopus",
            "Brachiopods",
            "Annelids"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
