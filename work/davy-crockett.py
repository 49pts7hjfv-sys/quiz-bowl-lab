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
    "id": "davy-crockett",
    "name": "Davy Crockett",
    "mono": "DCR",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "Tennessee frontiersman and congressman · Died defending the Alamo",
    "dates": "1786–1836",
    "briefing": "Davy Crockett was a real Tennessee frontiersman who became a legend while he was still alive. He scouted in the Creek War, served three terms in Congress, and broke with President Andrew Jackson by voting against the Indian Removal Act. After losing his seat, he went to Texas and died at the Alamo in 1836. A 1950s Disney TV show called him the “King of the Wild Frontier” and set off a craze for coonskin caps.",
    "answerHtml": "David “Davy” <b><u>Crockett</u></b>",
    "accept": [
        "davy crockett",
        "david crockett",
        "crockett",
        "dave crockett",
        "david davy crockett"
    ],
    "prompt": [
        "davy",
        "david",
        "king of the wild frontier"
    ],
    "reject": [
        "battle of the alamo",
        "the alamo",
        "alamo",
        "jim bowie",
        "james bowie",
        "bowie",
        "william travis",
        "william b travis",
        "travis",
        "sam houston",
        "houston",
        "daniel boone",
        "boone",
        "kit carson",
        "fess parker",
        "santa anna",
        "antonio lopez de santa anna",
        "andrew jackson",
        "adam huntsman",
        "james bonham",
        "johnny appleseed",
        "paul bunyan",
        "pecos bill"
    ],
    "tests": {
        "right": [
            "Davy Crockett",
            "David Crockett",
            "Crockett",
            "Davey Crockett"
        ],
        "prompt": [
            "Davy"
        ],
        "wrong": [
            "Daniel Boone",
            "Jim Bowie",
            "William Travis",
            "Sam Houston",
            "The Alamo"
        ]
    },
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Davy_Crockett",
    "qb": {
        "q": "Crockett",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        T("James Kirke Paulding’s play _The Lion of the West_ starred Colonel Nimrod Wildfire, a loud, boastful backwoodsman whom audiences took to be a portrait of this congressman. The play helped make this man a national celebrity in the early 1830s.",
          "A Disney show later called him the “King of the Wild Frontier.” For 10 points, name this Tennessee frontiersman who died at the Alamo."),
        T("This man lost his 1835 reelection race to Adam Huntsman, a lawyer with a wooden leg who supported President Andrew Jackson. Four years earlier, he had also lost his seat after breaking with Jackson.",
          "After his 1835 defeat, he left for Texas. For 10 points, name this congressman who died at the Alamo."),
        T("In the Tennessee legislature and in Congress, this man fought for poor squatters in the western part of his state, hoping to let them buy the land they farmed cheaply. He first won a seat in the state legislature in 1821.",
          "He later died at the Alamo. For 10 points, name this frontiersman nicknamed the “King of the Wild Frontier.”"),
        T("In 1834, Whig politicians sponsored this man’s speaking tour of Northern cities such as Philadelphia, New York, and Boston, hoping to use his fame against President Andrew Jackson. That same year, he published an autobiography.",
          "For 10 points, name this Tennessee congressman and frontiersman who died at the Alamo in 1836."),
        T("Breaking with President Andrew Jackson, this Tennessee congressman voted against the Indian Removal Act in 1830. Years earlier, he had served as a scout under Jackson’s command in the Creek War.",
          "A 1950s Disney show later made him a hero to a new generation. For 10 points, name this frontiersman who died defending the Alamo."),
        T("This hunter claimed in his autobiography to have killed more than a hundred bears in less than a year. He represented western Tennessee in Congress for three terms, though not all in a row.",
          "A popular song says he “kilt him a b’ar when he was only three.” For 10 points, name this frontiersman who died at the Alamo."),
        T("This man’s 1834 autobiography, written while he served in Congress, includes his motto, “Be always sure you’re right, then go ahead.” The book tells of his childhood, his hunting trips, and his service in the Creek War.",
          "For 10 points, name this Tennessee frontiersman who died at the Alamo in 1836."),
        T("Tall tales in almanacs bearing this man’s name claimed he could grin a raccoon out of a tree and once came home with a piece of sunrise in his pocket. Those almanacs kept appearing for about twenty years after his death.",
          "For 10 points, name this real frontiersman from Tennessee who died at the Alamo."),
        T("In a 1950s Disney TV series, Fess Parker played this man and Buddy Ebsen played his friend George Russel. Disney later edited the show’s first three episodes into a 1955 movie.",
          "The show set off a craze for coonskin caps. For 10 points, name this “King of the Wild Frontier,” who died at the Alamo."),
        T("John Wayne directed and starred as this man in a 1960 film shot on a replica set near Brackettville, Texas, and Billy Bob Thornton played him in a 2004 film about the same battle.",
          "He reached that battle’s fort in February 1836. For 10 points, name this frontiersman who died at the Alamo."),
        T("This man was born in 1786 near the Nolichucky [“nah-lih-CHUH-kee”] River, in what is now Greene County in the eastern part of his state. He later moved west, and voters there sent him to the state legislature and then to Congress.",
          "He was later called the “King of the Wild Frontier.” For 10 points, name this Tennessee congressman who died at the Alamo."),
        T("A national forest in East Texas is named for this man, as are counties in both Texas and Tennessee. He had moved to Texas after his political career in Tennessee ended.",
          "For 10 points, name this frontiersman who died defending the Alamo against Antonio López de Santa Anna’s Mexican army."),
        T("In a January 1836 letter to his family, this man called Texas “the garden spot of the world.” That same month, he signed an oath of loyalty to the provisional government of Texas.",
          "For 10 points, name this frontiersman, known as the “King of the Wild Frontier,” who died weeks later at the Alamo."),
        T("This man married Polly Finley in 1806, and after her death he married Elizabeth Patton, a widow. He moved his family several times, finally settling in western Tennessee, where he hunted bears.",
          "After leaving Congress, he went to Texas. For 10 points, name this frontiersman who died at the Alamo."),
        T("Bill Hayes’s recording of a song about this man reached number one on the pop charts in 1955, and Fess Parker, who played him on television, also recorded it. The song was written for a Disney TV show, and several other singers recorded it too.",
          "That song begins “Born on a mountain top in Tennessee.” For 10 points, name this frontiersman who died at the Alamo.")
    ],
    "clues": [
        C("alamo", "giveaway",
          "Died defending the Alamo in San Antonio, Texas, in March 1836",
          ["alamo", "san antonio", "1836"], "Battle of the Alamo"),
        C("frontiersman", "giveaway",
          "Frontiersman and congressman from Tennessee",
          ["frontiersman", "tennessee", "congressman"]),
        C("wild-frontier", "giveaway",
          "Called the “King of the Wild Frontier” in a 1950s Disney TV show and its hit theme song",
          ["king of the wild frontier", "wild frontier", "disney"]),
        C("coonskin", "giveaway",
          "The Disney show set off a craze for coonskin caps, made of raccoon fur",
          ["coonskin", "raccoon"]),
        C("removal-vote", "middle",
          "Broke with Andrew Jackson by voting against the Indian Removal Act (1830)",
          ["indian removal act", "andrew jackson", "1830"], "Trail of Tears"),
        C("creek-war", "middle",
          "Served as a scout under Andrew Jackson’s command in the Creek War (1813–1814)",
          ["creek war", "scout"]),
        C("motto", "middle",
          "His motto: “Be always sure you’re right, then go ahead”",
          ["sure you’re right", "go ahead", "motto"]),
        C("autobiography", "middle",
          "Published an autobiography in 1834, while serving his third term in Congress",
          ["autobiography", "1834", "third term"]),
        C("lost-seat", "middle",
          "Lost his seat in Congress in 1831 and again in 1835, then left for Texas",
          ["1831", "1835", "texas"]),
        C("tall-tales", "middle",
          "Hero of tall tales in comic almanacs (from 1835): he could grin a raccoon out of a tree",
          ["tall tales", "almanacs", "grin"]),
        C("bowie-travis", "middle",
          "Died at the Alamo alongside Jim Bowie and William Travis, fighting Santa Anna’s Mexican army",
          ["jim bowie", "bowie", "william travis", "travis", "santa anna"], "Antonio López de Santa Anna"),
        C("song", "middle",
          "The Disney song begins “Born on a mountain top in Tennessee” and says he “kilt him a b’ar when he was only three”",
          ["mountain top", "kilt him a b’ar", "b’ar"]),
        C("lion-of-the-west", "power",
          "James Kirke Paulding’s play _The Lion of the West_ starred Colonel Nimrod Wildfire, a character audiences linked to him",
          ["lion of the west", "nimrod wildfire", "paulding"]),
        C("huntsman", "power",
          "Lost his 1835 race to Adam Huntsman, a Jackson supporter with a wooden leg",
          ["adam huntsman", "huntsman", "wooden leg"]),
        C("squatters", "power",
          "Elected to the Tennessee legislature in 1821; fought for poor squatters in western Tennessee to buy the land they farmed",
          ["squatters", "legislature", "1821"]),
        C("whig-tour", "power",
          "Whig politicians sponsored his 1834 speaking tour of Northern cities like Philadelphia, New York, and Boston",
          ["whig", "speaking tour", "philadelphia"]),
        C("disney-cast", "power",
          "Fess Parker played him on TV, with Buddy Ebsen as his friend George Russel; the episodes became a 1955 movie",
          ["fess parker", "buddy ebsen", "george russel"]),
        C("hayes", "power",
          "Bill Hayes’s recording of the Disney song about him reached No. 1 in 1955",
          ["bill hayes", "1955"]),
        C("films", "power",
          "John Wayne directed and starred as him in a 1960 film shot near Brackettville, Texas; Billy Bob Thornton played him in 2004",
          ["john wayne", "billy bob thornton", "brackettville"]),
        C("bears", "power",
          "Claimed in his autobiography to have killed more than 100 bears in less than a year",
          ["bears", "100 bears"]),
        C("birthplace", "power",
          "Born in 1786 near the Nolichucky River, in today’s Greene County, Tennessee",
          ["nolichucky", "greene county", "1786"]),
        C("garden-spot", "power",
          "In January 1836, called Texas “the garden spot of the world” and signed an oath of loyalty to its provisional government",
          ["garden spot", "january 1836", "oath"]),
        C("forest", "power",
          "A national forest in East Texas and counties in Texas and Tennessee are named for him",
          ["national forest", "east texas", "counties"]),
        C("marriages", "power",
          "Married Polly Finley in 1806 and later the widow Elizabeth Patton",
          ["polly finley", "elizabeth patton"])
    ],
    "trap": {
        "title": "Crockett, Boone, or Bowie?",
        "body": "Fess Parker played both Davy Crockett and Daniel Boone on TV in a coonskin cap, so the two frontiersmen get mixed up. Boone explored Kentucky through the Cumberland Gap and founded Boonesborough; Crockett was a Tennessee congressman who died at the Alamo. At the Alamo itself, Crockett died alongside Jim Bowie, of the Bowie knife, and William Travis, who commanded the Texan defenders, and some tossups ask for the battle instead of the man.",
        "fix": "Tennessee, Congress, the vote against the Indian Removal Act, and “King of the Wild Frontier” mean Crockett. Kentucky and the Wilderness Road mean Boone. The famous knife means Bowie, and the “Victory or Death” letter means Travis. If the question says “this battle,” answer the Alamo.",
        "line": "Real answer line: David “Davy” <b><u>Crockett</u></b>"
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
