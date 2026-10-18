import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "alcohols-chemistry",
    "name": "Alcohols (chemistry)",
    "mono": "OH",
    "category": "Chemistry",
    "qbCategory": "Science · Chemistry",
    "kicker": "Organic compounds with an –OH group · Their names end in “-ol”",
    "dates": "Grignard’s method for making them, 1900",
    "briefing": "In chemistry, an alcohol is any organic compound with a hydroxyl group, an oxygen-hydrogen pair written –OH, attached to a carbon atom. Their names end in “-ol”: methanol has long been used as a race-car fuel, isopropanol is the rubbing alcohol in first-aid kits, and ethylene glycol keeps car engines from freezing. Because that –OH group forms hydrogen bonds, alcohols boil at much higher temperatures than hydrocarbons of similar size.",
    "answerHtml": "<b><u>Alcohols</u></b> (accept <u>alkanol</u>s; prompt on <u>hydroxy</u>l compounds; do not accept “hydroxyl” alone or specific alcohols like “ethanol”)",
    "accept": [
        "alcohols",
        "alcohol",
        "alkanols",
        "alkanol"
    ],
    "prompt": [
        "hydroxyl compounds",
        "hydroxyl compound",
        "hydroxy compounds",
        "hydroxy compound",
        "organic hydroxyl compounds"
    ],
    "reject": [
        "ethyl alcohol",
        "methyl alcohol",
        "isopropyl alcohol",
        "propyl alcohol",
        "butyl alcohol",
        "benzyl alcohol",
        "allyl alcohol",
        "polyvinyl alcohol",
        "rubbing alcohol",
        "wood alcohol",
        "grain alcohol",
        "ethanol",
        "methanol",
        "propanol",
        "isopropanol",
        "butanol",
        "octanol",
        "phenol",
        "phenols",
        "glycerol",
        "glycerin",
        "ethylene glycol",
        "glycol",
        "glycols",
        "diol",
        "diols",
        "hydroxyl",
        "hydroxyl group",
        "hydroxyl groups",
        "hydroxide",
        "hydroxides",
        "aldehyde",
        "aldehydes",
        "ketone",
        "ketones",
        "ether",
        "ethers",
        "ester",
        "esters",
        "carboxylic acid",
        "carboxylic acids",
        "acetic acid",
        "alkane",
        "alkanes",
        "alkene",
        "alkenes",
        "alkyne",
        "alkynes",
        "amine",
        "amines",
        "thiol",
        "thiols",
        "alkoxide",
        "alkoxides"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Alcohol_(chemistry)",
    "qb": {
        "q": "alcohol",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "Herbert C. Brown shared the 1979 Nobel Prize in Chemistry partly for hydroboration, a two-step reaction that turns alkenes into these compounds, putting the oxygen-containing group on the less crowded carbon. These compounds also form when sodium borohydride reduces an aldehyde or a ketone.",
            "r": "For 10 points, name these organic compounds that contain a hydroxyl group and have names ending in “-ol.”"
        },
        {
            "p": "The Lucas test uses zinc chloride in hydrochloric acid to tell three kinds of these compounds apart: tertiary ones turn the mixture cloudy almost at once, secondary ones take a few minutes, and primary ones barely react.",
            "r": "For 10 points, name this class of organic compounds, which includes methanol and ethanol."
        },
        {
            "p": "Orange potassium dichromate turns green as it oxidizes primary members of this class into aldehydes and then into carboxylic acids, while secondary members become ketones. Tertiary members of this class resist that oxidation.",
            "r": "For 10 points, name this class of compounds with an –OH group, such as isopropanol and ethanol."
        },
        {
            "p": "Dropping sodium metal into these compounds releases hydrogen gas and forms alkoxides, which react with alkyl halides to make ethers in Alexander Williamson’s ether synthesis. These compounds are only about as acidic as water.",
            "r": "For 10 points, name this class of compounds that includes methanol, whose names end in “-ol.”"
        },
        {
            "p": "Victor Grignard [“green-YAR”] won the 1912 Nobel Prize in Chemistry for reagents that add to ketones to form tertiary members of this class. Lithium aluminum hydride can also produce these compounds from esters or carboxylic acids.",
            "r": "For 10 points, name these organic compounds containing a hydroxyl group, such as ethanol and isopropanol."
        },
        {
            "p": "Heating these compounds with concentrated sulfuric acid can strip out a water molecule to form an alkene or, at a lower temperature, join two of their molecules into an ether. Industrial chemists make one of these compounds by reacting ethene with steam over a phosphoric acid catalyst.",
            "r": "For 10 points, name this class of organic compounds, whose simplest member is methanol and whose names end in “-ol.”"
        },
        {
            "p": "In Fischer esterification, an acid catalyst helps one of these compounds react with a carboxylic acid to form a fruity-smelling ester and water. Glycerol, a member of this class with three –OH groups, forms the backbone of fats.",
            "r": "For 10 points, name these compounds, such as ethanol and methanol, whose names end in “-ol.”"
        },
        {
            "p": "This class’s name comes from the Arabic word for kohl, a fine black powder used as eye makeup. Menthol from mint leaves, cholesterol, and retinol, also called vitamin A, all belong to this class.",
            "r": "For 10 points, name this class of organic compounds with a hydroxyl group, whose names end in “-ol.”"
        },
        {
            "p": "Octanol, a member of this class with a long carbon chain, barely dissolves in water, so chemists shake drugs with octanol and water to measure whether they prefer oily or watery surroundings. The smallest members of this class, such as methanol and ethanol, mix completely with water.",
            "r": "For 10 points, name this class of organic compounds that contain an –OH group and have names ending in “-ol.”"
        },
        {
            "p": "Members of this class are called primary, secondary, or tertiary depending on how many carbon atoms are attached to the carbon holding their –OH group. The tertiary example called tert-butanol has three methyl groups on that carbon.",
            "r": "For 10 points, name this class of compounds that includes isopropanol, the antiseptic liquid found in many first-aid kits."
        },
        {
            "p": "Antifreeze is mostly ethylene glycol, a member of this class with two –OH groups, which makes it a diol. Sugar-free gums are often sweetened with xylitol and sorbitol, which also belong to this class.",
            "r": "For 10 points, name this class of organic compounds whose names usually end in “-ol,” such as methanol."
        },
        {
            "p": "Methanol, the simplest member of this class, was once made by heating wood without air and was later made mostly from carbon monoxide and hydrogen gas. Methanol is highly toxic, even though it is a close chemical cousin of ethanol.",
            "r": "For 10 points, name this class of organic compounds, which also includes ethanol and isopropanol."
        },
        {
            "p": "Yeast turn sugar into carbon dioxide and one of these compounds during fermentation. Brazil fuels many of its cars with that compound made from sugarcane, and most American gasoline contains about 10 percent of it.",
            "r": "For 10 points, name this class of organic compounds, which have a hydroxyl group and names ending in “-ol.”"
        },
        {
            "p": "Thiols, sometimes called mercaptans, are the sulfur versions of these compounds, with an –SH group in place of their –OH group. In infrared spectra, these compounds show a broad peak caused by their O–H bonds.",
            "r": "For 10 points, name this class of compounds, including ethanol and methanol, whose names end in “-ol.”"
        },
        {
            "p": "Phenols have an –OH group attached directly to a benzene ring and are much more acidic, so they are usually counted as a separate class from these compounds. Because they form hydrogen bonds, these compounds boil at higher temperatures than alkanes of similar size.",
            "r": "For 10 points, name these organic compounds, such as isopropanol, that contain a hydroxyl group."
        }
    ],
    "clues": [
        {
            "id": "hydroxyl",
            "tier": "giveaway",
            "t": "Organic compounds containing a hydroxyl (–OH) group bonded to a carbon atom",
            "k": ["hydroxyl", "organic compounds"],
            "n": 0
        },
        {
            "id": "ol-suffix",
            "tier": "giveaway",
            "t": "Their names end in the suffix “-ol”",
            "k": ["suffix", "-ol"],
            "n": 0
        },
        {
            "id": "examples",
            "tier": "giveaway",
            "t": "Include methanol, ethanol, and isopropanol",
            "k": ["methanol", "ethanol", "isopropanol"],
            "n": 0
        },
        {
            "id": "first-aid",
            "tier": "giveaway",
            "t": "Isopropanol is the antiseptic liquid in first-aid kits; many hand sanitizers contain ethanol or isopropanol",
            "k": ["first-aid", "hand sanitizers", "antiseptic"],
            "n": 0
        },
        {
            "id": "classes",
            "tier": "middle",
            "t": "Primary, secondary, or tertiary, by how many carbons are attached to the carbon holding the –OH; tert-butanol is tertiary",
            "k": ["primary", "secondary", "tertiary"],
            "n": 0
        },
        {
            "id": "hydrogen-bonding",
            "tier": "middle",
            "t": "Their –OH groups form hydrogen bonds, so they boil higher than alkanes of similar size",
            "k": ["hydrogen bonds", "alkanes"],
            "n": 0,
            "rabbit": "Hydrogen bonds"
        },
        {
            "id": "solubility",
            "tier": "middle",
            "t": "Small ones like methanol and ethanol mix completely with water; long-chain ones like octanol barely dissolve",
            "k": ["mix completely", "octanol", "long-chain"],
            "n": 0
        },
        {
            "id": "oxidation",
            "tier": "middle",
            "t": "Oxidation: primary ones become aldehydes, then carboxylic acids; secondary ones become ketones; tertiary ones resist",
            "k": ["aldehydes", "ketones", "carboxylic acids", "oxidation"],
            "n": 0
        },
        {
            "id": "dichromate",
            "tier": "middle",
            "t": "Orange potassium dichromate turns green as it oxidizes them",
            "k": ["dichromate", "orange", "green"],
            "n": 0
        },
        {
            "id": "esterification",
            "tier": "middle",
            "t": "React with carboxylic acids in Fischer esterification to make fruity-smelling esters and water",
            "k": ["fischer esterification", "esters", "fruity"],
            "n": 0,
            "rabbit": "Esters"
        },
        {
            "id": "dehydration",
            "tier": "middle",
            "t": "Heating with concentrated sulfuric acid removes water, making alkenes (or ethers at lower temperatures)",
            "k": ["sulfuric acid", "alkenes", "removes water"],
            "n": 0,
            "rabbit": "Alkenes"
        },
        {
            "id": "antifreeze",
            "tier": "middle",
            "t": "Ethylene glycol (two –OH groups) is antifreeze; glycerol (three) is the backbone of fats",
            "k": ["ethylene glycol", "antifreeze", "glycerol"],
            "n": 0
        },
        {
            "id": "fermentation",
            "tier": "middle",
            "t": "Yeast make ethanol and carbon dioxide from sugar by fermentation",
            "k": ["fermentation", "yeast"],
            "n": 0,
            "rabbit": "Yeast"
        },
        {
            "id": "fuel",
            "tier": "middle",
            "t": "Ethanol from sugarcane fuels many cars in Brazil; most U.S. gasoline contains about 10 percent ethanol",
            "k": ["sugarcane", "brazil", "gasoline"],
            "n": 0
        },
        {
            "id": "hydroboration",
            "tier": "power",
            "t": "Herbert C. Brown (1979 Nobel) developed hydroboration, which turns alkenes into these with the –OH on the less crowded carbon",
            "k": ["hydroboration", "1979", "less crowded"],
            "n": 0
        },
        {
            "id": "lucas-test",
            "tier": "power",
            "t": "Lucas test (zinc chloride in hydrochloric acid): tertiary ones turn cloudy at once, secondary in minutes, primary barely react",
            "k": ["lucas test", "zinc chloride", "cloudy"],
            "n": 0
        },
        {
            "id": "williamson",
            "tier": "power",
            "t": "Sodium metal turns them into alkoxides and hydrogen gas; alkoxides plus alkyl halides make ethers in the Williamson synthesis",
            "k": ["alkoxides", "williamson", "sodium metal"],
            "n": 0
        },
        {
            "id": "grignard",
            "tier": "power",
            "t": "Grignard reagents add to aldehydes and ketones to make them; Victor Grignard won the 1912 Nobel Prize",
            "k": ["grignard", "1912"],
            "n": 0
        },
        {
            "id": "reduction",
            "tier": "power",
            "t": "Sodium borohydride or lithium aluminum hydride reduces aldehydes, ketones, or esters to them",
            "k": ["sodium borohydride", "lithium aluminum hydride", "reduces"],
            "n": 0
        },
        {
            "id": "ethene-steam",
            "tier": "power",
            "t": "Industrial ethanol can be made by reacting ethene with steam over a phosphoric acid catalyst",
            "k": ["ethene", "steam", "phosphoric acid"],
            "n": 0
        },
        {
            "id": "methanol-making",
            "tier": "power",
            "t": "Highly toxic methanol was once made by heating wood without air, and later from carbon monoxide and hydrogen",
            "k": ["heating wood", "carbon monoxide", "toxic"],
            "n": 0
        },
        {
            "id": "kohl",
            "tier": "power",
            "t": "The class name comes from the Arabic word for kohl, a fine powder used as eye makeup",
            "k": ["kohl", "arabic", "eye makeup"],
            "n": 0
        },
        {
            "id": "ol-examples",
            "tier": "power",
            "t": "Menthol, cholesterol, and retinol (vitamin A) are members",
            "k": ["menthol", "cholesterol", "retinol"],
            "n": 0,
            "rabbit": "Cholesterol"
        },
        {
            "id": "sweeteners",
            "tier": "power",
            "t": "Sugar-free gums use the sweeteners xylitol and sorbitol, which are members",
            "k": ["xylitol", "sorbitol", "sugar-free"],
            "n": 0
        },
        {
            "id": "thiols",
            "tier": "power",
            "t": "Thiols (mercaptans) are sulfur versions, with –SH in place of –OH",
            "k": ["thiols", "mercaptans", "sulfur"],
            "n": 0,
            "rabbit": "Sulfur"
        },
        {
            "id": "infrared",
            "tier": "power",
            "t": "Infrared spectra show a broad peak from their O–H bonds",
            "k": ["infrared", "broad"],
            "n": 0,
            "rabbit": "Infrared spectroscopy"
        },
        {
            "id": "phenols",
            "tier": "power",
            "t": "Phenols (–OH on a benzene ring) are more acidic and usually counted separately; these compounds are about as acidic as water",
            "k": ["phenols", "benzene ring", "acidic"],
            "n": 0,
            "rabbit": "Benzene"
        }
    ],
    "trap": {
        "title": "The class, not one member",
        "body": "Tossups on this class lean on famous members like ethanol, methanol, and isopropanol, so players blurt one compound’s name, which is wrong when the question asks for the whole class. Others answer “hydroxyl,” the name of the –OH group itself, rather than the compounds that contain it. Phenols also carry –OH groups but are a separate class, and carboxylic acids hide an –OH inside their –COOH group.",
        "fix": "Listen for “these compounds” or “this class,” and give the family name. If the question asks for the –OH group itself, say “hydroxyl”; an –OH on a benzene ring means phenol; an –OH next to a C=O in a –COOH group means carboxylic acid.",
        "line": "Real answer line: <b><u>Alcohols</u></b> (accept <u>alkanol</u>s; prompt on <u>hydroxy</u>l compounds; do not accept “hydroxyl” alone or specific alcohols like “ethanol”)"
    },
    "tests": {
        "right": [
            "Alcohols",
            "alcohol",
            "Alchohols",
            "Alkanols",
            "Primary alcohols"
        ],
        "prompt": [
            "Hydroxyl compounds"
        ],
        "wrong": [
            "Ethanol",
            "Methanol",
            "Hydroxyl",
            "Phenol",
            "Isopropyl alcohol",
            "Ethers",
            "Alkanes",
            "Esters"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
