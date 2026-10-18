import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "serotonin",
    "name": "Serotonin",
    "mono": "5HT",
    "category": "Biology",
    "qbCategory": "Science · Biology",
    "kicker": "Chemical messenger made from tryptophan · Helps regulate mood and sleep",
    "dates": "Named in 1948",
    "briefing": "Serotonin is a chemical messenger that nerve cells use to pass signals to one another, and it helps regulate mood, sleep, appetite, and digestion. The body builds it from tryptophan, an amino acid found in foods like eggs, cheese, and turkey. Surprisingly, most of the body’s serotonin is made in the gut rather than the brain, and at night a small gland in the brain turns some of it into melatonin, a hormone that helps control sleep.",
    "answerHtml": "<b><u>Serotonin</u></b> (accept <u>5-hydroxytryptamine</u> or <u>5-HT</u>; prompt on <u>monoamine</u>; do not accept “melatonin,” “tryptophan,” or “dopamine”)",
    "accept": [
        "serotonin",
        "5 hydroxytryptamine",
        "five hydroxytryptamine",
        "5 ht",
        "5ht"
    ],
    "prompt": [
        "monoamine",
        "monoamines",
        "monoamine neurotransmitter",
        "indoleamine"
    ],
    "reject": [
        "melatonin",
        "tryptophan",
        "l tryptophan",
        "5 hydroxytryptophan",
        "5 htp",
        "dopamine",
        "norepinephrine",
        "noradrenaline",
        "epinephrine",
        "adrenaline",
        "acetylcholine",
        "histamine",
        "gaba",
        "glutamate",
        "endorphin",
        "endorphins",
        "oxytocin",
        "cortisol",
        "tyrosine",
        "ssri",
        "ssris",
        "selective serotonin reuptake inhibitor",
        "selective serotonin reuptake inhibitors",
        "serotonin reuptake inhibitor",
        "serotonin reuptake inhibitors",
        "serotonin transporter",
        "monoamine oxidase",
        "fluoxetine",
        "prozac"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Serotonin",
    "qb": {
        "q": "serotonin",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "In 1948, Maurice Rapport, Arda Green, and Irvine Page at the Cleveland Clinic named this substance after isolating it from blood serum, because it made blood vessels tighten, changing their “tone.” It is often grouped with dopamine and norepinephrine as a monoamine.",
            "r": "For 10 points, name this neurotransmitter, made from the amino acid tryptophan, that helps regulate mood, sleep, and appetite."
        },
        {
            "p": "In the 1930s, Italian scientist Vittorio Erspamer [“er-SPAH-mer”] found a chemical in cells lining the gut that made smooth muscle contract, and he named it enteramine. In 1952, enteramine was shown to be the same chemical as this one, which had been found in blood.",
            "r": "Most of the body’s supply of it is made in the gut. For 10 points, name this neurotransmitter that helps control mood, sleep, and digestion."
        },
        {
            "p": "Betty Twarog [“TWAR-og”], who studied this chemical in the muscles of mussels, found it in the brains of mammals in 1953 while working with Irvine Page. In the brain, most of the nerve cells that make it sit in clusters in the brainstem called the raphe [“RAY-fee”] nuclei.",
            "r": "The pineal gland turns it into melatonin. For 10 points, name this neurotransmitter made from tryptophan."
        },
        {
            "p": "The slowest step in making this chemical adds a hydroxyl group to an amino acid, and a second enzyme then removes a carboxyl group to finish the job. This chemical’s two-ring indole [“IN-dohl”] structure comes from that amino acid.",
            "r": "That amino acid is tryptophan. For 10 points, name this neurotransmitter that helps regulate mood, sleep, and appetite."
        },
        {
            "p": "Blood cell fragments called platelets soak up this chemical from the blood and release it at a wound, where it helps nearby blood vessels narrow. Platelets cannot make it themselves; they collect it after cells in the gut make it.",
            "r": "In the brain, it acts as a neurotransmitter. For 10 points, name this chemical messenger linked to mood and sleep."
        },
        {
            "p": "At night, the pineal [“PIN-ee-ul”] gland adds an acetyl group to this chemical and then a methyl group, turning it into a hormone that helps control the body’s daily rhythm. Light hitting the eyes slows that conversion.",
            "r": "That hormone is melatonin. For 10 points, name this neurotransmitter, made from tryptophan, that helps regulate mood and sleep."
        },
        {
            "p": "Fluoxetine [“floo-OK-suh-teen”], sold as Prozac, belongs to a class of antidepressant medicines that block a protein pump called a transporter, which normally carries this chemical back into the nerve cell that released it. Blocking that reuptake lets this chemical stay longer in the synapse.",
            "r": "Those medicines are called SSRIs. For 10 points, name this neurotransmitter made from tryptophan."
        },
        {
            "p": "The enzyme monoamine oxidase breaks this chemical down, and some of the earliest antidepressant medicines worked by blocking that enzyme. Unlike dopamine and norepinephrine, which are catecholamines, this chemical is an indoleamine [“IN-dohl-uh-meen”]. Its molecular formula is C10H12N2O.",
            "r": "It is made from the amino acid tryptophan. For 10 points, name this neurotransmitter that helps regulate mood, sleep, and appetite."
        },
        {
            "p": "Bananas, pineapples, and walnuts contain this chemical, but eating them does not raise its level in the brain, because it cannot cross the blood-brain barrier. Instead, the brain makes its own supply from an amino acid that can cross that barrier.",
            "r": "That amino acid is tryptophan. For 10 points, name this neurotransmitter linked to mood and sleep."
        },
        {
            "p": "When desert locusts are crowded together, a surge of this chemical in their nervous systems helps switch them from shy, solitary insects into members of a swarm. In mussels, it relaxes “catch” muscles, which can stay tightly contracted for a long time while using little energy.",
            "r": "In people, it helps regulate mood, sleep, and appetite. For 10 points, name this neurotransmitter made from tryptophan."
        },
        {
            "p": "Michael Gershon, who studied this chemical in the gut, wrote the 1998 book _The Second Brain_ about the gut’s own nervous system. Enterochromaffin [“EN-tuh-roh-KROH-muh-fin”] cells in the lining of the intestines make most of the body’s supply of this chemical, which helps trigger the wavelike muscle contractions called peristalsis.",
            "r": "In the brain, it helps regulate mood and sleep. For 10 points, name this neurotransmitter made from the amino acid tryptophan."
        },
        {
            "p": "Scientists have found more than a dozen kinds of receptors for this chemical. All but one kind are G protein–coupled receptors, while the exception is an ion channel that opens when this chemical binds. Neurons that release it in the brain mostly start in the brainstem’s raphe nuclei.",
            "r": "SSRIs such as Prozac block its reuptake. For 10 points, name this neurotransmitter made from tryptophan."
        },
        {
            "p": "The tiny hollow hairs of stinging nettles inject this chemical into the skin along with histamine and acetylcholine, adding to the sting. Its name comes from the blood serum where it was first isolated and from its effect on the “tone” of blood vessels.",
            "r": "The pineal gland uses it to make melatonin. For 10 points, name this neurotransmitter that helps regulate mood, sleep, and appetite."
        },
        {
            "p": "Brainstem neurons that release this chemical fire fastest when an animal is awake, slow down during deep sleep, and fall nearly silent during REM sleep, the stage linked to vivid dreams. Like dopamine and norepinephrine, this chemical is a monoamine.",
            "r": "For 10 points, name this neurotransmitter, made from tryptophan, that the pineal gland turns into melatonin."
        },
        {
            "p": "After a neuron releases this chemical into a synapse, a transporter protein pumps it back into the neuron in a process called reuptake. The amino acid it is made from is often wrongly blamed for making people sleepy after a big turkey dinner.",
            "r": "That amino acid is tryptophan. For 10 points, name this neurotransmitter that helps regulate mood, sleep, and appetite."
        }
    ],
    "clues": [
        {
            "id": "neurotransmitter",
            "tier": "giveaway",
            "t": "A neurotransmitter: a chemical messenger that nerve cells use to signal one another",
            "k": ["neurotransmitter", "chemical messenger"],
            "n": 0,
            "rabbit": "Neurons"
        },
        {
            "id": "tryptophan",
            "tier": "giveaway",
            "t": "Made from the amino acid tryptophan",
            "k": ["tryptophan", "amino acid"],
            "n": 0,
            "rabbit": "Amino acids"
        },
        {
            "id": "mood-sleep",
            "tier": "giveaway",
            "t": "Helps regulate mood, sleep, and appetite",
            "k": ["mood", "sleep", "appetite"],
            "n": 0
        },
        {
            "id": "melatonin",
            "tier": "giveaway",
            "t": "The pineal gland turns it into melatonin, a hormone that helps control sleep",
            "k": ["melatonin", "pineal gland"],
            "n": 0
        },
        {
            "id": "ssri",
            "tier": "giveaway",
            "t": "SSRI antidepressants, such as fluoxetine (sold as Prozac), block its reuptake",
            "k": ["ssri", "prozac", "reuptake", "fluoxetine"],
            "n": 0
        },
        {
            "id": "gut",
            "tier": "middle",
            "t": "Most of the body’s supply is made in the gut, by enterochromaffin cells in the intestinal lining",
            "k": ["enterochromaffin", "intestinal", "gut"],
            "n": 0
        },
        {
            "id": "peristalsis",
            "tier": "middle",
            "t": "In the gut, it helps trigger peristalsis, the wavelike muscle contractions that push food along",
            "k": ["peristalsis", "wavelike"],
            "n": 0
        },
        {
            "id": "platelets",
            "tier": "middle",
            "t": "Platelets soak it up from the blood and release it at wounds, helping blood vessels narrow",
            "k": ["platelets", "wounds"],
            "n": 0,
            "rabbit": "Platelets"
        },
        {
            "id": "raphe",
            "tier": "middle",
            "t": "Most brain neurons that make it sit in clusters in the brainstem called the raphe nuclei",
            "k": ["raphe nuclei", "brainstem"],
            "n": 0
        },
        {
            "id": "reuptake",
            "tier": "middle",
            "t": "After it is released into a synapse, a transporter protein pumps it back into the neuron (reuptake)",
            "k": ["reuptake", "transporter", "synapse"],
            "n": 0
        },
        {
            "id": "monoamine",
            "tier": "middle",
            "t": "A monoamine like dopamine and norepinephrine, but an indoleamine rather than a catecholamine",
            "k": ["monoamine", "indoleamine", "catecholamine"],
            "n": 0,
            "rabbit": "Dopamine"
        },
        {
            "id": "mao",
            "tier": "middle",
            "t": "Broken down by the enzyme monoamine oxidase; some of the earliest antidepressants blocked that enzyme",
            "k": ["monoamine oxidase", "antidepressants"],
            "n": 0
        },
        {
            "id": "blood-brain-barrier",
            "tier": "middle",
            "t": "Cannot cross the blood-brain barrier, so the brain makes its own; bananas, pineapples, and walnuts contain it",
            "k": ["blood-brain barrier", "bananas", "walnuts"],
            "n": 0
        },
        {
            "id": "turkey",
            "tier": "middle",
            "t": "The amino acid it is made from is often wrongly blamed for sleepiness after a turkey dinner",
            "k": ["turkey", "wrongly blamed"],
            "n": 0
        },
        {
            "id": "named-1948",
            "tier": "power",
            "t": "Named in 1948 by Maurice Rapport, Arda Green, and Irvine Page, who isolated it from blood serum; it affects the “tone” of blood vessels",
            "k": ["1948", "serum", "tone", "rapport"],
            "n": 0
        },
        {
            "id": "erspamer",
            "tier": "power",
            "t": "In the 1930s, Vittorio Erspamer found it in gut cells and called it enteramine; the two were shown to be the same in 1952",
            "k": ["erspamer", "enteramine"],
            "n": 0
        },
        {
            "id": "twarog",
            "tier": "power",
            "t": "Betty Twarog, who studied it in mussel muscles, found it in mammal brains in 1953 while working with Irvine Page",
            "k": ["twarog", "1953", "mussel"],
            "n": 0
        },
        {
            "id": "synthesis",
            "tier": "power",
            "t": "Tryptophan hydroxylase adds a hydroxyl group in the slowest step of making it; a second enzyme then removes a carboxyl group",
            "k": ["tryptophan hydroxylase", "hydroxyl", "carboxyl"],
            "n": 0
        },
        {
            "id": "indole",
            "tier": "power",
            "t": "Built around a two-ring indole structure; its molecular formula is C10H12N2O",
            "k": ["indole", "c10h12n2o"],
            "n": 0
        },
        {
            "id": "night-conversion",
            "tier": "power",
            "t": "At night the pineal gland adds an acetyl group and then a methyl group to make melatonin; light slows this",
            "k": ["acetyl", "methyl", "night"],
            "n": 0
        },
        {
            "id": "locusts",
            "tier": "power",
            "t": "A surge of it in crowded desert locusts helps switch them from solitary insects to swarming ones",
            "k": ["locusts", "swarming"],
            "n": 0
        },
        {
            "id": "catch-muscles",
            "tier": "power",
            "t": "Relaxes the “catch” muscles of mussels, which can stay contracted for a long time using little energy",
            "k": ["catch", "mussels"],
            "n": 0
        },
        {
            "id": "second-brain",
            "tier": "power",
            "t": "Michael Gershon, who studied it in the gut, wrote _The Second Brain_ (1998) about the gut’s own nervous system",
            "k": ["gershon", "second brain"],
            "n": 0
        },
        {
            "id": "receptors",
            "tier": "power",
            "t": "Has more than a dozen kinds of receptors; all but one are G protein–coupled, and the exception is an ion channel",
            "k": ["receptors", "ion channel", "g protein"],
            "n": 0
        },
        {
            "id": "nettles",
            "tier": "power",
            "t": "Stinging nettle hairs inject it into the skin along with histamine and acetylcholine",
            "k": ["nettle", "histamine", "acetylcholine"],
            "n": 0
        },
        {
            "id": "rem-sleep",
            "tier": "power",
            "t": "Brainstem neurons that release it fire most when awake, slow down in deep sleep, and nearly stop during REM sleep",
            "k": ["rem sleep", "awake", "deep sleep"],
            "n": 0,
            "rabbit": "Sleep"
        }
    ],
    "trap": {
        "title": "Not its chemical relatives",
        "body": "Several separate answer lines share clues with serotonin. Tryptophan is the amino acid it is made from, and melatonin is the sleep hormone the pineal gland makes from it. Dopamine and norepinephrine are fellow monoamine messengers, but they are catecholamines made from a different amino acid, tyrosine, so naming any of these loses the tossup.",
        "fix": "An indole ring, the raphe nuclei, platelets, the gut, enteramine, or SSRIs such as Prozac all point to serotonin. If the question asks what the pineal gland releases into the blood at night, say melatonin; reward, motivation, and L-dopa point to dopamine.",
        "line": "Real answer line: <b><u>Serotonin</u></b> (accept <u>5-hydroxytryptamine</u> or <u>5-HT</u>; do not accept “melatonin” or “tryptophan”)"
    },
    "tests": {
        "right": [
            "Serotonin",
            "5-HT",
            "5-hydroxytryptamine",
            "Seratonin"
        ],
        "prompt": [
            "monoamine"
        ],
        "wrong": [
            "Melatonin",
            "Dopamine",
            "Tryptophan",
            "SSRI",
            "Norepinephrine",
            "5-HTP"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
