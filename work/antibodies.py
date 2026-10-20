import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "antibodies",
    "name": "Antibodies",
    "mono": "AB",
    "category": "Biology",
    "qbCategory": "Science · Biology",
    "kicker": "Y-shaped immune proteins · Made by B cells to grab specific antigens",
    "dates": "First found in blood serum in 1890",
    "briefing": "Antibodies are Y-shaped proteins that your B cells make to fight invaders. Each kind fits just one target, called an antigen, the way a key fits one lock, and your body can make billions of different kinds. When antibodies latch onto a virus or a toxin, they can block it or tag it for destruction, and vaccines work by teaching your body to make the right ones before you ever get sick.",
    "answerHtml": "<b><u>Antibodies</u></b> (accept <u>antibody</u> or <u>immunoglobulins</u>; do not accept “antigens” or “antibiotics”)",
    "accept": [
        "antibodies",
        "antibody",
        "immunoglobulins",
        "immunoglobulin"
    ],
    "prompt": [],
    "reject": [
        "antigen",
        "antigens",
        "antibiotic",
        "antibiotics",
        "b cells",
        "b cell",
        "b lymphocytes",
        "plasma cells",
        "plasma cell",
        "t cells",
        "t cell",
        "lymphocytes",
        "lymphocyte",
        "white blood cells",
        "white blood cell",
        "leukocytes",
        "immune system",
        "vaccines",
        "vaccine",
        "interferons",
        "interferon",
        "cytokines",
        "complement",
        "histamine",
        "allergens",
        "mast cells",
        "phagocytes",
        "macrophages",
        "hybridomas",
        "hybridoma",
        "hemoglobin",
        "enzymes"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Antibody",
    "qb": {
        "q": "antibodies",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "Rodney Porter used the enzyme papain to cut these molecules into three pieces: two identical arms that grab targets and one stem. Porter shared the 1972 Nobel Prize in Physiology or Medicine with Gerald Edelman, who showed that these molecules are built from separate heavy and light protein chains.",
            "r": "Plasma cells, which develop from B cells, release them into the blood. For 10 points, name these Y-shaped proteins that bind to antigens."
        },
        {
            "p": "Susumu Tonegawa [“toh-neh-GAH-wah”] won the 1987 Nobel Prize for showing that young B cells cut and rejoin gene segments to build a huge variety of these molecules. That shuffling, called V(D)J recombination, lets the body make billions of different kinds of them.",
            "r": "Each kind fits one antigen like a key in a lock. For 10 points, name these Y-shaped proteins made by B cells."
        },
        {
            "p": "In 1975, Georges Köhler and César Milstein fused B cells with cancer cells to create hybridomas, cell lines that pump out endless identical copies of one of these molecules. Medicines made by that method have names ending in “-mab.” Köhler and Milstein shared the 1984 Nobel Prize with Niels Jerne.",
            "r": "For 10 points, name these Y-shaped proteins of the immune system, which B cells make to bind antigens."
        },
        {
            "p": "In 1890, Emil von Behring and Kitasato Shibasaburō showed that blood serum from animals given small doses of tetanus or diphtheria toxin could protect other animals, because the serum held these molecules. Behring won the first Nobel Prize in Physiology or Medicine, in 1901, for that “serum therapy.”",
            "r": "For 10 points, name these proteins, made by B cells, that neutralize toxins by binding to antigens."
        },
        {
            "p": "Paul Ehrlich’s “side-chain theory” proposed that cells grow extra receptors that break off into the blood and become these molecules. Ehrlich shared the 1908 Nobel Prize with Élie Metchnikoff [“MECH-nih-koff”], who discovered that some white blood cells swallow germs.",
            "r": "Those cells eat germs more easily after these molecules coat them, a process called opsonization [“op-suh-nuh-ZAY-shun”]. For 10 points, name these Y-shaped proteins made by B cells."
        },
        {
            "p": "People with type O blood carry two kinds of these molecules in their plasma, one that binds the A marker and one that binds the B marker on red blood cells. People with type AB blood carry neither kind, which is why they can receive red cells of any ABO type.",
            "r": "When these molecules meet mismatched cells, the cells clump together. For 10 points, name these Y-shaped proteins of the immune system."
        },
        {
            "p": "One class of these molecules is the only class that crosses the placenta, protecting a baby during its first months of life. Another class guards wet surfaces such as tears, saliva, and mucus, and it is also passed to babies in breast milk.",
            "r": "Those classes are IgG and IgA. For 10 points, name these Y-shaped proteins, which are made by B cells."
        },
        {
            "p": "The M class of these molecules links five units into a star-shaped cluster held together by a small J chain, and it is the first class made during a new infection. The A class often travels in pairs.",
            "r": "Memory B cells help the body make them faster the second time. For 10 points, name these Y-shaped proteins that bind to antigens."
        },
        {
            "p": "The E class of these molecules coats mast cells, which release histamine when an allergen such as pollen latches onto that coating, causing sneezing and itching. That class also helps the body fight parasitic worms.",
            "r": "For 10 points, name these Y-shaped proteins, made by plasma cells, that each recognize one specific antigen."
        },
        {
            "p": "Camels and llamas make unusually small versions of these molecules that have no light chains, and scientists trim those versions into even smaller “nanobodies.” Sharks also make a version of these molecules built only from heavy chains.",
            "r": "Human versions have two heavy and two light chains in a Y shape. For 10 points, name these immune proteins that bind antigens."
        },
        {
            "p": "In myasthenia gravis [“my-us-THEE-nee-uh GRAV-iss”], these molecules block the receptors that let muscles respond to the nerve signal acetylcholine, causing weakness. In Graves’ disease, these molecules switch on the thyroid gland and make it overactive.",
            "r": "Normally, B cells make them to fight germs. For 10 points, name these Y-shaped proteins that bind to antigens."
        },
        {
            "p": "To make antivenom, scientists inject horses or sheep with small doses of snake venom and later collect these molecules from the animals’ blood. Giving a patient these molecules ready-made is called passive immunity, because the patient’s own body did not make them.",
            "r": "Vaccines, by contrast, train the body to make its own. For 10 points, name these proteins that plasma cells release to bind antigens."
        },
        {
            "p": "The tips of both arms of these molecules hold variable regions that fit one epitope, the small part of an antigen they recognize. A flexible hinge joins those arms to a stem called the Fc region, which other immune cells can grab.",
            "r": "They latch onto germs and toxins so the body can destroy them. For 10 points, name these Y-shaped proteins made by B cells and plasma cells."
        },
        {
            "p": "The ELISA [“ee-LY-zuh”] lab test links these molecules to an enzyme that causes a color change when they find their target. Home rapid tests for COVID-19 also use these molecules, which grab virus proteins and make a colored line appear.",
            "r": "In the body, B cells make them. For 10 points, name these Y-shaped proteins that recognize antigens."
        },
        {
            "p": "Frank Macfarlane Burnet’s clonal selection theory explained that each B cell makes just one kind of these molecules, and only the B cells whose kind matches an invader multiply. Some of those B cells become long-lived memory cells.",
            "r": "Vaccines work by training the body to make these molecules. For 10 points, name these Y-shaped proteins that bind antigens."
        }
    ],
    "clues": [
        {
            "id": "y-shaped",
            "tier": "giveaway",
            "t": "Y-shaped proteins that the immune system makes to latch onto antigens, the markers on germs and other invaders",
            "k": ["y-shaped", "antigens", "immune system"],
            "n": 0
        },
        {
            "id": "b-cells",
            "tier": "giveaway",
            "t": "Made by B cells; activated B cells called plasma cells release huge numbers of them",
            "k": ["b cells", "plasma cells"],
            "n": 0,
            "rabbit": "White blood cells"
        },
        {
            "id": "lock-and-key",
            "tier": "giveaway",
            "t": "Each kind fits one specific antigen, the way a key fits one lock",
            "k": ["specific antigen", "lock", "key"],
            "n": 0
        },
        {
            "id": "vaccines",
            "tier": "giveaway",
            "t": "Vaccines train the body to make them, and memory B cells make them faster the next time",
            "k": ["vaccines", "memory b cells"],
            "n": 0
        },
        {
            "id": "block-and-tag",
            "tier": "giveaway",
            "t": "They block viruses and toxins and tag germs so other immune cells can destroy them",
            "k": ["toxins", "viruses", "tag"],
            "n": 0
        },
        {
            "id": "heavy-light-chains",
            "tier": "middle",
            "t": "Built from two heavy chains and two light chains, held together by disulfide bonds",
            "k": ["heavy chains", "light chains", "disulfide bonds"],
            "n": 0
        },
        {
            "id": "variable-regions",
            "tier": "middle",
            "t": "The tips of the Y’s arms hold variable regions that fit the antigen; the stem is the Fc region",
            "k": ["variable regions", "fc region"],
            "n": 0
        },
        {
            "id": "epitope",
            "tier": "middle",
            "t": "The small part of an antigen that one of them recognizes is an epitope; a flexible hinge lets the arms swing",
            "k": ["epitope", "hinge"],
            "n": 0
        },
        {
            "id": "five-classes",
            "tier": "middle",
            "t": "Five classes: IgG (the most common in blood), IgA, IgM, IgE, and IgD",
            "k": ["five classes", "igg", "most common"],
            "n": 0
        },
        {
            "id": "placenta-milk",
            "tier": "middle",
            "t": "IgG is the only class that crosses the placenta; IgA guards tears, saliva, and mucus and is passed on in breast milk",
            "k": ["placenta", "breast milk", "saliva"],
            "n": 0
        },
        {
            "id": "ige-allergies",
            "tier": "middle",
            "t": "IgE makes mast cells release histamine in allergies, and it helps fight parasitic worms",
            "k": ["histamine", "mast cells", "allergies", "parasitic worms"],
            "n": 0
        },
        {
            "id": "igm-pentamer",
            "tier": "middle",
            "t": "IgM, the first class made in a new infection, joins five units into a star-shaped pentamer with a J chain",
            "k": ["pentamer", "j chain", "first class"],
            "n": 0
        },
        {
            "id": "blood-types",
            "tier": "middle",
            "t": "Type O plasma carries anti-A and anti-B kinds, and type AB plasma carries neither; mismatched blood clumps (agglutination)",
            "k": ["agglutination", "anti-a", "type ab"],
            "n": 0,
            "rabbit": "Blood types"
        },
        {
            "id": "passive-immunity",
            "tier": "middle",
            "t": "Receiving ready-made ones, from a mother or an antivenom shot, is passive immunity; making your own is active immunity",
            "k": ["passive immunity", "active immunity"],
            "n": 0
        },
        {
            "id": "opsonization",
            "tier": "middle",
            "t": "Coating a germ so that phagocytes can eat it more easily is called opsonization",
            "k": ["opsonization", "phagocytes"],
            "n": 0
        },
        {
            "id": "porter-edelman",
            "tier": "power",
            "t": "Rodney Porter and Gerald Edelman shared the 1972 Nobel Prize for their structure; Porter cut them apart with the enzyme papain",
            "k": ["porter", "edelman", "papain", "1972"],
            "n": 0
        },
        {
            "id": "tonegawa",
            "tier": "power",
            "t": "Susumu Tonegawa won the 1987 Nobel Prize for showing how shuffled gene segments (V(D)J recombination) create their huge variety",
            "k": ["tonegawa", "recombination", "1987"],
            "n": 0
        },
        {
            "id": "kohler-milstein",
            "tier": "power",
            "t": "Georges Köhler and César Milstein made the first hybridomas in 1975 to mass-produce monoclonal ones; they shared the 1984 Nobel Prize with Niels Jerne",
            "k": ["hybridomas", "milstein", "monoclonal", "1984"],
            "n": 0
        },
        {
            "id": "mab-names",
            "tier": "power",
            "t": "Medicines made from monoclonal ones have names ending in “-mab”",
            "k": ["-mab", "medicines"],
            "n": 0
        },
        {
            "id": "behring-kitasato",
            "tier": "power",
            "t": "Emil von Behring and Kitasato Shibasaburō found them in serum (1890); Behring won the first Nobel in Physiology or Medicine (1901) for serum therapy",
            "k": ["behring", "kitasato", "serum therapy", "1901"],
            "n": 0
        },
        {
            "id": "ehrlich",
            "tier": "power",
            "t": "Paul Ehrlich’s “side-chain theory” explained how cells make them; he shared the 1908 Nobel Prize with Élie Metchnikoff",
            "k": ["ehrlich", "side-chain theory", "metchnikoff", "1908"],
            "n": 0
        },
        {
            "id": "clonal-selection",
            "tier": "power",
            "t": "Frank Macfarlane Burnet’s clonal selection theory: each B cell makes one kind, and the B cells that match an invader multiply",
            "k": ["clonal selection", "burnet"],
            "n": 0
        },
        {
            "id": "camels-llamas",
            "tier": "power",
            "t": "Camels, llamas, and sharks make kinds with no light chains; tiny pieces of the camel kind are called nanobodies",
            "k": ["nanobodies", "llamas", "sharks"],
            "n": 0
        },
        {
            "id": "autoimmune",
            "tier": "power",
            "t": "In myasthenia gravis they block muscle receptors for acetylcholine; in Graves’ disease they overstimulate the thyroid gland",
            "k": ["myasthenia gravis", "graves", "acetylcholine"],
            "n": 0,
            "rabbit": "Thyroid gland"
        },
        {
            "id": "elisa",
            "tier": "power",
            "t": "ELISA tests and home rapid tests use them, linked to enzymes or dyes, to detect specific proteins",
            "k": ["elisa", "rapid tests"],
            "n": 0
        },
        {
            "id": "antivenom",
            "tier": "power",
            "t": "Antivenom is made by giving horses or sheep small doses of venom and collecting these proteins from their blood",
            "k": ["antivenom", "horses", "sheep"],
            "n": 0,
            "rabbit": "Snakes"
        }
    ],
    "trap": {
        "title": "Antibody or antigen?",
        "body": "The two words sound alike and show up in the same sentences. An antigen is the marker on a germ, a pollen grain, or a red blood cell that gets recognized; an antibody is the Y-shaped protein the body makes to grab it. Players also blurt “B cells,” the cells that make antibodies, or “antibiotics,” the germ-killing medicines.",
        "fix": "If the question asks for “these proteins” or “these Y-shaped molecules,” or mentions heavy and light chains, say antibodies (or immunoglobulins). Say antigen only for “this substance” that the immune system recognizes, and B cells only for “these cells” that make them.",
        "line": "Real answer line: <b><u>Antibodies</u></b> (accept <u>antibody</u> or <u>immunoglobulins</u>; do not accept “antigens”)"
    },
    "tests": {
        "right": [
            "Antibodies",
            "antibody",
            "Immunoglobulins",
            "Antibodys",
            "Monoclonal antibodies"
        ],
        "prompt": [],
        "wrong": [
            "Antigens",
            "Antigen",
            "Antibiotics",
            "B cells",
            "White blood cells",
            "Plasma cells"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
