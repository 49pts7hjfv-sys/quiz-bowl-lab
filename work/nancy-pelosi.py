import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "nancy-pelosi",
    "name": "Nancy Pelosi",
    "mono": "NP",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "First woman Speaker of the House · Speaker 2007–2011 and 2019–2023",
    "dates": "Born 1940",
    "briefing": "Nancy Pelosi grew up in Baltimore, where her father, Thomas D’Alesandro Jr., was the mayor. After moving to San Francisco, she won a seat in the U.S. House of Representatives in 1987. In 2007, she became the first woman to serve as Speaker of the House, and she held the job again from 2019 to 2023. She was Speaker when the House passed the Affordable Care Act and when it impeached Donald Trump twice.",
    "answerHtml": "Nancy <b><u>Pelosi</u></b> (accept Nancy Patricia D’Alesandro <u>Pelosi</u>)",
    "accept": [
        "nancy pelosi",
        "pelosi",
        "nancy patricia pelosi",
        "nancy patricia dalesandro pelosi",
        "nancy dalesandro pelosi",
        "nancy p pelosi",
        "speaker pelosi",
        "speaker nancy pelosi"
    ],
    "prompt": [],
    "reject": [
        "paul pelosi",
        "alexandra pelosi",
        "christine pelosi",
        "thomas dalesandro",
        "thomas dalesandro jr",
        "thomas dalesandro iii",
        "john boehner",
        "boehner",
        "newt gingrich",
        "gingrich",
        "kevin mccarthy",
        "paul ryan",
        "dennis hastert",
        "hastert",
        "mike johnson",
        "hakeem jeffries",
        "jeffries",
        "steny hoyer",
        "dick gephardt",
        "chuck schumer",
        "harry reid",
        "sam rayburn",
        "tip oneill",
        "sala burton",
        "nancy reagan",
        "nancy kassebaum",
        "dianne feinstein",
        "barbara boxer",
        "kamala harris",
        "hillary clinton",
        "geraldine ferraro"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Nancy_Pelosi",
    "qb": {
        "q": "Pelosi",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "Before she died in 1987, Congresswoman Sala Burton asked her supporters to back this woman as her successor, and this woman won the special election for Burton’s seat that June. Earlier, this woman had served as chair of the California Democratic Party.",
            "r": "For 10 points, name this San Francisco Democrat who became the first woman Speaker of the House in 2007."
        },
        {
            "p": "In 2019, this politician won back the Speaker’s gavel after losing it, something no one had done after Sam Rayburn returned to the job in 1955. She took over from Paul Ryan, just as she had taken over from Dennis Hastert twelve years earlier.",
            "r": "For 10 points, name this California Democrat, the first woman to serve as Speaker of the House."
        },
        {
            "p": "This politician’s father, Thomas D’Alesandro Jr., served in Congress and then as mayor of Baltimore, and one of her brothers later became Baltimore’s mayor too. She graduated from Trinity College in Washington, D.C., in 1962 and later moved to San Francisco.",
            "r": "For 10 points, name this Democrat who was Speaker of the House from 2007 to 2011 and from 2019 to 2023."
        },
        {
            "p": "When she took office in January 2007, this leader told the House, “For our daughters and granddaughters, today we have broken the marble ceiling.” Four years earlier, she had become the first woman to lead a major party in either house of Congress.",
            "r": "For 10 points, name this California Democrat, the first woman to serve as Speaker of the House of Representatives."
        },
        {
            "p": "In March 2010, this Speaker led the House as it voted 219 to 212 to pass a health-care bill the Senate had approved, and President Barack Obama signed it two days later. That law expanded Medicaid and required most Americans to have health insurance.",
            "r": "That law was the Affordable Care Act. For 10 points, name this first woman Speaker of the House."
        },
        {
            "p": "In September 2019, this Speaker announced a formal impeachment inquiry into President Donald Trump, and the House impeached him that December for abuse of power and obstruction of Congress. In January 2021, the House impeached Trump a second time while she was still Speaker.",
            "r": "For 10 points, name this California Democrat, the first woman Speaker of the House."
        },
        {
            "p": "In August 2022, this politician became the highest-ranking American official to visit Taiwan in 25 years, and China answered the trip with large military exercises around the island. The last official of her rank to visit had been Newt Gingrich, in 1997.",
            "r": "For 10 points, name this Speaker of the House from 2019 to 2023, the first woman to hold that job."
        },
        {
            "p": "In 1991, two years after the protests in Tiananmen Square, this member of Congress and two colleagues unfurled a small banner there honoring those who died for democracy in China. She had first won her House seat in a special election four years earlier.",
            "r": "For 10 points, name this San Francisco Democrat who became the first woman Speaker of the House."
        },
        {
            "p": "After the 2022 elections, this leader announced she would step down from her party’s leadership, and Hakeem Jeffries succeeded her as the top House Democrat. Her party then gave her the honorary title “Speaker Emerita.”",
            "r": "Kevin McCarthy replaced her as Speaker in January 2023. For 10 points, name this first woman Speaker of the House."
        },
        {
            "p": "In 2001, this congresswoman defeated Steny Hoyer to become her party’s whip, the first woman ever to hold that post in the House. The next year, she was chosen to lead House Democrats when Dick Gephardt stepped down as their leader.",
            "r": "For 10 points, name this Democrat who became the first woman Speaker of the House in 2007."
        },
        {
            "p": "This politician led the host committee that brought the 1984 Democratic National Convention to San Francisco, where Geraldine Ferraro became the first woman nominated for vice president by a major party. Three years later, she won her own seat in Congress.",
            "r": "For 10 points, name this San Francisco Democrat who served as Speaker of the House from 2007 to 2011 and from 2019 to 2023."
        },
        {
            "p": "As Speaker, this politician led the House as it passed the Lilly Ledbetter Fair Pay Act, the first bill that President Barack Obama signed into law, in January 2009. Her party had won control of the House in the 2006 elections.",
            "r": "For 10 points, name this California Democrat, the first woman to serve as Speaker of the House."
        },
        {
            "p": "John Boehner [“BAY-ner”] took the Speaker’s gavel from this politician in January 2011, after Republicans won back the House in the 2010 midterm elections. She then led House Democrats as Minority Leader for eight years.",
            "r": "For 10 points, name this San Francisco Democrat who was Speaker both before Boehner and after Paul Ryan."
        },
        {
            "p": "This politician was the first Californian and the first Italian American to serve as Speaker of the House. She was the 52nd person to hold that office, taking over from Dennis Hastert, a Republican from Illinois, in 2007.",
            "r": "For 10 points, name this Democrat from San Francisco who was also the first woman Speaker."
        },
        {
            "p": "During this politician’s second stretch as Speaker, the House passed the Infrastructure Investment and Jobs Act of 2021 and the CHIPS and Science Act of 2022, which offered money to build computer-chip factories in the United States.",
            "r": "She had first become Speaker in 2007. For 10 points, name this San Francisco Democrat, the first woman to hold that job."
        }
    ],
    "clues": [
        {
            "id": "first-woman-speaker",
            "tier": "giveaway",
            "t": "First woman Speaker of the House, serving from 2007 to 2011 and from 2019 to 2023",
            "k": ["first woman", "speaker of the house", "speaker"],
            "n": 0,
            "rabbit": "Speaker of the House of Representatives"
        },
        {
            "id": "san-francisco",
            "tier": "giveaway",
            "t": "Democrat who first won a House seat from San Francisco, California, in 1987",
            "k": ["san francisco", "democrat", "1987"],
            "n": 0
        },
        {
            "id": "aca",
            "tier": "giveaway",
            "t": "Led the House when it passed the Affordable Care Act (2010), which Barack Obama signed",
            "k": ["affordable care act", "barack obama", "2010"],
            "n": 0,
            "rabbit": "Affordable Care Act"
        },
        {
            "id": "impeachments",
            "tier": "giveaway",
            "t": "Speaker when the House impeached Donald Trump in December 2019 and again in January 2021",
            "k": ["impeached", "donald trump", "2019", "2021"],
            "n": 0,
            "rabbit": "Impeachment"
        },
        {
            "id": "baltimore",
            "tier": "middle",
            "t": "Grew up in Baltimore; her father, Thomas D’Alesandro Jr., was a congressman and the city’s mayor, and a brother later became mayor too",
            "k": ["baltimore", "d’alesandro", "mayor"],
            "n": 0
        },
        {
            "id": "marble-ceiling",
            "tier": "middle",
            "t": "Said on becoming Speaker in 2007: “For our daughters and granddaughters, today we have broken the marble ceiling”",
            "k": ["marble ceiling", "granddaughters", "daughters"],
            "n": 0
        },
        {
            "id": "party-leader",
            "tier": "middle",
            "t": "First woman to lead a major party in Congress: led House Democrats from 2003 to 2023, as Minority Leader in 2003–2007 and 2011–2019",
            "k": ["minority leader", "lead a major party", "2003"],
            "n": 0
        },
        {
            "id": "hastert-ryan",
            "tier": "middle",
            "t": "Took over as Speaker from Dennis Hastert (2007) and from Paul Ryan (2019)",
            "k": ["dennis hastert", "hastert", "paul ryan"],
            "n": 0,
            "rabbit": "Paul Ryan"
        },
        {
            "id": "boehner-mccarthy",
            "tier": "middle",
            "t": "Handed the gavel to John Boehner (2011) and to Kevin McCarthy (2023)",
            "k": ["john boehner", "boehner", "kevin mccarthy"],
            "n": 0,
            "rabbit": "John Boehner"
        },
        {
            "id": "rayburn",
            "tier": "middle",
            "t": "In 2019, won back the gavel after losing it, which no one had done after Sam Rayburn returned in 1955",
            "k": ["sam rayburn", "rayburn", "won back"],
            "n": 0
        },
        {
            "id": "elections-2006",
            "tier": "middle",
            "t": "Became Speaker after Democrats won the House in the 2006 elections; Republicans won it back in 2010",
            "k": ["2006", "2010", "elections"],
            "n": 0
        },
        {
            "id": "sala-burton",
            "tier": "power",
            "t": "Before her death in 1987, Congresswoman Sala Burton asked supporters to back her; she won Burton’s seat in a special election that June",
            "k": ["sala burton", "burton", "special election"],
            "n": 0
        },
        {
            "id": "state-chair",
            "tier": "power",
            "t": "Chaired the California Democratic Party from 1981 to 1983",
            "k": ["california democratic party", "chaired", "1981"],
            "n": 0
        },
        {
            "id": "trinity",
            "tier": "power",
            "t": "Graduated from Trinity College in Washington, D.C., in 1962",
            "k": ["trinity college", "trinity", "1962"],
            "n": 0
        },
        {
            "id": "convention-1984",
            "tier": "power",
            "t": "Led the host committee for the 1984 Democratic National Convention in San Francisco, which nominated Geraldine Ferraro for vice president",
            "k": ["host committee", "geraldine ferraro", "ferraro", "1984"],
            "n": 0
        },
        {
            "id": "whip",
            "tier": "power",
            "t": "Defeated Steny Hoyer in 2001 to become House Democratic whip, the first woman whip; elected to replace Dick Gephardt as leader in late 2002",
            "k": ["whip", "steny hoyer", "hoyer", "gephardt"],
            "n": 0
        },
        {
            "id": "vote-219",
            "tier": "power",
            "t": "The House passed the Senate’s health bill 219–212 on March 21, 2010; Obama signed it two days later",
            "k": ["219–212", "march 21", "two days"],
            "n": 0
        },
        {
            "id": "inquiry",
            "tier": "power",
            "t": "Announced a formal impeachment inquiry into Trump in September 2019",
            "k": ["impeachment inquiry", "inquiry", "september 2019"],
            "n": 0
        },
        {
            "id": "tiananmen",
            "tier": "power",
            "t": "In 1991, unfurled a small banner in Tiananmen Square honoring those who died in the 1989 pro-democracy protests",
            "k": ["tiananmen", "banner", "1991"],
            "n": 0
        },
        {
            "id": "taiwan",
            "tier": "power",
            "t": "In August 2022, became the highest-ranking U.S. official to visit Taiwan in 25 years; the last had been Newt Gingrich (1997)",
            "k": ["taiwan", "august 2022", "newt gingrich", "gingrich"],
            "n": 0,
            "rabbit": "Newt Gingrich"
        },
        {
            "id": "speaker-emerita",
            "tier": "power",
            "t": "Stepped down as party leader after the 2022 elections; Hakeem Jeffries succeeded her, and Democrats named her “Speaker Emerita”",
            "k": ["speaker emerita", "emerita", "hakeem jeffries", "jeffries"],
            "n": 0
        },
        {
            "id": "firsts",
            "tier": "power",
            "t": "The 52nd Speaker, and also the first Californian and the first Italian American to hold the job",
            "k": ["italian american", "californian", "52nd"],
            "n": 0
        },
        {
            "id": "ledbetter",
            "tier": "power",
            "t": "Led the House as it passed the Lilly Ledbetter Fair Pay Act (2009), the first bill Obama signed",
            "k": ["lilly ledbetter", "ledbetter", "fair pay act"],
            "n": 0
        },
        {
            "id": "chips",
            "tier": "power",
            "t": "In her second stretch as Speaker, the House passed the infrastructure law (2021) and the CHIPS and Science Act (2022)",
            "k": ["chips and science act", "chips", "infrastructure"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Order of the Speakers",
        "body": "Nancy Pelosi held the gavel twice, so the Speakers around her get mixed up: Dennis Hastert (1999–2007), Pelosi (2007–2011), John Boehner (2011–2015), Paul Ryan (2015–2019), Pelosi again (2019–2023), and Kevin McCarthy (2023). Newt Gingrich, Speaker from 1995 to 1999, also turns up in her questions because he was the last official of her rank to visit Taiwan before her 2022 trip.",
        "fix": "Pelosi clues: San Francisco, her father the Baltimore mayor, the “marble ceiling,” the 2010 health-care vote, and both Trump impeachments. Any clue about the first woman Speaker can only mean Pelosi, and saying just “Pelosi” is enough.",
        "line": "Real answer line: Nancy <b><u>Pelosi</u></b> (accept Nancy Patricia D’Alesandro <u>Pelosi</u>)"
    },
    "tests": {
        "right": [
            "Nancy Pelosi",
            "Pelosi",
            "Speaker Pelosi",
            "Nancy Pelosy",
            "Nancy D'Alesandro Pelosi",
            "Nancy Patricia Pelosi"
        ],
        "prompt": [],
        "wrong": [
            "John Boehner",
            "Newt Gingrich",
            "Kevin McCarthy",
            "Paul Pelosi",
            "Thomas D'Alesandro",
            "Hakeem Jeffries",
            "Nancy Reagan",
            "Dennis Hastert"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
