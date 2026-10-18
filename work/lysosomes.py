import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "lysosomes",
    "name": "Lysosomes",
    "mono": "LYS",
    "category": "Biology",
    "qbCategory": "Science · Biology",
    "kicker": "Organelles full of digestive enzymes · The cell’s cleanup and recycling crew",
    "dates": "Named by Christian de Duve in 1955",
    "briefing": "Lysosomes are the cell’s cleanup and recycling crew: small, bubble-like organelles packed with dozens of digestive enzymes that break down worn-out cell parts, food particles, and invading bacteria. Their insides are kept acidic, and their enzymes work best in acid, which helps protect the rest of the cell if one leaks. Belgian scientist Christian de Duve discovered them in the 1950s and later shared a Nobel Prize.",
    "answerHtml": "<b><u>Lysosomes</u></b> (accept <u>lysosome</u>; do not accept “lysozyme” or “peroxisome”)",
    "accept": [
        "lysosome",
        "lysosomes"
    ],
    "prompt": [],
    "reject": [
        "lysozyme",
        "lysozymes",
        "liposome",
        "liposomes",
        "peroxisome",
        "peroxisomes",
        "proteasome",
        "proteasomes",
        "vacuole",
        "vacuoles",
        "endosome",
        "endosomes",
        "phagosome",
        "phagosomes",
        "autophagosome",
        "autophagosomes",
        "ribosome",
        "ribosomes",
        "golgi",
        "golgi apparatus",
        "golgi body",
        "endoplasmic reticulum",
        "er",
        "mitochondria",
        "mitochondrion",
        "nucleus",
        "centrosome",
        "centrosomes",
        "melanosome",
        "acrosome"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Lysosome",
    "qb": {
        "q": "lysosome",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "Christian de Duve [“duh DOOV”] found this organelle after noticing that an enzyme called acid phosphatase became more active when rat liver samples sat in a refrigerator for several days, because the membranes holding the enzyme slowly broke open. He named this organelle in 1955.",
            "r": "For 10 points, name these organelles full of digestive enzymes that break down worn-out cell parts."
        },
        {
            "p": "Alex Novikoff took the first electron microscope pictures of this organelle in 1955, working with its discoverer, Christian de Duve [“duh DOOV”]. Its interior is kept at a pH of about 4.5 to 5 by pumps that bring in hydrogen ions.",
            "r": "Plants mostly rely on vacuoles for its job instead. For 10 points, name this organelle that uses digestive enzymes to break down old cell parts."
        },
        {
            "p": "Enzymes bound for this organelle are tagged with mannose-6-phosphate [“MAN-ohs six FOSS-fate”] in the Golgi apparatus. In I-cell disease, that tag is never added, so the enzymes are shipped out of the cell instead and undigested material piles up.",
            "r": "It is nicknamed the cell’s recycling center. For 10 points, name this acidic organelle that digests worn-out cell parts and invading bacteria."
        },
        {
            "p": "Yoshinori Ohsumi [“oh-SOO-mee”] won the 2016 Nobel Prize for his work on autophagy, a “self-eating” process in which animal cells wrap up their own worn-out parts and deliver them to this organelle. Its enzymes then break those parts down so their building blocks can be reused.",
            "r": "Its enzymes are shipped to it by the Golgi apparatus. For 10 points, name this organelle, nicknamed the cell’s recycling center."
        },
        {
            "p": "Heavily sugar-coated proteins called LAMPs line the inside of this organelle’s membrane, protecting it from being digested by the organelle’s own enzymes. Those enzymes, called acid hydrolases [“HY-druh-lay-zez”], work best at a low pH, so they do little damage if they leak into the cytoplasm.",
            "r": "Plants use vacuoles for much of this job. For 10 points, name this organelle that digests food particles and old cell parts."
        },
        {
            "p": "Pompe [“POM-puh”] disease, a glycogen storage disease, and Gaucher [“go-SHAY”] disease both happen when this organelle is missing one of its enzymes. In Tay-Sachs disease, a missing enzyme in this organelle lets a fatty substance build up in nerve cells.",
            "r": "For 10 points, name this organelle that uses digestive enzymes to break down materials inside the cell."
        },
        {
            "p": "Bone-dissolving cells called osteoclasts [“OSS-tee-oh-klasts”] release enzymes from this organelle, along with acid, to break down old bone. This organelle’s enzymes work best at a pH of about 5, which is much more acidic than the rest of the cell.",
            "r": "For 10 points, name this organelle filled with digestive enzymes that breaks down worn-out cell parts."
        },
        {
            "p": "Protein-cutting enzymes called cathepsins [“kuh-THEP-sinz”] do much of their work inside this organelle, alongside dozens of other enzymes that break down fats, sugars, and nucleic acids. Its enzymes are made on the rough ER and delivered by way of the Golgi apparatus.",
            "r": "For 10 points, name this organelle, the cell’s main digestive compartment, found mostly in animal cells."
        },
        {
            "p": "Albert Claude and George Palade [“puh-LAH-day”] shared the 1974 Nobel Prize with the Belgian scientist who discovered this organelle. That scientist, Christian de Duve, also discovered peroxisomes, which break down hydrogen peroxide, while this organelle uses acid-loving digestive enzymes.",
            "r": "For 10 points, name this organelle that breaks down worn-out cell parts, food particles, and bacteria."
        },
        {
            "p": "Older textbooks call a newly formed one of these organelles “primary” and one that has fused with material to digest “secondary.” Material that a cell takes in by endocytosis passes through compartments called endosomes before reaching this organelle.",
            "r": "For 10 points, name this organelle that uses digestive enzymes to break down worn-out cell parts."
        },
        {
            "p": "A pump called a V-type ATPase uses energy from ATP to push hydrogen ions into this organelle, keeping its inside acidic. This organelle’s name comes from Greek words meaning “loosening” and “body,” and plant cells mostly let their large central vacuole do its job.",
            "r": "For 10 points, name this organelle, found mainly in animal cells, that is packed with digestive enzymes."
        },
        {
            "p": "When cells die, enzymes leaking out of this organelle help digest them in a process called autolysis [“aw-TOL-ih-sis”], or self-digestion. In living cells, this organelle breaks down worn-out mitochondria and other old parts so their materials can be reused.",
            "r": "For 10 points, name this organelle that is sometimes nicknamed the cell’s “suicide bag.”"
        },
        {
            "p": "When a white blood cell swallows a bacterium, the bacterium ends up inside a sac called a phagosome [“FAG-oh-sohm”], which then fuses with this organelle so its enzymes can destroy the invader. Single-celled organisms like amoebas digest their food the same way.",
            "r": "For 10 points, name this organelle, sometimes called the cell’s recycling center, that is full of digestive enzymes."
        },
        {
            "p": "This organelle should not be confused with a similarly named enzyme in tears and saliva that Alexander Fleming discovered. This organelle’s own enzymes include nucleases, lipases, and proteases, which break down nucleic acids, fats, and proteins.",
            "r": "Its inside is kept acidic. For 10 points, name this organelle that breaks down worn-out cell parts."
        },
        {
            "p": "This organelle is a small sac wrapped in a single membrane and filled with dozens of digestive enzymes. It breaks down food particles, invading bacteria, and worn-out cell parts, and it is found mainly in animal cells.",
            "r": "For 10 points, name this organelle often called the cell’s garbage disposal or recycling center."
        }
    ],
    "clues": [
        {
            "id": "digestive-enzymes",
            "tier": "giveaway",
            "t": "Small, membrane-bound organelles filled with dozens of digestive enzymes",
            "k": ["digestive enzymes", "membrane-bound"],
            "n": 0
        },
        {
            "id": "recycling-center",
            "tier": "giveaway",
            "t": "Break down food particles, invading bacteria, and worn-out cell parts; nicknamed the cell’s recycling center or garbage disposal",
            "k": ["recycling center", "garbage disposal", "worn-out"],
            "n": 0
        },
        {
            "id": "suicide-bags",
            "tier": "giveaway",
            "t": "Nicknamed “suicide bags,” since their enzymes could digest the whole cell if they burst",
            "k": ["suicide bags", "burst"],
            "n": 0
        },
        {
            "id": "animal-cells",
            "tier": "giveaway",
            "t": "Found mainly in animal cells; plant cells mostly use their large central vacuole for the same job",
            "k": ["animal cells", "central vacuole"],
            "n": 0,
            "rabbit": "Vacuoles"
        },
        {
            "id": "golgi-delivery",
            "tier": "giveaway",
            "t": "Their enzymes are made on the rough ER and delivered by way of the Golgi apparatus",
            "k": ["golgi apparatus", "rough er"],
            "n": 0,
            "rabbit": "Golgi apparatus"
        },
        {
            "id": "acidic",
            "tier": "middle",
            "t": "Kept acidic inside (about pH 4.5 to 5) by V-type ATPase pumps that push in hydrogen ions",
            "k": ["acidic", "hydrogen ions", "v-type atpase"],
            "n": 0
        },
        {
            "id": "acid-hydrolases",
            "tier": "middle",
            "t": "Their enzymes, called acid hydrolases, work best in acid, so a leak into the neutral cytoplasm does little harm",
            "k": ["acid hydrolases", "neutral"],
            "n": 0
        },
        {
            "id": "phagocytosis",
            "tier": "middle",
            "t": "White blood cells destroy swallowed bacteria when a phagosome fuses with one of these; amoebas digest food this way too",
            "k": ["phagosome", "white blood cells", "amoebas"],
            "n": 0,
            "rabbit": "White blood cells"
        },
        {
            "id": "autophagy",
            "tier": "middle",
            "t": "In autophagy (“self-eating”), worn-out cell parts are wrapped up and delivered to them for recycling",
            "k": ["autophagy", "self-eating"],
            "n": 0
        },
        {
            "id": "tay-sachs",
            "tier": "middle",
            "t": "Tay-Sachs disease happens when one of their enzymes is missing, so a fatty substance builds up in nerve cells",
            "k": ["tay-sachs", "fatty substance", "nerve cells"],
            "n": 0
        },
        {
            "id": "de-duve",
            "tier": "middle",
            "t": "Discovered by Belgian scientist Christian de Duve, who named them in 1955",
            "k": ["de duve", "belgian", "1955"],
            "n": 0
        },
        {
            "id": "endosomes",
            "tier": "middle",
            "t": "Material taken in by endocytosis passes through endosomes on its way to them",
            "k": ["endocytosis", "endosomes"],
            "n": 0
        },
        {
            "id": "autolysis",
            "tier": "middle",
            "t": "When cells die, their leaking enzymes help digest the cells in autolysis (self-digestion)",
            "k": ["autolysis", "self-digestion"],
            "n": 0
        },
        {
            "id": "refrigerator",
            "tier": "power",
            "t": "De Duve noticed that acid phosphatase became more active after rat liver samples sat in a refrigerator for days, as the membranes around it broke",
            "k": ["acid phosphatase", "refrigerator", "rat liver"],
            "n": 0
        },
        {
            "id": "novikoff",
            "tier": "power",
            "t": "Alex Novikoff took the first electron microscope pictures of them in 1955",
            "k": ["novikoff", "electron microscope"],
            "n": 0
        },
        {
            "id": "nobel-1974",
            "tier": "power",
            "t": "De Duve shared the 1974 Nobel Prize with Albert Claude and George Palade",
            "k": ["1974", "albert claude", "palade"],
            "n": 0
        },
        {
            "id": "peroxisomes",
            "tier": "power",
            "t": "De Duve also discovered peroxisomes, a different organelle that breaks down hydrogen peroxide",
            "k": ["peroxisomes", "hydrogen peroxide"],
            "n": 0,
            "rabbit": "Peroxisomes"
        },
        {
            "id": "mannose-6-phosphate",
            "tier": "power",
            "t": "Enzymes headed for them get a mannose-6-phosphate tag in the Golgi apparatus",
            "k": ["mannose-6-phosphate", "tag"],
            "n": 0
        },
        {
            "id": "i-cell",
            "tier": "power",
            "t": "In I-cell disease that tag is missing, so the enzymes are shipped out of the cell instead",
            "k": ["i-cell disease", "shipped out"],
            "n": 0
        },
        {
            "id": "gaucher-pompe",
            "tier": "power",
            "t": "Gaucher disease and Pompe disease (a glycogen storage disease) also come from missing enzymes here",
            "k": ["gaucher", "pompe", "glycogen"],
            "n": 0
        },
        {
            "id": "ohsumi",
            "tier": "power",
            "t": "Yoshinori Ohsumi won the 2016 Nobel Prize for his work on autophagy",
            "k": ["ohsumi", "2016"],
            "n": 0
        },
        {
            "id": "lamps",
            "tier": "power",
            "t": "Sugar-coated membrane proteins called LAMPs protect their membrane from their own enzymes",
            "k": ["lamps", "sugar-coated"],
            "n": 0
        },
        {
            "id": "cathepsins",
            "tier": "power",
            "t": "Protein-cutting enzymes called cathepsins work inside them, alongside nucleases and lipases",
            "k": ["cathepsins", "nucleases", "lipases"],
            "n": 0
        },
        {
            "id": "osteoclasts",
            "tier": "power",
            "t": "Bone-dissolving osteoclasts release enzymes from them, along with acid, to break down old bone",
            "k": ["osteoclasts", "bone-dissolving"],
            "n": 0,
            "rabbit": "Bones"
        },
        {
            "id": "primary-secondary",
            "tier": "power",
            "t": "Older textbooks call new ones “primary” and ones that have fused with material to digest “secondary”",
            "k": ["primary", "secondary"],
            "n": 0
        },
        {
            "id": "greek-name",
            "tier": "power",
            "t": "The name comes from Greek words meaning “loosening” and “body”",
            "k": ["loosening", "greek"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Lysosome or lysozyme?",
        "body": "Lysozyme sounds almost the same, but it is a single enzyme in tears and saliva that breaks open bacterial cell walls, discovered by Alexander Fleming, not an organelle. Peroxisomes are a different organelle, also discovered by Christian de Duve, that destroy hydrogen peroxide. And plant cells mostly let their large central vacuole do the lysosome’s cleanup job.",
        "fix": "If the clues mention acid hydrolases, autophagy, Tay-Sachs disease, or mannose-6-phosphate, say lysosome. Hydrogen peroxide and the enzyme catalase mean peroxisome; tears and Fleming mean lysozyme.",
        "line": "Real answer line: <b><u>Lysosomes</u></b> (accept <u>lysosome</u>; do not accept “lysozyme” or “peroxisome”)"
    },
    "tests": {
        "right": [
            "Lysosomes",
            "lysosome",
            "Lysosome",
            "Lysosones"
        ],
        "prompt": [],
        "wrong": [
            "Lysozyme",
            "Peroxisome",
            "Vacuole",
            "Proteasome",
            "Liposome",
            "Golgi apparatus"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
