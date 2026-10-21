import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "jurassic-period",
    "name": "Jurassic period",
    "mono": "JUR",
    "category": "Earth Science",
    "qbCategory": "Science · Other Science (Earth Science)",
    "kicker": "Middle period of the Mesozoic Era · Age of Stegosaurus and giant sauropods",
    "dates": "About 201 to 145 million years ago",
    "briefing": "The Jurassic period, from about 201 to 145 million years ago, was the middle part of the Mesozoic Era, when giant long-necked dinosaurs like Brachiosaurus and Diplodocus roamed among ferns, cycads, and conifers. It is named for the Jura Mountains between France and Switzerland, and its rocks in Germany preserved Archaeopteryx, one of the earliest known birds. Meanwhile, the supercontinent Pangaea was breaking apart.",
    "answerHtml": "<b><u>Jurassic</u></b> period (prompt on <u>Mesozoic</u> Era; do not accept “Triassic,” “Cretaceous,” or “Jurassic Park”)",
    "accept": [
        "jurassic",
        "jurassic period",
        "the jurassic",
        "jurassic era",
        "jurassic age",
        "jurassic times",
        "jurassic system",
        "early jurassic",
        "middle jurassic",
        "late jurassic"
    ],
    "prompt": [
        "mesozoic",
        "mesozoic era",
        "age of reptiles",
        "age of dinosaurs",
        "age of the dinosaurs"
    ],
    "reject": [
        "triassic",
        "triassic period",
        "cretaceous",
        "cretaceous period",
        "permian",
        "cambrian",
        "ordovician",
        "silurian",
        "devonian",
        "carboniferous",
        "paleozoic",
        "cenozoic",
        "paleogene",
        "neogene",
        "quaternary",
        "precambrian",
        "jurassic park",
        "jurassic world",
        "jurassic coast",
        "jura",
        "jura mountains",
        "pangaea"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Jurassic",
    "qb": {
        "q": "Jurassic",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "Albert Oppel helped found the use of fossil zones by dividing this period’s rock layers into zones, each marked by a different kind of ammonite. British and German geologists once split this period’s rocks into the Lias, the Dogger, and the Malm.",
            "r": "Alexander von Humboldt named its limestone for the Jura Mountains. For 10 points, name this middle period of the Mesozoic Era."
        },
        {
            "p": "Mary Anning dug ichthyosaur and plesiosaur skeletons out of seaside cliffs at Lyme Regis, part of an English World Heritage coastline that is named for this period. Those marine reptiles swam in the shallow seas that covered much of Europe during this period.",
            "r": "On land, Stegosaurus and Allosaurus lived late in this period. For 10 points, name this period of the Mesozoic Era, about 201 to 145 million years ago."
        },
        {
            "p": "In 1824, William Buckland named Megalosaurus, the first dinosaur to receive a scientific name, from bones found in English rocks from the middle of this period. Christopher Wren built St. Paul’s Cathedral from Portland stone, a limestone that formed late in this period.",
            "r": "This period followed the Triassic. For 10 points, name this period whose name comes from the Jura Mountains."
        },
        {
            "p": "In 1861, a skeleton of Archaeopteryx [“ar-kee-OP-ter-iks”], a feathered animal with teeth and a long bony tail, was found in Germany’s Solnhofen [“ZOHLN-hoh-fen”] limestone, which formed late in this period. The same limestone preserved the small dinosaur Compsognathus and the pterosaur Pterodactylus.",
            "r": "For 10 points, name this middle period of the Mesozoic Era, which came between the Triassic and the Cretaceous."
        },
        {
            "p": "Enormous volcanic eruptions in the Central Atlantic Magmatic Province, which broke out as Pangaea began to split apart, are blamed for the mass extinction that opened this period. With many rivals gone, dinosaurs took over the land during this period.",
            "r": "This period ended about 145 million years ago, when the Cretaceous began. For 10 points, name this period that followed the Triassic."
        },
        {
            "p": "The Morrison Formation, a set of rock layers spread across the western United States, holds many dinosaur fossils from late in this period, including the bones at Dinosaur National Monument. Allosaurus, the state fossil of Utah, was a top predator in the Morrison.",
            "r": "For 10 points, name this period between the Triassic and the Cretaceous, whose name comes from a European mountain range."
        },
        {
            "p": "The spiked tail of Stegosaurus, a plant-eater from this period, is nicknamed a “thagomizer” after a joke in Gary Larson’s comic _The Far Side_. Stegosaurus shared the land with giant long-necked sauropods like Diplodocus.",
            "r": "Archaeopteryx also lived in this period. For 10 points, name this period that followed the Triassic, named for mountains on the border of France and Switzerland."
        },
        {
            "p": "Fossils from shale near Holzmaden, Germany, show that ichthyosaurs living early in this period gave birth to live young in the sea instead of laying eggs. Some of those fossils even preserve the outline of the ichthyosaurs’ skin.",
            "r": "Plesiosaurs and pterosaurs also lived in this period. For 10 points, name this period, about 201 to 145 million years ago."
        },
        {
            "p": "During this period, the supercontinent Pangaea split into Laurasia in the north and Gondwana in the south, and the central Atlantic Ocean began to open between North America and Africa. Warm, shallow seas flooded the edges of the continents.",
            "r": "Stegosaurus and Brachiosaurus lived late in this period. For 10 points, name this period between the Triassic and the Cretaceous."
        },
        {
            "p": "Forests of conifers, cycads, ginkgoes, and tree ferns covered the land during this period, before flowering plants became common. Huge plant-eating sauropods such as Diplodocus fed on that greenery, and no large ice sheets covered the poles.",
            "r": "Archaeopteryx, an early bird, lived near this period’s end. For 10 points, name this period, the middle part of the Mesozoic Era."
        },
        {
            "p": "The honey-colored stone of England’s Cotswold Hills and the city of Bath is oolitic limestone, built from tiny rounded grains that look like fish eggs, which formed in warm, shallow seas during this period. The name “oolite” comes from Greek words for “egg stone.”",
            "r": "On land, this period’s dinosaurs included Allosaurus and Stegosaurus. For 10 points, name this period that followed the Triassic."
        },
        {
            "p": "In 1903, Elmer Riggs named Brachiosaurus [“brak-ee-uh-SOR-us”], or “arm lizard,” from bones found in western Colorado, because its front legs were longer than its back legs. Riggs called it the largest known dinosaur, and it lived late in this period.",
            "r": "Archaeopteryx and Stegosaurus also lived in this period. For 10 points, name this middle period of the Mesozoic Era."
        },
        {
            "p": "During the 1870s “Bone Wars” against his rival Edward Drinker Cope, Othniel Charles Marsh named Stegosaurus, Allosaurus, and Diplodocus from fossils of animals that lived during this period. Many of those fossils came from Como Bluff in Wyoming.",
            "r": "This period came between the Triassic and the Cretaceous. For 10 points, name this period, about 201 to 145 million years ago."
        },
        {
            "p": "The Kimmeridge Clay, a dark rock layer laid down late in this period, is the main source rock for the oil pumped from beneath the North Sea. Its name comes from a village on England’s Dorset coast.",
            "r": "Stegosaurus lived on land at the same time. For 10 points, name this period named for the Jura Mountains."
        },
        {
            "p": "Stegosaurus, Allosaurus, and the giant Brachiosaurus all lived during this period, while ichthyosaurs and plesiosaurs swam in its seas and the early bird Archaeopteryx lived on islands in present-day Germany. Pangaea broke apart during this period.",
            "r": "Michael Crichton named a 1990 novel about cloned dinosaurs for this period. For 10 points, name this middle period of the Mesozoic Era."
        }
    ],
    "clues": [
        {
            "id": "mesozoic-middle",
            "tier": "giveaway",
            "t": "The middle period of the Mesozoic Era, between the Triassic and the Cretaceous",
            "k": ["mesozoic", "triassic", "cretaceous"],
            "n": 0,
            "rabbit": "Mesozoic Era"
        },
        {
            "id": "dates",
            "tier": "giveaway",
            "t": "Lasted from about 201 to 145 million years ago",
            "k": ["201", "145 million"],
            "n": 0
        },
        {
            "id": "jura-mountains",
            "tier": "giveaway",
            "t": "Named for the Jura Mountains on the border of France and Switzerland",
            "k": ["jura mountains", "france", "switzerland"],
            "n": 0
        },
        {
            "id": "crichton",
            "tier": "giveaway",
            "t": "Michael Crichton named his 1990 novel about cloned dinosaurs (a 1993 Steven Spielberg film) after it",
            "k": ["crichton", "cloned dinosaurs", "spielberg"],
            "n": 0
        },
        {
            "id": "dinosaurs",
            "tier": "middle",
            "t": "Home to Stegosaurus, Allosaurus, Brachiosaurus, and Diplodocus",
            "k": ["stegosaurus", "allosaurus", "brachiosaurus", "diplodocus"],
            "n": 0
        },
        {
            "id": "archaeopteryx",
            "tier": "middle",
            "t": "Archaeopteryx, a feathered early bird with teeth, lived late in it; a skeleton was found in Germany’s Solnhofen limestone in 1861",
            "k": ["archaeopteryx", "solnhofen", "1861"],
            "n": 0,
            "rabbit": "Birds"
        },
        {
            "id": "pangaea-breakup",
            "tier": "middle",
            "t": "Pangaea split into Laurasia and Gondwana, and the central Atlantic Ocean began to open",
            "k": ["pangaea", "laurasia", "gondwana", "atlantic"],
            "n": 0,
            "rabbit": "Pangaea"
        },
        {
            "id": "end-triassic",
            "tier": "middle",
            "t": "Began right after the end-Triassic mass extinction, which let dinosaurs take over the land",
            "k": ["mass extinction", "end-triassic"],
            "n": 0
        },
        {
            "id": "plants",
            "tier": "middle",
            "t": "Conifers, cycads, ginkgoes, and ferns filled its forests; flowering plants were not yet common",
            "k": ["conifers", "cycads", "ginkgoes", "ferns"],
            "n": 0
        },
        {
            "id": "marine-reptiles",
            "tier": "middle",
            "t": "Ichthyosaurs and plesiosaurs swam in its seas, and pterosaurs flew overhead",
            "k": ["ichthyosaurs", "plesiosaurs", "pterosaurs"],
            "n": 0
        },
        {
            "id": "ammonites",
            "tier": "middle",
            "t": "Ammonites are index fossils used to divide its rocks into zones",
            "k": ["ammonites", "index fossils"],
            "n": 0
        },
        {
            "id": "humboldt",
            "tier": "power",
            "t": "Alexander von Humboldt named its limestone after the Jura Mountains",
            "k": ["humboldt", "limestone"],
            "n": 0
        },
        {
            "id": "oppel",
            "tier": "power",
            "t": "Albert Oppel split its rocks into ammonite zones; old names for its layers are Lias, Dogger, and Malm",
            "k": ["albert oppel", "oppel", "lias", "dogger", "malm"],
            "n": 0
        },
        {
            "id": "anning",
            "tier": "power",
            "t": "Mary Anning found ichthyosaur and plesiosaur skeletons at Lyme Regis, on an English World Heritage coast named for it",
            "k": ["mary anning", "lyme regis", "world heritage"],
            "n": 0
        },
        {
            "id": "megalosaurus",
            "tier": "power",
            "t": "William Buckland named Megalosaurus (1824), the first dinosaur to get a scientific name, from English rocks of this age",
            "k": ["megalosaurus", "buckland", "1824"],
            "n": 0
        },
        {
            "id": "portland-stone",
            "tier": "power",
            "t": "Christopher Wren built St. Paul’s Cathedral from Portland stone, a limestone from late in it",
            "k": ["portland stone", "wren", "st. paul’s"],
            "n": 0
        },
        {
            "id": "oolite",
            "tier": "power",
            "t": "Oolitic limestone (Greek for “egg stone”) of the Cotswolds and Bath formed in its warm seas",
            "k": ["oolitic", "egg stone", "cotswolds", "bath"],
            "n": 0
        },
        {
            "id": "camp",
            "tier": "power",
            "t": "Eruptions in the Central Atlantic Magmatic Province are blamed for the extinction at its start",
            "k": ["central atlantic magmatic province", "eruptions"],
            "n": 0
        },
        {
            "id": "morrison",
            "tier": "power",
            "t": "The Morrison Formation of the western U.S., including Dinosaur National Monument, holds its late dinosaurs",
            "k": ["morrison formation", "dinosaur national monument"],
            "n": 0
        },
        {
            "id": "allosaurus-utah",
            "tier": "power",
            "t": "Allosaurus, a top predator from late in it, is Utah’s state fossil",
            "k": ["utah", "state fossil", "predator"],
            "n": 0
        },
        {
            "id": "thagomizer",
            "tier": "power",
            "t": "Stegosaurus’s spiked tail is nicknamed the “thagomizer,” from a _Far Side_ cartoon",
            "k": ["thagomizer", "far side"],
            "n": 0
        },
        {
            "id": "marsh-bone-wars",
            "tier": "power",
            "t": "Othniel Charles Marsh named Stegosaurus, Allosaurus, and Diplodocus in the 1870s, during the Bone Wars with Edward Drinker Cope",
            "k": ["marsh", "bone wars", "cope", "como bluff"],
            "n": 0
        },
        {
            "id": "riggs",
            "tier": "power",
            "t": "Elmer Riggs named Brachiosaurus (“arm lizard”) in 1903 from bones found in western Colorado",
            "k": ["elmer riggs", "arm lizard", "1903"],
            "n": 0
        },
        {
            "id": "holzmaden",
            "tier": "power",
            "t": "Fossils from Holzmaden, Germany, show that its ichthyosaurs gave birth to live young",
            "k": ["holzmaden", "live young"],
            "n": 0
        },
        {
            "id": "kimmeridge",
            "tier": "power",
            "t": "The Kimmeridge Clay, from late in it, is the main source rock for North Sea oil",
            "k": ["kimmeridge clay", "north sea", "oil"],
            "n": 0
        },
        {
            "id": "compsognathus",
            "tier": "power",
            "t": "Solnhofen limestone also preserved the small dinosaur Compsognathus and the pterosaur Pterodactylus",
            "k": ["compsognathus", "pterodactylus"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Jurassic or Cretaceous?",
        "body": "Many famous dinosaurs did not live in the Jurassic. Tyrannosaurus, Triceratops, and Velociraptor all lived in the later Cretaceous, even though they star in a movie named for this period, and the first dinosaurs appeared earlier, in the Triassic. Saying “Mesozoic” names the whole era, and naming the book or movie is wrong too.",
        "fix": "Stegosaurus, Allosaurus, Brachiosaurus, Diplodocus, Archaeopteryx, the Jura Mountains, and Pangaea splitting apart mean the Jurassic. Tyrannosaurus, Triceratops, flowering plants, and the asteroid impact mean the Cretaceous; the first dinosaurs and Pangaea still mostly in one piece mean the Triassic. If you say “Mesozoic,” expect a prompt.",
        "line": "Real answer line: <b><u>Jurassic</u></b> period (prompt on Mesozoic; do not accept “Triassic” or “Cretaceous”)"
    },
    "tests": {
        "right": [
            "Jurassic",
            "Jurassic period",
            "the Jurassic",
            "Jurrasic",
            "Late Jurassic"
        ],
        "prompt": [
            "Mesozoic",
            "Mesozoic Era"
        ],
        "wrong": [
            "Triassic",
            "Cretaceous",
            "Jurassic Park",
            "Cambrian",
            "Jura Mountains"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
