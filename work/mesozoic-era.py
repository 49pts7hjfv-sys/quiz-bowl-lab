import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TIP = "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."

data = {
    "id": "mesozoic-era",
    "name": "Mesozoic Era",
    "mono": "MZ",
    "category": "Earth Science",
    "qbCategory": "Science · Other Science (Earth Science)",
    "kicker": "The “Age of Reptiles,” about 252 to 66 million years ago · Home of the dinosaurs",
    "dates": "About 252 to 66 million years ago",
    "briefing": "The Mesozoic Era, from about 252 to 66 million years ago, is nicknamed the “Age of Reptiles”: dinosaurs ruled the land, pterosaurs flew overhead, and giant marine reptiles swam the seas. It is split into three periods, the Triassic, Jurassic, and Cretaceous. It began right after the largest mass extinction in Earth’s history and ended when an asteroid struck Mexico’s Yucatán Peninsula, wiping out every dinosaur except the birds.",
    "answerHtml": "<b><u>Mesozoic</u></b> Era (prompt on <u>Age of Reptiles</u> or <u>Age of Dinosaurs</u>; do not accept “Triassic,” “Jurassic,” “Cretaceous,” “Paleozoic,” or “Cenozoic”)",
    "accept": [
        "mesozoic",
        "mesozoic era",
        "the mesozoic",
        "the mesozoic era",
        "mesozoic erathem",
        "mesozoic period",
        "mesozoic times"
    ],
    "prompt": [
        "age of reptiles",
        "the age of reptiles",
        "age of dinosaurs",
        "age of the dinosaurs",
        "dinosaur age",
        "dinosaur era"
    ],
    "reject": [
        "triassic",
        "triassic period",
        "jurassic",
        "jurassic period",
        "cretaceous",
        "cretaceous period",
        "paleozoic",
        "paleozoic era",
        "palaeozoic",
        "cenozoic",
        "cenozoic era",
        "cainozoic",
        "precambrian",
        "proterozoic",
        "archean",
        "hadean",
        "phanerozoic",
        "permian",
        "carboniferous",
        "devonian",
        "silurian",
        "ordovician",
        "cambrian",
        "paleogene",
        "neogene",
        "quaternary",
        "tertiary",
        "age of mammals",
        "pangaea"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Mesozoic",
    "qb": {"q": "Mesozoic", "found": 0, "tip": TIP},
    "sample": {"n": 0, "note": "no real tossups checked yet"},
    "tossups": [
        {
            "p": "The English geologist John Phillips named this era in 1840 from Greek words meaning “middle life,” placing it between an era of “ancient life” and one of “new life.” Ammonites, coiled relatives of squid, are used as index fossils to split its rock layers into zones.",
            "r": "Its three periods are the Triassic, Jurassic, and Cretaceous. For 10 points, name this era, nicknamed the “Age of Reptiles.”"
        },
        {
            "p": "Lystrosaurus [“liss-troh-SOR-us”], a stocky, tusked plant-eater, survived the mass extinction that began this era and became one of the most common land animals of its first period. Fossils of Lystrosaurus found in Antarctica, India, and South Africa show that those lands were once joined in the supercontinent Pangaea.",
            "r": "This era ended when an asteroid struck Mexico 66 million years ago. For 10 points, name this era, the “Age of Reptiles.”"
        },
        {
            "p": "In 1977, Geerat Vermeij named a “marine revolution” for this era, after noticing that shell-crushing predators spread during it while snails evolved thicker, spinier shells and clams burrowed deeper. Mosasaurs, plesiosaurs, and ichthyosaurs were giant reptiles that swam in its seas.",
            "r": "Dinosaurs ruled the land during this era. For 10 points, name this era that includes the Triassic, Jurassic, and Cretaceous periods."
        },
        {
            "p": "In 1923, Roy Chapman Andrews’s team found nests of fossil eggs from this era in Mongolia’s Gobi, at a site called the Flaming Cliffs. Scientists later showed that many of those eggs belonged to Oviraptor, whose name means “egg thief,” rather than to Protoceratops.",
            "r": "Non-bird dinosaurs died out at the end of this era. For 10 points, name this era, the “Age of Reptiles,” which followed the Paleozoic."
        },
        {
            "p": "In 1834, Friedrich von Alberti named the first period of this era for a set of three rock layers in Germany. Hundreds of skeletons of Coelophysis [“see-loh-FY-sis”], a slender, early meat-eater, were found together at Ghost Ranch in New Mexico, in rocks from that first period.",
            "r": "That first period, the Triassic, was followed by the Jurassic and Cretaceous. For 10 points, name this era, the “Age of Reptiles.”"
        },
        {
            "p": "In 1822, the Belgian geologist Jean d’Omalius d’Halloy named the last period of this era after the Latin word for chalk. Late in that period, a shallow sea called the Western Interior Seaway split North America into eastern and western landmasses.",
            "r": "That last period, the Cretaceous, ended with the extinction of the non-bird dinosaurs. For 10 points, name this era, which came between the Paleozoic and the Cenozoic."
        },
        {
            "p": "In 1980, Luis and Walter Alvarez argued that a thin, iridium-rich clay layer marking the end of this era was left by an asteroid impact. Grains of shocked quartz in that layer also point to an impact, and the crater, Chicxulub [“CHEEK-shoo-loob”], was later found buried beneath Mexico’s Yucatán Peninsula.",
            "r": "That impact, 66 million years ago, wiped out the non-bird dinosaurs. For 10 points, name this era that began about 252 million years ago."
        },
        {
            "p": "This era began right after the largest mass extinction in Earth’s history, nicknamed the “Great Dying,” which wiped out most species in the oceans. Scientists link that disaster to enormous volcanic eruptions in what is now Russia that built the Siberian Traps.",
            "r": "This era ended 66 million years ago with the extinction of the non-bird dinosaurs. For 10 points, name this era, often called the “Age of Reptiles.”"
        },
        {
            "p": "A fossil of Repenomamus, a badger-sized mammal from this era found in China, had the bones of a young Psittacosaurus [“sih-TAK-uh-SOR-us”] in its stomach. Most mammals of this era, though, were small, and many probably came out mainly at night. The earliest mammals appeared during this era’s first period.",
            "r": "Dinosaurs dominated the land during this era. For 10 points, name this era of the Triassic, Jurassic, and Cretaceous periods."
        },
        {
            "p": "Gideon Mantell named Iguanodon in 1825 because its fossil teeth, found in English rocks from this era, looked like a giant iguana’s. In 1854, Benjamin Waterhouse Hawkins built life-size models of Iguanodon and other animals from this era for a London park.",
            "r": "In 1842, Richard Owen named the dinosaurs, which ruled the land during this era. For 10 points, name this era, the “Age of Reptiles.”"
        },
        {
            "p": "Quetzalcoatlus [“ket-sul-koh-AT-lus”], a pterosaur from late in this era found in Texas, had a wingspan of about 10 meters and is one of the largest flying animals ever known. Pterosaurs first took to the air during this era’s first period and died out at its end.",
            "r": "Dinosaurs ruled the land below them. For 10 points, name this era, which included the Triassic, Jurassic, and Cretaceous periods."
        },
        {
            "p": "In 1996, scientists described Sinosauropteryx [“SY-noh-sor-OP-ter-iks”], a small meat-eater from China’s Liaoning Province that was covered in simple, fuzzy feathers. Fossils like it support the idea that birds evolved during this era from small, two-legged meat-eaters called theropods.",
            "r": "Archaeopteryx, an early bird, lived in the middle of this era. For 10 points, name this era, home to the dinosaurs."
        },
        {
            "p": "Charles Darwin called the sudden spread of flowering plants late in this era an “abominable mystery.” Before then, forests in this era were dominated by conifers, cycads, and ginkgoes, and grasses were rare or absent for most of it.",
            "r": "Dinosaurs fed on those plants during this era. For 10 points, name this era, which spanned the Triassic, Jurassic, and Cretaceous periods."
        },
        {
            "p": "For most of this era, Earth had a warm greenhouse climate with no large ice sheets at the poles, and sea levels late in this era were far higher than modern ones. The supercontinent Pangaea broke apart during this era, opening the Atlantic Ocean.",
            "r": "This era came between the Paleozoic and the Cenozoic. For 10 points, name this era, the “Age of Reptiles.”"
        },
        {
            "p": "Mary Anning dug ichthyosaur and plesiosaur skeletons from this era out of the seaside cliffs at Lyme Regis, England, in the early 1800s, and her finds helped show that whole groups of animals could go extinct. Huge marine lizards called mosasaurs ruled the seas near this era’s end.",
            "r": "Dinosaurs ruled the land during this era, which ended 66 million years ago. For 10 points, name this era that includes the Jurassic period."
        }
    ],
    "clues": [
        {"id": "age-of-reptiles", "tier": "giveaway",
         "t": "Nicknamed the “Age of Reptiles” (or “Age of Dinosaurs”), when dinosaurs ruled the land",
         "k": ["age of reptiles", "dinosaurs"], "n": 0},
        {"id": "three-periods", "tier": "giveaway",
         "t": "Made up of three periods: the Triassic, Jurassic, and Cretaceous",
         "k": ["triassic", "jurassic", "cretaceous"], "n": 0, "rabbit": "Jurassic period"},
        {"id": "dates", "tier": "giveaway",
         "t": "Lasted from about 252 to 66 million years ago",
         "k": ["252", "66 million"], "n": 0},
        {"id": "between", "tier": "giveaway",
         "t": "Came after the Paleozoic Era and before the Cenozoic Era",
         "k": ["paleozoic", "cenozoic"], "n": 0},
        {"id": "asteroid-end", "tier": "giveaway",
         "t": "Ended 66 million years ago when an asteroid hit Mexico’s Yucatán Peninsula, killing every dinosaur except the birds",
         "k": ["asteroid", "yucatán", "birds"], "n": 0, "rabbit": "Asteroids"},
        {"id": "middle-life", "tier": "middle",
         "t": "Its name comes from Greek words meaning “middle life”",
         "k": ["middle life", "greek"], "n": 0},
        {"id": "great-dying", "tier": "middle",
         "t": "Began right after the end-Permian mass extinction, the “Great Dying,” the largest in Earth’s history",
         "k": ["great dying", "end-permian", "largest"], "n": 0},
        {"id": "siberian-traps", "tier": "middle",
         "t": "That extinction is linked to enormous eruptions that built the Siberian Traps in Russia",
         "k": ["siberian traps", "eruptions"], "n": 0, "rabbit": "Basalt"},
        {"id": "alvarez", "tier": "middle",
         "t": "Luis and Walter Alvarez (1980) used an iridium-rich clay layer at its end to argue for an asteroid impact; the crater is Chicxulub",
         "k": ["alvarez", "iridium", "chicxulub", "1980"], "n": 0},
        {"id": "pangaea", "tier": "middle",
         "t": "The supercontinent Pangaea broke apart during it, opening the Atlantic Ocean",
         "k": ["pangaea", "atlantic"], "n": 0, "rabbit": "Pangaea"},
        {"id": "marine-reptiles", "tier": "middle",
         "t": "Ichthyosaurs, plesiosaurs, and mosasaurs swam its seas, and pterosaurs flew overhead",
         "k": ["ichthyosaurs", "plesiosaurs", "mosasaurs", "pterosaurs"], "n": 0},
        {"id": "plants", "tier": "middle",
         "t": "Conifers, cycads, and ginkgoes ruled its forests until flowering plants spread in its last period",
         "k": ["conifers", "cycads", "flowering plants"], "n": 0, "rabbit": "Gymnosperms"},
        {"id": "mammals-birds", "tier": "middle",
         "t": "The earliest mammals appeared early in it, and birds evolved from small theropods during it",
         "k": ["mammals", "theropods", "birds"], "n": 0},
        {"id": "ammonites", "tier": "middle",
         "t": "Ammonites, coiled relatives of squid, are index fossils for its rocks and died out at its end",
         "k": ["ammonites", "index fossils"], "n": 0},
        {"id": "greenhouse", "tier": "middle",
         "t": "A warm greenhouse climate with no large polar ice sheets for most of it; late in it, sea levels were far higher than modern ones",
         "k": ["greenhouse", "sea levels"], "n": 0},
        {"id": "phillips", "tier": "power",
         "t": "John Phillips named it in 1840, placing it between the eras of “ancient life” and “new life”",
         "k": ["john phillips", "1840"], "n": 0},
        {"id": "lystrosaurus", "tier": "power",
         "t": "Lystrosaurus survived the extinction at its start; its fossils in Antarctica, India, and South Africa show those lands were once joined",
         "k": ["lystrosaurus", "antarctica"], "n": 0},
        {"id": "vermeij", "tier": "power",
         "t": "Geerat Vermeij (1977) named a “marine revolution” for it: shell-crushing predators spread, and prey grew thicker shells or burrowed deeper",
         "k": ["vermeij", "marine revolution", "1977"], "n": 0},
        {"id": "andrews-eggs", "tier": "power",
         "t": "Roy Chapman Andrews found fossil egg nests at Mongolia’s Flaming Cliffs (1923); many turned out to belong to Oviraptor",
         "k": ["roy chapman andrews", "flaming cliffs", "oviraptor", "1923"], "n": 0},
        {"id": "alberti-coelophysis", "tier": "power",
         "t": "Friedrich von Alberti named its first period, the Triassic, for three rock layers in Germany (1834); Coelophysis skeletons fill New Mexico’s Ghost Ranch",
         "k": ["alberti", "1834", "coelophysis", "ghost ranch"], "n": 0},
        {"id": "omalius-seaway", "tier": "power",
         "t": "Jean d’Omalius d’Halloy named its last period for chalk (1822); the Western Interior Seaway split North America late in it",
         "k": ["omalius", "chalk", "western interior seaway"], "n": 0},
        {"id": "repenomamus", "tier": "power",
         "t": "Repenomamus, a badger-sized mammal from China, was found with a young Psittacosaurus in its stomach",
         "k": ["repenomamus", "psittacosaurus", "badger-sized"], "n": 0},
        {"id": "mantell-owen", "tier": "power",
         "t": "Gideon Mantell named Iguanodon (1825), Richard Owen named the dinosaurs (1842), and Benjamin Waterhouse Hawkins built life-size models for a London park (1854)",
         "k": ["mantell", "iguanodon", "richard owen", "1842"], "n": 0},
        {"id": "quetzalcoatlus", "tier": "power",
         "t": "Quetzalcoatlus, a pterosaur from Texas with a wingspan of about 10 meters, lived late in it",
         "k": ["quetzalcoatlus", "10 meters", "texas"], "n": 0},
        {"id": "sinosauropteryx", "tier": "power",
         "t": "Sinosauropteryx (described in 1996), from China’s Liaoning Province, was a small meat-eater covered in simple feathers",
         "k": ["sinosauropteryx", "liaoning", "1996"], "n": 0, "rabbit": "Birds"},
        {"id": "abominable-mystery", "tier": "power",
         "t": "Charles Darwin called the sudden spread of flowering plants late in it an “abominable mystery”",
         "k": ["abominable mystery", "darwin"], "n": 0},
        {"id": "anning", "tier": "power",
         "t": "Mary Anning found ichthyosaur and plesiosaur skeletons from it at Lyme Regis, England, in the early 1800s",
         "k": ["mary anning", "lyme regis"], "n": 0}
    ],
    "trap": {
        "title": "The era, not a period",
        "body": "Mesozoic tossups are packed with clues about the Triassic, Jurassic, and Cretaceous, so players often name one of those periods instead of the whole era. Those are separate answer lines, and so are the Paleozoic (before it) and the Cenozoic (after it). Nicknames like “Age of Reptiles” earn only a prompt.",
        "fix": "Listen for “this era”: clues that span the first dinosaurs, the Great Dying, and the asteroid impact mean the Mesozoic Era. If you hear “this period” with Stegosaurus or Archaeopteryx, it is the Jurassic; Tyrannosaurus, Triceratops, and the asteroid point to the Cretaceous.",
        "line": "Real answer line: <b><u>Mesozoic</u></b> Era (prompt on Age of Reptiles; do not accept “Triassic,” “Jurassic,” or “Cretaceous”)"
    },
    "tests": {
        "right": ["Mesozoic Era", "Mesozoic", "the Mesozoic", "Mesozoic period", "Mesozoik"],
        "prompt": ["Age of Reptiles", "Age of the dinosaurs"],
        "wrong": ["Jurassic", "Cretaceous period", "Triassic", "Paleozoic", "Cenozoic Era", "Precambrian"]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
