import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "malaria",
    "name": "Malaria",
    "mono": "MAL",
    "category": "Biology",
    "qbCategory": "Science · Biology",
    "kicker": "Parasitic disease spread by mosquitoes · Named for Italian “bad air”",
    "dates": "Parasite first seen by Alphonse Laveran in 1880",
    "briefing": "Malaria is caused not by a virus or bacterium but by Plasmodium, a single-celled parasite carried by female Anopheles mosquitoes. Inside a person, the parasites multiply in the liver and then invade red blood cells, causing repeating waves of fever and chills. It is one of history’s deadliest diseases, but bed nets, the drug artemisinin, and the first vaccines, recommended in 2021 and 2023, are helping fight it.",
    "answerHtml": "<b><u>Malaria</u></b> (do not accept “Plasmodium” or “mosquito”)",
    "accept": [
        "malaria",
        "malarial fever"
    ],
    "prompt": [],
    "reject": [
        "plasmodium",
        "plasmodium falciparum",
        "plasmodium vivax",
        "falciparum",
        "anopheles",
        "mosquito",
        "mosquitoes",
        "mosquitos",
        "yellow fever",
        "dengue",
        "dengue fever",
        "zika",
        "west nile",
        "sleeping sickness",
        "sickle cell",
        "sickle cell disease",
        "sickle cell anemia",
        "quinine",
        "artemisinin",
        "cholera",
        "typhoid",
        "tuberculosis"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Malaria",
    "qb": {
        "q": "malaria",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "The parasites that cause this disease digest hemoglobin inside red blood cells, leaving behind dark crystals of a pigment called hemozoin [“hee-moh-ZOH-in”]. The drug chloroquine was widely used against this disease until many of those parasites became resistant to it.",
            "r": "For 10 points, name this disease caused by Plasmodium parasites and spread by the bites of Anopheles mosquitoes."
        },
        {
            "p": "Two species that cause this disease, vivax and ovale, can hide in the liver as dormant forms called hypnozoites [“hip-noh-ZOH-ites”] and cause relapses weeks or months later. The drug primaquine is given to clear out those dormant liver forms.",
            "r": "For 10 points, name this disease spread by mosquitoes that causes repeating bouts of fever and chills."
        },
        {
            "p": "In 1880, French army doctor Alphonse Laveran [“lav-RAHN”] became the first person to see the single-celled parasite behind this disease, in a patient’s blood. In 1897, Ronald Ross found that parasite in the stomach of a mosquito, a discovery remembered each August 20 on World Mosquito Day.",
            "r": "Both men won Nobel Prizes. For 10 points, name this disease caused by Plasmodium and carried by Anopheles mosquitoes."
        },
        {
            "p": "Tu Youyou [“TOO yoh-YOH”] shared a 2015 Nobel Prize after a 4th-century Chinese medical text led her to a treatment for this disease made from sweet wormwood. That drug, artemisinin [“ar-teh-MISS-ih-nin”], is combined with other medicines to treat this disease around the world.",
            "r": "For 10 points, name this disease caused by Plasmodium parasites that spread through mosquito bites."
        },
        {
            "p": "Jesuit missionaries helped bring a bark nicknamed “Jesuit’s bark” from Peru to Europe to treat this disease. In 1820, Pierre-Joseph Pelletier and Joseph Caventou isolated the bark’s bitter active ingredient, which also flavors tonic water.",
            "r": "That ingredient is quinine, from the cinchona tree. For 10 points, name this disease spread by Anopheles mosquitoes."
        },
        {
            "p": "Many people in West and Central Africa lack the Duffy antigen on their red blood cells, which helps protect them from vivax, one of the species that cause this disease, since vivax uses that antigen to enter the cells.",
            "r": "Insecticide-treated bed nets help prevent this disease. For 10 points, name this illness caused by Plasmodium parasites and spread by Anopheles mosquitoes."
        },
        {
            "p": "In the classic example of heterozygote advantage, people who carry one copy of the gene for sickle-cell hemoglobin are partly protected from this disease. That protection helps explain why the sickle-cell gene is common in regions where this disease is widespread.",
            "r": "For 10 points, name this mosquito-borne disease caused by Plasmodium parasites that invade red blood cells."
        },
        {
            "p": "The Communicable Disease Center, which became the CDC, was founded in Atlanta in 1946, growing out of a wartime office set up to fight this disease in the American South. By the early 1950s, this disease had been eliminated from the United States.",
            "r": "It causes repeating fevers and chills. For 10 points, name this disease spread by Anopheles mosquitoes and caused by Plasmodium."
        },
        {
            "p": "In 2021, the World Health Organization recommended RTS,S, the first vaccine against this disease, and in 2023 it recommended a second vaccine, R21. This disease kills hundreds of thousands of people each year, most of them young children in Africa.",
            "r": "People in at-risk areas protect themselves with bed nets and insect repellent. For 10 points, name this disease carried by Anopheles mosquitoes."
        },
        {
            "p": "During the building of the Panama Canal, William Gorgas cut cases of yellow fever and this other disease by draining standing water and spreading oil on ponds where mosquitoes bred. Buildings were also fitted with screens to keep out the mosquitoes that carry this disease.",
            "r": "Its name comes from Italian words meaning “bad air.” For 10 points, name this disease caused by Plasmodium parasites."
        },
        {
            "p": "Paul Müller won a 1948 Nobel Prize for discovering that DDT kills insects, and DDT spraying was a key part of the World Health Organization’s 1955 campaign to wipe out this disease. That campaign worked in some countries, but mosquitoes became resistant to DDT.",
            "r": "Quinine was an early treatment for it. For 10 points, name this disease carried by Anopheles mosquitoes and caused by Plasmodium."
        },
        {
            "p": "The deadliest species that causes this disease forms crescent-shaped cells called gametocytes, the stage that a feeding mosquito picks up. That species, falciparum, causes most deaths from this disease in Africa.",
            "r": "Infected red blood cells break open on a regular cycle, causing repeating fevers. For 10 points, name this disease caused by Plasmodium parasites."
        },
        {
            "p": "Unlike many other mosquitoes, the ones that spread this disease rest at a steep angle with their abdomens pointed up, and their larvae lie flat against the water’s surface. Only the females of that genus, Anopheles [“uh-NOFF-uh-leez”], bite people.",
            "r": "For 10 points, name this disease caused by Plasmodium parasites and treated with drugs like quinine and artemisinin."
        },
        {
            "p": "The parasites that cause this disease reproduce sexually inside mosquitoes, which makes the mosquito their definitive host. Forms called sporozoites [“SPOR-uh-ZOH-ites”] travel from the mosquito’s salivary glands to a person’s liver, where they multiply and release new forms that invade red blood cells.",
            "r": "Its main symptoms are repeating fevers and chills. For 10 points, name this disease caused by Plasmodium."
        },
        {
            "p": "Plasmodium knowlesi [“NOHLZ-ee-eye”], which normally infects macaque monkeys, can also give people this disease in Southeast Asia. People once blamed this disease on foul air rising from swamps, which is why its name comes from the Italian for “bad air.”",
            "r": "For 10 points, name this disease spread by Anopheles mosquitoes and treated with quinine."
        }
    ],
    "clues": [
        {
            "id": "anopheles",
            "tier": "giveaway",
            "t": "Spread by the bites of infected female Anopheles mosquitoes",
            "k": ["anopheles", "mosquitoes", "female"],
            "n": 0
        },
        {
            "id": "plasmodium",
            "tier": "giveaway",
            "t": "Caused by single-celled parasites in the genus Plasmodium, not by a virus or bacterium",
            "k": ["plasmodium", "parasites", "single-celled"],
            "n": 0
        },
        {
            "id": "bad-air",
            "tier": "giveaway",
            "t": "Its name comes from Italian for “bad air,” from an old belief that swamp air caused it",
            "k": ["bad air", "italian", "swamp"],
            "n": 0
        },
        {
            "id": "quinine",
            "tier": "giveaway",
            "t": "Long treated with quinine, from the bark of the South American cinchona tree",
            "k": ["quinine", "cinchona", "bark"],
            "n": 0
        },
        {
            "id": "fevers",
            "tier": "giveaway",
            "t": "Causes repeating bouts of fever and chills",
            "k": ["fever", "chills", "repeating"],
            "n": 0
        },
        {
            "id": "liver-then-blood",
            "tier": "middle",
            "t": "The parasites first multiply in the liver, then invade red blood cells",
            "k": ["liver", "red blood cells"],
            "n": 0,
            "rabbit": "Red blood cells"
        },
        {
            "id": "sickle-cell-trait",
            "tier": "middle",
            "t": "One copy of the sickle-cell gene gives partial protection against it, the classic case of heterozygote advantage",
            "k": ["sickle-cell", "heterozygote advantage"],
            "n": 0,
            "rabbit": "Sickle-cell disease"
        },
        {
            "id": "falciparum",
            "tier": "middle",
            "t": "Plasmodium falciparum is the deadliest species and causes most deaths from it in Africa",
            "k": ["falciparum", "deadliest", "africa"],
            "n": 0
        },
        {
            "id": "bed-nets",
            "tier": "middle",
            "t": "Prevented with insecticide-treated bed nets and by draining standing water where mosquitoes breed",
            "k": ["bed nets", "insecticide", "standing water"],
            "n": 0
        },
        {
            "id": "ronald-ross",
            "tier": "middle",
            "t": "Ronald Ross found its parasite in a mosquito in 1897 (marked by World Mosquito Day, August 20) and won the 1902 Nobel Prize",
            "k": ["ronald ross", "1897", "1902", "mosquito day"],
            "n": 0
        },
        {
            "id": "laveran",
            "tier": "middle",
            "t": "French army doctor Alphonse Laveran first saw its parasite in a patient’s blood in 1880",
            "k": ["laveran", "1880"],
            "n": 0
        },
        {
            "id": "artemisinin",
            "tier": "middle",
            "t": "Tu Youyou found the drug artemisinin in sweet wormwood and shared a 2015 Nobel Prize",
            "k": ["artemisinin", "tu youyou", "sweet wormwood", "2015"],
            "n": 0
        },
        {
            "id": "hypnozoites",
            "tier": "power",
            "t": "Vivax and ovale can lie dormant in the liver as hypnozoites and cause relapses; primaquine clears them",
            "k": ["hypnozoites", "vivax", "ovale", "primaquine"],
            "n": 0
        },
        {
            "id": "hemozoin",
            "tier": "power",
            "t": "The parasites digest hemoglobin and leave dark crystals of a pigment called hemozoin",
            "k": ["hemozoin", "pigment"],
            "n": 0
        },
        {
            "id": "chloroquine",
            "tier": "power",
            "t": "Chloroquine was a standard drug against it until many parasites became resistant",
            "k": ["chloroquine", "resistant"],
            "n": 0
        },
        {
            "id": "duffy",
            "tier": "power",
            "t": "People who lack the Duffy antigen on their red blood cells resist vivax, which uses that antigen to get in",
            "k": ["duffy", "antigen"],
            "n": 0
        },
        {
            "id": "cdc",
            "tier": "power",
            "t": "The CDC began in Atlanta in 1946, growing out of a wartime office that fought it in the American South",
            "k": ["cdc", "atlanta", "1946"],
            "n": 0
        },
        {
            "id": "gorgas",
            "tier": "power",
            "t": "William Gorgas fought it and yellow fever by controlling mosquitoes during the building of the Panama Canal",
            "k": ["gorgas", "panama canal", "yellow fever"],
            "n": 0
        },
        {
            "id": "ddt",
            "tier": "power",
            "t": "Paul Müller won a 1948 Nobel Prize for showing that DDT kills insects; DDT was central to the WHO’s 1955 campaign against it",
            "k": ["müller", "ddt", "1948", "1955"],
            "n": 0
        },
        {
            "id": "vaccines",
            "tier": "power",
            "t": "The WHO recommended the first vaccines against it: RTS,S in 2021 and R21 in 2023",
            "k": ["rts,s", "r21", "vaccines"],
            "n": 0
        },
        {
            "id": "definitive-host",
            "tier": "power",
            "t": "Its parasite reproduces sexually inside the mosquito, which makes the mosquito its definitive host",
            "k": ["definitive host", "sexually"],
            "n": 0
        },
        {
            "id": "sporozoites",
            "tier": "power",
            "t": "Sporozoites travel from a mosquito’s salivary glands to a person’s liver",
            "k": ["sporozoites", "salivary glands"],
            "n": 0
        },
        {
            "id": "resting-angle",
            "tier": "power",
            "t": "Anopheles mosquitoes rest at a steep angle with abdomens raised, and their larvae lie flat on the water",
            "k": ["steep angle", "abdomens", "larvae"],
            "n": 0
        },
        {
            "id": "pelletier-caventou",
            "tier": "power",
            "t": "Pelletier and Caventou isolated quinine in 1820; cinchona bark was nicknamed “Jesuit’s bark”",
            "k": ["pelletier", "caventou", "1820", "jesuit’s bark"],
            "n": 0
        },
        {
            "id": "gametocytes",
            "tier": "power",
            "t": "Falciparum’s gametocytes, the stage that a feeding mosquito picks up, are crescent-shaped",
            "k": ["gametocytes", "crescent-shaped"],
            "n": 0
        },
        {
            "id": "knowlesi",
            "tier": "power",
            "t": "Plasmodium knowlesi, a parasite of macaque monkeys, also infects people in Southeast Asia",
            "k": ["knowlesi", "macaque", "southeast asia"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Disease, parasite, or mosquito?",
        "body": "These tossups describe three different living things: the disease, the Plasmodium parasite that causes it, and the Anopheles mosquito that carries it. If the question asks for “this disease,” naming the parasite or the mosquito is wrong. Players also mix it up with other mosquito-borne diseases, such as yellow fever, dengue, and Zika, which are caused by viruses.",
        "fix": "Plasmodium is the parasite, Anopheles is the mosquito, and malaria is the disease. Quinine, artemisinin, hypnozoites, and the sickle-cell trait point to malaria; Walter Reed and Aedes mosquitoes point to yellow fever.",
        "line": "Real answer line: <b><u>Malaria</u></b> (do not accept “Plasmodium” or “mosquito”)"
    },
    "tests": {
        "right": [
            "Malaria",
            "malaria",
            "Maleria",
            "Malarea",
            "Malarial fever"
        ],
        "prompt": [],
        "wrong": [
            "Plasmodium",
            "Yellow fever",
            "Dengue fever",
            "Mosquito",
            "Sickle-cell disease",
            "Sleeping sickness"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
