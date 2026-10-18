import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "apoptosis",
    "name": "Apoptosis",
    "mono": "APT",
    "category": "Biology",
    "qbCategory": "Science · Biology",
    "kicker": "Programmed cell death · Cells take themselves apart neatly",
    "dates": "Named in 1972",
    "briefing": "Apoptosis is programmed cell death: a tidy, step-by-step way for a cell to take itself apart when it is damaged or no longer needed. Before you were born, it carved your fingers apart by removing the webbing between them. Enzymes called caspases chop the cell up from the inside, and white blood cells eat the leftover pieces, so nothing spills out to cause inflammation.",
    "answerHtml": "<b><u>Apoptosis</u></b> (accept <u>programmed cell death</u>; prompt on <u>cell death</u>; do not accept “necrosis” or “autophagy”)",
    "accept": [
        "apoptosis",
        "programmed cell death",
        "apoptotic cell death",
        "cell suicide",
        "cellular suicide"
    ],
    "prompt": [
        "cell death",
        "cellular death",
        "programmed death"
    ],
    "reject": [
        "necrosis",
        "necroptosis",
        "pyroptosis",
        "ferroptosis",
        "autophagy",
        "autolysis",
        "phagocytosis",
        "mitosis",
        "meiosis",
        "senescence",
        "cytokinesis",
        "lysis",
        "cell lysis",
        "apoptosome",
        "caspase",
        "caspases",
        "ptosis",
        "inflammation"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Apoptosis",
    "qb": {
        "q": "apoptosis",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "In the hermaphrodite form of the worm _Caenorhabditis elegans_ [“SEE-noh-rab-DY-tiss EL-uh-ganz”], exactly 131 of the 1,090 body cells formed during development die by this process. H. Robert Horvitz, John Sulston, and Sydney Brenner shared the 2002 Nobel Prize in Physiology or Medicine partly for studying this process in that worm.",
            "r": "This process is carried out by enzymes called caspases. For 10 points, name this orderly form of cell death, which removes the webbing between a developing embryo’s fingers."
        },
        {
            "p": "Mutations in the worm genes ced-3 and ced-4 stop this process, while the gene ced-9, which matches the human gene Bcl-2, normally holds it in check. The protein made by ced-3 belongs to a family of protein-cutting enzymes called caspases.",
            "r": "For 10 points, name this tidy form of cell death, a cell’s planned self-destruction, which, unlike necrosis, causes no inflammation."
        },
        {
            "p": "John Kerr, Andrew Wyllie [“WY-lee”], and Alastair Currie named this process in 1972, choosing a Greek word that describes leaves falling off a tree. During this process, the cell shrinks and breaks into small membrane-wrapped packets.",
            "r": "Macrophages eat those packets, so nothing spills out to cause inflammation. For 10 points, name this orderly form of cell death."
        },
        {
            "p": "When cytochrome c leaks out of the mitochondria, it binds a protein called Apaf-1, forming a wheel-shaped complex that switches on caspase-9 and starts the intrinsic pathway of this process. That pathway is often triggered when a cell’s DNA is badly damaged.",
            "r": "For 10 points, name this form of cell death in which a cell neatly takes itself apart, as when it removes the webbing between an embryo’s fingers and toes."
        },
        {
            "p": "A protein called Fas ligand binds to a “death receptor” called Fas to start the extrinsic pathway of this process, which switches on caspase-8. That initiator caspase then turns on executioner caspases, such as caspase-3, that chop apart the cell’s proteins.",
            "r": "For 10 points, name this process, a cell’s orderly self-destruction, which is different from messy necrosis."
        },
        {
            "p": "The protein Bcl-2, first found in a type of B-cell lymphoma, blocks this process, while its relatives Bax and Bak promote it by punching holes in the outer membranes of mitochondria. Cancer cells often avoid this process, which lets damaged cells keep dividing.",
            "r": "For 10 points, name this tidy form of cell death that removes damaged or unneeded cells."
        },
        {
            "p": "Douglas Hanahan and Robert Weinberg listed “evading” this process as one of the hallmarks of cancer. The protein p53, nicknamed the “guardian of the genome,” can trigger this process when a cell’s DNA is too damaged to repair.",
            "r": "For 10 points, name this form of cell death, carried out by enzymes called caspases, in which a cell destroys itself in an orderly way."
        },
        {
            "p": "Scientists use a protein called annexin V to spot cells undergoing this process, because it binds phosphatidylserine [“foss-fuh-TY-dul-SAIR-een”], a lipid that flips to the outside of the cell membrane as an “eat me” signal. Macrophages that sense that signal swallow the cell’s remains.",
            "r": "For 10 points, name this orderly form of cell death that, unlike necrosis, does not cause inflammation."
        },
        {
            "p": "The TUNEL test labels the cut ends of DNA in cells undergoing this process, in which enzymes chop the DNA into regular-sized pieces that form a “ladder” on a gel. During this process, the cell’s membrane bulges out in bubbles called blebs.",
            "r": "For 10 points, name this tidy form of cell death, which removes the webbing between a developing embryo’s fingers."
        },
        {
            "p": "Cytotoxic T cells and natural killer cells trigger this process in infected cells by releasing perforin, which opens pores in the target cell, and granzymes, which enter through those pores. Inside the target cell, enzymes called caspases then carry out this process.",
            "r": "For 10 points, name this process, a cell’s orderly self-destruction, which is different from necrosis."
        },
        {
            "p": "In the thymus, young T cells that would attack the body’s own tissues are removed by this process during negative selection. This process also removes a tadpole’s tail during metamorphosis, a change triggered by thyroid hormone.",
            "r": "For 10 points, name this orderly form of cell death, in which caspases help a cell take itself apart."
        },
        {
            "p": "Proteins called IAPs, such as XIAP, hold back this process by blocking caspases, until mitochondria release a protein named Smac, also called DIABLO, that blocks the IAPs in turn. During this process, the cell shrinks and its chromatin clumps together.",
            "r": "For 10 points, name this tidy form of cell death that removes unneeded cells, like the webbing between an embryo’s fingers."
        },
        {
            "p": "Anoikis, whose name is Greek for “homelessness,” is a form of this process that happens to cells that lose their grip on the tissue around them. Release of cytochrome c from mitochondria starts this process’s intrinsic pathway.",
            "r": "For 10 points, name this orderly form of cell death that, unlike necrosis, causes no inflammation."
        },
        {
            "p": "Caspase-3 and caspase-7 act as “executioner” enzymes in this process, cutting apart key proteins inside the cell. One of those cuts frees an enzyme that chops the cell’s DNA into pieces, and the cell then splits into small packets that neighboring cells can eat.",
            "r": "For 10 points, name this form of cell death, in which a cell neatly takes itself apart instead of bursting as in necrosis."
        },
        {
            "p": "Neutrophils, short-lived white blood cells, normally die by this process after an infection has been cleared, and macrophages then eat them. During this process, a cell shrinks and breaks into small membrane-wrapped packets instead of bursting open.",
            "r": "For 10 points, name this orderly self-destruction of cells, which removes the webbing between an embryo’s fingers and toes."
        }
    ],
    "clues": [
        {
            "id": "orderly-self-destruction",
            "tier": "giveaway",
            "t": "A cell’s planned, orderly self-destruction, controlled by its own genes",
            "k": ["self-destruction", "orderly", "planned"],
            "n": 0
        },
        {
            "id": "webbing",
            "tier": "giveaway",
            "t": "Removes the webbing between the fingers and toes of a developing embryo",
            "k": ["webbing", "fingers", "embryo"],
            "n": 0
        },
        {
            "id": "not-necrosis",
            "tier": "giveaway",
            "t": "Unlike necrosis (messy cell death from injury, where cells swell and burst), it is tidy and causes no inflammation",
            "k": ["necrosis", "inflammation"],
            "n": 0
        },
        {
            "id": "damaged-cells",
            "tier": "giveaway",
            "t": "Removes damaged, infected, or unneeded cells for the good of the whole body",
            "k": ["damaged", "unneeded", "infected"],
            "n": 0
        },
        {
            "id": "falling-off",
            "tier": "middle",
            "t": "Its name comes from a Greek word for “falling off,” like leaves dropping from a tree",
            "k": ["falling off", "greek", "leaves"],
            "n": 0
        },
        {
            "id": "caspases",
            "tier": "middle",
            "t": "Carried out by protein-cutting enzymes called caspases",
            "k": ["caspases", "protein-cutting"],
            "n": 0,
            "rabbit": "Enzymes"
        },
        {
            "id": "blebs-packets",
            "tier": "middle",
            "t": "The cell shrinks, its membrane bulges out in blebs, and it breaks into small membrane-wrapped packets",
            "k": ["blebs", "shrinks", "packets"],
            "n": 0
        },
        {
            "id": "macrophages",
            "tier": "middle",
            "t": "Macrophages and other phagocytes eat the leftover packets, so nothing spills out",
            "k": ["macrophages", "phagocytes"],
            "n": 0,
            "rabbit": "White blood cells"
        },
        {
            "id": "cytochrome-c",
            "tier": "middle",
            "t": "Mitochondria release cytochrome c to start its intrinsic pathway",
            "k": ["cytochrome c", "intrinsic pathway", "mitochondria"],
            "n": 0,
            "rabbit": "Mitochondria"
        },
        {
            "id": "cancer",
            "tier": "middle",
            "t": "Cancer cells avoid it, which lets damaged cells keep dividing; “evading” it is a hallmark of cancer",
            "k": ["cancer", "evading", "hallmark"],
            "n": 0,
            "rabbit": "Cancer"
        },
        {
            "id": "p53",
            "tier": "middle",
            "t": "The protein p53, the “guardian of the genome,” can trigger it when DNA is too damaged to repair",
            "k": ["p53", "guardian of the genome"],
            "n": 0
        },
        {
            "id": "tadpole",
            "tier": "middle",
            "t": "Removes a tadpole’s tail during metamorphosis, a change triggered by thyroid hormone",
            "k": ["tadpole", "metamorphosis", "thyroid hormone"],
            "n": 0,
            "rabbit": "Metamorphosis"
        },
        {
            "id": "kerr-1972",
            "tier": "middle",
            "t": "Named in 1972 by John Kerr, Andrew Wyllie, and Alastair Currie",
            "k": ["kerr", "wyllie", "currie", "1972"],
            "n": 0
        },
        {
            "id": "elegans-131",
            "tier": "power",
            "t": "In the worm C. elegans, exactly 131 of the 1,090 body cells made in a hermaphrodite die this way",
            "k": ["c. elegans", "131", "1,090"],
            "n": 0
        },
        {
            "id": "nobel-2002",
            "tier": "power",
            "t": "Sydney Brenner, H. Robert Horvitz, and John Sulston shared the 2002 Nobel Prize partly for studying it in that worm",
            "k": ["horvitz", "sulston", "brenner", "2002"],
            "n": 0
        },
        {
            "id": "ced-genes",
            "tier": "power",
            "t": "The worm genes ced-3 and ced-4 drive it, while ced-9, which matches the human gene Bcl-2, holds it back",
            "k": ["ced-3", "ced-4", "ced-9"],
            "n": 0
        },
        {
            "id": "apaf-1",
            "tier": "power",
            "t": "Cytochrome c joins Apaf-1 to form a wheel-shaped complex that switches on caspase-9",
            "k": ["apaf-1", "caspase-9", "wheel-shaped"],
            "n": 0
        },
        {
            "id": "fas",
            "tier": "power",
            "t": "Fas ligand binds the “death receptor” Fas to start the extrinsic pathway through caspase-8",
            "k": ["death receptor", "extrinsic pathway", "caspase-8", "fas"],
            "n": 0
        },
        {
            "id": "bcl-2",
            "tier": "power",
            "t": "Bcl-2, first found in a B-cell lymphoma, blocks it; its relatives Bax and Bak promote it by opening holes in mitochondria",
            "k": ["bcl-2", "bax", "bak", "lymphoma"],
            "n": 0
        },
        {
            "id": "executioner",
            "tier": "power",
            "t": "“Executioner” caspases such as caspase-3 and caspase-7 are switched on by “initiator” caspases",
            "k": ["executioner", "caspase-3", "initiator"],
            "n": 0
        },
        {
            "id": "eat-me",
            "tier": "power",
            "t": "Phosphatidylserine flips to the outside of the membrane as an “eat me” signal; annexin V binds it to spot dying cells",
            "k": ["phosphatidylserine", "eat me", "annexin v"],
            "n": 0
        },
        {
            "id": "dna-ladder",
            "tier": "power",
            "t": "Its DNA is chopped into regular-sized pieces that form a “ladder” on a gel; the TUNEL test labels those cut ends",
            "k": ["ladder", "tunel"],
            "n": 0
        },
        {
            "id": "perforin-granzymes",
            "tier": "power",
            "t": "Cytotoxic T cells and natural killer cells trigger it in infected cells using perforin and granzymes",
            "k": ["perforin", "granzymes", "natural killer"],
            "n": 0
        },
        {
            "id": "thymus",
            "tier": "power",
            "t": "In the thymus, young T cells that would attack the body’s own tissues are removed this way (negative selection)",
            "k": ["thymus", "negative selection"],
            "n": 0
        },
        {
            "id": "iaps-smac",
            "tier": "power",
            "t": "IAP proteins such as XIAP block caspases; mitochondria release Smac (DIABLO) to block the IAPs",
            "k": ["xiap", "smac", "diablo"],
            "n": 0
        },
        {
            "id": "anoikis",
            "tier": "power",
            "t": "Anoikis, Greek for “homelessness,” is this kind of death in cells that lose their grip on surrounding tissue",
            "k": ["anoikis", "homelessness"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Apoptosis, not necrosis",
        "body": "Both are ways a cell dies, so players who hear “cell death” buzz with the first one they think of. Necrosis is messy, accidental death from injury or loss of blood flow: the cell swells and bursts, and its leaking contents cause inflammation. Autophagy, in which a cell digests some of its own parts inside lysosomes, is a second trap; it often helps a cell survive.",
        "fix": "Planned, tidy, shrinking, caspases, cytochrome c, blebs, and webbing between fingers mean apoptosis. Swelling, bursting, injury, and inflammation mean necrosis. “Self-eating” and lysosomes mean autophagy.",
        "line": "Real answer line: <b><u>Apoptosis</u></b> (accept <u>programmed cell death</u>; prompt on <u>cell death</u>; do not accept “necrosis”)"
    },
    "tests": {
        "right": [
            "Apoptosis",
            "apoptosis",
            "Apotosis",
            "Programmed cell death",
            "Apoptosys"
        ],
        "prompt": [
            "Cell death"
        ],
        "wrong": [
            "Necrosis",
            "Autophagy",
            "Mitosis",
            "Phagocytosis",
            "Necroptosis"
        ]
    }
}

out = ROOT / "topics" / "apoptosis.json"
with open(out, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("wrote", out)
