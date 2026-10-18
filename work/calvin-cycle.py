import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "calvin-cycle",
    "name": "Calvin cycle",
    "mono": "CVC",
    "category": "Biology",
    "qbCategory": "Science · Biology",
    "kicker": "Sugar-building stage of photosynthesis · Fixes carbon dioxide in the stroma",
    "dates": "Nobel Prize in Chemistry, 1961",
    "briefing": "The Calvin cycle is the second half of photosynthesis, where a plant actually builds sugar. In the stroma of each chloroplast, the enzyme RuBisCO grabs carbon dioxide from the air, and the cycle spends ATP and NADPH from the light reactions to turn it into a three-carbon sugar called G3P. Melvin Calvin’s team at Berkeley worked out every step by tracing radioactive carbon through algae, earning him the 1961 Nobel Prize in Chemistry.",
    "answerHtml": "<b><u>Calvin cycle</u></b> (accept <u>Calvin–Benson</u> cycle, <u>Calvin–Benson–Bassham</u> cycle, <u>CBB</u> cycle, <u>light-independent reactions</u>, or <u>dark reactions</u>; prompt on <u>carbon fixation</u>; do not accept “photosynthesis”)",
    "accept": [
        "calvin cycle",
        "calvin cycles",
        "calvin benson cycle",
        "benson calvin cycle",
        "calvin benson bassham cycle",
        "cbb cycle",
        "light independent reactions",
        "light independent reaction",
        "light independent stage",
        "light independent phase",
        "dark reactions",
        "dark reaction"
    ],
    "prompt": [
        "carbon fixation",
        "calvin",
        "light independent"
    ],
    "reject": [
        "photosynthesis",
        "light reactions",
        "light reaction",
        "light dependent reactions",
        "light dependent reaction",
        "krebs cycle",
        "citric acid cycle",
        "tca cycle",
        "glycolysis",
        "cellular respiration",
        "electron transport chain",
        "carbon cycle",
        "cell cycle",
        "c4 pathway",
        "hatch slack pathway",
        "melvin calvin",
        "john calvin",
        "calvinism"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Calvin_cycle",
    "qb": {
        "q": "Calvin cycle",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "The radioactive tracer used to work out this process, carbon-14, had been discovered at Berkeley in 1940 by Sam Ruben and Martin Kamen. Researchers gave the green alga _Chlorella_ [“kluh-REL-uh”] carbon dioxide made with that tracer and stopped the reactions after a few seconds to see which molecules picked it up first.",
            "r": "For 10 points, name this cycle, the second stage of photosynthesis, which turns carbon dioxide into sugar in the stroma."
        },
        {
            "p": "Algae were bathed in light inside a thin, flat glass flask nicknamed the “lollipop” as scientists traced how this process captures carbon. The resulting molecules were separated by two-dimensional paper chromatography and found by laying X-ray film over the paper, a method called autoradiography.",
            "r": "This process earned its Berkeley namesake the 1961 Nobel Prize in Chemistry. For 10 points, name this cycle of photosynthesis that builds sugar from carbon dioxide."
        },
        {
            "p": "In daylight, a small protein called thioredoxin [“thy-oh-ree-DOX-in”] switches on several enzymes of this process, one reason an old nickname suggesting that this process runs in darkness is misleading. This process spends the ATP and NADPH made by the light-capturing reactions in the thylakoid membranes.",
            "r": "For 10 points, name this cycle that takes place in the stroma of chloroplasts and fixes carbon dioxide into sugar."
        },
        {
            "p": "When this process’s first enzyme grabs oxygen instead of carbon dioxide, especially on hot, dry days, the cell wastes energy in a process called photorespiration. That enzyme, RuBisCO [“roo-BISS-koh”], is slow, handling only a few molecules each second, so leaves pack in huge amounts of it.",
            "r": "For 10 points, name this sugar-building cycle, the second stage of photosynthesis, which takes place in the stroma."
        },
        {
            "p": "Corn and sugarcane first trap carbon dioxide in a four-carbon acid using PEP carboxylase [“kar-BOK-sih-lays”], then release it in bundle-sheath cells where this process runs, in a pathway named for Marshall Hatch and Roger Slack. That arrangement of cells is called Kranz anatomy, from the German word for “wreath.”",
            "r": "For 10 points, name this cycle of reactions in the stroma that uses ATP and NADPH to turn carbon dioxide into sugar."
        },
        {
            "p": "Pineapples and cacti open their pores only at night, storing carbon dioxide as malic acid, and then run this process during the day with their pores closed to save water. That strategy is called crassulacean [“kras-yoo-LAY-shun”] acid metabolism, or CAM.",
            "r": "For 10 points, name this cycle, the second stage of photosynthesis, which builds sugar in the stroma of chloroplasts."
        },
        {
            "p": "Most plants are called “C3” plants because this process’s first stable product, 3-phosphoglycerate [“FOS-foh-GLISS-er-ate”], has three carbon atoms. That product forms when a five-carbon sugar called RuBP takes on carbon dioxide and the resulting six-carbon molecule splits in two.",
            "r": "For 10 points, name this cycle, the stage of photosynthesis that uses carbon dioxide to build sugar."
        },
        {
            "p": "For every six molecules of G3P made by this process, five are rearranged to rebuild three molecules of RuBP, and only one leaves to help build glucose. Making one glucose molecule takes six turns of this process, 18 ATP, and 12 NADPH.",
            "r": "For 10 points, name this cycle in the stroma of chloroplasts that fixes carbon dioxide into sugar."
        },
        {
            "p": "Cyanobacteria speed up this process by packing its key enzyme inside protein shells called carboxysomes [“kar-BOK-sih-sohmz”], which concentrate carbon dioxide. Some bacteria that get energy from chemicals instead of light also use this process to fix carbon.",
            "r": "For 10 points, name this cycle, the second stage of photosynthesis, which makes sugar in the stroma of chloroplasts."
        },
        {
            "p": "This process is often divided into three phases: carbon fixation, reduction, and the regeneration of RuBP. In the reduction phase, energy from ATP and electrons from NADPH convert 3-PGA into a three-carbon sugar.",
            "r": "This process uses carbon dioxide that enters leaves through stomata. For 10 points, name this cycle of photosynthesis that takes place in the stroma."
        },
        {
            "p": "The direct product of this process is glyceraldehyde 3-phosphate [“GLISS-er-AL-duh-hyde three FOS-fate”], a three-carbon sugar often shortened to G3P. That sugar can be turned into sucrose and shipped through the phloem, or stored in the chloroplast as starch.",
            "r": "For 10 points, name this cycle that uses ATP and NADPH from the light reactions to fix carbon dioxide."
        },
        {
            "p": "The enzyme that starts this process, RuBisCO, is often called the most abundant protein on Earth. That enzyme attaches carbon dioxide to a five-carbon sugar called RuBP in a step called carbon fixation.",
            "r": "This process is named for a chemist who won the 1961 Nobel Prize in Chemistry. For 10 points, name this cycle, the second stage of photosynthesis."
        },
        {
            "p": "An old nickname for this process wrongly suggests that it happens in darkness, but it mostly runs in daylight, when the light reactions keep making the ATP and NADPH it needs. In the dark, this process soon stops as those supplies run out.",
            "r": "For 10 points, name this cycle in the chloroplast’s stroma that turns carbon dioxide into sugar."
        },
        {
            "p": "This process sends ADP and NADP+ [“N-A-D-P-plus”] back to the thylakoid membranes, where the light reactions recharge them. It does not use light directly, but depends on the ATP and NADPH made in those membranes.",
            "r": "For 10 points, name this cycle, the sugar-building stage of photosynthesis, which takes place in the stroma."
        },
        {
            "p": "Carbon dioxide that enters a leaf through tiny pores called stomata diffuses into chloroplasts, where this process builds it into sugar. This process uses the ATP and NADPH made by the light reactions.",
            "r": "For 10 points, name this second stage of photosynthesis, a cycle named for a Nobel Prize–winning chemist from Berkeley."
        }
    ],
    "clues": [
        {
            "id": "second-stage",
            "tier": "giveaway",
            "t": "The second, sugar-building stage of photosynthesis",
            "k": ["second", "sugar-building", "photosynthesis"],
            "n": 0,
            "rabbit": "Photosynthesis"
        },
        {
            "id": "stroma",
            "tier": "giveaway",
            "t": "Takes place in the stroma, the fluid around the thylakoids inside chloroplasts",
            "k": ["stroma", "thylakoids", "chloroplasts"],
            "n": 0,
            "rabbit": "Chloroplasts"
        },
        {
            "id": "atp-nadph",
            "tier": "giveaway",
            "t": "Spends the ATP and NADPH made by the light reactions",
            "k": ["nadph", "light reactions"],
            "n": 0
        },
        {
            "id": "co2-sugar",
            "tier": "giveaway",
            "t": "Turns carbon dioxide from the air into sugar",
            "k": ["carbon dioxide", "sugar"],
            "n": 0
        },
        {
            "id": "namesake",
            "tier": "giveaway",
            "t": "Named for a Berkeley chemist who won the 1961 Nobel Prize in Chemistry",
            "k": ["berkeley", "1961", "nobel prize"],
            "n": 0
        },
        {
            "id": "rubisco",
            "tier": "middle",
            "t": "Its first enzyme, RuBisCO, attaches carbon dioxide to RuBP; RuBisCO is often called the most abundant protein on Earth",
            "k": ["rubisco", "rubp", "most abundant"],
            "n": 0
        },
        {
            "id": "phases",
            "tier": "middle",
            "t": "Three phases: carbon fixation, reduction, and regeneration of RuBP",
            "k": ["carbon fixation", "reduction", "regeneration"],
            "n": 0
        },
        {
            "id": "g3p",
            "tier": "middle",
            "t": "Its direct product is G3P (glyceraldehyde 3-phosphate), a three-carbon sugar",
            "k": ["g3p", "glyceraldehyde", "three-carbon"],
            "n": 0
        },
        {
            "id": "pga",
            "tier": "middle",
            "t": "Fixing carbon dioxide to five-carbon RuBP makes a six-carbon molecule that splits into two 3-PGA",
            "k": ["3-pga", "five-carbon", "six-carbon"],
            "n": 0
        },
        {
            "id": "old-nickname",
            "tier": "middle",
            "t": "An old nickname wrongly suggests it runs in the dark; it mostly runs in daylight",
            "k": ["old nickname", "daylight"],
            "n": 0
        },
        {
            "id": "carbon-14",
            "tier": "middle",
            "t": "Mapped by giving _Chlorella_ algae carbon dioxide made with radioactive carbon-14",
            "k": ["carbon-14", "chlorella", "radioactive"],
            "n": 0
        },
        {
            "id": "counts",
            "tier": "middle",
            "t": "One glucose takes six turns, 18 ATP, and 12 NADPH",
            "k": ["six turns", "18 atp", "12 nadph"],
            "n": 0
        },
        {
            "id": "sucrose-starch",
            "tier": "middle",
            "t": "Its sugar becomes sucrose (shipped through phloem) or starch (stored in the chloroplast)",
            "k": ["sucrose", "starch", "phloem"],
            "n": 0
        },
        {
            "id": "lollipop",
            "tier": "power",
            "t": "Algae were lit inside a flat glass flask nicknamed the “lollipop”",
            "k": ["lollipop", "flat glass flask"],
            "n": 0
        },
        {
            "id": "chromatography",
            "tier": "power",
            "t": "Its molecules were sorted by two-dimensional paper chromatography and spotted with X-ray film (autoradiography)",
            "k": ["paper chromatography", "autoradiography", "x-ray film"],
            "n": 0
        },
        {
            "id": "ruben-kamen",
            "tier": "power",
            "t": "Carbon-14 was discovered at Berkeley in 1940 by Sam Ruben and Martin Kamen",
            "k": ["ruben", "kamen", "1940"],
            "n": 0
        },
        {
            "id": "photorespiration",
            "tier": "power",
            "t": "When RuBisCO grabs oxygen instead of carbon dioxide, energy is wasted in photorespiration",
            "k": ["photorespiration", "oxygen"],
            "n": 0
        },
        {
            "id": "rubisco-slow",
            "tier": "power",
            "t": "RuBisCO is slow, handling only a few molecules per second, so leaves pack in huge amounts",
            "k": ["slow", "per second"],
            "n": 0
        },
        {
            "id": "c4",
            "tier": "power",
            "t": "C4 species like corn trap carbon dioxide with PEP carboxylase and run it in bundle-sheath cells (Kranz anatomy, the Hatch–Slack pathway)",
            "k": ["pep carboxylase", "bundle-sheath", "kranz", "hatch"],
            "n": 0
        },
        {
            "id": "cam",
            "tier": "power",
            "t": "CAM species like pineapples and cacti store carbon dioxide as malic acid at night and run it by day",
            "k": ["cam", "malic acid", "pineapples", "cacti"],
            "n": 0
        },
        {
            "id": "c3",
            "tier": "power",
            "t": "Most species are “C3” because its first stable product, 3-PGA, has three carbons",
            "k": ["c3", "first stable product"],
            "n": 0
        },
        {
            "id": "thioredoxin",
            "tier": "power",
            "t": "In daylight, a small protein called thioredoxin switches on several of its enzymes",
            "k": ["thioredoxin", "switches on"],
            "n": 0
        },
        {
            "id": "regeneration",
            "tier": "power",
            "t": "Of every six G3P it makes, five rebuild three RuBP and only one leaves",
            "k": ["five", "rebuild", "only one"],
            "n": 0
        },
        {
            "id": "carboxysomes",
            "tier": "power",
            "t": "Cyanobacteria pack its key enzyme into protein shells called carboxysomes",
            "k": ["carboxysomes", "cyanobacteria"],
            "n": 0
        },
        {
            "id": "chemo",
            "tier": "power",
            "t": "Some bacteria that get energy from chemicals instead of light also use it to fix carbon",
            "k": ["chemicals", "bacteria"],
            "n": 0
        },
        {
            "id": "recharge",
            "tier": "power",
            "t": "It sends ADP and NADP+ back to the thylakoids to be recharged",
            "k": ["adp", "nadp+", "recharged"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Part, not the whole",
        "body": "This cycle is only the second half of photosynthesis, so players who hear “chloroplast” or “carbon dioxide” often blurt “photosynthesis,” which is too general. Others mix it up with the light reactions, which happen in the thylakoids and split water, or with the Krebs cycle, the cycle in mitochondria that breaks sugar down instead of building it up.",
        "fix": "Clues about the stroma, RuBisCO, RuBP, G3P, or spending ATP and NADPH mean the Calvin cycle. Water splitting, oxygen release, or photosystems mean the light reactions; acetyl-CoA or the mitochondrial matrix means the Krebs cycle.",
        "line": "Real answer line: <b><u>Calvin cycle</u></b> (accept <u>Calvin–Benson</u> cycle or <u>light-independent reactions</u>; accept <u>dark reactions</u>; prompt on <u>carbon fixation</u>; do not accept “photosynthesis”)"
    },
    "tests": {
        "right": [
            "Calvin cycle",
            "Calvin-Benson cycle",
            "light-independent reactions",
            "dark reactions",
            "Calvin cylce"
        ],
        "prompt": [
            "Carbon fixation",
            "Calvin"
        ],
        "wrong": [
            "Photosynthesis",
            "Krebs cycle",
            "Light reactions",
            "Light-dependent reactions",
            "Glycolysis"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
