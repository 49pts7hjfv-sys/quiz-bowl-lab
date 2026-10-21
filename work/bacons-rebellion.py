import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "bacons-rebellion",
    "name": "Bacon’s Rebellion",
    "mono": "BCR",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "1676 revolt against Virginia’s governor · Rebels burned Jamestown",
    "dates": "1676",
    "briefing": "In 1676, a 29-year-old planter named Nathaniel Bacon led angry frontier settlers, servants, and some enslaved Africans in a revolt against Virginia’s governor, William Berkeley. The rebels attacked Native peoples, including some who had been at peace with the colony, and burned the capital, Jamestown, to the ground. The revolt fell apart after Bacon died of disease, and many historians think it pushed Virginia’s planters to rely more on enslaved labor.",
    "answerHtml": "<b><u>Bacon’s Rebellion</u></b> (prompt on <u>Bacon</u> or <u>Nathaniel Bacon</u>)",
    "accept": [
        "bacons rebellion",
        "bacon rebellion",
        "bacons revolt",
        "bacon revolt",
        "bacons uprising",
        "nathaniel bacons rebellion",
        "nathaniel bacon rebellion",
        "rebellion of nathaniel bacon"
    ],
    "prompt": [
        "bacon",
        "nathaniel bacon"
    ],
    "reject": [
        "francis bacon",
        "roger bacon",
        "henry bacon",
        "shays rebellion",
        "whiskey rebellion",
        "leislers rebellion",
        "stono rebellion",
        "nat turners rebellion",
        "nat turner",
        "slave rebellions",
        "slave rebellion",
        "pueblo revolt",
        "king philips war",
        "metacoms war",
        "culpepers rebellion",
        "fries rebellion",
        "dorr rebellion",
        "pontiacs rebellion",
        "pontiacs war",
        "glorious revolution",
        "jamestown",
        "colony of virginia",
        "virginia colony",
        "william berkeley",
        "berkeley",
        "powhatan wars",
        "starving time"
    ],
    "mediaPending": True,
    "media": [],
    "wiki": "https://en.wikipedia.org/wiki/Bacon%27s_Rebellion",
    "qb": {
        "q": "Bacon's Rebellion",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "In 1675, a quarrel over trade goods between a planter in northern Virginia and the Doeg people led to killings on the frontier. Soon afterward, Virginia and Maryland militias killed five Susquehannock [“suss-kwuh-HAN-uk”] leaders who had come out to negotiate, and raids and counterattacks spread along the frontier.",
            "r": "For 10 points, name this 1676 revolt in which Nathaniel Bacon led frontier settlers against Governor William Berkeley."
        },
        {
            "p": "In May 1676, a planter led volunteers to an island in the Roanoke River, where they persuaded the Occaneechi [“oh-kuh-NEE-chee”] people to attack the Susquehannock and then turned on the Occaneechi themselves. Virginia’s governor declared that planter a rebel for marching without permission.",
            "r": "That planter was Nathaniel Bacon. For 10 points, name this 1676 uprising in colonial Virginia."
        },
        {
            "p": "In June 1676, after the armed followers of this uprising’s leader surrounded the statehouse, a governor reportedly bared his chest and dared the leader to shoot him. The governor then gave the leader a commission to fight Native Americans.",
            "r": "That governor was William Berkeley. For 10 points, name this rebellion in Virginia, led by Nathaniel Bacon."
        },
        {
            "p": "On July 30, 1676, the leader of this event issued a “Declaration in the Name of the People” that accused Virginia’s governor of unjust taxes, rewarding his favorites, and failing to defend settlers on the frontier.",
            "r": "For 10 points, name this 1676 rebellion in which Nathaniel Bacon’s followers burned Jamestown."
        },
        {
            "p": "A House of Burgesses elected in June 1676 passed reforms named for the leader of this uprising, including a law that again allowed free men who owned no land to vote. The king’s government later canceled those reforms.",
            "r": "That leader was Nathaniel Bacon. For 10 points, name this 1676 rebellion against Virginia governor William Berkeley."
        },
        {
            "p": "During this event, a governor fled across the Chesapeake Bay to Accomack County on Virginia’s Eastern Shore, where he gathered loyal men and ships before returning to fight. His plantation, Green Spring, stood just a few miles from the capital.",
            "r": "That governor was William Berkeley. For 10 points, name this 1676 revolt led by Nathaniel Bacon."
        },
        {
            "p": "Rebels held a brick house in Surry County for several months during this event, and the house is still named for their leader, even though he never went there. Built in 1665, it is one of the oldest brick houses in the United States.",
            "r": "That leader was Nathaniel Bacon. For 10 points, name this 1676 rebellion in colonial Virginia."
        },
        {
            "p": "After this event, King Charles II reportedly complained that his governor had hanged more men in Virginia than the king had executed for the killing of his own father. That governor had 23 rebels hanged before he was called back to England.",
            "r": "That governor was William Berkeley. For 10 points, name this 1676 revolt led by Nathaniel Bacon."
        },
        {
            "p": "In his book _American Slavery, American Freedom_, historian Edmund Morgan argued that after this event, Virginia’s wealthy planters came to rely more on enslaved Africans and less on poor white servants, many of whom had joined it.",
            "r": "For 10 points, name this 1676 rebellion against Governor William Berkeley, led by Nathaniel Bacon."
        },
        {
            "p": "The Treaty of Middle Plantation, signed in 1677 after this event, made peace between Virginia and several Native nations, including the Pamunkey, whose leader was a woman the English called the Queen of Pamunkey. Her people had been attacked during this event.",
            "r": "For 10 points, name this rebellion of 1676, led by Nathaniel Bacon against Virginia’s governor."
        },
        {
            "p": "The leader of this event died of disease in October 1676 at age 29, and his body was never found; his followers may have buried it in secret. Joseph Ingram took over, but the revolt soon fell apart.",
            "r": "That leader was Nathaniel Bacon. For 10 points, name this rebellion in which Jamestown was burned."
        },
        {
            "p": "King Charles II sent about 1,000 soldiers and three commissioners, including Herbert Jeffreys, to Virginia in response to this event. The colony’s longtime governor was ordered back to England, where he died in 1677, and Jeffreys took over the government.",
            "r": "For 10 points, name this rebellion in which Nathaniel Bacon’s followers burned Jamestown, Virginia’s capital."
        },
        {
            "p": "Near the end of this event, some of the last rebels holding out were enslaved Africans and English indentured servants who had joined it hoping to win their freedom. A ship captain named Thomas Grantham talked them into giving up.",
            "r": "For 10 points, name this 1676 Virginia uprising led by Nathaniel Bacon against Governor William Berkeley."
        },
        {
            "p": "The leader of this event had arrived in Virginia only in 1674, bought land along the James River, and was quickly given a seat on the governor’s council. In 1676, his overseer was killed in a raid on his frontier plantation.",
            "r": "That leader, Nathaniel Bacon, then led settlers against Governor William Berkeley. For 10 points, name this 1676 revolt."
        },
        {
            "p": "A 1676 law backed by a colonial governor called for a line of expensive forts along the frontier, which many settlers saw as costly and useless. Some settlers also believed the governor wanted to protect his friends’ profitable fur trade with Native peoples.",
            "r": "Those settlers wanted war instead, and Nathaniel Bacon led them against Governor William Berkeley. For 10 points, name this 1676 rebellion."
        }
    ],
    "clues": [
        {
            "id": "bacon-berkeley",
            "tier": "giveaway",
            "t": "Led by Nathaniel Bacon against Virginia’s governor, William Berkeley, in 1676",
            "k": ["nathaniel", "william berkeley", "berkeley", "1676"],
            "n": 0
        },
        {
            "id": "jamestown-burned",
            "tier": "giveaway",
            "t": "Rebels burned Jamestown, Virginia’s capital, in September 1676",
            "k": ["jamestown", "burned", "september 1676"],
            "n": 0,
            "rabbit": "Jamestown"
        },
        {
            "id": "frontier",
            "tier": "giveaway",
            "t": "Frontier settlers were angry that Berkeley would not let them attack Native Americans",
            "k": ["frontier", "native americans"],
            "n": 0,
            "rabbit": "Colony of Virginia"
        },
        {
            "id": "bacon-death",
            "tier": "middle",
            "t": "Fell apart after Bacon died of disease in October 1676",
            "k": ["died", "disease", "october 1676"],
            "n": 0
        },
        {
            "id": "declaration",
            "tier": "middle",
            "t": "Bacon’s “Declaration in the Name of the People” (July 30, 1676) accused Berkeley of unjust taxes and favoritism",
            "k": ["declaration in the name of the people", "declaration", "unjust taxes"],
            "n": 0
        },
        {
            "id": "servants",
            "tier": "middle",
            "t": "Bacon’s followers included poor white indentured servants and enslaved Africans",
            "k": ["indentured servants", "enslaved africans", "servants"],
            "n": 0
        },
        {
            "id": "historians",
            "tier": "middle",
            "t": "Many historians argue that afterward, Virginia’s planters relied more on enslaved Africans and less on indentured servants",
            "k": ["historians", "planters", "enslaved"],
            "n": 0,
            "rabbit": "Tobacco"
        },
        {
            "id": "pamunkey",
            "tier": "middle",
            "t": "Bacon’s men attacked Native peoples who had been at peace with the colony, such as the Pamunkey",
            "k": ["pamunkey", "at peace"],
            "n": 0
        },
        {
            "id": "rebel-declared",
            "tier": "middle",
            "t": "Berkeley declared Bacon a rebel for marching against Native peoples without permission (May 1676)",
            "k": ["rebel", "without permission", "may 1676"],
            "n": 0
        },
        {
            "id": "commission",
            "tier": "middle",
            "t": "In June 1676, Bacon’s armed men surrounded the statehouse and forced Berkeley to give him a commission",
            "k": ["commission", "statehouse", "june 1676"],
            "n": 0
        },
        {
            "id": "charles-ii",
            "tier": "middle",
            "t": "King Charles II sent about 1,000 soldiers; Berkeley was called back to England and died there in 1677",
            "k": ["charles ii", "1,000 soldiers", "1677"],
            "n": 0
        },
        {
            "id": "doeg",
            "tier": "power",
            "t": "Grew out of a 1675 trade quarrel with the Doeg people; militias then killed five Susquehannock leaders who came out to negotiate",
            "k": ["doeg", "susquehannock", "1675"],
            "n": 0
        },
        {
            "id": "occaneechi",
            "tier": "power",
            "t": "May 1676: on a Roanoke River island, Bacon’s volunteers persuaded the Occaneechi to attack the Susquehannock, then turned on them",
            "k": ["occaneechi", "roanoke river", "island"],
            "n": 0
        },
        {
            "id": "bared-chest",
            "tier": "power",
            "t": "Berkeley reportedly bared his chest and dared Bacon to shoot him",
            "k": ["bared his chest", "dared", "shoot"],
            "n": 0
        },
        {
            "id": "bacons-laws",
            "tier": "power",
            "t": "A House of Burgesses elected in June 1676 passed “Bacon’s Laws,” including one letting landless free men vote again",
            "k": ["house of burgesses", "bacon’s laws", "landless"],
            "n": 0
        },
        {
            "id": "eastern-shore",
            "tier": "power",
            "t": "Berkeley fled across the Chesapeake Bay to Accomack on Virginia’s Eastern Shore; his plantation was Green Spring",
            "k": ["eastern shore", "accomack", "chesapeake", "green spring"],
            "n": 0
        },
        {
            "id": "bacons-castle",
            "tier": "power",
            "t": "Rebels held a 1665 brick house in Surry County still called “Bacon’s Castle,” though Bacon never went there",
            "k": ["surry county", "1665", "bacon’s castle"],
            "n": 0
        },
        {
            "id": "hanged",
            "tier": "power",
            "t": "Berkeley hanged 23 rebels; Charles II reportedly said he had hanged more men than the king executed for his own father’s death",
            "k": ["23 rebels", "hanged", "father"],
            "n": 0
        },
        {
            "id": "morgan",
            "tier": "power",
            "t": "Historian Edmund Morgan’s _American Slavery, American Freedom_ (1975) tied the revolt to the rise of slavery in Virginia",
            "k": ["edmund morgan", "american slavery, american freedom", "1975"],
            "n": 0
        },
        {
            "id": "middle-plantation",
            "tier": "power",
            "t": "Treaty of Middle Plantation (1677): peace with several Native nations, including the Pamunkey, led by a woman the English called their queen",
            "k": ["middle plantation", "1677", "queen"],
            "n": 0
        },
        {
            "id": "ingram",
            "tier": "power",
            "t": "After Bacon died at age 29, Joseph Ingram led the rebels; Bacon’s body was never found",
            "k": ["joseph ingram", "ingram", "never found"],
            "n": 0
        },
        {
            "id": "jeffreys",
            "tier": "power",
            "t": "Royal commissioners, including Herbert Jeffreys, came to investigate; Jeffreys then took over the government",
            "k": ["herbert jeffreys", "jeffreys", "commissioners"],
            "n": 0
        },
        {
            "id": "grantham",
            "tier": "power",
            "t": "Ship captain Thomas Grantham talked the last holdouts, including enslaved Africans and servants, into surrendering",
            "k": ["thomas grantham", "grantham", "surrendering"],
            "n": 0
        },
        {
            "id": "newcomer",
            "tier": "power",
            "t": "Bacon arrived in Virginia in 1674 and got a seat on the governor’s council; his overseer was killed in a 1676 raid",
            "k": ["1674", "council", "overseer"],
            "n": 0
        },
        {
            "id": "forts",
            "tier": "power",
            "t": "Berkeley wanted expensive frontier forts instead of attacks; settlers suspected he was protecting his friends’ fur trade",
            "k": ["forts", "fur trade"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Rebel or rebellion?",
        "body": "Nathaniel Bacon is the man and Bacon’s Rebellion is the event, so saying just his name earns only a prompt. Players also mix up colonial uprisings: Bacon’s Rebellion (1676, Virginia) is different from Leisler’s Rebellion (1689–1691, New York), the Stono Rebellion (1739, South Carolina), Shays’ Rebellion (1786–1787, Massachusetts), and the Whiskey Rebellion (1791–1794, Pennsylvania). King Philip’s War was raging in New England at the same time, but it was a separate conflict.",
        "fix": "Virginia, 1676, Governor William Berkeley, frontier attacks on Native peoples, and the burning of Jamestown mean Bacon’s Rebellion. If you are prompted after saying “Bacon,” add “Rebellion.”",
        "line": "Real answer line: <b><u>Bacon’s Rebellion</u></b> (prompt on <u>Bacon</u> or <u>Nathaniel Bacon</u>)"
    },
    "tests": {
        "right": [
            "Bacon's Rebellion",
            "Bacon Rebellion",
            "Bacons Rebelion",
            "Nathaniel Bacon's Rebellion",
            "Bacon's Revolt"
        ],
        "prompt": [
            "Bacon",
            "Nathaniel Bacon"
        ],
        "wrong": [
            "Shays' Rebellion",
            "Whiskey Rebellion",
            "Leisler's Rebellion",
            "King Philip's War",
            "Francis Bacon",
            "Jamestown",
            "Stono Rebellion"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("wrote", data["id"])
