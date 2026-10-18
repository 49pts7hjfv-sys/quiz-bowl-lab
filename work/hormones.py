import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "hormones",
    "name": "Hormones",
    "mono": "HRM",
    "category": "Biology",
    "qbCategory": "Science · Biology",
    "kicker": "Chemical messengers carried by the blood · Signals of the endocrine system",
    "dates": "Named by Ernest Starling in 1905",
    "briefing": "Hormones are chemical messengers: glands release them into the blood, and they travel through the body until they reach cells with the right receptors. Insulin from the pancreas lowers blood sugar, adrenaline from the adrenal glands gets you ready for “fight or flight,” and growth hormone from the pituitary helps you grow. The first one discovered, secretin, was found in 1902, and in 1905 Ernest Starling named the whole group from a Greek word meaning “to set in motion.”",
    "answerHtml": "<b><u>Hormones</u></b> (accept <u>hormone</u>; prompt on <u>chemical messengers</u> or <u>signaling molecules</u>; do not accept “neurotransmitters,” “pheromones,” or the name of a single hormone)",
    "accept": [
        "hormones",
        "hormone",
        "endocrine hormones",
        "phytohormones"
    ],
    "prompt": [
        "chemical messengers",
        "chemical messenger",
        "chemical signals",
        "signaling molecules"
    ],
    "reject": [
        "neurotransmitters",
        "neurotransmitter",
        "pheromones",
        "pheromone",
        "enzymes",
        "enzyme",
        "endocrine system",
        "endocrine glands",
        "endocrine gland",
        "glands",
        "gland",
        "steroids",
        "growth hormone",
        "growth hormones",
        "thyroid hormone",
        "thyroid hormones",
        "parathyroid hormone",
        "antidiuretic hormone",
        "luteinizing hormone",
        "stimulating hormone",
        "releasing hormone",
        "adrenocorticotropic hormone",
        "juvenile hormone",
        "mullerian hormone",
        "insulin",
        "glucagon",
        "epinephrine",
        "adrenaline",
        "cortisol",
        "testosterone",
        "estrogen",
        "thyroxine",
        "melatonin",
        "secretin",
        "auxin",
        "auxins",
        "receptors",
        "cytokines",
        "prostaglandins"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Hormone",
    "qb": {
        "q": "hormones",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "Ernest Starling introduced the name for these substances in a 1905 lecture, borrowing a Greek word meaning “to set in motion.” Three years earlier, Starling and William Bayliss had discovered the first known one, secretin, which tells the pancreas to release its juices.",
            "r": "Insulin and adrenaline are examples. For 10 points, name these chemical messengers that endocrine glands release into the blood."
        },
        {
            "p": "Earl Sutherland won a Nobel Prize for showing that many of these substances do not need to enter their target cells, instead triggering a “second messenger” called cyclic AMP inside them. By contrast, the steroid kind of these substances, made from cholesterol, can slip right through the cell membrane.",
            "r": "For 10 points, name these chemical messengers, such as insulin and estrogen, that glands release into the bloodstream."
        },
        {
            "p": "Roger Guillemin and Andrew Schally shared a Nobel Prize for identifying the “releasing” substances of this kind that the hypothalamus sends to the pituitary through tiny portal blood vessels. The pituitary answers with more of these substances, which control other glands.",
            "r": "For 10 points, name these chemical messengers of the endocrine system, such as cortisol and insulin."
        },
        {
            "p": "Rosalyn Yalow won a Nobel Prize for the radioimmunoassay [“ray-dee-oh-im-yoo-noh-ASS-ay”], a method that measures the tiny amounts of these substances found in a person’s blood. Many of these substances are kept in balance by negative feedback, much like a thermostat turning a furnace on and off.",
            "r": "The field that studies them is endocrinology. For 10 points, name these chemical messengers, such as insulin, made by glands."
        },
        {
            "p": "Charles Darwin and his son Francis showed that grass seedlings bend toward light only if their tips are uncovered, work that led to the discovery of auxin, one of these substances made by plants. Another plant one, ethylene, is a gas that makes fruit ripen.",
            "r": "For 10 points, name these chemical messengers that, in animals, are released into the blood by endocrine glands."
        },
        {
            "p": "Japanese scientists studying a fungus that made rice seedlings grow strangely tall, a disease called “foolish seedling,” discovered gibberellins [“jib-uh-REL-inz”], a group of these substances in plants. In insects, one of these substances called ecdysone [“EK-dih-sohn”] triggers molting.",
            "r": "In humans, these substances include insulin and adrenaline. For 10 points, name these chemical messengers made by glands."
        },
        {
            "p": "One of these substances called calcitonin [“kal-sih-TOH-nin”], made by the thyroid, lowers the amount of calcium in the blood, while another one from the four small parathyroid glands raises it. The thyroid also makes thyroxine, one of these substances that contains iodine.",
            "r": "A lack of iodine can cause a swollen thyroid called a goiter. For 10 points, name these chemical messengers made by endocrine glands."
        },
        {
            "p": "The posterior pituitary stores and releases two of these substances made in the hypothalamus: oxytocin and vasopressin [“vay-zoh-PRESS-in”], which tells the kidneys to save water. The pituitary, nicknamed the “master gland,” also makes several more that control other glands.",
            "r": "For 10 points, name these chemical messengers, which travel through the blood to their target cells."
        },
        {
            "p": "The kidneys make one of these substances, erythropoietin [“ih-RITH-roh-POY-ih-tin”], which tells bone marrow to build more red blood cells when oxygen runs low. The stomach and small intestine make others, such as gastrin, which signals the stomach to release acid.",
            "r": "For 10 points, name these chemical messengers, such as insulin and cortisol, that travel in the blood."
        },
        {
            "p": "When fatty food reaches the small intestine, cells in its lining release one of these substances, cholecystokinin [“koh-luh-sis-toh-KY-nin”], which tells the gallbladder to squeeze out bile. Unlike the digestive juices of exocrine glands, these substances are released straight into the blood, without ducts.",
            "r": "For 10 points, name these chemical messengers made by the endocrine system, such as insulin."
        },
        {
            "p": "Edward Kendall, who isolated thyroxine, shared a 1950 Nobel Prize for work on substances of this kind made by the adrenal cortex, such as cortisone. That outer layer of the adrenal glands also makes cortisol, the main “stress” one of these substances.",
            "r": "For 10 points, name these chemical messengers, such as insulin and adrenaline, that glands release into the blood."
        },
        {
            "p": "The pituitary releases one of these substances, somatotropin [“soh-muh-toh-TROH-pin”], which helps children grow, and much of it comes out during deep sleep. As evening gets dark, the pineal gland releases another of these substances, melatonin, which helps bring on sleep.",
            "r": "For 10 points, name these chemical messengers made by endocrine glands and carried by the blood."
        },
        {
            "p": "Each of these substances affects only target cells that carry a matching receptor, the way a key fits only certain locks. Compared with nerve signals, these substances act more slowly, but their effects usually last longer.",
            "r": "For 10 points, name these chemical messengers, such as insulin, made by the glands of the endocrine system."
        },
        {
            "p": "Oxytocin [“ok-sih-TOH-sin”], one of these substances, is a rare example controlled by positive feedback, since the contractions it causes during childbirth trigger the release of even more of it. Most of these substances are instead controlled by negative feedback, as when rising thyroxine makes the pituitary send out less of the signal that tells the thyroid to work.",
            "r": "Insulin and glucagon are two of them. For 10 points, name these chemical messengers released into the blood by endocrine glands."
        },
        {
            "p": "Angiotensin II [“an-jee-oh-TEN-sin two”], one of these substances, raises blood pressure and also signals the adrenal glands to release another one, aldosterone [“al-DOSS-tuh-rohn”]. Aldosterone tells the kidneys to hold on to sodium, which helps the body keep water.",
            "r": "The adrenal glands also release adrenaline. For 10 points, name these chemical messengers carried by the blood."
        }
    ],
    "clues": [
        {
            "id": "messengers",
            "tier": "giveaway",
            "t": "Chemical messengers that travel through the blood to their target cells",
            "k": ["chemical messengers", "blood", "target cells"],
            "n": 0
        },
        {
            "id": "endocrine-glands",
            "tier": "giveaway",
            "t": "Made by the glands of the endocrine system, such as the pituitary, thyroid, adrenal glands, and pancreas",
            "k": ["endocrine system", "glands", "pituitary"],
            "n": 0,
            "rabbit": "Pituitary gland"
        },
        {
            "id": "examples",
            "tier": "giveaway",
            "t": "Insulin, adrenaline (epinephrine), testosterone, and estrogen are examples",
            "k": ["insulin", "adrenaline", "epinephrine", "estrogen"],
            "n": 0,
            "rabbit": "Epinephrine (adrenaline)"
        },
        {
            "id": "jobs",
            "tier": "giveaway",
            "t": "Control growth, metabolism, blood sugar, sleep, and the body’s response to stress",
            "k": ["growth", "metabolism"],
            "n": 0
        },
        {
            "id": "receptors",
            "tier": "middle",
            "t": "Act only on target cells with a matching receptor, like a key that fits only certain locks",
            "k": ["receptor", "locks"],
            "n": 0
        },
        {
            "id": "slower-than-nerves",
            "tier": "middle",
            "t": "Act more slowly than nerve signals, but their effects usually last longer",
            "k": ["nerve signals", "slowly", "last longer"],
            "n": 0
        },
        {
            "id": "ductless",
            "tier": "middle",
            "t": "Endocrine glands are ductless and release them straight into the blood (exocrine glands use ducts); their study is endocrinology",
            "k": ["ductless", "exocrine", "endocrinology"],
            "n": 0
        },
        {
            "id": "master-gland",
            "tier": "middle",
            "t": "The pituitary, the “master gland,” is run by the hypothalamus and makes several that control other glands",
            "k": ["master gland", "hypothalamus"],
            "n": 0
        },
        {
            "id": "negative-feedback",
            "tier": "middle",
            "t": "Most are kept in balance by negative feedback, like a thermostat controlling a furnace",
            "k": ["negative feedback", "thermostat"],
            "n": 0
        },
        {
            "id": "steroid-protein",
            "tier": "middle",
            "t": "Steroid ones, made from cholesterol, slip through cell membranes; protein ones bind receptors on the cell surface",
            "k": ["steroid", "cholesterol", "cell surface"],
            "n": 0,
            "rabbit": "Cholesterol"
        },
        {
            "id": "insulin-glucagon",
            "tier": "middle",
            "t": "Insulin and glucagon from the pancreas work as a pair to lower and raise blood sugar",
            "k": ["glucagon", "blood sugar", "pancreas"],
            "n": 0,
            "rabbit": "Insulin"
        },
        {
            "id": "thyroxine-iodine",
            "tier": "middle",
            "t": "Thyroxine from the thyroid contains iodine; too little iodine can cause a swollen thyroid called a goiter",
            "k": ["thyroxine", "iodine", "goiter"],
            "n": 0,
            "rabbit": "Thyroid gland"
        },
        {
            "id": "cortisol",
            "tier": "middle",
            "t": "Cortisol, the main “stress” one, comes from the adrenal cortex, the outer layer of the adrenal glands",
            "k": ["cortisol", "adrenal cortex"],
            "n": 0,
            "rabbit": "Adrenal glands"
        },
        {
            "id": "melatonin",
            "tier": "middle",
            "t": "The pineal gland releases melatonin as it gets dark, helping bring on sleep",
            "k": ["melatonin", "pineal"],
            "n": 0,
            "rabbit": "Sleep"
        },
        {
            "id": "starling",
            "tier": "power",
            "t": "Ernest Starling named them in 1905, from a Greek word meaning “to set in motion”",
            "k": ["starling", "1905", "set in motion"],
            "n": 0
        },
        {
            "id": "secretin",
            "tier": "power",
            "t": "Secretin, found by William Bayliss and Ernest Starling in 1902, was the first one discovered",
            "k": ["secretin", "bayliss", "1902"],
            "n": 0
        },
        {
            "id": "sutherland",
            "tier": "power",
            "t": "Earl Sutherland found the “second messenger” cyclic AMP, which carries many of their signals inside a cell",
            "k": ["sutherland", "second messenger", "cyclic amp"],
            "n": 0
        },
        {
            "id": "yalow",
            "tier": "power",
            "t": "Rosalyn Yalow’s radioimmunoassay measures the tiny amounts of them in blood",
            "k": ["yalow", "radioimmunoassay"],
            "n": 0
        },
        {
            "id": "guillemin-schally",
            "tier": "power",
            "t": "Roger Guillemin and Andrew Schally found the hypothalamus’s “releasing” ones, which reach the pituitary through tiny portal vessels",
            "k": ["guillemin", "schally", "releasing", "portal"],
            "n": 0
        },
        {
            "id": "posterior-pituitary",
            "tier": "power",
            "t": "The posterior pituitary releases oxytocin and vasopressin, both made in the hypothalamus; vasopressin tells the kidneys to save water",
            "k": ["posterior pituitary", "vasopressin", "oxytocin"],
            "n": 0
        },
        {
            "id": "calcitonin-pth",
            "tier": "power",
            "t": "Calcitonin from the thyroid lowers blood calcium; PTH from the four parathyroid glands raises it",
            "k": ["calcitonin", "parathyroid", "calcium"],
            "n": 0
        },
        {
            "id": "other-organs",
            "tier": "power",
            "t": "Not just glands: the kidneys make erythropoietin (red blood cells), the stomach makes gastrin (acid), and the intestine makes cholecystokinin (bile)",
            "k": ["erythropoietin", "gastrin", "cholecystokinin"],
            "n": 0
        },
        {
            "id": "kendall",
            "tier": "power",
            "t": "Edward Kendall, who isolated thyroxine, shared a 1950 Nobel Prize for work on cortisone and other adrenal ones",
            "k": ["kendall", "cortisone", "1950"],
            "n": 0
        },
        {
            "id": "somatotropin",
            "tier": "power",
            "t": "The pituitary releases somatotropin, the growth signal, much of it during deep sleep",
            "k": ["somatotropin", "deep sleep"],
            "n": 0
        },
        {
            "id": "oxytocin-positive",
            "tier": "power",
            "t": "Oxytocin during childbirth is a rare example controlled by positive feedback",
            "k": ["positive feedback", "childbirth"],
            "n": 0
        },
        {
            "id": "aldosterone",
            "tier": "power",
            "t": "Angiotensin II raises blood pressure and triggers aldosterone, which tells the kidneys to keep sodium",
            "k": ["angiotensin", "aldosterone", "sodium"],
            "n": 0
        },
        {
            "id": "plant-auxin",
            "tier": "power",
            "t": "Plants make them too: the Darwins’ seedling experiments led to auxin, and ethylene gas ripens fruit",
            "k": ["auxin", "darwins", "ethylene"],
            "n": 0
        },
        {
            "id": "gibberellins-ecdysone",
            "tier": "power",
            "t": "Gibberellins were found by studying rice’s “foolish seedling” disease; in insects, ecdysone triggers molting",
            "k": ["gibberellins", "foolish seedling", "ecdysone"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Messenger mix-ups",
        "body": "Hormones, neurotransmitters, and pheromones are all chemical messengers, so clues about signals can pull players toward the wrong one. Hormones travel through the blood from endocrine glands; neurotransmitters cross the tiny gap between nerve cells; pheromones travel through the air or water to other animals. Many clues also name one example, like insulin or adrenaline, tempting players to answer that single substance instead of the whole group.",
        "fix": "Blood, glands, target cells, the pituitary, or the endocrine system mean hormones. Synapses mean neurotransmitters, and signals between different animals, like an ant’s scent trail, mean pheromones. If the question says “these substances” or “these chemical messengers,” give the group name, not one example.",
        "line": "Real answer line: <b><u>Hormones</u></b> (prompt on <u>chemical messengers</u>; do not accept “neurotransmitters,” “pheromones,” or the name of a single hormone)"
    },
    "tests": {
        "right": [
            "Hormones",
            "hormone",
            "Hormons",
            "Endocrine hormones",
            "Steroid hormones"
        ],
        "prompt": [
            "Chemical messengers",
            "Signaling molecules"
        ],
        "wrong": [
            "Neurotransmitters",
            "Pheromones",
            "Enzymes",
            "Growth hormone",
            "Insulin",
            "Endocrine system"
        ]
    }
}

with open(ROOT / "topics" / "hormones.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("wrote topics/hormones.json")
