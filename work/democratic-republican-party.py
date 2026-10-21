import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TIP = "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."

data = {
    "id": "democratic-republican-party",
    "name": "Democratic-Republican Party",
    "mono": "DR",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "Party of Jefferson and Madison · Rival of the Federalists, 1790s–1820s",
    "dates": "Founded early 1790s; split after 1824",
    "briefing": "In the early 1790s, Thomas Jefferson and James Madison organized a party to fight Alexander Hamilton’s Federalists. Its members usually called themselves “Republicans,” and they wanted a small national government, a strict reading of the Constitution, and a nation of independent farmers. The Democratic-Republican Party won the presidency in 1800, and its leaders held that office for decades before the party split apart after the election of 1824.",
    "answerHtml": "<b><u>Democratic-Republican</u></b> Party (accept <u>Democratic-Republicans</u> or <u>Jeffersonian Republicans</u>; prompt on <u>Republicans</u>; do not accept “Republican Party” or “Democratic Party”)",
    "accept": [
        "democratic republican party",
        "the democratic republican party",
        "democratic republicans",
        "the democratic republicans",
        "democratic republican",
        "jeffersonian republicans",
        "the jeffersonian republicans",
        "jeffersonian republican party",
        "jeffersonian republican"
    ],
    "prompt": [
        "republicans",
        "republican",
        "the republicans",
        "jeffersonians",
        "jeffersonian party",
        "jeffersonian democrats"
    ],
    "reject": [
        "democratic party",
        "the democratic party",
        "democrats",
        "the democrats",
        "democrat",
        "gop",
        "grand old party",
        "federalist party",
        "the federalist party",
        "federalists",
        "federalist",
        "anti federalists",
        "anti federalist",
        "antifederalists",
        "antifederalist",
        "national republican party",
        "national republicans",
        "national republican",
        "whig party",
        "whigs",
        "whig",
        "free soil party",
        "know nothing party",
        "tammany hall",
        "tammany"
    ],
    "tests": {
        "right": [
            "Democratic-Republican Party",
            "Democratic Republicans",
            "Jeffersonian Republicans",
            "Democratic-Republican",
            "the Democratic-Republican Party",
            "Democratic Republican Partty"
        ],
        "prompt": [
            "Republicans",
            "Republican"
        ],
        "wrong": [
            "Republican Party",
            "Democratic Party",
            "Federalist Party",
            "Democrats",
            "Whig Party",
            "National Republicans",
            "Anti-Federalists"
        ]
    },
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Democratic-Republican_Party",
    "qb": {
        "q": "Democratic-Republican",
        "found": 0,
        "tip": TIP
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "The secretary of state gave the poet Philip Freneau [“freh-NOH”] a job as a State Department translator in 1791, and Freneau soon began the _National Gazette_, a newspaper that spoke for this party. That paper’s chief rival was John Fenno’s _Gazette of the United States_.",
            "r": "For 10 points, name this political party founded by Thomas Jefferson and James Madison to oppose Alexander Hamilton’s Federalists."
        },
        {
            "p": "After a bitter campaign, the first president from this party declared in his inaugural address, “We are all Republicans, we are all Federalists.” Years later, he described his own victory as “the revolution of 1800.”",
            "r": "That president was Thomas Jefferson. For 10 points, name this party that he and James Madison founded to oppose the Federalists."
        },
        {
            "p": "John Randolph of Roanoke led a small group called the “Tertium Quids” [“TER-shee-um KWIDZ”] that broke away from this party around 1806, accusing its leaders of abandoning the principles of limited government. Randolph had been one of this party’s leaders in the House.",
            "r": "Thomas Jefferson was then the president from this party. For 10 points, name this party that opposed the Federalists."
        },
        {
            "p": "In 1800, two candidates from this party tied with 73 electoral votes each, so the House of Representatives had to choose between them, finally doing so on its 36th ballot. That tie led to the Twelfth Amendment, which had electors vote separately for president and vice president.",
            "r": "The winner was Thomas Jefferson. For 10 points, name this party that Jefferson founded with James Madison."
        },
        {
            "p": "In 1820, a president from this party won every electoral vote but one, which William Plumer of New Hampshire cast for John Quincy Adams. The only other major party of the time had not even nominated a candidate against him.",
            "r": "That president, James Monroe, led the country during the Era of Good Feelings. For 10 points, name this party founded by Thomas Jefferson and James Madison."
        },
        {
            "p": "This party’s members in Congress met in a caucus to pick its presidential candidates, a system critics called “King Caucus.” That system collapsed in 1824, when the caucus chose William Crawford but three other members of this party also ran for president.",
            "r": "After that election, the party split into followers of Andrew Jackson and of John Quincy Adams. For 10 points, name this party founded by Thomas Jefferson."
        },
        {
            "p": "In 1798, two founders of this party secretly wrote resolutions for the legislatures of Kentucky and Virginia, arguing that states could resist unconstitutional federal laws. Those resolutions attacked the Alien and Sedition Acts, which John Adams had signed.",
            "r": "Those founders were Thomas Jefferson and James Madison. For 10 points, name the political party they created."
        },
        {
            "p": "In 1816, a president from this party signed a charter for the Second Bank of the United States, even though in 1791 he had argued in Congress that it had no power to create the first national bank. That same year, this party’s Congress passed what is often called the first protective tariff.",
            "r": "That president, James Madison, had led the country through the War of 1812. For 10 points, name the party he founded with Thomas Jefferson."
        },
        {
            "p": "Members of this party condemned the treaty that John Jay signed with Britain in 1794, and protesters burned Jay in effigy. In 1796, this party’s leaders in the House of Representatives tried, and failed, to block the money needed to carry out that treaty.",
            "r": "This party generally favored France over Britain. For 10 points, name this party led by Thomas Jefferson and James Madison."
        },
        {
            "p": "In a 1791 opinion for George Washington, a future founder of this party argued that Congress had no power to charter a national bank, because the Constitution did not list that power. The treasury secretary answered that the Constitution’s “necessary and proper” clause implied such powers.",
            "r": "This party, which opposed Alexander Hamilton’s Federalists, favored a strict reading of the Constitution. For 10 points, name this party founded by Thomas Jefferson and James Madison."
        },
        {
            "p": "Swiss-born Albert Gallatin [“GAL-uh-tin”], a leader of this party in the House, later served as Treasury Secretary longer than anyone else in history, cutting the national debt under two of its presidents. Gallatin also helped negotiate the Treaty of Ghent.",
            "r": "Those presidents were Thomas Jefferson and James Madison. For 10 points, name the party they founded."
        },
        {
            "p": "In a November 1794 speech to Congress, George Washington blamed “self-created societies” for stirring up the Whiskey Rebellion, meaning political clubs that shared this party’s views. Many of those clubs had been inspired by the French Revolution.",
            "r": "For 10 points, name this party founded by Thomas Jefferson and James Madison to oppose Hamilton’s Federalists."
        },
        {
            "p": "A president from this party worried that the Constitution did not allow him to buy land from a foreign country, so he drafted an amendment to permit it. He went ahead with the purchase anyway in 1803, roughly doubling the size of the country.",
            "r": "That president, Thomas Jefferson, made the Louisiana Purchase. For 10 points, name the party he founded with James Madison."
        },
        {
            "p": "Young members of this party called “War Hawks,” led by Henry Clay and John C. Calhoun, pushed Congress to declare war on Britain in 1812. The rival party’s opposition to that war, shown at the Hartford Convention, helped leave this party with almost no opponents.",
            "r": "For 10 points, name this party of Thomas Jefferson, James Madison, and James Monroe."
        },
        {
            "p": "Critics drew a snapping turtle named “Ograbme” [“oh-GRAB-mee”] to mock a law passed by this party, since the turtle’s name spelled “embargo” backward. That 1807 law banned American ships from trading at foreign ports and badly hurt New England’s merchants.",
            "r": "That law was signed by Thomas Jefferson. For 10 points, name the party Jefferson founded with James Madison."
        }
    ],
    "clues": [
        {
            "id": "founders",
            "tier": "giveaway",
            "t": "Founded by Thomas Jefferson and James Madison in the early 1790s",
            "k": ["jefferson", "madison", "1790s"],
            "n": 0,
            "rabbit": "Thomas Jefferson"
        },
        {
            "id": "vs-federalists",
            "tier": "giveaway",
            "t": "Rival of Alexander Hamilton’s Federalist Party; together they made up the first U.S. two-party system",
            "k": ["federalist", "hamilton", "two-party"],
            "n": 0,
            "rabbit": "Federalist Party"
        },
        {
            "id": "presidents",
            "tier": "giveaway",
            "t": "Its presidents: Jefferson, Madison, James Monroe, and John Quincy Adams",
            "k": ["monroe", "john quincy adams"],
            "n": 0
        },
        {
            "id": "strict-construction",
            "tier": "giveaway",
            "t": "Favored a strict reading of the Constitution, states’ rights, a small national government, and farmers",
            "k": ["strict", "states’ rights", "farmers"],
            "n": 0
        },
        {
            "id": "election-1800",
            "tier": "middle",
            "t": "Won the presidency in the election of 1800, which Jefferson called “the revolution of 1800”",
            "k": ["1800", "revolution of 1800"],
            "n": 0
        },
        {
            "id": "good-feelings",
            "tier": "middle",
            "t": "Ruled almost unopposed during James Monroe’s “Era of Good Feelings” (1817–1825)",
            "k": ["era of good feelings", "good feelings"],
            "n": 0,
            "rabbit": "James Monroe"
        },
        {
            "id": "split-1824",
            "tier": "middle",
            "t": "Split after the election of 1824: Andrew Jackson’s followers became the Democrats, and Adams and Clay’s became the National Republicans",
            "k": ["1824", "national republicans", "jackson"],
            "n": 0,
            "rabbit": "Democratic Party"
        },
        {
            "id": "kentucky-virginia",
            "tier": "middle",
            "t": "Jefferson and Madison secretly wrote the Kentucky and Virginia Resolutions (1798) against the Alien and Sedition Acts",
            "k": ["kentucky", "virginia resolutions", "alien and sedition"],
            "n": 0
        },
        {
            "id": "jay-treaty",
            "tier": "middle",
            "t": "Opposed John Jay’s 1794 treaty with Britain and generally favored France",
            "k": ["jay", "britain", "france"],
            "n": 0
        },
        {
            "id": "bank-opinion",
            "tier": "middle",
            "t": "Jefferson argued in a 1791 opinion that Hamilton’s national bank was unconstitutional",
            "k": ["national bank", "unconstitutional", "1791"],
            "n": 0
        },
        {
            "id": "name",
            "tier": "middle",
            "t": "Members usually called it the “Republican” party, but it is not the modern Republican Party, founded in 1854",
            "k": ["1854", "modern"],
            "n": 0
        },
        {
            "id": "all-federalists",
            "tier": "middle",
            "t": "Jefferson’s First Inaugural Address (1801): “We are all Republicans, we are all Federalists”",
            "k": ["first inaugural", "we are all"],
            "n": 0
        },
        {
            "id": "freneau",
            "tier": "power",
            "t": "Philip Freneau’s _National Gazette_ (1791), backed by Jefferson, spoke for it; John Fenno’s _Gazette of the United States_ backed Hamilton",
            "k": ["freneau", "national gazette", "fenno"],
            "n": 0
        },
        {
            "id": "quids",
            "tier": "power",
            "t": "John Randolph of Roanoke led the “Tertium Quids,” a small group that broke away around 1806",
            "k": ["tertium quids", "quids", "randolph"],
            "n": 0
        },
        {
            "id": "burr-tie",
            "tier": "power",
            "t": "In 1800, Jefferson and Aaron Burr tied with 73 electoral votes; the House chose Jefferson on its 36th ballot, leading to the 12th Amendment",
            "k": ["aaron burr", "36th ballot", "12th amendment"],
            "n": 0,
            "rabbit": "Aaron Burr"
        },
        {
            "id": "plumer",
            "tier": "power",
            "t": "In 1820, Monroe won every electoral vote but one, cast by William Plumer for John Quincy Adams",
            "k": ["plumer", "1820", "every electoral vote"],
            "n": 0
        },
        {
            "id": "king-caucus",
            "tier": "power",
            "t": "Its members of Congress picked its presidential nominees in a caucus (“King Caucus”) until 1824, when they chose William Crawford",
            "k": ["king caucus", "caucus", "crawford"],
            "n": 0
        },
        {
            "id": "second-bank",
            "tier": "power",
            "t": "Under Madison, it chartered the Second Bank of the United States and passed a protective tariff (both 1816), though Madison had opposed the first bank in 1791",
            "k": ["second bank", "1816", "protective tariff"],
            "n": 0
        },
        {
            "id": "gallatin",
            "tier": "power",
            "t": "Albert Gallatin, the longest-serving Treasury Secretary, cut the national debt under Jefferson and Madison",
            "k": ["gallatin", "treasury"],
            "n": 0
        },
        {
            "id": "societies",
            "tier": "power",
            "t": "Washington blamed clubs that shared its views, the “self-created societies,” for the Whiskey Rebellion (1794)",
            "k": ["self-created societies", "whiskey rebellion"],
            "n": 0,
            "rabbit": "Whiskey Rebellion"
        },
        {
            "id": "louisiana",
            "tier": "power",
            "t": "Jefferson doubted the Constitution allowed the Louisiana Purchase (1803) and drafted an amendment, but went ahead anyway",
            "k": ["louisiana purchase", "1803", "amendment"],
            "n": 0
        },
        {
            "id": "war-hawks",
            "tier": "power",
            "t": "Its “War Hawks,” led by Henry Clay and John C. Calhoun, pushed for the War of 1812; the Federalists’ Hartford Convention opposed that war",
            "k": ["war hawks", "war of 1812", "hartford convention"],
            "n": 0
        },
        {
            "id": "embargo",
            "tier": "power",
            "t": "Jefferson’s Embargo Act (1807) hurt New England; critics drew a snapping turtle named “Ograbme” (embargo spelled backward)",
            "k": ["embargo act", "1807", "ograbme"],
            "n": 0
        },
        {
            "id": "jay-money",
            "tier": "power",
            "t": "Protesters burned John Jay in effigy; in 1796, its House leaders failed to block money to carry out his treaty",
            "k": ["effigy", "1796"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Neither modern party",
        "body": "This party’s members usually called themselves “Republicans,” but it is not the Republican Party of Abraham Lincoln, which was founded in 1854. The modern Democratic Party grew out of Andrew Jackson’s wing of this party in the late 1820s, but it is a separate answer line too. Real answer lines prompt on “Republicans” and do not accept “Republican Party” or “Democratic Party.”",
        "fix": "Use the date: clues from the 1790s to the 1820s, like Jefferson, Madison, Monroe, and fights with the Federalists, want the Democratic-Republicans. Say the full name, “Democratic-Republican Party,” so you are not stuck with a prompt.",
        "line": "Real answer line: <b><u>Democratic-Republican</u></b> Party (accept <u>Jeffersonian Republicans</u>; prompt on <u>Republicans</u>; do not accept “Republican Party” or “Democratic Party”)"
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("wrote", data["id"])
