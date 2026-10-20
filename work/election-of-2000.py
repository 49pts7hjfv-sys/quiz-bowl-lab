import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "election-of-2000",
    "name": "Election of 2000",
    "mono": "E00",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "Bush beats Gore by 537 Florida votes · Recount ended by the Supreme Court",
    "dates": "Held November 7, 2000; decided in December",
    "briefing": "The 2000 presidential race between Texas governor George W. Bush and Vice President Al Gore came down to Florida, where the vote was so close that it led to weeks of recounts and lawsuits over “butterfly ballots” and “hanging chads.” On December 12, the Supreme Court’s ruling in _Bush v. Gore_ ended the recount, leaving Bush ahead by 537 votes. Gore won the national popular vote but lost in the Electoral College, 271 to 266.",
    "answerHtml": "Election of <b><u>2000</u></b> (or <b><u>2000</u></b> presidential election; prompt on <u>presidential election</u> or <u>Florida recount</u>; do not accept “Bush v. Gore”)",
    "accept": [
        "2000"
    ],
    "prompt": [
        "election",
        "the election",
        "presidential election",
        "the presidential election",
        "us presidential election",
        "florida recount",
        "the florida recount",
        "recount"
    ],
    "reject": [
        "1996",
        "2004",
        "1992",
        "1988",
        "2008",
        "2016",
        "2020",
        "1876",
        "1888",
        "1824",
        "1800",
        "1960",
        "2001",
        "2002",
        "bush v gore",
        "bush vs gore",
        "bush versus gore",
        "bush v palm beach county canvassing board"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/2000_United_States_presidential_election",
    "qb": {
        "q": "2000 presidential election",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "The Supreme Court ruled 7–2 that Florida’s recount in this election, which used different standards in different counties, violated the Equal Protection Clause. By a 5–4 vote, the justices also ruled that there was no time left for a new recount.",
            "r": "That December ruling, in _Bush v. Gore_, ended the recount. For 10 points, name this presidential election."
        },
        {
            "p": "Theresa LePore, the elections supervisor of Palm Beach County, designed a two-page “butterfly ballot” for this election that some voters said led them to vote for Pat Buchanan by mistake. Recount workers in Florida later examined punch-card ballots for “hanging” or “dimpled” chads.",
            "r": "Florida’s result decided the winner. For 10 points, name this election in which George W. Bush defeated Al Gore."
        },
        {
            "p": "Florida’s secretary of state, Katherine Harris, certified one candidate as the winner of her state in this election by just 537 votes. That candidate had led by fewer than 2,000 votes after the first count on election night, which set off an automatic recount under Florida law.",
            "r": "That candidate, George W. Bush, became president. For 10 points, name this election in which he defeated Al Gore."
        },
        {
            "p": "Ralph Nader won more than 97,000 votes in Florida as the Green Party’s candidate in this election, while Pat Buchanan ran on the Reform Party ticket. Nationwide, Nader won almost 3 percent of the popular vote.",
            "r": "For 10 points, name this election decided by a few hundred votes in Florida, in which George W. Bush beat Al Gore."
        },
        {
            "p": "In this election, Senator Joe Lieberman of Connecticut became the first Jewish candidate on a major party’s presidential ticket. His opponent for vice president, Dick Cheney, had led the search for a running mate before being chosen himself.",
            "r": "For 10 points, name this election in which Lieberman’s running mate, Al Gore, lost to George W. Bush."
        },
        {
            "p": "One elector from Washington, D.C., left her ballot blank in protest after this election, so the winner’s final margin in the Electoral College was 271 votes to 266. The loser won the national popular vote by more than half a million votes.",
            "r": "For 10 points, name this election in which Al Gore won more votes nationwide but lost to George W. Bush."
        },
        {
            "p": "On election night, TV networks projected that one candidate had won Florida, took it back, and later declared that his opponent had won the state. The first candidate then phoned his opponent to concede, only to call back later that night and take back his concession.",
            "r": "For 10 points, name this election that ended weeks later when Al Gore conceded to George W. Bush."
        },
        {
            "p": "One candidate in this election lost his home state of Tennessee, whose 11 electoral votes would have given him the presidency. That candidate, the sitting vice president, also lost Arkansas, the home state of the president he served under.",
            "r": "For 10 points, name this election in which Al Gore lost to George W. Bush."
        },
        {
            "p": "In this election, Hillary Clinton became the first First Lady elected to public office, winning a Senate seat from New York. Voters also chose a president who was the son of a former president, the first since John Quincy Adams.",
            "r": "For 10 points, name this election in which George W. Bush defeated Al Gore."
        },
        {
            "p": "During the legal fight after this election, former secretaries of state James Baker and Warren Christopher led the opposing campaigns’ teams. At the Supreme Court, Theodore Olson argued for one candidate and David Boies [“BOYZ”] argued for the other.",
            "r": "For 10 points, name this election decided by a Florida recount, in which George W. Bush beat Al Gore."
        },
        {
            "p": "Problems with punch-card voting machines in this election led Congress to pass the Help America Vote Act in 2002, which gave states money to buy new voting equipment and created the Election Assistance Commission.",
            "r": "For 10 points, name this election decided by a recount in Florida, which George W. Bush won over Al Gore."
        },
        {
            "p": "One candidate in this election described his philosophy as “compassionate conservatism,” while the other promised to protect Social Security money in a “lockbox.” The first candidate was the governor of Texas, and the second was the sitting vice president.",
            "r": "For 10 points, name this election in which George W. Bush defeated Al Gore."
        },
        {
            "p": "Before the final ruling in this election’s legal fight, the U.S. Supreme Court unanimously sent back a Florida decision in _Bush v. Palm Beach County Canvassing Board_. On December 8, the Florida Supreme Court ordered a statewide hand recount of ballots with no machine-recorded vote for president.",
            "r": "For 10 points, name this election in which a recount in Florida decided whether George W. Bush or Al Gore won."
        },
        {
            "p": "One candidate in this election conceded in a televised speech on December 13, the day after a Supreme Court ruling ended the Florida recount. That candidate had served eight years as vice president under Bill Clinton.",
            "r": "For 10 points, name this election in which Al Gore lost to George W. Bush."
        },
        {
            "p": "This was the first election since 1888 in which the winner of the national popular vote lost the presidency. Florida’s 25 electoral votes decided it, and the winning candidate’s younger brother Jeb was governor of Florida at the time.",
            "r": "For 10 points, name this election in which George W. Bush defeated Vice President Al Gore after weeks of recounts."
        }
    ],
    "clues": [
        {
            "id": "bush-gore",
            "tier": "giveaway",
            "t": "Republican George W. Bush, governor of Texas, defeated Democrat Al Gore, the sitting vice president",
            "k": ["george w. bush", "al gore", "gore", "vice president"],
            "n": 0,
            "rabbit": "George W. Bush"
        },
        {
            "id": "florida-recount",
            "tier": "giveaway",
            "t": "Decided by a disputed recount in Florida, which Bush won by 537 votes",
            "k": ["florida", "recount", "537"],
            "n": 0
        },
        {
            "id": "bush-v-gore",
            "tier": "giveaway",
            "t": "The Supreme Court’s ruling in _Bush v. Gore_ (December 12) ended the Florida recount",
            "k": ["bush v. gore", "supreme court", "december 12"],
            "n": 0
        },
        {
            "id": "popular-vote",
            "tier": "giveaway",
            "t": "Gore won the national popular vote but lost the Electoral College, 271 to 266",
            "k": ["popular vote", "electoral college", "271", "266"],
            "n": 0,
            "rabbit": "Electoral College"
        },
        {
            "id": "butterfly",
            "tier": "middle",
            "t": "Palm Beach County’s confusing “butterfly ballot”: some voters said they chose Pat Buchanan by mistake",
            "k": ["butterfly ballot", "palm beach", "buchanan"],
            "n": 0
        },
        {
            "id": "chads",
            "tier": "middle",
            "t": "Recount workers examined punch-card ballots with “hanging” and “dimpled” chads",
            "k": ["chads", "punch-card", "hanging", "dimpled"],
            "n": 0
        },
        {
            "id": "nader",
            "tier": "middle",
            "t": "Ralph Nader, the Green Party candidate, won almost 3 percent nationally and more than 97,000 votes in Florida",
            "k": ["ralph nader", "nader", "green party"],
            "n": 0,
            "rabbit": "Ralph Nader"
        },
        {
            "id": "running-mates",
            "tier": "middle",
            "t": "Running mates: Dick Cheney (Bush) and Joe Lieberman (Gore), the first Jewish candidate on a major party’s ticket",
            "k": ["dick cheney", "cheney", "joe lieberman", "lieberman"],
            "n": 0
        },
        {
            "id": "katherine-harris",
            "tier": "middle",
            "t": "Florida’s secretary of state, Katherine Harris, certified Bush as the winner of the state",
            "k": ["katherine harris", "harris", "certified"],
            "n": 0
        },
        {
            "id": "election-night",
            "tier": "middle",
            "t": "On election night, TV networks called Florida for Gore, took it back, then called it for Bush; Gore conceded by phone, then took it back",
            "k": ["election night", "networks"],
            "n": 0
        },
        {
            "id": "jeb-bush",
            "tier": "middle",
            "t": "Bush’s younger brother Jeb was governor of Florida, whose 25 electoral votes decided the race",
            "k": ["jeb", "25 electoral votes", "governor of florida"],
            "n": 0
        },
        {
            "id": "gore-concedes",
            "tier": "middle",
            "t": "Gore conceded in a televised speech on December 13, the day after the Supreme Court’s ruling",
            "k": ["december 13", "televised speech", "conceded"],
            "n": 0
        },
        {
            "id": "since-1888",
            "tier": "middle",
            "t": "The first election since 1888 in which the national popular-vote winner lost",
            "k": ["since 1888", "1888"],
            "n": 0
        },
        {
            "id": "equal-protection",
            "tier": "power",
            "t": "_Bush v. Gore_: 7–2 that the recount’s differing county standards violated the Equal Protection Clause; 5–4 that no time remained for a new recount",
            "k": ["equal protection", "7–2", "5–4"],
            "n": 0
        },
        {
            "id": "lepore",
            "tier": "power",
            "t": "Palm Beach County’s elections supervisor, Theresa LePore, designed the two-page butterfly ballot",
            "k": ["theresa lepore", "lepore"],
            "n": 0
        },
        {
            "id": "automatic-recount",
            "tier": "power",
            "t": "Bush led by fewer than 2,000 votes after the first count, which set off an automatic recount under Florida law",
            "k": ["automatic recount", "2,000", "automatic"],
            "n": 0
        },
        {
            "id": "dc-elector",
            "tier": "power",
            "t": "A Washington, D.C., elector left her ballot blank in protest, so Gore finished with 266 electoral votes instead of 267",
            "k": ["washington, d.c.", "blank", "protest"],
            "n": 0
        },
        {
            "id": "baker-christopher",
            "tier": "power",
            "t": "Former secretaries of state James Baker (for Bush) and Warren Christopher (for Gore) led the legal teams",
            "k": ["james baker", "warren christopher", "baker"],
            "n": 0
        },
        {
            "id": "olson-boies",
            "tier": "power",
            "t": "Theodore Olson argued for Bush and David Boies argued for Gore at the Supreme Court",
            "k": ["theodore olson", "olson", "david boies", "boies"],
            "n": 0
        },
        {
            "id": "tennessee",
            "tier": "power",
            "t": "Gore lost his home state of Tennessee, whose 11 electoral votes would have made him president, and Bill Clinton’s home state of Arkansas",
            "k": ["tennessee", "11 electoral votes", "arkansas"],
            "n": 0
        },
        {
            "id": "hillary-senate",
            "tier": "power",
            "t": "Hillary Clinton won a Senate seat from New York, the first First Lady elected to public office",
            "k": ["hillary clinton", "first lady", "new york"],
            "n": 0,
            "rabbit": "Hillary Clinton"
        },
        {
            "id": "son-of-president",
            "tier": "power",
            "t": "Bush became the second son of a president to win the presidency, after John Quincy Adams",
            "k": ["john quincy adams", "son of a president"],
            "n": 0
        },
        {
            "id": "help-america-vote",
            "tier": "power",
            "t": "The Help America Vote Act (2002) paid states to replace old voting machines and created the Election Assistance Commission",
            "k": ["help america vote act", "election assistance commission", "voting machines"],
            "n": 0
        },
        {
            "id": "canvassing-board",
            "tier": "power",
            "t": "In _Bush v. Palm Beach County Canvassing Board_, the Supreme Court unanimously sent back an earlier Florida ruling",
            "k": ["canvassing board", "unanimously"],
            "n": 0
        },
        {
            "id": "florida-supreme-court",
            "tier": "power",
            "t": "On December 8, the Florida Supreme Court ordered a statewide hand recount of ballots with no machine-recorded vote for president",
            "k": ["florida supreme court", "december 8", "hand recount"],
            "n": 0
        },
        {
            "id": "slogans",
            "tier": "power",
            "t": "Bush called his philosophy “compassionate conservatism”; Gore promised a Social Security “lockbox”",
            "k": ["compassionate conservatism", "lockbox"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Election or court case?",
        "body": "This election’s most famous clues, the Florida recount, hanging chads, and the Supreme Court, also lead tossups whose answer is the case _Bush v. Gore_, and some questions ask for George W. Bush or Al Gore themselves. Answering “Bush v. Gore” when the question says “this election” is wrong, and so is naming the election when it asks for “this case.” The election of 1876, which also turned on disputed Florida votes, is a different answer.",
        "fix": "Listen for the noun: “this election” wants 2000, “this case” or “this ruling” wants _Bush v. Gore_, and “this candidate” wants a person. Rutherford B. Hayes, Samuel Tilden, and a fifteen-member commission mean 1876, not 2000.",
        "line": "Real answer line: United States presidential election of <b><u>2000</u></b> (prompt on <u>presidential election</u>; do not accept “Bush v. Gore”)"
    },
    "tests": {
        "right": [
            "2000",
            "Election of 2000",
            "2000 presidential election",
            "the 2000 election",
            "Bush-Gore election of 2000"
        ],
        "prompt": [
            "presidential election",
            "Florida recount"
        ],
        "wrong": [
            "Bush v. Gore",
            "Election of 2004",
            "1876",
            "Election of 1992",
            "Al Gore",
            "1996"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
