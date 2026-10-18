import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

CE = "_Caenorhabditis elegans_ [“SEE-noh-rab-DY-tiss EL-uh-ganz”]"

data = {
    "id": "nematodes",
    "name": "Nematodes",
    "mono": "NEM",
    "category": "Biology",
    "qbCategory": "Science · Biology",
    "kicker": "Unsegmented roundworms · Includes the famous lab worm C. elegans",
    "dates": "First animal genome sequenced: C. elegans, 1998",
    "briefing": "Nematodes, or roundworms, are smooth, unsegmented worms named for the Greek word for “thread,” and they may be the most numerous animals on Earth, living in soil, in oceans, and inside plants and animals. Some, like hookworms and pinworms, are parasites, but the see-through soil worm _Caenorhabditis elegans_ is a lab superstar: it was the first animal to have its whole genome read, and studying it has led to several Nobel Prizes.",
    "answerHtml": "<b><u>Nematodes</u></b> (accept <u>roundworms</u> or <u>Nematoda</u>; prompt on <u>worms</u>; do not accept “flatworms” or “annelids”)",
    "accept": [
        "nematodes",
        "nematode",
        "nematoda",
        "nemata",
        "roundworms",
        "roundworm",
        "round worms",
        "round worm",
        "phylum nematoda"
    ],
    "prompt": [
        "worms",
        "worm",
        "helminths",
        "helminth",
        "parasitic worms",
        "pseudocoelomates",
        "ecdysozoa",
        "ecdysozoans"
    ],
    "reject": [
        "flatworms",
        "flatworm",
        "platyhelminthes",
        "annelids",
        "annelid",
        "annelida",
        "segmented worms",
        "earthworms",
        "earthworm",
        "tapeworms",
        "tapeworm",
        "flukes",
        "planarians",
        "leeches",
        "nemerteans",
        "nemertea",
        "ribbon worms",
        "nematocysts",
        "nematocyst",
        "nematomorpha",
        "horsehair worms",
        "ringworm",
        "ringworms",
        "arthropods",
        "rotifers",
        "c elegans",
        "caenorhabditis elegans"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Nematode",
    "qb": {
        "q": "nematode",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "Victor Ambros and Gary Ruvkun shared the 2024 Nobel Prize in Physiology or Medicine for discovering microRNAs, tiny gene-controlling RNA molecules, in a species of these animals. The first microRNA they found, lin-4, controls the timing of that species’ growth through its larval stages.",
            "r": "These animals have a tough outer cuticle that they shed as they grow. For 10 points, name this phylum of unsegmented worms that includes hookworms."
        },
        {
            "p": "Andrew Fire and Craig Mello won a 2006 Nobel Prize after they injected double-stranded RNA into one of these animals and found that it silenced the matching gene, a process called RNA interference. Their test subject was a see-through species about one millimeter long that eats bacteria in soil.",
            "r": "Members of this phylum have a body cavity called a pseudocoelom [“SOO-doh-SEE-lum”]. For 10 points, name this phylum of worms that includes the lab species " + CE + "."
        },
        {
            "p": "John Sulston watched every cell division in a living species of these animals to map its complete cell lineage, showing that exactly 131 cells die by programmed cell death as a hermaphrodite develops. Sydney Brenner, who had chosen that species as a model organism, shared a 2002 Nobel Prize with Sulston and H. Robert Horvitz.",
            "r": "That species’ adult hermaphrodites have exactly 959 body cells. For 10 points, name this phylum of unsegmented worms that also includes hookworms and pinworms."
        },
        {
            "p": "Canisters holding these animals survived the 2003 disaster in which the space shuttle _Columbia_ broke apart over Texas, and they were found alive in the wreckage. The species on that flight grows from an egg into an adult in about three days, one reason it is popular in labs.",
            "r": "That species, _Caenorhabditis elegans_, is a tiny soil worm. For 10 points, name this phylum of cylindrical, unsegmented worms."
        },
        {
            "p": "In 2011, scientists described the “devil worm,” _Halicephalobus mephisto_, a member of this phylum found living more than a kilometer underground in a South African gold mine. Nathan Cobb, who studied these animals for the U.S. Department of Agriculture, wrote that a film of them would still outline Earth’s landscape if everything else vanished.",
            "r": "These animals’ name comes from the Greek word for “thread.” For 10 points, name this phylum of unsegmented worms that includes hookworms and pinworms."
        },
        {
            "p": "William Campbell and Satoshi Ōmura [“OH-moo-rah”] shared a 2015 Nobel Prize for discovering avermectin, which led to the drug ivermectin. That drug is given out free in many countries to fight river blindness, a disease caused by one of these worms and spread by the bites of black flies.",
            "r": "Other members of this phylum, spread by mosquitoes, cause elephantiasis. For 10 points, name this phylum of worms that includes hookworms and heartworms."
        },
        {
            "p": "The Carter Center, founded by former president Jimmy Carter, has led a campaign that cut cases of a disease caused by one of these worms from about 3.5 million in 1986 to only a handful a year by the 2020s. People catch that disease, Guinea worm disease, by drinking water containing tiny water fleas that carry its larvae.",
            "r": "Hookworms and pinworms also belong to this phylum. For 10 points, name this phylum of unsegmented worms with a tough outer cuticle."
        },
        {
            "p": "John D. Rockefeller funded a 1909 commission to fight a disease caused by one kind of these worms across the American South, where many children went barefoot. That kind’s genus name, _Necator_, means “killer,” and its young larvae enter the body through the skin of bare feet.",
            "r": "That kind is commonly called the hookworm. For 10 points, name this phylum of worms that also includes the lab species _C. elegans_."
        },
        {
            "p": "Eating undercooked pork or wild game can cause trichinosis [“trik-ih-NOH-sis”], a disease caused by members of this phylum whose larvae curl up inside tiny cysts in muscle. Those parasites belong to the genus _Trichinella_ [“trik-ih-NEL-uh”], whose name refers to their hair-like thinness.",
            "r": "Another member of this phylum, _Ascaris_ [“ASS-kuh-riss”], can grow longer than a foot. For 10 points, name this phylum of unsegmented worms that also includes hookworms."
        },
        {
            "p": "Along with arthropods, these animals are placed in a group called Ecdysozoa [“ek-dih-soh-ZOH-uh”] because they molt their outer covering as they grow. Biologists call them pseudocoelomates [“soo-doh-SEE-loh-mayts”], since their fluid-filled body cavity is only partly lined by tissue from the embryo’s middle layer, the mesoderm.",
            "r": "Their muscles run only lengthwise, so they move by whipping their bodies back and forth. For 10 points, name this phylum of unsegmented worms that includes hookworms."
        },
        {
            "p": "Cynthia Kenyon found that a single change in a gene called daf-2 roughly doubled the lifespan of a species of these animals. When food runs short, young members of that species can enter a tough, resting “dauer” [“DOW-er”] stage, named for a German word meaning “lasting.”",
            "r": "Hermaphrodites of that species, _C. elegans_, have exactly 302 nerve cells. For 10 points, name this phylum of worms that includes hookworms and pinworms."
        },
        {
            "p": "In 1986, a team including John White and Sydney Brenner published the first complete wiring diagram of an animal’s nervous system, mapping the connections among the nerve cells of a species of these animals. In 1998, that species became the first animal to have its complete genome sequenced.",
            "r": "That species is a see-through soil worm about one millimeter long. For 10 points, name this phylum of unsegmented worms that also includes hookworms."
        },
        {
            "p": "Root-knot species of these animals cause swellings called galls on plant roots, and the soybean cyst species is one of the worst pests of soybean crops in the United States. Farmers sometimes plant marigolds, whose roots release chemicals that are toxic to these tiny soil animals.",
            "r": "Others are parasites of people, such as hookworms and pinworms. For 10 points, name this phylum of unsegmented worms."
        },
        {
            "p": "Martin Chalfie shared the 2008 Nobel Prize in Chemistry after he made a jellyfish’s green fluorescent protein glow inside the nerve cells of a species of these see-through animals. Unlike flatworms, these animals have a complete digestive tract, with food entering the mouth and wastes leaving through a separate opening.",
            "r": "Most have thread-shaped bodies tapered at both ends. For 10 points, name this phylum of unsegmented worms that includes _C. elegans_."
        },
        {
            "p": "In 2023, scientists reported reviving tiny members of this phylum that had been frozen in Siberian permafrost for more than 40,000 years. Despite its name, the skin infection ringworm is caused by a fungus, not by one of these animals.",
            "r": "Mosquitoes spread one of these animals, the heartworm, to dogs. For 10 points, name this phylum of worms that also includes hookworms and pinworms."
        }
    ],
    "clues": [
        {
            "id": "unsegmented-worms",
            "tier": "giveaway",
            "t": "A phylum of smooth, unsegmented worms with cylindrical bodies tapered at both ends",
            "k": ["unsegmented", "cylindrical", "tapered"],
            "n": 0
        },
        {
            "id": "parasites",
            "tier": "giveaway",
            "t": "Parasitic members include hookworms, pinworms, and the heartworms that mosquitoes spread to dogs",
            "k": ["hookworms", "pinworms", "heartworms", "parasitic"],
            "n": 0
        },
        {
            "id": "c-elegans",
            "tier": "giveaway",
            "t": "The tiny see-through soil worm _Caenorhabditis elegans_ (_C. elegans_) is a famous laboratory model organism",
            "k": ["caenorhabditis elegans", "c. elegans", "model organism"],
            "n": 0
        },
        {
            "id": "everywhere",
            "tier": "giveaway",
            "t": "Found in soil, in oceans, and inside plants and animals; they may be the most numerous animals on Earth",
            "k": ["most numerous", "soil"],
            "n": 0
        },
        {
            "id": "cuticle-molting",
            "tier": "middle",
            "t": "Covered by a tough outer cuticle that they shed (molt) as they grow, which puts them in the group Ecdysozoa with arthropods",
            "k": ["cuticle", "molt", "ecdysozoa", "arthropods"],
            "n": 0
        },
        {
            "id": "pseudocoelom",
            "tier": "middle",
            "t": "Their fluid-filled body cavity, a pseudocoelom, is only partly lined by mesoderm, so they are called pseudocoelomates",
            "k": ["pseudocoelomates", "pseudocoelom", "mesoderm"],
            "n": 0
        },
        {
            "id": "digestive-tract",
            "tier": "middle",
            "t": "Unlike flatworms, they have a complete digestive tract with two openings: a mouth at one end and an anus at the other",
            "k": ["complete digestive tract", "two openings", "flatworms"],
            "n": 0,
            "rabbit": "Flatworms"
        },
        {
            "id": "lengthwise-muscles",
            "tier": "middle",
            "t": "Have only lengthwise (longitudinal) muscles, so they move by whipping back and forth; they have no circulatory or respiratory system",
            "k": ["longitudinal", "lengthwise", "whipping"],
            "n": 0
        },
        {
            "id": "thread-name",
            "tier": "middle",
            "t": "Their name comes from the Greek word for “thread”",
            "k": ["thread", "greek"],
            "n": 0
        },
        {
            "id": "cell-count",
            "tier": "middle",
            "t": "Adult _C. elegans_ hermaphrodites have exactly 959 body cells, including 302 nerve cells",
            "k": ["959", "302", "hermaphrodites"],
            "n": 0
        },
        {
            "id": "ascaris",
            "tier": "middle",
            "t": "_Ascaris_ causes one of the most common worm infections in the world and can grow longer than a foot",
            "k": ["ascaris", "longer than a foot"],
            "n": 0
        },
        {
            "id": "elephantiasis",
            "tier": "middle",
            "t": "Mosquito-borne filarial worms cause elephantiasis (lymphatic filariasis), severe swelling of the legs",
            "k": ["elephantiasis", "filarial", "mosquito"],
            "n": 0
        },
        {
            "id": "microrna",
            "tier": "power",
            "t": "Victor Ambros and Gary Ruvkun won the 2024 Nobel Prize for discovering microRNAs, starting with lin-4, in _C. elegans_",
            "k": ["ambros", "ruvkun", "micrornas", "lin-4"],
            "n": 0
        },
        {
            "id": "rnai",
            "tier": "power",
            "t": "Andrew Fire and Craig Mello won the 2006 Nobel Prize for RNA interference, found by injecting double-stranded RNA into _C. elegans_",
            "k": ["andrew fire", "mello", "rna interference", "double-stranded"],
            "n": 0,
            "rabbit": "RNA"
        },
        {
            "id": "lineage-2002",
            "tier": "power",
            "t": "John Sulston mapped the complete cell lineage of _C. elegans_, in which 131 cells die by programmed cell death; he shared the 2002 Nobel Prize with Sydney Brenner and H. Robert Horvitz",
            "k": ["sulston", "brenner", "horvitz", "131"],
            "n": 0,
            "rabbit": "Apoptosis"
        },
        {
            "id": "connectome-genome",
            "tier": "power",
            "t": "_C. elegans_ had the first complete wiring diagram of an animal’s nervous system (1986) and the first fully sequenced animal genome (1998)",
            "k": ["wiring diagram", "genome", "1986", "1998"],
            "n": 0
        },
        {
            "id": "columbia",
            "tier": "power",
            "t": "_C. elegans_ worms survived the 2003 _Columbia_ space shuttle disaster and were found alive in the wreckage",
            "k": ["columbia", "space shuttle", "2003"],
            "n": 0
        },
        {
            "id": "kenyon-dauer",
            "tier": "power",
            "t": "Cynthia Kenyon doubled the lifespan of _C. elegans_ with a change in the gene daf-2; hungry larvae can enter a tough “dauer” (German for “lasting”) stage",
            "k": ["kenyon", "daf-2", "dauer", "lifespan"],
            "n": 0
        },
        {
            "id": "chalfie-gfp",
            "tier": "power",
            "t": "Martin Chalfie made green fluorescent protein glow in the nerve cells of _C. elegans_ and shared the 2008 Nobel Prize in Chemistry",
            "k": ["chalfie", "green fluorescent protein", "2008"],
            "n": 0
        },
        {
            "id": "devil-worm",
            "tier": "power",
            "t": "The “devil worm,” _Halicephalobus mephisto_, lives over a kilometer underground in a South African gold mine; Nathan Cobb wrote that a film of them would still outline Earth’s landscape",
            "k": ["devil worm", "mephisto", "gold mine", "nathan cobb"],
            "n": 0
        },
        {
            "id": "ivermectin",
            "tier": "power",
            "t": "William Campbell and Satoshi Ōmura won the 2015 Nobel Prize for avermectin; the drug ivermectin fights river blindness, which black flies spread",
            "k": ["ivermectin", "river blindness", "black flies", "ōmura"],
            "n": 0
        },
        {
            "id": "guinea-worm",
            "tier": "power",
            "t": "The Carter Center’s campaign cut Guinea worm disease from about 3.5 million cases (1986) to a handful a year; people catch it from water fleas in drinking water",
            "k": ["guinea worm", "carter center", "water fleas"],
            "n": 0
        },
        {
            "id": "hookworm-rockefeller",
            "tier": "power",
            "t": "John D. Rockefeller funded a 1909 campaign against hookworm in the American South; hookworm larvae enter through bare feet, and the genus name _Necator_ means “killer”",
            "k": ["rockefeller", "1909", "necator", "bare feet"],
            "n": 0
        },
        {
            "id": "trichinosis",
            "tier": "power",
            "t": "_Trichinella_ worms cause trichinosis, caught from undercooked pork or wild game; their larvae curl up in tiny cysts in muscle",
            "k": ["trichinosis", "trichinella", "pork"],
            "n": 0
        },
        {
            "id": "plant-pests",
            "tier": "power",
            "t": "Root-knot species cause galls on plant roots, the soybean cyst species is a major U.S. crop pest, and marigold roots release chemicals toxic to them",
            "k": ["root-knot", "galls", "soybean cyst", "marigold"],
            "n": 0
        },
        {
            "id": "permafrost",
            "tier": "power",
            "t": "In 2023, scientists revived some that had been frozen in Siberian permafrost for over 40,000 years; ringworm, despite its name, is a fungus, not one of them",
            "k": ["permafrost", "siberian", "ringworm"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Roundworms, flatworms, or annelids?",
        "body": "Three phyla of worms show up in quiz bowl, and tossups on nematodes often name one of the others to rule it out. Flatworms (Platyhelminthes), like tapeworms and planarians, are flat and have a gut with only one opening, while annelids, like earthworms and leeches, are built from ring-shaped segments. Players also mix up nematodes with nematocysts, the stinging cells of jellyfish, and with ringworm, which is a fungus.",
        "fix": "Unsegmented, cylindrical bodies, a pseudocoelom, a gut with two openings, molting, hookworms, or _C. elegans_ mean nematodes (roundworms). Flat bodies or tapeworms mean flatworms; ring-shaped segments, earthworms, or leeches mean annelids.",
        "line": "Real answer line: <b><u>Nematodes</u></b> (accept <u>roundworms</u> or <u>Nematoda</u>; prompt on <u>worms</u>; do not accept “flatworms” or “annelids”)"
    },
    "tests": {
        "right": [
            "Nematodes",
            "roundworms",
            "Nematoda",
            "Nematods",
            "round worm",
            "phylum Nematoda"
        ],
        "prompt": [
            "Worms",
            "Helminths"
        ],
        "wrong": [
            "Flatworms",
            "Annelids",
            "Earthworms",
            "Nematocysts",
            "Ringworm",
            "Tapeworms",
            "C. elegans"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
