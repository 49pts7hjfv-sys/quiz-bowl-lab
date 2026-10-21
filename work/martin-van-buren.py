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
    "id": "martin-van-buren",
    "name": "Martin Van Buren",
    "mono": "MVB",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "8th U.S. President · Andrew Jackson’s vice president and the “Little Magician”",
    "dates": "1782–1862",
    "briefing": "Martin Van Buren, born in 1782 in the Dutch-speaking village of Kinderhook, New York, was the first president born a citizen of the United States instead of a British subject. A master politician nicknamed the “Little Magician,” he helped build the Democratic Party and served as Andrew Jackson’s vice president before winning the presidency in 1836. The Panic of 1837 hit just weeks after he took office, and voters turned him out four years later.",
    "answerHtml": "Martin <b><u>Van Buren</u></b> (do not accept “Andrew Jackson” or “William Henry Harrison”)",
    "accept": [
        "martin van buren",
        "van buren",
        "vanburen",
        "martin vanburen",
        "president van buren",
        "m van buren"
    ],
    "prompt": [
        "martin",
        "little magician",
        "the little magician",
        "old kinderhook"
    ],
    "reject": [
        "andrew jackson",
        "jackson",
        "william henry harrison",
        "harrison",
        "john tyler",
        "tyler",
        "james k polk",
        "polk",
        "zachary taylor",
        "taylor",
        "john c calhoun",
        "calhoun",
        "richard mentor johnson",
        "richard m johnson",
        "dewitt clinton",
        "george clinton",
        "william marcy",
        "william l marcy",
        "hannah van buren",
        "hannah hoes",
        "angelica van buren",
        "angelica singleton",
        "abraham van buren",
        "john van buren",
        "smith van buren",
        "lewis cass",
        "charles francis adams",
        "free soil party",
        "martin luther",
        "martin luther king",
        "martin luther king jr",
        "james buchanan",
        "buchanan",
        "millard fillmore",
        "john quincy adams",
        "henry clay",
        "daniel webster",
        "hugh lawson white",
        "kinderhook",
        "rip van winkle",
        "washington irving",
        "peggy eaton",
        "john eaton"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Martin_Van_Buren",
    "qb": {
        "q": "Van Buren",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {"n": 0, "note": "no real tossups checked yet"},
    "tossups": [
        T("In 1832, Vice President John C. Calhoun broke a tie to block this man’s appointment as minister to Great Britain, a snub that backfired and won this man sympathy. A year earlier, this man had resigned as Secretary of State during the Petticoat Affair.",
          "Later that year he was elected Andrew Jackson’s vice president. For 10 points, name this New Yorker who became the eighth president."),
        T("William Marcy, a member of this man’s political machine called the Albany Regency, defended the spoils system by declaring that “to the victor belong the spoils.” This man’s faction, the Bucktails, had earlier fought New York governor DeWitt Clinton for control of the state.",
          "For 10 points, name this New York politician nicknamed the “Little Magician,” who became the eighth president."),
        T("In an 1827 letter to Virginia newspaper editor Thomas Ritchie, this man proposed rebuilding an alliance between “the planters of the South and the plain Republicans of the North.” That plan helped create the party that elected Andrew Jackson president the next year.",
          "That party became the Democrats. For 10 points, name this New Yorker who succeeded Jackson as president in 1837."),
        T("In one election, this man defeated several regional candidates from a new opposition party, including William Henry Harrison, Hugh Lawson White, and Daniel Webster. His running mate, Richard Mentor Johnson, fell short of an electoral majority and became the only vice president ever chosen by the Senate.",
          "For 10 points, name this Democrat who won the election of 1836, becoming the eighth president of the United States."),
        T("Just weeks after this man took office, banks in New York stopped paying out gold and silver, setting off a depression that lasted for years. Many people blamed his predecessor’s Specie Circular, which had required buyers of public land to pay in gold or silver.",
          "That crisis was the Panic of 1837. For 10 points, name this president, mocked as “Martin Van Ruin.”"),
        T("This president’s answer to a financial crisis was to keep federal money in government vaults instead of private banks, a “divorce” of the government from the banks. He signed the act creating that system on July 4, 1840, but the Whigs repealed it the next year.",
          "That system was called the Independent Treasury. For 10 points, name this president who faced the Panic of 1837."),
        T("After British and Canadian forces set fire to the American steamboat _Caroline_ on the Niagara River in 1837, this president sent General Winfield Scott to calm the border. Scott also helped end the bloodless Aroostook [“uh-ROO-stuk”] War, a dispute over timberland between Maine and New Brunswick, during this man’s term.",
          "For 10 points, name this one-term president, who served between Andrew Jackson and William Henry Harrison in the late 1830s."),
        T("This president’s administration argued that Africans who had taken over the Spanish ship _La Amistad_ should be handed over to Spanish authorities in Cuba. In 1841, days after he left office, John Quincy Adams won their freedom before the Supreme Court.",
          "For 10 points, name this president, who had lost his bid for reelection to William Henry Harrison."),
        T("Ralph Waldo Emerson wrote an open letter in 1838 pleading with this president not to enforce a removal treaty, but that year soldiers under General Winfield Scott forced thousands of Cherokee people out of their homes and onto the road west. Most of them did not reach Indian Territory until early 1839.",
          "That forced march became known as the Trail of Tears. For 10 points, name this president, who had been Andrew Jackson’s vice president."),
        T("Pennsylvania congressman Charles Ogle attacked this president in the 1840 “Gold Spoon Oration,” claiming that he lived like a king in a lavishly decorated White House. That year, his opponents portrayed their own candidate as a plain man of log cabins and hard cider.",
          "Whigs chanted “Van, Van, is a used-up man.” For 10 points, name this president who lost to William Henry Harrison in 1840."),
        T("Supporters of this man formed “O.K. Clubs” in 1840, named for his nickname “Old Kinderhook,” which helped spread a popular two-letter expression. He grew up speaking Dutch in his New York hometown, where his father ran a tavern.",
          "He was the first president born a citizen of the United States. For 10 points, name this eighth president."),
        T("In 1844, this former president lost the support of many Southern Democrats when he published a letter opposing the immediate annexation of Texas. Unable to win two-thirds of the delegates at his party’s convention, he lost the nomination to the dark horse James K. Polk.",
          "For 10 points, name this New Yorker, who had served one term as president from 1837 to 1841."),
        T("In 1848, this former president ran again with Charles Francis Adams as his running mate, winning about ten percent of the popular vote but no electoral votes. Antislavery New York Democrats nicknamed “Barnburners” backed that campaign, which split the Democratic vote and may have helped Zachary Taylor win.",
          "He ran as the candidate of the Free Soil Party. For 10 points, name this man who had been the eighth president."),
        T("In 1840, this president ordered a ten-hour workday for laborers on federal public works projects. Earlier in his term, he turned down the Republic of Texas’s request to join the United States, fearing a war with Mexico and a fight over slavery.",
          "For 10 points, name this eighth president, whose term began with the Panic of 1837."),
        T("Because this president’s wife, Hannah, had died in 1819, his daughter-in-law Angelica Singleton, a relative of Dolley Madison, served as White House hostess. In retirement, he lived at Lindenwald, his estate in Kinderhook, New York, where he died in 1862.",
          "For 10 points, name this eighth president, known for his bushy sideburns and the nickname “the Little Magician.”")
    ],
    "clues": [
        C("eighth", "giveaway", "8th President (1837–1841), a Democrat from New York",
          ["8th president", "eighth", "democrat"]),
        C("jackson-vp", "giveaway", "Andrew Jackson’s second vice president (1833–1837) and chosen successor",
          ["andrew jackson", "jackson", "vice president"], "Andrew Jackson"),
        C("panic", "giveaway", "President during the Panic of 1837, which began weeks after he took office; critics called him “Martin Van Ruin”",
          ["panic of 1837", "1837", "panic"]),
        C("first-citizen", "giveaway", "The first president born a citizen of the United States (1782) instead of a British subject",
          ["first president", "citizen", "1782"]),
        C("little-magician", "giveaway", "Nicknamed the “Little Magician” for his political skill",
          ["little magician", "magician"]),
        C("kinderhook", "middle", "Grew up speaking Dutch in Kinderhook, New York, where his father ran a tavern",
          ["kinderhook", "dutch", "tavern"]),
        C("independent-treasury", "middle", "Created the Independent Treasury (1840) to keep federal money in government vaults instead of banks",
          ["independent treasury", "vaults", "1840"]),
        C("trail-of-tears", "middle", "The Cherokee were forced west on the Trail of Tears (1838–1839) during his presidency",
          ["trail of tears", "cherokee", "1838"], "Trail of Tears"),
        C("harrison-1840", "middle", "Lost the 1840 election to William Henry Harrison’s log-cabin campaign",
          ["william henry harrison", "log-cabin", "1840"], "William Henry Harrison"),
        C("free-soil", "middle", "Free Soil Party candidate in 1848, with Charles Francis Adams; antislavery “Barnburners” backed him",
          ["free soil", "charles francis adams", "barnburners", "1848"], "Free Soil Party"),
        C("ok", "middle", "His nickname “Old Kinderhook” helped spread the expression “OK” (O.K. Clubs, 1840)",
          ["old kinderhook", "o.k. clubs"]),
        C("petticoat", "middle", "Resigned as Secretary of State (1831) during the Petticoat Affair",
          ["petticoat", "secretary of state", "1831"]),
        C("albany-regency", "middle", "Built a New York political machine called the Albany Regency",
          ["albany regency", "machine"]),
        C("democrats", "middle", "Helped organize the Democratic Party around Andrew Jackson in the late 1820s",
          ["democratic party", "organize"], "Democratic Party"),
        C("calhoun", "power", "Vice President John C. Calhoun’s tie-breaking vote rejected him as minister to Great Britain (1832)",
          ["calhoun", "minister to great britain", "tie-breaking"]),
        C("marcy", "power", "Regency member William Marcy: “to the victor belong the spoils”",
          ["marcy", "spoils"]),
        C("bucktails", "power", "His Bucktails faction fought Governor DeWitt Clinton",
          ["bucktails", "dewitt clinton"]),
        C("ritchie", "power", "1827 letter to Thomas Ritchie: unite “the planters of the South and the plain Republicans of the North”",
          ["ritchie", "planters of the south"]),
        C("regional-whigs", "power", "Beat several regional Whig candidates in 1836, including Hugh Lawson White and Daniel Webster",
          ["hugh lawson white", "regional", "1836"]),
        C("rm-johnson", "power", "Running mate Richard Mentor Johnson became the only vice president chosen by the Senate (1837)",
          ["richard mentor johnson", "senate"]),
        C("specie", "power", "Many blamed Jackson’s Specie Circular (1836), which required gold or silver for public land",
          ["specie circular", "gold or silver"]),
        C("caroline", "power", "Sent Winfield Scott to the border after the steamboat _Caroline_ was burned (1837); the Aroostook War with New Brunswick ended peacefully",
          ["caroline", "aroostook", "winfield scott"]),
        C("amistad", "power", "His administration wanted the _Amistad_ Africans handed over to Spanish authorities",
          ["amistad", "spanish authorities"], "John Quincy Adams"),
        C("emerson", "power", "Ralph Waldo Emerson’s 1838 open letter begged him not to remove the Cherokee",
          ["emerson", "open letter"]),
        C("gold-spoon", "power", "Charles Ogle’s “Gold Spoon Oration” (1840) attacked his White House lifestyle; Whigs chanted “Van, Van, is a used-up man”",
          ["gold spoon", "ogle", "used-up man"]),
        C("texas-1844", "power", "Opposed annexing Texas in 1844 and lost the Democratic nomination to dark horse James K. Polk",
          ["texas", "dark horse", "james k. polk"]),
        C("ten-hour", "power", "Ordered a ten-hour day for laborers on federal public works (1840); refused Texas’s request to join (1837)",
          ["ten-hour", "public works"]),
        C("lindenwald", "power", "Retired to Lindenwald in Kinderhook; daughter-in-law Angelica Singleton was White House hostess",
          ["lindenwald", "angelica singleton"])
    ],
    "trap": {
        "title": "Jackson’s heir, not Jackson",
        "body": "Van Buren spent his career at Andrew Jackson’s side as secretary of state, vice president, and chosen successor, so his tossups are full of Jackson clues like the Petticoat Affair, the Bank War, and Indian removal. The Trail of Tears is a common trap: Jackson signed the Indian Removal Act in 1830, but most Cherokees were forced west in 1838–1839, while Van Buren was president. William Henry Harrison, who beat him in 1840, is another wrong buzz.",
        "fix": "The Panic of 1837, the Independent Treasury, the _Caroline_ and _Amistad_ affairs, Kinderhook, and the 1848 Free Soil run mean Van Buren. Vetoing the national bank’s recharter, the Battle of New Orleans, and signing the Indian Removal Act mean Jackson.",
        "line": "Real answer line: Martin <b><u>Van Buren</u></b> (do not accept “Andrew Jackson”)"
    },
    "tests": {
        "right": [
            "Martin Van Buren",
            "Van Buren",
            "vanburen",
            "Martin Van Buran",
            "President Van Buren"
        ],
        "prompt": [
            "Martin",
            "Little Magician"
        ],
        "wrong": [
            "Andrew Jackson",
            "William Henry Harrison",
            "John C. Calhoun",
            "James K. Polk",
            "Martin Luther",
            "Richard Mentor Johnson",
            "Hannah Van Buren"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
