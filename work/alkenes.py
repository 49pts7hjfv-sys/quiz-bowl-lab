import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TIP = "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."

LINE = "<b><u>Alkenes</u></b> (accept <u>alkene</u> or <u>olefin</u>s; prompt on <u>unsaturated hydrocarbon</u>s; do not accept “alkanes” or “alkynes”)"

data = {
    "id": "alkenes",
    "name": "Alkenes",
    "mono": "ENE",
    "category": "Chemistry",
    "qbCategory": "Science · Chemistry",
    "kicker": "Hydrocarbons with a C=C double bond · Building blocks of plastics",
    "dates": "Markovnikov’s rule, 1870",
    "briefing": "Alkenes are hydrocarbons with at least one carbon–carbon double bond, and their names end in “-ene,” like ethene and propene. That double bond makes them much more reactive than alkanes: they quickly turn orange bromine water colorless, and they link up by the thousands into plastics such as polyethylene and polypropylene. The simplest one, ethene (also called ethylene), is even a plant hormone that makes fruit ripen.",
    "answerHtml": LINE,
    "accept": [
        "alkenes",
        "alkene",
        "olefins",
        "olefin",
        "olefines",
        "olefine"
    ],
    "prompt": [
        "unsaturated hydrocarbons",
        "unsaturated hydrocarbon",
        "unsaturated compounds",
        "unsaturated compound"
    ],
    "reject": [
        "alkane",
        "alkanes",
        "alkyne",
        "alkynes",
        "alkine",
        "alkines",
        "alkyl",
        "alkyls",
        "alkyl halide",
        "alkyl halides",
        "allene",
        "allenes",
        "aromatic",
        "aromatics",
        "aromatic hydrocarbon",
        "aromatic hydrocarbons",
        "alcohol",
        "alcohols",
        "alkali",
        "alkalis",
        "alkoxide",
        "alkoxides",
        "ethene",
        "ethylene",
        "propene",
        "propylene",
        "butene",
        "butylene",
        "benzene",
        "polyethylene",
        "polypropylene",
        "polyolefin",
        "polyolefins",
        "polymer",
        "polymers",
        "cycloalkane",
        "cycloalkanes",
        "diene",
        "dienes",
        "polyene",
        "polyenes",
        "saturated hydrocarbon",
        "saturated hydrocarbons",
        "paraffin",
        "paraffins"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Alkene",
    "qb": {
        "q": "alkene",
        "found": 0,
        "tip": TIP
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "Yves Chauvin [“shoh-VAN”], Robert Grubbs, and Richard Schrock shared the 2005 Nobel Prize in Chemistry for metathesis, a reaction in which two of these compounds trade carbon groups, like two dancing couples swapping partners. Grubbs’s ruthenium catalysts made that reaction practical in ordinary labs.",
            "r": "These compounds’ names end in “-ene.” For 10 points, name these hydrocarbons that contain at least one carbon–carbon double bond."
        },
        {
            "p": "A rule named for Vladimir Markovnikov [“mar-KOV-nih-kof”] predicts that when hydrogen bromide adds to one of these compounds, the hydrogen atom goes to the carbon that already has more hydrogen atoms, and the bromine goes to the other carbon.",
            "r": "These compounds turn orange bromine water colorless. For 10 points, name these hydrocarbons with at least one carbon–carbon double bond."
        },
        {
            "p": "In 1933, Morris Kharasch showed that peroxides make hydrogen bromide add to these compounds the “wrong” way, against Markovnikov’s rule, because the reaction then runs through free radicals. Herbert C. Brown’s hydroboration also adds to these compounds in an “anti-Markovnikov” way.",
            "r": "Hydroboration turns these compounds into alcohols. For 10 points, name these hydrocarbons, such as ethene, that have a carbon–carbon double bond."
        },
        {
            "p": "In ozonolysis [“oh-zoh-NOL-ih-sis”], ozone splits one of these molecules into two pieces, and a reagent such as zinc or dimethyl sulfide then turns those pieces into aldehydes or ketones. Identifying those pieces tells chemists where the original molecule was broken.",
            "r": "For 10 points, name these hydrocarbons, such as propene, whose carbon–carbon double bonds make them unsaturated."
        },
        {
            "p": "In Baeyer’s [“BYE-erz”] test, cold, dilute potassium permanganate loses its purple color and forms a brown solid when it is shaken with these compounds, which it turns into diols. Osmium tetroxide adds two –OH groups to these compounds the same way.",
            "r": "Bromine water also detects them by losing its orange color. For 10 points, name these unsaturated hydrocarbons whose names end in “-ene.”"
        },
        {
            "p": "Zaitsev’s [“ZYE-tsefs”] rule predicts that when a strong base removes HBr from an alkyl bromide, the main product is the more substituted of these compounds, while a bulky base can favor the less substituted one, called the Hofmann product.",
            "r": "Removing water from alcohols also makes them. For 10 points, name these hydrocarbons with at least one carbon–carbon double bond, such as propene."
        },
        {
            "p": "Georg Wittig [“VIT-ik”] shared the 1979 Nobel Prize in Chemistry for a reaction that uses phosphorus ylides [“ILL-idz”] to turn aldehydes and ketones into these compounds. In that reaction, the oxygen atom from the aldehyde or ketone ends up bonded to phosphorus instead.",
            "r": "For 10 points, name these hydrocarbons with a carbon–carbon double bond, which are unsaturated and have names ending in “-ene.”"
        },
        {
            "p": "Karl Ziegler and Giulio Natta [“JOO-lee-oh NAH-tah”] shared the 1963 Nobel Prize in Chemistry for catalysts, made from titanium compounds and aluminum alkyls, that link molecules of these compounds into long, orderly chains. Natta used such catalysts to control which way the side groups of a chain point.",
            "r": "Those catalysts make plastics such as polyethylene and polypropylene. For 10 points, name these hydrocarbons, such as ethylene, that have a carbon–carbon double bond."
        },
        {
            "p": "In 1933, Eric Fawcett and Reginald Gibson at the British company ICI accidentally made a waxy white solid while heating the simplest of these compounds with benzaldehyde at very high pressure. That solid became the world’s most common plastic.",
            "r": "That plastic is polyethylene. For 10 points, name these hydrocarbons, including ethene, that have at least one carbon–carbon double bond."
        },
        {
            "p": "Dutch chemists in the 1790s called the simplest member of this class “olefiant gas,” meaning “oil-forming gas,” because it reacts with chlorine to form an oily liquid. Factories make more of that compound than of any other organic chemical, mostly by steam cracking.",
            "r": "In plants, that compound is a gas hormone that ripens fruit. For 10 points, name this class of hydrocarbons, including ethene, that have a carbon–carbon double bond."
        },
        {
            "p": "Chemists label some isomers of these compounds Z, from the German word zusammen [“tsoo-ZAH-men”], meaning “together,” and others E, from entgegen [“ent-GAY-gen”], meaning “opposite,” by using priority rules named for Cahn, Ingold, and Prelog. The Z form has its two higher-priority groups on the same side.",
            "r": "Because their key bond cannot rotate, 2-butene comes in cis and trans forms. For 10 points, name these hydrocarbons with a carbon–carbon double bond."
        },
        {
            "p": "Vision begins when light flips one bond in the molecule retinal [“RET-ih-nal”] from a bent cis shape to a straight trans shape inside the protein rhodopsin [“roh-DOP-sin”]. Retinal is a long chain with several of the bonds that define this class of compounds.",
            "r": "For 10 points, name these hydrocarbons, such as ethene and propene, that contain a carbon–carbon double bond."
        },
        {
            "p": "In the Diels–Alder [“DEELZ AHL-der”] reaction, a diene joins with one of these compounds, called the dienophile [“dye-EE-nuh-file”], to build a six-membered ring. Otto Diels and Kurt Alder shared the 1950 Nobel Prize in Chemistry for that reaction.",
            "r": "For 10 points, name these unsaturated hydrocarbons, such as ethylene, whose names end in “-ene” and which turn bromine water colorless."
        },
        {
            "p": "Paul Sabatier [“sah-bah-TYAY”] won a Nobel Prize for using finely powdered nickel to help hydrogen add to these compounds, turning them into alkanes. Partly hydrogenating vegetable oils this way makes solid margarine but can also create trans fats, which many countries have restricted.",
            "r": "For 10 points, name these unsaturated hydrocarbons, such as ethene, whose names end in “-ene.”"
        },
        {
            "p": "Each carbon atom in the key bond of these compounds is sp2 hybridized and trigonal planar, with bond angles near 120 degrees, because that bond is made of one sigma bond and one pi bond. Non-ring members with just one such bond have the general formula CnH2n.",
            "r": "For 10 points, name these hydrocarbons with at least one carbon–carbon double bond, such as ethene."
        }
    ],
    "clues": [
        {
            "id": "double-bond",
            "tier": "giveaway",
            "t": "Hydrocarbons with at least one carbon–carbon double bond",
            "k": ["double bond", "hydrocarbons"],
            "n": 0
        },
        {
            "id": "ene-names",
            "tier": "giveaway",
            "t": "Their names end in “-ene,” like ethene and propene",
            "k": ["-ene", "ethene", "propene"],
            "n": 0
        },
        {
            "id": "unsaturated",
            "tier": "giveaway",
            "t": "Unsaturated: more atoms can be added across the double bond",
            "k": ["unsaturated", "added"],
            "n": 0
        },
        {
            "id": "bromine-water",
            "tier": "giveaway",
            "t": "Turn orange bromine water colorless",
            "k": ["bromine water", "colorless", "orange"],
            "n": 0
        },
        {
            "id": "plastics",
            "tier": "giveaway",
            "t": "Link up into plastics: ethene makes polyethylene, and propene makes polypropylene",
            "k": ["polyethylene", "polypropylene", "plastics"],
            "n": 0,
            "rabbit": "Polymers"
        },
        {
            "id": "formula",
            "tier": "middle",
            "t": "Non-ring ones with one double bond have the general formula CnH2n",
            "k": ["general formula", "cnh2n"],
            "n": 0
        },
        {
            "id": "pi-bond",
            "tier": "middle",
            "t": "The double bond is one sigma bond plus one pi bond; its carbons are sp2 and trigonal planar, about 120°",
            "k": ["pi bond", "sigma", "trigonal planar"],
            "n": 0
        },
        {
            "id": "addition",
            "tier": "middle",
            "t": "They undergo addition reactions: hydrogen, halogens, water, and hydrogen halides add across the double bond",
            "k": ["addition reactions", "halogens", "hydrogen halides"],
            "n": 0
        },
        {
            "id": "hydrogenation",
            "tier": "middle",
            "t": "Hydrogenation with a nickel catalyst (Paul Sabatier) turns them into alkanes; it is used to make margarine from oils",
            "k": ["hydrogenation", "nickel", "margarine", "sabatier"],
            "n": 0,
            "rabbit": "Hydrogen"
        },
        {
            "id": "markovnikov",
            "tier": "middle",
            "t": "Markovnikov’s rule: when HBr adds, the hydrogen goes to the carbon that already has more hydrogens",
            "k": ["markovnikov", "more hydrogens"],
            "n": 0
        },
        {
            "id": "cis-trans",
            "tier": "middle",
            "t": "The double bond can’t rotate, so some, like 2-butene, have cis and trans isomers",
            "k": ["cis", "trans", "rotate", "2-butene"],
            "n": 0
        },
        {
            "id": "ripening",
            "tier": "middle",
            "t": "Ethylene (ethene), the simplest one, is a plant hormone that ripens fruit",
            "k": ["plant hormone", "ripens", "ethylene"],
            "n": 0
        },
        {
            "id": "cracking",
            "tier": "middle",
            "t": "Cracking big hydrocarbons from crude oil makes them; ethylene is the most-produced organic chemical",
            "k": ["cracking", "crude oil", "most-produced"],
            "n": 0
        },
        {
            "id": "dehydration",
            "tier": "middle",
            "t": "Removing water from alcohols with hot concentrated sulfuric acid makes them",
            "k": ["removing water", "alcohols", "sulfuric acid"],
            "n": 0,
            "rabbit": "Alcohols (chemistry)"
        },
        {
            "id": "metathesis",
            "tier": "power",
            "t": "Chauvin, Grubbs, and Schrock won the 2005 Nobel Prize for metathesis, which swaps the groups on their double bonds",
            "k": ["metathesis", "grubbs", "2005"],
            "n": 0
        },
        {
            "id": "ziegler-natta",
            "tier": "power",
            "t": "Ziegler–Natta catalysts (1963 Nobel), made from titanium and aluminum compounds, link them into orderly chains",
            "k": ["ziegler", "natta", "1963"],
            "n": 0
        },
        {
            "id": "ici-1933",
            "tier": "power",
            "t": "Eric Fawcett and Reginald Gibson made polyethylene by accident at ICI in 1933",
            "k": ["fawcett", "gibson", "1933"],
            "n": 0
        },
        {
            "id": "ozonolysis",
            "tier": "power",
            "t": "Ozonolysis splits them into aldehydes or ketones, showing where the double bond was",
            "k": ["ozonolysis", "aldehydes", "ketones"],
            "n": 0
        },
        {
            "id": "baeyer",
            "tier": "power",
            "t": "Baeyer’s test: cold, purple potassium permanganate turns brown as it makes diols from them",
            "k": ["baeyer", "permanganate", "diols"],
            "n": 0
        },
        {
            "id": "kharasch",
            "tier": "power",
            "t": "Kharasch’s peroxide effect (1933): peroxides make HBr add the anti-Markovnikov way, through free radicals",
            "k": ["kharasch", "peroxide", "anti-markovnikov"],
            "n": 0
        },
        {
            "id": "hydroboration",
            "tier": "power",
            "t": "Herbert C. Brown’s hydroboration turns them into alcohols with the –OH on the less crowded carbon",
            "k": ["hydroboration", "less crowded"],
            "n": 0
        },
        {
            "id": "zaitsev",
            "tier": "power",
            "t": "Zaitsev’s rule: eliminations usually give the more substituted one; bulky bases give the Hofmann product",
            "k": ["zaitsev", "more substituted", "hofmann"],
            "n": 0
        },
        {
            "id": "wittig",
            "tier": "power",
            "t": "Georg Wittig (1979 Nobel) made them from aldehydes and ketones using phosphorus ylides",
            "k": ["wittig", "ylides", "1979"],
            "n": 0
        },
        {
            "id": "e-z",
            "tier": "power",
            "t": "E/Z names: Z from zusammen (“together”) and E from entgegen (“opposite”), using Cahn–Ingold–Prelog priorities",
            "k": ["zusammen", "entgegen", "cahn–ingold–prelog"],
            "n": 0
        },
        {
            "id": "retinal",
            "tier": "power",
            "t": "Vision starts when light flips a double bond in retinal from cis to trans inside rhodopsin",
            "k": ["retinal", "rhodopsin", "vision"],
            "n": 0
        },
        {
            "id": "diels-alder",
            "tier": "power",
            "t": "In the Diels–Alder reaction (1950 Nobel), one acts as the dienophile that joins a diene to make a six-membered ring",
            "k": ["dienophile", "diels–alder", "six-membered"],
            "n": 0,
            "rabbit": "Diels–Alder reaction"
        },
        {
            "id": "olefiant",
            "tier": "power",
            "t": "Ethylene was once called “olefiant gas” (oil-forming gas), since it reacts with chlorine to make an oily liquid",
            "k": ["olefiant", "oil-forming"],
            "n": 0
        }
    ],
    "trap": {
        "title": "One vowel: a, e, or y",
        "body": "Alkanes (only single bonds), alkenes (a carbon–carbon double bond), and alkynes (a triple bond) differ by a single vowel, so a slip of the tongue gives a wrong answer. Players also blurt “ethylene,” the simplest example, when the question wants the whole class, or “alcohols,” since many clues describe reactions that turn these compounds into alcohols.",
        "fix": "Match the vowel to the bond: a = single (saturated, “-ane”), e = double (“-ene”), y = triple (“-yne”). Bromine water turning colorless, Markovnikov’s rule, cis–trans isomers, and polyethylene all mean double bonds.",
        "line": "Real answer line: " + LINE
    },
    "tests": {
        "right": [
            "Alkenes",
            "alkene",
            "Olefins",
            "Alkens",
            "alkene hydrocarbons"
        ],
        "prompt": [
            "Unsaturated hydrocarbons"
        ],
        "wrong": [
            "Alkanes",
            "Alkynes",
            "Ethylene",
            "Alcohols",
            "Polyethylene",
            "Allenes",
            "Dienes",
            "Benzene"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
