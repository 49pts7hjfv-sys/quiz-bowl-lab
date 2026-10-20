import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "honey-bees",
    "name": "Honey bees",
    "mono": "BEE",
    "category": "Biology",
    "qbCategory": "Science · Biology",
    "kicker": "Honey-making social insects · Famous for their waggle dance",
    "dates": "Kept by people since ancient Egypt",
    "briefing": "A honey bee colony can hold tens of thousands of insects: one egg-laying queen, thousands of female workers, and hundreds of male drones. A worker who finds flowers tells her sisters where they are with a “waggle dance,” a code cracked by Karl von Frisch, who shared the 1973 Nobel Prize. The western honey bee, _Apis mellifera_, pollinates crops around the world, which is why scientists keep a close eye on threats like Varroa mites and colony collapse disorder.",
    "answerHtml": "<b><u>Honey bees</u></b> (accept <u>honeybees</u>, <u>Apis</u>, or <u>Apis mellifera</u>; prompt on <u>bees</u>; do not accept “bumblebees,” “wasps,” or “hornets”)",
    "accept": [
        "honey bees",
        "honey bee",
        "honeybees",
        "honeybee",
        "apis",
        "apis mellifera",
        "western honey bee",
        "western honey bees",
        "european honey bee",
        "european honey bees"
    ],
    "prompt": [
        "bees",
        "bee",
        "worker bees",
        "worker bee"
    ],
    "reject": [
        "bumblebees",
        "bumblebee",
        "bumble bees",
        "bumble bee",
        "bombus",
        "wasps",
        "wasp",
        "hornets",
        "hornet",
        "yellow jackets",
        "yellowjackets",
        "carpenter bees",
        "carpenter bee",
        "mason bees",
        "mason bee",
        "sweat bees",
        "stingless bees",
        "ants",
        "termites",
        "flies",
        "hoverflies",
        "butterflies"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Honey_bee",
    "qb": {
        "q": "honey bee",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "Karl von Frisch shared the 1973 Nobel Prize in Physiology or Medicine for decoding how foragers of this species share the location of food. He found that the angle of a forager’s straight “waggle run” on the vertical comb, measured from straight up, matches the angle between the food and the sun.",
            "r": "If food is very close, a forager does a round dance instead. For 10 points, name these insects that make honey."
        },
        {
            "p": "In 1852, the minister Lorenzo Langstroth patented a wooden hive with removable hanging frames, after noticing that these insects leave a gap of less than a centimeter open instead of filling it with comb. People who keep these insects puff smoke at them to keep them calm.",
            "r": "Their colonies have a queen, thousands of female workers, and male drones. For 10 points, name these insects that store honey in wax combs."
        },
        {
            "p": "In 1956, geneticist Warwick Kerr brought queens of an African subspecies of these insects to Brazil, and the next year some of their swarms escaped and began interbreeding with European members of the species. Their “Africanized” descendants, known for defending their nests in huge, aggressive groups, spread north and reached Texas in 1990.",
            "r": "Their workers carry pollen home in “baskets” on their hind legs. For 10 points, name these insects that store honey in six-sided wax cells."
        },
        {
            "p": "Starting in late 2006, commercial keepers of these insects in the United States reported hives where most of the adult workers had suddenly vanished, leaving behind the queen, the young, and stored food. Scientists have studied mites, viruses, pesticides, and poor nutrition as possible causes.",
            "r": "That problem is called colony collapse disorder. For 10 points, name these pollinating insects that make honey."
        },
        {
            "p": "The bacterium _Paenibacillus larvae_ causes American foulbrood, a deadly disease of these insects’ young. A mite that jumped to these insects from a related Asian species feeds on their young and adults and spreads deformed wing virus through their colonies.",
            "r": "That mite is _Varroa destructor_. For 10 points, name these insects whose colonies have one queen, thousands of female workers, and stores of honey."
        },
        {
            "p": "Workers of this species raise their abdomens and fan their wings to spread a scent from the Nasonov gland, guiding nestmates home. A worker spends her first weeks cleaning cells, feeding young, and building comb before she becomes a guard and then a forager.",
            "r": "A worker usually dies after stinging a person, because its barbed stinger stays in the skin. For 10 points, name these insects whose workers make honey and wax."
        },
        {
            "p": "Thomas Hales proved in 1999 that the shape these insects use for their storage cells divides a flat surface into equal areas with the least total wall length. These insects make wax for those cells in glands on the undersides of their abdomens, and they seal cracks with propolis, a sticky substance made from plant resins.",
            "r": "Their combs are made of six-sided wax cells. For 10 points, name these insects that store honey in those combs."
        },
        {
            "p": "Nurse workers of this species make a protein-rich food in glands in their heads, and a female larva fed only that food inside a large, peanut-shaped cell grows into a queen instead of a worker. Ordinary worker larvae get that food only for their first few days.",
            "r": "That food is called royal jelly. For 10 points, name these social insects that make honey in hives."
        },
        {
            "p": "Thomas Seeley studied how scouts of this species dance on a hanging cluster to “debate” possible new homes, such as hollow tree trunks, until enough scouts agree on one site. That cluster forms when an old queen leaves a crowded hive with a large share of its workers.",
            "r": "That way of starting a new colony is called swarming. For 10 points, name these insects that make honey."
        },
        {
            "p": "Aristotle called the largest member of this insect’s colony its “king,” but Jan Swammerdam’s dissections in the 1600s showed that this leader is female. That leader’s queen mandibular pheromone keeps workers from raising new queens or laying eggs of their own.",
            "r": "A queen can lay more than a thousand eggs in a single day. For 10 points, name these honey-making insects whose colonies also include workers and drones."
        },
        {
            "p": "Under this insect’s haplodiploid [“HAP-loh-DIP-loyd”] system, males develop from unfertilized eggs, so each male has a mother but no father, and counting a male’s ancestors generation by generation gives the Fibonacci sequence. Those males have no stingers, and workers push them out of the hive before winter.",
            "r": "Their females are the queen and the workers. For 10 points, name these honey-making insects whose males are called drones."
        },
        {
            "p": "Members of an Asian species in this insect’s genus defend their nests against giant hornets by packing around an intruder in a ball and heating it with their vibrating flight muscles until it dies. In winter, colonies of the western species huddle in a cluster and shiver to stay warm instead of hibernating.",
            "r": "For 10 points, name these insects that survive the winter by eating the honey they stored during the summer."
        },
        {
            "p": "Karl von Frisch trained these insects to find sugar water on a blue card placed among gray cards of many shades, proving that they can see color. They can see ultraviolet light but not red, and they find their way using patterns of polarized light in the sky.",
            "r": "Their foragers use a waggle dance to tell nestmates where food is. For 10 points, name these insects that make honey."
        },
        {
            "p": "Foragers of this species carry nectar home in a stomach-like crop, and workers add the enzyme invertase to split its sucrose into glucose and fructose, then fan their wings to evaporate most of the water. When one of these insects stings, it releases an alarm scent that smells like bananas.",
            "r": "Their colonies are made of a queen, female workers, and male drones. For 10 points, name these insects that make honey."
        },
        {
            "p": "Thomas Jefferson wrote that Native Americans called this insect the “white man’s fly,” because it spread west a little ahead of European settlers after colonists brought it from Europe. Each February, a large share of the colonies of this insect kept in the United States are trucked to California to pollinate almond orchards.",
            "r": "Their colonies have a single egg-laying queen. For 10 points, name these insects that live in hives and make honey."
        }
    ],
    "clues": [
        {
            "id": "nectar-combs",
            "tier": "giveaway",
            "t": "Social insects that turn flower nectar into a thick, sweet food and store it in wax combs",
            "k": ["nectar", "wax combs"],
            "n": 0
        },
        {
            "id": "castes",
            "tier": "giveaway",
            "t": "Each colony has one egg-laying queen (more than a thousand eggs a day), thousands of female workers, and male drones",
            "k": ["queen", "workers", "drones"],
            "n": 0
        },
        {
            "id": "hexagonal-cells",
            "tier": "giveaway",
            "t": "Build combs of six-sided (hexagonal) cells out of wax made by the workers",
            "k": ["hexagonal", "six-sided", "wax"],
            "n": 0
        },
        {
            "id": "pollinators",
            "tier": "giveaway",
            "t": "Important crop pollinators; workers carry pollen home in “baskets” on their hind legs",
            "k": ["pollinators", "baskets", "hind legs"],
            "n": 0,
            "rabbit": "Pollen"
        },
        {
            "id": "barbed-stinger",
            "tier": "giveaway",
            "t": "A worker’s barbed stinger usually stays stuck in a person’s skin, so the worker dies after stinging",
            "k": ["barbed stinger", "dies"],
            "n": 0
        },
        {
            "id": "waggle-dance",
            "tier": "middle",
            "t": "Foragers do a waggle dance to show nestmates the direction and distance to food; a round dance means food is close by",
            "k": ["waggle dance", "round dance", "direction"],
            "n": 0
        },
        {
            "id": "royal-jelly",
            "tier": "middle",
            "t": "A larva fed only royal jelly, made in glands in nurse workers’ heads, grows into a queen",
            "k": ["royal jelly", "nurse"],
            "n": 0
        },
        {
            "id": "swarming",
            "tier": "middle",
            "t": "Colonies reproduce by swarming: an old queen leaves the hive with a large share of the workers",
            "k": ["swarming"],
            "n": 0
        },
        {
            "id": "colony-collapse",
            "tier": "middle",
            "t": "Colony collapse disorder, reported from late 2006: adult workers vanish, leaving the queen, young, and food behind",
            "k": ["colony collapse disorder", "2006", "vanish"],
            "n": 0
        },
        {
            "id": "varroa",
            "tier": "middle",
            "t": "Threats include the mite _Varroa destructor_, which spreads deformed wing virus, and American foulbrood, a bacterial disease of their young",
            "k": ["varroa", "deformed wing virus", "american foulbrood"],
            "n": 0
        },
        {
            "id": "winter-cluster",
            "tier": "middle",
            "t": "They don’t hibernate: in winter they huddle in a cluster, shiver to stay warm, and live on stored food",
            "k": ["hibernate", "cluster", "shiver"],
            "n": 0
        },
        {
            "id": "vision",
            "tier": "middle",
            "t": "They see ultraviolet light but not red, and they find their way using patterns of polarized light in the sky",
            "k": ["ultraviolet", "polarized"],
            "n": 0
        },
        {
            "id": "mellifera",
            "tier": "middle",
            "t": "Carl Linnaeus named the western species, the one kept around the world, _mellifera_ (“honey-bearing”) in 1758",
            "k": ["mellifera", "linnaeus", "1758"],
            "n": 0
        },
        {
            "id": "von-frisch",
            "tier": "power",
            "t": "Karl von Frisch decoded their dances and proved they see color; he shared the 1973 Nobel Prize with Konrad Lorenz and Nikolaas Tinbergen",
            "k": ["von frisch", "1973", "lorenz", "tinbergen"],
            "n": 0
        },
        {
            "id": "africanized",
            "tier": "power",
            "t": "“Africanized” strains come from African queens Warwick Kerr brought to Brazil; swarms escaped in 1957 and reached Texas in 1990",
            "k": ["africanized", "warwick kerr", "brazil", "texas"],
            "n": 0
        },
        {
            "id": "langstroth",
            "tier": "power",
            "t": "Lorenzo Langstroth patented the hive with removable frames in 1852, after noticing they leave a narrow gap open between combs",
            "k": ["langstroth", "1852", "removable frames"],
            "n": 0
        },
        {
            "id": "hales",
            "tier": "power",
            "t": "Thomas Hales proved the honeycomb conjecture in 1999: six-sided cells split a surface into equal areas with the least wall",
            "k": ["hales", "honeycomb conjecture", "1999"],
            "n": 0
        },
        {
            "id": "propolis",
            "tier": "power",
            "t": "Workers make wax in glands under the abdomen and seal cracks with propolis, a sticky “glue” made from plant resins",
            "k": ["propolis", "resins", "glands"],
            "n": 0
        },
        {
            "id": "invertase",
            "tier": "power",
            "t": "Workers add the enzyme invertase to nectar, splitting sucrose into glucose and fructose, then fan their wings to dry it",
            "k": ["invertase", "sucrose"],
            "n": 0,
            "rabbit": "Enzymes"
        },
        {
            "id": "nasonov",
            "tier": "power",
            "t": "Workers fan their wings to spread a scent from the Nasonov gland at the tip of the abdomen, guiding nestmates home",
            "k": ["nasonov"],
            "n": 0,
            "rabbit": "Pheromones"
        },
        {
            "id": "alarm-scent",
            "tier": "power",
            "t": "Their alarm scent, released with a sting, contains isoamyl acetate, which smells like bananas; keepers use smoke to mask it",
            "k": ["isoamyl acetate", "bananas", "smoke"],
            "n": 0,
            "rabbit": "Esters"
        },
        {
            "id": "swammerdam",
            "tier": "power",
            "t": "Aristotle called the colony’s leader a “king,” but Jan Swammerdam’s dissections in the 1600s showed it is female",
            "k": ["swammerdam", "aristotle", "king"],
            "n": 0
        },
        {
            "id": "queen-pheromone",
            "tier": "power",
            "t": "Queen mandibular pheromone holds the colony together and keeps workers from raising new queens or laying eggs",
            "k": ["queen mandibular pheromone", "mandibular"],
            "n": 0
        },
        {
            "id": "haplodiploidy",
            "tier": "power",
            "t": "Haplodiploidy: males come from unfertilized eggs, so a male’s family tree follows the Fibonacci sequence",
            "k": ["haplodiploidy", "unfertilized", "fibonacci"],
            "n": 0,
            "rabbit": "Fibonacci sequence"
        },
        {
            "id": "hornet-ball",
            "tier": "power",
            "t": "An Asian species in their genus kills invading giant hornets by surrounding each one in a ball and heating it with flight muscles",
            "k": ["giant hornets", "ball"],
            "n": 0
        },
        {
            "id": "seeley",
            "tier": "power",
            "t": "Thomas Seeley showed how swarm scouts dance to “debate” new nest sites until enough of them agree (a quorum)",
            "k": ["seeley", "scouts", "quorum"],
            "n": 0
        },
        {
            "id": "white-mans-fly",
            "tier": "power",
            "t": "Not native to the Americas; Thomas Jefferson wrote that Native Americans called them the “white man’s fly”",
            "k": ["white man’s fly", "jefferson"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Honey bees, not bumblebees",
        "body": "Bumblebees are also fuzzy, striped, social insects that pollinate flowers, so an early buzz on “these pollinators” can go wrong. Saying just “bees” earns only a prompt, and naming bumblebees, wasps, or hornets is wrong. Bumblebees live in small colonies that usually last a single summer, and their workers can sting more than once.",
        "fix": "The waggle dance, royal jelly, propolis, Langstroth hives, Varroa mites, colony collapse disorder, and “Africanized” strains all mean honey bees. Buzz pollination of tomatoes and blueberries and the genus _Bombus_ mean bumblebees. If you hear only “bees,” answer “honey bees” in full.",
        "line": "Real answer line: <b><u>Honey bees</u></b> (accept <u>Apis mellifera</u>; prompt on <u>bees</u>; do not accept “bumblebees” or “wasps”)"
    },
    "tests": {
        "right": [
            "Honey bees",
            "honeybee",
            "Apis mellifera",
            "hony bees",
            "Western honey bee"
        ],
        "prompt": [
            "Bees"
        ],
        "wrong": [
            "Bumblebees",
            "Wasps",
            "Hornets",
            "Carpenter bees",
            "Honey"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
