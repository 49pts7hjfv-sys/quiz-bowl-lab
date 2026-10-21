import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "lactic-acid",
    "name": "Lactic acid",
    "mono": "LA",
    "category": "Biology",
    "qbCategory": "Science · Biology",
    "kicker": "Sour product of fermentation · Made in yogurt and oxygen-starved muscles",
    "dates": "Isolated from sour milk in 1780",
    "briefing": "Lactic acid is the sour compound in yogurt and sour milk, and your own muscles make it too when you sprint so hard that oxygen can’t keep up. Bacteria in yogurt, sauerkraut, and even the plaque on your teeth make it by fermenting sugar, while your liver turns lactic acid from muscles back into glucose. For years it was blamed for next-day muscle soreness, but many scientists now doubt that idea.",
    "answerHtml": "<b><u>Lactic acid</u></b> (accept <u>lactate</u>; prompt on <u>lactic</u> alone or <u>lactic acid fermentation</u>; do not accept “lactose,” “pyruvate,” or “ethanol”)",
    "accept": [
        "lactic acid",
        "lactic acids",
        "lactate",
        "lactates",
        "l lactic acid",
        "d lactic acid",
        "l lactate",
        "d lactate",
        "2 hydroxypropanoic acid",
        "2 hydroxypropionic acid"
    ],
    "prompt": [
        "lactic",
        "lactic acid fermentation",
        "lactate fermentation",
        "lactic fermentation"
    ],
    "reject": [
        "lactose",
        "lactase",
        "pyruvate",
        "pyruvic acid",
        "ethanol",
        "ethyl alcohol",
        "alcohol",
        "alcoholic fermentation",
        "ethanol fermentation",
        "acetic acid",
        "citric acid",
        "formic acid",
        "carbonic acid",
        "uric acid",
        "malic acid",
        "butyric acid",
        "propanoic acid",
        "propionic acid",
        "lactobacillus",
        "lactobacilli",
        "lactic acid bacteria",
        "lactate dehydrogenase",
        "ldh",
        "lactate threshold",
        "polylactic acid",
        "pla",
        "glucose",
        "glycogen",
        "galactose",
        "lactulose",
        "acetaldehyde",
        "cori cycle",
        "glycolysis",
        "carbon dioxide",
        "atp",
        "nadh"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Lactic_acid",
    "qb": {
        "q": "lactic acid",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "In 1780, the Swedish chemist Carl Wilhelm Scheele [“SHAY-luh”] first isolated this compound from sour milk. Its name comes from the Latin word for milk, and it exists in two mirror-image forms, labeled L and D.",
            "r": "Bacteria that make it turn milk into yogurt. For 10 points, name this acid made by muscles that run short of oxygen."
        },
        {
            "p": "Louis Pasteur’s 1857 paper on the fermentation that produces this compound helped convince scientists that fermentation is carried out by living microbes, not by a purely chemical process. That kind of fermentation also preserves sauerkraut and kimchi.",
            "r": "Human muscles make it from pyruvate during hard exercise. For 10 points, name this acid found in sour milk and yogurt."
        },
        {
            "p": "Otto Meyerhof [“MY-er-hoff”] shared the 1922 Nobel Prize in Physiology or Medicine with A. V. Hill for finding a fixed relationship between the body’s oxygen use and its processing of this compound. The pathway that leads to this compound, glycolysis, is sometimes named partly for Meyerhof.",
            "r": "Muscles make it when they run short of oxygen. For 10 points, name this acid that gives yogurt its sour taste."
        },
        {
            "p": "In a loop named for Carl and Gerty Cori, the liver rebuilds this compound into glucose. Gerty Cori, who won the 1947 Nobel Prize along with her husband, was the first American woman to win a Nobel Prize in science.",
            "r": "Working muscles make it from pyruvate when oxygen runs low. For 10 points, name this acid that also sours milk."
        },
        {
            "p": "An enzyme called LDH makes this compound by adding hydrogen to pyruvate, turning NADH back into NAD+. That lets glycolysis keep making a little ATP even when no oxygen is available. Yeast handle the same problem by making ethanol instead.",
            "r": "For 10 points, name this acid made by muscles during hard exercise and by the bacteria in yogurt."
        },
        {
            "p": "One carbon atom in this compound is chiral, so it comes in two mirror-image forms, labeled L and D, that rotate polarized light in opposite directions. Its formula is C3H6O3, and it carries both a hydroxyl group and a carboxyl group.",
            "r": "Bacteria such as _Lactobacillus_ make it in yogurt. For 10 points, name this acid that muscles make when they run short of oxygen."
        },
        {
            "p": "Long chains of this compound make up PLA, a biodegradable plastic often made from corn and widely used in 3D printers. It belongs to a group called alpha-hydroxy acids, which are used in some skin-care products.",
            "r": "Muscles make it from pyruvate when oxygen runs low. For 10 points, name this acid that gives sour milk its taste."
        },
        {
            "p": "Bacteria in dental plaque, such as _Streptococcus mutans_ [“MYOO-tanz”], feed on sugar and release this compound, which can dissolve tooth enamel and lead to cavities. Those bacteria break down sugar without using oxygen, by fermentation.",
            "r": "Human muscles also make it during hard exercise. For 10 points, name this acid made from pyruvate during fermentation."
        },
        {
            "p": "Because they have no mitochondria, red blood cells make all of their ATP by glycolysis and constantly release this compound into the blood. The liver and the heart take it up from the blood, and the heart can even burn it as fuel.",
            "r": "Yogurt bacteria make it from sugar. For 10 points, name this acid that muscles make when oxygen runs short."
        },
        {
            "p": "Endurance athletes train to raise the exercise intensity at which this compound starts piling up quickly in their blood, a point often called the anaerobic threshold. Coaches sometimes measure it with a finger-prick blood test during workouts.",
            "r": "Its supposed role in next-day muscle soreness is now widely doubted. For 10 points, name this acid made by muscles short of oxygen."
        },
        {
            "p": "In the 1920s, Otto Warburg noticed that many cancer cells break down glucose and make large amounts of this compound even when plenty of oxygen is around, a pattern now called the Warburg effect. Most normal cells make large amounts of it only when oxygen is scarce.",
            "r": "Bacteria make it when they turn milk into yogurt. For 10 points, name this acid produced by fermentation in muscle cells."
        },
        {
            "p": "Bacteria such as _Leuconostoc_ [“loo-koh-NOSS-tock”] and _Lactobacillus_ turn cabbage into sauerkraut and kimchi by fermenting its sugars into this compound, which makes the vegetables sour and helps keep harmful microbes from growing. Silage for cattle is preserved the same way.",
            "r": "Muscles make it when they run short of oxygen. For 10 points, name this acid that gives yogurt its tang."
        },
        {
            "p": "When bacteria such as _Streptococcus thermophilus_ ferment milk sugar into this compound, the rising acidity makes milk proteins called caseins [“KAY-seenz”] clump together into a thick gel. A partner bacterium in that process, _Lactobacillus bulgaricus_, is named for Bulgaria.",
            "r": "That is how milk becomes yogurt. For 10 points, name this acid also made by muscles that run short of oxygen."
        },
        {
            "p": "The tangy flavor of sourdough bread comes partly from this compound, made by bacteria that live alongside wild yeast in the dough’s starter. Those bacteria, like the yeast, can break down sugar without oxygen. The yeast instead make carbon dioxide, which makes the dough rise.",
            "r": "Muscles make it from pyruvate when oxygen runs low. For 10 points, name this acid found in sour milk."
        },
        {
            "p": "Mosquitoes find people partly by sensing this compound in human sweat, together with the carbon dioxide that people breathe out. It is a three-carbon molecule with a hydroxyl group right next to its carboxyl group.",
            "r": "Yogurt bacteria make it from milk sugar. For 10 points, name this acid that muscles make from pyruvate when oxygen runs short."
        }
    ],
    "clues": [
        {
            "id": "muscles-oxygen",
            "tier": "giveaway",
            "t": "Muscles make it when they run short of oxygen during hard exercise",
            "k": ["muscles", "oxygen", "exercise"],
            "n": 0,
            "rabbit": "Muscles"
        },
        {
            "id": "yogurt",
            "tier": "giveaway",
            "t": "Gives yogurt and sour milk their tangy, sour taste",
            "k": ["yogurt", "sour milk", "tangy"],
            "n": 0
        },
        {
            "id": "fermentation",
            "tier": "giveaway",
            "t": "The end product of the fermentation that happens in muscle cells and in many bacteria",
            "k": ["fermentation", "bacteria", "muscle cells"],
            "n": 0
        },
        {
            "id": "pyruvate",
            "tier": "middle",
            "t": "Made from pyruvate, the end product of glycolysis, when oxygen is scarce",
            "k": ["pyruvate", "glycolysis", "scarce"],
            "n": 0,
            "rabbit": "Glycolysis"
        },
        {
            "id": "nad",
            "tier": "middle",
            "t": "Making it turns NADH back into NAD+, so glycolysis can keep making ATP without oxygen",
            "k": ["nadh", "without oxygen", "nad+"],
            "n": 0
        },
        {
            "id": "ethanol-contrast",
            "tier": "middle",
            "t": "Yeast turn pyruvate into ethanol and carbon dioxide instead, in alcoholic fermentation",
            "k": ["yeast", "ethanol", "alcoholic fermentation"],
            "n": 0,
            "rabbit": "Yeast"
        },
        {
            "id": "sauerkraut",
            "tier": "middle",
            "t": "Bacteria such as _Lactobacillus_ make it to turn cabbage into sauerkraut and kimchi",
            "k": ["lactobacillus", "sauerkraut", "kimchi"],
            "n": 0
        },
        {
            "id": "cori-cycle",
            "tier": "middle",
            "t": "In the Cori cycle, the liver rebuilds it into glucose",
            "k": ["cori cycle", "liver", "glucose"],
            "n": 0,
            "rabbit": "Liver"
        },
        {
            "id": "soreness",
            "tier": "middle",
            "t": "Long blamed for next-day muscle soreness, an idea that many scientists now doubt",
            "k": ["soreness", "next-day", "doubt"],
            "n": 0
        },
        {
            "id": "tooth-decay",
            "tier": "middle",
            "t": "Mouth bacteria such as _Streptococcus mutans_ make it from sugar; it can dissolve tooth enamel, leading to cavities",
            "k": ["streptococcus mutans", "enamel", "cavities"],
            "n": 0,
            "rabbit": "Teeth"
        },
        {
            "id": "casein",
            "tier": "middle",
            "t": "In yogurt making, it makes milk proteins called caseins clump into a thick gel",
            "k": ["caseins", "thick gel"],
            "n": 0
        },
        {
            "id": "scheele",
            "tier": "power",
            "t": "Carl Wilhelm Scheele first isolated it from sour milk in 1780; its name comes from the Latin word for milk",
            "k": ["scheele", "1780", "latin"],
            "n": 0
        },
        {
            "id": "pasteur",
            "tier": "power",
            "t": "Louis Pasteur’s 1857 paper on the fermentation that makes it helped show that living microbes cause fermentation",
            "k": ["pasteur", "1857", "microbes"],
            "n": 0,
            "rabbit": "Louis Pasteur"
        },
        {
            "id": "meyerhof",
            "tier": "power",
            "t": "Otto Meyerhof shared the 1922 Nobel Prize with A. V. Hill for linking the body’s oxygen use to its processing of this compound",
            "k": ["meyerhof", "1922", "hill"],
            "n": 0
        },
        {
            "id": "gerty-cori",
            "tier": "power",
            "t": "Carl and Gerty Cori won the 1947 Nobel Prize; Gerty was the first American woman to win a Nobel Prize in science",
            "k": ["gerty cori", "1947", "first american woman"],
            "n": 0
        },
        {
            "id": "chiral",
            "tier": "power",
            "t": "Has one chiral carbon, so it comes in two mirror-image forms, L and D; its formula is C3H6O3",
            "k": ["chiral", "mirror-image", "c3h6o3"],
            "n": 0
        },
        {
            "id": "pla",
            "tier": "power",
            "t": "Long chains of it make PLA, a biodegradable plastic often made from corn and used in 3D printing",
            "k": ["pla", "biodegradable", "3d printing"],
            "n": 0,
            "rabbit": "Corn (maize)"
        },
        {
            "id": "ldh",
            "tier": "power",
            "t": "An enzyme called LDH makes it by adding hydrogen to pyruvate",
            "k": ["ldh", "adding hydrogen"],
            "n": 0
        },
        {
            "id": "red-blood-cells",
            "tier": "power",
            "t": "Red blood cells, which lack mitochondria, constantly release it; the heart can burn it as fuel",
            "k": ["red blood cells", "mitochondria", "fuel"],
            "n": 0,
            "rabbit": "Red blood cells"
        },
        {
            "id": "threshold",
            "tier": "power",
            "t": "Athletes train to raise the intensity at which it piles up in their blood, often called the anaerobic threshold",
            "k": ["anaerobic threshold", "athletes"],
            "n": 0
        },
        {
            "id": "warburg",
            "tier": "power",
            "t": "Otto Warburg found in the 1920s that many cancer cells make lots of it even with plenty of oxygen",
            "k": ["warburg", "cancer cells", "1920s"],
            "n": 0,
            "rabbit": "Cancer"
        },
        {
            "id": "alpha-hydroxy",
            "tier": "power",
            "t": "An alpha-hydroxy acid, one of a group of chemicals used in some skin-care products",
            "k": ["alpha-hydroxy", "skin-care"],
            "n": 0
        },
        {
            "id": "mosquitoes",
            "tier": "power",
            "t": "Mosquitoes find people partly by sensing it in sweat, along with the carbon dioxide people breathe out",
            "k": ["mosquitoes", "sweat"],
            "n": 0
        },
        {
            "id": "sourdough",
            "tier": "power",
            "t": "Bacteria in a sourdough starter make it, giving the bread its tang, while wild yeast make the dough rise",
            "k": ["sourdough", "starter"],
            "n": 0
        },
        {
            "id": "leuconostoc-silage",
            "tier": "power",
            "t": "_Leuconostoc_ bacteria help start sauerkraut fermentation; silage for cattle is preserved the same way",
            "k": ["leuconostoc", "silage"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Lactic, lactose, or lactase?",
        "body": "Three milk words sound alike: lactose is milk sugar, lactase is the enzyme that digests lactose, and lactic acid is the sour compound bacteria make when they ferment that sugar. Players also blurt pyruvate, the molecule lactic acid is made from, or ethanol, which yeast make instead in alcoholic fermentation, and all of those are wrong. Answering with the process, “lactic acid fermentation,” only earns a prompt to name the compound.",
        "fix": "Sour taste, yogurt, oxygen-starved muscles, the Cori cycle, or Scheele and sour milk mean lactic acid (lactate is fine too). “This sugar” in milk means lactose, “this enzyme” that breaks it down means lactase, and yeast making carbon dioxide bubbles points to ethanol.",
        "line": "Real answer line: <b><u>Lactic acid</u></b> (accept <u>lactate</u>; prompt on <u>lactic</u> alone or <u>lactic acid fermentation</u>; do not accept “lactose,” “pyruvate,” or “ethanol”)"
    },
    "tests": {
        "right": [
            "Lactic acid",
            "lactate",
            "L-lactic acid",
            "Lactic acd",
            "lactic acids"
        ],
        "prompt": [
            "Lactic",
            "Lactic acid fermentation"
        ],
        "wrong": [
            "Lactose",
            "Pyruvate",
            "Ethanol",
            "Alcoholic fermentation",
            "Acetic acid",
            "Lactase",
            "Lactobacillus",
            "Fermentation"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
