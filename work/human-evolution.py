import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "human-evolution",
    "name": "Human evolution",
    "mono": "HEV",
    "category": "Biology",
    "qbCategory": "Science · Biology",
    "kicker": "How our species arose from earlier primates · Traced through fossils and DNA",
    "dates": "Spans about 7 million years",
    "briefing": "Human evolution is the story of how our species, Homo sapiens, arose from earlier primates over roughly 7 million years. Fossils like “Lucy,” a 3.2-million-year-old skeleton found in Ethiopia in 1974, show that our ancestors walked upright long before their brains grew large. Most scientists agree that modern humans first appeared in Africa and later spread across the world, meeting Neanderthals along the way.",
    "answerHtml": "<b><u>Human evolution</u></b> (accept <u>evolution of humans</u> or <u>hominin evolution</u>; prompt on <u>evolution</u>; do not accept “Neanderthals”)",
    "accept": [
        "human evolution",
        "evolution of humans",
        "evolution of humanity",
        "evolution of humankind",
        "evolution of mankind",
        "evolution of man",
        "evolution of homo sapiens",
        "hominin evolution",
        "hominid evolution",
        "evolution of hominins",
        "evolution of hominids",
        "human origins",
        "origin of humans",
        "anthropogenesis",
        "hominization"
    ],
    "prompt": [
        "evolution",
        "theory of evolution",
        "biological evolution",
        "evolutionary theory",
        "descent with modification"
    ],
    "reject": [
        "neanderthals",
        "neanderthal",
        "neandertals",
        "neandertal",
        "denisovans",
        "natural selection",
        "speciation",
        "creationism",
        "intelligent design",
        "social darwinism",
        "paleoanthropology",
        "anthropology",
        "australopithecus",
        "australopithecines",
        "homo erectus",
        "homo habilis",
        "lucy",
        "cultural evolution",
        "stellar evolution"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Human_evolution",
    "qb": {
        "q": "human evolution",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "Ethiopians call a skeleton found at Hadar in 1974 Dinkinesh [“din-KEE-nesh”], meaning “you are marvelous,” but its English nickname comes from a Beatles song that played at the discoverers’ camp. Donald Johanson’s team found that partial skeleton, an Australopithecus afarensis about 3.2 million years old.",
            "r": "That skeleton is nicknamed “Lucy.” For 10 points, name this process, studied by paleoanthropologists, by which our species arose from earlier primates."
        },
        {
            "p": "Volcanic ash at Laetoli [“lay-TOH-lee”], Tanzania, preserved a trail of footprints about 3.6 million years old, showing that some early hominins walked upright long before their brains grew large. Mary Leakey’s team uncovered those footprints in the late 1970s.",
            "r": "For 10 points, name this process, illustrated by fossils like “Lucy,” in which modern people arose from earlier hominins."
        },
        {
            "p": "In 1959, Mary Leakey found the skull of a big-toothed hominin nicknamed “Nutcracker Man” at Olduvai [“OHL-duh-vy”] Gorge in Tanzania. Her family later found fossils of Homo habilis, the “handy man,” there, near simple stone tools called Oldowan tools.",
            "r": "For 10 points, name this process by which Homo sapiens arose from earlier primates, a story that fossils like “Lucy” help tell."
        },
        {
            "p": "In 1891, Eugène Dubois [“oo-ZHEN doo-BWAH”] found “Java Man” in Indonesia, and in the 1920s, scientists dug up “Peking Man” near Beijing, though most of those Chinese fossils were lost in 1941. Both finds belong to Homo erectus, which made teardrop-shaped Acheulean [“uh-SHOO-lee-un”] hand axes.",
            "r": "For 10 points, name this process, studied through fossils like “Lucy,” by which our species arose from earlier primates."
        },
        {
            "p": "In 1984, Kamoya Kimeu, working with Richard Leakey’s team, found the nearly complete skeleton of a Homo erectus youth near Lake Turkana in Kenya. Homo erectus was probably the first hominin to spread out of Africa, reaching places as far away as Indonesia.",
            "r": "That skeleton is the “Turkana Boy.” For 10 points, name this process by which modern people arose from earlier hominins."
        },
        {
            "p": "In 1925, Raymond Dart described the “Taung Child,” a young fossil skull from South Africa, and named its species Australopithecus africanus, meaning “southern ape from Africa.” For years, many experts rejected Dart’s claim that the skull belonged to one of our early relatives.",
            "r": "For 10 points, name this process, studied by paleoanthropologists, by which Homo sapiens arose from earlier primates."
        },
        {
            "p": "Fossils found in a gravel pit at Piltdown, England, in 1912 fooled many scientists for decades, until tests in 1953 proved them a hoax made from a person’s skull and an orangutan’s jaw. That fake “missing link” had distracted researchers studying this process.",
            "r": "For 10 points, name this process, studied through real fossils like “Lucy,” in which our species arose from earlier primates."
        },
        {
            "p": "The multiregional hypothesis says that modern people developed from older hominin groups in several parts of the world, linked by interbreeding. Its main rival says Homo sapiens arose in Africa and later spread across the world, an idea supported by studies of mitochondrial DNA.",
            "r": "That rival is the “Out of Africa” model. For 10 points, name this process, by which our species arose from earlier primates."
        },
        {
            "p": "Fossils from Jebel Irhoud [“JEB-ul eer-HOOD”] in Morocco, announced in 2017, pushed the oldest known remains of Homo sapiens back to about 300,000 years ago. Before that, skulls found near the Omo River in Ethiopia had been the oldest known.",
            "r": "For 10 points, name this process, illustrated by fossils like “Lucy,” through which our species arose from earlier primates."
        },
        {
            "p": "People have 46 chromosomes while chimpanzees have 48, because two ancestral chromosomes fused end to end to form our chromosome 2. Comparing the two species’ genomes shows that their DNA is more than 98 percent identical.",
            "r": "Chimpanzees and bonobos are our closest living relatives. For 10 points, name this process by which Homo sapiens arose from earlier primates."
        },
        {
            "p": "In his 1871 book _The Descent of Man_, Charles Darwin predicted that people most likely first arose in Africa, because gorillas and chimpanzees live there. Eight years earlier, Thomas Henry Huxley had compared the skeletons of people and apes in _Evidence as to Man’s Place in Nature_.",
            "r": "For 10 points, name this process, studied through fossils like “Lucy,” in which modern people arose from earlier hominins."
        },
        {
            "p": "A skull nicknamed Toumaï [“too-MY”], found in Chad in 2001 by Michel Brunet’s team, may be one of the oldest known hominins, at about 7 million years old. Ardi, a skeleton of Ardipithecus from Ethiopia described in 2009, lived about 4.4 million years ago.",
            "r": "For 10 points, name this process by which Homo sapiens arose from earlier primates over millions of years."
        },
        {
            "p": "Lee Berger’s team announced Homo naledi [“nah-LEH-dee”] in 2015 after recovering its fossils from deep inside the Rising Star cave system in South Africa. Eleven years earlier, scientists described a tiny species nicknamed the “hobbit,” Homo floresiensis, from the island of Flores in Indonesia.",
            "r": "For 10 points, name this process, studied by paleoanthropologists, in which modern people arose from earlier hominins."
        },
        {
            "p": "Svante Pääbo [“SVAHN-teh PAY-boh”] won the 2022 Nobel Prize for ancient-DNA research showing that early modern people had children with Neanderthals and with Denisovans, a group first identified from a finger bone in a Siberian cave. Most people with ancestors from outside Africa carry about 1 to 2 percent Neanderthal DNA.",
            "r": "The Laetoli footprints and the skeleton “Lucy” are famous evidence of this process. For 10 points, name this process by which our species arose from earlier primates."
        },
        {
            "p": "The foramen magnum [“for-AY-men MAG-num”], the hole where the spinal cord enters the skull, sits farther forward in species that walk upright. The hip and leg bones of a skeleton found in Ethiopia in 1974 showed that it walked on two legs, though its brain was about the size of a chimpanzee’s.",
            "r": "That skeleton is “Lucy,” found by Donald Johanson’s team. For 10 points, name this process by which modern people arose from earlier hominins."
        }
    ],
    "clues": [
        {
            "id": "definition",
            "tier": "giveaway",
            "t": "The process by which our species, Homo sapiens, arose from earlier primates over millions of years",
            "k": ["homo sapiens", "earlier primates", "millions of years"],
            "n": 0,
            "rabbit": "Evolution"
        },
        {
            "id": "lucy",
            "tier": "giveaway",
            "t": "“Lucy,” a 3.2-million-year-old _Australopithecus afarensis_ skeleton, was found in Ethiopia in 1974 by Donald Johanson’s team",
            "k": ["lucy", "australopithecus afarensis", "johanson", "1974"],
            "n": 0
        },
        {
            "id": "out-of-africa",
            "tier": "giveaway",
            "t": "“Out of Africa”: Homo sapiens first arose in Africa and later spread across the world",
            "k": ["out of africa", "spread"],
            "n": 0
        },
        {
            "id": "chimpanzees",
            "tier": "giveaway",
            "t": "Chimpanzees and bonobos are our closest living relatives; we share a common ancestor from about 6 to 7 million years ago",
            "k": ["chimpanzees", "bonobos", "common ancestor"],
            "n": 0
        },
        {
            "id": "leakeys",
            "tier": "giveaway",
            "t": "The Leakey family (Louis, Mary, Richard, and Meave) found many key fossils in East Africa",
            "k": ["leakey", "east africa"],
            "n": 0
        },
        {
            "id": "bipedalism",
            "tier": "middle",
            "t": "Walking upright on two legs (bipedalism) came long before big brains",
            "k": ["bipedalism", "two legs", "big brains"],
            "n": 0
        },
        {
            "id": "laetoli",
            "tier": "middle",
            "t": "The Laetoli footprints in Tanzania, about 3.6 million years old and preserved in volcanic ash, were uncovered by Mary Leakey’s team",
            "k": ["laetoli", "footprints", "volcanic ash"],
            "n": 0
        },
        {
            "id": "homo-habilis",
            "tier": "middle",
            "t": "_Homo habilis_ (“handy man”) is linked to simple Oldowan stone tools found at Olduvai Gorge, Tanzania",
            "k": ["homo habilis", "handy man", "olduvai", "oldowan"],
            "n": 0
        },
        {
            "id": "homo-erectus",
            "tier": "middle",
            "t": "_Homo erectus_ (“upright man”) made Acheulean hand axes and was probably the first hominin to leave Africa",
            "k": ["homo erectus", "upright man", "acheulean", "hand axes"],
            "n": 0
        },
        {
            "id": "neanderthals",
            "tier": "middle",
            "t": "Early modern people had children with Neanderthals and Denisovans, so many people carry a little of their DNA",
            "k": ["neanderthals", "denisovans"],
            "n": 0,
            "rabbit": "Neanderthals"
        },
        {
            "id": "hominins",
            "tier": "middle",
            "t": "Our species and its extinct close relatives are called hominins",
            "k": ["hominins", "extinct"],
            "n": 0
        },
        {
            "id": "multiregional",
            "tier": "middle",
            "t": "The multiregional hypothesis, the main rival to “Out of Africa,” says modern people developed in several regions at once",
            "k": ["multiregional", "several regions"],
            "n": 0
        },
        {
            "id": "mitochondrial-dna",
            "tier": "middle",
            "t": "Mitochondrial DNA traces all living people back to a “Mitochondrial Eve” who lived in Africa",
            "k": ["mitochondrial dna", "mitochondrial eve"],
            "n": 0,
            "rabbit": "Mitochondria"
        },
        {
            "id": "descent-of-man",
            "tier": "middle",
            "t": "Charles Darwin’s _The Descent of Man_ (1871) predicted that people first arose in Africa",
            "k": ["descent of man", "darwin", "1871"],
            "n": 0,
            "rabbit": "Charles Darwin"
        },
        {
            "id": "dinkinesh",
            "tier": "power",
            "t": "Lucy is called Dinkinesh (“you are marvelous”) in Amharic; her English name comes from a Beatles song played at camp",
            "k": ["dinkinesh", "beatles", "marvelous"],
            "n": 0
        },
        {
            "id": "java-peking",
            "tier": "power",
            "t": "Java Man (Eugène Dubois, 1891) and Peking Man (China, 1920s) are _Homo erectus_; most Peking Man fossils were lost in 1941",
            "k": ["java man", "peking man", "dubois", "1941"],
            "n": 0
        },
        {
            "id": "turkana-boy",
            "tier": "power",
            "t": "Kamoya Kimeu found the Turkana Boy, a nearly complete _Homo erectus_ skeleton, in Kenya in 1984",
            "k": ["turkana boy", "kimeu", "kenya", "1984"],
            "n": 0
        },
        {
            "id": "taung-child",
            "tier": "power",
            "t": "Raymond Dart described the Taung Child (1925) and named _Australopithecus africanus_, “southern ape from Africa”",
            "k": ["taung child", "raymond dart", "southern ape", "1925"],
            "n": 0
        },
        {
            "id": "nutcracker-man",
            "tier": "power",
            "t": "Mary Leakey found the big-toothed “Nutcracker Man” at Olduvai Gorge in 1959",
            "k": ["nutcracker man", "1959"],
            "n": 0
        },
        {
            "id": "piltdown",
            "tier": "power",
            "t": "Piltdown Man (England, 1912) was exposed in 1953 as a hoax: a person’s skull with an orangutan’s jaw",
            "k": ["piltdown", "hoax", "orangutan", "1953"],
            "n": 0
        },
        {
            "id": "jebel-irhoud",
            "tier": "power",
            "t": "Fossils from Jebel Irhoud, Morocco (announced 2017), are the oldest known _Homo sapiens_, about 300,000 years old",
            "k": ["jebel irhoud", "morocco", "300,000"],
            "n": 0
        },
        {
            "id": "chromosome-2",
            "tier": "power",
            "t": "Our chromosome 2 formed when two ancestral chromosomes fused, so people have 46 chromosomes and chimpanzees have 48",
            "k": ["chromosome 2", "fused", "46 chromosomes"],
            "n": 0
        },
        {
            "id": "huxley",
            "tier": "power",
            "t": "Thomas Henry Huxley compared the skeletons of people and apes in _Evidence as to Man’s Place in Nature_ (1863)",
            "k": ["huxley", "man’s place in nature", "1863"],
            "n": 0
        },
        {
            "id": "toumai-ardi",
            "tier": "power",
            "t": "Toumaï (Chad, found 2001, about 7 million years old) and Ardi (_Ardipithecus_, Ethiopia, described 2009) are among the oldest known hominins",
            "k": ["toumaï", "ardi", "chad", "ardipithecus"],
            "n": 0
        },
        {
            "id": "naledi-hobbit",
            "tier": "power",
            "t": "_Homo naledi_ (Rising Star cave, South Africa, 2015) and the tiny “hobbit,” _Homo floresiensis_ (Flores, Indonesia, 2004)",
            "k": ["homo naledi", "rising star", "hobbit", "flores"],
            "n": 0
        },
        {
            "id": "paabo",
            "tier": "power",
            "t": "Svante Pääbo won the 2022 Nobel Prize for ancient-DNA work showing interbreeding with Neanderthals and Denisovans",
            "k": ["pääbo", "2022", "ancient-dna"],
            "n": 0
        },
        {
            "id": "foramen-magnum",
            "tier": "power",
            "t": "A foramen magnum (where the spinal cord enters the skull) that sits farther forward shows a species walked upright",
            "k": ["foramen magnum", "spinal cord"],
            "n": 0
        }
    ],
    "trap": {
        "title": "The process, not a fossil",
        "body": "Human evolution tossups are packed with famous fossils and species, like Lucy, _Homo erectus_, and the Neanderthals, and each of those is its own answer line. A player who blurts the name of a fossil or species when the question asks for “this process” gets it wrong. Saying just “evolution” is on the right track but earns only a prompt.",
        "fix": "Listen to the last line: “this process” plus fossils, hominins, or our species wants human evolution. “This species” or “these hominins” wants a specific group, like the Neanderthals. If you hear only general Darwin clues, like finches and natural selection, the answer may be plain evolution instead.",
        "line": "Real answer line: <b><u>Human evolution</u></b> (accept <u>evolution of humans</u>; prompt on <u>evolution</u>; do not accept “Neanderthals”)"
    },
    "tests": {
        "right": [
            "Human evolution",
            "evolution of humans",
            "Hominin evolution",
            "human evoluton",
            "Evolution of man"
        ],
        "prompt": [
            "Evolution",
            "theory of evolution"
        ],
        "wrong": [
            "Neanderthals",
            "Natural selection",
            "Lucy",
            "Homo erectus",
            "Speciation",
            "Australopithecus"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
