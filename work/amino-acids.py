import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "amino-acids",
    "name": "Amino acids",
    "mono": "AA",
    "category": "Biology",
    "qbCategory": "Science · Biology",
    "kicker": "Building blocks of proteins · Twenty kinds spelled out by the genetic code",
    "dates": "First one found in asparagus juice, 1806",
    "briefing": "Amino acids are the small building blocks that link together, like beads on a necklace, to make every protein in your body, from the keratin in your hair to the enzymes that digest your lunch. Living things use 20 main kinds, and the order they are strung in is spelled out by the genetic code in DNA. Your body can make some of them, but nine, called essential amino acids, have to come from food.",
    "answerHtml": "<b><u>Amino acids</u></b> (accept <u>amino acid</u>; prompt on <u>acids</u>; do not accept “proteins” or “peptides”)",
    "accept": [
        "amino acids",
        "amino acid",
        "aminoacids",
        "aminoacid"
    ],
    "prompt": [
        "acids",
        "acid",
        "amino",
        "residues"
    ],
    "reject": [
        "proteins",
        "protein",
        "peptides",
        "peptide",
        "polypeptides",
        "polypeptide",
        "peptide bonds",
        "peptide bond",
        "nucleotides",
        "nucleotide",
        "nucleic acids",
        "nucleic acid",
        "fatty acids",
        "fatty acid",
        "amines",
        "amine",
        "amino group",
        "amino groups",
        "amine group",
        "carboxylic acids",
        "carboxyl group",
        "enzymes",
        "enzyme",
        "glycine",
        "monosaccharides",
        "sugars",
        "dna",
        "rna"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Amino_acid",
    "qb": {
        "q": "amino acid",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "Forensic scientists spray ninhydrin [“nin-HY-drin”] on paper to reveal fingerprints, because it turns purple when it reacts with these molecules left behind in sweat. Ribosomes join these molecules into long chains using peptide bonds.",
            "r": "Each one has a central carbon bonded to an amine group, a carboxyl group, and a side chain. For 10 points, name these building blocks of proteins."
        },
        {
            "p": "In a famous 1950s experiment, Stanley Miller and Harold Urey sent electric sparks through a flask of methane, ammonia, hydrogen, and water vapor and produced several of these molecules. The simplest of these molecules, glycine, has just a hydrogen atom as its side chain.",
            "r": "For 10 points, name these molecules that are joined by peptide bonds to build proteins."
        },
        {
            "p": "The Murchison meteorite, which fell in Australia in 1969, contained dozens of kinds of these molecules, including many that living things on Earth never use. Living things build their proteins from 20 standard kinds of these molecules.",
            "r": "For 10 points, name these molecules, each containing an amine group and a carboxyl group."
        },
        {
            "p": "The first of these molecules ever discovered was isolated from asparagus juice in 1806, and William Cumming Rose discovered the last of the 20 common ones, threonine, in the 1930s. Rose also showed which of these molecules people must get from food.",
            "r": "Nine of them are called “essential” for humans. For 10 points, name these building blocks that ribosomes join together to make proteins."
        },
        {
            "p": "Selenocysteine, which contains the element selenium, is sometimes called the 21st of these molecules, and pyrrolysine [“peer-oh-LY-seen”], used by some archaea, is called the 22nd. In a protein, the order of these molecules is called its primary structure.",
            "r": "Transfer RNA carries them to the ribosome. For 10 points, name these molecules that ribosomes link together with peptide bonds."
        },
        {
            "p": "At a particular pH called the isoelectric point, one of these molecules carries no net charge, and in water at neutral pH, these molecules exist as zwitterions [“TSVIT-er-eye-unz”], with both a positive and a negative charge.",
            "r": "Their side chains, called R groups, can be polar, nonpolar, acidic, or basic. For 10 points, name these 20 kinds of molecules that make up proteins."
        },
        {
            "p": "All of these molecules except glycine are chiral, and proteins in living things are built almost entirely from their L-forms, though D-forms do appear in bacterial cell walls. Three-base codons in messenger RNA spell out which of these molecules comes next in a protein.",
            "r": "Nine of them are essential in the human diet. For 10 points, name these building blocks of proteins, such as glycine and lysine."
        },
        {
            "p": "In the 1950s, Vernon Ingram showed that sickle-cell disease comes from a single swap in hemoglobin, in which glutamic acid is replaced by valine. Both of those are examples of these molecules, each of which is spelled out by a three-base codon.",
            "r": "Their order in a protein is called its primary structure. For 10 points, name these molecules that are strung together to make proteins."
        },
        {
            "p": "Without vitamin C, the body cannot properly modify proline, one of these molecules, in collagen, which can lead to scurvy. In collagen’s long chains, every third one of these molecules is glycine.",
            "r": "For 10 points, name these molecules that join together through peptide bonds to make proteins like collagen and keratin."
        },
        {
            "p": "In 1908, chemist Kikunae Ikeda traced the savory “umami” taste of seaweed broth to glutamate, a form of one of these molecules, and helped turn it into the seasoning MSG. Transfer RNA molecules carry these molecules to the ribosome, matching each codon with an anticodon.",
            "r": "Each has an amine group, a carboxyl group, and an R group. For 10 points, name these building blocks of proteins."
        },
        {
            "p": "Edman degradation identifies these molecules one at a time by snipping them off the N-terminus end of a protein chain. Frederick Sanger won the 1958 Nobel Prize in Chemistry for working out the order of these molecules in insulin.",
            "r": "For 10 points, name these molecules, the building blocks of proteins, that ribosomes link with peptide bonds."
        },
        {
            "p": "Tryptophan, one of these molecules, is the raw material the body uses to make serotonin and melatonin, and it is often wrongly blamed for sleepiness after a turkey dinner. Tyrosine, another of these molecules, is used to make dopamine and adrenaline.",
            "r": "For 10 points, name these molecules, 20 kinds of which build the proteins in your body."
        },
        {
            "p": "Diet sodas sweetened with aspartame carry a warning for people with PKU, an inherited condition in which the body cannot break down phenylalanine, one of these molecules. Aspartame itself is made from two of these molecules, aspartic acid and phenylalanine.",
            "r": "For 10 points, name these building blocks of proteins, such as glycine and alanine."
        },
        {
            "p": "Sixty-one of the 64 codons in the genetic code stand for these molecules, while the other three are stop signals. The codon AUG stands for methionine, which is usually the first of these molecules in a new protein.",
            "r": "For 10 points, name these molecules, which transfer RNA carries to ribosomes to be built into proteins."
        },
        {
            "p": "Cysteine, one of these molecules, contains sulfur and can form disulfide bridges that hold the keratin in hair in shape, which is why hair perms work by breaking and re-forming those bonds. When two of these molecules join, a water molecule is released.",
            "r": "Your body cannot make nine of them. For 10 points, name these building blocks of proteins, linked by peptide bonds."
        }
    ],
    "clues": [
        {
            "id": "building-blocks",
            "tier": "giveaway",
            "t": "The building blocks (monomers) of proteins",
            "k": ["building blocks", "monomers"],
            "n": 0,
            "rabbit": "Proteins"
        },
        {
            "id": "twenty",
            "tier": "giveaway",
            "t": "Living things build their proteins from 20 standard kinds",
            "k": ["20 standard", "standard"],
            "n": 0
        },
        {
            "id": "peptide-bonds",
            "tier": "giveaway",
            "t": "Linked by peptide bonds into chains called polypeptides",
            "k": ["peptide bonds", "polypeptides"],
            "n": 0
        },
        {
            "id": "essential",
            "tier": "giveaway",
            "t": "Nine are “essential” for humans: the body cannot make them, so they must come from food",
            "k": ["essential", "nine", "food"],
            "n": 0
        },
        {
            "id": "structure",
            "tier": "giveaway",
            "t": "Each has a central carbon bonded to an amine group, a carboxyl group, a hydrogen, and a side chain (R group)",
            "k": ["amine group", "carboxyl group", "side chain"],
            "n": 0
        },
        {
            "id": "glycine",
            "tier": "middle",
            "t": "Glycine is the simplest: its side chain is a single hydrogen atom",
            "k": ["glycine", "simplest"],
            "n": 0,
            "rabbit": "Glycine"
        },
        {
            "id": "dehydration",
            "tier": "middle",
            "t": "Joining two of them is a dehydration (condensation) reaction that releases a water molecule",
            "k": ["dehydration", "condensation", "water molecule"],
            "n": 0
        },
        {
            "id": "codons",
            "tier": "middle",
            "t": "The genetic code uses three-base codons: 61 of the 64 codons stand for them, and three are stop codons",
            "k": ["codons", "stop codons", "genetic code"],
            "n": 0,
            "rabbit": "DNA"
        },
        {
            "id": "trna",
            "tier": "middle",
            "t": "Transfer RNA (tRNA) carries them to the ribosome, matching its anticodon to a codon",
            "k": ["transfer rna", "anticodon", "ribosome"],
            "n": 0,
            "rabbit": "Ribosomes"
        },
        {
            "id": "primary-structure",
            "tier": "middle",
            "t": "Their order in a protein is called its primary structure",
            "k": ["primary structure"],
            "n": 0
        },
        {
            "id": "methionine",
            "tier": "middle",
            "t": "The start codon AUG stands for methionine, usually the first one in a new protein",
            "k": ["methionine", "start codon"],
            "n": 0
        },
        {
            "id": "r-groups",
            "tier": "middle",
            "t": "Their R groups can be nonpolar, polar, acidic, or basic, which affects how a protein folds",
            "k": ["nonpolar", "acidic", "basic", "folds"],
            "n": 0
        },
        {
            "id": "cysteine",
            "tier": "middle",
            "t": "Cysteine contains sulfur and forms disulfide bridges that hold the keratin in hair in shape",
            "k": ["cysteine", "disulfide", "sulfur"],
            "n": 0,
            "rabbit": "Keratin"
        },
        {
            "id": "tryptophan",
            "tier": "middle",
            "t": "Tryptophan is used to make serotonin and melatonin; tyrosine is used to make dopamine and adrenaline",
            "k": ["tryptophan", "tyrosine", "serotonin"],
            "n": 0,
            "rabbit": "Serotonin"
        },
        {
            "id": "miller-urey",
            "tier": "middle",
            "t": "The Miller–Urey experiment (1950s) made several of them by sparking methane, ammonia, hydrogen, and water",
            "k": ["miller", "urey", "sparking"],
            "n": 0
        },
        {
            "id": "zwitterions",
            "tier": "power",
            "t": "At neutral pH they exist as zwitterions, with both a positive and a negative charge; at the isoelectric point the net charge is zero",
            "k": ["zwitterions", "isoelectric point"],
            "n": 0
        },
        {
            "id": "chirality",
            "tier": "power",
            "t": "All but glycine are chiral; proteins use L-forms, but D-forms appear in bacterial cell walls",
            "k": ["chiral", "l-forms", "d-forms"],
            "n": 0
        },
        {
            "id": "murchison",
            "tier": "power",
            "t": "The Murchison meteorite (Australia, 1969) carried dozens of kinds, many never used by life on Earth",
            "k": ["murchison", "meteorite", "1969"],
            "n": 0
        },
        {
            "id": "asparagine",
            "tier": "power",
            "t": "Asparagine, isolated from asparagus juice in 1806, was the first one discovered",
            "k": ["asparagine", "asparagus", "1806"],
            "n": 0
        },
        {
            "id": "threonine",
            "tier": "power",
            "t": "William Cumming Rose discovered threonine, the last of the 20 common ones, in the 1930s",
            "k": ["threonine", "william cumming rose"],
            "n": 0
        },
        {
            "id": "selenocysteine",
            "tier": "power",
            "t": "Selenocysteine (containing selenium) and pyrrolysine are sometimes called the 21st and 22nd",
            "k": ["selenocysteine", "pyrrolysine", "selenium"],
            "n": 0
        },
        {
            "id": "ninhydrin",
            "tier": "power",
            "t": "Ninhydrin turns purple when it reacts with them, revealing fingerprints on paper",
            "k": ["ninhydrin", "purple", "fingerprints"],
            "n": 0
        },
        {
            "id": "umami",
            "tier": "power",
            "t": "Kikunae Ikeda traced umami, the savory taste of seaweed broth, to glutamate in 1908; it became the seasoning MSG",
            "k": ["umami", "glutamate", "ikeda"],
            "n": 0
        },
        {
            "id": "sanger",
            "tier": "power",
            "t": "Frederick Sanger worked out their order in insulin and won the 1958 Nobel Prize in Chemistry",
            "k": ["frederick sanger", "sanger", "insulin"],
            "n": 0,
            "rabbit": "Insulin"
        },
        {
            "id": "edman",
            "tier": "power",
            "t": "Edman degradation removes and identifies them one at a time from a protein’s N-terminus",
            "k": ["edman", "n-terminus"],
            "n": 0
        },
        {
            "id": "ingram",
            "tier": "power",
            "t": "Vernon Ingram showed that sickle-cell disease comes from one swap in hemoglobin: glutamic acid replaced by valine",
            "k": ["vernon ingram", "valine", "glutamic acid"],
            "n": 0,
            "rabbit": "Sickle-cell disease"
        },
        {
            "id": "collagen",
            "tier": "power",
            "t": "Vitamin C is needed to modify proline in collagen, which prevents scurvy; every third one in collagen is glycine",
            "k": ["proline", "collagen", "scurvy"],
            "n": 0,
            "rabbit": "Collagen"
        },
        {
            "id": "pku",
            "tier": "power",
            "t": "People with PKU cannot break down phenylalanine, so aspartame, made from aspartic acid and phenylalanine, carries a warning",
            "k": ["phenylalanine", "aspartame", "pku"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Links, not chains",
        "body": "Many clues describe what these molecules build, like enzymes, keratin, collagen, or insulin, so players blurt “proteins.” But proteins are the long, folded chains, and these molecules are the single links. Nucleotides are the other trap: they are the building blocks of DNA and RNA, and clues about codons and the genetic code involve both kinds of molecules.",
        "fix": "If the question wants monomers, “building blocks,” or molecules with an R group and an amine group, say amino acids. A folded chain or a named molecule like hemoglobin means a protein; a sugar, a phosphate, and a base mean nucleotides; long carbon tails in fats mean fatty acids.",
        "line": "Real answer line: <b><u>Amino acids</u></b> (accept <u>amino acid</u>; prompt on <u>acids</u>; do not accept “proteins”)"
    },
    "tests": {
        "right": [
            "Amino acids",
            "amino acid",
            "Amino acds",
            "Aminoacids",
            "L-amino acids"
        ],
        "prompt": [
            "Acids"
        ],
        "wrong": [
            "Proteins",
            "Peptides",
            "Nucleotides",
            "Fatty acids",
            "Nucleic acids",
            "Amines"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
