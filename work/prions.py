import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "prions",
    "name": "Prions",
    "mono": "PRN",
    "category": "Biology",
    "qbCategory": "Science · Biology",
    "kicker": "Misfolded proteins that spread · Cause mad cow disease and kuru",
    "dates": "Named in 1982",
    "briefing": "Prions are the strangest infectious agents known: they have no DNA or RNA at all, just a protein folded into the wrong shape. When a prion meets a normal copy of the same protein, it makes that copy misfold too, and the slow chain reaction damages the brain, leaving tiny holes that make it look like a sponge. Prions cause mad cow disease in cattle, scrapie in sheep, and Creutzfeldt-Jakob disease in people.",
    "answerHtml": "<b><u>Prions</u></b> (accept <u>prion</u> or <u>prion proteins</u>; prompt on <u>proteins</u> or <u>misfolded proteins</u>; do not accept “viruses” or “viroids”)",
    "accept": [
        "prions",
        "prion",
        "prion protein",
        "prion proteins",
        "prp",
        "prpsc",
        "prp sc"
    ],
    "prompt": [
        "proteins",
        "protein",
        "misfolded proteins",
        "misfolded protein",
        "infectious proteins",
        "infectious protein",
        "infectious agents",
        "infectious agent",
        "pathogens",
        "pathogen",
        "proteinaceous infectious particle",
        "proteinaceous infectious particles"
    ],
    "reject": [
        "viruses",
        "virus",
        "viroids",
        "viroid",
        "bacteria",
        "pions",
        "pion",
        "orion",
        "prison",
        "prisons",
        "prusiner",
        "stanley prusiner",
        "mad cow disease",
        "mad cow",
        "bse",
        "scrapie",
        "kuru",
        "cjd",
        "creutzfeldt jakob disease",
        "amyloid",
        "amyloids",
        "chaperones"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Prion",
    "qb": {
        "q": "prions",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "In the 1960s, Tikvah Alper found that the agent of scrapie survived doses of radiation strong enough to destroy DNA or RNA, a hint that these agents carry no genes at all. The abnormal shape of these agents is rich in flat, folded beta sheets.",
            "r": "They are misfolded proteins, and Stanley Prusiner won a Nobel Prize for discovering them. For 10 points, name these agents that cause mad cow disease."
        },
        {
            "p": "The human gene for the normal form of the protein in these agents sits on chromosome 20, and inherited changes in that gene can cause fatal familial insomnia. Stanley Prusiner’s “protein-only hypothesis” said that these agents need no genes to spread.",
            "r": "They spread by forcing normal copies of a protein to misfold. For 10 points, name these infectious agents that cause mad cow disease."
        },
        {
            "p": "D. Carleton Gajdusek [“GUY-duh-shek”] shared the 1976 Nobel Prize for showing that kuru, a disease of the Fore [“FOR-ay”] people of Papua New Guinea, could be passed to chimpanzees. Kuru, whose name means “trembling,” spread through traditional funeral customs and is now known to be caused by these agents.",
            "r": "They also cause scrapie in sheep. For 10 points, name these misfolded proteins behind mad cow disease."
        },
        {
            "p": "Chronic wasting disease, which affects deer, elk, and moose in North America, is caused by these agents. In sheep and goats, these agents cause scrapie, a disease named for the way sick animals rub and scrape themselves against fences.",
            "r": "For 10 points, name these infectious misfolded proteins that also cause mad cow disease in cattle."
        },
        {
            "p": "Some yeast cells carry harmless versions of these agents that pass traits on to their daughter cells without any change to their DNA. One of those yeast versions is formed by a protein called Sup35.",
            "r": "Like the disease-causing kind, they copy themselves by making normal proteins misfold. For 10 points, name these agents, which cause mad cow disease in cattle."
        },
        {
            "p": "In 1982, Stanley Prusiner coined the name of these agents by shortening the phrase “proteinaceous infectious particle,” and in 1997 he won the Nobel Prize in medicine for discovering them. Many scientists at first doubted his claim that these agents spread disease without any genes.",
            "r": "Unlike viruses, they contain no DNA or RNA. For 10 points, name these misfolded proteins that cause mad cow disease."
        },
        {
            "p": "In 1996, British scientists linked a new form of Creutzfeldt-Jakob [“KROITS-felt YAH-kohb”] disease in young people to eating beef from cattle sick with an illness caused by these agents. That cattle illness had spread when cows were fed meal made from the remains of infected animals.",
            "r": "These agents are proteins folded into the wrong shape. For 10 points, name these infectious agents that cause mad cow disease."
        },
        {
            "p": "These agents are rich in flat beta sheets, which let them stack into long fibers called amyloid [“AM-uh-loyd”] that clump together in brain tissue. The normal version of their protein sits on the outer surface of nerve cells and is folded mostly into spiral alpha helices.",
            "r": "For 10 points, name these misfolded proteins, which have no DNA or RNA, that cause diseases such as mad cow disease."
        },
        {
            "p": "Hospitals use extra-strong cleaning, such as long, very hot steam treatments or harsh chemicals, on surgical tools that might carry these agents, because ordinary sterilizing does not reliably destroy them. Cooking meat does not destroy these agents either.",
            "r": "For 10 points, name these misfolded proteins that cause mad cow disease and contain no genes."
        },
        {
            "p": "Diseases caused by these agents are called transmissible spongiform encephalopathies [“en-SEF-uh-LOP-uh-theez”], because they leave tiny holes that make brain tissue look like a sponge under a microscope. Those diseases can take years or even decades to show symptoms after infection.",
            "r": "They are misfolded proteins with no DNA or RNA. For 10 points, name these agents that cause mad cow disease."
        },
        {
            "p": "The abnormal form of the protein in these agents partly resists being cut apart by the enzyme proteinase K, which completely digests the normal form, even though both forms have the same sequence of amino acids. Researchers use that resistance to detect these agents in brain samples.",
            "r": "One of these agents acts as a template that makes normal copies of its protein refold into its own abnormal shape. For 10 points, name these agents that cause mad cow disease."
        },
        {
            "p": "Viroids [“VYE-roydz”] are infectious agents made of nothing but a small loop of RNA, and they infect plants such as potatoes. These agents are even simpler, with no RNA or DNA at all, and antibiotics and antiviral drugs do not work against them.",
            "r": "These misfolded proteins cause scrapie in sheep. For 10 points, name these agents that cause mad cow disease."
        },
        {
            "p": "The misfolded form of the protein in these agents is labeled with the letters “Sc,” short for scrapie, while the healthy form is labeled with a “C,” for cellular. Scrapie, a disease of sheep and goats caused by these agents, has been known in Europe for centuries.",
            "r": "Stanley Prusiner named these agents in 1982. For 10 points, name these misfolded proteins that also cause mad cow disease."
        },
        {
            "p": "The most common human disease caused by these agents, Creutzfeldt-Jakob disease, usually appears for no known reason in older adults, while a smaller share of cases run in families. Kuru, a disease once found among the Fore people of Papua New Guinea, is caused by these agents as well.",
            "r": "They are proteins folded into the wrong shape. For 10 points, name these agents behind mad cow disease."
        },
        {
            "p": "In 1988, Britain banned feeding cattle meal made from the remains of sheep and cattle, trying to stop an epidemic caused by these agents. That epidemic peaked in the early 1990s, and in 1996 the European Union banned exports of British beef.",
            "r": "For 10 points, name these misfolded proteins that cause bovine spongiform encephalopathy, better known as mad cow disease."
        }
    ],
    "clues": [
        {
            "id": "misfolded-protein",
            "tier": "giveaway",
            "t": "Infectious agents made only of a misfolded protein",
            "k": ["misfolded", "infectious agents"],
            "n": 0,
            "rabbit": "Proteins"
        },
        {
            "id": "mad-cow",
            "tier": "giveaway",
            "t": "Cause mad cow disease, or bovine spongiform encephalopathy (BSE), in cattle",
            "k": ["mad cow", "bse", "cattle"],
            "n": 0
        },
        {
            "id": "no-dna",
            "tier": "giveaway",
            "t": "Have no DNA or RNA, unlike viruses and bacteria",
            "k": ["no dna", "viruses", "bacteria"],
            "n": 0,
            "rabbit": "Viruses"
        },
        {
            "id": "prusiner",
            "tier": "giveaway",
            "t": "Named by Stanley Prusiner, who won the 1997 Nobel Prize in medicine for discovering them",
            "k": ["prusiner", "1997", "nobel"],
            "n": 0
        },
        {
            "id": "spread-misfolding",
            "tier": "giveaway",
            "t": "Spread by forcing normal copies of the same protein to misfold",
            "k": ["normal copies", "misfold"],
            "n": 0
        },
        {
            "id": "scrapie",
            "tier": "middle",
            "t": "Cause scrapie in sheep and goats, named for how sick animals scrape against fences",
            "k": ["scrapie", "sheep", "fences"],
            "n": 0
        },
        {
            "id": "cjd",
            "tier": "middle",
            "t": "Cause Creutzfeldt-Jakob disease (CJD) in humans",
            "k": ["creutzfeldt-jakob", "cjd"],
            "n": 0
        },
        {
            "id": "kuru",
            "tier": "middle",
            "t": "Cause kuru, a “trembling” disease of the Fore people of Papua New Guinea, spread by funeral customs",
            "k": ["kuru", "fore", "papua new guinea"],
            "n": 0
        },
        {
            "id": "chronic-wasting",
            "tier": "middle",
            "t": "Cause chronic wasting disease in deer, elk, and moose",
            "k": ["chronic wasting", "deer", "elk"],
            "n": 0
        },
        {
            "id": "spongiform",
            "tier": "middle",
            "t": "Their diseases, transmissible spongiform encephalopathies, leave sponge-like holes in brain tissue",
            "k": ["spongiform", "encephalopathies", "sponge"],
            "n": 0
        },
        {
            "id": "name-origin",
            "tier": "middle",
            "t": "The name is short for “proteinaceous infectious particle,” coined in 1982",
            "k": ["proteinaceous", "infectious particle", "1982"],
            "n": 0
        },
        {
            "id": "variant-cjd",
            "tier": "middle",
            "t": "In 1996, a new variant of CJD in young people was linked to eating beef from cattle with mad cow disease",
            "k": ["variant", "1996", "beef"],
            "n": 0
        },
        {
            "id": "cattle-feed",
            "tier": "middle",
            "t": "Mad cow disease spread through cattle feed made from the remains of infected animals",
            "k": ["cattle feed", "remains"],
            "n": 0
        },
        {
            "id": "hard-to-destroy",
            "tier": "middle",
            "t": "Survive cooking and ordinary sterilization, so hospitals use extra-strong cleaning on tools",
            "k": ["cooking", "sterilization"],
            "n": 0
        },
        {
            "id": "long-incubation",
            "tier": "middle",
            "t": "Their diseases can take years or even decades to show symptoms",
            "k": ["decades", "years"],
            "n": 0
        },
        {
            "id": "beta-sheets",
            "tier": "power",
            "t": "The normal protein sits on the surface of nerve cells and is mostly alpha helices; the misfolded form is rich in beta sheets",
            "k": ["beta sheets", "alpha helices", "nerve cells"],
            "n": 0
        },
        {
            "id": "amyloid",
            "tier": "power",
            "t": "Misfolded copies stack into long fibers called amyloid that clump in brain tissue",
            "k": ["amyloid", "fibers"],
            "n": 0
        },
        {
            "id": "alper",
            "tier": "power",
            "t": "In the 1960s, Tikvah Alper showed the scrapie agent survives radiation strong enough to destroy DNA and RNA",
            "k": ["alper", "radiation"],
            "n": 0
        },
        {
            "id": "gajdusek",
            "tier": "power",
            "t": "D. Carleton Gajdusek shared the 1976 Nobel Prize for showing kuru could be passed to chimpanzees",
            "k": ["gajdusek", "1976", "chimpanzees"],
            "n": 0
        },
        {
            "id": "protein-only",
            "tier": "power",
            "t": "The “protein-only hypothesis” says they need no genes to spread",
            "k": ["protein-only", "hypothesis"],
            "n": 0
        },
        {
            "id": "chromosome-20",
            "tier": "power",
            "t": "The human gene for the normal protein is on chromosome 20; inherited changes can cause fatal familial insomnia",
            "k": ["chromosome 20", "fatal familial insomnia"],
            "n": 0
        },
        {
            "id": "sc-label",
            "tier": "power",
            "t": "The misfolded form is labeled “Sc” for scrapie, known for centuries; the normal form is labeled “C” for cellular",
            "k": ["cellular", "labeled", "centuries"],
            "n": 0
        },
        {
            "id": "yeast",
            "tier": "power",
            "t": "Harmless versions in yeast, such as one formed by the protein Sup35, pass traits to daughter cells without changing their DNA",
            "k": ["yeast", "sup35", "daughter cells"],
            "n": 0
        },
        {
            "id": "same-sequence",
            "tier": "power",
            "t": "The misfolded and normal forms have the same amino acid sequence, but only the misfolded form partly resists the enzyme proteinase K",
            "k": ["proteinase k", "amino acid sequence"],
            "n": 0
        },
        {
            "id": "viroids",
            "tier": "power",
            "t": "Viroids, by contrast, are bare loops of RNA with no protein at all; they infect plants such as potatoes",
            "k": ["viroids", "loops of rna", "potatoes"],
            "n": 0
        },
        {
            "id": "feed-ban",
            "tier": "power",
            "t": "Britain banned feeding cattle meal made from animal remains in 1988; the epidemic peaked in the early 1990s",
            "k": ["1988", "banned", "early 1990s"],
            "n": 0
        },
        {
            "id": "eu-beef-ban",
            "tier": "power",
            "t": "In 1996, the European Union banned exports of British beef because of mad cow disease",
            "k": ["european union", "british beef"],
            "n": 0
        },
        {
            "id": "sporadic-cjd",
            "tier": "power",
            "t": "Most CJD cases appear for no known reason in older adults; a smaller share run in families",
            "k": ["no known reason", "older adults", "families"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Agent or disease?",
        "body": "Prion tossups and tossups on the diseases prions cause share almost every clue, so players blurt “mad cow disease” or “Creutzfeldt-Jakob disease” when the question wants the agent, or the reverse. Players also say “viruses,” but prions have no genes at all, and viroids are a different agent made only of RNA.",
        "fix": "Listen for the noun. “These agents,” “these particles,” or “these proteins” means prions; “this disease” wants a disease name, like mad cow disease (BSE), scrapie, kuru, or CJD. Genes inside a protein coat mean a virus, and a bare loop of RNA means a viroid. Saying only “proteins” earns a prompt.",
        "line": "Real answer line: <b><u>Prions</u></b> (accept <u>prion proteins</u>; prompt on <u>proteins</u>; do not accept “viruses”)"
    },
    "tests": {
        "right": [
            "Prions",
            "prion",
            "Prion proteins",
            "Pryons",
            "PrPSc"
        ],
        "prompt": [
            "Proteins",
            "Misfolded proteins"
        ],
        "wrong": [
            "Viruses",
            "Viroids",
            "Mad cow disease",
            "Pions",
            "Prisons",
            "Stanley Prusiner"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
