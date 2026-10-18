import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "proteins",
    "name": "Proteins",
    "mono": "PRT",
    "category": "Biology",
    "qbCategory": "Science · Biology",
    "kicker": "Folded chains of amino acids · They do most of the work in every cell",
    "dates": "Named by Berzelius in 1838",
    "briefing": "Proteins are long chains of amino acids that fold into precise 3D shapes, and each shape decides the job. Some are enzymes that speed up chemical reactions, some are antibodies that fight germs, and some, like keratin and collagen, build hair, nails, and skin. Cells build them on ribosomes by following instructions copied from genes, so a single change in a gene can change a protein’s shape.",
    "answerHtml": "<b><u>Proteins</u></b> (accept <u>protein</u> or <u>polypeptides</u>; prompt on <u>peptides</u>; do not accept “amino acids” or “enzymes”)",
    "accept": [
        "proteins",
        "protein",
        "polypeptides",
        "polypeptide",
        "polypeptide chains",
        "polypeptide chain"
    ],
    "prompt": [
        "peptides",
        "peptide",
        "peptide chains",
        "peptide chain"
    ],
    "reject": [
        "amino acids",
        "amino acid",
        "enzymes",
        "enzyme",
        "protons",
        "proton",
        "prions",
        "prion",
        "protists",
        "carbohydrates",
        "lipids",
        "fats",
        "nucleic acids",
        "peptide bond",
        "peptide bonds",
        "protein synthesis",
        "translation",
        "ribosomes",
        "hemoglobin",
        "keratin",
        "collagen"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Protein",
    "qb": {
        "q": "protein",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "Cyrus Levinthal pointed out that one of these molecules could never fold in a reasonable time by randomly testing every possible shape, yet many fold in less than a second. Christian Anfinsen showed that one of these molecules, ribonuclease, refolds correctly on its own after being unfolded, proving that its sequence determines its shape.",
            "r": "Ribosomes link amino acids together to build these molecules. For 10 points, name these large molecules, such as enzymes and antibodies."
        },
        {
            "p": "In 2024, Demis Hassabis and John Jumper shared a Nobel Prize for AlphaFold, an artificial intelligence program that predicts the folded shapes of these molecules. David Baker shared the same prize for designing brand-new examples of these molecules on computers.",
            "r": "Ribosomes build these molecules by linking amino acids. For 10 points, name these biomolecules, which include enzymes and antibodies."
        },
        {
            "p": "Linus Pauling and Robert Corey proposed two common patterns in the shapes of these molecules, the alpha helix and the beta pleated sheet, which are held together by hydrogen bonds. Those patterns make up the secondary level of these molecules’ structure.",
            "r": "Most enzymes are examples of these molecules. For 10 points, name these molecules made of amino acids linked by peptide bonds."
        },
        {
            "p": "Frederick Sanger won his first Nobel Prize for working out the exact order of building blocks in one of these molecules, insulin. That order, which is spelled out by a gene, is called the primary structure of one of these molecules.",
            "r": "For 10 points, name these large molecules that ribosomes build from chains of amino acids."
        },
        {
            "p": "John Kendrew used X-ray crystallography to reveal the first three-dimensional structure of one of these molecules, myoglobin, while Max Perutz solved hemoglobin, which has four subunits. Hemoglobin’s four fitted-together chains are an example of these molecules’ quaternary [“KWAH-ter-nair-ee”] structure.",
            "r": "For 10 points, name these biomolecules made of amino acids, which include enzymes and antibodies."
        },
        {
            "p": "Jöns Jacob Berzelius [“ber-ZEE-lee-us”] suggested the name for this class of molecules in 1838, from a Greek word meaning “primary” or “of first importance.” Unlike carbohydrates and fats, these molecules always contain nitrogen, in the amino groups of their building blocks.",
            "r": "For 10 points, name this class of nutrients, found in meat, eggs, and beans, that are made of amino acids."
        },
        {
            "p": "Stanley Prusiner won a Nobel Prize for discovering prions [“PREE-onz”], misfolded versions of these molecules that force normal copies to misfold, leading to mad cow disease. Sickle-cell disease comes from swapping just one building block, valine for glutamic acid, in one of these molecules, hemoglobin.",
            "r": "Ribosomes build these molecules from amino acids. For 10 points, name these large biomolecules, which include enzymes, antibodies, and keratin."
        },
        {
            "p": "Barrel-shaped “chaperones” such as GroEL give newly made copies of these molecules a sheltered space in which to fold into the right shape. Cells tag worn-out examples of these molecules with a small marker called ubiquitin [“yoo-BIK-wih-tin”] so they can be chopped up and recycled.",
            "r": "For 10 points, name these molecules, such as enzymes and antibodies, that are made of chains of amino acids."
        },
        {
            "p": "Cooking an egg turns its clear white solid and opaque because heat unfolds, or denatures, these molecules in it. Strong acids and bases can also denature these molecules, destroying the shapes that let them do their jobs.",
            "r": "Most enzymes are examples of these molecules. For 10 points, name these biomolecules, which are chains of amino acids."
        },
        {
            "p": "In the lab, a blue solution called biuret [“bye-yuh-RET”] reagent turns violet when mixed with these molecules, because it reacts with the bonds that link their building blocks. Those bonds, called peptide bonds, form in dehydration synthesis reactions that each release a molecule of water.",
            "r": "For 10 points, name these nutrients found in meat and beans, which are made of amino acids."
        },
        {
            "p": "Hair perms work by breaking and remaking disulfide bridges, links between sulfur atoms on cysteine [“SIS-teen”] units that help hold these molecules in shape. Collagen, the most abundant one of these molecules in the human body, is a fibrous example.",
            "r": "Keratin, which makes up hair and nails, is another one. For 10 points, name these large biomolecules built from amino acids."
        },
        {
            "p": "Each chain in these molecules has an amino end, called the N-terminus, and a carboxyl end, called the C-terminus. Their building blocks come in 20 common kinds, each with a different side chain, or R group.",
            "r": "Ribosomes build these molecules starting from the amino end. For 10 points, name these molecules whose structure has primary, secondary, tertiary, and quaternary levels."
        },
        {
            "p": "A glowing green example of these molecules, first found in the jellyfish _Aequorea victoria_ [“ee-KWOR-ee-uh vik-TOR-ee-uh”], earned a 2008 Nobel Prize because it lets scientists make living cells light up. The largest known one of these molecules, titin [“TYE-tin”], works like a spring inside muscle cells.",
            "r": "Actin and myosin, which make muscles contract, are also examples of these molecules. For 10 points, name these large molecules built from amino acids."
        },
        {
            "p": "Water-fearing side chains tend to cluster in the middle of these molecules as they fold, helping form their tertiary [“TUR-shee-air-ee”] structure. In some of these molecules, several folded chains fit together, forming a quaternary structure.",
            "r": "Ribosomes assemble these molecules by reading messenger RNA. For 10 points, name these macromolecules made of amino acids."
        },
        {
            "p": "Messenger RNA carries instructions from DNA to ribosomes, where they are translated into these molecules, the last step of the “central dogma” of molecular biology. Antibodies that fight germs and the hormone insulin are both examples of these molecules.",
            "r": "For 10 points, name these nutrients found in meat, eggs, and beans, which are made of amino acids."
        }
    ],
    "clues": [
        {
            "id": "amino-acids",
            "tier": "giveaway",
            "t": "Chains of amino acids linked by peptide bonds",
            "k": ["amino acids", "peptide bonds"],
            "n": 0,
            "rabbit": "Amino acids"
        },
        {
            "id": "ribosomes",
            "tier": "giveaway",
            "t": "Built by ribosomes, which translate messenger RNA, the last step of the “central dogma”",
            "k": ["ribosomes", "messenger rna", "central dogma"],
            "n": 0,
            "rabbit": "Ribosomes"
        },
        {
            "id": "food",
            "tier": "giveaway",
            "t": "A nutrient in meat, eggs, beans, and nuts that the body uses to build and repair tissue",
            "k": ["meat", "eggs", "beans", "repair"],
            "n": 0
        },
        {
            "id": "jobs",
            "tier": "giveaway",
            "t": "Most enzymes, all antibodies, and hormones like insulin are examples",
            "k": ["enzymes", "antibodies", "insulin"],
            "n": 0,
            "rabbit": "Enzymes"
        },
        {
            "id": "twenty",
            "tier": "giveaway",
            "t": "Built from 20 common kinds of building blocks, each with a different side chain (R group)",
            "k": ["side chain", "r group", "20 common"],
            "n": 0
        },
        {
            "id": "four-levels",
            "tier": "middle",
            "t": "Have up to four levels of structure: primary (the amino acid order), secondary, tertiary, and quaternary",
            "k": ["primary", "secondary", "tertiary", "quaternary"],
            "n": 0
        },
        {
            "id": "secondary",
            "tier": "middle",
            "t": "Secondary structure: alpha helices and beta pleated sheets, held by hydrogen bonds",
            "k": ["alpha helices", "beta pleated sheets", "hydrogen bonds"],
            "n": 0
        },
        {
            "id": "quaternary",
            "tier": "middle",
            "t": "Quaternary structure: several chains fit together, like hemoglobin’s four subunits",
            "k": ["hemoglobin", "four subunits"],
            "n": 0,
            "rabbit": "Hemoglobin"
        },
        {
            "id": "denature",
            "tier": "middle",
            "t": "Heat or harsh acids and bases unfold (denature) them, as when an egg white turns solid",
            "k": ["denature", "egg white", "unfold"],
            "n": 0
        },
        {
            "id": "biuret",
            "tier": "middle",
            "t": "Biuret reagent turns from blue to violet when they are present",
            "k": ["biuret", "violet"],
            "n": 0
        },
        {
            "id": "dehydration",
            "tier": "middle",
            "t": "Each peptide bond forms by dehydration synthesis, releasing a molecule of water",
            "k": ["dehydration synthesis", "water"],
            "n": 0
        },
        {
            "id": "disulfide",
            "tier": "middle",
            "t": "Disulfide bridges between cysteines hold their shape; hair perms break and remake them",
            "k": ["disulfide", "cysteines", "perms"],
            "n": 0
        },
        {
            "id": "collagen-keratin",
            "tier": "middle",
            "t": "Collagen is the most abundant one in the human body; keratin makes up hair and nails",
            "k": ["collagen", "keratin", "most abundant"],
            "n": 0,
            "rabbit": "Collagen"
        },
        {
            "id": "sickle",
            "tier": "middle",
            "t": "Sickle-cell disease comes from one swap, valine for glutamic acid, in hemoglobin",
            "k": ["sickle-cell", "valine", "glutamic acid"],
            "n": 0,
            "rabbit": "Sickle-cell disease"
        },
        {
            "id": "levinthal",
            "tier": "power",
            "t": "Levinthal’s paradox: a chain could never test every shape in time, yet many fold in under a second",
            "k": ["levinthal", "paradox"],
            "n": 0
        },
        {
            "id": "anfinsen",
            "tier": "power",
            "t": "Christian Anfinsen showed unfolded ribonuclease refolds by itself, so sequence determines shape",
            "k": ["anfinsen", "ribonuclease"],
            "n": 0
        },
        {
            "id": "alphafold",
            "tier": "power",
            "t": "AlphaFold predicts their shapes; Demis Hassabis and John Jumper shared the 2024 Nobel Prize in Chemistry with designer David Baker",
            "k": ["alphafold", "hassabis", "david baker", "2024"],
            "n": 0
        },
        {
            "id": "pauling",
            "tier": "power",
            "t": "Linus Pauling and Robert Corey proposed the alpha helix and beta sheet (1951)",
            "k": ["pauling", "corey", "1951"],
            "n": 0
        },
        {
            "id": "sanger",
            "tier": "power",
            "t": "Frederick Sanger first worked out the full amino acid order of one, insulin (his first Nobel Prize, 1958)",
            "k": ["sanger", "insulin", "1958"],
            "n": 0
        },
        {
            "id": "kendrew-perutz",
            "tier": "power",
            "t": "John Kendrew (myoglobin) and Max Perutz (hemoglobin) solved the first 3D shapes with X-ray crystallography",
            "k": ["kendrew", "perutz", "myoglobin", "x-ray crystallography"],
            "n": 0
        },
        {
            "id": "berzelius",
            "tier": "power",
            "t": "Jöns Jacob Berzelius suggested their name in 1838, from a Greek word meaning “primary”",
            "k": ["berzelius", "1838", "greek"],
            "n": 0
        },
        {
            "id": "prions",
            "tier": "power",
            "t": "Prions are misfolded ones that make normal copies misfold, causing mad cow disease (Stanley Prusiner, Nobel 1997)",
            "k": ["prions", "misfolded", "prusiner", "mad cow"],
            "n": 0,
            "rabbit": "Prions"
        },
        {
            "id": "chaperones",
            "tier": "power",
            "t": "Barrel-shaped chaperones like GroEL give new chains a sheltered space to fold",
            "k": ["chaperones", "groel"],
            "n": 0
        },
        {
            "id": "ubiquitin",
            "tier": "power",
            "t": "Cells tag worn-out ones with ubiquitin so they get broken down and recycled",
            "k": ["ubiquitin", "recycled"],
            "n": 0
        },
        {
            "id": "termini",
            "tier": "power",
            "t": "Each chain runs from an amino end (N-terminus) to a carboxyl end (C-terminus); ribosomes build from the amino end",
            "k": ["n-terminus", "c-terminus", "carboxyl"],
            "n": 0
        },
        {
            "id": "titin",
            "tier": "power",
            "t": "Titin, a spring-like giant in muscle, is the largest known one",
            "k": ["titin", "largest known", "spring-like"],
            "n": 0
        },
        {
            "id": "gfp",
            "tier": "power",
            "t": "A glowing green one from the jellyfish _Aequorea victoria_ earned the 2008 Nobel Prize in Chemistry",
            "k": ["jellyfish", "aequorea", "glowing"],
            "n": 0
        }
    ],
    "trap": {
        "title": "The chain, not the link",
        "body": "Many tossups describe the building blocks on the way to the giveaway (20 kinds, R groups, amino and carboxyl ends), and players buzz with “amino acids,” which are the links, not the chain. Others hear “enzyme,” “hemoglobin,” or “keratin” and name a single example instead of the whole class of molecules.",
        "fix": "If the question asks for “these monomers” or a unit with one side chain, say amino acids. If it describes folding, levels of structure, or jobs like speeding up reactions and fighting germs, say proteins (polypeptides is also fine).",
        "line": "Real answer line: <b><u>Proteins</u></b> (accept <u>polypeptides</u>; prompt on <u>peptides</u>; do not accept “amino acids” or “enzymes”)"
    },
    "tests": {
        "right": [
            "Proteins",
            "protein",
            "Polypeptides",
            "Proteens",
            "polypeptide chain"
        ],
        "prompt": [
            "Peptides"
        ],
        "wrong": [
            "Amino acids",
            "Enzymes",
            "Protons",
            "Prions",
            "Lipids"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
