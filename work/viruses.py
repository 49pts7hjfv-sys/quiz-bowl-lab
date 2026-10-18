import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "viruses",
    "name": "Viruses",
    "mono": "VIR",
    "category": "Biology",
    "qbCategory": "Science · Biology",
    "kicker": "Tiny agents that hijack living cells · Cause the flu, colds, and COVID-19",
    "dates": "First found in 1892, in sick tobacco plants",
    "briefing": "Viruses are tiny packages of genes wrapped in a protein coat, so small that most can be seen only with an electron microscope. They are not made of cells and cannot do anything on their own, but once inside a living cell, they hijack its machinery to make many new copies of themselves. Viruses cause the flu, colds, chickenpox, and COVID-19, and vaccines train the body’s immune system to fight them.",
    "answerHtml": "<b><u>Viruses</u></b> (accept <u>virus</u> or <u>virions</u>; prompt on <u>pathogens</u> or <u>germs</u>; do not accept “bacteria” or “prions”)",
    "accept": [
        "viruses",
        "virus",
        "virions",
        "virion",
        "viral particles",
        "viral particle"
    ],
    "prompt": [
        "pathogens",
        "pathogen",
        "germs",
        "germ",
        "microbes",
        "microbe",
        "infectious agents",
        "infectious agent"
    ],
    "reject": [
        "bacteria",
        "bacterium",
        "prions",
        "prion",
        "viroids",
        "viroid",
        "bacteriophages",
        "bacteriophage",
        "phages",
        "phage",
        "influenza virus",
        "flu virus",
        "influenza",
        "flu",
        "hiv",
        "fungi",
        "protists",
        "parasites",
        "plasmids",
        "capsid",
        "capsids",
        "vaccines",
        "vaccine",
        "antibodies",
        "virology",
        "computer virus",
        "computer viruses"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Virus",
    "qb": {
        "q": "virus",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "In 1892, Dmitri Ivanovsky [“ee-vuh-NOFF-skee”] showed that the cause of tobacco mosaic disease could pass through porcelain filters fine enough to trap bacteria. Martinus Beijerinck [“BYE-er-ink”] later called that cause a “contagious living fluid.” These agents consist of genetic material inside a protein coat.",
            "r": "For 10 points, name these tiny infectious agents that can reproduce only inside living cells."
        },
        {
            "p": "Wendell Stanley shared a Nobel Prize in Chemistry after he crystallized the agent of tobacco mosaic disease in 1935, showing that these infectious agents can form crystals like ordinary chemicals. Unlike bacteria, these agents have no ribosomes and cannot make their own proteins.",
            "r": "Antibiotics do not work against them. For 10 points, name these agents that cause the flu and the common cold."
        },
        {
            "p": "Alfred Hershey and Martha Chase tagged some of these agents with radioactive sulfur and phosphorus to show that DNA, not protein, carries genetic information. The ones they used, called bacteriophages, have a head, a tail, and tail fibers that grab onto bacteria.",
            "r": "For 10 points, name these tiny agents that must hijack a host cell to copy themselves."
        },
        {
            "p": "Lambda phage, one of these agents, can either burst its host right away or tuck its DNA into the host’s chromosome as a prophage, choosing between the lytic and lysogenic cycles. Some of these agents, like HIV, carry RNA instead of DNA.",
            "r": "For 10 points, name these infectious agents, which consist of genetic material wrapped in a protein coat."
        },
        {
            "p": "Howard Temin and David Baltimore independently discovered reverse transcriptase in 1970, an enzyme that some of these agents use to copy their RNA into DNA. A system named for Baltimore sorts these agents into seven groups based on their genetic material.",
            "r": "HIV is one of them. For 10 points, name these agents, which also cause smallpox and measles."
        },
        {
            "p": "Aphids spreading one of these agents gave tulips the flame-like stripes that made some bulbs sell for huge prices during the 1600s Dutch “tulip mania.” Another of these agents causes tobacco mosaic disease, which makes leaves look mottled.",
            "r": "For 10 points, name these tiny infectious agents that can reproduce only inside a host’s cells."
        },
        {
            "p": "Alick Isaacs and Jean Lindenmann discovered interferons in 1957, proteins that infected cells release to warn their neighbors and block the spread of these agents. Edward Jenner used material from cowpox sores to protect people against smallpox, a disease caused by one of these agents.",
            "r": "For 10 points, name these agents, which are not made of cells and need a host cell to reproduce."
        },
        {
            "p": "Rinderpest, a cattle disease declared wiped out in 2011, and smallpox, declared eradicated in 1980, are the only two infectious diseases ever eradicated, and both were caused by these agents. Jonas Salk developed a vaccine against polio, which is caused by another one of these agents.",
            "r": "These agents are much smaller than bacteria. For 10 points, name these tiny agents, which antibiotics cannot kill."
        },
        {
            "p": "Katalin Karikó [“KAH-ree-koh”] and Drew Weissman won the 2023 Nobel Prize in Physiology or Medicine for work that made mRNA vaccines against one of these agents, SARS-CoV-2, possible. That agent has crown-like spikes on its outer envelope, which it takes from a host cell’s membranes.",
            "r": "COVID-19 is caused by one. For 10 points, name these agents, which also cause the flu and chickenpox."
        },
        {
            "p": "Bacteria store snippets of these agents’ DNA in CRISPR regions of their own genomes so that Cas enzymes can recognize and cut them during a later attack. Jennifer Doudna and Emmanuelle Charpentier turned that defense system into a gene-editing tool.",
            "r": "Bacteriophages are the ones that attack bacteria. For 10 points, name these infectious agents that copy themselves inside host cells."
        },
        {
            "p": "The first giant member of this group to be recognized, found inside amoebae and described in 2003, is larger than some bacteria and has nearly a thousand genes. Most of these agents are far too small to see with a light microscope and were first photographed with electron microscopes.",
            "r": "For 10 points, name these tiny infectious agents, made of genetic material inside a protein coat, that hijack living cells."
        },
        {
            "p": "The protein coats of many of these agents are icosahedrons, with 20 triangular faces built from units called capsomeres [“CAP-suh-meerz”]. Others, like the agent of tobacco mosaic disease, form long, hollow, spiral-shaped rods.",
            "r": "For 10 points, name these agents whose protein coat, or capsid, surrounds a core of DNA or RNA, and which reproduce only inside host cells."
        },
        {
            "p": "About 8 percent of the human genome is made of leftover genes from ancient members of this group that inserted their DNA into our ancestors’ chromosomes. Some members of this group have an outer envelope stolen from the host cell’s membrane as they bud out.",
            "r": "Vaccines protect against many of them. For 10 points, name these agents that cause measles, mumps, and chickenpox."
        },
        {
            "p": "Louis Pasteur made a rabies vaccine in 1885 even though he could never see the tiny agent that causes rabies, which is one of these. Each kind of these agents can enter only cells that have the right surface receptors, so many infect just one or a few host species.",
            "r": "Antibiotics do not work on them. For 10 points, name these infectious agents, which include the cause of the flu."
        },
        {
            "p": "Strains of one of these agents get codes like H1N1 and H5N1, named for two of its surface proteins, hemagglutinin [“hee-muh-GLOO-tuh-nin”] and neuraminidase [“noor-uh-MIN-ih-dayss”]. Small changes in those proteins, called antigenic drift, mean that the vaccine against that agent must be updated every year.",
            "r": "For 10 points, name these infectious agents, which include the causes of influenza and the common cold."
        }
    ],
    "clues": [
        {
            "id": "definition",
            "tier": "giveaway",
            "t": "Tiny infectious agents that can reproduce only inside the living cells of a host",
            "k": ["infectious agents", "living cells", "host"],
            "n": 0
        },
        {
            "id": "capsid",
            "tier": "giveaway",
            "t": "Made of genetic material (DNA or RNA) inside a protein coat called a capsid",
            "k": ["capsid", "protein coat"],
            "n": 0
        },
        {
            "id": "diseases",
            "tier": "giveaway",
            "t": "Cause the flu, the common cold, measles, chickenpox, COVID-19, and HIV/AIDS",
            "k": ["common cold", "measles", "chickenpox"],
            "n": 0
        },
        {
            "id": "not-alive",
            "tier": "giveaway",
            "t": "Not made of cells and have no metabolism of their own, so many biologists say they are not truly alive",
            "k": ["not truly alive", "metabolism"],
            "n": 0
        },
        {
            "id": "antibiotics",
            "tier": "giveaway",
            "t": "Antibiotics, which fight bacteria, do not work against them",
            "k": ["antibiotics"],
            "n": 0,
            "rabbit": "Bacteria"
        },
        {
            "id": "small",
            "tier": "middle",
            "t": "Much smaller than bacteria; most can be seen only with an electron microscope",
            "k": ["electron microscope", "smaller than bacteria"],
            "n": 0
        },
        {
            "id": "phages",
            "tier": "middle",
            "t": "Bacteriophages, or phages, are the ones that infect bacteria",
            "k": ["bacteriophages", "phages"],
            "n": 0,
            "rabbit": "Bacteriophages"
        },
        {
            "id": "lytic-lysogenic",
            "tier": "middle",
            "t": "Lytic cycle: the host cell makes copies until it bursts. Lysogenic cycle: the genes hide inside the host’s DNA",
            "k": ["lytic", "lysogenic"],
            "n": 0
        },
        {
            "id": "envelope",
            "tier": "middle",
            "t": "Some have an outer envelope taken from a host cell’s membrane as they bud out",
            "k": ["envelope", "bud"],
            "n": 0
        },
        {
            "id": "jenner",
            "tier": "middle",
            "t": "Edward Jenner’s 1796 cowpox vaccine protected against smallpox, which was declared eradicated in 1980",
            "k": ["edward jenner", "cowpox", "smallpox", "1796"],
            "n": 0
        },
        {
            "id": "salk",
            "tier": "middle",
            "t": "Jonas Salk’s vaccine, announced in 1955, protects against polio, which one of them causes",
            "k": ["jonas salk", "polio", "1955"],
            "n": 0,
            "rabbit": "Polio"
        },
        {
            "id": "hiv",
            "tier": "middle",
            "t": "HIV attacks the immune system’s helper T cells",
            "k": ["helper t cells", "immune system"],
            "n": 0,
            "rabbit": "HIV"
        },
        {
            "id": "pasteur",
            "tier": "middle",
            "t": "Louis Pasteur made a rabies vaccine in 1885 without ever seeing the agent behind the disease",
            "k": ["louis pasteur", "rabies", "1885"],
            "n": 0,
            "rabbit": "Louis Pasteur"
        },
        {
            "id": "receptors",
            "tier": "middle",
            "t": "Each kind can enter only cells with the right surface receptors, so many infect just one or a few host species",
            "k": ["receptors", "host species"],
            "n": 0
        },
        {
            "id": "ivanovsky-beijerinck",
            "tier": "power",
            "t": "Dmitri Ivanovsky (1892) showed the cause of tobacco mosaic disease slips through bacteria-trapping filters; Martinus Beijerinck called it a “contagious living fluid”",
            "k": ["ivanovsky", "beijerinck", "contagious living fluid"],
            "n": 0
        },
        {
            "id": "stanley",
            "tier": "power",
            "t": "Wendell Stanley crystallized the tobacco mosaic agent in 1935 and shared the 1946 Nobel Prize in Chemistry",
            "k": ["wendell stanley", "crystallized", "1935"],
            "n": 0
        },
        {
            "id": "hershey-chase",
            "tier": "power",
            "t": "Alfred Hershey and Martha Chase tagged phages with radioactive sulfur and phosphorus to show DNA is the genetic material",
            "k": ["hershey", "chase", "radioactive"],
            "n": 0,
            "rabbit": "DNA"
        },
        {
            "id": "reverse-transcriptase",
            "tier": "power",
            "t": "Howard Temin and David Baltimore discovered reverse transcriptase (1970); the Baltimore classification sorts them into seven groups",
            "k": ["reverse transcriptase", "temin", "baltimore classification"],
            "n": 0
        },
        {
            "id": "prophage",
            "tier": "power",
            "t": "Lambda phage can tuck its DNA into a bacterium’s chromosome as a prophage",
            "k": ["prophage", "lambda"],
            "n": 0
        },
        {
            "id": "capsomeres",
            "tier": "power",
            "t": "Capsids are built from units called capsomeres, often shaped like a 20-sided icosahedron or a spiral rod",
            "k": ["capsomeres", "icosahedron"],
            "n": 0
        },
        {
            "id": "interferons",
            "tier": "power",
            "t": "Interferons, discovered by Alick Isaacs and Jean Lindenmann in 1957, are proteins that cells release to block their spread",
            "k": ["interferons", "isaacs", "lindenmann"],
            "n": 0
        },
        {
            "id": "tulip-mania",
            "tier": "power",
            "t": "Aphid-spread ones gave tulips flame-like stripes during the 1600s Dutch tulip mania",
            "k": ["tulip mania", "aphid", "stripes"],
            "n": 0
        },
        {
            "id": "crispr",
            "tier": "power",
            "t": "Bacteria’s CRISPR defense stores bits of phage DNA so that Cas enzymes can cut invaders later",
            "k": ["crispr", "enzymes"],
            "n": 0
        },
        {
            "id": "giant",
            "tier": "power",
            "t": "The first giant one recognized (2003) was found inside amoebae, is bigger than some bacteria, and has nearly a thousand genes",
            "k": ["giant", "amoebae", "2003"],
            "n": 0
        },
        {
            "id": "human-genome",
            "tier": "power",
            "t": "About 8 percent of the human genome comes from ancient ones that inserted their genes into our ancestors’ DNA",
            "k": ["human genome", "8 percent"],
            "n": 0
        },
        {
            "id": "mrna-vaccines",
            "tier": "power",
            "t": "Katalin Karikó and Drew Weissman won the 2023 Nobel Prize for work behind the mRNA vaccines against COVID-19",
            "k": ["weissman", "mrna vaccines", "2023"],
            "n": 0
        },
        {
            "id": "rinderpest",
            "tier": "power",
            "t": "Smallpox (1980) and the cattle disease rinderpest (2011) are the only infectious diseases ever eradicated; both were caused by them",
            "k": ["rinderpest", "eradicated", "2011"],
            "n": 0
        },
        {
            "id": "flu-codes",
            "tier": "power",
            "t": "Flu strains are named for two surface proteins, hemagglutinin (H) and neuraminidase (N), as in H1N1",
            "k": ["hemagglutinin", "neuraminidase", "h1n1"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Not bacteria, not prions",
        "body": "Bacteria are living cells with their own ribosomes, and antibiotics can kill them; these agents are not cells at all, are far smaller, and must hijack a host cell to make copies of themselves. Prions (misfolded proteins with no genes) and viroids (bare loops of RNA with no protein coat) are even simpler agents with their own answer lines. Many clues also name one famous example, like HIV or influenza, but the question wants the whole group.",
        "fix": "A protein coat (capsid), a host cell, the lytic cycle, or tobacco mosaic disease mean viruses. Cell walls, binary fission, or antibiotics that work mean bacteria; a misfolded protein with no DNA or RNA means prions.",
        "line": "Real answer line: <b><u>Viruses</u></b> (accept <u>virus</u> or <u>virions</u>; prompt on <u>pathogens</u> or <u>germs</u>; do not accept “bacteria” or “prions”)"
    },
    "tests": {
        "right": [
            "Viruses",
            "virus",
            "Virions",
            "Virses",
            "A virus"
        ],
        "prompt": [
            "Pathogens",
            "Germs"
        ],
        "wrong": [
            "Bacteria",
            "Prions",
            "Viroids",
            "Bacteriophages",
            "Influenza virus",
            "HIV"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
