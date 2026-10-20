import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def T(p, r):
    return {"p": p, "r": r}


def C(cid, tier, t, k, rabbit=None):
    c = {"id": cid, "tier": tier, "t": t, "k": k, "n": 0}
    if rabbit:
        c["rabbit"] = rabbit
    return c


data = {
    "id": "henry-clay",
    "name": "Henry Clay",
    "mono": "HC",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "Kentucky senator and Speaker · Nicknamed “the Great Compromiser”",
    "dates": "1777–1852",
    "briefing": "Henry Clay of Kentucky was such a skilled deal-maker that he earned the nickname “the Great Compromiser.” He helped hold the Union together three times, with the Missouri Compromise, the Compromise Tariff of 1833, and the Compromise of 1850. He ran for president three times and lost every time, famously saying, “I would rather be right than be president.”",
    "answerHtml": "Henry <b><u>Clay</u></b> (accept <u>Henry Clay Sr.</u>)",
    "accept": [
        "henry clay",
        "clay",
        "henry clay sr",
        "henry clay senior"
    ],
    "prompt": [
        "henry",
        "great compromiser",
        "the great compromiser",
        "harry of the west"
    ],
    "reject": [
        "henry clay frick",
        "frick",
        "henry clay jr",
        "henry clay junior",
        "henry clay pate",
        "cassius clay",
        "cassius marcellus clay",
        "lucius clay",
        "lucius d clay",
        "daniel webster",
        "webster",
        "john c calhoun",
        "calhoun",
        "andrew jackson",
        "john quincy adams",
        "patrick henry",
        "stephen douglas",
        "james k polk",
        "william henry harrison",
        "zachary taylor",
        "john randolph"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Henry_Clay",
    "qb": {
        "q": "Henry Clay",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {"n": 0, "note": "no real tossups checked yet"},
    "tossups": [
        T("This man was appointed to the U.S. Senate in 1806 even though, at 29, he was younger than the Constitution allows. When he moved to the House of Representatives in 1811, he was elected Speaker on his very first day.",
          "He later earned the nickname “the Great Compromiser.” For 10 points, name this Kentucky senator who proposed the Compromise of 1850."),
        T("Senator John Randolph of Roanoke insulted this man so harshly that the two fought a duel in 1826, though neither was hurt. Randolph was angry about the election of 1824, in which this man finished fourth but then helped John Quincy Adams win in the House.",
          "Adams then made him Secretary of State, a deal Andrew Jackson called a “corrupt bargain.” For 10 points, name this Kentuckian known as the Great Compromiser."),
        T("In one election, this man’s supporters taunted voters by asking, “Who is James K. Polk?” His “Raleigh letter” opposing the immediate annexation of Texas cost him support, and he narrowly lost that 1844 race to Polk.",
          "For 10 points, name this Whig leader and longtime Kentucky senator who proposed the Compromise of 1850."),
        T("Abraham Lincoln called this man “my beau ideal of a statesman” and delivered a eulogy for him in Springfield in 1852. That year, this man became the first person to lie in state in the Rotunda of the U.S. Capitol.",
          "He had earned the nickname “the Great Compromiser.” For 10 points, name this Whig senator from Kentucky."),
        T("This senator’s “Omnibus Bill” fell apart in the summer of 1850 when opponents picked it to pieces. Stephen Douglas then split it into separate bills and got them passed after President Zachary Taylor died.",
          "Those bills admitted California as a free state and passed a stricter Fugitive Slave Act. For 10 points, name this Great Compromiser from Kentucky."),
        T("In 1830, Andrew Jackson vetoed federal money for the Maysville Road, which would have run from the Ohio River to this man’s home city of Lexington, because it lay entirely within one state. The veto was a blow to this rival’s plans for federal roads and canals.",
          "Those plans were part of his American System. For 10 points, name this Kentucky senator, the Great Compromiser."),
        T("This man joined John Quincy Adams and Albert Gallatin as an American negotiator of the Treaty of Ghent, which ended the War of 1812. Before that war, he and John C. Calhoun led the “War Hawks” who pushed Congress to fight Britain.",
          "For 10 points, name this Kentuckian who later helped pass the Missouri Compromise and the Compromise of 1850."),
        T("This man and John C. Calhoun worked out the Compromise Tariff of 1833, which slowly lowered tariff rates and ended the Nullification Crisis with South Carolina. Andrew Jackson had threatened force against that state, which had tried to cancel federal tariffs.",
          "This man had also pushed high tariffs as part of his American System. For 10 points, name this Kentucky senator nicknamed “the Great Compromiser.”"),
        T("This senator introduced the 1834 resolution in which the Senate censured Andrew Jackson for removing federal money from the Second Bank of the United States. Anger at “King Andrew” led this man and Daniel Webster to found the Whig Party.",
          "He ran as the Whig nominee for president in 1844. For 10 points, name this Kentucky politician known as the Great Compromiser."),
        T("In 1832, this man urged the Second Bank of the United States to seek a new charter four years early so he could make the bank a campaign issue. Andrew Jackson vetoed the recharter bill and then defeated this man in that year’s presidential election.",
          "For 10 points, name this Kentucky senator, later a leader of the Whig Party, known as the Great Compromiser."),
        T("This man presided over the first meeting of the American Colonization Society in 1816, a group that later helped found Liberia as a home for free Black Americans. He also enslaved dozens of people at his estate, Ashland.",
          "He later served as that society’s president. For 10 points, name this Kentucky senator known as the Great Compromiser."),
        T("In 1821, this man worked out a deal over a clause in a new state’s constitution that tried to keep free Black people from moving there. A year earlier, as Speaker of the House, he had helped pass a compromise that admitted Maine as a free state.",
          "That deal was the Missouri Compromise. For 10 points, name this Kentucky politician known as the Great Compromiser."),
        T("Told that a speech criticizing abolitionists might cost him the presidency, this man replied, “I would rather be right than be president.” He ran for president three times, in 1824, 1832, and 1844, and lost every time.",
          "For 10 points, name this Kentucky senator who helped work out the Missouri Compromise and the Compromise of 1850."),
        T("Born in an area of Hanover County, Virginia, called the Slashes, this man later campaigned as “the Mill Boy of the Slashes.” As a young lawyer he moved west to Lexington, where he built an estate called Ashland.",
          "He later served as Speaker of the House and as Secretary of State. For 10 points, name this Kentucky senator nicknamed “the Great Compromiser.”"),
        T("Nicknamed “Harry of the West,” this senator formed the “Great Triumvirate” with Daniel Webster and John C. Calhoun. In 1850, a dying Calhoun had another senator read aloud his last major speech, which opposed this man’s plan.",
          "That plan became the Compromise of 1850. For 10 points, name this Kentuckian known as the Great Compromiser."),
    ],
    "clues": [
        C("great-compromiser", "giveaway", "Nicknamed “the Great Compromiser” for his deals between North and South", ["great compromiser", "compromiser", "north and south"]),
        C("kentucky", "giveaway", "Senator from Kentucky; his estate, Ashland, was near Lexington", ["kentucky", "ashland", "lexington"]),
        C("american-system", "giveaway", "American System: a protective tariff, a national bank, and internal improvements like roads and canals", ["american system", "protective tariff", "national bank", "internal improvements"]),
        C("compromise-1850", "giveaway", "Proposed the Compromise of 1850, which admitted California as a free state", ["compromise of 1850", "california", "1850"], "Compromise of 1850"),
        C("missouri", "middle", "As Speaker of the House, helped pass the Missouri Compromise (1820) and a second deal over Missouri’s constitution (1821)", ["missouri compromise", "1820", "1821"], "Missouri Compromise"),
        C("corrupt-bargain", "middle", "In 1824 he backed John Quincy Adams in the House and became his Secretary of State; Jackson called it a “corrupt bargain”", ["corrupt bargain", "john quincy adams", "secretary of state", "1824"], "John Quincy Adams"),
        C("speaker", "middle", "Elected Speaker of the House on his very first day as a congressman (1811)", ["speaker", "first day", "1811"]),
        C("war-hawks", "middle", "Led the “War Hawks” with John C. Calhoun before the War of 1812, then helped negotiate the Treaty of Ghent", ["war hawks", "calhoun", "ghent"], "War of 1812"),
        C("whigs", "middle", "Founded the Whig Party with Daniel Webster to oppose “King Andrew” Jackson", ["whig", "daniel webster", "king andrew"], "Daniel Webster"),
        C("rather-be-right", "middle", "Said “I would rather be right than be president” (1839)", ["rather be right", "1839"]),
        C("triumvirate", "middle", "Formed the “Great Triumvirate” of senators with Daniel Webster and John C. Calhoun", ["great triumvirate", "triumvirate"]),
        C("elections", "middle", "Lost three presidential races: 1824, 1832 (to Andrew Jackson), and 1844 (to James K. Polk)", ["three", "1832", "1844", "polk"]),
        C("under-30", "power", "Appointed to the U.S. Senate in 1806 at age 29, younger than the Constitution allows", ["1806", "younger", "age 29"]),
        C("randolph", "power", "Fought a duel with Senator John Randolph of Roanoke in 1826; neither man was hurt", ["randolph", "duel", "roanoke"]),
        C("polk-raleigh", "power", "1844: Whigs mocked his opponent by asking “Who is James K. Polk?”; his Raleigh letter against annexing Texas cost him votes", ["raleigh", "texas", "annexing"]),
        C("omnibus", "power", "His “Omnibus Bill” fell apart in 1850; Stephen Douglas passed its parts as separate bills", ["omnibus", "stephen douglas", "separate bills"]),
        C("compromise-tariff", "power", "Ended the Nullification Crisis with John C. Calhoun through the Compromise Tariff of 1833", ["compromise tariff", "nullification", "1833"]),
        C("censure", "power", "Led the Senate’s 1834 censure of Andrew Jackson for removing federal money from the national bank", ["censure", "1834", "removing"], "Andrew Jackson"),
        C("bank-1832", "power", "Urged the Second Bank of the United States to seek an early recharter in 1832; Jackson vetoed it and beat him that fall", ["recharter", "second bank", "1832"]),
        C("lie-in-state", "power", "First person to lie in state in the U.S. Capitol Rotunda (1852)", ["lie in state", "rotunda", "1852"]),
        C("beau-ideal", "power", "Abraham Lincoln called him “my beau ideal of a statesman” and gave a eulogy for him in Springfield (1852)", ["beau ideal", "lincoln", "eulogy"], "Abraham Lincoln"),
        C("colonization", "power", "Presided over the first meeting of the American Colonization Society (1816), which helped found Liberia; he also enslaved dozens of people", ["colonization", "liberia", "1816"]),
        C("slashes", "power", "Born in the Slashes of Hanover County, Virginia (“the Mill Boy of the Slashes”); also nicknamed “Harry of the West”", ["slashes", "mill boy", "harry of the west", "hanover"]),
        C("fourth-1824", "power", "Finished fourth in the 1824 Electoral College vote, so the House could not choose him", ["fourth", "electoral college"]),
        C("maysville", "power", "Andrew Jackson vetoed the Maysville Road (1830), which would have run to his home city of Lexington", ["maysville", "lexington"]),
    ],
    "trap": {
        "title": "Clay, Webster, or Calhoun?",
        "body": "Henry Clay, Daniel Webster, and John C. Calhoun were the “Great Triumvirate,” three senators who argued over tariffs, the bank, and slavery for decades, and all three appear in clues about the Nullification Crisis and the Compromise of 1850. Clay also shares clues with John Quincy Adams (the “corrupt bargain” of 1824) and with his great rival, Andrew Jackson.",
        "fix": "Clay is the Kentucky deal-maker: the American System, the Missouri Compromise, the Compromise Tariff of 1833, and the Omnibus Bill. Webster is the Massachusetts speaker who said “Liberty and Union, now and forever, one and inseparable!”; Calhoun is the South Carolinian who defended nullification. Also skip Henry Clay Frick, the steel boss, and General Lucius Clay of the Berlin Airlift.",
        "line": "Real answer line: Henry <b><u>Clay</u></b> (accept <u>Henry Clay Sr.</u>)"
    },
    "tests": {
        "right": [
            "Henry Clay",
            "Clay",
            "Henry Clay Sr.",
            "Henery Clay",
            "Senator Henry Clay"
        ],
        "prompt": [
            "Henry",
            "The Great Compromiser"
        ],
        "wrong": [
            "Cassius Clay",
            "Lucius Clay",
            "Henry Clay Frick",
            "Daniel Webster",
            "John C. Calhoun",
            "Patrick Henry",
            "Henry Clay Jr."
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
