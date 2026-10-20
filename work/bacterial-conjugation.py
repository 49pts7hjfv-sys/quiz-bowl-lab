import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "bacterial-conjugation",
    "name": "Bacterial conjugation",
    "mono": "CNJ",
    "category": "Biology",
    "qbCategory": "Science · Biology",
    "kicker": "How bacteria share plasmids · DNA passed through a pilus",
    "dates": "Discovered in 1946",
    "briefing": "Bacteria can swap genes without making new cells. In bacterial conjugation, a donor cell reaches out with a thin tube called a pilus, pulls a neighbor close, and passes it a copy of a plasmid, a small ring of DNA. It is a big reason genes for surviving antibiotics can spread quickly from one bacterium to another, sometimes even between different species.",
    "answerHtml": "<b><u>Conjugation</u></b> (accept <u>bacterial conjugation</u>; prompt on <u>horizontal gene transfer</u> or <u>lateral gene transfer</u>; do not accept “transformation” or “transduction”)",
    "accept": [
        "conjugation",
        "bacterial conjugation",
        "conjugation in bacteria"
    ],
    "prompt": [
        "horizontal gene transfer",
        "lateral gene transfer",
        "gene transfer",
        "horizontal transfer",
        "lateral transfer",
        "hgt"
    ],
    "reject": [
        "transformation",
        "bacterial transformation",
        "transduction",
        "binary fission",
        "fission",
        "mitosis",
        "meiosis",
        "fertilization",
        "replication",
        "dna replication",
        "rolling circle replication",
        "transcription",
        "translation",
        "transposition",
        "transposons",
        "budding",
        "sporulation",
        "conjunction",
        "conjugate",
        "conjugated",
        "plasmid",
        "plasmids",
        "pilus",
        "pili",
        "f plasmid",
        "f factor",
        "hfr",
        "crispr",
        "cloning",
        "mutation",
        "mutations",
        "antibiotic resistance",
        "endosymbiosis",
        "quorum sensing",
        "transfection"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Bacterial_conjugation",
    "qb": {
        "q": "conjugation",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "In 1946, Joshua Lederberg and Edward Tatum mixed two strains of E. coli that each could not make certain nutrients, and found new cells that could make all of them. To rule out simple mutation, each strain lacked several abilities at once. That result revealed this process.",
            "r": "In this process, a donor bacterium passes a plasmid through a tube called a pilus. For 10 points, name this way that bacteria share genes."
        },
        {
            "p": "In 1950, Bernard Davis put two bacterial strains in the two arms of a U-shaped tube, separated by a filter that let liquid but not cells pass through, and found that this process could not happen without direct contact.",
            "r": "That showed it differs from transformation, in which bacteria pick up loose DNA. For 10 points, name this process in which bacteria pass plasmids through a pilus."
        },
        {
            "p": "Élie Wollman and François Jacob mapped bacterial genes by stopping this process at set times with a kitchen blender, which is why the E. coli gene map is measured in minutes. Genes closest to the starting point entered the recipient first.",
            "r": "In this process, a donor bacterium passes DNA to a neighbor through a pilus. For 10 points, name this form of horizontal gene transfer."
        },
        {
            "p": "In Hfr strains, short for “high frequency of recombination,” the F plasmid has joined the main chromosome, so this process can carry chromosome genes into another cell in a fixed order. Transferring a whole chromosome this way takes about 100 minutes, so the cells usually separate first.",
            "r": "For 10 points, name this process in which one bacterium passes DNA to another through a tube called a pilus."
        },
        {
            "p": "Esther Lederberg helped discover the F factor, a plasmid that lets the cells carrying it start this process. When an F-positive cell completes this process with an F-negative cell, the recipient becomes F-positive, too.",
            "r": "Afterward, both cells have a copy of the plasmid. For 10 points, name this process in which bacteria pass copies of plasmids through a pilus."
        },
        {
            "p": "An enzyme called relaxase cuts one strand of a plasmid at a spot called oriT to begin this process. As that single strand moves into the recipient, the donor rebuilds its own copy by rolling-circle replication.",
            "r": "For 10 points, name this process in which a bacterium passes a plasmid to a neighbor through a pilus."
        },
        {
            "p": "Agrobacterium tumefaciens [“ag-roh-bak-TEER-ee-um too-muh-FAY-shee-enz”] uses machinery related to this process to move DNA from its Ti plasmid into plant cells, causing lumpy growths called crown galls. Scientists borrow that system to put new genes into crops.",
            "r": "In ordinary bacteria, this process sends a copy of a plasmid through a tube called a pilus. For 10 points, name this way that bacteria share genes."
        },
        {
            "p": "The scientist who coined the word “plasmid” in 1952 shared the 1958 Nobel Prize partly for discovering this process, and he was only 33 years old when he won. He shared that prize with Edward Tatum and George Beadle.",
            "r": "That scientist was Joshua Lederberg. For 10 points, name this process in which a bacterium passes DNA to another through a pilus."
        },
        {
            "p": "Plasmids called R factors, which can carry genes for resistance to several antibiotics at once, often spread between gut bacteria by this process, even between different species. They were discovered in Japan after dysentery bacteria that resisted several drugs at once appeared there in the 1950s.",
            "r": "For 10 points, name this process in which a donor bacterium sends a copy of a plasmid through a tube called a pilus."
        },
        {
            "p": "Many bacteria carry out this process using a type IV secretion system, a protein machine that spans the cell envelope and pushes DNA into a partner cell. Plasmid genes called tra genes build that machine.",
            "r": "It is one way that genes for antibiotic resistance spread. For 10 points, name this process of plasmid transfer between bacteria that are touching."
        },
        {
            "p": "Paramecia swap small nuclei called micronuclei in a process that shares this process’s name, and the green alga Spirogyra [“spy-roh-JY-ruh”] joins side-by-side filaments with tubes in another process with the same name.",
            "r": "In bacteria, this process sends a copy of a plasmid through a pilus. For 10 points, name this process, a form of horizontal gene transfer."
        },
        {
            "p": "When an F plasmid pops out of the chromosome and takes a few chromosome genes with it, it becomes an F-prime plasmid, which can then carry those genes into new cells during this process.",
            "r": "Unlike binary fission, this process makes no new cells. For 10 points, name this process in which bacteria share plasmids through a pilus."
        },
        {
            "p": "The thin appendage that starts this process can latch onto a partner cell and then shrink back, reeling the two cells together. Only cells carrying certain plasmids can build that appendage.",
            "r": "That appendage is called a pilus. For 10 points, name this process in which a donor bacterium passes DNA to a recipient."
        },
        {
            "p": "This process needs no virus, unlike transduction, which Norton Zinder and Joshua Lederberg discovered in 1952, and no loose DNA, unlike transformation, which Frederick Griffith first saw in 1928.",
            "r": "Instead, two living cells touch, and a plasmid passes through a pilus. For 10 points, name this way that bacteria share genes."
        },
        {
            "p": "Bacteria can even use this process to pass plasmids into yeast cells, which belong to a different kingdom of life. Genes moved this way are one example of horizontal gene transfer, which spreads genes without parents passing them to offspring.",
            "r": "Usually, this process moves a plasmid from one bacterium to another through a pilus. For 10 points, name this process."
        }
    ],
    "clues": [
        {
            "id": "pilus",
            "tier": "giveaway",
            "t": "A donor bacterium passes DNA to a recipient through a thin tube called a pilus",
            "k": ["pilus", "donor", "recipient"],
            "n": 0
        },
        {
            "id": "plasmid",
            "tier": "giveaway",
            "t": "Usually moves a copy of a plasmid, a small ring of DNA separate from the main chromosome",
            "k": ["plasmid", "ring of dna"],
            "n": 0,
            "rabbit": "Bacteria"
        },
        {
            "id": "horizontal",
            "tier": "giveaway",
            "t": "A form of horizontal gene transfer: genes pass between living cells, not from parent to offspring",
            "k": ["horizontal gene transfer", "offspring"],
            "n": 0
        },
        {
            "id": "contact",
            "tier": "giveaway",
            "t": "Needs direct contact between two living cells",
            "k": ["direct contact"],
            "n": 0
        },
        {
            "id": "antibiotic-resistance",
            "tier": "giveaway",
            "t": "Spreads genes for antibiotic resistance from one bacterium to another",
            "k": ["antibiotic resistance", "antibiotic"],
            "n": 0,
            "rabbit": "Penicillin"
        },
        {
            "id": "lederberg-tatum",
            "tier": "middle",
            "t": "Discovered by Joshua Lederberg and Edward Tatum in 1946, using E. coli strains that each couldn’t make certain nutrients",
            "k": ["lederberg", "tatum", "1946"],
            "n": 0,
            "rabbit": "E. coli"
        },
        {
            "id": "f-plasmid",
            "tier": "middle",
            "t": "The F plasmid lets a cell start it: F-positive cells are donors and F-negative cells are recipients",
            "k": ["f plasmid", "f-positive", "f-negative"],
            "n": 0
        },
        {
            "id": "becomes-donor",
            "tier": "middle",
            "t": "Afterward, the recipient has its own copy of the F plasmid and can become a donor too",
            "k": ["become a donor", "copy"],
            "n": 0
        },
        {
            "id": "not-reproduction",
            "tier": "middle",
            "t": "It is not reproduction, since no new cells are made; bacteria reproduce by binary fission",
            "k": ["binary fission", "reproduction"],
            "n": 0
        },
        {
            "id": "other-transfers",
            "tier": "middle",
            "t": "Unlike transformation (loose DNA; Griffith, 1928) or transduction (carried by phages; Zinder and Lederberg, 1952), it needs cell contact",
            "k": ["transformation", "transduction", "phages"],
            "n": 0,
            "rabbit": "Bacteriophages"
        },
        {
            "id": "single-strand",
            "tier": "middle",
            "t": "Only one strand of the plasmid crosses over, and each cell then rebuilds a double-stranded copy",
            "k": ["one strand", "double-stranded"],
            "n": 0
        },
        {
            "id": "r-factors",
            "tier": "middle",
            "t": "R factors are plasmids carrying resistance to several antibiotics; they were found in Japan after multidrug-resistant dysentery bacteria appeared in the 1950s",
            "k": ["r factors", "dysentery", "japan"],
            "n": 0
        },
        {
            "id": "davis-u-tube",
            "tier": "power",
            "t": "Bernard Davis’s U-tube experiment (1950) showed it needs contact: a filter between two strains stopped it",
            "k": ["u-tube", "davis", "filter", "1950"],
            "n": 0
        },
        {
            "id": "wollman-jacob",
            "tier": "power",
            "t": "Élie Wollman and François Jacob stopped it at set times in a kitchen blender to map genes, so the E. coli gene map is measured in minutes",
            "k": ["kitchen blender", "wollman", "jacob", "minutes"],
            "n": 0
        },
        {
            "id": "hfr",
            "tier": "power",
            "t": "In Hfr (“high frequency of recombination”) strains, the F plasmid has joined the chromosome; passing a whole chromosome takes about 100 minutes",
            "k": ["high frequency of recombination", "hfr", "100 minutes"],
            "n": 0
        },
        {
            "id": "esther-lederberg",
            "tier": "power",
            "t": "Esther Lederberg helped discover the F plasmid, also called the F factor",
            "k": ["esther lederberg", "f factor"],
            "n": 0
        },
        {
            "id": "plasmid-word",
            "tier": "power",
            "t": "Joshua Lederberg coined the word “plasmid” (1952) and shared the 1958 Nobel Prize, at age 33, with Tatum and George Beadle",
            "k": ["coined", "beadle", "1958", "age 33"],
            "n": 0
        },
        {
            "id": "relaxase",
            "tier": "power",
            "t": "The enzyme relaxase nicks one strand of the plasmid at its origin of transfer, called oriT",
            "k": ["origin of transfer", "relaxase", "orit"],
            "n": 0
        },
        {
            "id": "rolling-circle",
            "tier": "power",
            "t": "The donor replaces the strand it sends by rolling-circle replication",
            "k": ["rolling-circle replication", "rolling-circle"],
            "n": 0
        },
        {
            "id": "type-iv",
            "tier": "power",
            "t": "Its machinery is a type IV secretion system, built by plasmid genes called tra genes",
            "k": ["type iv secretion system", "tra genes"],
            "n": 0
        },
        {
            "id": "agrobacterium",
            "tier": "power",
            "t": "Agrobacterium tumefaciens uses related machinery to move DNA from its Ti plasmid into plants, causing crown galls",
            "k": ["agrobacterium", "ti plasmid", "crown galls"],
            "n": 0
        },
        {
            "id": "f-prime",
            "tier": "power",
            "t": "An F plasmid that leaves the chromosome carrying extra genes is an F-prime plasmid",
            "k": ["f-prime"],
            "n": 0
        },
        {
            "id": "same-name",
            "tier": "power",
            "t": "Paramecia (which swap micronuclei) and the alga Spirogyra (which joins filaments with tubes) carry out processes with the same name",
            "k": ["micronuclei", "spirogyra", "paramecia"],
            "n": 0
        },
        {
            "id": "yeast",
            "tier": "power",
            "t": "Bacteria can even pass plasmids to yeast cells this way, crossing into another kingdom",
            "k": ["yeast", "kingdom"],
            "n": 0,
            "rabbit": "Yeast"
        },
        {
            "id": "pilus-retracts",
            "tier": "power",
            "t": "The pilus latches onto a partner cell and then shrinks back, reeling the two cells together",
            "k": ["shrinks back", "reeling"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Three ways to swap genes",
        "body": "Bacteria share genes in three ways, and tossups often name one to rule it out. In transformation, a cell picks up loose DNA from its surroundings (Griffith’s 1928 experiment); in transduction, a virus called a phage carries DNA from cell to cell. Conjugation is the only one that needs two living cells to touch, usually through a pilus.",
        "fix": "A pilus, the F plasmid, F-positive and F-negative cells, Hfr strains, or a U-tube experiment mean conjugation. Loose DNA or “rough” and “smooth” strains mean transformation, and phages mean transduction. Don’t answer “binary fission”: that is how bacteria reproduce, not how they share genes.",
        "line": "Real answer line: <b><u>Conjugation</u></b> (accept <u>bacterial conjugation</u>; prompt on <u>horizontal gene transfer</u>; do not accept “transformation” or “transduction”)"
    },
    "tests": {
        "right": [
            "Conjugation",
            "Bacterial conjugation",
            "conjugaton",
            "bacterial conjegation",
            "Conjugation in bacteria"
        ],
        "prompt": [
            "Horizontal gene transfer",
            "Lateral gene transfer"
        ],
        "wrong": [
            "Transformation",
            "Transduction",
            "Binary fission",
            "Conjunction",
            "Plasmid",
            "Pilus",
            "Mitosis"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
