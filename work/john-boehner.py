import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "john-boehner",
    "name": "John Boehner",
    "mono": "JAB",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "Speaker of the House, 2011–2015 · Ohio Republican who resigned in 2015",
    "dates": "Born 1949",
    "briefing": "John Boehner [“BAY-ner”] grew up near Cincinnati, Ohio, as one of 12 children and worked in his father’s bar before becoming the first in his family to graduate from college. Elected to the U.S. House in 1990, he helped write the 1994 “Contract with America” and served as Speaker of the House from 2011 to 2015. Known for showing his emotions in public, he announced his resignation in 2015, the day after Pope Francis spoke to Congress at his invitation.",
    "answerHtml": "John <b><u>Boehner</u></b> (accept John Andrew <u>Boehner</u>)",
    "accept": [
        "john boehner",
        "boehner",
        "john andrew boehner",
        "john a boehner",
        "speaker boehner",
        "speaker john boehner",
        "john bayner",
        "bayner"
    ],
    "prompt": [],
    "reject": [
        "paul ryan",
        "ryan",
        "nancy pelosi",
        "pelosi",
        "newt gingrich",
        "gingrich",
        "dennis hastert",
        "hastert",
        "kevin mccarthy",
        "mccarthy",
        "eric cantor",
        "cantor",
        "tom delay",
        "dick armey",
        "roy blunt",
        "mike johnson",
        "mitch mcconnell",
        "harry reid",
        "john kasich",
        "kasich",
        "rob portman",
        "mark meadows",
        "warren davidson",
        "jim jordan",
        "john mccain",
        "john kerry",
        "john roberts",
        "barack obama"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/John_Boehner",
    "qb": {
        "q": "Boehner",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "This politician grew up near Cincinnati as the second of twelve children and worked as a boy at his father’s bar, Andy’s Cafe. He took seven years to finish college at Xavier University, working to pay his way, and became the first in his family to graduate.",
            "r": "For 10 points, name this Ohio Republican who served as Speaker of the House from 2011 to 2015."
        },
        {
            "p": "This future politician enlisted in the Navy during the Vietnam War, but he was honorably discharged after about eight weeks because of a back injury. He later ran a small company that sold plastics and packaging.",
            "r": "For 10 points, name this Ohio congressman who succeeded Nancy Pelosi as Speaker of the House in 2011."
        },
        {
            "p": "As a first-term congressman in 1991, this man joined the “Gang of Seven,” a group of freshman Republicans who publicized a scandal in which House members had overdrawn their accounts at the House bank. He had beaten a Republican incumbent in a primary the year before.",
            "r": "For 10 points, name this Ohio Republican who became Speaker of the House in 2011 and resigned in 2015."
        },
        {
            "p": "This congressman helped Newt Gingrich and Dick Armey write the “Contract with America,” the 1994 Republican campaign plan, and then served as chairman of the House Republican Conference from 1995 to 1999.",
            "r": "For 10 points, name this Ohio Republican who later served as Speaker of the House from 2011 to 2015."
        },
        {
            "p": "As chairman of the House Education and the Workforce Committee, this congressman worked with Senator Ted Kennedy to pass the No Child Left Behind Act, which President George W. Bush signed in January 2002.",
            "r": "For 10 points, name this Ohio Republican who was Speaker of the House until Paul Ryan replaced him in 2015."
        },
        {
            "p": "In February 2006, House Republicans chose this congressman as their Majority Leader over Roy Blunt, replacing Tom DeLay. After Democrats won the House that November, he became the Minority Leader instead. He had first been elected to Congress in 1990.",
            "r": "For 10 points, name this Ohioan who served as Speaker of the House from 2011 to 2015."
        },
        {
            "p": "Months before the 2010 midterm elections, this congressman unveiled the “Pledge to America,” a list of his party’s promises. After those elections gave his party control of the House, he took the gavel from Nancy Pelosi.",
            "r": "In January 2011, he became the 53rd Speaker of the House. For 10 points, name this Ohio Republican."
        },
        {
            "p": "In the summer of 2011, this congressional leader held talks with President Barack Obama on a “grand bargain” to cut the federal deficit, but the talks fell apart. The standoff over raising the debt ceiling ended with the Budget Control Act.",
            "r": "For 10 points, name this Ohio Republican who was Speaker of the House from 2011 to 2015."
        },
        {
            "p": "In December 2012, this leader pulled his “Plan B” bill to avoid the “fiscal cliff” after it failed to win enough support from his own party. Weeks later, the House reelected him to its top job.",
            "r": "For 10 points, name this Ohio Republican who was Speaker of the House from 2011 to 2015."
        },
        {
            "p": "In October 2013, the federal government shut down for 16 days while this leader’s chamber and the Senate disagreed over funding for the Affordable Care Act. The shutdown ended when Congress passed a deal to reopen the government.",
            "r": "For 10 points, name this Ohio Republican who was Speaker of the House at the time."
        },
        {
            "p": "This congressional leader invited Israeli Prime Minister Benjamin Netanyahu to address Congress in March 2015 without first consulting the White House. Netanyahu used the speech to argue against a nuclear deal with Iran that the Obama administration was negotiating.",
            "r": "For 10 points, name this Ohio Republican who was Speaker of the House from 2011 to 2015."
        },
        {
            "p": "This man wept as Pope Francis became the first pope to address a joint meeting of Congress, a visit this man had sought for years. The next day, he announced that he would resign from Congress.",
            "r": "For 10 points, name this Ohio Republican who stepped down as Speaker of the House in October 2015."
        },
        {
            "p": "In July 2015, North Carolina congressman Mark Meadows filed a “motion to vacate the chair,” seeking a vote to remove this man from his leadership post. Pressure from the House Freedom Caucus helped lead this man to step down later that year.",
            "r": "For 10 points, name this Ohio Republican who was replaced as Speaker of the House by Paul Ryan."
        },
        {
            "p": "This man wrote the 2021 memoir _On the House_ about his years in Congress. In 2016, Warren Davidson won a special election for the Ohio district this man had represented for more than two decades.",
            "r": "For 10 points, name this Republican who was Speaker of the House from 2011 to 2015."
        },
        {
            "p": "Before going to Congress, this businessman served in the Ohio House of Representatives from 1985 to 1990. In Washington, he represented Ohio’s 8th District, which included suburbs north of Cincinnati, for nearly 25 years.",
            "r": "For 10 points, name this Republican who was Speaker of the House from 2011 until he resigned in 2015."
        }
    ],
    "clues": [
        {
            "id": "speaker",
            "tier": "giveaway",
            "t": "Speaker of the House of Representatives from January 2011 to October 2015",
            "k": ["speaker of the house", "speaker", "2011"],
            "n": 0,
            "rabbit": "Speaker of the House of Representatives"
        },
        {
            "id": "ohio",
            "tier": "giveaway",
            "t": "Republican congressman from Ohio (1991–2015), from the Cincinnati area",
            "k": ["ohio", "republican", "cincinnati"],
            "n": 0
        },
        {
            "id": "pelosi-ryan",
            "tier": "giveaway",
            "t": "Succeeded Nancy Pelosi as Speaker; Paul Ryan succeeded him",
            "k": ["nancy pelosi", "pelosi", "paul ryan", "ryan"],
            "n": 0,
            "rabbit": "Paul Ryan"
        },
        {
            "id": "resigned",
            "tier": "giveaway",
            "t": "Announced his resignation in September 2015 and left Congress that October",
            "k": ["resignation", "2015"],
            "n": 0
        },
        {
            "id": "pope",
            "tier": "middle",
            "t": "Announced his resignation the day after Pope Francis, whom he had invited, addressed Congress",
            "k": ["pope francis", "pope"],
            "n": 0
        },
        {
            "id": "contract",
            "tier": "middle",
            "t": "Helped write the “Contract with America” (1994) with Newt Gingrich and Dick Armey",
            "k": ["contract with america", "newt gingrich", "gingrich"],
            "n": 0,
            "rabbit": "Newt Gingrich"
        },
        {
            "id": "shutdown",
            "tier": "middle",
            "t": "Speaker during the 16-day government shutdown over funding for the Affordable Care Act (October 2013)",
            "k": ["shutdown", "affordable care act"],
            "n": 0,
            "rabbit": "Affordable Care Act"
        },
        {
            "id": "debt-ceiling",
            "tier": "middle",
            "t": "Negotiated with Barack Obama during the 2011 debt-ceiling standoff, which ended with the Budget Control Act",
            "k": ["debt-ceiling", "budget control act", "barack obama"],
            "n": 0
        },
        {
            "id": "emotional",
            "tier": "middle",
            "t": "Known for openly showing emotion and often tearing up in public",
            "k": ["tearing up", "emotion"],
            "n": 0
        },
        {
            "id": "majority-leader",
            "tier": "middle",
            "t": "House Majority Leader (2006), replacing Tom DeLay, then Minority Leader (2007–2011)",
            "k": ["majority leader", "minority leader", "tom delay"],
            "n": 0
        },
        {
            "id": "twelve-children",
            "tier": "middle",
            "t": "Grew up as one of 12 children and worked at his father’s bar, Andy’s Cafe",
            "k": ["12 children", "andy’s cafe", "bar"],
            "n": 0
        },
        {
            "id": "navy",
            "tier": "power",
            "t": "Enlisted in the Navy during the Vietnam War but was discharged after about eight weeks because of a back injury",
            "k": ["navy", "eight weeks", "back injury"],
            "n": 0
        },
        {
            "id": "xavier",
            "tier": "power",
            "t": "First in his family to graduate from college: Xavier University (1977), after seven years of work and study",
            "k": ["xavier", "1977", "seven years"],
            "n": 0
        },
        {
            "id": "plastics",
            "tier": "power",
            "t": "Ran a small plastics and packaging sales company before entering politics",
            "k": ["plastics", "packaging"],
            "n": 0
        },
        {
            "id": "ohio-house",
            "tier": "power",
            "t": "Served in the Ohio House of Representatives (1985–1990); represented Ohio’s 8th District in Congress",
            "k": ["ohio house", "8th district", "1985"],
            "n": 0
        },
        {
            "id": "gang-of-seven",
            "tier": "power",
            "t": "Member of the “Gang of Seven” freshmen who publicized the House banking scandal (1991–1992)",
            "k": ["gang of seven", "banking scandal"],
            "n": 0
        },
        {
            "id": "conference-chair",
            "tier": "power",
            "t": "Chairman of the House Republican Conference (1995–1999)",
            "k": ["republican conference", "1995"],
            "n": 0
        },
        {
            "id": "nclb",
            "tier": "power",
            "t": "Chaired the Education and the Workforce Committee; worked with Ted Kennedy on the No Child Left Behind Act (2002)",
            "k": ["no child left behind", "ted kennedy", "education"],
            "n": 0
        },
        {
            "id": "blunt",
            "tier": "power",
            "t": "Beat Roy Blunt to become Majority Leader in February 2006",
            "k": ["roy blunt", "blunt"],
            "n": 0
        },
        {
            "id": "pledge",
            "tier": "power",
            "t": "Unveiled the “Pledge to America” before the 2010 midterm elections",
            "k": ["pledge to america", "pledge"],
            "n": 0
        },
        {
            "id": "plan-b",
            "tier": "power",
            "t": "Pulled his “Plan B” bill to avoid the “fiscal cliff” in December 2012",
            "k": ["plan b", "fiscal cliff"],
            "n": 0
        },
        {
            "id": "netanyahu",
            "tier": "power",
            "t": "Invited Benjamin Netanyahu to address Congress (March 2015) without consulting the White House",
            "k": ["benjamin netanyahu", "netanyahu"],
            "n": 0
        },
        {
            "id": "meadows",
            "tier": "power",
            "t": "Mark Meadows filed a “motion to vacate the chair” against him (July 2015); the House Freedom Caucus opposed him",
            "k": ["mark meadows", "motion to vacate", "freedom caucus"],
            "n": 0
        },
        {
            "id": "memoir",
            "tier": "power",
            "t": "Wrote the memoir _On the House_ (2021); Warren Davidson won his old seat in 2016",
            "k": ["on the house", "warren davidson", "davidson"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Which recent Speaker?",
        "body": "Four modern Speakers of the House get mixed up. Newt Gingrich of Georgia led the 1994 “Contract with America” and was Speaker from 1995 to 1999; Nancy Pelosi of California held the job from 2007 to 2011 and again from 2019 to 2023; John Boehner of Ohio served from 2011 until he resigned in 2015; and Paul Ryan of Wisconsin followed him until 2019. Boehner helped write the Contract with America, so that clue alone doesn’t tell you which one it is.",
        "fix": "Ohio, Cincinnati, Andy’s Cafe, the 2013 shutdown, Pope Francis’s visit, and resigning in 2015 mean Boehner. Georgia means Gingrich, California and being the first woman Speaker mean Pelosi, and Janesville and Mitt Romney’s 2012 ticket mean Ryan.",
        "line": "Real answer line: John <b><u>Boehner</u></b> (accept John Andrew <u>Boehner</u>)"
    },
    "tests": {
        "right": [
            "John Boehner",
            "Boehner",
            "Speaker Boehner",
            "John Andrew Boehner",
            "Jon Boehner",
            "Boener",
            "John Bayner"
        ],
        "prompt": [],
        "wrong": [
            "Paul Ryan",
            "Nancy Pelosi",
            "Newt Gingrich",
            "Kevin McCarthy",
            "Dennis Hastert",
            "Eric Cantor",
            "John Kasich",
            "Mitch McConnell"
        ]
    }
}

out = ROOT / "topics" / f"{data['id']}.json"
with open(out, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("wrote", out)
