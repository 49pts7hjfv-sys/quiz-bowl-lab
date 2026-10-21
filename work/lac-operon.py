import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "lac-operon",
    "name": "Lac operon",
    "mono": "LAC",
    "category": "Biology",
    "qbCategory": "Science · Biology",
    "kicker": "E. coli genes for digesting lactose · The classic case of gene control",
    "dates": "Model published 1961",
    "briefing": "The lac operon is a set of three genes that lets the gut bacterium E. coli digest lactose, the sugar in milk. Most of the time a repressor protein sits on the DNA and keeps the genes switched off, but when lactose shows up, it pulls the repressor away and the genes turn on. François Jacob and Jacques Monod figured this out in 1961 and won a Nobel Prize, giving biologists their first clear picture of how genes are switched on and off.",
    "answerHtml": "<b><u>Lac operon</u></b> (accept <u>lactose operon</u>; prompt on <u>operon</u>; do not accept “trp operon”)",
    "accept": [
        "lac operon",
        "lac operons",
        "lactose operon",
        "lactose operons"
    ],
    "prompt": [
        "operon",
        "operons",
        "lac"
    ],
    "reject": [
        "trp operon",
        "tryptophan operon",
        "trp",
        "ara operon",
        "arabinose operon",
        "gal operon",
        "lac repressor",
        "repressor",
        "repressors",
        "operator",
        "lac operator",
        "promoter",
        "lac promoter",
        "lactase",
        "beta galactosidase",
        "galactosidase",
        "permease",
        "lacz",
        "laci",
        "e coli",
        "escherichia coli",
        "transcription",
        "gene expression",
        "plasmid",
        "plasmids",
        "cap",
        "camp",
        "catabolite activator protein"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Lac_operon",
    "qb": {
        "q": "lac operon",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "A French biologist’s doctoral research found that E. coli fed a mix of two sugars grows in two separate spurts, a pattern he called diauxie [“dy-AWK-see”], because the bacteria use up the glucose before switching on this set of genes. The two spurts are separated by a pause while the bacteria build new enzymes.",
            "r": "That biologist, Jacques Monod, later explained these genes with François Jacob. For 10 points, name this set of E. coli genes that is switched on by lactose."
        },
        {
            "p": "In the 1959 “PaJaMo” experiment, named for its three scientists, bacterial mating showed that one gene in this system makes a substance that can travel through the cell and shut the other genes off. Arthur Pardee supplied the “Pa” in that experiment’s name.",
            "r": "The other syllables stand for François Jacob and Jacques Monod. For 10 points, name this set of E. coli genes for digesting lactose."
        },
        {
            "p": "In 1966, Walter Gilbert and Benno Müller-Hill became the first scientists to isolate a repressor protein, the one that controls this set of genes. That repressor is built from four identical units and can bend DNA into a loop by gripping two operator sites at once.",
            "r": "Lactose removes that repressor and switches these genes on. For 10 points, name this set of E. coli genes studied by Jacob and Monod."
        },
        {
            "p": "In blue-white screening, scientists insert new DNA into the middle of a gene from this system, so bacterial colonies that carry the new DNA stay white on dishes containing X-gal instead of turning blue. Lab workers often switch these genes on with IPTG, a look-alike of the natural trigger that bacteria cannot break down.",
            "r": "Its Z gene makes beta-galactosidase. For 10 points, name this set of E. coli genes that is switched on by lactose."
        },
        {
            "p": "The three main genes of this system, labeled Z, Y, and A, code for beta-galactosidase [“BAY-tuh guh-lak-TOH-sih-dayss”], a permease that carries sugar into the cell, and a transacetylase [“trans-uh-SEE-tuh-layss”]. Beta-galactosidase splits a sugar into glucose and galactose.",
            "r": "That sugar is lactose. For 10 points, name this set of E. coli genes explained by François Jacob and Jacques Monod."
        },
        {
            "p": "The true trigger for this system is allolactose [“al-oh-LAK-tohss”], a rearranged form of a sugar, which binds the repressor and changes its shape so that it lets go of the DNA. Because binding a small molecule changes its shape, that repressor is called an allosteric protein.",
            "r": "That form comes from lactose. For 10 points, name this set of E. coli genes studied by Jacob and Monod."
        },
        {
            "p": "“Constitutive” mutants of this system make its enzymes all the time, even without the sugar that normally switches it on. Bacteria carrying two copies of these genes showed that the operator controls only the genes on its own stretch of DNA, while the repressor can act from anywhere in the cell.",
            "r": "Jacob and Monod explained these genes. For 10 points, name this set of E. coli genes that is switched on by lactose."
        },
        {
            "p": "When glucose is plentiful, levels of cyclic AMP drop, so the catabolite activator protein, or CAP, cannot attach near this system’s promoter and boost it, an effect called catabolite repression. As a result, these genes work hardest only when glucose is absent.",
            "r": "They also need lactose to be present. For 10 points, name this set of E. coli genes studied by Jacob and Monod."
        },
        {
            "p": "One of the two scientists who explained this system wrote the 1970 book _Chance and Necessity_, and the other wrote _The Logic of Life_. Both men fought against Nazi Germany in World War II, one in the French Resistance and the other with the Free French forces.",
            "r": "Those scientists were Jacques Monod and François Jacob. For 10 points, name this set of E. coli genes for digesting lactose."
        },
        {
            "p": "This system’s three structural genes are copied together into a single messenger RNA that carries the instructions for three different proteins, a kind of message called polycistronic [“pol-ee-sis-TROH-nik”]. A single promoter and a single operator control all three of those genes.",
            "r": "Lactose switches them on. For 10 points, name this classic example of gene regulation in E. coli."
        },
        {
            "p": "Charles Yanofsky [“yuh-NOFF-skee”] studied a contrasting set of E. coli genes that is switched off when tryptophan is plentiful. Unlike that “repressible” set, this set of genes is “inducible,” staying off until its food molecule appears.",
            "r": "That food molecule is lactose. For 10 points, name this set of genes explained by Jacob and Monod."
        },
        {
            "p": "The two scientists who explained this system shared the 1965 Nobel Prize in Physiology or Medicine with André Lwoff, who had studied viruses that hide inside bacteria. Their 1961 model of this system also predicted a short-lived “messenger” molecule that carries genetic instructions to ribosomes.",
            "r": "That molecule is messenger RNA. For 10 points, name this set of E. coli genes that is switched on by lactose."
        },
        {
            "p": "Glucose keeps this system quiet partly through “inducer exclusion,” in which taking in glucose blocks the permease that would carry another sugar into the cell. Glucose also lowers cyclic AMP, so the activator protein CAP cannot help switch this system on.",
            "r": "This system’s inducer comes from lactose. For 10 points, name this set of E. coli genes studied by Jacob and Monod."
        },
        {
            "p": "In 2000, Michael Elowitz and Stanislas Leibler built the “repressilator,” a genetic clock in which three repressors switch each other off in turn; one of those repressors came from this system. Biotech companies often use parts of this system to switch on genes for medicines made in bacteria.",
            "r": "Normally, its repressor sits on the operator. For 10 points, name this set of E. coli genes that is switched on by lactose."
        },
        {
            "p": "A typical E. coli cell holds only about 10 to 20 copies of this system’s repressor, yet that tiny amount keeps its genes almost completely off until the right sugar arrives. The repressor is made by a gene labeled I, which sits just before this system’s promoter.",
            "r": "That sugar is lactose. For 10 points, name this set of genes explained by Jacob and Monod."
        }
    ],
    "clues": [
        {
            "id": "ecoli-genes",
            "tier": "giveaway",
            "t": "A cluster of genes that lets the bacterium E. coli use lactose, the sugar in milk",
            "k": ["e. coli", "lactose", "milk"],
            "n": 0,
            "rabbit": "E. coli"
        },
        {
            "id": "jacob-monod",
            "tier": "giveaway",
            "t": "Explained by François Jacob and Jacques Monod, who published their model in 1961",
            "k": ["jacob", "monod", "1961"],
            "n": 0
        },
        {
            "id": "lactose-inducer",
            "tier": "giveaway",
            "t": "Switched on when lactose is present: lactose acts as the inducer",
            "k": ["switched on", "inducer"],
            "n": 0
        },
        {
            "id": "classic-regulation",
            "tier": "giveaway",
            "t": "The classic example of gene regulation: several genes switched on and off together as one unit",
            "k": ["gene regulation", "one unit"],
            "n": 0
        },
        {
            "id": "repressor-operator",
            "tier": "middle",
            "t": "When lactose is absent, a repressor protein binds a stretch of DNA called the operator and shuts the genes off",
            "k": ["repressor", "operator"],
            "n": 0
        },
        {
            "id": "rna-polymerase",
            "tier": "middle",
            "t": "The bound repressor keeps RNA polymerase, which attaches at the promoter, from transcribing the genes",
            "k": ["rna polymerase", "promoter"],
            "n": 0,
            "rabbit": "Transcription"
        },
        {
            "id": "nobel-1965",
            "tier": "middle",
            "t": "Jacob and Monod shared the 1965 Nobel Prize in Physiology or Medicine with André Lwoff",
            "k": ["1965", "lwoff", "nobel prize"],
            "n": 0,
            "rabbit": "Bacteriophages"
        },
        {
            "id": "beta-gal",
            "tier": "middle",
            "t": "Its Z gene makes beta-galactosidase, which splits lactose into glucose and galactose",
            "k": ["beta-galactosidase", "galactose", "z gene"],
            "n": 0,
            "rabbit": "Glucose"
        },
        {
            "id": "zya",
            "tier": "middle",
            "t": "Its three structural genes are Z (beta-galactosidase), Y (a permease), and A (a transacetylase)",
            "k": ["permease", "transacetylase", "structural genes"],
            "n": 0
        },
        {
            "id": "inducible",
            "tier": "middle",
            "t": "It is inducible (normally off), unlike the repressible trp genes, which tryptophan switches off",
            "k": ["inducible", "repressible", "tryptophan"],
            "n": 0
        },
        {
            "id": "cap-camp",
            "tier": "middle",
            "t": "When glucose is low, cyclic AMP binds CAP, which boosts the genes; plenty of glucose keeps them low (catabolite repression)",
            "k": ["cyclic amp", "catabolite repression", "cap"],
            "n": 0
        },
        {
            "id": "polycistronic",
            "tier": "middle",
            "t": "Its genes are copied together into one polycistronic messenger RNA that codes for several proteins",
            "k": ["polycistronic", "messenger rna"],
            "n": 0
        },
        {
            "id": "pasteur",
            "tier": "middle",
            "t": "Jacob and Monod did this work at the Pasteur Institute in Paris",
            "k": ["pasteur institute", "paris"],
            "n": 0
        },
        {
            "id": "diauxie",
            "tier": "power",
            "t": "Monod’s doctoral work found diauxie: E. coli fed two sugars grows in two spurts, using up the glucose first",
            "k": ["diauxie", "two spurts"],
            "n": 0
        },
        {
            "id": "pajamo",
            "tier": "power",
            "t": "The 1959 PaJaMo experiment (Pardee, Jacob, Monod) showed that the repressor gene’s product can act anywhere in the cell",
            "k": ["pajamo", "pardee", "1959"],
            "n": 0
        },
        {
            "id": "gilbert",
            "tier": "power",
            "t": "Walter Gilbert and Benno Müller-Hill first isolated its repressor in 1966; the repressor has four units and can loop DNA",
            "k": ["gilbert", "müller-hill", "1966", "loop"],
            "n": 0
        },
        {
            "id": "blue-white",
            "tier": "power",
            "t": "Blue-white screening: putting new DNA into its Z gene keeps colonies white instead of blue on X-gal",
            "k": ["blue-white screening", "x-gal"],
            "n": 0
        },
        {
            "id": "iptg",
            "tier": "power",
            "t": "IPTG is a lab look-alike of its inducer that bacteria cannot break down",
            "k": ["iptg", "look-alike"],
            "n": 0
        },
        {
            "id": "allolactose",
            "tier": "power",
            "t": "The true inducer is allolactose, which changes the repressor’s shape, so the repressor is an allosteric protein",
            "k": ["allolactose", "allosteric"],
            "n": 0
        },
        {
            "id": "constitutive",
            "tier": "power",
            "t": "Constitutive mutants make its enzymes all the time; the operator works only on its own DNA, but the repressor works from anywhere",
            "k": ["constitutive", "own dna", "anywhere"],
            "n": 0
        },
        {
            "id": "chance-necessity",
            "tier": "power",
            "t": "Monod wrote _Chance and Necessity_ (1970) and Jacob wrote _The Logic of Life_; both fought Nazi Germany in World War II",
            "k": ["chance and necessity", "logic of life", "world war ii"],
            "n": 0
        },
        {
            "id": "mrna-prediction",
            "tier": "power",
            "t": "Jacob and Monod’s 1961 model predicted a short-lived messenger molecule: messenger RNA",
            "k": ["short-lived", "predicted"],
            "n": 0,
            "rabbit": "RNA"
        },
        {
            "id": "yanofsky",
            "tier": "power",
            "t": "Charles Yanofsky studied the contrasting trp genes, which are switched off when tryptophan is plentiful",
            "k": ["yanofsky", "trp genes"],
            "n": 0
        },
        {
            "id": "inducer-exclusion",
            "tier": "power",
            "t": "Glucose also blocks the permease that would bring lactose in, an effect called inducer exclusion",
            "k": ["inducer exclusion", "permease"],
            "n": 0
        },
        {
            "id": "repressilator",
            "tier": "power",
            "t": "Its repressor is one of the three in the “repressilator,” a genetic clock built by Michael Elowitz and Stanislas Leibler in 2000",
            "k": ["repressilator", "elowitz", "2000"],
            "n": 0
        },
        {
            "id": "few-copies",
            "tier": "power",
            "t": "An E. coli cell holds only about 10 to 20 copies of its repressor, which is made by the I gene just before the promoter",
            "k": ["10 to 20", "i gene"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Lac, not trp",
        "body": "Bacteria have more than one famous operon. The trp operon makes the amino acid tryptophan and is repressible: it is normally on and gets switched off when tryptophan piles up. The lac operon is inducible: it is normally off and gets switched on when lactose shows up. Players also mix up the lac operon with lactase, the enzyme people use to digest milk sugar.",
        "fix": "Lactose, allolactose, beta-galactosidase, IPTG, X-gal, CAP, or Jacob and Monod mean the lac operon; tryptophan, attenuation, and Charles Yanofsky mean the trp operon. Saying just “operon” earns a prompt, so be ready to add “lac.”",
        "line": "Real answer line: <b><u>Lac operon</u></b> (accept <u>lactose operon</u>; prompt on <u>operon</u>; do not accept “trp operon”)"
    },
    "tests": {
        "right": [
            "Lac operon",
            "lactose operon",
            "the lac operon",
            "lac opron",
            "Lac operons"
        ],
        "prompt": [
            "operon",
            "Lac"
        ],
        "wrong": [
            "trp operon",
            "Lac repressor",
            "Lactase",
            "E. coli",
            "Operator",
            "Promoter",
            "Beta-galactosidase"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
