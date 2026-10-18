import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "bacteria",
    "name": "Bacteria",
    "mono": "BAC",
    "category": "Biology",
    "qbCategory": "Science · Biology",
    "kicker": "Single-celled prokaryotes · A few cause disease; most are harmless or helpful",
    "dates": "First described by Leeuwenhoek in the 1670s",
    "briefing": "Bacteria are single-celled living things far too small to see without a microscope, yet they live almost everywhere: in soil, in boiling hot springs, and by the trillions in your own gut. Antonie van Leeuwenhoek first spotted them through his homemade microscopes in the 1670s and called them “animalcules.” A few cause illnesses like strep throat, but most are harmless or helpful, from the ones that turn milk into yogurt to the ones that help bean plants get nitrogen.",
    "answerHtml": "<b><u>Bacteria</u></b> (accept <u>bacterium</u> or <u>eubacteria</u>; prompt on <u>prokaryotes</u>, <u>microbes</u>, or <u>germs</u>; do not accept “archaea” or “viruses”)",
    "accept": [
        "bacteria",
        "bacterium",
        "eubacteria",
        "eubacterium",
        "domain bacteria",
        "kingdom bacteria",
        "bacterial cells",
        "bacterial cell"
    ],
    "prompt": [
        "prokaryotes",
        "prokaryote",
        "procaryotes",
        "procaryote",
        "prokaryotic cells",
        "microbes",
        "microbe",
        "microorganisms",
        "microorganism",
        "germs",
        "germ",
        "monera",
        "kingdom monera"
    ],
    "reject": [
        "archaea",
        "archaeon",
        "archaebacteria",
        "archaebacterium",
        "viruses",
        "virus",
        "phages",
        "phage",
        "bacteriophages",
        "bacteriophage",
        "bacterial conjugation",
        "cyanobacteria",
        "e coli",
        "escherichia coli",
        "bacilli",
        "bacillus",
        "cocci",
        "fungi",
        "fungus",
        "protists",
        "prions",
        "algae",
        "yeast",
        "mold",
        "eukaryotes",
        "antibiotics",
        "penicillin",
        "bactria",
        "santeria"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Bacteria",
    "qb": {
        "q": "bacteria",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "Carl Woese compared ribosomal RNA from many microbes in 1977 and concluded that the archaea, long lumped together with this group, form a very different branch of life. Unlike archaea, most members of this domain build their cell walls out of peptidoglycan [“pep-tih-doh-GLY-kan”].",
            "r": "Members of this domain reproduce by binary fission. For 10 points, name these single-celled prokaryotes, some of which cause strep throat and tuberculosis."
        },
        {
            "p": "In the 1960s, Thomas Brock found a heat-loving species of these organisms in a Yellowstone hot spring, and its heat-resistant enzyme, Taq polymerase, later made it possible to copy DNA quickly using PCR. That species is named Thermus aquaticus [“THER-mus uh-KWAT-ih-kus”].",
            "r": "These organisms have no nucleus and usually keep their DNA in one circular chromosome. For 10 points, name these prokaryotes that can be killed by antibiotics."
        },
        {
            "p": "Jennifer Doudna and Emmanuelle Charpentier won the 2020 Nobel Prize in Chemistry for turning CRISPR, a defense system these organisms use against invading viruses, into a tool for editing genes. The viruses that infect these organisms are called phages.",
            "r": "Antibiotics such as penicillin kill these organisms but do not work on viruses. For 10 points, name these single-celled prokaryotes."
        },
        {
            "p": "Frederick Griffith showed in 1928 that a harmless “rough” strain of one species of these organisms could turn deadly to mice after being mixed with a heat-killed “smooth” strain, a change later called transformation. These organisms can also swap small rings of DNA called plasmids.",
            "r": "For 10 points, name these prokaryotes that reproduce by splitting in two, a process called binary fission."
        },
        {
            "p": "In a 1683 letter, Antonie van Leeuwenhoek [“LAY-vun-hook”] described these organisms in plaque scraped from his own teeth, calling them tiny “animalcules.” Robert Koch later proved that specific types of these organisms cause the diseases anthrax and tuberculosis.",
            "r": "For 10 points, name these microbes, some of which cause illnesses that can be treated with antibiotics."
        },
        {
            "p": "The Hawaiian bobtail squid hides its shadow using light made by Vibrio fischeri [“VIB-ree-oh FISH-er-eye”], a species of these organisms that glows only when enough of its members gather, a process called quorum sensing.",
            "r": "Many of these organisms swim using whip-like flagella. For 10 points, name these prokaryotes, whose shapes include round cocci and rod-shaped bacilli."
        },
        {
            "p": "MRSA is a strain of Staphylococcus aureus, one of these organisms, that resists the antibiotic methicillin. In 1928, Alexander Fleming noticed that a mold growing in a petri dish had killed the colonies of these organisms around it.",
            "r": "That mold made penicillin. For 10 points, name these single-celled microbes that are killed by antibiotics."
        },
        {
            "p": "Clostridium and Bacillus are types of these organisms that can survive boiling, drying, and harsh chemicals by forming tough, dormant endospores. In 1876, Robert Koch showed that one rod-shaped species of these organisms causes the disease anthrax.",
            "r": "Like all members of their domain, these organisms have no nucleus. For 10 points, name these single-celled prokaryotes, which reproduce by binary fission."
        },
        {
            "p": "Fanny Hesse suggested that her husband, who worked with Robert Koch, grow these organisms on agar, a jelly made from seaweed. In 1887, Koch’s assistant Julius Petri invented a shallow covered dish for growing them.",
            "r": "Koch’s postulates are rules for proving that one of these organisms causes a disease. For 10 points, name these germs, some of which cause strep throat."
        },
        {
            "p": "Rocky mounds called stromatolites [“stroh-MAT-uh-lyts”] were built in shallow seas by a group of these organisms that was once misnamed blue-green algae. That group’s photosynthesis began filling Earth’s air with oxygen about 2.4 billion years ago, in the Great Oxidation Event.",
            "r": "Like all members of their domain, they lack a nucleus. For 10 points, name these prokaryotes, which include E. coli."
        },
        {
            "p": "The antibiotic streptomycin attacks the small 70S ribosomes of these organisms, which differ from the larger 80S ribosomes in human cells. Penicillin works by stopping these organisms from building cell walls out of peptidoglycan.",
            "r": "These organisms can be sorted into two groups by Gram staining. For 10 points, name these single-celled prokaryotes, some of which cause strep throat and cholera."
        },
        {
            "p": "During conjugation, one of these organisms can pass a copy of a plasmid to a neighbor through a tube called a pilus. Viruses called phages can also carry genes from one of these organisms to another, in a process called transduction.",
            "r": "These organisms reproduce by binary fission. For 10 points, name these prokaryotes, some of which have become resistant to antibiotics."
        },
        {
            "p": "According to the endosymbiotic theory, mitochondria began as one of these organisms that was swallowed by a larger cell. Rhizobium [“ry-ZOH-bee-um”], a type of these organisms that lives in nodules on the roots of beans and peas, turns nitrogen from the air into a form plants can use.",
            "r": "Along with fungi, these organisms are important decomposers. For 10 points, name these microbes that include E. coli."
        },
        {
            "p": "Yersinia pestis [“yer-SIN-ee-uh PES-tis”], a species of these organisms, caused the Black Death in the 1300s. Another species, E. coli, lives in the human large intestine, where gut members of this group help make vitamin K.",
            "r": "For 10 points, name these single-celled organisms that lack a nucleus, some of which cause diseases treated with antibiotics."
        },
        {
            "p": "In a test developed by Hans Christian Gram in 1884, these organisms are stained with purple crystal violet and then a pink dye called safranin. Types with thick peptidoglycan walls stay purple, while types with a thin wall and an outer membrane turn pink.",
            "r": "Their three main shapes are cocci, bacilli, and spirilla. For 10 points, name these single-celled prokaryotes."
        }
    ],
    "clues": [
        {
            "id": "prokaryotes",
            "tier": "giveaway",
            "t": "Single-celled prokaryotes: they have no nucleus and no membrane-bound organelles",
            "k": ["prokaryotes", "nucleus", "single-celled"],
            "n": 0
        },
        {
            "id": "shapes",
            "tier": "giveaway",
            "t": "Three main shapes: round cocci, rod-shaped bacilli, and spiral spirilla",
            "k": ["cocci", "bacilli", "spirilla", "shapes"],
            "n": 0
        },
        {
            "id": "antibiotics",
            "tier": "giveaway",
            "t": "Killed by antibiotics such as penicillin, which do not work on viruses",
            "k": ["antibiotics", "penicillin"],
            "n": 0,
            "rabbit": "Penicillin"
        },
        {
            "id": "diseases",
            "tier": "giveaway",
            "t": "Some cause diseases such as strep throat, tuberculosis, and cholera",
            "k": ["strep throat", "tuberculosis", "cholera"],
            "n": 0,
            "rabbit": "Cholera"
        },
        {
            "id": "binary-fission",
            "tier": "giveaway",
            "t": "Reproduce by splitting in two, a process called binary fission",
            "k": ["binary fission", "splitting"],
            "n": 0
        },
        {
            "id": "peptidoglycan",
            "tier": "middle",
            "t": "Their cell walls are built from peptidoglycan; penicillin stops them from building those walls",
            "k": ["peptidoglycan", "cell walls"],
            "n": 0,
            "rabbit": "Cell wall"
        },
        {
            "id": "gram-stain",
            "tier": "middle",
            "t": "Gram staining (Hans Christian Gram, 1884) sorts them into purple Gram-positive and pink Gram-negative types",
            "k": ["gram", "gram-positive", "gram-negative", "staining"],
            "n": 0
        },
        {
            "id": "leeuwenhoek",
            "tier": "middle",
            "t": "First seen by Antonie van Leeuwenhoek, who called them “animalcules”; in 1683 he found them in plaque from his teeth",
            "k": ["leeuwenhoek", "animalcules", "plaque"],
            "n": 0
        },
        {
            "id": "plasmids",
            "tier": "middle",
            "t": "Usually keep one circular chromosome in a region called the nucleoid, plus small DNA rings called plasmids",
            "k": ["plasmids", "nucleoid", "circular"],
            "n": 0
        },
        {
            "id": "koch",
            "tier": "middle",
            "t": "Robert Koch linked specific ones to anthrax (1876) and tuberculosis (1882); Koch’s postulates test whether a microbe causes a disease",
            "k": ["koch", "postulates", "anthrax"],
            "n": 0,
            "rabbit": "Louis Pasteur"
        },
        {
            "id": "fleming",
            "tier": "middle",
            "t": "Alexander Fleming discovered penicillin in 1928 when a mold killed the colonies growing in his petri dish",
            "k": ["fleming", "mold", "petri dish", "1928"],
            "n": 0
        },
        {
            "id": "nitrogen-fixation",
            "tier": "middle",
            "t": "Rhizobium in root nodules of beans and peas turns nitrogen from the air into a form plants can use",
            "k": ["rhizobium", "nodules", "nitrogen"],
            "n": 0
        },
        {
            "id": "gut-e-coli",
            "tier": "middle",
            "t": "E. coli lives in the human large intestine, where gut species help make vitamin K",
            "k": ["vitamin k", "intestine", "e. coli"],
            "n": 0,
            "rabbit": "E. coli"
        },
        {
            "id": "decomposers-flagella",
            "tier": "middle",
            "t": "Important decomposers along with fungi; many swim with whip-like flagella and grip surfaces with hair-like pili",
            "k": ["decomposers", "flagella", "pili"],
            "n": 0
        },
        {
            "id": "woese",
            "tier": "power",
            "t": "Carl Woese compared ribosomal RNA in 1977 and split prokaryotes into two groups, later called domains: these and the archaea",
            "k": ["woese", "ribosomal rna", "archaea", "domains"],
            "n": 0
        },
        {
            "id": "ribosomes-70s",
            "tier": "power",
            "t": "Their small 70S ribosomes differ from the 80S ribosomes in human cells, so streptomycin can attack them",
            "k": ["streptomycin", "70s", "ribosomes"],
            "n": 0
        },
        {
            "id": "endospores",
            "tier": "power",
            "t": "Clostridium and Bacillus survive boiling and drying as tough, dormant endospores",
            "k": ["endospores", "clostridium", "dormant"],
            "n": 0
        },
        {
            "id": "griffith",
            "tier": "power",
            "t": "Frederick Griffith’s 1928 experiment with “rough” and “smooth” strains in mice revealed transformation",
            "k": ["griffith", "transformation", "smooth"],
            "n": 0
        },
        {
            "id": "conjugation",
            "tier": "power",
            "t": "Swap plasmids through a pilus in conjugation; viruses called phages carry genes between them in transduction",
            "k": ["conjugation", "transduction", "phages"],
            "n": 0,
            "rabbit": "Bacterial conjugation"
        },
        {
            "id": "crispr",
            "tier": "power",
            "t": "CRISPR began as their defense against viruses; Jennifer Doudna and Emmanuelle Charpentier won the 2020 Chemistry Nobel for making it a gene-editing tool",
            "k": ["crispr", "doudna", "charpentier"],
            "n": 0
        },
        {
            "id": "taq",
            "tier": "power",
            "t": "Taq polymerase, used to copy DNA in PCR, comes from Thermus aquaticus, found by Thomas Brock in a Yellowstone hot spring",
            "k": ["taq polymerase", "thermus aquaticus", "yellowstone", "pcr"],
            "n": 0
        },
        {
            "id": "mrsa",
            "tier": "power",
            "t": "MRSA is a strain of Staphylococcus aureus that resists the antibiotic methicillin",
            "k": ["mrsa", "methicillin", "staphylococcus"],
            "n": 0
        },
        {
            "id": "quorum-sensing",
            "tier": "power",
            "t": "Quorum sensing: chemical signals let them sense their own numbers, as when Vibrio fischeri glow inside the Hawaiian bobtail squid",
            "k": ["quorum sensing", "vibrio fischeri", "bobtail squid"],
            "n": 0
        },
        {
            "id": "petri-agar",
            "tier": "power",
            "t": "Grown on agar (suggested by Fanny Hesse) in shallow dishes invented in 1887 by Koch’s assistant Julius Petri",
            "k": ["agar", "fanny hesse", "julius petri", "1887"],
            "n": 0
        },
        {
            "id": "oxygen-stromatolites",
            "tier": "power",
            "t": "A photosynthetic group once called blue-green algae built stromatolites and filled the air with oxygen starting about 2.4 billion years ago",
            "k": ["blue-green algae", "stromatolites", "great oxidation"],
            "n": 0
        },
        {
            "id": "endosymbiosis",
            "tier": "power",
            "t": "Endosymbiotic theory: mitochondria and chloroplasts began as ancient ones swallowed by a larger cell",
            "k": ["endosymbiotic", "mitochondria", "chloroplasts"],
            "n": 0
        },
        {
            "id": "black-death",
            "tier": "power",
            "t": "Yersinia pestis, one species, caused the Black Death in the 1300s",
            "k": ["yersinia pestis", "black death", "1300s"],
            "n": 0,
            "rabbit": "Black Death"
        }
    ],
    "trap": {
        "title": "Bacteria, archaea, or viruses?",
        "body": "Bacteria and archaea are both single-celled prokaryotes with no nucleus, and until Carl Woese’s work in 1977 they were lumped together. Viruses are not cells at all and are not killed by antibiotics. Saying “prokaryotes,” “microbes,” or “germs” is too general and earns only a prompt.",
        "fix": "Peptidoglycan walls, Gram staining, antibiotics, penicillin, E. coli, and diseases like strep throat mean bacteria. Life in extreme places, methane-making, and “the third domain” mean archaea. A protein capsid and needing a host cell to copy itself mean viruses.",
        "line": "Real answer line: <b><u>Bacteria</u></b> (accept <u>bacterium</u>; prompt on <u>prokaryotes</u> or <u>microbes</u>; do not accept “archaea” or “viruses”)"
    },
    "tests": {
        "right": [
            "Bacteria",
            "bacterium",
            "Bactera",
            "Eubacteria",
            "domain Bacteria"
        ],
        "prompt": [
            "Prokaryotes",
            "microbes",
            "germs"
        ],
        "wrong": [
            "Archaea",
            "Viruses",
            "Cyanobacteria",
            "E. coli",
            "Fungi",
            "Bacteriophage",
            "Santeria"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
