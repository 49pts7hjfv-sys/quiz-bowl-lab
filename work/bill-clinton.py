import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "bill-clinton",
    "name": "Bill Clinton",
    "mono": "WJC",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "42nd U.S. President · Governor of Arkansas before the White House",
    "dates": "Born 1946; president 1993–2001",
    "briefing": "Bill Clinton was born in Hope, Arkansas, shook hands with President John F. Kennedy as a teenager, and became the nation’s youngest governor at 32. In 1992 he defeated President George H. W. Bush and independent Ross Perot to become the 42nd president, the first born after World War II. His two terms brought NAFTA, welfare reform, and a balanced federal budget; the House impeached him in 1998, and the Senate acquitted him in 1999.",
    "answerHtml": "<b><u>Bill Clinton</u></b> (accept <u>William</u> Jefferson <u>Clinton</u>; prompt on “Clinton” alone; do not accept “Hillary Clinton”)",
    "accept": [
        "bill clinton",
        "william clinton",
        "william jefferson clinton",
        "william j clinton",
        "william jefferson bill clinton",
        "president clinton",
        "william jefferson blythe iii",
        "william jefferson blythe"
    ],
    "prompt": [
        "clinton",
        "mr clinton",
        "governor clinton"
    ],
    "reject": [
        "hillary clinton",
        "hillary rodham clinton",
        "hillary",
        "hillary rodham",
        "chelsea clinton",
        "dewitt clinton",
        "george clinton",
        "henry clinton",
        "roger clinton",
        "al gore",
        "gore",
        "george h w bush",
        "george bush",
        "george w bush",
        "ross perot",
        "bob dole",
        "newt gingrich",
        "barack obama",
        "jimmy carter",
        "thomas jefferson"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Bill_Clinton",
    "qb": {
        "q": "Bill Clinton",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "In July 1963, a 16-year-old delegate to the American Legion’s Boys Nation program shook hands with President John F. Kennedy in the White House Rose Garden, a moment captured in a famous photograph. That teenager later said the meeting helped inspire him to enter public service.",
            "r": "For 10 points, name this man from Arkansas who became the 42nd U.S. president in 1993."
        },
        {
            "p": "After graduating from Georgetown University’s School of Foreign Service, this man spent two years at Oxford as a Rhodes Scholar. He earned a law degree from Yale in 1973, then lost his first race, for a seat in Congress, the following year.",
            "r": "At Yale, he had met his future wife, Hillary Rodham. For 10 points, name this Democrat who served as governor of Arkansas before becoming president in 1993."
        },
        {
            "p": "In 1978, at age 32, this former state attorney general was elected the nation’s youngest governor, but he lost his first reelection bid in 1980 to Republican Frank White. He won the job back two years later and kept it for about ten more years.",
            "r": "For 10 points, name this Arkansas governor who defeated George H. W. Bush in the 1992 presidential election."
        },
        {
            "p": "This politician’s long speech nominating Michael Dukakis at the 1988 Democratic convention drew cheers when he finally said “In closing.” He joked about it soon after on _The Tonight Show_, where he played the saxophone, and in 1992 he played the sax again, in sunglasses, on _The Arsenio Hall Show_.",
            "r": "That year, he won the presidency. For 10 points, name this longtime governor of Arkansas, the 42nd president."
        },
        {
            "p": "After finishing second to Paul Tsongas in the 1992 New Hampshire primary, this candidate called himself “the Comeback Kid.” His campaign film at that year’s Democratic convention was titled _The Man from Hope_, after the small town where he was born.",
            "r": "For 10 points, name this Arkansas Democrat who won the 1992 presidential election and served two terms."
        },
        {
            "p": "In 1992, this candidate chose Tennessee senator Al Gore as his running mate and beat both a sitting president and independent Ross Perot, who won about 19 percent of the popular vote. He became the first president born after World War II.",
            "r": "That sitting president was George H. W. Bush. For 10 points, name this 42nd president."
        },
        {
            "p": "The first major bill this president signed, the Family and Medical Leave Act, let many workers take unpaid time off to care for a new baby or a sick relative. That same year, he created the AmeriCorps national service program and signed the Brady Bill, requiring background checks for many handgun buyers.",
            "r": "His vice president was Al Gore. For 10 points, name this Democratic president who served from 1993 to 2001."
        },
        {
            "p": "Vice President Al Gore broke a tie in the Senate to pass this president’s 1993 budget plan, which raised taxes on the highest earners. A health care plan drawn up by a task force led by this president’s wife never came to a vote in Congress and was dropped in 1994.",
            "r": "For 10 points, name this Democratic president, a former governor of Arkansas and the husband of Hillary Rodham."
        },
        {
            "p": "In December 1993, this president signed a trade deal with Canada and Mexico that his predecessor had negotiated, despite opposition from many labor unions. During the 1992 campaign, Ross Perot had warned that the deal would cause a “giant sucking sound” of jobs heading south to Mexico.",
            "r": "That free-trade deal was NAFTA. For 10 points, name this 42nd president, a Democrat from Arkansas."
        },
        {
            "p": "After Republicans won control of both houses of Congress in 1994 with their “Contract with America,” this president clashed with Speaker Newt Gingrich over the budget, leading to two government shutdowns. In his 1996 State of the Union address, he declared that “the era of big government is over.”",
            "r": "That November, he won reelection over Republican Bob Dole. For 10 points, name this Democratic president from Arkansas."
        },
        {
            "p": "In 1996, this president signed a welfare reform law that replaced Aid to Families with Dependent Children with a new program that set time limits and work requirements. He also used a new “line-item veto” until the Supreme Court struck it down in 1998.",
            "r": "For 10 points, name this president, the first Democrat since Franklin Roosevelt to win two full terms."
        },
        {
            "p": "On the White House lawn in September 1993, this president stood between Israeli prime minister Yitzhak Rabin and PLO leader Yasser Arafat as they shook hands after signing the Oslo Accords. Two years later, his envoy Richard Holbrooke helped negotiate the Dayton Accords, which ended the war in Bosnia.",
            "r": "For 10 points, name this former Arkansas governor who served as president from 1993 to 2001."
        },
        {
            "p": "This president’s special envoy, former senator George Mitchell, chaired the talks that produced Northern Ireland’s 1998 Good Friday Agreement. In 1999, this president backed a NATO bombing campaign against Serbia to stop attacks on ethnic Albanians in Kosovo.",
            "r": "For 10 points, name this 42nd president, whose vice president was Al Gore."
        },
        {
            "p": "In early 1999, Chief Justice William Rehnquist presided over this president’s trial in the Senate, the first trial of its kind since Andrew Johnson’s in 1868. The Senate voted to acquit this president on both charges against him.",
            "r": "The House had impeached him in December 1998 on charges of perjury and obstruction of justice. For 10 points, name this 42nd president."
        },
        {
            "p": "This man won a Grammy Award for the audiobook of his 2004 memoir, _My Life_, and later served as the United Nations special envoy to Haiti. With George H. W. Bush, he raised money for victims of the 2004 Indian Ocean tsunami.",
            "r": "His presidential library is in Little Rock. For 10 points, name this 42nd president, the husband of Hillary Rodham."
        }
    ],
    "clues": [
        {
            "id": "42nd-president",
            "tier": "giveaway",
            "t": "42nd President of the United States (1993–2001), a Democrat",
            "k": ["42nd president", "forty-second", "democrat", "1993"],
            "n": 0
        },
        {
            "id": "arkansas",
            "tier": "giveaway",
            "t": "Governor of Arkansas (1979–1981 and 1983–1992); born in Hope, Arkansas",
            "k": ["arkansas", "governor", "hope"],
            "n": 0
        },
        {
            "id": "hillary",
            "tier": "giveaway",
            "t": "Husband of Hillary Rodham, a U.S. senator (2001–2009) and secretary of state (2009–2013)",
            "k": ["hillary rodham", "hillary", "rodham"],
            "n": 0,
            "rabbit": "Hillary Clinton"
        },
        {
            "id": "impeached",
            "tier": "giveaway",
            "t": "Impeached by the House in 1998 on charges of perjury and obstruction of justice; acquitted by the Senate in 1999",
            "k": ["impeached", "perjury", "obstruction of justice", "acquitted"],
            "n": 0,
            "rabbit": "Impeachment"
        },
        {
            "id": "election-1992",
            "tier": "middle",
            "t": "Won the 1992 election over President George H. W. Bush and independent Ross Perot",
            "k": ["1992", "ross perot", "perot", "george h. w. bush"],
            "n": 0,
            "rabbit": "Election of 1992"
        },
        {
            "id": "gore",
            "tier": "middle",
            "t": "His vice president was Al Gore (1993–2001)",
            "k": ["al gore", "gore", "vice president"],
            "n": 0
        },
        {
            "id": "reelection-1996",
            "tier": "middle",
            "t": "Reelected in 1996 over Bob Dole; the first Democrat since FDR to win two full terms",
            "k": ["bob dole", "dole", "1996", "two full terms"],
            "n": 0
        },
        {
            "id": "baby-boomer",
            "tier": "middle",
            "t": "The first president born after World War II (1946), part of the baby boom generation",
            "k": ["baby boom", "world war ii", "1946"],
            "n": 0
        },
        {
            "id": "little-rock",
            "tier": "middle",
            "t": "His presidential library opened in Little Rock, Arkansas, in 2004",
            "k": ["little rock", "presidential library"],
            "n": 0
        },
        {
            "id": "boys-nation",
            "tier": "power",
            "t": "As a 16-year-old Boys Nation delegate, shook hands with John F. Kennedy in the Rose Garden (1963)",
            "k": ["boys nation", "kennedy", "rose garden", "1963"],
            "n": 0
        },
        {
            "id": "rhodes",
            "tier": "power",
            "t": "Georgetown graduate and Rhodes Scholar at Oxford; met Hillary Rodham at Yale Law School; lost a race for Congress in 1974",
            "k": ["rhodes scholar", "oxford", "yale law school", "georgetown"],
            "n": 0
        },
        {
            "id": "youngest-governor",
            "tier": "power",
            "t": "Elected the nation’s youngest governor at 32 (1978); lost in 1980 to Frank White, then won the job back",
            "k": ["youngest governor", "frank white", "1978"],
            "n": 0
        },
        {
            "id": "saxophone",
            "tier": "power",
            "t": "Played the saxophone on _The Tonight Show_ (1988) and _The Arsenio Hall Show_ (1992); his 1988 convention speech ran long",
            "k": ["saxophone", "arsenio hall", "tonight show", "in closing"],
            "n": 0
        },
        {
            "id": "comeback-kid",
            "tier": "power",
            "t": "Called himself “the Comeback Kid” after the 1992 New Hampshire primary; campaign film _The Man from Hope_",
            "k": ["comeback kid", "new hampshire", "the man from hope", "tsongas"],
            "n": 0
        },
        {
            "id": "fmla",
            "tier": "power",
            "t": "Signed the Family and Medical Leave Act (his first major bill) and the Brady Bill, and created AmeriCorps (1993)",
            "k": ["family and medical leave act", "brady bill", "americorps"],
            "n": 0
        },
        {
            "id": "budget-1993",
            "tier": "power",
            "t": "Al Gore broke a Senate tie to pass his 1993 budget; a health care plan from a task force led by Hillary Rodham failed (1994)",
            "k": ["1993 budget", "health care", "task force"],
            "n": 0
        },
        {
            "id": "nafta",
            "tier": "power",
            "t": "Signed NAFTA (December 1993) with Canada and Mexico; Ross Perot had warned of a “giant sucking sound”",
            "k": ["nafta", "giant sucking sound", "canada", "mexico"],
            "n": 0,
            "rabbit": "NAFTA"
        },
        {
            "id": "gingrich",
            "tier": "power",
            "t": "Clashed with Speaker Newt Gingrich after the 1994 “Contract with America”; two shutdowns; “the era of big government is over” (1996)",
            "k": ["newt gingrich", "gingrich", "contract with america", "era of big government"],
            "n": 0,
            "rabbit": "Newt Gingrich"
        },
        {
            "id": "welfare",
            "tier": "power",
            "t": "Signed welfare reform (1996) with time limits and work requirements; used the line-item veto until it was struck down (1998)",
            "k": ["welfare reform", "welfare", "line-item veto", "work requirements"],
            "n": 0
        },
        {
            "id": "oslo-dayton",
            "tier": "power",
            "t": "Hosted the Oslo Accords handshake of Yitzhak Rabin and Yasser Arafat (1993); the Dayton Accords ended the Bosnian War (1995)",
            "k": ["oslo accords", "rabin", "arafat", "dayton accords"],
            "n": 0
        },
        {
            "id": "good-friday",
            "tier": "power",
            "t": "Envoy George Mitchell chaired talks for Northern Ireland’s Good Friday Agreement (1998); NATO bombed Serbia over Kosovo (1999)",
            "k": ["good friday agreement", "george mitchell", "kosovo"],
            "n": 0
        },
        {
            "id": "rehnquist",
            "tier": "power",
            "t": "Chief Justice William Rehnquist presided over his Senate trial (1999), the first since Andrew Johnson’s in 1868",
            "k": ["rehnquist", "senate trial", "andrew johnson"],
            "n": 0
        },
        {
            "id": "grammy-haiti",
            "tier": "power",
            "t": "Won a Grammy for the audiobook of _My Life_ (2004); UN special envoy to Haiti; raised tsunami aid with George H. W. Bush",
            "k": ["grammy", "my life", "haiti", "tsunami"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Which Clinton?",
        "body": "Several famous Clintons show up in quiz bowl. Bill Clinton was the 42nd president; his wife, Hillary Rodham Clinton, was a senator from New York (2001–2009), secretary of state (2009–2013), and the 2016 Democratic nominee for president. Two earlier New York governors share the name too: George Clinton, who also served as vice president, and DeWitt Clinton, who championed the Erie Canal. Saying only “Clinton” earns a prompt.",
        "fix": "Arkansas, the saxophone, NAFTA, welfare reform, Al Gore, and the 1998 impeachment mean Bill. Secretary of State and the 2016 election mean Hillary. The Erie Canal means DeWitt, and New York’s first governor is George. When the question says “this president,” answer “Bill Clinton.”",
        "line": "Real answer line: <b><u>Bill Clinton</u></b> (or <b><u>William</u></b> Jefferson <b><u>Clinton</u></b>; prompt on <u>Clinton</u>; do not accept “Hillary Clinton”)"
    },
    "tests": {
        "right": [
            "Bill Clinton",
            "William Jefferson Clinton",
            "President Clinton",
            "Bill Clintin",
            "William J. Clinton",
            "William Jefferson “Bill” Clinton"
        ],
        "prompt": [
            "Clinton"
        ],
        "wrong": [
            "Hillary Clinton",
            "DeWitt Clinton",
            "Al Gore",
            "George H. W. Bush",
            "Ross Perot",
            "George Clinton"
        ]
    }
}

out = ROOT / "topics" / f"{data['id']}.json"
with open(out, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", out)
