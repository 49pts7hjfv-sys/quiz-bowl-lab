import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "vitamin-c",
    "name": "Vitamin C",
    "mono": "VC",
    "category": "Biology",
    "qbCategory": "Science · Biology",
    "kicker": "Vitamin found in citrus fruits · A lack of it causes scurvy",
    "dates": "Identified in 1932; two Nobel Prizes in 1937",
    "briefing": "For centuries, sailors on long voyages came down with scurvy: their gums bled, bruises appeared, and wounds healed slowly. The cure turned out to be vitamin C, found in citrus fruits, strawberries, peppers, and broccoli. Our bodies need it to build collagen, the protein that holds skin, blood vessels, and gums together, but unlike most other mammals, humans cannot make their own and must get it from food.",
    "answerHtml": "<b><u>Vitamin C</u></b> (accept <u>ascorbic acid</u> or <u>ascorbate</u>; accept <u>C</u> after “this vitamin”; prompt on <u>vitamin</u>; do not accept other vitamins)",
    "accept": [
        "vitamin c",
        "ascorbic acid",
        "l ascorbic acid",
        "ascorbic",
        "ascorbate",
        "vit c",
        "c"
    ],
    "prompt": [
        "vitamin",
        "vitamins"
    ],
    "reject": [
        "vitamin a",
        "vitamin b",
        "vitamin b1",
        "vitamin b2",
        "vitamin b3",
        "vitamin b6",
        "vitamin b9",
        "vitamin b12",
        "vitamin d",
        "vitamin d3",
        "vitamin e",
        "vitamin k",
        "b vitamins",
        "vit a",
        "vit b",
        "vit d",
        "vit e",
        "vit k",
        "thiamine",
        "riboflavin",
        "niacin",
        "folic acid",
        "folate",
        "retinol",
        "calciferol",
        "tocopherol",
        "citric acid",
        "scurvy",
        "collagen",
        "iron"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Vitamin_C",
    "qb": {
        "q": "vitamin C",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "In 1747, the Scottish naval surgeon James Lind gave six pairs of sick sailors aboard HMS _Salisbury_ different treatments, such as cider, vinegar, and seawater, in one of the first controlled medical experiments. The pair given oranges and lemons recovered fastest because of this nutrient.",
            "r": "A lack of it causes scurvy, which makes gums bleed. For 10 points, name this vitamin found in citrus fruits."
        },
        {
            "p": "Albert Szent-Györgyi [“SENT JUR-jee”] first isolated this substance from adrenal glands, calling it hexuronic acid, and later extracted large amounts of it from Hungarian paprika peppers. He won the 1937 Nobel Prize in Physiology or Medicine partly for his work on it.",
            "r": "Sailors who lacked it got scurvy. For 10 points, name this vitamin found in oranges and lemons."
        },
        {
            "p": "British chemist Norman Haworth worked out the ring-shaped structure of this compound and shared the 1937 Nobel Prize in Chemistry partly for that work. Tadeus Reichstein [“RIKE-shtine”] developed a method for mass-producing it from glucose in 1933.",
            "r": "For 10 points, name this vitamin whose lack causes scurvy, a disease that once struck sailors on long voyages."
        },
        {
            "p": "In 1907, Norwegian scientists Axel Holst and Theodor Frølich discovered that guinea pigs fed a diet of grain and bread fell ill without this nutrient. Like humans, guinea pigs cannot make it, because their gene for the last enzyme needed to build it is broken.",
            "r": "Most other mammals make their own. For 10 points, name this vitamin, found in citrus fruits, whose lack causes scurvy."
        },
        {
            "p": "Enzymes that add hydroxyl groups to the amino acids proline and lysine need this nutrient as a helper, so the body uses it to build strong collagen fibers. It also helps the intestines absorb iron from plant foods such as beans and lentils.",
            "r": "Without it, gums bleed and wounds heal slowly in a disease called scurvy. For 10 points, name this vitamin."
        },
        {
            "p": "In the winter of 1535 to 1536, Iroquoian people near what is now Quebec City showed Jacques Cartier’s sick crew how to make a tea from the bark and needles of an evergreen tree, which supplied this nutrient.",
            "r": "Without it, sailors developed scurvy. For 10 points, name this vitamin found in citrus fruits."
        },
        {
            "p": "During World War II, British volunteers gathered wild rose hips to make a syrup rich in this nutrient. Captain James Cook fed his crews sauerkraut to prevent a disease caused by a lack of it.",
            "r": "Lime juice given to British sailors for the same reason earned them the nickname “limeys.” For 10 points, name this vitamin found in citrus fruits."
        },
        {
            "p": "Drops of fruit juice turn the blue dye DCPIP colorless when they contain this nutrient, a strong reducing agent. Food makers add this antioxidant, listed as E300, to keep cut fruit from turning brown.",
            "r": "It is found in oranges, strawberries, and broccoli. For 10 points, name this vitamin that prevents scurvy."
        },
        {
            "p": "Two-time Nobel Prize winner Linus Pauling wrote a 1970 bestseller promoting large doses of this nutrient against the common cold. It dissolves in water rather than fat, so the body cannot store much of it, and extra amounts leave in urine.",
            "r": "Oranges and lemons are rich in it. For 10 points, name this vitamin whose lack causes scurvy."
        },
        {
            "p": "Gram for gram, red bell peppers contain more of this nutrient than oranges do, and the Kakadu plum of Australia is one of the richest known sources of it. Cooking and long storage destroy much of it, because heat and air break it down.",
            "r": "A lack of it causes scurvy, which once killed many sailors. For 10 points, name this vitamin."
        },
        {
            "p": "Although its chemical name calls it an acid, this compound has no carboxyl group; its acidity comes instead from hydroxyl groups on a five-membered lactone ring. Its formula is C6H8O6, and most mammals make it from glucose.",
            "r": "Humans must get it from foods like oranges and broccoli. For 10 points, name this vitamin that prevents scurvy."
        },
        {
            "p": "This compound’s chemical name, chosen by Albert Szent-Györgyi and Norman Haworth, comes from the Latin name of the disease it prevents, plus a prefix meaning “without.” Humans, other apes, monkeys, and some bats are among the few mammals that cannot make it.",
            "r": "Sailors who lacked it developed scurvy. For 10 points, name this vitamin found in citrus fruits."
        },
        {
            "p": "In 1932, American chemist Charles Glen King reported isolating this nutrient from lemon juice, at about the same time Albert Szent-Györgyi identified it. Much earlier, Gilbert Blane persuaded Britain’s Royal Navy to give every sailor a daily ration of lemon juice, which supplied it.",
            "r": "Without it, sailors got scurvy. For 10 points, name this vitamin found in oranges, lemons, and limes."
        },
        {
            "p": "In 1912, Casimir Funk suggested that a disease caused by a lack of this nutrient, along with beriberi and pellagra, came from missing substances he called “vitamines.” This nutrient helps the body build collagen, the protein that holds skin and gums together.",
            "r": "Strawberries and oranges are rich in it. For 10 points, name this vitamin whose lack causes scurvy."
        },
        {
            "p": "This antioxidant dissolves in water and works alongside vitamin E, a fat-soluble antioxidant, by restoring vitamin E after it neutralizes harmful molecules called free radicals. Pet guinea pigs need extra amounts of it in their food, since they cannot make it.",
            "r": "Humans also need it from food, such as oranges. For 10 points, name this vitamin whose lack causes scurvy."
        }
    ],
    "clues": [
        {
            "id": "scurvy",
            "tier": "giveaway",
            "t": "A lack of it causes scurvy: bleeding gums, bruising, and slow-healing wounds",
            "k": ["scurvy", "bleeding gums"],
            "n": 0
        },
        {
            "id": "citrus",
            "tier": "giveaway",
            "t": "Found in citrus fruits like oranges, lemons, and limes, and also in strawberries, kiwifruit, and broccoli",
            "k": ["citrus", "oranges", "lemons"],
            "n": 0
        },
        {
            "id": "sailors",
            "tier": "giveaway",
            "t": "Scurvy struck sailors on long voyages who had no fresh fruits or vegetables",
            "k": ["sailors", "voyages"],
            "n": 0
        },
        {
            "id": "humans-need-food",
            "tier": "giveaway",
            "t": "Humans cannot make it, so it must come from food",
            "k": ["cannot make", "food"],
            "n": 0,
            "rabbit": "Vitamins"
        },
        {
            "id": "collagen",
            "tier": "middle",
            "t": "Needed to build collagen, the protein that holds skin, blood vessels, and gums together",
            "k": ["collagen", "protein"],
            "n": 0,
            "rabbit": "Collagen"
        },
        {
            "id": "proline-lysine",
            "tier": "middle",
            "t": "Helps enzymes add hydroxyl groups to the amino acids proline and lysine in collagen",
            "k": ["proline", "lysine", "hydroxyl"],
            "n": 0,
            "rabbit": "Amino acids"
        },
        {
            "id": "iron",
            "tier": "middle",
            "t": "Helps the intestines absorb iron from plant foods",
            "k": ["iron", "absorb"],
            "n": 0
        },
        {
            "id": "lind",
            "tier": "middle",
            "t": "James Lind’s 1747 experiment aboard HMS _Salisbury_: the sailors given oranges and lemons recovered fastest",
            "k": ["james lind", "1747", "salisbury"],
            "n": 0
        },
        {
            "id": "limeys",
            "tier": "middle",
            "t": "British sailors were nicknamed “limeys” for the lime juice they drank to prevent scurvy",
            "k": ["limeys", "lime juice"],
            "n": 0
        },
        {
            "id": "water-soluble",
            "tier": "middle",
            "t": "Water-soluble: the body stores little of it, and extra amounts leave in urine",
            "k": ["water-soluble", "urine"],
            "n": 0
        },
        {
            "id": "dcpip",
            "tier": "middle",
            "t": "A strong reducing agent: it turns the blue dye DCPIP colorless; food makers add it as antioxidant E300 to keep cut fruit from browning",
            "k": ["dcpip", "reducing agent", "e300", "browning"],
            "n": 0
        },
        {
            "id": "heat",
            "tier": "middle",
            "t": "Cooking, heat, and long storage destroy much of it",
            "k": ["cooking", "heat", "storage"],
            "n": 0
        },
        {
            "id": "bell-peppers",
            "tier": "middle",
            "t": "Red bell peppers have more of it per gram than oranges",
            "k": ["bell peppers", "per gram"],
            "n": 0
        },
        {
            "id": "szent-gyorgyi",
            "tier": "power",
            "t": "Albert Szent-Györgyi isolated it as “hexuronic acid,” later from Hungarian paprika, and won the 1937 Nobel Prize in Physiology or Medicine",
            "k": ["szent-györgyi", "hexuronic acid", "paprika"],
            "n": 0
        },
        {
            "id": "haworth-reichstein",
            "tier": "power",
            "t": "Norman Haworth worked out its structure (1937 Nobel Prize in Chemistry); Tadeus Reichstein found a way to mass-produce it from glucose (1933)",
            "k": ["haworth", "reichstein", "mass-produce"],
            "n": 0
        },
        {
            "id": "holst-frolich",
            "tier": "power",
            "t": "In 1907, Axel Holst and Theodor Frølich found that guinea pigs fed grain and bread fall ill without it",
            "k": ["guinea pigs", "1907", "holst"],
            "n": 0
        },
        {
            "id": "broken-gene",
            "tier": "power",
            "t": "Humans, other apes, monkeys, guinea pigs, and some bats cannot make it, because their gene for the last enzyme in the recipe is broken",
            "k": ["broken", "apes", "bats"],
            "n": 0
        },
        {
            "id": "cartier",
            "tier": "power",
            "t": "Iroquoian people near what is now Quebec City taught Jacques Cartier’s sick crew (1535–1536) to make a tea from an evergreen tree’s bark and needles",
            "k": ["cartier", "iroquoian", "evergreen"],
            "n": 0
        },
        {
            "id": "rose-hips",
            "tier": "power",
            "t": "During World War II, British volunteers gathered rose hips to make a syrup rich in it",
            "k": ["rose hips", "syrup"],
            "n": 0
        },
        {
            "id": "cook-sauerkraut",
            "tier": "power",
            "t": "Captain James Cook fed his crews sauerkraut to prevent scurvy",
            "k": ["james cook", "sauerkraut"],
            "n": 0
        },
        {
            "id": "pauling",
            "tier": "power",
            "t": "Two-time Nobel winner Linus Pauling wrote a 1970 bestseller promoting large doses of it against the common cold",
            "k": ["linus pauling", "1970", "common cold"],
            "n": 0
        },
        {
            "id": "kakadu",
            "tier": "power",
            "t": "The Kakadu plum of Australia is one of the richest known sources",
            "k": ["kakadu plum", "richest"],
            "n": 0
        },
        {
            "id": "lactone",
            "tier": "power",
            "t": "Formula C6H8O6; despite being called an acid, it has no carboxyl group, and its acidity comes from hydroxyl groups on a five-membered lactone ring",
            "k": ["lactone", "c6h8o6", "carboxyl"],
            "n": 0
        },
        {
            "id": "name-meaning",
            "tier": "power",
            "t": "Its chemical name, chosen by Szent-Györgyi and Haworth, comes from the Latin name for scurvy plus a prefix meaning “without”",
            "k": ["latin", "without"],
            "n": 0
        },
        {
            "id": "king-blane",
            "tier": "power",
            "t": "Charles Glen King isolated it from lemon juice in 1932; much earlier, Gilbert Blane got the Royal Navy to give sailors daily lemon juice",
            "k": ["charles glen king", "gilbert blane", "royal navy"],
            "n": 0
        },
        {
            "id": "funk",
            "tier": "power",
            "t": "Casimir Funk (1912) blamed scurvy, beriberi, and pellagra on missing substances he called “vitamines”",
            "k": ["casimir funk", "vitamines", "beriberi"],
            "n": 0
        },
        {
            "id": "free-radicals",
            "tier": "power",
            "t": "A water-soluble antioxidant that restores fat-soluble vitamin E after vitamin E neutralizes free radicals",
            "k": ["free radicals", "restores"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Which vitamin?",
        "body": "Several vitamins come with a famous deficiency disease, and a fast buzz can grab the wrong letter. A lack of vitamin C causes scurvy, a lack of vitamin D causes rickets, a lack of thiamine (vitamin B1) causes beriberi, and a lack of niacin (vitamin B3) causes pellagra. Vitamin K helps blood clot, and vitamin A helps with night vision.",
        "fix": "Sailors, citrus fruits, limeys, collagen, James Lind, Szent-Györgyi, and paprika all mean vitamin C. Sunshine and rickets mean vitamin D. Saying just “vitamin” earns a prompt, so be ready to add the letter.",
        "line": "Real answer line: <b><u>Vitamin C</u></b> (accept <u>ascorbic acid</u> or <u>ascorbate</u>; do not accept other vitamins)"
    },
    "tests": {
        "right": [
            "Vitamin C",
            "ascorbic acid",
            "Vitamen C",
            "C",
            "L-ascorbic acid",
            "ascorbate"
        ],
        "prompt": [
            "Vitamin"
        ],
        "wrong": [
            "Vitamin D",
            "Vitamin B12",
            "Vitamin B6",
            "Citric acid",
            "Scurvy",
            "Vitamin A",
            "Collagen"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
