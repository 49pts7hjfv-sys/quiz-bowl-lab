import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "dopamine",
    "name": "Dopamine",
    "mono": "DA",
    "category": "Biology",
    "qbCategory": "Science · Biology",
    "kicker": "Chemical messenger in the brain · Key to movement, motivation, and reward",
    "dates": "First made in a lab in 1910",
    "briefing": "Dopamine is a chemical messenger that nerve cells use to signal each other, and it helps your brain control movement and decide what is worth working for. Cells build it from the amino acid tyrosine, mostly in two small midbrain regions, including a dark patch called the substantia nigra. Losing many of the dopamine-making cells there causes Parkinson’s disease, which brings shaking and slow, stiff movements.",
    "answerHtml": "<b><u>Dopamine</u></b> (prompt on <u>neurotransmitter</u> or <u>catecholamine</u>; do not accept “L-DOPA,” “serotonin,” or “norepinephrine”)",
    "accept": [
        "dopamine",
        "dopamin"
    ],
    "prompt": [
        "neurotransmitter",
        "neurotransmitters",
        "catecholamine",
        "catecholamines",
        "monoamine",
        "monoamines"
    ],
    "reject": [
        "l dopa",
        "levodopa",
        "dopa",
        "dopamine receptor",
        "dopamine receptors",
        "dopamine transporter",
        "carbidopa",
        "serotonin",
        "norepinephrine",
        "noradrenaline",
        "epinephrine",
        "adrenaline",
        "acetylcholine",
        "gaba",
        "glutamate",
        "endorphins",
        "endorphin",
        "oxytocin",
        "melatonin",
        "histamine",
        "tyrosine",
        "tryptophan",
        "substantia nigra",
        "parkinsons disease",
        "parkinsons",
        "neuromelanin",
        "prolactin"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Dopamine",
    "qb": {
        "q": "dopamine",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "Arvid Carlsson gave L-DOPA to rabbits that had been left unable to move by the drug reserpine, and they moved again because their brains turned it into this chemical. Carlsson shared the 2000 Nobel Prize in Physiology or Medicine for showing that this chemical is a neurotransmitter.",
            "r": "For 10 points, name this brain chemical linked to movement and reward, whose shortage causes Parkinson’s disease."
        },
        {
            "p": "In 1960, Oleh Hornykiewicz found that brain tissue from people with a certain movement disorder held far less of this chemical than normal. That finding led doctors to treat the disorder with L-DOPA, which the brain turns into this chemical.",
            "r": "That disorder is Parkinson’s disease. For 10 points, name this neurotransmitter linked to the brain’s reward system."
        },
        {
            "p": "George Barger and James Ewens first made this compound in a London lab in 1910, decades before anyone knew that the brain uses it. Cells in the body make this compound from the amino acid tyrosine.",
            "r": "For 10 points, name this neurotransmitter tied to movement, motivation, and reward, whose loss causes Parkinson’s disease."
        },
        {
            "p": "Oliver Sacks’s book _Awakenings_ describes patients left frozen for decades by an illness called encephalitis lethargica [“en-sef-uh-LY-tis luh-THAR-jih-kuh”] who briefly “woke up” in 1969 after taking a drug that the brain turns into this chemical. Robin Williams played a doctor based on Sacks in the 1990 film version.",
            "r": "That drug was L-DOPA. For 10 points, name this neurotransmitter whose loss in the brain causes Parkinson’s disease."
        },
        {
            "p": "Wolfram Schultz found that monkey brain cells that release this chemical fire strongly when a reward comes as a surprise, but dip below their usual rate when an expected reward fails to arrive, a signal called a reward prediction error.",
            "r": "This chemical is made in the midbrain’s substantia nigra. For 10 points, name this neurotransmitter linked to motivation and reward."
        },
        {
            "p": "In 1954, James Olds and Peter Milner found that rats would press a lever over and over to send small electric pulses into certain parts of their brains. Later research tied that behavior to brain circuits that use this chemical.",
            "r": "For 10 points, name this neurotransmitter, often called a “feel-good” chemical, whose loss causes Parkinson’s disease."
        },
        {
            "p": "As cells in the substantia nigra [“sub-STAN-shuh NY-gruh”] make this chemical, some of it turns into a dark pigment called neuromelanin, which gives that brain region its name, meaning “black substance.”",
            "r": "Losing those cells causes Parkinson’s disease. For 10 points, name this neurotransmitter that helps control movement and is linked to reward."
        },
        {
            "p": "This molecule, with the formula C8H11NO2, has a benzene ring carrying two hydroxyl groups, called a catechol [“KAT-uh-kol”], linked to an amine group. Enzymes called MAO and COMT break this molecule down after it is released.",
            "r": "This chemical is made from the amino acid tyrosine. For 10 points, name this neurotransmitter, a catecholamine linked to reward and movement."
        },
        {
            "p": "Cells in the hypothalamus release this chemical to stop the pituitary gland from making prolactin, a hormone that triggers milk production. That signal travels along the tuberoinfundibular [“too-buh-roh-in-fun-DIB-yuh-lur”] pathway, one of four major pathways that carry this chemical.",
            "r": "In the midbrain, the substantia nigra makes this chemical to help control movement. For 10 points, name this neurotransmitter whose loss causes Parkinson’s disease."
        },
        {
            "p": "The enzyme tyrosine hydroxylase carries out the slowest step in making this chemical, turning the amino acid tyrosine into L-DOPA. Another enzyme then turns L-DOPA into this chemical, which cells can later convert into norepinephrine.",
            "r": "Losing the cells that make it causes Parkinson’s disease. For 10 points, name this neurotransmitter, often linked to pleasure and reward."
        },
        {
            "p": "This chemical acts on five kinds of receptors, named D1 through D5, which fall into two families. After it signals, a transporter protein pulls it back into the nerve cell that released it, a process called reuptake.",
            "r": "For 10 points, name this neurotransmitter, made from tyrosine, that is central to the brain’s reward system."
        },
        {
            "p": "The nigrostriatal [“ny-groh-stry-AY-tul”] pathway carries this chemical from the substantia nigra to the striatum, part of the basal ganglia that helps start and smooth out movements. The cells that send it also make a dark pigment called neuromelanin.",
            "r": "Damage to that pathway causes the tremors and slow movements of Parkinson’s disease. For 10 points, name this neurotransmitter made from tyrosine."
        },
        {
            "p": "The mesolimbic pathway carries this chemical from the ventral tegmental [“teg-MEN-tul”] area to the nucleus accumbens [“uh-KUM-benz”], deep in the forebrain. Cells in the ventral tegmental area also send this chemical to the prefrontal cortex along a separate pathway.",
            "r": "Rewards, especially surprising ones, cause bursts of this chemical. For 10 points, name this neurotransmitter, often called a “feel-good” chemical."
        },
        {
            "p": "Doctors cannot treat a shortage of this chemical simply by giving it to patients, because it cannot cross the blood-brain barrier, so they give its precursor, L-DOPA, instead. That precursor was first tested on patients in 1961.",
            "r": "That shortage causes Parkinson’s disease, which brings tremors and slow movement. For 10 points, name this neurotransmitter linked to movement and reward."
        },
        {
            "p": "Nerve cells and adrenal gland cells turn this catecholamine into norepinephrine, and adrenal cells can then turn norepinephrine into epinephrine. This chemical is made mainly in the substantia nigra and the ventral tegmental area.",
            "r": "Losing the cells that make this chemical causes Parkinson’s disease. For 10 points, name this neurotransmitter tied to motivation, pleasure, and reward."
        }
    ],
    "clues": [
        {
            "id": "neurotransmitter",
            "tier": "giveaway",
            "t": "A neurotransmitter: a chemical messenger that carries signals between nerve cells",
            "k": ["neurotransmitter", "chemical messenger", "nerve cells"],
            "n": 0,
            "rabbit": "Neurons"
        },
        {
            "id": "reward",
            "tier": "giveaway",
            "t": "Central to the brain’s reward system, motivation, and pleasure",
            "k": ["reward", "motivation", "pleasure"],
            "n": 0
        },
        {
            "id": "parkinsons",
            "tier": "giveaway",
            "t": "Helps control movement; losing the brain cells that make it causes Parkinson’s disease",
            "k": ["parkinson’s disease", "movement"],
            "n": 0,
            "rabbit": "Parkinson’s disease"
        },
        {
            "id": "feel-good",
            "tier": "giveaway",
            "t": "Often called a “feel-good” chemical, along with serotonin and endorphins",
            "k": ["feel-good", "serotonin", "endorphins"],
            "n": 0,
            "rabbit": "Serotonin"
        },
        {
            "id": "tyrosine",
            "tier": "middle",
            "t": "Built from the amino acid tyrosine, by way of L-DOPA",
            "k": ["tyrosine", "l-dopa", "amino acid"],
            "n": 0,
            "rabbit": "Amino acids"
        },
        {
            "id": "catecholamine",
            "tier": "middle",
            "t": "A catecholamine; cells turn it into norepinephrine, which can become epinephrine",
            "k": ["catecholamine", "norepinephrine", "epinephrine"],
            "n": 0,
            "rabbit": "Epinephrine (adrenaline)"
        },
        {
            "id": "substantia-nigra",
            "tier": "middle",
            "t": "Made mainly in the substantia nigra (“black substance”) and the ventral tegmental area of the midbrain",
            "k": ["substantia nigra", "ventral tegmental area", "midbrain"],
            "n": 0
        },
        {
            "id": "l-dopa",
            "tier": "middle",
            "t": "Parkinson’s is treated with L-DOPA (levodopa), which crosses the blood-brain barrier and turns into it",
            "k": ["levodopa", "blood-brain barrier"],
            "n": 0
        },
        {
            "id": "carlsson",
            "tier": "middle",
            "t": "Arvid Carlsson showed in the 1950s that it is a neurotransmitter and shared the 2000 Nobel Prize in Physiology or Medicine",
            "k": ["carlsson", "2000", "nobel prize"],
            "n": 0
        },
        {
            "id": "awakenings",
            "tier": "middle",
            "t": "Oliver Sacks’s _Awakenings_ tells of patients who briefly “woke up” on L-DOPA in 1969; Robin Williams starred in the 1990 film",
            "k": ["awakenings", "oliver sacks", "robin williams"],
            "n": 0
        },
        {
            "id": "reuptake",
            "tier": "middle",
            "t": "After signaling, a transporter protein pulls it back into the sending cell, a process called reuptake",
            "k": ["reuptake", "transporter"],
            "n": 0
        },
        {
            "id": "barger-ewens",
            "tier": "power",
            "t": "First made in a London lab in 1910 by George Barger and James Ewens",
            "k": ["barger", "ewens", "1910"],
            "n": 0
        },
        {
            "id": "hornykiewicz",
            "tier": "power",
            "t": "Oleh Hornykiewicz found in 1960 that brains affected by Parkinson’s held far less of it, which led to L-DOPA treatment",
            "k": ["hornykiewicz", "1960"],
            "n": 0
        },
        {
            "id": "reserpine-rabbits",
            "tier": "power",
            "t": "Carlsson got rabbits left unable to move by the drug reserpine moving again by giving them L-DOPA",
            "k": ["reserpine", "rabbits"],
            "n": 0
        },
        {
            "id": "schultz",
            "tier": "power",
            "t": "Wolfram Schultz showed that its cells in monkeys fire for surprise rewards and dip when expected rewards fail to come: a “reward prediction error”",
            "k": ["schultz", "prediction error", "monkeys"],
            "n": 0
        },
        {
            "id": "olds-milner",
            "tier": "power",
            "t": "James Olds and Peter Milner (1954) found rats would press a lever again and again to stimulate reward areas of their brains",
            "k": ["olds", "milner", "lever", "1954"],
            "n": 0
        },
        {
            "id": "mesolimbic",
            "tier": "power",
            "t": "The mesolimbic reward pathway carries it from the ventral tegmental area to the nucleus accumbens; a separate pathway carries it to the prefrontal cortex",
            "k": ["mesolimbic", "nucleus accumbens"],
            "n": 0
        },
        {
            "id": "nigrostriatal",
            "tier": "power",
            "t": "The nigrostriatal pathway carries it from the substantia nigra to the striatum, part of the basal ganglia",
            "k": ["nigrostriatal", "striatum", "basal ganglia"],
            "n": 0
        },
        {
            "id": "neuromelanin",
            "tier": "power",
            "t": "Some of it turns into neuromelanin, the dark pigment that gives the substantia nigra its color",
            "k": ["neuromelanin", "pigment"],
            "n": 0
        },
        {
            "id": "catechol",
            "tier": "power",
            "t": "A catechol (benzene ring with two hydroxyl groups) linked to an amine; formula C8H11NO2; broken down by MAO and COMT",
            "k": ["catechol", "hydroxyl", "c8h11no2", "comt"],
            "n": 0
        },
        {
            "id": "prolactin",
            "tier": "power",
            "t": "Released by the hypothalamus along the tuberoinfundibular pathway, it stops the pituitary from making the hormone prolactin",
            "k": ["prolactin", "pituitary", "hypothalamus"],
            "n": 0,
            "rabbit": "Pituitary gland"
        },
        {
            "id": "receptors",
            "tier": "power",
            "t": "Acts on five receptor types, D1 through D5, which fall into two families",
            "k": ["receptor", "d1", "d5", "five"],
            "n": 0
        },
        {
            "id": "tyrosine-hydroxylase",
            "tier": "power",
            "t": "The enzyme tyrosine hydroxylase makes L-DOPA, the slowest step in building it",
            "k": ["tyrosine hydroxylase", "slowest step"],
            "n": 0
        },
        {
            "id": "blood-brain-barrier",
            "tier": "power",
            "t": "It cannot cross the blood-brain barrier itself, so doctors give its precursor instead",
            "k": ["precursor", "cannot cross"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Which feel-good chemical?",
        "body": "Dopamine, serotonin, endorphins, and oxytocin are all called “feel-good” or “happy” chemicals in pop culture, so a quick buzz can grab the wrong one. L-DOPA is the building block that becomes dopamine, not dopamine itself, and norepinephrine and epinephrine are made from dopamine, so all three are wrong here.",
        "fix": "Parkinson’s disease, the substantia nigra, L-DOPA, tyrosine, reward, and motivation point to dopamine. Mood, sleep, the gut, and the amino acid tryptophan point to serotonin. The fight-or-flight response points to epinephrine.",
        "line": "Real answer line: <b><u>Dopamine</u></b> (do not accept “L-DOPA” or “serotonin”)"
    },
    "tests": {
        "right": [
            "Dopamine",
            "dopamin",
            "Dopamene",
            "DOPAMINE"
        ],
        "prompt": [
            "neurotransmitter",
            "catecholamine"
        ],
        "wrong": [
            "L-DOPA",
            "Serotonin",
            "Norepinephrine",
            "Adrenaline",
            "Tyrosine",
            "Dopamine receptor"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
