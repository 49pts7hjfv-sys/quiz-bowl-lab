import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "muscles",
    "name": "Muscles",
    "mono": "MUS",
    "category": "Biology",
    "qbCategory": "Science · Biology",
    "kicker": "Tissue that contracts to move the body · Skeletal, smooth, and cardiac",
    "dates": "More than 600 in the human body",
    "briefing": "Every move you make, from blinking to sprinting, comes from muscles, tissues that work by contracting, or getting shorter. Skeletal muscles pull on your bones through tendons, smooth muscles squeeze food through your gut, and cardiac muscle keeps your heart beating your whole life. Inside each muscle cell, protein threads called actin and myosin slide past each other to make the cell shorter.",
    "answerHtml": "<b><u>Muscles</u></b> (accept <u>muscle</u> tissue or specific types such as skeletal <u>muscle</u>; do not accept “tendons” or “bones”)",
    "accept": [
        "muscles",
        "muscle",
        "muscle tissue",
        "muscle tissues",
        "muscular tissue",
        "muscular system",
        "musculature",
        "muscle fibers",
        "muscle fiber",
        "muscle cells",
        "muscle cell",
        "myocytes",
        "myocyte",
        "skeletal muscle",
        "skeletal muscles",
        "smooth muscle",
        "smooth muscles",
        "cardiac muscle",
        "cardiac muscles",
        "heart muscle",
        "striated muscle"
    ],
    "prompt": [],
    "reject": [
        "tendons",
        "tendon",
        "bones",
        "bone",
        "ligaments",
        "ligament",
        "cartilage",
        "skeleton",
        "skeletal system",
        "joints",
        "nerves",
        "neurons",
        "actin",
        "myosin",
        "sarcomeres",
        "sarcomere",
        "myofibrils",
        "myofibril",
        "titin",
        "myoglobin",
        "mussels",
        "mussel",
        "muscular dystrophy"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Muscle",
    "qb": {
        "q": "muscle",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "In the 1780s, Luigi Galvani made the legs of dead frogs twitch by touching their nerves with metal tools, and he argued that this tissue held a kind of “animal electricity.” Alessandro Volta disagreed and built the first battery to show that the two metals made the electricity.",
            "r": "For 10 points, name this tissue that contracts to move the body, which comes in skeletal, smooth, and cardiac types."
        },
        {
            "p": "A. V. Hill shared the 1922 Nobel Prize in Physiology or Medicine for measuring the heat given off by this tissue as it works. His co-winner, Otto Meyerhof [“MY-er-hoff”], linked the oxygen this tissue uses to the lactic acid it makes.",
            "r": "Tendons connect the skeletal type of this tissue to bones. For 10 points, name this tissue that contracts to move the body."
        },
        {
            "p": "In 1954, Hugh Huxley and Jean Hanson, and separately Andrew Huxley and Rolf Niedergerke [“NEE-der-gair-kuh”], proposed that thin and thick filaments slide past each other when this tissue contracts. Each repeating unit of the striped, or striated, types of this tissue runs from one Z-disc to the next and is called a sarcomere.",
            "r": "The thin filaments are made of actin, and the thick ones of myosin. For 10 points, name this tissue that contracts to move the body."
        },
        {
            "p": "John Kendrew won a Nobel Prize for working out the 3D structure of myoglobin, an oxygen-storing protein found in this tissue, the first protein structure ever solved by X-ray crystallography. Slow-twitch fibers of this tissue are packed with myoglobin and mitochondria, which is why a chicken’s legs are dark meat.",
            "r": "Its skeletal type is attached to bones by tendons. For 10 points, name this tissue that comes in skeletal, smooth, and cardiac types."
        },
        {
            "p": "This tissue’s name comes from the Latin for “little mouse,” supposedly because a bulge of it rippling under the skin looked like a mouse. Cells of the skeletal type of this tissue are long and striped and can each contain hundreds of nuclei.",
            "r": "The biceps and triceps are examples. For 10 points, name these organs that move the body by contracting."
        },
        {
            "p": "Belgian Blue cattle look extra bulky because a mutation in their gene for myostatin [“my-oh-STAT-in”], a protein that normally limits the growth of this tissue, lets it keep growing. Weight training makes the fibers of this tissue thicker, a change called hypertrophy.",
            "r": "When it goes unused, it shrinks in a process called atrophy. For 10 points, name this tissue whose skeletal type pulls on bones."
        },
        {
            "p": "Hunters in South America tipped darts with curare [“koo-RAH-ree”], which paralyzes prey by blocking the acetylcholine receptors on this tissue. A single motor neuron and all the fibers of this tissue that it controls are together called a motor unit.",
            "r": "Its skeletal type is controlled voluntarily. For 10 points, name this tissue that contracts to move the body."
        },
        {
            "p": "When a nerve signal races down the T-tubules of this tissue, a network called the sarcoplasmic reticulum releases calcium ions. The calcium binds to troponin, which shifts tropomyosin aside so that myosin heads can grab actin and pull.",
            "r": "For 10 points, name this tissue that contracts to move the body, found in skeletal, smooth, and cardiac forms."
        },
        {
            "p": "Gap junctions inside structures called intercalated [“in-TER-kuh-lay-ted”] discs let electrical signals spread quickly from cell to cell in one type of this tissue. That type contracts in a steady rhythm set by its own pacemaker cells, without needing signals from the brain.",
            "r": "That type makes up the walls of the heart. For 10 points, name this tissue whose three types are skeletal, smooth, and cardiac."
        },
        {
            "p": "Tiny arrector pili [“uh-REK-tor PY-lye”], which make hairs stand up as goosebumps, are made of the smooth type of this tissue. That smooth type also forms layers in the walls of the stomach and intestines, pushing food along in waves called peristalsis [“pair-ih-STALL-sis”].",
            "r": "Its skeletal type is attached to bones by tendons. For 10 points, name this tissue that contracts to move the body."
        },
        {
            "p": "The stapedius [“stuh-PEE-dee-us”], which steadies the tiniest bone in the middle ear, is usually called the smallest skeletal one of these organs. The sartorius [“sar-TOR-ee-us”], which crosses the thigh from the hip to the inside of the knee, is often called the longest.",
            "r": "The gluteus maximus is usually called the largest. For 10 points, name these organs that are attached to bones by tendons."
        },
        {
            "p": "Titin, the largest known protein, acts like a spring that lets this tissue bounce back after being stretched. Dystrophin [“dis-TROH-fin”], a protein missing in people with Duchenne [“doo-SHEN”] dystrophy, links the filaments inside this tissue’s cells to their outer membrane.",
            "r": "Actin and myosin filaments slide past each other inside it. For 10 points, name this tissue that contracts to move the body."
        },
        {
            "p": "After death, cells of this tissue run out of ATP, so their myosin heads stay locked onto actin, causing the stiffness called rigor mortis. During a short sprint, this tissue quickly remakes ATP using energy stored in creatine phosphate.",
            "r": "It contracts to move the body. For 10 points, name this tissue that makes up the biceps and the diaphragm."
        },
        {
            "p": "During hard exercise, this tissue can turn pyruvate into lactate when oxygen runs low, and the liver turns that lactate back into glucose in a loop named for Carl and Gerty Cori. This tissue stores glucose as glycogen for quick energy.",
            "r": "Its cells contract using actin and myosin. For 10 points, name this tissue whose skeletal type is attached to bones by tendons."
        },
        {
            "p": "Each skeletal one of these organs is wrapped in a sheath called the epimysium [“ep-ih-MIZ-ee-um”], and the bundles inside it, called fascicles [“FASS-ih-kulz”], are wrapped in perimysium. These organs often work in antagonistic pairs, so that when one contracts, its partner relaxes.",
            "r": "The biceps and triceps form one such pair. For 10 points, name these organs that move the body by contracting."
        }
    ],
    "clues": [
        {
            "id": "contracts",
            "tier": "giveaway",
            "t": "Tissue that contracts (gets shorter) to move the body and its parts",
            "k": ["contracts", "move the body"],
            "n": 0
        },
        {
            "id": "three-types",
            "tier": "giveaway",
            "t": "Comes in three types: skeletal, smooth, and cardiac",
            "k": ["three types", "skeletal", "smooth", "cardiac"],
            "n": 0
        },
        {
            "id": "tendons",
            "tier": "giveaway",
            "t": "Skeletal ones are attached to bones by tendons",
            "k": ["tendons", "bones"],
            "n": 0,
            "rabbit": "Bones"
        },
        {
            "id": "examples",
            "tier": "giveaway",
            "t": "Examples include the biceps, triceps, quadriceps, and diaphragm",
            "k": ["biceps", "diaphragm", "quadriceps"],
            "n": 0
        },
        {
            "id": "actin-myosin",
            "tier": "giveaway",
            "t": "Their cells contract when filaments of actin and myosin slide past each other",
            "k": ["actin", "myosin", "filaments"],
            "n": 0,
            "rabbit": "Actin"
        },
        {
            "id": "skeletal-type",
            "tier": "middle",
            "t": "Skeletal type: voluntary and striped (striated), with long cells that hold many nuclei",
            "k": ["voluntary", "striated", "many nuclei"],
            "n": 0
        },
        {
            "id": "smooth-type",
            "tier": "middle",
            "t": "Smooth type: involuntary and not striped; found in the walls of the stomach, intestines, and blood vessels",
            "k": ["involuntary", "blood vessels", "intestines"],
            "n": 0
        },
        {
            "id": "cardiac-type",
            "tier": "middle",
            "t": "Cardiac type: striated and found in the heart, its cells linked by intercalated discs with gap junctions",
            "k": ["intercalated discs", "gap junctions", "heart"],
            "n": 0,
            "rabbit": "Heart"
        },
        {
            "id": "sliding-filament",
            "tier": "middle",
            "t": "Sliding filament model (1954): thin actin filaments slide past thick myosin filaments in each sarcomere, which runs from Z-disc to Z-disc",
            "k": ["sliding filament", "sarcomere", "z-disc", "1954"],
            "n": 0
        },
        {
            "id": "antagonistic",
            "tier": "middle",
            "t": "Work in antagonistic pairs, like the biceps and triceps: when one contracts, its partner relaxes",
            "k": ["antagonistic pairs", "triceps"],
            "n": 0
        },
        {
            "id": "calcium",
            "tier": "middle",
            "t": "A signal travels down T-tubules; calcium from the sarcoplasmic reticulum binds troponin, moving tropomyosin aside",
            "k": ["calcium", "sarcoplasmic reticulum", "troponin", "t-tubules"],
            "n": 0
        },
        {
            "id": "acetylcholine",
            "tier": "middle",
            "t": "Motor neurons trigger them with acetylcholine; one motor neuron plus the fibers it controls is a motor unit",
            "k": ["acetylcholine", "motor unit", "motor neurons"],
            "n": 0
        },
        {
            "id": "little-mouse",
            "tier": "middle",
            "t": "The name comes from the Latin for “little mouse”",
            "k": ["little mouse", "latin"],
            "n": 0
        },
        {
            "id": "peristalsis",
            "tier": "middle",
            "t": "The smooth type pushes food through the digestive tract in waves called peristalsis",
            "k": ["peristalsis", "digestive tract"],
            "n": 0
        },
        {
            "id": "galvani",
            "tier": "power",
            "t": "In the 1780s, Luigi Galvani made dead frogs’ legs twitch and claimed “animal electricity”; Alessandro Volta disagreed and built the first battery",
            "k": ["galvani", "frogs", "animal electricity", "volta"],
            "n": 0
        },
        {
            "id": "hill-meyerhof",
            "tier": "power",
            "t": "A. V. Hill (heat) and Otto Meyerhof (oxygen use and lactic acid) shared the 1922 Nobel Prize for studying them",
            "k": ["hill", "meyerhof", "1922"],
            "n": 0
        },
        {
            "id": "huxley-hanson",
            "tier": "power",
            "t": "Hugh Huxley and Jean Hanson, and separately Andrew Huxley and Rolf Niedergerke, proposed the sliding filament model",
            "k": ["huxley", "hanson", "niedergerke"],
            "n": 0
        },
        {
            "id": "myoglobin",
            "tier": "power",
            "t": "Myoglobin, their oxygen-storing protein, was the first protein whose structure was solved by X-ray crystallography (John Kendrew)",
            "k": ["myoglobin", "kendrew", "crystallography"],
            "n": 0
        },
        {
            "id": "twitch-fibers",
            "tier": "power",
            "t": "Slow-twitch fibers, rich in myoglobin and mitochondria, resist tiring (dark meat); fast-twitch fibers give quick bursts",
            "k": ["slow-twitch", "fast-twitch", "dark meat"],
            "n": 0
        },
        {
            "id": "myostatin",
            "tier": "power",
            "t": "A myostatin mutation makes Belgian Blue cattle extra bulky; training causes hypertrophy and disuse causes atrophy",
            "k": ["myostatin", "belgian blue", "hypertrophy", "atrophy"],
            "n": 0
        },
        {
            "id": "curare",
            "tier": "power",
            "t": "Curare on South American hunting darts blocks their acetylcholine receptors, causing paralysis",
            "k": ["curare", "darts", "paralysis"],
            "n": 0
        },
        {
            "id": "record-holders",
            "tier": "power",
            "t": "The stapedius is usually called the smallest skeletal one, the sartorius the longest, and the gluteus maximus the largest",
            "k": ["stapedius", "sartorius", "gluteus maximus"],
            "n": 0
        },
        {
            "id": "titin-dystrophin",
            "tier": "power",
            "t": "Titin, the largest known protein, acts as a spring; dystrophin, missing in Duchenne dystrophy, anchors their filaments",
            "k": ["titin", "dystrophin", "duchenne"],
            "n": 0
        },
        {
            "id": "rigor-creatine",
            "tier": "power",
            "t": "Without ATP after death, myosin stays stuck to actin (rigor mortis); creatine phosphate quickly remakes ATP during sprints",
            "k": ["rigor mortis", "creatine phosphate"],
            "n": 0
        },
        {
            "id": "cori-cycle",
            "tier": "power",
            "t": "During hard exercise they make lactate, which the liver turns back into glucose (Cori cycle); they store glucose as glycogen",
            "k": ["cori cycle", "lactate", "glycogen"],
            "n": 0,
            "rabbit": "Lactic acid"
        },
        {
            "id": "arrector-pili",
            "tier": "power",
            "t": "Arrector pili, tiny smooth ones, raise hairs to make goosebumps",
            "k": ["arrector pili", "goosebumps"],
            "n": 0
        },
        {
            "id": "epimysium",
            "tier": "power",
            "t": "Each skeletal one is wrapped in epimysium; the bundles inside, called fascicles, are wrapped in perimysium",
            "k": ["epimysium", "fascicles", "perimysium"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Not the tendon or bone",
        "body": "Many clues describe how muscles pull on the skeleton, so players blurt the parts being pulled. Tendons connect muscles to bones, ligaments connect bones to other bones, and bones are the levers that get moved. Clues about actin and myosin can also tempt a player to name a protein instead of the tissue.",
        "fix": "If the question asks for “this tissue” that contracts, or names skeletal, smooth, and cardiac types, say “muscles.” Tough cords that attach it to bone are tendons, and links between two bones are ligaments.",
        "line": "Real answer line: <b><u>Muscles</u></b> (accept <u>muscle</u> tissue; do not accept “tendons” or “bones”)"
    },
    "tests": {
        "right": [
            "Muscles",
            "muscle",
            "Muscle tissue",
            "Skeletal muscle",
            "musles",
            "Muscular system"
        ],
        "prompt": [],
        "wrong": [
            "Tendons",
            "Bones",
            "Ligaments",
            "Mussels",
            "Actin",
            "Heart",
            "Skeleton"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
