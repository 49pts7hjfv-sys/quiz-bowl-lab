import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "glycolysis",
    "name": "Glycolysis",
    "mono": "GLY",
    "category": "Biology",
    "qbCategory": "Science · Biology",
    "kicker": "First stage of cellular respiration · Splits glucose into two pyruvates",
    "dates": "All ten steps worked out by 1940",
    "briefing": "Glycolysis is the first step cells take to get energy out of sugar. In ten enzyme-run steps in the cytoplasm, it splits one six-carbon glucose molecule into two three-carbon pyruvate molecules, for a net gain of two ATP. It does not need oxygen, so nearly every living thing can do it, from bacteria to the muscle cells powering a hard sprint.",
    "answerHtml": "<b><u>Glycolysis</u></b> (accept <u>Embden–Meyerhof–Parnas pathway</u> or <u>EMP pathway</u>; prompt on <u>cellular respiration</u>; do not accept “gluconeogenesis” or “fermentation”)",
    "accept": [
        "glycolysis",
        "glycolytic pathway",
        "embden meyerhof parnas pathway",
        "embden meyerhof pathway",
        "emp pathway"
    ],
    "prompt": [
        "cellular respiration",
        "respiration",
        "aerobic respiration",
        "anaerobic respiration"
    ],
    "reject": [
        "gluconeogenesis",
        "glycogenolysis",
        "glycogenesis",
        "glycogen",
        "glucose",
        "pyruvate",
        "pyruvic acid",
        "fermentation",
        "lactic acid fermentation",
        "alcoholic fermentation",
        "krebs cycle",
        "citric acid cycle",
        "tca cycle",
        "calvin cycle",
        "cori cycle",
        "electron transport chain",
        "oxidative phosphorylation",
        "pyruvate oxidation",
        "link reaction",
        "pentose phosphate pathway",
        "entner doudoroff pathway",
        "hydrolysis",
        "lipolysis",
        "photosynthesis",
        "atp"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Glycolysis",
    "qb": {
        "q": "glycolysis",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "Phosphofructokinase [“FOSS-foh-FROOK-toh-KY-nayss”] catalyzes the committed step of this pathway, and it is slowed down by high levels of ATP and citrate but sped up by AMP. Another enzyme in this pathway, aldolase, splits a six-carbon sugar into two three-carbon pieces.",
            "r": "For 10 points, name this first stage of cellular respiration, which breaks glucose into two molecules of pyruvate."
        },
        {
            "p": "Otto Warburg noticed that cancer cells rely heavily on this pathway even when plenty of oxygen is available, a pattern called the Warburg effect. Mature red blood cells, which have no mitochondria, make all of their ATP through this pathway.",
            "r": "For 10 points, name this ten-step pathway in the cytoplasm that splits glucose into pyruvate."
        },
        {
            "p": "Arthur Harden and William Young found that adding phosphate made yeast juice ferment sugar faster, and they identified a sugar with two phosphate groups that builds up during this pathway. Earlier, Eduard Buchner had shown that juice from ground-up yeast cells could still ferment sugar.",
            "r": "For 10 points, name this anaerobic pathway that turns one glucose into two pyruvate molecules and nets two ATP."
        },
        {
            "p": "Otto Meyerhof, who shared a 1922 Nobel Prize for studying how working muscles make lactic acid, is one of three scientists, along with Gustav Embden and Jakub Parnas, whose names are sometimes given to this pathway. All ten of its steps had been worked out by 1940.",
            "r": "For 10 points, name this pathway that splits glucose into two pyruvate molecules in the cytoplasm."
        },
        {
            "p": "Triose phosphate isomerase, an enzyme in this pathway, is often called a “perfect” enzyme because it works about as fast as its target molecules can reach it. In the next step, glyceraldehyde 3-phosphate dehydrogenase adds a phosphate group and passes electrons to NAD+, making NADH.",
            "r": "For 10 points, name this first stage of cellular respiration, which happens in the cytoplasm."
        },
        {
            "p": "Fluoride blocks enolase, the enzyme that makes phosphoenolpyruvate in this pathway, so blood samples for sugar tests are often collected in tubes containing sodium fluoride, which stops blood cells from using up the sugar. The enzyme pyruvate kinase then makes ATP in the final step.",
            "r": "For 10 points, name this ten-step pathway that nets two ATP from each glucose molecule."
        },
        {
            "p": "In the first step of this pathway, hexokinase spends an ATP to attach a phosphate group to a sugar, trapping the sugar inside the cell. Liver cells use a related enzyme, glucokinase, which only works quickly when sugar levels are high.",
            "r": "For 10 points, name this pathway that splits glucose into two pyruvate molecules without needing oxygen."
        },
        {
            "p": "This pathway’s first half is called the energy-investment phase because it uses up two ATP, while its second half, the payoff phase, makes four ATP by substrate-level phosphorylation. That payoff phase also produces two molecules of NADH.",
            "r": "That leaves a net gain of two ATP. For 10 points, name this first stage of cellular respiration."
        },
        {
            "p": "When oxygen runs short, cells regenerate the NAD+ that this pathway needs through fermentation, turning its end product into lactic acid in muscle cells or into ethanol and carbon dioxide in yeast. That lets this pathway keep making small amounts of ATP.",
            "r": "For 10 points, name this pathway in the cytoplasm that breaks glucose into pyruvate."
        },
        {
            "p": "Gluconeogenesis builds new glucose in the liver by running roughly in reverse of this pathway, using different enzymes to get around its three one-way steps. In the Cori cycle, lactic acid made in working muscles after this pathway travels to the liver to be rebuilt into glucose.",
            "r": "For 10 points, name this first stage of cellular respiration, which turns glucose into pyruvate and nets two ATP."
        },
        {
            "p": "In the Pasteur effect, yeast cells break down sugar through this pathway much more slowly when oxygen is present, since aerobic respiration gets far more ATP from each sugar molecule. This pathway is so ancient that nearly every living thing, from bacteria to people, uses it.",
            "r": "It does not need oxygen. For 10 points, name this pathway that splits glucose into two three-carbon pyruvate molecules."
        },
        {
            "p": "The fourth step of this pathway splits fructose 1,6-bisphosphate into two three-carbon sugars, dihydroxyacetone [“dy-hy-DROK-see-ASS-uh-tohn”] phosphate and glyceraldehyde 3-phosphate, which an isomerase then interconverts. This pathway’s name comes from Greek words meaning “sweet” and “splitting.”",
            "r": "For 10 points, name this first stage of cellular respiration, which breaks one glucose into two pyruvate molecules in the cytoplasm."
        },
        {
            "p": "When oxygen is plentiful, the end products of this pathway are carried into mitochondria, where an enzyme complex turns each one into acetyl-CoA [“uh-SEE-tul koh-AY”] and carbon dioxide to feed the Krebs cycle. Unlike those later stages, this pathway takes place in the cytoplasm.",
            "r": "For 10 points, name this first stage of cellular respiration, which splits glucose into pyruvate."
        },
        {
            "p": "The signaling molecule fructose 2,6-bisphosphate strongly speeds up this pathway by switching on phosphofructokinase. During a hard sprint, muscle cells lean heavily on this pathway, which makes ATP quickly without oxygen but releases only a small share of the energy stored in sugar.",
            "r": "Each glucose gives a net of two ATP this way. For 10 points, name this first stage of cellular respiration."
        },
        {
            "p": "In this pathway, phosphoglycerate kinase moves a phosphate group from 1,3-bisphosphoglycerate onto ADP, making the first ATP of the payoff phase. A mutase then shifts the remaining phosphate group to a different carbon atom. Both steps happen twice for every glucose molecule, since that sugar was split in half earlier.",
            "r": "It nets two ATP and two NADH. For 10 points, name this ten-step pathway that turns glucose into pyruvate."
        }
    ],
    "clues": [
        {
            "id": "first-stage",
            "tier": "giveaway",
            "t": "The first stage of cellular respiration",
            "k": ["first stage", "cellular respiration"],
            "n": 0
        },
        {
            "id": "glucose-to-pyruvate",
            "tier": "giveaway",
            "t": "Splits one glucose (six carbons) into two pyruvate molecules (three carbons each)",
            "k": ["glucose", "pyruvate", "six carbons"],
            "n": 0,
            "rabbit": "Glucose"
        },
        {
            "id": "net-two-atp",
            "tier": "giveaway",
            "t": "Nets two ATP (it makes four and spends two) and two NADH for each glucose",
            "k": ["two atp", "nadh", "nets"],
            "n": 0,
            "rabbit": "ATP"
        },
        {
            "id": "cytoplasm",
            "tier": "giveaway",
            "t": "Takes place in the cytoplasm, not in the mitochondria",
            "k": ["cytoplasm", "cytosol"],
            "n": 0
        },
        {
            "id": "no-oxygen",
            "tier": "giveaway",
            "t": "Does not need oxygen (it is anaerobic), so nearly every living thing can do it",
            "k": ["oxygen", "anaerobic"],
            "n": 0
        },
        {
            "id": "ten-steps",
            "tier": "middle",
            "t": "Ten steps, each run by its own enzyme",
            "k": ["ten steps", "enzyme"],
            "n": 0
        },
        {
            "id": "investment-payoff",
            "tier": "middle",
            "t": "An energy-investment phase spends two ATP; a payoff phase then makes four",
            "k": ["energy-investment", "payoff"],
            "n": 0
        },
        {
            "id": "hexokinase",
            "tier": "middle",
            "t": "Hexokinase attaches a phosphate to glucose in the first step, trapping it inside the cell",
            "k": ["hexokinase", "trapping"],
            "n": 0
        },
        {
            "id": "phosphofructokinase",
            "tier": "middle",
            "t": "Phosphofructokinase runs the committed step; ATP and citrate slow it down, and AMP speeds it up",
            "k": ["phosphofructokinase", "committed step", "citrate"],
            "n": 0
        },
        {
            "id": "fermentation",
            "tier": "middle",
            "t": "Fermentation regenerates NAD+ so it can keep going without oxygen: lactic acid in muscles, ethanol and carbon dioxide in yeast",
            "k": ["fermentation", "lactic acid", "ethanol"],
            "n": 0,
            "rabbit": "Lactic acid"
        },
        {
            "id": "substrate-level",
            "tier": "middle",
            "t": "Makes ATP by substrate-level phosphorylation, at the phosphoglycerate kinase and pyruvate kinase steps",
            "k": ["substrate-level", "pyruvate kinase", "phosphoglycerate kinase"],
            "n": 0
        },
        {
            "id": "pyruvate-fate",
            "tier": "middle",
            "t": "With oxygen, its pyruvate enters the mitochondria and becomes acetyl-CoA for the Krebs cycle",
            "k": ["acetyl-coa", "krebs cycle", "mitochondria"],
            "n": 0,
            "rabbit": "Mitochondria"
        },
        {
            "id": "red-blood-cells",
            "tier": "middle",
            "t": "Mature red blood cells, which lack mitochondria, make all of their ATP this way",
            "k": ["red blood cells", "mature"],
            "n": 0,
            "rabbit": "Red blood cells"
        },
        {
            "id": "sprint",
            "tier": "middle",
            "t": "Muscle cells lean on it during a hard sprint because it makes ATP quickly without oxygen",
            "k": ["sprint", "quickly"],
            "n": 0
        },
        {
            "id": "name-meaning",
            "tier": "middle",
            "t": "Its name comes from Greek words meaning “sweet” and “splitting”",
            "k": ["greek", "sweet", "splitting"],
            "n": 0
        },
        {
            "id": "warburg",
            "tier": "power",
            "t": "The Warburg effect: cancer cells rely heavily on it even when plenty of oxygen is around",
            "k": ["warburg", "cancer"],
            "n": 0,
            "rabbit": "Cancer"
        },
        {
            "id": "harden-young",
            "tier": "power",
            "t": "Arthur Harden and William Young found that phosphate sped up fermentation in yeast juice and identified a sugar with two phosphate groups",
            "k": ["harden", "yeast juice", "phosphate"],
            "n": 0
        },
        {
            "id": "buchner",
            "tier": "power",
            "t": "Eduard Buchner showed that juice from ground-up yeast cells could still ferment sugar (1907 Nobel Prize)",
            "k": ["buchner", "ground-up yeast"],
            "n": 0,
            "rabbit": "Enzymes"
        },
        {
            "id": "embden-meyerhof-parnas",
            "tier": "power",
            "t": "Also named for Gustav Embden, Otto Meyerhof, and Jakub Parnas; Meyerhof shared a 1922 Nobel Prize for work on lactic acid in muscles",
            "k": ["meyerhof", "embden", "parnas"],
            "n": 0
        },
        {
            "id": "triose-phosphate-isomerase",
            "tier": "power",
            "t": "Triose phosphate isomerase is called a “perfect” enzyme: it works about as fast as its target molecules can reach it",
            "k": ["triose phosphate isomerase", "perfect"],
            "n": 0
        },
        {
            "id": "gapdh",
            "tier": "power",
            "t": "Glyceraldehyde 3-phosphate dehydrogenase adds a phosphate group and makes NADH",
            "k": ["glyceraldehyde 3-phosphate dehydrogenase", "dehydrogenase"],
            "n": 0
        },
        {
            "id": "aldolase",
            "tier": "power",
            "t": "Aldolase splits fructose 1,6-bisphosphate into two three-carbon sugars, DHAP and glyceraldehyde 3-phosphate",
            "k": ["aldolase", "fructose 1,6-bisphosphate", "dhap"],
            "n": 0
        },
        {
            "id": "fluoride-enolase",
            "tier": "power",
            "t": "Fluoride blocks enolase, the enzyme that makes phosphoenolpyruvate, so blood-sugar samples go in sodium fluoride tubes",
            "k": ["fluoride", "enolase", "phosphoenolpyruvate"],
            "n": 0
        },
        {
            "id": "glucokinase",
            "tier": "power",
            "t": "Liver cells use glucokinase, which works quickly only when sugar levels are high",
            "k": ["glucokinase", "liver"],
            "n": 0
        },
        {
            "id": "gluconeogenesis-cori",
            "tier": "power",
            "t": "Gluconeogenesis runs roughly in reverse, bypassing its three one-way steps; the Cori cycle sends muscle lactic acid to the liver to become glucose",
            "k": ["gluconeogenesis", "cori cycle", "one-way"],
            "n": 0
        },
        {
            "id": "pasteur-effect",
            "tier": "power",
            "t": "The Pasteur effect: yeast run it much more slowly when oxygen is present",
            "k": ["pasteur effect", "yeast"],
            "n": 0,
            "rabbit": "Louis Pasteur"
        },
        {
            "id": "fructose-26-bisphosphate",
            "tier": "power",
            "t": "Fructose 2,6-bisphosphate speeds it up by switching on phosphofructokinase",
            "k": ["fructose 2,6-bisphosphate", "switching"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Not its reverse",
        "body": "Gluconeogenesis runs this pathway roughly backward to build new glucose, and glycogenolysis breaks stored glycogen down into glucose, so the long sugar-names can blur together. Fermentation is a separate step that follows this pathway when oxygen is missing, and the Krebs cycle follows it when oxygen is present.",
        "fix": "Splitting glucose into two pyruvates in the cytoplasm, hexokinase, phosphofructokinase, aldolase, or a net of two ATP all mean glycolysis. Making new glucose means gluconeogenesis, breaking down glycogen means glycogenolysis, and turning pyruvate into lactic acid or ethanol means fermentation.",
        "line": "Real answer line: <b><u>Glycolysis</u></b> (accept <u>Embden–Meyerhof–Parnas pathway</u>; prompt on <u>cellular respiration</u>; do not accept “gluconeogenesis”)"
    },
    "tests": {
        "right": [
            "Glycolysis",
            "glycolisis",
            "Embden-Meyerhof pathway",
            "glycolytic pathway",
            "anaerobic glycolysis"
        ],
        "prompt": [
            "Cellular respiration"
        ],
        "wrong": [
            "Gluconeogenesis",
            "Krebs cycle",
            "Fermentation",
            "Glycogenolysis",
            "Calvin cycle"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
