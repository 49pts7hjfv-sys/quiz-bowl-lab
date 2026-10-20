import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "federalist-party",
    "name": "Federalist Party",
    "mono": "FED",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "One of the first two U.S. political parties · Party of Hamilton and John Adams",
    "dates": "Formed early 1790s; faded after 1816",
    "briefing": "George Washington warned against political parties, but his own cabinet split into the first two of them. The Federalists, led by Alexander Hamilton, wanted a strong national government, a national bank, and friendly ties with Britain, and John Adams became their only president. After New England Federalists protested the War of 1812 at the Hartford Convention, the party faded away.",
    "answerHtml": "<b><u>Federalist</u></b> Party (accept <u>Federalists</u>; do not accept “Anti-Federalists” or “Democratic-Republicans”)",
    "accept": [
        "federalist party",
        "federalists",
        "federalist",
        "the federalists",
        "the federalist party",
        "federalist party of the united states"
    ],
    "prompt": [],
    "reject": [
        "anti federalists",
        "anti federalist",
        "antifederalists",
        "antifederalist",
        "anti federalist party",
        "federalist papers",
        "federalist essays",
        "federalist society",
        "federalist no 10",
        "federalist 10",
        "federalist number 10",
        "federalist no 51",
        "federalism",
        "democratic republican party",
        "democratic republicans",
        "democratic republican",
        "jeffersonian republicans",
        "republican party",
        "republicans",
        "democratic party",
        "democrats",
        "whig party",
        "whigs",
        "national republican party",
        "hartford convention",
        "essex junto"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Federalist_Party",
    "qb": {
        "q": "Federalist Party",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "Rufus King, who had signed the Constitution for Massachusetts, became this party’s last presidential candidate in 1816, but he won only three states against James Monroe. After that loss, this party faded away during the so-called “Era of Good Feelings.”",
            "r": "This party’s only president was John Adams. For 10 points, name this party of Alexander Hamilton, the rival of the Democratic-Republicans."
        },
        {
            "p": "Charles Cotesworth Pinckney was this party’s choice for vice president in 1800 and its candidate for president in 1804 and 1808, losing first to Thomas Jefferson and then to James Madison. Pinckney had earlier been one of the American diplomats asked for a bribe in the XYZ Affair.",
            "r": "This party’s leaders included John Adams and Alexander Hamilton. For 10 points, name this early political party that rivaled Jefferson’s Democratic-Republicans."
        },
        {
            "p": "John Fenno’s newspaper, the _Gazette of the United States_, supported this party, so Thomas Jefferson helped the poet Philip Freneau [“freh-NOH”] start the rival _National Gazette_ in 1791. Those newspapers spread the feud between this party and Jefferson’s supporters during George Washington’s presidency.",
            "r": "This party backed Treasury Secretary Alexander Hamilton’s plans. For 10 points, name this party that opposed the Democratic-Republicans."
        },
        {
            "p": "Timothy Pickering, who was linked to a group of this party’s Massachusetts leaders called the Essex Junto [“JUN-toh”], plotted for New England to break away from the Union during Thomas Jefferson’s first term. Pickering hoped Aaron Burr would bring New York into that northern confederacy if Burr became its governor.",
            "r": "Burr lost that 1804 race and later killed this party’s leader, Alexander Hamilton, in a duel. For 10 points, name this party of John Adams."
        },
        {
            "p": "George Cabot presided over a meeting of this party’s leaders where delegates proposed amendments such as requiring a two-thirds vote of Congress to declare war. Harrison Gray Otis and other messengers carried that meeting’s demands to Washington, arriving just as news of Andrew Jackson’s victory at New Orleans spread.",
            "r": "That meeting was the Hartford Convention, held during a war this party mocked as “Mr. Madison’s War.” For 10 points, name this party, which soon collapsed."
        },
        {
            "p": "Weeks before losing power, this party’s Congress passed the Judiciary Act of 1801, which created sixteen new federal judgeships that its outgoing president filled with “midnight judges.” The next year, Congress, now run by the rival party, repealed that law.",
            "r": "That outgoing president, John Adams, also named John Marshall Chief Justice. For 10 points, name this party that lost power to Thomas Jefferson’s Democratic-Republicans in 1801."
        },
        {
            "p": "Members of this party in Congress passed a 1798 law under which Vermont congressman Matthew Lyon was jailed for criticizing President John Adams. Thomas Jefferson and James Madison secretly wrote resolutions for Kentucky and Virginia to protest that law and three others passed with it.",
            "r": "Those laws were the Alien and Sedition Acts. For 10 points, name this party that controlled Congress at the time, led by Alexander Hamilton and John Adams."
        },
        {
            "p": "Fisher Ames of Massachusetts gave a famous speech in 1796 urging the House to pay for a treaty that this party supported and its rivals hated. That treaty, negotiated by John Jay, avoided war with Britain but did not stop the British from forcing American sailors into their navy.",
            "r": "Democratic-Republicans called this party too friendly to Britain. For 10 points, name this party that supported Jay’s Treaty and Alexander Hamilton."
        },
        {
            "p": "Members of this party cheered the slogan “Millions for defense, but not one cent for tribute” after French agents demanded a bribe from American diplomats. That XYZ Affair helped this party gain seats in the 1798 elections and build up the navy for an undeclared war with France.",
            "r": "That war came under this party’s only president, John Adams. For 10 points, name this party of Alexander Hamilton."
        },
        {
            "p": "In 1800, this party’s president fired Secretary of State Timothy Pickering and forced Secretary of War James McHenry to resign, because both men were more loyal to Alexander Hamilton. Hamilton then wrote a pamphlet attacking that president, which split this party before the election.",
            "r": "That president, John Adams, lost to Thomas Jefferson in 1800. For 10 points, name this party that never won the presidency again."
        },
        {
            "p": "This party made a comeback in New England after Thomas Jefferson’s Embargo Act of 1807 hurt merchants and sailors there. Opponents of the embargo, many of them members of this party, mocked it as “Ograbme” [“oh-GRAB-mee”], which is “embargo” spelled backward.",
            "r": "This party had been led by Alexander Hamilton until his death in 1804. For 10 points, name this party of John Adams."
        },
        {
            "p": "Many members of this party opposed the Louisiana Purchase, fearing that new western states would weaken the power of New England. This party drew much of its support from merchants, bankers, and lawyers in the Northeast who wanted close trade ties with Britain.",
            "r": "Its founder, Alexander Hamilton, created the First Bank of the United States. For 10 points, name this party, the opponent of Jefferson’s Democratic-Republicans."
        },
        {
            "p": "This party supported a plan for the national government to take over the states’ war debts, and its leaders argued that the Constitution’s “necessary and proper” clause let Congress charter a bank. They favored a loose reading of the Constitution and a strong central government.",
            "r": "That plan came from Treasury Secretary Alexander Hamilton. For 10 points, name this political party that he led, the party of John Adams."
        },
        {
            "p": "This party lost control of both the presidency and Congress in the election of 1800, which Thomas Jefferson later called a “revolution.” That handover was the first time power in the United States passed peacefully from one party to another.",
            "r": "This party’s candidate that year, John Adams, had been its only president. For 10 points, name this party built around Alexander Hamilton."
        },
        {
            "p": "John Marshall, a Virginian from this party, served as Chief Justice for 34 years and kept its ideas about a strong national government alive long after the party itself died out. Marshall had been named Chief Justice in 1801 by this party’s only president.",
            "r": "That president was John Adams of Massachusetts. For 10 points, name this political party led by Alexander Hamilton."
        }
    ],
    "clues": [
        {
            "id": "hamilton",
            "tier": "giveaway",
            "t": "Led by Alexander Hamilton, the first Secretary of the Treasury",
            "k": ["alexander hamilton", "hamilton"],
            "n": 0,
            "rabbit": "Alexander Hamilton"
        },
        {
            "id": "adams",
            "tier": "giveaway",
            "t": "John Adams was its only president (1797–1801)",
            "k": ["john adams", "only president"],
            "n": 0,
            "rabbit": "John Adams"
        },
        {
            "id": "rivals",
            "tier": "giveaway",
            "t": "Rival of Thomas Jefferson and James Madison’s Democratic-Republican Party; together they were the first two U.S. parties",
            "k": ["democratic-republican", "jefferson", "first two"],
            "n": 0,
            "rabbit": "Democratic-Republican Party"
        },
        {
            "id": "strong-government",
            "tier": "giveaway",
            "t": "Wanted a strong national government, a national bank, and close ties with Britain",
            "k": ["strong national government", "national bank", "britain"],
            "n": 0
        },
        {
            "id": "alien-sedition",
            "tier": "middle",
            "t": "Its Congress passed the Alien and Sedition Acts (1798); Congressman Matthew Lyon was jailed under the Sedition Act",
            "k": ["alien and sedition", "sedition", "matthew lyon"],
            "n": 0
        },
        {
            "id": "hartford",
            "tier": "middle",
            "t": "Hartford Convention (1814–1815): New England members protested the War of 1812, and the party collapsed",
            "k": ["hartford convention", "war of 1812"],
            "n": 0,
            "rabbit": "War of 1812"
        },
        {
            "id": "jay-treaty",
            "tier": "middle",
            "t": "Supported Jay’s Treaty with Britain (1795), which its rivals hated",
            "k": ["jay’s treaty", "1795"],
            "n": 0
        },
        {
            "id": "election-1800",
            "tier": "middle",
            "t": "Lost the election of 1800, which Jefferson called a “revolution”: the first peaceful handover of power between parties",
            "k": ["election of 1800", "1800", "peaceful"],
            "n": 0
        },
        {
            "id": "northeast",
            "tier": "middle",
            "t": "Strongest in New England, among merchants, bankers, and lawyers",
            "k": ["new england", "merchants", "bankers"],
            "n": 0
        },
        {
            "id": "marshall",
            "tier": "middle",
            "t": "Chief Justice John Marshall (1801–1835) kept its ideas alive on the Supreme Court for 34 years",
            "k": ["john marshall", "chief justice"],
            "n": 0
        },
        {
            "id": "loose",
            "tier": "middle",
            "t": "Read the Constitution loosely: the “necessary and proper” clause let Congress create a national bank",
            "k": ["loosely", "necessary and proper"],
            "n": 0
        },
        {
            "id": "rufus-king",
            "tier": "power",
            "t": "Rufus King, its last presidential candidate (1816), won only three states against James Monroe; the party faded in the “Era of Good Feelings”",
            "k": ["rufus king", "1816", "era of good feelings"],
            "n": 0
        },
        {
            "id": "pinckney",
            "tier": "power",
            "t": "Charles Cotesworth Pinckney: vice-presidential pick in 1800, then lost the presidency to Jefferson (1804) and Madison (1808)",
            "k": ["charles cotesworth pinckney", "pinckney", "1804", "1808"],
            "n": 0
        },
        {
            "id": "gazette",
            "tier": "power",
            "t": "John Fenno’s _Gazette of the United States_ backed it; Jefferson helped Philip Freneau start the rival _National Gazette_ (1791)",
            "k": ["fenno", "gazette of the united states", "freneau"],
            "n": 0
        },
        {
            "id": "essex-junto",
            "tier": "power",
            "t": "Timothy Pickering, linked to the Essex Junto, plotted for New England to leave the Union and hoped Aaron Burr would join (1804)",
            "k": ["essex junto", "pickering", "aaron burr"],
            "n": 0
        },
        {
            "id": "hartford-leaders",
            "tier": "power",
            "t": "George Cabot presided at Hartford; Harrison Gray Otis carried its demands, such as a two-thirds vote to declare war, to Washington",
            "k": ["george cabot", "harrison gray otis", "two-thirds"],
            "n": 0
        },
        {
            "id": "judiciary-1801",
            "tier": "power",
            "t": "Judiciary Act of 1801: sixteen new judgeships filled with “midnight judges”; repealed in 1802",
            "k": ["judiciary act", "midnight judges", "sixteen"],
            "n": 0
        },
        {
            "id": "resolutions",
            "tier": "power",
            "t": "Jefferson and Madison’s Kentucky and Virginia Resolutions protested the Alien and Sedition Acts",
            "k": ["kentucky", "virginia resolutions"],
            "n": 0
        },
        {
            "id": "fisher-ames",
            "tier": "power",
            "t": "Fisher Ames’s 1796 speech urged the House to fund Jay’s Treaty",
            "k": ["fisher ames", "ames"],
            "n": 0
        },
        {
            "id": "millions",
            "tier": "power",
            "t": "XYZ Affair slogan: “Millions for defense, but not one cent for tribute”; the party gained seats in 1798",
            "k": ["millions for defense", "tribute", "xyz"],
            "n": 0
        },
        {
            "id": "adams-cabinet",
            "tier": "power",
            "t": "Adams fired Timothy Pickering and pushed out James McHenry (1800); Hamilton’s pamphlet attacking Adams split the party",
            "k": ["james mchenry", "mchenry", "pamphlet"],
            "n": 0
        },
        {
            "id": "embargo",
            "tier": "power",
            "t": "Made a comeback in New England after Jefferson’s Embargo Act (1807), mocked as “Ograbme”",
            "k": ["embargo act", "ograbme"],
            "n": 0
        },
        {
            "id": "louisiana",
            "tier": "power",
            "t": "Many members opposed the Louisiana Purchase, fearing new western states would weaken New England",
            "k": ["louisiana purchase", "western states"],
            "n": 0
        },
        {
            "id": "madisons-war",
            "tier": "power",
            "t": "Members mocked the War of 1812 as “Mr. Madison’s War”",
            "k": ["madison’s war"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Party, papers, or ratifiers?",
        "body": "“Federalist” is part of three different answer lines. In 1787 and 1788, “Federalists” meant everyone who wanted to ratify the Constitution, including James Madison, against the Anti-Federalists. _The Federalist Papers_ were the 85 essays by Hamilton, Madison, and John Jay. The Federalist Party formed in the 1790s around Hamilton, and Madison helped lead the other side, the Democratic-Republicans.",
        "fix": "Listen for the noun and the date. “This party” with clues from the 1790s to 1816 (Hamilton’s bank, John Adams, the Alien and Sedition Acts, the Hartford Convention) wants the Federalist Party; “these essays” wants _The Federalist Papers_. Never answer “Anti-Federalists” or “Democratic-Republicans” for Hamilton’s party.",
        "line": "Real answer line: <b><u>Federalist</u></b> Party (accept <u>Federalists</u>)"
    },
    "tests": {
        "right": [
            "Federalist Party",
            "Federalists",
            "the Federalists",
            "Federalist",
            "Federalist Pary"
        ],
        "prompt": [],
        "wrong": [
            "Anti-Federalists",
            "Democratic-Republicans",
            "Federalism",
            "The Federalist Papers",
            "Whig Party",
            "Republican Party"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
