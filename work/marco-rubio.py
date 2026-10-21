import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TIP = "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."

data = {
    "id": "marco-rubio",
    "name": "Marco Rubio",
    "mono": "MR",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "Florida senator from 2011 to 2025 · Confirmed as Secretary of State in 2025",
    "dates": "Born 1971; U.S. senator 2011–2025",
    "briefing": "Marco Rubio, the son of Cuban immigrants, grew up in Miami and Las Vegas and became the first Cuban American Speaker of the Florida House. Elected to the U.S. Senate in 2010, he represented Florida from 2011 to 2025, ran for the Republican presidential nomination in 2016, and helped write a 2013 immigration bill as part of the “Gang of Eight.” In January 2025, the Senate voted 99–0 to confirm him as Secretary of State.",
    "answerHtml": "Marco <b><u>Rubio</u></b> (prompt on <u>Marco</u>; do not accept “Ted Cruz” or “Jeb Bush”)",
    "accept": [
        "marco rubio",
        "rubio",
        "marco antonio rubio",
        "senator rubio",
        "secretary rubio"
    ],
    "prompt": [
        "marco"
    ],
    "reject": [
        "ted cruz",
        "rafael cruz",
        "cruz",
        "jeb bush",
        "bush",
        "rick scott",
        "charlie crist",
        "crist",
        "kendrick meek",
        "ron desantis",
        "desantis",
        "ashley moody",
        "mel martinez",
        "bob menendez",
        "menendez",
        "john mccain",
        "lindsey graham",
        "jeff flake",
        "chuck schumer",
        "dick durbin",
        "michael bennet",
        "donald trump",
        "jd vance",
        "j d vance",
        "doug burgum",
        "mike pompeo",
        "antony blinken",
        "patrick murphy",
        "val demings",
        "ricky rubio",
        "marco polo",
        "fidel castro"
    ],
    "tests": {
        "right": [
            "Marco Rubio",
            "Rubio",
            "Senator Rubio",
            "Marco Antonio Rubio",
            "Marco Rubbio",
            "Secretary Rubio"
        ],
        "prompt": [
            "Marco"
        ],
        "wrong": [
            "Ted Cruz",
            "Jeb Bush",
            "Rick Scott",
            "Charlie Crist",
            "Ron DeSantis",
            "Ricky Rubio",
            "Mike Pompeo",
            "Donald Trump"
        ]
    },
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Marco_Rubio",
    "qb": {
        "q": "Rubio",
        "found": 0,
        "tip": TIP
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "This politician played college football for one year at Tarkio College in Missouri before earning degrees from the University of Florida and the University of Miami’s law school. He won his first election in 1998, to the city commission of West Miami.",
            "r": "He later represented Florida in the U.S. Senate from 2011 to 2025. For 10 points, name this son of Cuban immigrants who ran for president in 2016."
        },
        {
            "p": "As Speaker of a state House, this politician asked citizens to send in suggestions and published the best ones in a book called _100 Innovative Ideas for Florida’s Future_. He became the first Cuban American to lead that chamber, serving as its Speaker from 2006 to 2008.",
            "r": "For 10 points, name this Florida Republican who served in the U.S. Senate from 2011 to 2025."
        },
        {
            "p": "In a 2010 Senate race, this candidate trailed Florida’s governor, Charlie Crist, in early Republican primary polls, but Crist left the party to run as an independent. This candidate then won a three-way November election against Crist and Democrat Kendrick Meek.",
            "r": "For 10 points, name this Cuban American Republican who represented Florida in the U.S. Senate from 2011 to 2025."
        },
        {
            "p": "In 2013, this senator joined John McCain, Chuck Schumer, and five other senators in a bipartisan group that wrote a major immigration bill. That bill passed the Senate by a vote of 68 to 32 but never came to a vote in the House of Representatives.",
            "r": "That group was called the “Gang of Eight.” For 10 points, name this Florida senator who later became Secretary of State."
        },
        {
            "p": "This candidate announced a presidential campaign in April 2015 at Miami’s Freedom Tower, where many Cuban exiles had been welcomed decades earlier. In the 2016 Republican primaries, he won the Minnesota caucuses and the primaries in Puerto Rico and Washington, D.C.",
            "r": "He dropped out of the race after losing the Florida primary to Donald Trump. For 10 points, name this senator who later became Secretary of State."
        },
        {
            "p": "In March 2022, the Senate passed this lawmaker’s Sunshine Protection Act, which would have made daylight saving time permanent, but the House never voted on it. He also co-wrote a 2021 law that blocks imports of goods made with forced labor in China’s Xinjiang [“shin-JYAHNG”] region.",
            "r": "For 10 points, name this Florida senator from 2011 to 2025 who became Secretary of State in 2025."
        },
        {
            "p": "As chairman of the Senate’s small business committee, this senator helped create the Paycheck Protection Program, which offered loans to businesses during the COVID-19 pandemic in 2020. That year, he also became acting chairman of the Senate Intelligence Committee, and he was its vice chairman from 2021 to 2025.",
            "r": "For 10 points, name this Republican who represented Florida in the Senate before becoming Secretary of State."
        },
        {
            "p": "This politician’s 2012 memoir, _An American Son_, describes the years his family spent in Las Vegas, where his father worked as a hotel bartender, before they moved back to Miami. His parents had come to the United States from Cuba in the 1950s.",
            "r": "For 10 points, name this Cuban American who represented Florida in the U.S. Senate from 2011 to 2025."
        },
        {
            "p": "After dropping out of the 2016 presidential race, this politician changed his earlier decision not to seek reelection to his Senate seat, and he went on to defeat Democrat Patrick Murphy that November. In 2022, he won a third term by defeating Val Demings.",
            "r": "For 10 points, name this Florida senator who resigned his seat in January 2025 to become Secretary of State."
        },
        {
            "p": "In May 2025, this man was named interim national security adviser, becoming the first person to hold that job and his cabinet post at the same time after Henry Kissinger in the 1970s. Months earlier, the Senate had voted 99 to 0 to confirm him for that cabinet post.",
            "r": "He was the first Latino to hold that office. For 10 points, name this former Florida senator who became Secretary of State in 2025."
        },
        {
            "p": "When this man resigned from the Senate in January 2025, Florida governor Ron DeSantis appointed state attorney general Ashley Moody to fill his seat. Fourteen years earlier, he had taken over the seat once held by Mel Martinez, another Cuban American Republican.",
            "r": "For 10 points, name this Floridian who became Secretary of State under Donald Trump in 2025."
        },
        {
            "p": "Donald Trump chose J.D. Vance as his running mate in July 2024 over a short list of finalists that included North Dakota’s governor, Doug Burgum, and this senator from Florida. Both Burgum and this man later joined Trump’s cabinet.",
            "r": "This man was confirmed as Secretary of State in January 2025. For 10 points, name this son of Cuban immigrants."
        },
        {
            "p": "After Barack Obama’s 2013 State of the Union address, this senator delivered his party’s official response, giving it in both English and Spanish. In 2016, he ran for president against Ted Cruz, a fellow Cuban American senator, and Jeb Bush.",
            "r": "Bush had been the governor of this senator’s home state. For 10 points, name this Florida Republican who became Secretary of State in 2025."
        },
        {
            "p": "In February 2025, this cabinet member was also named acting head of the U.S. Agency for International Development, the government’s main foreign-aid agency, and acting Archivist of the United States. Earlier, he had served as Speaker of the Florida House.",
            "r": "He had represented Florida in the U.S. Senate from 2011 to 2025. For 10 points, name this man who became Secretary of State in January 2025."
        },
        {
            "p": "Florida’s term limits forced this politician to leave the state House in 2008, after eight years there, and he then taught classes as an adjunct professor at Florida International University. Two years later, he won an election to the U.S. Senate.",
            "r": "For 10 points, name this Cuban American Republican who served as a senator from 2011 to 2025."
        }
    ],
    "clues": [
        {
            "id": "senator",
            "tier": "giveaway",
            "t": "Republican U.S. senator from Florida (2011–2025)",
            "k": ["senator", "florida", "republican"],
            "n": 0
        },
        {
            "id": "cuban",
            "tier": "giveaway",
            "t": "Son of Cuban immigrants; born in Miami in 1971",
            "k": ["cuban immigrants", "cuban", "miami", "1971"],
            "n": 0,
            "rabbit": "Cuba"
        },
        {
            "id": "president-2016",
            "tier": "giveaway",
            "t": "Ran for the Republican presidential nomination in 2016, which Donald Trump won",
            "k": ["presidential nomination", "2016", "donald trump"],
            "n": 0,
            "rabbit": "Donald Trump"
        },
        {
            "id": "secretary",
            "tier": "giveaway",
            "t": "Confirmed as Secretary of State in January 2025, under President Donald Trump",
            "k": ["secretary of state", "january 2025"],
            "n": 0,
            "rabbit": "Secretary of State"
        },
        {
            "id": "speaker",
            "tier": "middle",
            "t": "First Cuban American Speaker of the Florida House of Representatives (2006–2008)",
            "k": ["speaker", "florida house", "2006"],
            "n": 0
        },
        {
            "id": "gang-of-eight",
            "tier": "middle",
            "t": "Part of the bipartisan “Gang of Eight” that wrote a 2013 immigration bill; it passed the Senate 68–32, but the House never voted on it",
            "k": ["gang of eight", "immigration", "bipartisan"],
            "n": 0
        },
        {
            "id": "crist",
            "tier": "middle",
            "t": "Won the 2010 Senate race over Democrat Kendrick Meek and Governor Charlie Crist, who had left the Republican Party to run as an independent",
            "k": ["charlie crist", "kendrick meek", "independent", "2010"],
            "n": 0
        },
        {
            "id": "cruz-bush",
            "tier": "middle",
            "t": "In the 2016 race, faced Ted Cruz, another Cuban American senator, and Jeb Bush, a former governor of Florida",
            "k": ["ted cruz", "jeb bush", "cuban american"],
            "n": 0
        },
        {
            "id": "florida-primary",
            "tier": "middle",
            "t": "Dropped out of the 2016 race after losing the Florida primary to Donald Trump (March 15, 2016)",
            "k": ["florida primary", "march 15", "dropped out"],
            "n": 0
        },
        {
            "id": "confirmed-99",
            "tier": "middle",
            "t": "The Senate confirmed him 99–0 on January 20, 2025; he was the first Latino Secretary of State",
            "k": ["99–0", "first latino", "latino"],
            "n": 0
        },
        {
            "id": "national-security",
            "tier": "middle",
            "t": "Also named interim national security adviser (May 2025), the first to hold both jobs at once after Henry Kissinger",
            "k": ["national security adviser", "henry kissinger", "kissinger"],
            "n": 0
        },
        {
            "id": "memoir",
            "tier": "middle",
            "t": "Wrote the memoir _An American Son_ (2012); spent part of his childhood in Las Vegas, where his father was a hotel bartender",
            "k": ["an american son", "memoir", "las vegas"],
            "n": 0
        },
        {
            "id": "sotu",
            "tier": "middle",
            "t": "Gave the Republican response to Barack Obama’s 2013 State of the Union address, in English and in Spanish",
            "k": ["state of the union", "spanish", "2013"],
            "n": 0
        },
        {
            "id": "tarkio",
            "tier": "power",
            "t": "Played a season of college football at Tarkio College in Missouri, then graduated from the University of Florida and the University of Miami’s law school",
            "k": ["tarkio", "football", "university of florida", "university of miami"],
            "n": 0
        },
        {
            "id": "west-miami",
            "tier": "power",
            "t": "First won office in 1998, on the West Miami city commission",
            "k": ["west miami", "city commission", "1998"],
            "n": 0
        },
        {
            "id": "ideas",
            "tier": "power",
            "t": "As Speaker, published _100 Innovative Ideas for Florida’s Future_, built from citizens’ suggestions",
            "k": ["100 innovative ideas", "innovative", "suggestions"],
            "n": 0
        },
        {
            "id": "term-limits",
            "tier": "power",
            "t": "Left the Florida House in 2008 because of term limits, then taught as an adjunct professor at Florida International University",
            "k": ["term limits", "adjunct professor", "florida international"],
            "n": 0
        },
        {
            "id": "freedom-tower",
            "tier": "power",
            "t": "Announced his presidential campaign at Miami’s Freedom Tower, where Cuban exiles were once welcomed (April 2015)",
            "k": ["freedom tower", "april 2015", "exiles"],
            "n": 0
        },
        {
            "id": "minnesota",
            "tier": "power",
            "t": "Won only three 2016 contests: the Minnesota caucuses and the Puerto Rico and Washington, D.C., primaries",
            "k": ["minnesota", "puerto rico", "washington, d.c."],
            "n": 0
        },
        {
            "id": "reelection",
            "tier": "power",
            "t": "Changed his mind and ran for reelection in 2016, defeating Patrick Murphy; defeated Val Demings in 2022",
            "k": ["patrick murphy", "val demings", "reelection"],
            "n": 0
        },
        {
            "id": "ppp",
            "tier": "power",
            "t": "As chairman of the Senate small business committee, helped create the Paycheck Protection Program (2020)",
            "k": ["paycheck protection program", "small business", "2020"],
            "n": 0
        },
        {
            "id": "intelligence",
            "tier": "power",
            "t": "Acting chairman (2020) and then vice chairman (2021–2025) of the Senate Intelligence Committee",
            "k": ["intelligence committee", "vice chairman", "acting chairman"],
            "n": 0
        },
        {
            "id": "sunshine",
            "tier": "power",
            "t": "His Sunshine Protection Act, to make daylight saving time permanent, passed the Senate in 2022 but not the House",
            "k": ["sunshine protection act", "daylight saving time", "2022"],
            "n": 0
        },
        {
            "id": "uyghur",
            "tier": "power",
            "t": "Co-wrote a 2021 law blocking imports of goods made with forced labor in China’s Xinjiang region",
            "k": ["forced labor", "xinjiang", "2021"],
            "n": 0
        },
        {
            "id": "vp-shortlist",
            "tier": "power",
            "t": "A finalist to be Donald Trump’s 2024 running mate, along with Doug Burgum, before Trump chose J.D. Vance",
            "k": ["running mate", "doug burgum", "j.d. vance", "vance"],
            "n": 0
        },
        {
            "id": "moody",
            "tier": "power",
            "t": "Governor Ron DeSantis appointed Ashley Moody to his Senate seat (January 2025); he had won the seat once held by Mel Martinez",
            "k": ["ashley moody", "ron desantis", "mel martinez"],
            "n": 0
        },
        {
            "id": "usaid",
            "tier": "power",
            "t": "In February 2025, also became acting head of the U.S. Agency for International Development and acting Archivist of the United States",
            "k": ["agency for international development", "archivist", "february 2025"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Which Cuban American senator?",
        "body": "Ted Cruz, a Cuban American Republican elected to the Senate from Texas in 2012, also ran for president in 2016, finishing second to Donald Trump. Jeb Bush, a former governor of Florida, ran in 2016 as well, and Rick Scott, Florida’s governor from 2011 to 2019, became a U.S. senator from Florida in 2019. Florida clues alone are not enough to tell these men apart.",
        "fix": "The Florida House speakership, the Gang of Eight, Charlie Crist, the Freedom Tower, and Secretary of State mean Rubio. Texas and the 2016 Iowa caucuses mean Cruz; a former governor whose father and brother were presidents means Jeb Bush. “Marco” alone earns a prompt, so say “Rubio.”",
        "line": "Real answer line: Marco <b><u>Rubio</u></b> (prompt on <u>Marco</u>; do not accept “Ted Cruz” or “Jeb Bush”)"
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
