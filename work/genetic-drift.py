import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "genetic-drift",
    "name": "Genetic drift",
    "mono": "GD",
    "category": "Biology",
    "qbCategory": "Science · Biology",
    "kicker": "Random shifts in a population’s alleles · Evolution by luck, not fitness",
    "dates": "Happens in every population, but most in small ones",
    "briefing": "Genetic drift is evolution by pure luck. In every generation, chance decides which individuals happen to pass on their genes, so some alleles (gene versions) become more common and others disappear, whether they help or not. It hits small populations hardest: after a typhoon in the late 1700s left about 20 survivors on the Pacific atoll of Pingelap, a rare kind of total color blindness became common there.",
    "answerHtml": "<b><u>Genetic drift</u></b> (accept <u>allelic drift</u> or <u>Sewall Wright effect</u>; prompt on <u>drift</u> or <u>evolution</u>; do not accept “natural selection,” “gene flow,” “founder effect,” or “bottleneck effect”)",
    "accept": [
        "genetic drift",
        "random genetic drift",
        "random drift",
        "allelic drift",
        "allele drift",
        "gene drift",
        "sewall wright effect"
    ],
    "prompt": [
        "drift",
        "evolution",
        "microevolution"
    ],
    "reject": [
        "natural selection",
        "selection",
        "sexual selection",
        "artificial selection",
        "gene flow",
        "migration",
        "founder effect",
        "founders effect",
        "founder principle",
        "bottleneck effect",
        "bottleneck",
        "genetic bottleneck",
        "population bottleneck",
        "mutation",
        "mutations",
        "continental drift",
        "antigenic drift",
        "antigenic shift",
        "genetic shift",
        "hardy weinberg",
        "hardy weinberg equilibrium",
        "hardy weinberg principle",
        "inbreeding",
        "speciation",
        "genetic variation",
        "neutral theory"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Genetic_drift",
    "qb": {
        "q": "genetic drift",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "In 1956, Peter Buri tracked an eye-color allele through more than 100 small populations of fruit flies, and over the generations many of those populations lost one version of the gene entirely. When this process pushes an allele’s frequency all the way to 100 percent, that allele is said to be fixed.",
            "r": "For 10 points, name this mechanism of evolution in which allele frequencies change by random chance, especially in small populations."
        },
        {
            "p": "Oliver Sacks visited Pingelap for his book _The Island of the Colorblind_. On that Pacific atoll, a typhoon in the late 1700s left only about 20 survivors, and because one survivor carried a rare allele, a form of total color blindness called achromatopsia [“ay-kroh-muh-TOP-see-uh”] later became common.",
            "r": "That disaster created a population bottleneck. For 10 points, name this random change in allele frequencies that is strongest in small populations."
        },
        {
            "p": "Motoo Kimura’s neutral theory, proposed in 1968, says that most DNA changes that become fixed in a species got there through this process rather than through natural selection. Under that theory, much of the variety in DNA neither helps nor hurts survival.",
            "r": "This process can wipe out an allele purely by luck. For 10 points, name this random change in allele frequencies, strongest in small populations."
        },
        {
            "p": "The Wright-Fisher model describes this process mathematically by treating each new generation as a random sample of the alleles in the one before it. In that model, every allele eventually ends up either fixed or lost unless new mutations appear.",
            "r": "Mutation, gene flow, and natural selection are the other main mechanisms of evolution besides this one. For 10 points, name this process in which chance changes allele frequencies."
        },
        {
            "p": "After their numbers crashed, greater prairie chickens in Illinois lost many alleles and had fewer eggs hatch, until birds brought in from other states restored some of the lost variety. Biologists call a sudden population crash like that one a bottleneck.",
            "r": "For 10 points, name this mechanism of evolution, strongest in small populations, in which allele frequencies change by luck rather than by natural selection."
        },
        {
            "p": "Ellis–van Creveld syndrome, a rare inherited condition that causes short limbs and extra fingers, is unusually common among the Old Order Amish of Lancaster County, Pennsylvania, whose community grew from a small number of families. Ernst Mayr named the general idea behind cases like that one the “founder principle.”",
            "r": "For 10 points, name this mechanism of evolution, which includes the founder effect, in which allele frequencies change by chance."
        },
        {
            "p": "The strength of this process depends on a number called the effective population size, which is often much smaller than a population’s actual head count. Because of this process, a new allele that neither helps nor hurts has a chance of spreading to the whole population equal to its starting frequency.",
            "r": "It can make an allele disappear by luck alone. For 10 points, name this random change in allele frequencies that matters most in small populations."
        },
        {
            "p": "Cheetahs have remarkably little genetic variation, probably because their numbers crashed near the end of the last ice age, letting this process erase many of their alleles. In a crash like that, the survivors carry only a random sample of the original population’s alleles.",
            "r": "Hardy-Weinberg equilibrium assumes a population too large for this process to matter. For 10 points, name this mechanism of evolution in which chance changes allele frequencies."
        },
        {
            "p": "American geneticist Sewall Wright argued that this process could help small, partly isolated groups cross from one peak to another on his “adaptive landscape,” as part of his “shifting balance” theory. One alternate name for this process honors Wright.",
            "r": "It works like sampling error in each new generation. For 10 points, name this random change in allele frequencies, strongest in small populations."
        },
        {
            "p": "When a few birds blown to a remote island start a new population, they may carry only a small, unusual sample of the mainland population’s alleles, an example of the founder effect. A disaster that suddenly kills most of a population can have a similar result, called the bottleneck effect.",
            "r": "For 10 points, name this mechanism of evolution in which allele frequencies change randomly from one generation to the next."
        },
        {
            "p": "Without new mutations or migrants, this process steadily lowers a population’s heterozygosity [“het-er-oh-zye-GOSS-ih-tee”], the share of individuals carrying two different alleles of a gene. Because its effects are unpredictable, two isolated groups that start out alike will slowly grow apart genetically.",
            "r": "Unlike natural selection, it does not favor helpful alleles. For 10 points, name this mechanism of evolution in which allele frequencies change by chance."
        },
        {
            "p": "Northern elephant seals were hunted almost to extinction by the 1890s, and although their numbers have bounced back, their DNA still shows very little variety. Because so few seals survived, this process had erased much of their genetic variation.",
            "r": "That crash is called a bottleneck. For 10 points, name this mechanism of evolution in which allele frequencies change by random chance."
        },
        {
            "p": "In a model of this process named for Patrick Moran, at each step one randomly chosen individual reproduces and one randomly chosen individual dies. That model lets generations overlap instead of replacing one another all at once.",
            "r": "This process includes the founder effect. For 10 points, name this random change in allele frequencies that is strongest in small populations."
        },
        {
            "p": "Tomoko Ohta’s “nearly neutral” theory argues that slightly harmful mutations can still spread by this process when selection against them is very weak. Hardy-Weinberg equilibrium can hold only if a population is so large that this process can be ignored.",
            "r": "For 10 points, name this mechanism of evolution in which allele frequencies change by luck, not fitness."
        },
        {
            "p": "Ronald Fisher argued that this process mattered much less than natural selection in large populations, a view that kept him arguing with Sewall Wright for decades. The founder effect and the bottleneck effect are two special cases of this process.",
            "r": "For 10 points, name this mechanism of evolution in which allele frequencies change randomly from one generation to the next."
        }
    ],
    "clues": [
        {
            "id": "random-change",
            "tier": "giveaway",
            "t": "Random change in how common alleles (versions of a gene) are in a population from one generation to the next",
            "k": ["random", "alleles", "generation"],
            "n": 0
        },
        {
            "id": "small-populations",
            "tier": "giveaway",
            "t": "Strongest in small populations, where luck has the biggest effect",
            "k": ["small populations", "luck"],
            "n": 0
        },
        {
            "id": "not-selection",
            "tier": "giveaway",
            "t": "Unlike natural selection, it does not favor helpful traits: evolution by chance, not fitness",
            "k": ["natural selection", "chance", "fitness"],
            "n": 0,
            "rabbit": "Natural selection"
        },
        {
            "id": "four-mechanisms",
            "tier": "giveaway",
            "t": "One of the four main mechanisms of evolution, along with natural selection, mutation, and gene flow",
            "k": ["mechanisms", "gene flow", "mutation"],
            "n": 0,
            "rabbit": "Evolution"
        },
        {
            "id": "founder-effect",
            "tier": "middle",
            "t": "Founder effect: a few individuals start a new population, carrying only a small sample of the old population’s alleles",
            "k": ["founder effect", "founder"],
            "n": 0
        },
        {
            "id": "bottleneck-effect",
            "tier": "middle",
            "t": "Bottleneck effect: a disaster or hunting crashes a population, and the few survivors carry a random sample of its alleles",
            "k": ["bottleneck", "survivors"],
            "n": 0
        },
        {
            "id": "fixed-or-lost",
            "tier": "middle",
            "t": "Can make an allele vanish (lost) or become the only version left, at 100 percent (fixed)",
            "k": ["fixed", "lost", "100 percent"],
            "n": 0
        },
        {
            "id": "less-variation",
            "tier": "middle",
            "t": "Lowers genetic variation over time, so populations hit hard by it end up genetically alike",
            "k": ["genetic variation", "variation"],
            "n": 0
        },
        {
            "id": "hardy-weinberg",
            "tier": "middle",
            "t": "Hardy-Weinberg equilibrium assumes a population so large that this effect can be ignored",
            "k": ["hardy-weinberg", "equilibrium"],
            "n": 0
        },
        {
            "id": "sampling-error",
            "tier": "middle",
            "t": "A kind of sampling error: like a coin flipped only a few times, a small sample can stray far from 50-50",
            "k": ["sampling error", "coin"],
            "n": 0
        },
        {
            "id": "grow-apart",
            "tier": "middle",
            "t": "Makes isolated populations slowly grow apart genetically, even when no selection is acting",
            "k": ["isolated", "grow apart"],
            "n": 0
        },
        {
            "id": "sewall-wright",
            "tier": "power",
            "t": "American geneticist Sewall Wright stressed its importance in his “shifting balance” theory and “adaptive landscape”; one alternate name honors him",
            "k": ["sewall wright", "shifting balance", "adaptive landscape"],
            "n": 0
        },
        {
            "id": "fisher",
            "tier": "power",
            "t": "Ronald Fisher thought it mattered far less than natural selection, a long-running argument with Sewall Wright",
            "k": ["ronald fisher", "fisher"],
            "n": 0
        },
        {
            "id": "models",
            "tier": "power",
            "t": "Described by the Wright-Fisher model (each generation is a random sample of the last) and the Moran model (generations overlap)",
            "k": ["wright-fisher", "moran"],
            "n": 0
        },
        {
            "id": "kimura-ohta",
            "tier": "power",
            "t": "Motoo Kimura’s neutral theory (1968): most DNA changes that become fixed spread by chance; Tomoko Ohta added the “nearly neutral” theory",
            "k": ["kimura", "neutral theory", "ohta"],
            "n": 0
        },
        {
            "id": "pingelap",
            "tier": "power",
            "t": "Pingelap: a typhoon in the late 1700s left about 20 survivors, and total color blindness (achromatopsia) became common; Oliver Sacks wrote about it in _The Island of the Colorblind_",
            "k": ["pingelap", "achromatopsia", "oliver sacks"],
            "n": 0
        },
        {
            "id": "buri",
            "tier": "power",
            "t": "Peter Buri (1956) tracked an eye-color allele in over 100 small fruit fly populations; many ended up fixed or lost",
            "k": ["buri", "fruit fly", "1956"],
            "n": 0,
            "rabbit": "Fruit flies"
        },
        {
            "id": "effective-size",
            "tier": "power",
            "t": "Its strength depends on the effective population size, which is often much smaller than the actual head count",
            "k": ["effective population size", "head count"],
            "n": 0
        },
        {
            "id": "fixation-chance",
            "tier": "power",
            "t": "A new allele that neither helps nor hurts has a chance of spreading to everyone equal to its starting frequency",
            "k": ["starting frequency", "neither helps nor hurts"],
            "n": 0
        },
        {
            "id": "heterozygosity",
            "tier": "power",
            "t": "Without new mutations or migrants, it steadily lowers heterozygosity, the share of individuals with two different alleles of a gene",
            "k": ["heterozygosity", "migrants"],
            "n": 0
        },
        {
            "id": "mayr",
            "tier": "power",
            "t": "Ernst Mayr named the “founder principle,” the idea behind the founder effect",
            "k": ["ernst mayr", "mayr", "founder principle"],
            "n": 0
        },
        {
            "id": "amish",
            "tier": "power",
            "t": "Founder effect: Ellis-van Creveld syndrome (short limbs, extra fingers) is unusually common among the Old Order Amish of Lancaster County, Pennsylvania",
            "k": ["amish", "lancaster", "extra fingers"],
            "n": 0
        },
        {
            "id": "prairie-chickens",
            "tier": "power",
            "t": "Greater prairie chickens in Illinois lost alleles after a population crash; birds brought from other states helped more eggs hatch",
            "k": ["prairie chickens", "illinois"],
            "n": 0
        },
        {
            "id": "cheetahs-seals",
            "tier": "power",
            "t": "Bottleneck examples: cheetahs (a crash near the end of the last ice age) and northern elephant seals (hunted almost to extinction by the 1890s)",
            "k": ["cheetahs", "elephant seals", "ice age"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Chance or fitness?",
        "body": "Genetic drift is one of the four main mechanisms of evolution, and tossups about it often mention the others, especially natural selection, so players blurt the wrong one. Drift changes allele frequencies by luck, while natural selection changes them because some traits help survival. The founder effect and the bottleneck effect are special cases of drift, but naming just one of them on a general question is wrong.",
        "fix": "Chance, luck, sampling error, small or isolated populations, founders, disaster survivors, Sewall Wright, or Kimura’s neutral theory mean genetic drift. Adaptation, “survival of the fittest,” or peppered moths mean natural selection, and migration between populations means gene flow. Don’t mix it up with antigenic drift (flu viruses) or continental drift (geology).",
        "line": "Real answer line: <b><u>Genetic drift</u></b> (accept <u>allelic drift</u> or <u>Sewall Wright effect</u>; prompt on <u>drift</u>; do not accept “natural selection,” “gene flow,” “founder effect,” or “bottleneck effect”)"
    },
    "tests": {
        "right": [
            "Genetic drift",
            "genetic drfit",
            "Allelic drift",
            "Random genetic drift",
            "Sewall Wright effect"
        ],
        "prompt": [
            "Drift",
            "Evolution"
        ],
        "wrong": [
            "Natural selection",
            "Gene flow",
            "Founder effect",
            "Bottleneck effect",
            "Continental drift",
            "Antigenic drift"
        ]
    }
}

with open(ROOT / "topics" / "genetic-drift.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("wrote topics/genetic-drift.json")
