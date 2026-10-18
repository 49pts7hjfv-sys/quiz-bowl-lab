import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "acids",
    "name": "Acids",
    "mono": "HA",
    "category": "Chemistry",
    "qbCategory": "Science · Chemistry",
    "kicker": "Proton donors that taste sour · Below 7 on the pH scale",
    "dates": "Defined by Arrhenius (1884) and by Brønsted, Lowry, and Lewis (1923)",
    "briefing": "Acids are the sour substances of chemistry: the tang in lemon juice, the bite of vinegar, and the powerful liquid in your stomach that helps digest food. Chemists define an acid as a substance that gives away hydrogen ions (protons), which is why acids have a pH below 7 and turn blue litmus paper red. Strong acids like sulfuric acid can burn skin, while weak ones like citric acid flavor sour candy.",
    "answerHtml": "<b><u>Acid</u></b>s (accept Brønsted–Lowry <u>acid</u>s, Lewis <u>acid</u>s, or Arrhenius <u>acid</u>s; prompt on <u>proton donor</u>s)",
    "accept": [
        "acid",
        "acids",
        "arrhenius acid",
        "arrhenius acids",
        "bronsted lowry acid",
        "bronsted lowry acids",
        "bronsted acid",
        "bronsted acids",
        "lewis acid",
        "lewis acids"
    ],
    "prompt": [
        "proton donor",
        "proton donors",
        "hydrogen ion donor",
        "hydrogen ion donors",
        "electron pair acceptor",
        "electron pair acceptors"
    ],
    "reject": [
        "base",
        "bases",
        "alkali",
        "alkalis",
        "alkaline",
        "ph",
        "litmus",
        "salt",
        "salts",
        "buffer",
        "buffers",
        "hydronium",
        "acid rain",
        "acid base",
        "acid dissociation constant",
        "sulfuric acid",
        "hydrochloric acid",
        "nitric acid",
        "acetic acid",
        "citric acid",
        "lactic acid",
        "carbonic acid",
        "phosphoric acid",
        "hydrofluoric acid",
        "formic acid",
        "ascorbic acid",
        "boric acid",
        "uric acid",
        "amino acid",
        "amino acids",
        "nucleic acid",
        "nucleic acids",
        "fatty acid",
        "fatty acids",
        "deoxyribonucleic acid",
        "ribonucleic acid",
        "stomach acid",
        "lewis base",
        "lewis bases",
        "conjugate base",
        "conjugate bases",
        "antacid",
        "antacids",
        "superacid",
        "superacids"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Acid",
    "qb": {
        "q": "acid",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "Antoine Lavoisier wrongly believed that all of these substances contain oxygen, which is why he gave oxygen a name meaning “former” of these substances. Humphry Davy later showed that hydrogen chloride dissolved in water is one of these substances, even though it contains no oxygen.",
            "r": "These substances turn blue litmus paper red. For 10 points, name these sour-tasting substances with a pH below 7."
        },
        {
            "p": "Gilbert N. Lewis defined these substances as electron-pair acceptors, a definition that includes boron trifluoride even though it has no hydrogen to give away. In the same year, 1923, Johannes Brønsted and Thomas Lowry defined these substances as proton donors.",
            "r": "For 10 points, name these substances that turn blue litmus paper red and react with bases to form salts."
        },
        {
            "p": "Svante Arrhenius, who won the 1903 Nobel Prize in Chemistry for explaining how dissolved substances break apart into ions, defined these substances as compounds that release hydrogen ions in water. Those hydrogen ions join water molecules to form hydronium ions.",
            "r": "For 10 points, name these substances with a pH below 7, found in vinegar and lemon juice."
        },
        {
            "p": "The Henderson–Hasselbalch equation relates a solution’s pH to the pKa of one of these substances and the ratio of its conjugate base to the original compound. A smaller pKa, or a larger dissociation constant Ka, means one of these substances is stronger.",
            "r": "For 10 points, name these proton donors, which turn blue litmus paper red and taste sour."
        },
        {
            "p": "Because of the leveling effect, the strongest of these substances all seem equally strong in water, since each one hands its proton to water completely. Chemists compare those strongest examples using the Hammett function instead of the pH scale.",
            "r": "Examples of these substances include HCl and H₂SO₄. For 10 points, name these proton donors with a pH below 7."
        },
        {
            "p": "In 1940, George de Hevesy [“HEV-eh-shee”] dissolved two gold Nobel Prize medals in aqua regia to hide them from the Nazis. Aqua regia, which can dissolve gold, is made by mixing the nitric and hydrochloric types of these substances in a 1 to 3 ratio.",
            "r": "For 10 points, name these sour substances that donate protons and have a pH below 7."
        },
        {
            "p": "In the 1600s, Robert Boyle noticed that these substances turn a blue dye called syrup of violets red, and he used that change to tell them apart from other substances. Litmus, a dye made from lichens, also turns red in these substances.",
            "r": "Phenolphthalein stays colorless in them. For 10 points, name these sour-tasting compounds with a pH below 7."
        },
        {
            "p": "John Ray first collected a simple one of these substances in 1671 by distilling a large number of ants, so it is named for the Latin word for “ant.” Your muscles make another one of these substances, named for milk, during hard exercise.",
            "r": "For 10 points, name these sour substances, which include the main ingredient of vinegar."
        },
        {
            "p": "Parietal [“puh-RYE-uh-tul”] cells in the stomach lining pump out hydrogen ions to make a strong one of these substances, giving gastric juice a pH of about 2. Heartburn tablets made of calcium carbonate work by neutralizing these substances.",
            "r": "For 10 points, name these compounds that react with bases to form a salt and water."
        },
        {
            "p": "Polyprotic examples of these substances can give away more than one proton: H₂SO₄ can give away two, and H₃PO₄, an ingredient in cola, can give away three. These substances react with active metals such as zinc to release hydrogen gas.",
            "r": "When these substances react with bases, they form water and a salt. For 10 points, name these proton donors."
        },
        {
            "p": "Ralph Pearson’s HSAB theory sorts these substances and their partners into “hard” and “soft” types, predicting that hard ones pair best with hard partners. Metal ions such as Fe³⁺ act as these substances in the Lewis sense by accepting electron pairs.",
            "r": "For 10 points, name these substances, which Brønsted and Lowry defined as proton donors."
        },
        {
            "p": "Water is amphoteric, meaning it can behave either as one of these substances or as a base. A buffer, which resists changes in pH, can be made by mixing a weak one of these substances with its conjugate base.",
            "r": "For 10 points, name these compounds with a pH below 7, such as the main ingredient of vinegar."
        },
        {
            "p": "Søren Sørensen [“SUR-en-sen”] introduced the pH scale in 1909 at the Carlsberg Laboratory to describe how strong solutions of these substances are. In a titration, a base of known concentration is added to one of these substances until an indicator changes color.",
            "r": "These substances turn blue litmus paper red. For 10 points, name these sour compounds with pH values below 7."
        },
        {
            "p": "Alchemists made “oil of vitriol” by heating green vitriol, an iron sulfate, and they used “aqua fortis,” or “strong water,” to separate silver from gold. Chemists call those two liquids the sulfuric and nitric kinds of these substances.",
            "r": "For 10 points, name these compounds, which turn blue litmus red and donate protons."
        },
        {
            "p": "George Olah won the 1994 Nobel Prize in Chemistry for using extremely strong types of these substances, stronger than pure H₂SO₄, to study positively charged carbon ions. One of those extreme mixtures was named for the “magic” way it dissolved a Christmas candle.",
            "r": "Ordinary examples of these substances give foods like lemons a sour taste. For 10 points, name these proton donors."
        }
    ],
    "clues": [
        {
            "id": "ph-below-7",
            "tier": "giveaway",
            "t": "Have a pH below 7 and taste sour, like lemon juice and vinegar",
            "k": ["below 7", "sour", "vinegar"],
            "n": 0,
            "rabbit": "pH"
        },
        {
            "id": "litmus",
            "tier": "giveaway",
            "t": "Turn blue litmus paper red",
            "k": ["litmus", "blue", "red"],
            "n": 0
        },
        {
            "id": "proton-donors",
            "tier": "giveaway",
            "t": "Brønsted–Lowry definition: proton (H⁺) donors",
            "k": ["proton", "donors", "bronsted", "lowry"],
            "n": 0
        },
        {
            "id": "neutralize",
            "tier": "giveaway",
            "t": "React with bases in neutralization reactions to form a salt and water",
            "k": ["neutralization", "bases", "salt and water"],
            "n": 0
        },
        {
            "id": "stomach",
            "tier": "giveaway",
            "t": "The stomach makes a strong one, HCl, to help digest food",
            "k": ["stomach", "hcl", "digest"],
            "n": 0
        },
        {
            "id": "latin-sour",
            "tier": "giveaway",
            "t": "Their name comes from the Latin word for “sour”",
            "k": ["latin", "sour"],
            "n": 0
        },
        {
            "id": "arrhenius",
            "tier": "middle",
            "t": "Arrhenius definition: they release hydrogen ions (H⁺) in water; Svante Arrhenius won the 1903 Nobel Prize",
            "k": ["arrhenius", "hydrogen ions", "1903"],
            "n": 0
        },
        {
            "id": "lewis",
            "tier": "middle",
            "t": "Lewis definition (1923): electron-pair acceptors, such as boron trifluoride",
            "k": ["lewis", "electron-pair acceptors", "boron trifluoride"],
            "n": 0
        },
        {
            "id": "hydronium",
            "tier": "middle",
            "t": "In water, their hydrogen ions join water molecules to form hydronium ions, H₃O⁺",
            "k": ["hydronium", "h3o+"],
            "n": 0
        },
        {
            "id": "conjugate-base",
            "tier": "middle",
            "t": "After giving away a proton, one becomes its conjugate base; amphoteric water can act as one or as a base",
            "k": ["conjugate base", "amphoteric"],
            "n": 0
        },
        {
            "id": "strong-weak",
            "tier": "middle",
            "t": "Strong ones, like HCl, ionize completely in water; weak ones, like the one in vinegar, ionize only partly",
            "k": ["ionize", "strong", "weak"],
            "n": 0
        },
        {
            "id": "metals-carbonates",
            "tier": "middle",
            "t": "React with metals like zinc to make hydrogen gas, and with carbonates to make carbon dioxide",
            "k": ["zinc", "hydrogen gas", "carbonates"],
            "n": 0
        },
        {
            "id": "ka-pka",
            "tier": "middle",
            "t": "Strength is measured by the dissociation constant Ka; a smaller pKa means a stronger one",
            "k": ["dissociation constant", "pka"],
            "n": 0
        },
        {
            "id": "titration",
            "tier": "middle",
            "t": "In a titration, a base is added until an indicator changes color; phenolphthalein stays colorless in them",
            "k": ["titration", "indicator", "phenolphthalein"],
            "n": 0,
            "rabbit": "Titration"
        },
        {
            "id": "lavoisier",
            "tier": "power",
            "t": "Antoine Lavoisier wrongly thought all of them contain oxygen, so he named oxygen as their “former”",
            "k": ["lavoisier", "oxygen", "former"],
            "n": 0,
            "rabbit": "Oxygen"
        },
        {
            "id": "davy-hcl",
            "tier": "power",
            "t": "Humphry Davy showed that hydrogen chloride in water is one, though it has no oxygen",
            "k": ["humphry davy", "hydrogen chloride"],
            "n": 0
        },
        {
            "id": "henderson",
            "tier": "power",
            "t": "Buffers mix a weak one with its conjugate base; the Henderson–Hasselbalch equation gives their pH from the pKa",
            "k": ["hasselbalch", "buffers", "pka"],
            "n": 0
        },
        {
            "id": "leveling",
            "tier": "power",
            "t": "Leveling effect: the strongest ones all look equally strong in water; the Hammett function compares them",
            "k": ["leveling effect", "hammett"],
            "n": 0
        },
        {
            "id": "aqua-regia",
            "tier": "power",
            "t": "Aqua regia, nitric and hydrochloric mixed 1 to 3, dissolves gold",
            "k": ["aqua regia", "gold", "1 to 3"],
            "n": 0,
            "rabbit": "Gold"
        },
        {
            "id": "hevesy",
            "tier": "power",
            "t": "In 1940, George de Hevesy dissolved two gold Nobel medals in aqua regia to hide them from the Nazis",
            "k": ["de hevesy", "nobel medals", "1940"],
            "n": 0
        },
        {
            "id": "boyle",
            "tier": "power",
            "t": "Robert Boyle saw them turn syrup of violets red; litmus is made from lichens",
            "k": ["boyle", "syrup of violets", "lichens"],
            "n": 0
        },
        {
            "id": "ants-milk",
            "tier": "power",
            "t": "John Ray collected a simple one in 1671 by distilling ants (named for the Latin “ant”); muscles make one named for milk",
            "k": ["john ray", "ants", "1671", "milk"],
            "n": 0
        },
        {
            "id": "parietal",
            "tier": "power",
            "t": "Parietal cells pump out hydrogen ions, giving gastric juice a pH of about 2; calcium carbonate heartburn tablets neutralize it",
            "k": ["parietal cells", "gastric juice", "heartburn"],
            "n": 0,
            "rabbit": "Stomach"
        },
        {
            "id": "polyprotic",
            "tier": "power",
            "t": "Polyprotic ones give away more than one proton: H₂SO₄ gives two, and H₃PO₄, found in cola, gives three",
            "k": ["polyprotic", "cola"],
            "n": 0
        },
        {
            "id": "hsab",
            "tier": "power",
            "t": "Ralph Pearson’s HSAB theory sorts them and bases into “hard” and “soft” types",
            "k": ["hsab", "pearson", "hard"],
            "n": 0
        },
        {
            "id": "sorensen",
            "tier": "power",
            "t": "Søren Sørensen introduced the pH scale in 1909 at the Carlsberg Laboratory",
            "k": ["sorensen", "sørensen", "carlsberg", "1909"],
            "n": 0
        },
        {
            "id": "olah",
            "tier": "power",
            "t": "George Olah won the 1994 Nobel Prize using extreme ones stronger than pure H₂SO₄; one was named “magic” after it dissolved a candle",
            "k": ["olah", "1994", "candle"],
            "n": 0
        },
        {
            "id": "vitriol",
            "tier": "power",
            "t": "Alchemists called H₂SO₄ “oil of vitriol” and called HNO₃ “aqua fortis,” or “strong water”",
            "k": ["oil of vitriol", "aqua fortis"],
            "n": 0
        }
    ],
    "trap": {
        "title": "The class, not one example",
        "body": "Tossups on this answer are packed with single examples: the HCl in your stomach, the H₂SO₄ in car batteries, the sour compound in vinegar. Blurting one specific name, like “hydrochloric acid,” is wrong when the question wants the whole class. Bases are the other trap, since clues about pH, litmus, titration, and neutralization fit both.",
        "fix": "Listen for “these substances” or “these compounds” and answer with the class name. Proton donors, pH below 7, a sour taste, and blue litmus turning red mean this class; proton acceptors, pH above 7, a bitter, slippery feel, and red litmus turning blue mean bases.",
        "line": "Real answer line: <b><u>Acid</u></b>s (accept Brønsted–Lowry <u>acid</u>s, Lewis <u>acid</u>s, or Arrhenius <u>acid</u>s; prompt on <u>proton donor</u>s)"
    },
    "tests": {
        "right": [
            "Acids",
            "acid",
            "Lewis acids",
            "Brønsted–Lowry acids",
            "acides",
            "Arrhenius acid"
        ],
        "prompt": [
            "Proton donors"
        ],
        "wrong": [
            "Bases",
            "Sulfuric acid",
            "pH",
            "Hydrochloric acid",
            "Amino acids",
            "Acid rain",
            "Alkali",
            "Salts"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
