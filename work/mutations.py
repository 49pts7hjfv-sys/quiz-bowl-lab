import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "mutations",
    "name": "Mutations",
    "mono": "MUT",
    "category": "Biology",
    "qbCategory": "Science · Biology",
    "kicker": "Changes in a DNA sequence · The raw material of evolution",
    "dates": "Named by Hugo de Vries in 1901",
    "briefing": "Comic-book mutants get superpowers, but real mutations are usually tiny typos in DNA, like one swapped letter in a gene’s three-letter code words. Most do nothing or cause harm, yet a few turn out to be helpful, and over many generations those rare winners supply the new variety that evolution works with. Ultraviolet light, X-rays, and some chemicals can cause mutations, though many happen by accident when cells copy their DNA.",
    "answerHtml": "<b><u>Mutations</u></b> (accept <u>mutation</u> or specific types such as point <u>mutation</u>s; prompt on descriptive answers like “genetic changes”; do not accept “mutagens,” “evolution,” or “natural selection”)",
    "accept": [
        "mutations",
        "mutation",
        "genetic mutations",
        "genetic mutation",
        "gene mutations",
        "gene mutation",
        "dna mutations",
        "dna mutation",
        "point mutations",
        "point mutation",
        "frameshift mutations",
        "frameshift mutation",
        "chromosomal mutations",
        "chromosomal mutation"
    ],
    "prompt": [
        "genetic changes",
        "genetic change",
        "dna changes",
        "dna change",
        "changes in dna",
        "change in dna"
    ],
    "reject": [
        "mutagens",
        "mutagen",
        "mutagenesis",
        "mutants",
        "mutant",
        "evolution",
        "natural selection",
        "genetic drift",
        "gene flow",
        "adaptation",
        "adaptations",
        "genetic variation",
        "variation",
        "recombination",
        "genetic recombination",
        "crossing over",
        "dna damage",
        "dna repair",
        "dna replication",
        "replication",
        "transcription",
        "translation",
        "carcinogens",
        "carcinogen",
        "cancer",
        "radiation",
        "permutations",
        "permutation",
        "dna"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Mutation",
    "qb": {
        "q": "mutation",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "In 1943, Salvador Luria and Max Delbrück [“DEL-brook”] grew many separate cultures of bacteria and counted how many cells in each one survived an attack by a virus. The counts varied wildly from culture to culture, showing that these changes arise at random before they are needed, not in response to a threat.",
            "r": "Ultraviolet light, X-rays, and some chemicals can cause them. For 10 points, name these changes in an organism’s DNA sequence."
        },
        {
            "p": "After strange new forms suddenly appeared among his evening primroses, the Dutch botanist Hugo de Vries [“duh VREES”] gave these changes their modern scientific name in 1901. A year earlier, de Vries had been one of three scientists to rediscover Gregor Mendel’s forgotten work on heredity.",
            "r": "Sickle-cell disease is caused by one of these changes. For 10 points, name these changes in a gene’s DNA sequence."
        },
        {
            "p": "Hermann J. Muller won the 1946 Nobel Prize in Physiology or Medicine for showing in 1927 that exposing fruit flies to radiation greatly raised the rate of these changes in their offspring. Muller had studied under Thomas Hunt Morgan in the famous “Fly Room” at Columbia University.",
            "r": "Muller used X-rays to cause them. For 10 points, name these changes in DNA that supply the raw material for evolution."
        },
        {
            "p": "In 1961, Francis Crick and Sydney Brenner studied these changes in a virus that infects bacteria, finding that adding one or two DNA letters to a gene wrecked it, but adding three nearby letters often let it work again. That showed the genetic code is read in three-letter words, called codons.",
            "r": "Adding or removing single letters causes a frameshift type of these changes. For 10 points, name these changes in a DNA sequence."
        },
        {
            "p": "During World War II, Charlotte Auerbach [“OW-er-bahk”] showed that mustard gas could cause these changes in fruit flies, though wartime secrecy kept her results from being published until 1946. Some chemicals in tobacco smoke can also cause these changes.",
            "r": "Ultraviolet light and X-rays can cause them too. For 10 points, name these changes in an organism’s DNA."
        },
        {
            "p": "Bruce Ames designed a test that checks whether a chemical causes these changes by counting how many Salmonella bacteria regain the ability to make the amino acid histidine. Because many chemicals that cause these changes also cause cancer, the Ames test is used to flag possible carcinogens.",
            "r": "Substitutions, insertions, and deletions are three main kinds of these. For 10 points, name these changes in an organism’s DNA sequence."
        },
        {
            "p": "People with the rare inherited condition xeroderma pigmentosum [“zeer-oh-DER-muh pig-men-TOH-sum”] are extremely sensitive to sunlight because their cells cannot properly repair thymine dimers, in which two neighboring thymine bases bond together. Left unrepaired, those dimers can turn into these permanent changes.",
            "r": "Ultraviolet light causes thymine dimers. For 10 points, name these changes in a DNA sequence, such as substitutions and deletions."
        },
        {
            "p": "Changing a single DNA letter turns the codon GAG into GTG in the gene for hemoglobin’s beta chain, putting the amino acid valine in place of glutamic acid. That swap is a classic missense example of these changes.",
            "r": "In people with two copies, it causes sickle-cell disease. For 10 points, name these changes in an organism’s DNA sequence."
        },
        {
            "p": "One kind of these changes creates an early stop codon, such as UAG, so the ribosome stops building a protein too soon and leaves it cut short. That kind is called “nonsense,” while a “missense” kind swaps one amino acid for another.",
            "r": "Some are caused by X-rays or ultraviolet light. For 10 points, name these changes in DNA, which are the source of new genetic variation."
        },
        {
            "p": "The codons GCU, GCC, GCA, and GCG all stand for the amino acid alanine, so changing the last letter of any of them is a “silent” example of these changes that leaves the protein the same. Such silent examples are possible because the genetic code is redundant.",
            "r": "Ones that occur in egg or sperm cells can be passed to offspring. For 10 points, name these changes in an organism’s DNA."
        },
        {
            "p": "Teachers often model one type of these changes by deleting a single letter from a sentence like “THE FAT CAT ATE THE RAT,” which scrambles every three-letter word after it. That type, a frameshift, happens when the number of DNA bases inserted or deleted is not a multiple of three.",
            "r": "Substitutions of a single base are another kind. For 10 points, name these changes in an organism’s DNA sequence, which can be caused by radiation."
        },
        {
            "p": "Swapping one purine base for another, such as adenine for guanine, is called a transition, while swapping a purine for a pyrimidine is called a transversion. Both are substitution types of these changes, many of which come from mistakes made when DNA is copied.",
            "r": "Ultraviolet light and X-rays can also cause them. For 10 points, name these changes in a DNA sequence."
        },
        {
            "p": "Only the germline kind of these changes, which arise in egg or sperm cells, can be passed to children, while the somatic kind, which arise in other body cells, cannot be inherited. Somatic ones in genes that control cell division, such as the p53 gene, can lead to cancer.",
            "r": "Insertions, deletions, and substitutions are three kinds of these. For 10 points, name these changes in an organism’s DNA."
        },
        {
            "p": "The most common one of these changes behind cystic fibrosis deletes three DNA bases, removing a single phenylalanine from a protein without shifting the reading frame. Deleting just one or two bases there would have caused a frameshift instead.",
            "r": "A single changed DNA letter causes sickle-cell disease. For 10 points, name these changes in an organism’s DNA sequence."
        },
        {
            "p": "Large-scale examples of these changes include inversions, in which a piece of a chromosome flips around, and translocations, like the swap between chromosomes 9 and 22 that creates the Philadelphia chromosome. Duplications copy a stretch of a chromosome, adding extra copies of genes.",
            "r": "Fictional versions give the X-Men their superpowers. For 10 points, name these changes in DNA, which supply new genetic variation for evolution."
        }
    ],
    "clues": [
        {
            "id": "dna-changes",
            "tier": "giveaway",
            "t": "Permanent changes in an organism’s DNA sequence",
            "k": ["dna sequence", "permanent", "changes"],
            "n": 0
        },
        {
            "id": "causes",
            "tier": "giveaway",
            "t": "Caused by ultraviolet light, X-rays, some chemicals, or mistakes made when cells copy their DNA",
            "k": ["ultraviolet", "x-rays", "chemicals", "mistakes"],
            "n": 0,
            "rabbit": "X-rays"
        },
        {
            "id": "raw-material",
            "tier": "giveaway",
            "t": "The source of new genetic variation, the raw material that evolution works on",
            "k": ["raw material", "variation", "evolution"],
            "n": 0,
            "rabbit": "Evolution"
        },
        {
            "id": "x-men",
            "tier": "giveaway",
            "t": "Fictional versions give comic-book heroes like the X-Men their superpowers",
            "k": ["x-men", "superpowers", "comic-book"],
            "n": 0
        },
        {
            "id": "kinds",
            "tier": "middle",
            "t": "Small-scale kinds: substitutions, insertions, and deletions of DNA bases",
            "k": ["substitutions", "insertions", "deletions"],
            "n": 0
        },
        {
            "id": "point",
            "tier": "middle",
            "t": "A “point” one changes just a single DNA base, or letter",
            "k": ["point", "single", "letter"],
            "n": 0
        },
        {
            "id": "silent-missense-nonsense",
            "tier": "middle",
            "t": "Single-base substitutions can be silent (same amino acid), missense (a different amino acid), or nonsense (an early stop codon)",
            "k": ["silent", "missense", "nonsense"],
            "n": 0
        },
        {
            "id": "frameshift",
            "tier": "middle",
            "t": "Inserting or deleting a number of bases that is not a multiple of three causes a frameshift",
            "k": ["frameshift", "multiple of three", "reading frame"],
            "n": 0
        },
        {
            "id": "sickle-cell",
            "tier": "middle",
            "t": "Sickle-cell disease comes from a one-letter DNA change (GAG to GTG) that puts valine in place of glutamic acid",
            "k": ["sickle-cell", "valine", "gag", "gtg"],
            "n": 0,
            "rabbit": "Sickle-cell disease"
        },
        {
            "id": "germline-somatic",
            "tier": "middle",
            "t": "Germline ones (in eggs or sperm) can be inherited; somatic ones (in other body cells) cannot",
            "k": ["germline", "somatic", "inherited"],
            "n": 0
        },
        {
            "id": "cancer",
            "tier": "middle",
            "t": "Ones in genes that control cell division, such as the p53 gene, can lead to cancer",
            "k": ["cancer", "p53", "cell division"],
            "n": 0,
            "rabbit": "Cancer"
        },
        {
            "id": "chromosomal",
            "tier": "middle",
            "t": "Large-scale kinds rearrange chromosomes: deletions, duplications, inversions, and translocations",
            "k": ["inversions", "translocations", "duplications"],
            "n": 0,
            "rabbit": "Chromosomes"
        },
        {
            "id": "de-vries",
            "tier": "power",
            "t": "Hugo de Vries gave them their modern name in 1901 after studying evening primroses; in 1900 he had helped rediscover Mendel’s work",
            "k": ["de vries", "evening primroses", "1901"],
            "n": 0,
            "rabbit": "Gregor Mendel"
        },
        {
            "id": "muller",
            "tier": "power",
            "t": "Hermann J. Muller, a student of Thomas Hunt Morgan, showed in 1927 that X-rays cause them in fruit flies (Nobel Prize, 1946)",
            "k": ["muller", "1927", "1946", "fruit flies"],
            "n": 0,
            "rabbit": "Fruit flies"
        },
        {
            "id": "luria-delbruck",
            "tier": "power",
            "t": "The Luria–Delbrück fluctuation test (1943) used bacteria and viruses to show they arise at random, before they are needed",
            "k": ["luria", "delbrück", "fluctuation test", "random"],
            "n": 0,
            "rabbit": "Bacteriophages"
        },
        {
            "id": "crick-brenner",
            "tier": "power",
            "t": "Crick and Brenner (1961) added DNA letters to a virus gene and showed the genetic code is read in three-letter codons",
            "k": ["crick", "brenner", "1961", "codons"],
            "n": 0
        },
        {
            "id": "auerbach",
            "tier": "power",
            "t": "Charlotte Auerbach found that mustard gas causes them in fruit flies; wartime secrecy delayed her report until 1946",
            "k": ["auerbach", "mustard gas"],
            "n": 0
        },
        {
            "id": "ames-test",
            "tier": "power",
            "t": "The Ames test checks whether a chemical causes them by watching Salmonella bacteria regain the ability to make histidine",
            "k": ["ames test", "salmonella", "histidine"],
            "n": 0
        },
        {
            "id": "thymine-dimers",
            "tier": "power",
            "t": "Ultraviolet light bonds neighboring thymine bases into thymine dimers; people with xeroderma pigmentosum cannot repair them well",
            "k": ["thymine dimers", "xeroderma pigmentosum", "thymine"],
            "n": 0
        },
        {
            "id": "redundant-code",
            "tier": "power",
            "t": "Silent ones are possible because the genetic code is redundant: GCU, GCC, GCA, and GCG all code for alanine",
            "k": ["redundant", "alanine", "gcu"],
            "n": 0
        },
        {
            "id": "stop-codons",
            "tier": "power",
            "t": "Nonsense ones create an early stop codon, such as UAG, so the protein comes out cut short",
            "k": ["stop codon", "uag", "cut short"],
            "n": 0
        },
        {
            "id": "fat-cat",
            "tier": "power",
            "t": "Classroom model: deleting one letter from “THE FAT CAT ATE THE RAT” scrambles every word after it, like a frameshift",
            "k": ["fat cat", "scrambles"],
            "n": 0
        },
        {
            "id": "transition-transversion",
            "tier": "power",
            "t": "A transition swaps a purine for a purine (A and G) or a pyrimidine for a pyrimidine (C and T); a transversion swaps a purine for a pyrimidine",
            "k": ["transition", "transversion", "purine", "pyrimidine"],
            "n": 0
        },
        {
            "id": "cystic-fibrosis",
            "tier": "power",
            "t": "The most common one behind cystic fibrosis deletes three bases, removing one phenylalanine without causing a frameshift",
            "k": ["cystic fibrosis", "phenylalanine", "three bases"],
            "n": 0,
            "rabbit": "Cystic fibrosis"
        },
        {
            "id": "philadelphia",
            "tier": "power",
            "t": "A translocation between chromosomes 9 and 22 creates the Philadelphia chromosome",
            "k": ["philadelphia", "9 and 22", "translocation"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Change, cause, or result?",
        "body": "Tossups on this answer are full of X-rays, ultraviolet light, and chemicals, so players blurt the cause, but agents that cause these changes are called mutagens, and “mutagens” is wrong. Others answer “evolution” or “natural selection,” which happen to whole populations over many generations; mutations only supply the new variation those processes act on. DNA damage is not the same thing either, because damage that gets repaired never becomes a mutation.",
        "fix": "If the question asks for “these changes” in a DNA sequence, such as substitutions, insertions, deletions, frameshifts, or silent, missense, and nonsense ones, say mutations. Save “evolution” for a population changing over generations and “genetic drift” for random changes in how common an allele is.",
        "line": "Real answer line: <b><u>Mutations</u></b> (accept <u>mutation</u> or specific types such as point <u>mutation</u>s; prompt on descriptive answers like “genetic changes”; do not accept “mutagens,” “evolution,” or “natural selection”)"
    },
    "tests": {
        "right": [
            "Mutations",
            "mutation",
            "Point mutations",
            "Frameshift mutation",
            "Mutatoins",
            "genetic mutations"
        ],
        "prompt": [
            "Genetic changes",
            "DNA changes"
        ],
        "wrong": [
            "Mutagens",
            "Evolution",
            "Natural selection",
            "Genetic drift",
            "Permutations",
            "DNA damage",
            "Mutants"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
