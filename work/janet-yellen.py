import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "janet-yellen",
    "name": "Janet Yellen",
    "mono": "JY",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "First woman to chair the Federal Reserve · Treasury Secretary, 2021–2025",
    "dates": "Born 1946",
    "briefing": "Janet Yellen grew up in Brooklyn, earned a Ph.D. in economics at Yale, and taught for years at the University of California, Berkeley. In 2014 she became the first woman to chair the Federal Reserve, America’s central bank, and in 2021 she became the first woman to serve as Secretary of the Treasury. She was the first person ever to lead the Fed, the Treasury, and the White House Council of Economic Advisers.",
    "answerHtml": "Janet <b><u>Yellen</u></b> (accept Janet Louise <u>Yellen</u>)",
    "accept": [
        "janet yellen",
        "yellen",
        "janet louise yellen",
        "janet l yellen",
        "secretary yellen",
        "chair yellen",
        "chairwoman yellen"
    ],
    "prompt": [
        "janet"
    ],
    "reject": [
        "jerome powell",
        "jay powell",
        "powell",
        "ben bernanke",
        "bernanke",
        "alan greenspan",
        "greenspan",
        "paul volcker",
        "volcker",
        "george akerlof",
        "akerlof",
        "steven mnuchin",
        "mnuchin",
        "scott bessent",
        "henry paulson",
        "timothy geithner",
        "lawrence summers",
        "larry summers",
        "robert rubin",
        "lael brainard",
        "christine lagarde",
        "james tobin",
        "janet reno",
        "janet napolitano",
        "janet jackson",
        "alexander hamilton",
        "kamala harris"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Janet_Yellen",
    "qb": {
        "q": "Yellen",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "This economist wrote her doctoral dissertation at Yale under James Tobin, who later won a Nobel Prize, and then taught at Harvard and the London School of Economics. She spent most of her teaching career at the University of California, Berkeley.",
            "r": "In 2014, she became the first woman to chair the Federal Reserve. For 10 points, name this economist who later served as Treasury Secretary."
        },
        {
            "p": "This economist met her husband, George Akerlof, in the Federal Reserve’s cafeteria; he later won a Nobel Prize for research that included his paper “The Market for ‘Lemons.’” Together they studied efficiency wages, the idea that paying workers more than the going rate can make them work harder.",
            "r": "For 10 points, name this economist who in 2014 became the first woman to chair the Federal Reserve."
        },
        {
            "p": "From 1997 to 1999, this economist chaired Bill Clinton’s Council of Economic Advisers, after more than two years as a member of the Federal Reserve’s Board of Governors. She then returned to teaching at the University of California, Berkeley.",
            "r": "In 2014, she became the first woman to chair the Fed. For 10 points, name this economist who later served as Secretary of the Treasury."
        },
        {
            "p": "From 2004 to 2010, this economist was president of the Federal Reserve Bank of San Francisco, whose district covers nine western states. She then served as vice chair of the Federal Reserve’s board under Ben Bernanke.",
            "r": "For 10 points, name this economist who succeeded Bernanke in 2014, becoming the first woman to lead the Federal Reserve."
        },
        {
            "p": "In October 2013, Barack Obama chose this vice chair of the Federal Reserve to lead it, after Lawrence Summers withdrew from consideration. Summers had been Treasury Secretary under Bill Clinton. The Senate confirmed her in January 2014.",
            "r": "She replaced Ben Bernanke and became the first woman in that job. For 10 points, name this Federal Reserve chair from 2014 to 2018."
        },
        {
            "p": "In December 2015, the central bank led by this economist raised its key interest rate for the first time in almost ten years. It had kept that rate near zero for seven years after the financial crisis of 2008.",
            "r": "For 10 points, name this economist who chaired the Federal Reserve from 2014 to 2018, the first woman to do so."
        },
        {
            "p": "In October 2017, the central bank led by this economist began slowly shrinking the huge supply of bonds it had bought to help the economy recover from the 2008 financial crisis. By then, it had raised interest rates four times.",
            "r": "Jerome Powell succeeded her in early 2018. For 10 points, name this economist who in 2014 became the first woman to chair the Federal Reserve."
        },
        {
            "p": "Joe Biden chose this economist for his cabinet, and in January 2021 she became the first woman to hold a job first held by Alexander Hamilton. She followed Steven Mnuchin in that post.",
            "r": "She had earlier been the first woman to chair the Federal Reserve. For 10 points, name this Treasury Secretary from 2021 to 2025."
        },
        {
            "p": "In 2021, this official pushed for a global minimum tax of 15 percent on large corporations, and more than 130 countries signed on to the plan through the Organisation for Economic Co-operation and Development.",
            "r": "For 10 points, name this economist who served as Treasury Secretary from 2021 to 2025 after chairing the Federal Reserve."
        },
        {
            "p": "This economist was the valedictorian of Fort Hamilton High School in Brooklyn, then graduated from Brown University in 1967 and earned a doctorate from Yale. She was an assistant professor at Harvard in the 1970s.",
            "r": "For 10 points, name this economist who became the first woman to chair the Federal Reserve and, later, the first woman to serve as Treasury Secretary."
        },
        {
            "p": "In 2023, this official warned Congress that the government could run out of money to pay all of its bills in early June unless lawmakers raised the debt ceiling. Congress suspended the limit days before that deadline.",
            "r": "For 10 points, name this Treasury Secretary under Joe Biden, who had earlier chaired the Federal Reserve."
        },
        {
            "p": "Under the American Rescue Plan of 2021, a law meant to help the economy recover from the COVID-19 pandemic, this official’s department sent $1,400 relief payments to most Americans. That July, it also began sending families monthly child tax credit payments.",
            "r": "She was the first person to have led the Treasury, the Federal Reserve, and the Council of Economic Advisers. For 10 points, name this economist."
        },
        {
            "p": "In March 2023, after Silicon Valley Bank collapsed, this official joined leaders of the Federal Reserve and the Federal Deposit Insurance Corporation in promising that all of the bank’s depositors would get their money back.",
            "r": "For 10 points, name this Treasury Secretary under Joe Biden, who had chaired the Federal Reserve from 2014 to 2018."
        },
        {
            "p": "As head of America’s central bank, this economist often pointed to its “dual mandate” from Congress to aim for both maximum employment and stable prices. She had earlier written research papers on unemployment with her husband, George Akerlof.",
            "r": "For 10 points, name this economist who was the first woman to chair the Federal Reserve."
        },
        {
            "p": "In July 2023, this cabinet official traveled to Beijing to meet China’s premier, Li Qiang, hoping to ease tensions between the world’s two largest economies. As head of her department, she also chaired the Financial Stability Oversight Council.",
            "r": "For 10 points, name this Treasury Secretary under Joe Biden, who had been the first woman to chair the Federal Reserve."
        }
    ],
    "clues": [
        {
            "id": "fed-chair",
            "tier": "giveaway",
            "t": "Chair of the Federal Reserve, the U.S. central bank, from 2014 to 2018, the first woman in that job",
            "k": ["federal reserve", "first woman", "central bank"],
            "n": 0,
            "rabbit": "Federal Reserve System"
        },
        {
            "id": "treasury",
            "tier": "giveaway",
            "t": "Secretary of the Treasury under Joe Biden (2021–2025), the first woman in that job",
            "k": ["treasury", "joe biden", "2021"],
            "n": 0
        },
        {
            "id": "bernanke-powell",
            "tier": "giveaway",
            "t": "Succeeded Ben Bernanke as Fed chair in 2014; Jerome Powell succeeded her in 2018",
            "k": ["ben bernanke", "bernanke", "jerome powell", "powell"],
            "n": 0,
            "rabbit": "Ben Bernanke"
        },
        {
            "id": "berkeley",
            "tier": "giveaway",
            "t": "Economist who taught for many years at the University of California, Berkeley",
            "k": ["berkeley", "economist"],
            "n": 0
        },
        {
            "id": "three-jobs",
            "tier": "middle",
            "t": "The first person to lead all three: the Fed, the Treasury, and the White House Council of Economic Advisers",
            "k": ["first person", "all three"],
            "n": 0
        },
        {
            "id": "cea",
            "tier": "middle",
            "t": "Chaired Bill Clinton’s Council of Economic Advisers (1997–1999)",
            "k": ["council of economic advisers", "bill clinton"],
            "n": 0
        },
        {
            "id": "obama",
            "tier": "middle",
            "t": "Barack Obama nominated her to lead the Fed in October 2013",
            "k": ["barack obama", "2013"],
            "n": 0,
            "rabbit": "Barack Obama"
        },
        {
            "id": "vice-chair",
            "tier": "middle",
            "t": "Vice chair of the Federal Reserve (2010–2014), under Ben Bernanke",
            "k": ["vice chair", "2010"],
            "n": 0
        },
        {
            "id": "rate-hike",
            "tier": "middle",
            "t": "December 2015: the Fed raised interest rates for the first time in almost ten years",
            "k": ["interest rates", "december 2015"],
            "n": 0
        },
        {
            "id": "mnuchin",
            "tier": "middle",
            "t": "Followed Steven Mnuchin at the Treasury, a job first held by Alexander Hamilton",
            "k": ["steven mnuchin", "mnuchin", "alexander hamilton"],
            "n": 0,
            "rabbit": "Alexander Hamilton"
        },
        {
            "id": "tobin",
            "tier": "power",
            "t": "Earned her Ph.D. at Yale under future Nobel winner James Tobin; taught at Harvard and the London School of Economics",
            "k": ["james tobin", "tobin", "yale", "harvard"],
            "n": 0
        },
        {
            "id": "akerlof",
            "tier": "power",
            "t": "Met her husband, George Akerlof, at the Fed; he won a Nobel Prize for research including “The Market for ‘Lemons’”",
            "k": ["george akerlof", "akerlof", "lemons"],
            "n": 0
        },
        {
            "id": "efficiency-wages",
            "tier": "power",
            "t": "With Akerlof, studied efficiency wages: paying more than the going rate can make people work harder",
            "k": ["efficiency wages", "efficiency"],
            "n": 0
        },
        {
            "id": "fed-governor",
            "tier": "power",
            "t": "Member of the Fed’s Board of Governors (1994–1997), appointed by Bill Clinton",
            "k": ["board of governors", "1994"],
            "n": 0
        },
        {
            "id": "san-francisco",
            "tier": "power",
            "t": "President of the Federal Reserve Bank of San Francisco (2004–2010), whose district covers nine western states",
            "k": ["san francisco", "nine western states"],
            "n": 0
        },
        {
            "id": "summers",
            "tier": "power",
            "t": "Got the Fed nomination after Lawrence Summers withdrew (2013)",
            "k": ["lawrence summers", "summers"],
            "n": 0
        },
        {
            "id": "balance-sheet",
            "tier": "power",
            "t": "In October 2017, the Fed under her began shrinking the bonds it had bought after the 2008 crisis",
            "k": ["shrinking", "bonds", "2017"],
            "n": 0
        },
        {
            "id": "global-tax",
            "tier": "power",
            "t": "Pushed for a 15 percent global minimum tax on big corporations; more than 130 countries agreed (2021)",
            "k": ["global minimum tax", "15 percent"],
            "n": 0
        },
        {
            "id": "rescue-plan",
            "tier": "power",
            "t": "Her department sent $1,400 relief payments under the American Rescue Plan (2021)",
            "k": ["american rescue plan", "relief payments"],
            "n": 0
        },
        {
            "id": "debt-ceiling",
            "tier": "power",
            "t": "Warned Congress in 2023 that the government could run out of money unless the debt ceiling was raised",
            "k": ["debt ceiling", "2023"],
            "n": 0
        },
        {
            "id": "svb",
            "tier": "power",
            "t": "Helped promise that all of Silicon Valley Bank’s depositors would be repaid (March 2023)",
            "k": ["silicon valley bank", "depositors"],
            "n": 0
        },
        {
            "id": "fort-hamilton",
            "tier": "power",
            "t": "Valedictorian of Fort Hamilton High School in Brooklyn; graduated from Brown University (1967)",
            "k": ["fort hamilton", "brown university", "brooklyn"],
            "n": 0
        },
        {
            "id": "dual-mandate",
            "tier": "power",
            "t": "Stressed the Fed’s “dual mandate” from Congress: maximum employment and stable prices",
            "k": ["dual mandate", "maximum employment"],
            "n": 0
        },
        {
            "id": "beijing",
            "tier": "power",
            "t": "Visited Beijing in July 2023 to meet China’s premier, Li Qiang",
            "k": ["beijing", "li qiang", "china"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Which Fed chair?",
        "body": "Federal Reserve chairs blur together in quiz bowl. Alan Greenspan led the Fed from 1987 to 2006, Ben Bernanke from 2006 to 2014, and Janet Yellen from 2014 to 2018, when Jerome Powell succeeded her. Yellen also led the Treasury from 2021 to 2025, so a question about “this Treasury Secretary” can want her too, while Henry Paulson and Steven Mnuchin were Treasury Secretaries who never led the Fed.",
        "fix": "The first woman to chair the Fed, Berkeley, George Akerlof, the Council of Economic Advisers, and Joe Biden’s Treasury mean Yellen. Princeton, the 2008 crisis, and “Helicopter Ben” mean Bernanke; Donald Trump’s 2017 pick to lead the Fed means Powell.",
        "line": "Real answer line: Janet <b><u>Yellen</u></b> (accept Janet Louise <u>Yellen</u>)"
    },
    "tests": {
        "right": [
            "Janet Yellen",
            "Yellen",
            "Janet Louise Yellen",
            "Secretary Yellen",
            "Janet Yellin",
            "Treasury Secretary Janet Yellen"
        ],
        "prompt": [
            "Janet"
        ],
        "wrong": [
            "Jerome Powell",
            "Ben Bernanke",
            "Alan Greenspan",
            "Janet Reno",
            "Steven Mnuchin",
            "George Akerlof",
            "Paul Volcker",
            "Christine Lagarde"
        ]
    }
}

out = ROOT / "topics" / f"{data['id']}.json"
with open(out, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("wrote", out)
