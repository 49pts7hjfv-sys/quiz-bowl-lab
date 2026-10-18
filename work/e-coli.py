import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "e-coli",
    "name": "E. coli",
    "mono": "EC",
    "category": "Biology",
    "qbCategory": "Science · Biology",
    "kicker": "Rod-shaped gut bacterium · Biology’s favorite lab organism",
    "dates": "Discovered 1885",
    "briefing": "E. coli, short for _Escherichia coli_, is a rod-shaped bacterium that lives by the billions in the intestines of people and other warm-blooded animals. Most kinds are harmless or even helpful, but a few strains can cause food poisoning, which is why food-safety rules call for cooking ground beef all the way through. Because it is easy to grow and can divide about every 20 minutes, it is one of the most-studied living things in science.",
    "answerHtml": "<b><u>E. coli</u></b> (accept <u>Escherichia coli</u>; prompt on <u>Escherichia</u> or <u>coliform</u> bacteria; do not accept “Salmonella” or “Shigella”)",
    "accept": [
        "e coli",
        "ecoli",
        "escherichia coli",
        "e coli bacteria",
        "e coli bacterium"
    ],
    "prompt": [
        "escherichia",
        "coli",
        "coliform",
        "coliforms",
        "coliform bacteria"
    ],
    "reject": [
        "salmonella",
        "shigella",
        "listeria",
        "staphylococcus",
        "staphylococcus aureus",
        "staph",
        "streptococcus",
        "strep",
        "clostridium",
        "clostridioides difficile",
        "c diff",
        "vibrio cholerae",
        "cholera",
        "lactobacillus",
        "bacillus",
        "bacillus subtilis",
        "helicobacter pylori",
        "h pylori",
        "pseudomonas",
        "klebsiella",
        "yersinia",
        "enterobacter",
        "theodor escherich",
        "colitis"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Escherichia_coli",
    "qb": {
        "q": "E. coli",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "In 1885, a German-Austrian pediatrician who was studying bacteria in infants discovered this organism, which was later renamed in his honor. This organism is Gram-negative, so it stains pink, not purple, in a Gram stain.",
            "r": "For 10 points, name this bacterium that lives in the human gut and whose harmful strains can cause food poisoning."
        },
        {
            "p": "Since 1988, Richard Lenski’s lab has grown twelve populations of this organism for tens of thousands of generations, and in one of them the cells evolved the ability to feed on citrate when oxygen is present. Samples frozen every 500 generations serve as that experiment’s “fossil record.”",
            "r": "This organism can divide about every 20 minutes. For 10 points, name this rod-shaped gut bacterium."
        },
        {
            "p": "In 1958, Matthew Meselson and Franklin Stahl grew this organism on food containing heavy nitrogen-15 and followed its DNA through new generations, showing that DNA copies itself semiconservatively. Their experiment separated the DNA by density in a spinning centrifuge.",
            "r": "For 10 points, name this rod-shaped bacterium, a favorite model organism that lives in the human intestine."
        },
        {
            "p": "In 1946, Joshua Lederberg and Edward Tatum showed that strains of this organism could swap genes, a process now called bacterial conjugation. Cells of this organism that carry the F plasmid, or fertility factor, build a bridge called a pilus to pass DNA to other cells.",
            "r": "For 10 points, name this gut bacterium, known by a short form of its Latin name, whose dangerous strains can cause food poisoning."
        },
        {
            "p": "The restriction enzyme EcoRI, which cuts DNA wherever it finds the sequence GAATTC, takes the first part of its name from this organism. Restriction enzymes like that one help this organism defend itself by chopping up the DNA of invading viruses.",
            "r": "For 10 points, name this rod-shaped bacterium that lives in human intestines and is a favorite of biology labs."
        },
        {
            "p": "In 1973, Herbert Boyer and Stanley Cohen made some of the first recombinant DNA by putting a plasmid carrying foreign genes into this organism. Genetically engineered strains of this organism later produced human insulin, which in 1982 became the first approved drug made with recombinant DNA.",
            "r": "This organism’s harmful strains can cause food poisoning. For 10 points, name this common gut bacterium, a favorite model organism."
        },
        {
            "p": "The genome of this organism’s laboratory strain K-12, about 4.6 million base pairs long, was published in 1997 by Frederick Blattner’s team. In the human gut, this organism helps make vitamin K.",
            "r": "For 10 points, name this rod-shaped bacterium that lives in the intestines and whose dangerous strains can cause food poisoning."
        },
        {
            "p": "A 1993 outbreak traced to undercooked hamburgers from Jack in the Box restaurants, which sickened hundreds of people, led the United States to tighten its rules on ground beef. That outbreak was caused by a strain of this organism called O157:H7, which makes Shiga toxin.",
            "r": "Most strains of this organism are harmless. For 10 points, name this bacterium that lives in the human intestine."
        },
        {
            "p": "Grown on EMB, or eosin methylene blue, agar, colonies of this organism show a shiny, metallic green sheen. Water is tested for this coliform bacterium as a sign of contamination by sewage.",
            "r": "For 10 points, name this rod-shaped bacterium found in the human gut, whose harmful strains can cause food poisoning."
        },
        {
            "p": "In 1952, Alfred Hershey and Martha Chase showed that DNA carries genetic information by tagging T2 phages, viruses that infect this organism, with radioactive phosphorus and sulfur. Another virus that infects this organism, lambda, can hide inside its DNA as a prophage.",
            "r": "For 10 points, name this bacterium that lives in the human intestine and is a favorite model organism."
        },
        {
            "p": "François Jacob and Jacques Monod [“moh-NOH”] worked out the lac operon, a set of genes for digesting the sugar lactose, by studying this organism. This organism swims with whiplike flagella in a pattern known as “run and tumble.”",
            "r": "For 10 points, name this rod-shaped gut bacterium whose dangerous strains can cause food poisoning."
        },
        {
            "p": "During World War I, Alfred Nissle isolated a strain of this organism from a soldier who stayed healthy during an outbreak of dysentery, and that strain, Nissle 1917, became a widely used probiotic. In the gut, this organism helps make vitamin K.",
            "r": "For 10 points, name this rod-shaped bacterium whose harmful strains, such as O157:H7, can cause food poisoning."
        },
        {
            "p": "_Shigella_ [“shih-GEL-uh”] bacteria, which cause dysentery, are so closely related to this organism that some scientists consider them strains of it. Like _Salmonella_, this organism is a Gram-negative member of the family Enterobacteriaceae [“en-ter-oh-bak-teer-ee-AY-see-ee”].",
            "r": "For 10 points, name this rod-shaped bacterium that lives in human intestines and is a favorite lab organism."
        },
        {
            "p": "In the IMViC [“IM-vik”] series of lab tests, this organism is positive for indole and methyl red but negative for citrate. This organism is Gram-negative, with a thin cell wall wrapped in an outer membrane.",
            "r": "For 10 points, name this rod-shaped bacterium that lives in the guts of warm-blooded animals and is a favorite of biology labs."
        },
        {
            "p": "Arthur Kornberg discovered DNA polymerase I, the first known enzyme that builds DNA, by studying extracts of this organism in 1956. Genetically engineered strains of this organism were later used to produce human insulin.",
            "r": "For 10 points, name this gut bacterium that divides about every 20 minutes in the lab and whose harmful strains cause food poisoning."
        }
    ],
    "clues": [
        {
            "id": "gut-bacterium",
            "tier": "giveaway",
            "t": "A bacterium that lives in the intestines of humans and other warm-blooded animals",
            "k": ["intestines", "warm-blooded", "bacterium"],
            "n": 0,
            "rabbit": "Bacteria"
        },
        {
            "id": "food-poisoning",
            "tier": "giveaway",
            "t": "Most strains are harmless, but some cause food poisoning, often from undercooked ground beef or unwashed produce",
            "k": ["food poisoning", "undercooked", "strains"],
            "n": 0
        },
        {
            "id": "model-organism",
            "tier": "giveaway",
            "t": "Biology’s favorite model organism: easy to grow, and it can divide about every 20 minutes",
            "k": ["model organism", "20 minutes"],
            "n": 0
        },
        {
            "id": "rod-shaped",
            "tier": "giveaway",
            "t": "A rod-shaped (bacillus) bacterium, known by a short form of its Latin name",
            "k": ["rod-shaped", "latin name"],
            "n": 0
        },
        {
            "id": "gram-negative",
            "tier": "middle",
            "t": "Gram-negative: stains pink in a Gram stain, with a thin cell wall wrapped in an outer membrane",
            "k": ["gram-negative", "pink", "outer membrane"],
            "n": 0
        },
        {
            "id": "pediatrician-1885",
            "tier": "middle",
            "t": "Discovered in 1885 by a German-Austrian pediatrician studying babies’ gut bacteria, and later renamed in his honor",
            "k": ["pediatrician", "1885"],
            "n": 0
        },
        {
            "id": "o157",
            "tier": "middle",
            "t": "The dangerous strain O157:H7 makes Shiga toxin, which can harm the kidneys",
            "k": ["o157:h7", "shiga toxin"],
            "n": 0
        },
        {
            "id": "lac-operon",
            "tier": "middle",
            "t": "Jacob and Monod worked out the lac operon, genes for digesting the sugar lactose, in this bacterium",
            "k": ["lac operon", "lactose", "monod"],
            "n": 0,
            "rabbit": "Lac operon"
        },
        {
            "id": "sewage-indicator",
            "tier": "middle",
            "t": "Water is tested for this coliform bacterium as a sign of sewage contamination",
            "k": ["coliform", "sewage"],
            "n": 0
        },
        {
            "id": "vitamin-k",
            "tier": "middle",
            "t": "In the gut, it helps make vitamin K",
            "k": ["vitamin k"],
            "n": 0,
            "rabbit": "Vitamins"
        },
        {
            "id": "insulin",
            "tier": "middle",
            "t": "Engineered strains made human insulin, approved in 1982 as the first drug made with recombinant DNA",
            "k": ["insulin", "recombinant dna", "1982"],
            "n": 0,
            "rabbit": "Insulin"
        },
        {
            "id": "conjugation",
            "tier": "middle",
            "t": "Joshua Lederberg and Edward Tatum discovered bacterial conjugation in it in 1946; the F plasmid builds a bridge called a pilus",
            "k": ["conjugation", "lederberg", "tatum", "pilus"],
            "n": 0,
            "rabbit": "Bacterial conjugation"
        },
        {
            "id": "flagella",
            "tier": "middle",
            "t": "Swims with whiplike flagella in a “run and tumble” pattern",
            "k": ["flagella", "run and tumble"],
            "n": 0
        },
        {
            "id": "lenski",
            "tier": "power",
            "t": "Richard Lenski has grown 12 populations since 1988; one evolved the ability to feed on citrate when oxygen is present",
            "k": ["lenski", "citrate", "1988"],
            "n": 0
        },
        {
            "id": "meselson-stahl",
            "tier": "power",
            "t": "Meselson and Stahl grew it on heavy nitrogen-15 (1958) to show that DNA copies itself semiconservatively",
            "k": ["meselson", "stahl", "nitrogen-15", "semiconservatively"],
            "n": 0,
            "rabbit": "DNA"
        },
        {
            "id": "ecori",
            "tier": "power",
            "t": "The restriction enzyme EcoRI, which cuts DNA at GAATTC, is named for it",
            "k": ["ecori", "gaattc", "restriction enzyme"],
            "n": 0
        },
        {
            "id": "boyer-cohen",
            "tier": "power",
            "t": "Herbert Boyer and Stanley Cohen made recombinant DNA in it in 1973 by adding a plasmid carrying foreign genes",
            "k": ["boyer", "cohen", "1973", "plasmid"],
            "n": 0
        },
        {
            "id": "k-12",
            "tier": "power",
            "t": "The genome of lab strain K-12, about 4.6 million base pairs, was published in 1997 by Frederick Blattner’s team",
            "k": ["k-12", "1997", "blattner"],
            "n": 0
        },
        {
            "id": "jack-in-the-box",
            "tier": "power",
            "t": "A 1993 O157:H7 outbreak traced to undercooked Jack in the Box hamburgers led to tighter U.S. rules on ground beef",
            "k": ["jack in the box", "1993", "hamburgers"],
            "n": 0
        },
        {
            "id": "emb-agar",
            "tier": "power",
            "t": "On EMB (eosin methylene blue) agar, its colonies show a metallic green sheen",
            "k": ["metallic green sheen", "eosin methylene blue", "emb"],
            "n": 0
        },
        {
            "id": "hershey-chase",
            "tier": "power",
            "t": "Hershey and Chase tagged T2 phages, viruses that infect it, to show in 1952 that DNA is the genetic material",
            "k": ["hershey", "chase", "t2", "1952"],
            "n": 0,
            "rabbit": "Bacteriophages"
        },
        {
            "id": "lambda",
            "tier": "power",
            "t": "Bacteriophage lambda can hide inside its DNA as a prophage",
            "k": ["lambda", "prophage"],
            "n": 0
        },
        {
            "id": "nissle",
            "tier": "power",
            "t": "The probiotic strain Nissle 1917 came from a World War I soldier who stayed healthy during a dysentery outbreak",
            "k": ["nissle", "probiotic", "1917"],
            "n": 0
        },
        {
            "id": "shigella",
            "tier": "power",
            "t": "_Shigella_ bacteria are so closely related that some scientists consider them strains of it; both are in the family Enterobacteriaceae",
            "k": ["shigella", "enterobacteriaceae"],
            "n": 0
        },
        {
            "id": "imvic",
            "tier": "power",
            "t": "In the IMViC tests, it is positive for indole and methyl red but negative for citrate",
            "k": ["imvic", "indole", "methyl red"],
            "n": 0
        },
        {
            "id": "kornberg",
            "tier": "power",
            "t": "Arthur Kornberg discovered DNA polymerase I, the first known DNA-building enzyme, in its extracts in 1956",
            "k": ["kornberg", "dna polymerase i", "1956"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Not Salmonella",
        "body": "E. coli and Salmonella are both rod-shaped, Gram-negative gut bacteria in the same family, and both are famous for food poisoning, so players mix them up. Shigella is even closer: it is so similar to E. coli that some scientists call it a kind of E. coli, but it is still named separately. “Coliform” is a bigger group that includes E. coli, so it earns only a prompt.",
        "fix": "Lab-history clues, such as Meselson and Stahl, Lederberg and Tatum, the lac operon, EcoRI, and Lenski’s experiment, point to E. coli, biology’s favorite model organism. Raw eggs, chicken, and typhoid fever point to Salmonella. Say “E. coli” or the full name, not just “coliform.”",
        "line": "Real answer line: <b><u>E. coli</u></b> (accept <u>Escherichia coli</u>; prompt on <u>Escherichia</u>)"
    },
    "tests": {
        "right": [
            "E. coli",
            "e coli",
            "Escherichia coli",
            "E coli O157:H7",
            "Escherichia coly",
            "ecoli"
        ],
        "prompt": [
            "Escherichia",
            "Coliform"
        ],
        "wrong": [
            "Salmonella",
            "Shigella",
            "Listeria",
            "Staph",
            "Cholera"
        ]
    }
}

out = ROOT / "topics" / "e-coli.json"
with open(out, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("wrote", out)
