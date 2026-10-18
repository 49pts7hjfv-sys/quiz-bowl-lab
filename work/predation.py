import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "predation",
    "name": "Predation",
    "mono": "PRD",
    "category": "Biology",
    "qbCategory": "Science · Biology",
    "kicker": "One organism hunts and eats another · Drives population cycles and arms races",
    "dates": "Modeled by Lotka and Volterra in the 1920s",
    "briefing": "Predation happens whenever one organism kills and eats another, from a cheetah sprinting after a gazelle to a ladybug munching aphids. Predators and prey are locked in an evolutionary race: hunters get faster, sneakier, or better at spotting food, while prey evolve camouflage, poisons, warning colors, and clever mimicry. When predators vanish, prey populations can explode and reshape a whole ecosystem, which is one reason wolves were brought back to Yellowstone in 1995.",
    "answerHtml": "<b><u>Predation</u></b> (accept <u>predators</u>, <u>predator</u>–prey relationships, or <u>predatory</u> behavior; prompt on <u>hunting</u>; do not accept “parasitism” or “competition”)",
    "accept": [
        "predation",
        "predators",
        "predator",
        "predatory",
        "predatory behavior",
        "predator prey",
        "predator prey relationship",
        "predator prey relationships",
        "predator prey interaction",
        "predator prey interactions",
        "predation relationship"
    ],
    "prompt": [
        "hunting",
        "carnivory",
        "carnivores",
        "carnivore"
    ],
    "reject": [
        "parasitism",
        "parasite",
        "parasites",
        "mutualism",
        "commensalism",
        "symbiosis",
        "competition",
        "herbivory",
        "herbivores",
        "camouflage",
        "mimicry",
        "food chain",
        "food chains",
        "food web"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Predation",
    "qb": {
        "q": "predation",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "G. F. Gause watched the single-celled _Didinium_ [“dye-DIN-ee-um”] devour every _Paramecium_ [“pair-uh-MEE-see-um”] in a test tube and then starve, showing how unstable this interaction can be when victims have no place to hide. Alfred Lotka and Vito Volterra wrote paired equations to model this interaction.",
            "r": "For 10 points, name this interaction in which one organism kills and eats another, its prey."
        },
        {
            "p": "C. S. Holling modeled this interaction by having a blindfolded person tap a tabletop to find sandpaper discs, which led to his “disc equation.” Holling’s three types of “functional response” describe how an animal’s eating rate changes as its food becomes more common.",
            "r": "A lion chasing a zebra is an example of this interaction. For 10 points, name this relationship in which one animal kills and eats another."
        },
        {
            "p": "Since 1958, scientists have tracked wolves and moose on Isle Royale [“ROY-ul”], an island in Lake Superior, in the longest-running study of this interaction. In that study, the two animals’ populations have risen and fallen in response to each other.",
            "r": "For 10 points, name this ecological interaction in which wolves hunt, kill, and eat moose."
        },
        {
            "p": "Fur-trapping records from the Hudson’s Bay Company show Canada lynx and snowshoe hare populations rising and falling in cycles about ten years long, a classic example of this interaction. In those cycles, lynx numbers peak shortly after hare numbers do.",
            "r": "For 10 points, name this interaction between a hunter and the animal it kills and eats."
        },
        {
            "p": "Robert Paine pried _Pisaster_ [“pye-ZAS-ter”] sea stars off rocks on the Washington coast and found that mussels took over, so he called the sea star a “keystone species.” Sea otters protect kelp forests in a similar way through this interaction, by eating sea urchins.",
            "r": "For 10 points, name this interaction in which one organism, like a sea star or an otter, kills and eats another."
        },
        {
            "p": "After wolves returned to Yellowstone National Park in 1995, scientists studied how fear of these animals changed where elk grazed, a possible “trophic cascade.” Orcas are called “apex” examples of these animals, since no other wild animals hunt adult orcas.",
            "r": "For 10 points, name these animals, such as lions and wolves, that hunt and kill other animals for food."
        },
        {
            "p": "Thomson’s gazelles leap high on stiff legs, a behavior called stotting, possibly to show a chasing cheetah that they are too fit to catch. Animals that are often hunted tend to have eyes on the sides of their heads, while hunters tend to have forward-facing eyes for judging distance.",
            "r": "For 10 points, name this interaction in which an animal like a cheetah kills and eats its prey."
        },
        {
            "p": "Periodical cicadas emerge by the billions every 13 or 17 years, overwhelming birds and other hungry animals with a defense against this interaction called “satiation.” Some scientists think those prime-numbered cycles help the cicadas avoid enemies with shorter life cycles.",
            "r": "For 10 points, name this interaction, seen when a frog snaps up and eats a fly."
        },
        {
            "p": "Henry Walter Bates studied Amazon butterflies and described a kind of mimicry in which a harmless species copies the warning colors of a dangerous one, fooling animals that would otherwise eat it. Hoverflies striped like wasps use that defense against this interaction.",
            "r": "For 10 points, name this interaction in which one animal hunts, kills, and eats another, its prey."
        },
        {
            "p": "In Müllerian [“myoo-LEER-ee-un”] mimicry, two harmful species share the same warning pattern, so the animals that might eat them learn to avoid both. Bright warning colors, like those of poison dart frogs, are called aposematism [“ap-uh-SEE-muh-tiz-um”], another defense against this interaction.",
            "r": "Camouflage is a defense against it, too. For 10 points, name this interaction in which one organism kills and eats another."
        },
        {
            "p": "Female _Photuris_ [“foh-TOOR-is”] fireflies copy the flash signals of other firefly species to lure in males, which they then eat, an example of “aggressive mimicry” used in this interaction. Deep-sea anglerfish dangle glowing lures in front of their mouths for the same purpose.",
            "r": "For 10 points, name this interaction in which one organism, the hunter, catches and eats its prey."
        },
        {
            "p": "Garter snakes in the Pacific Northwest have evolved resistance to tetrodotoxin [“teh-TROH-duh-tox-in”], the poison in the rough-skinned newts they eat, while the newts have evolved even more toxin, an evolutionary “arms race” driven by this interaction.",
            "r": "An owl catching a mouse is another example. For 10 points, name this interaction in which one animal kills and eats another."
        },
        {
            "p": "In 1888 and 1889, vedalia [“vuh-DAY-lee-uh”] beetles from Australia were brought to California, where they saved citrus groves by eating cottony cushion scale insects, an early success of biological control based on this interaction. Gardeners release other ladybugs to eat aphids in the same way.",
            "r": "For 10 points, name this ecological interaction in which one organism kills and eats another, called its prey."
        },
        {
            "p": "Alfred, Lord Tennyson’s poem _In Memoriam A.H.H._ describes nature as “red in tooth and claw,” a phrase often used for this interaction. In science classes, students learn about this interaction by pulling apart owl pellets to find the tiny bones of animals the owls swallowed.",
            "r": "A hawk catching a mouse is another example. For 10 points, name this relationship between a hunting animal and its prey."
        },
        {
            "p": "In this interaction, energy moves up a food chain when one consumer eats another, and the animals that do the eating are usually less common than the animals they eat. Many animals avoid this interaction by using camouflage to blend into their surroundings.",
            "r": "For 10 points, name this interaction, in which a lion might kill and eat a zebra."
        }
    ],
    "clues": [
        {
            "id": "definition",
            "tier": "giveaway",
            "t": "An interaction in which one organism hunts, kills, and eats another, its prey",
            "k": ["prey", "kills", "eats"],
            "n": 0
        },
        {
            "id": "examples",
            "tier": "giveaway",
            "t": "Classic examples: lions and zebras, owls and mice, wolves and elk",
            "k": ["lions", "owls", "wolves"],
            "n": 0
        },
        {
            "id": "food-chain",
            "tier": "giveaway",
            "t": "Moves energy up food chains when one consumer eats another",
            "k": ["food chains", "consumer", "energy"],
            "n": 0,
            "rabbit": "Food chains"
        },
        {
            "id": "apex",
            "tier": "giveaway",
            "t": "“Apex” hunters at the top of a food chain, like adult orcas, have no natural enemies",
            "k": ["apex", "orcas", "natural enemies"],
            "n": 0
        },
        {
            "id": "eyes",
            "tier": "giveaway",
            "t": "Hunters tend to have forward-facing eyes; hunted animals often have eyes on the sides of the head",
            "k": ["forward-facing", "sides"],
            "n": 0
        },
        {
            "id": "lynx-hare",
            "tier": "middle",
            "t": "Canada lynx and snowshoe hare numbers rise and fall in roughly 10-year cycles (Hudson’s Bay Company records)",
            "k": ["lynx", "snowshoe hare", "hudson’s bay"],
            "n": 0
        },
        {
            "id": "lotka-volterra",
            "tier": "middle",
            "t": "Alfred Lotka and Vito Volterra wrote paired equations to model it",
            "k": ["lotka", "volterra", "equations"],
            "n": 0
        },
        {
            "id": "camouflage",
            "tier": "middle",
            "t": "Prey defenses include camouflage and bright warning colors (aposematism), as on poison dart frogs",
            "k": ["camouflage", "aposematism", "poison dart frogs"],
            "n": 0
        },
        {
            "id": "batesian",
            "tier": "middle",
            "t": "Batesian mimicry (from Henry Walter Bates’s study of Amazon butterflies): a harmless species copies a dangerous one, like a wasp-striped hoverfly",
            "k": ["batesian", "amazon butterflies", "hoverfly"],
            "n": 0
        },
        {
            "id": "mullerian",
            "tier": "middle",
            "t": "Müllerian mimicry: two harmful species share the same warning pattern",
            "k": ["müllerian", "warning pattern"],
            "n": 0
        },
        {
            "id": "keystone",
            "tier": "middle",
            "t": "Robert Paine removed _Pisaster_ sea stars, mussels took over, and he coined “keystone species”",
            "k": ["paine", "pisaster", "keystone species", "mussels"],
            "n": 0
        },
        {
            "id": "yellowstone",
            "tier": "middle",
            "t": "Wolves were brought back to Yellowstone in 1995, changing how elk behaved",
            "k": ["yellowstone", "1995", "elk"],
            "n": 0
        },
        {
            "id": "owl-pellets",
            "tier": "middle",
            "t": "Students pull apart owl pellets, coughed-up bundles of bones and fur, to see what owls ate",
            "k": ["owl pellets", "bones", "fur"],
            "n": 0
        },
        {
            "id": "gause",
            "tier": "power",
            "t": "G. F. Gause’s _Didinium_ ate every _Paramecium_ in a tube and then starved, unless the prey had places to hide",
            "k": ["gause", "didinium", "paramecium"],
            "n": 0
        },
        {
            "id": "holling",
            "tier": "power",
            "t": "C. S. Holling’s “disc equation” came from a blindfolded person finding sandpaper discs; he described three types of functional response",
            "k": ["holling", "disc equation", "functional response", "sandpaper"],
            "n": 0
        },
        {
            "id": "isle-royale",
            "tier": "power",
            "t": "Wolves and moose on Isle Royale in Lake Superior have been studied since 1958, the longest such study",
            "k": ["isle royale", "moose", "1958"],
            "n": 0
        },
        {
            "id": "sea-otters",
            "tier": "power",
            "t": "Sea otters eat sea urchins, keeping urchins from destroying kelp forests",
            "k": ["sea otters", "sea urchins", "kelp"],
            "n": 0
        },
        {
            "id": "trophic-cascade",
            "tier": "power",
            "t": "Effects of a top hunter that ripple down through a food web are called a trophic cascade",
            "k": ["trophic cascade", "ripple"],
            "n": 0
        },
        {
            "id": "cicadas",
            "tier": "power",
            "t": "Periodical cicadas swamp birds by emerging by the billions every 13 or 17 years, a defense called satiation",
            "k": ["cicadas", "satiation", "17 years"],
            "n": 0
        },
        {
            "id": "stotting",
            "tier": "power",
            "t": "Gazelles leap stiff-legged (stotting), possibly to show a cheetah they are too fit to catch",
            "k": ["stotting", "gazelles", "cheetah"],
            "n": 0
        },
        {
            "id": "photuris",
            "tier": "power",
            "t": "Female _Photuris_ fireflies fake other species’ flashes to lure and eat males (aggressive mimicry)",
            "k": ["photuris", "fireflies", "aggressive mimicry"],
            "n": 0
        },
        {
            "id": "anglerfish",
            "tier": "power",
            "t": "Deep-sea anglerfish dangle glowing lures in front of their mouths",
            "k": ["anglerfish", "glowing lures"],
            "n": 0
        },
        {
            "id": "newts",
            "tier": "power",
            "t": "Garter snakes evolved resistance to the tetrodotoxin of rough-skinned newts, an evolutionary arms race",
            "k": ["garter snakes", "rough-skinned newts", "tetrodotoxin", "arms race"],
            "n": 0
        },
        {
            "id": "vedalia",
            "tier": "power",
            "t": "Vedalia beetles brought from Australia to California in 1888–89 ate scale insects that were ruining citrus (biological control)",
            "k": ["vedalia", "biological control", "citrus"],
            "n": 0
        },
        {
            "id": "tennyson",
            "tier": "power",
            "t": "Tennyson’s _In Memoriam A.H.H._ calls nature “red in tooth and claw”",
            "k": ["tennyson", "red in tooth and claw", "in memoriam"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Predation or parasitism?",
        "body": "Both interactions help one organism at another’s expense, so players mix them up. A predator kills and eats its prey, usually all at once, while a parasite, like a tick or a tapeworm, lives on or inside its host and usually does not kill it right away. Herbivory (eating plants) and competition (fighting over the same resources) are separate interactions too.",
        "fix": "Ask whether the eater kills its victim and moves on (predation) or stays attached for a long time (parasitism). If both species lose by sharing food or space, it is competition; if both benefit, it is mutualism.",
        "line": "Real answer line: <b><u>Predation</u></b> (accept <u>predators</u> or <u>predator</u>–prey relationships; do not accept “parasitism”)"
    },
    "tests": {
        "right": [
            "Predation",
            "predators",
            "Predator-prey relationship",
            "Predatoin",
            "predator"
        ],
        "prompt": [
            "Hunting",
            "Carnivory"
        ],
        "wrong": [
            "Prey",
            "Parasitism",
            "Mutualism",
            "Competition",
            "Commensalism"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
