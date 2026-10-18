import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "mitosis",
    "name": "Mitosis",
    "mono": "MTS",
    "category": "Biology",
    "qbCategory": "Science · Biology",
    "kicker": "Cell division that splits the nucleus · Makes two identical daughter cells",
    "dates": "Named by Walther Flemming in 1882",
    "briefing": "Your body makes millions of new cells every second, and they come from mitosis. In this kind of cell division, a cell that has already copied its chromosomes splits its nucleus so each new cell gets an identical, complete set, which is how you grow and how a scraped knee heals. It runs in four stages, prophase, metaphase, anaphase, and telophase (“PMAT”), and then cytokinesis pinches the cell in two.",
    "answerHtml": "<b><u>Mitosis</u></b> (accept <u>karyokinesis</u> or <u>M phase</u>; prompt on <u>cell division</u>; do not accept “meiosis” or the name of a single stage, such as “prophase”)",
    "accept": [
        "mitosis",
        "mitoses",
        "karyokinesis",
        "m phase",
        "mitotic phase",
        "mitotic division",
        "mitotic cell division"
    ],
    "prompt": [
        "cell division",
        "cellular division",
        "nuclear division",
        "cell cycle",
        "division"
    ],
    "reject": [
        "meiosis",
        "meiosis i",
        "meiosis ii",
        "meiosis 1",
        "meiosis 2",
        "miosis",
        "binary fission",
        "fission",
        "budding",
        "prophase",
        "prometaphase",
        "metaphase",
        "anaphase",
        "telophase",
        "interphase",
        "cytokinesis",
        "s phase",
        "g1 phase",
        "g2 phase",
        "g0 phase",
        "apoptosis",
        "mutation",
        "dna replication",
        "replication",
        "fertilization",
        "chromosomes"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Mitosis",
    "qb": {
        "q": "mitosis",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "Walther Flemming named this process in 1882 from the Greek word for “thread,” based on his studies of stained cells from salamanders. Flemming also coined the word chromatin for the material that coils up into visible chromosomes during this process.",
            "r": "For 10 points, name this kind of cell division that produces two genetically identical daughter cells."
        },
        {
            "p": "Colchicine [“KOL-chih-seen”] halts this process at metaphase by keeping spindle microtubules from forming, a trick used to prepare karyotypes. The cancer drug Taxol, first found in the bark of the Pacific yew, also stops this process by interfering with microtubules.",
            "r": "For 10 points, name this process that splits one nucleus into two identical nuclei."
        },
        {
            "p": "In many fungi, including yeasts, this process is “closed” because the nuclear envelope never breaks apart. In animal cells, the envelope does break apart during a stage called prometaphase, so that spindle fibers can grab the chromosomes.",
            "r": "For 10 points, name this kind of nuclear division that keeps the chromosome number the same."
        },
        {
            "p": "Before this process, plant cells form a preprophase band, a ring of microtubules that marks where the cell will split. As this process ends, a structure called the phragmoplast [“FRAG-moh-plast”] guides vesicles from the Golgi apparatus that build a new cell plate.",
            "r": "For 10 points, name this process of cell division often observed in onion root tips."
        },
        {
            "p": "The anaphase-promoting complex starts the separation stage of this process by freeing an enzyme called separase, which cuts the cohesin rings that hold sister chromatids together. The chromatids are then pulled to opposite ends of the cell.",
            "r": "For 10 points, name this process whose stages include prophase, metaphase, anaphase, and telophase."
        },
        {
            "p": "Tim Hunt discovered proteins called cyclins, which rise and fall to control when cells begin this process, by studying sea urchin eggs. Hunt shared a 2001 Nobel Prize with Leland Hartwell and Paul Nurse for finding key regulators of the cell cycle.",
            "r": "It is followed by cytokinesis. For 10 points, name this process that divides one nucleus into two identical nuclei."
        },
        {
            "p": "The spindle assembly checkpoint delays the start of anaphase in this process until every chromosome’s kinetochore [“kih-NET-oh-kor”] is attached to spindle fibers. Kinetochores are protein structures that form at each chromosome’s centromere.",
            "r": "During this process, chromosomes line up at the metaphase plate. For 10 points, name this process that produces two identical daughter cells."
        },
        {
            "p": "Biology students often look for this process in slides of whitefish embryos and onion root tips, where cells divide quickly. In those slides, cells in its first stage show thick, condensed chromosomes and no visible nucleolus.",
            "r": "That stage is prophase. For 10 points, name this process of cell division whose stages also include metaphase and anaphase."
        },
        {
            "p": "Leonard Hayflick found that normal human cells grown in a lab can go through this process only about 40 to 60 times before they stop. Each round of copying shortens the protective caps on the ends of chromosomes, called telomeres.",
            "r": "For 10 points, name this process that splits a nucleus to make two identical body cells."
        },
        {
            "p": "Most mature nerve cells stay in a resting stage called G0 and rarely, if ever, go through this process again. Most other cells spend far more time in interphase, which includes the S phase when DNA is copied, than in this process.",
            "r": "For 10 points, name this part of the cell cycle that includes prophase and telophase."
        },
        {
            "p": "Star-shaped clusters of microtubules called asters form around the centrosomes as this process begins in animal cells. During this process’s first stage, chromatin condenses into visible chromosomes, the nucleolus fades away, and the centrosomes move toward opposite sides of the cell.",
            "r": "In its last stage, telophase, new nuclear envelopes form. For 10 points, name this process that produces two identical daughter cells."
        },
        {
            "p": "In anaphase A of this process, kinetochore microtubules shorten and pull chromatids toward the poles, while in anaphase B the poles themselves move farther apart. Motor proteins such as kinesins and dynein help power these movements.",
            "r": "For 10 points, name this process in which a cell’s copied chromosomes are split evenly between two new nuclei."
        },
        {
            "p": "As this process finishes, a contractile ring of actin and myosin forms a cleavage furrow that pinches an animal cell in two. That splitting of the cytoplasm, called cytokinesis, usually begins during this process’s final stage, telophase.",
            "r": "For 10 points, name this process that, unlike meiosis, keeps the chromosome number the same."
        },
        {
            "p": "Vinblastine and vincristine, drugs made from the Madagascar periwinkle, treat some cancers by blocking this process. Cancer cells go through this process again and again because the checkpoints that normally control the cell cycle no longer work properly.",
            "r": "For 10 points, name this process of cell division that makes two identical copies of a cell."
        },
        {
            "p": "Rudolf Virchow popularized the idea that every cell comes from another cell, summed up in the Latin phrase “omnis cellula e cellula.” Bacteria divide by binary fission, but the body cells of plants and animals divide their nuclei by this process.",
            "r": "In human body cells, it makes two diploid cells, while meiosis makes four haploid ones. For 10 points, name this kind of cell division."
        }
    ],
    "clues": [
        {
            "id": "two-identical",
            "tier": "giveaway",
            "t": "Divides a cell’s nucleus to make two genetically identical daughter cells",
            "k": ["identical", "daughter cells", "nucleus"],
            "n": 0
        },
        {
            "id": "pmat",
            "tier": "giveaway",
            "t": "Its stages, in order: prophase, metaphase, anaphase, telophase (“PMAT”)",
            "k": ["prophase", "metaphase", "anaphase", "telophase", "pmat"],
            "n": 0
        },
        {
            "id": "growth-repair",
            "tier": "giveaway",
            "t": "Lets the body grow and replace old or damaged cells",
            "k": ["grow", "damaged cells", "replace"],
            "n": 0
        },
        {
            "id": "not-meiosis",
            "tier": "giveaway",
            "t": "Unlike meiosis, it keeps the chromosome number the same (46 in human body cells)",
            "k": ["meiosis", "chromosome number", "46"],
            "n": 0,
            "rabbit": "Meiosis"
        },
        {
            "id": "interphase",
            "tier": "middle",
            "t": "Comes after interphase (G1, S, and G2), when the cell grows and copies its DNA; mature nerve cells rest in G0",
            "k": ["interphase", "copies its dna", "g0"],
            "n": 0
        },
        {
            "id": "prophase",
            "tier": "middle",
            "t": "Prophase: chromatin condenses into visible chromosomes and the nucleolus disappears",
            "k": ["prophase", "chromatin", "nucleolus"],
            "n": 0
        },
        {
            "id": "metaphase-plate",
            "tier": "middle",
            "t": "Metaphase: chromosomes line up along the middle of the cell, called the metaphase plate",
            "k": ["metaphase plate", "line up"],
            "n": 0
        },
        {
            "id": "anaphase",
            "tier": "middle",
            "t": "Anaphase: sister chromatids separate and are pulled to opposite ends of the cell",
            "k": ["anaphase", "sister chromatids", "opposite ends"],
            "n": 0
        },
        {
            "id": "telophase",
            "tier": "middle",
            "t": "Telophase: new nuclear envelopes form around the two sets of chromosomes",
            "k": ["telophase", "nuclear envelopes"],
            "n": 0
        },
        {
            "id": "spindle",
            "tier": "middle",
            "t": "Spindle fibers made of microtubules grow from centrosomes, ringed by star-shaped asters in animal cells",
            "k": ["spindle", "microtubules", "centrosomes", "asters"],
            "n": 0
        },
        {
            "id": "cytokinesis",
            "tier": "middle",
            "t": "Usually followed by cytokinesis: a ring of actin and myosin pinches animal cells in two, while plant cells build a cell plate",
            "k": ["cytokinesis", "actin", "myosin", "cell plate"],
            "n": 0
        },
        {
            "id": "onion-root",
            "tier": "middle",
            "t": "Often observed in slides of onion root tips and whitefish embryos",
            "k": ["onion root tips", "whitefish"],
            "n": 0
        },
        {
            "id": "flemming",
            "tier": "power",
            "t": "Named in 1882 by Walther Flemming, from the Greek for “thread”; he studied salamander cells and coined “chromatin”",
            "k": ["flemming", "thread", "salamander", "1882"],
            "n": 0
        },
        {
            "id": "kinetochores",
            "tier": "power",
            "t": "Spindle fibers attach to kinetochores, protein structures at each chromosome’s centromere",
            "k": ["kinetochores", "centromere"],
            "n": 0
        },
        {
            "id": "prometaphase",
            "tier": "power",
            "t": "Prometaphase: the nuclear envelope breaks apart so microtubules can grab the chromosomes",
            "k": ["prometaphase", "nuclear envelope"],
            "n": 0
        },
        {
            "id": "separase",
            "tier": "power",
            "t": "The anaphase-promoting complex frees separase, which cuts the cohesin holding sister chromatids together",
            "k": ["separase", "cohesin", "anaphase-promoting complex"],
            "n": 0
        },
        {
            "id": "anaphase-a-b",
            "tier": "power",
            "t": "Anaphase A pulls chromatids to the poles; in anaphase B, the poles themselves move farther apart",
            "k": ["anaphase a", "anaphase b", "poles"],
            "n": 0
        },
        {
            "id": "cyclins",
            "tier": "power",
            "t": "Timed by cyclins and kinases; Hartwell, Hunt (who found cyclins in sea urchin eggs), and Nurse shared the 2001 Nobel Prize",
            "k": ["cyclins", "sea urchin", "2001", "hartwell", "nurse"],
            "n": 0
        },
        {
            "id": "checkpoint",
            "tier": "power",
            "t": "The spindle assembly checkpoint holds off anaphase until every kinetochore is attached",
            "k": ["spindle assembly checkpoint", "checkpoint"],
            "n": 0
        },
        {
            "id": "colchicine",
            "tier": "power",
            "t": "Colchicine blocks spindle formation and stops cells at metaphase, which helps in making karyotypes",
            "k": ["colchicine", "karyotypes"],
            "n": 0
        },
        {
            "id": "taxol-vinca",
            "tier": "power",
            "t": "Cancer drugs Taxol (from the Pacific yew) and vinblastine (from the Madagascar periwinkle) block it",
            "k": ["taxol", "pacific yew", "vinblastine", "periwinkle"],
            "n": 0
        },
        {
            "id": "closed",
            "tier": "power",
            "t": "In many fungi, including yeasts, it is “closed”: the nuclear envelope never breaks down",
            "k": ["closed", "fungi", "yeasts"],
            "n": 0,
            "rabbit": "Yeast"
        },
        {
            "id": "phragmoplast",
            "tier": "power",
            "t": "Plant cells mark the dividing line with a preprophase band, and a phragmoplast builds the cell plate from Golgi vesicles",
            "k": ["phragmoplast", "preprophase band", "golgi"],
            "n": 0
        },
        {
            "id": "hayflick",
            "tier": "power",
            "t": "Hayflick limit: normal human cells can divide only about 40 to 60 times as their telomeres shorten",
            "k": ["hayflick", "telomeres", "40 to 60"],
            "n": 0
        },
        {
            "id": "virchow",
            "tier": "power",
            "t": "Rudolf Virchow popularized “omnis cellula e cellula”: every cell comes from another cell",
            "k": ["virchow", "omnis cellula", "every cell"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Whole process, or one stage?",
        "body": "Mitosis and meiosis sound alike and share stage names (prophase, metaphase, anaphase, telophase), so one wrong vowel costs the tossup. Many tossups also spend their power clues on a single stage, which tempts players to buzz with “anaphase” or “prophase” when the question wants the whole process. Cytokinesis, the splitting of the cytoplasm, is a separate step that usually follows it.",
        "fix": "Two identical cells, growth, repair, or onion root tips mean mitosis; four haploid cells, gametes, crossing over, or tetrads mean meiosis. If the question says “this process” or “this kind of cell division,” never answer with a stage name.",
        "line": "Real answer line: <b><u>Mitosis</u></b> (accept <u>karyokinesis</u> or <u>M phase</u>; prompt on <u>cell division</u>; do not accept “meiosis” or the name of a single stage)"
    },
    "tests": {
        "right": [
            "Mitosis",
            "mitosis",
            "Mytosis",
            "Karyokinesis",
            "M phase"
        ],
        "prompt": [
            "Cell division",
            "Cell cycle"
        ],
        "wrong": [
            "Meiosis",
            "Cytokinesis",
            "Prophase",
            "Anaphase",
            "Interphase",
            "Binary fission"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
