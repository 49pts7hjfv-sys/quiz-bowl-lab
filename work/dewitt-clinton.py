import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TIP = "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."

data = {
    "id": "dewitt-clinton",
    "name": "DeWitt Clinton",
    "mono": "DWC",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "New York governor and New York City mayor · Father of the Erie Canal",
    "dates": "1769–1828",
    "briefing": "When DeWitt Clinton pushed to dig a canal more than 360 miles across New York, from the Hudson River to Lake Erie, critics laughed and called it “Clinton’s Ditch.” As governor, he got it built anyway, and in 1825 he celebrated its opening by pouring a keg of Lake Erie water into the Atlantic Ocean. Earlier, he had served as mayor of New York City and run for president against James Madison.",
    "answerHtml": "<b><u>DeWitt Clinton</u></b> (prompt on <u>Clinton</u>; do not accept “George Clinton,” “Bill Clinton,” “Erie Canal,” or “Clinton’s Ditch”)",
    "accept": [
        "dewitt clinton",
        "de witt clinton",
        "governor dewitt clinton",
        "mayor dewitt clinton"
    ],
    "prompt": [
        "clinton",
        "governor clinton",
        "mayor clinton",
        "dewitt",
        "de witt"
    ],
    "reject": [
        "george clinton",
        "governor george clinton",
        "bill clinton",
        "william clinton",
        "william jefferson clinton",
        "president clinton",
        "hillary clinton",
        "hillary rodham clinton",
        "chelsea clinton",
        "henry clinton",
        "sir henry clinton",
        "erie canal",
        "the erie canal",
        "clintons ditch",
        "clintons big ditch",
        "clintons folly",
        "big ditch",
        "castle clinton",
        "james madison",
        "martin van buren",
        "gouverneur morris",
        "daniel tompkins",
        "aaron burr",
        "john swartwout",
        "simeon de witt"
    ],
    "tests": {
        "right": [
            "DeWitt Clinton",
            "De Witt Clinton",
            "Dewitt Clinton",
            "Governor DeWitt Clinton",
            "DeWit Clinton"
        ],
        "prompt": [
            "Clinton",
            "DeWitt"
        ],
        "wrong": [
            "George Clinton",
            "Bill Clinton",
            "Erie Canal",
            "Clinton’s Ditch",
            "Hillary Clinton",
            "Henry Clinton",
            "James Madison"
        ]
    },
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/DeWitt_Clinton",
    "qb": {
        "q": "DeWitt Clinton",
        "found": 0,
        "tip": TIP
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "Martin Van Buren led a faction called the Bucktails, named for the deer tails its members wore on their hats, against this man’s followers. In 1824, this man’s enemies in the legislature removed him from a state board he had served on for years, but voters were so angry that they elected him governor that fall.",
            "r": "That board oversaw the building of the Erie Canal. For 10 points, name this New York politician."
        },
        {
            "p": "In November 1825, after riding the boat _Seneca Chief_ from Buffalo to New York City, this man poured a keg of lake water into the Atlantic Ocean. People called that ceremony the “Wedding of the Waters.”",
            "r": "The water came from Lake Erie, and the ceremony celebrated the opening of the Erie Canal. For 10 points, name this New York governor."
        },
        {
            "p": "In 1812, Federalist leaders meeting secretly in New York City agreed to back this Democratic-Republican for president instead of naming a candidate of their own. His running mate in that race was Jared Ingersoll of Pennsylvania.",
            "r": "This man lost to James Madison. For 10 points, name this New Yorker who later championed the Erie Canal as governor."
        },
        {
            "p": "This man served as mayor of New York City for most of the years from 1803 to 1815, and for part of that time he was also the state’s lieutenant governor. He had resigned from the U.S. Senate to take the mayor’s job.",
            "r": "As governor, he later pushed through the Erie Canal. For 10 points, name this New York politician."
        },
        {
            "p": "In 1805, this man helped found the Free School Society, which opened free schools for poor children in New York City. He became the society’s president while he was also serving as the city’s mayor.",
            "r": "For 10 points, name this man, later the governor of New York who championed the Erie Canal."
        },
        {
            "p": "An early steam locomotive named for this man pulled one of the first passenger trains in New York State, on the Mohawk and Hudson Railroad between Albany and Schenectady [“skuh-NEK-tuh-dee”] in 1831. This man had died three years earlier.",
            "r": "He had been governor of New York when the Erie Canal opened. For 10 points, name this politician."
        },
        {
            "p": "On July 4, 1817, just days after this man took office, workers broke ground at Rome, New York, on a project he had championed for years. Critics mocked that project as his “Big Ditch” and his “Folly.”",
            "r": "That project was the Erie Canal. For 10 points, name this New York governor."
        },
        {
            "p": "After graduating from Columbia College in 1786, this man became private secretary to his uncle, who was New York’s first governor and later served as vice president under Thomas Jefferson and James Madison.",
            "r": "That uncle was George Clinton. For 10 points, name this nephew, the New York governor who championed the Erie Canal."
        },
        {
            "p": "In 1802, this man fought a duel at Weehawken, New Jersey, with John Swartwout, a friend and ally of Aaron Burr. Swartwout was wounded, but both men survived, and this man left the U.S. Senate the next year to become a mayor.",
            "r": "For 10 points, name this New Yorker who later championed the Erie Canal as governor."
        },
        {
            "p": "In 1820, this man narrowly won reelection by defeating Daniel Tompkins, who was then serving as vice president of the United States. This man did not run again in 1822, but he won back his office two years later.",
            "r": "For 10 points, name this governor of New York who championed the Erie Canal."
        },
        {
            "p": "A fort at the southern tip of Manhattan, built just before the War of 1812, was renamed in 1815 to honor this man, then the city’s mayor. As Castle Garden, that fort later served as New York’s main station for arriving immigrants before Ellis Island opened.",
            "r": "For 10 points, name this mayor and governor who championed the Erie Canal."
        },
        {
            "p": "In one presidential election, this candidate carried every New England state except Vermont, along with New York, New Jersey, and Delaware, but he lost the electoral vote 128 to 89.",
            "r": "He lost that 1812 race to James Madison. For 10 points, name this New Yorker who later championed the Erie Canal."
        },
        {
            "p": "In 1810, this man and Gouverneur Morris were named to a state commission that traveled across western New York to study a possible route for a waterway. Years later, this man led the effort to build it.",
            "r": "That waterway became the Erie Canal. For 10 points, name this mayor of New York City and governor of New York."
        },
        {
            "p": "After this man died suddenly in office in February 1828, his longtime rival Martin Van Buren won the election to replace him. Van Buren served only about ten weeks before leaving to become Andrew Jackson’s secretary of state.",
            "r": "For 10 points, name this New York governor who championed the Erie Canal."
        },
        {
            "p": "Months before this man ran for president in 1812, his uncle died in office as vice president, the first vice president ever to do so. That uncle had also served as New York’s first governor.",
            "r": "That uncle was George Clinton. For 10 points, name this nephew, who later championed the Erie Canal as governor."
        }
    ],
    "clues": [
        {
            "id": "erie-canal",
            "tier": "giveaway",
            "t": "Championed the Erie Canal, a waterway of more than 360 miles across New York State",
            "k": ["erie canal", "360 miles", "waterway"],
            "n": 0,
            "rabbit": "Erie Canal"
        },
        {
            "id": "canal-route",
            "tier": "giveaway",
            "t": "The canal opened in 1825, linking the Hudson River at Albany with Lake Erie at Buffalo",
            "k": ["1825", "hudson river", "lake erie", "buffalo", "albany"],
            "n": 0
        },
        {
            "id": "governor",
            "tier": "giveaway",
            "t": "Governor of New York (1817–1822 and 1825–1828)",
            "k": ["governor", "new york", "1817"],
            "n": 0,
            "rabbit": "New York"
        },
        {
            "id": "big-ditch",
            "tier": "middle",
            "t": "Critics mocked the canal as his “Ditch,” his “Big Ditch,” or his “Folly”",
            "k": ["big ditch", "ditch", "folly"],
            "n": 0
        },
        {
            "id": "wedding",
            "tier": "middle",
            "t": "“Wedding of the Waters” (1825): rode the _Seneca Chief_ to New York City and poured a keg of Lake Erie water into the Atlantic",
            "k": ["wedding of the waters", "seneca chief", "keg"],
            "n": 0
        },
        {
            "id": "mayor",
            "tier": "middle",
            "t": "Mayor of New York City for most of the years from 1803 to 1815",
            "k": ["mayor", "new york city"],
            "n": 0
        },
        {
            "id": "election-1812",
            "tier": "middle",
            "t": "Lost the 1812 presidential election to James Madison, 128 electoral votes to 89",
            "k": ["1812", "james madison", "madison"],
            "n": 0,
            "rabbit": "James Madison"
        },
        {
            "id": "uncle",
            "tier": "middle",
            "t": "Nephew of George Clinton, New York’s first governor and vice president under Jefferson and Madison",
            "k": ["nephew", "uncle", "george"],
            "n": 0
        },
        {
            "id": "federalists-1812",
            "tier": "middle",
            "t": "In 1812, Federalists backed him, a Democratic-Republican, as did Republicans who opposed the War of 1812",
            "k": ["federalists", "war of 1812"],
            "n": 0
        },
        {
            "id": "bucktails",
            "tier": "middle",
            "t": "Martin Van Buren’s faction, the Bucktails, led the opposition to his followers in New York",
            "k": ["bucktails", "van buren"],
            "n": 0
        },
        {
            "id": "removed-1824",
            "tier": "middle",
            "t": "His enemies removed him from the canal commission in 1824; the backlash helped him win back the governorship that year",
            "k": ["canal commission", "1824", "removed"],
            "n": 0
        },
        {
            "id": "free-school",
            "tier": "power",
            "t": "Helped found the Free School Society (1805), which opened free schools for poor children in New York City",
            "k": ["free school society", "1805", "poor children"],
            "n": 0
        },
        {
            "id": "locomotive",
            "tier": "power",
            "t": "An early steam locomotive named for him ran on the Mohawk and Hudson Railroad (1831)",
            "k": ["locomotive", "mohawk and hudson", "1831"],
            "n": 0
        },
        {
            "id": "rome-1817",
            "tier": "power",
            "t": "Ground was broken for the canal at Rome, New York, on July 4, 1817, days after he took office",
            "k": ["rome", "july 4, 1817"],
            "n": 0
        },
        {
            "id": "secretary",
            "tier": "power",
            "t": "Graduated from Columbia College (1786), then became private secretary to his uncle, the governor",
            "k": ["private secretary", "columbia", "1786"],
            "n": 0
        },
        {
            "id": "swartwout",
            "tier": "power",
            "t": "Fought a duel with John Swartwout, an ally of Aaron Burr, at Weehawken (1802); both men survived",
            "k": ["swartwout", "weehawken", "duel"],
            "n": 0
        },
        {
            "id": "tompkins",
            "tier": "power",
            "t": "Won reelection in 1820 by narrowly defeating Vice President Daniel Tompkins",
            "k": ["daniel tompkins", "tompkins", "1820"],
            "n": 0
        },
        {
            "id": "castle-garden",
            "tier": "power",
            "t": "A fort at Manhattan’s southern tip was renamed for him in 1815; as Castle Garden, it became an immigration station before Ellis Island",
            "k": ["castle garden", "1815", "ellis island"],
            "n": 0
        },
        {
            "id": "ingersoll",
            "tier": "power",
            "t": "Federalist leaders met secretly in New York City to back him in 1812; his running mate was Jared Ingersoll",
            "k": ["jared ingersoll", "ingersoll", "secretly"],
            "n": 0
        },
        {
            "id": "electoral-map",
            "tier": "power",
            "t": "In 1812, he carried New England (except Vermont), New York, New Jersey, and Delaware",
            "k": ["vermont", "new england", "delaware"],
            "n": 0
        },
        {
            "id": "morris",
            "tier": "power",
            "t": "Served with Gouverneur Morris on an 1810 state commission that studied a route for the canal",
            "k": ["gouverneur morris", "1810", "commission"],
            "n": 0
        },
        {
            "id": "died-1828",
            "tier": "power",
            "t": "Died in office in February 1828; his rival Martin Van Buren was elected governor but served only about ten weeks",
            "k": ["1828", "ten weeks"],
            "n": 0
        },
        {
            "id": "lieutenant-governor",
            "tier": "power",
            "t": "Was also lieutenant governor while mayor; had resigned from the U.S. Senate in 1803 to become mayor",
            "k": ["lieutenant governor", "senate", "1803"],
            "n": 0
        },
        {
            "id": "uncle-died",
            "tier": "power",
            "t": "His uncle was the first vice president to die in office (April 1812), months before his own presidential run",
            "k": ["first vice president", "die in office", "april 1812"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Which Clinton?",
        "body": "Several famous Clintons show up in quiz bowl: DeWitt Clinton, the governor behind the Erie Canal; his uncle George Clinton, New York’s first governor and a vice president; Bill Clinton, the 42nd president; Hillary Clinton, a senator and secretary of state; and Henry Clinton, a British general in the American Revolution. Saying only “Clinton” earns a prompt. Erie Canal clues also lead tossups on the canal itself, where “Clinton’s Ditch” is accepted.",
        "fix": "The Erie Canal, the Wedding of the Waters, New York City’s mayor, and the 1812 race against Madison mean DeWitt; New York’s first governor and Jefferson’s vice president mean George. Listen for the noun: “this man” or “this governor” wants “DeWitt Clinton,” while “this canal” wants the Erie Canal.",
        "line": "Real answer line: <b><u>DeWitt Clinton</u></b> (prompt on <u>Clinton</u>; do not accept “George Clinton” or “Erie Canal”)"
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("wrote", data["id"])
