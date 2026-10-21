import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "gerald-ford",
    "name": "Gerald Ford",
    "mono": "GRF",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "38th U.S. President · The only one never elected president or vice president",
    "dates": "1913–2006",
    "briefing": "Gerald Ford was born Leslie Lynch King Jr. in Omaha, grew up in Grand Rapids, Michigan, and played center for the University of Michigan football team. After nearly 25 years in Congress, he was chosen as vice president in 1973 and became the 38th president when Richard Nixon resigned in 1974, making him the only president never elected to either office. A month later, he pardoned Nixon, a decision that stirred fierce debate, and in 1976 he lost the election to Jimmy Carter.",
    "answerHtml": "<b><u>Gerald Ford</u></b> (or Gerald R. Ford Jr.; prompt on <u>Ford</u> alone; do not accept “Henry Ford”)",
    "accept": [
        "gerald ford",
        "gerald r ford",
        "gerald rudolph ford",
        "gerald rudolph ford jr",
        "gerald ford jr",
        "gerald r ford jr",
        "jerry ford",
        "president ford",
        "pres ford",
        "president gerald ford"
    ],
    "prompt": [
        "ford",
        "gerald",
        "jerry",
        "mr ford"
    ],
    "reject": [
        "henry ford",
        "henry ford ii",
        "harrison ford",
        "betty ford",
        "betty ford center",
        "edsel ford",
        "ford motor company",
        "ford motor",
        "john ford",
        "whitey ford",
        "ford madox ford",
        "fords theatre",
        "fords theater",
        "richard nixon",
        "nixon",
        "jimmy carter",
        "carter",
        "nelson rockefeller",
        "rockefeller",
        "spiro agnew",
        "agnew",
        "bob dole",
        "ronald reagan",
        "reagan",
        "henry kissinger",
        "kissinger",
        "dick cheney",
        "donald rumsfeld",
        "george h w bush",
        "lyndon johnson",
        "carl albert",
        "walter mondale"
    ],
    "mediaPending": True,
    "media": [],
    "wiki": "https://en.wikipedia.org/wiki/Gerald_Ford",
    "qb": {
        "q": "Gerald Ford",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "Press secretary Jerald terHorst resigned in protest over a decision this president made a month after taking office. In October 1974, this president went before a House subcommittee to explain that decision, insisting there had been “no deal.”",
            "r": "That decision was his “full, free, and absolute” pardon of Richard Nixon. For 10 points, name this 38th president."
        },
        {
            "p": "During World War II, this future president served on the light aircraft carrier USS _Monterey_ in the Pacific, and in December 1944 he nearly went overboard during a deadly typhoon that swept across the fleet.",
            "r": "When he took office in 1974, he declared, “Our long national nightmare is over.” For 10 points, name this 38th president."
        },
        {
            "p": "After starring at center for the University of Michigan football team, this man turned down contract offers from both the Detroit Lions and the Green Bay Packers. Instead, he took a job coaching football and boxing at Yale, where he later earned a law degree.",
            "r": "For 10 points, name this man who became the 38th president in 1974 after Richard Nixon resigned."
        },
        {
            "p": "As a congressman, this man served on the Warren Commission, which investigated the assassination of John F. Kennedy. In 1965, his fellow Republicans chose him as their leader in the House of Representatives.",
            "r": "In 1973, he replaced Spiro Agnew as vice president under the 25th Amendment. For 10 points, name this man who became president a year later."
        },
        {
            "p": "In May 1975, this president sent Marines to rescue the crew of the American cargo ship _Mayaguez_ [“mah-yah-GWEZ”], which had been seized by Cambodia’s Khmer Rouge [“kuh-MEER ROOZH”]. Weeks earlier, the last Americans had been flown out of Saigon by helicopter as the city fell.",
            "r": "His wife, Betty, won praise for speaking openly about her breast cancer. For 10 points, name this president who took office in 1974."
        },
        {
            "p": "In November 1974, this president met Leonid Brezhnev at Vladivostok [“vlad-ih-vah-STOCK”] to set limits on nuclear weapons. The next summer, he, Brezhnev, and the leaders of 33 other countries signed the Helsinki Accords, which accepted Europe’s postwar borders and included promises to respect human rights.",
            "r": "He was president during the nation’s 200th birthday in 1976. For 10 points, name this Republican, who lost that year’s election to Jimmy Carter."
        },
        {
            "p": "Alan Greenspan, later the longtime head of the Federal Reserve, led this president’s Council of Economic Advisers while this president battled rising prices. In 1974, this president asked Americans to wear buttons reading “WIN,” short for “Whip Inflation Now.”",
            "r": "Critics mocked that campaign as the economy slid into recession. For 10 points, name this president, who succeeded Richard Nixon."
        },
        {
            "p": "During New York City’s 1975 money crisis, the _Daily News_ ran a famous front-page headline claiming that this president had told the city to “Drop Dead.” He later agreed to federal loans that helped the city avoid bankruptcy.",
            "r": "For 10 points, name this president, who pardoned Richard Nixon and was never elected president or vice president."
        },
        {
            "p": "In September 1975, this president survived two attempts on his life in California within three weeks, first in Sacramento and then in San Francisco. Both would-be assassins were women, and neither of them hurt him.",
            "r": "A year earlier, he had taken over from Richard Nixon. For 10 points, name this 38th president."
        },
        {
            "p": "During a 1976 debate, this president said that “there is no Soviet domination of Eastern Europe,” a remark that drew wide criticism. Earlier that year, he had narrowly beaten Ronald Reagan for the Republican nomination.",
            "r": "That fall, he lost the election to Jimmy Carter. For 10 points, name this president who had succeeded Richard Nixon."
        },
        {
            "p": "In a 1975 shake-up nicknamed the “Halloween Massacre,” this president made Donald Rumsfeld secretary of defense and George H. W. Bush director of the CIA. Dick Cheney replaced Rumsfeld as his White House chief of staff.",
            "r": "Neither he nor his vice president, Nelson Rockefeller, had been elected to their offices. For 10 points, name this 38th president."
        },
        {
            "p": "This president’s only appointment to the Supreme Court was John Paul Stevens, who served on the Court for more than 34 years. In 1974, this president offered clemency to Vietnam War draft evaders and deserters who agreed to do public service.",
            "r": "For 10 points, name this president, who took office after the Watergate scandal forced Richard Nixon to resign."
        },
        {
            "p": "In 2001, the John F. Kennedy Library Foundation gave this former president its Profile in Courage Award for a decision he made in September 1974, which had angered many Americans at the time. Senator Ted Kennedy, who had criticized that decision, later praised it.",
            "r": "That decision was his pardon of Richard Nixon. For 10 points, name this 38th president."
        },
        {
            "p": "After this president stumbled down the steps of Air Force One in Salzburg, Austria, in 1975, comedian Chevy Chase began playing him as a clumsy bumbler on _Saturday Night Live_. In fact, this president had been a star college athlete.",
            "r": "For 10 points, name this president, a former University of Michigan football player, who served from 1974 to 1977."
        },
        {
            "p": "This man was born Leslie Lynch King Jr. in Omaha, Nebraska, but took the name of his stepfather after his mother remarried in Grand Rapids, Michigan. He later became the only Eagle Scout ever to serve as president.",
            "r": "For 10 points, name this man who became president in 1974 without ever winning a national election."
        }
    ],
    "clues": [
        {
            "id": "38th",
            "tier": "giveaway",
            "t": "38th President (1974–1977), a Republican from Michigan",
            "k": ["38th", "michigan", "republican"],
            "n": 0
        },
        {
            "id": "nixon-resigned",
            "tier": "giveaway",
            "t": "Became president when Richard Nixon resigned during the Watergate scandal (August 1974)",
            "k": ["richard nixon", "watergate", "resigned"],
            "n": 0,
            "rabbit": "Richard Nixon"
        },
        {
            "id": "pardon",
            "tier": "giveaway",
            "t": "Pardoned Nixon in September 1974",
            "k": ["pardoned", "september 1974"],
            "n": 0,
            "rabbit": "Watergate scandal"
        },
        {
            "id": "never-elected",
            "tier": "giveaway",
            "t": "The only president never elected president or vice president",
            "k": ["never elected", "only president"],
            "n": 0
        },
        {
            "id": "nightmare",
            "tier": "giveaway",
            "t": "On taking office, declared, “Our long national nightmare is over”",
            "k": ["national nightmare", "nightmare"],
            "n": 0
        },
        {
            "id": "carter-reagan",
            "tier": "middle",
            "t": "Narrowly beat Ronald Reagan for the 1976 Republican nomination, then lost the election to Jimmy Carter",
            "k": ["jimmy carter", "ronald reagan", "1976"],
            "n": 0,
            "rabbit": "Jimmy Carter"
        },
        {
            "id": "agnew-25th",
            "tier": "middle",
            "t": "Chosen vice president in 1973 under the 25th Amendment after Spiro Agnew resigned; his own vice president, Nelson Rockefeller, was chosen the same way",
            "k": ["25th amendment", "spiro agnew", "nelson rockefeller", "1973"],
            "n": 0,
            "rabbit": "Vice President of the United States"
        },
        {
            "id": "win",
            "tier": "middle",
            "t": "WIN (“Whip Inflation Now”) buttons: a 1974 campaign against rising prices",
            "k": ["whip inflation now", "inflation", "buttons"],
            "n": 0
        },
        {
            "id": "assassination-attempts",
            "tier": "middle",
            "t": "Survived two assassination attempts in California in September 1975, in Sacramento and San Francisco",
            "k": ["assassination attempts", "sacramento", "san francisco", "1975"],
            "n": 0
        },
        {
            "id": "helsinki",
            "tier": "middle",
            "t": "Signed the Helsinki Accords (1975), which accepted Europe’s postwar borders and promised respect for human rights",
            "k": ["helsinki accords", "helsinki", "human rights"],
            "n": 0
        },
        {
            "id": "michigan-football",
            "tier": "middle",
            "t": "Played center for the University of Michigan and turned down offers from the Detroit Lions and Green Bay Packers",
            "k": ["university of michigan", "detroit lions", "green bay packers", "center"],
            "n": 0
        },
        {
            "id": "house-leader",
            "tier": "middle",
            "t": "Represented Grand Rapids in the U.S. House (1949–1973) and became House Minority Leader in 1965",
            "k": ["grand rapids", "minority leader", "1965"],
            "n": 0
        },
        {
            "id": "betty",
            "tier": "middle",
            "t": "His wife, Betty, won praise for speaking openly about her breast cancer",
            "k": ["betty", "breast cancer"],
            "n": 0
        },
        {
            "id": "saigon",
            "tier": "middle",
            "t": "President when Saigon fell and the Vietnam War ended (April 1975)",
            "k": ["saigon", "vietnam", "april 1975"],
            "n": 0
        },
        {
            "id": "king",
            "tier": "power",
            "t": "Born Leslie Lynch King Jr. in Omaha (1913); took his stepfather’s name; the only Eagle Scout to become president",
            "k": ["leslie lynch king", "omaha", "eagle scout", "stepfather"],
            "n": 0
        },
        {
            "id": "terhorst",
            "tier": "power",
            "t": "Press secretary Jerald terHorst quit over the pardon, and the president told a House subcommittee there had been “no deal”",
            "k": ["terhorst", "press secretary", "no deal"],
            "n": 0
        },
        {
            "id": "monterey",
            "tier": "power",
            "t": "Served on the light aircraft carrier USS _Monterey_ in World War II and nearly went overboard in a December 1944 typhoon",
            "k": ["monterey", "typhoon", "aircraft carrier"],
            "n": 0
        },
        {
            "id": "yale",
            "tier": "power",
            "t": "Coached football and boxing at Yale, where he later earned a law degree (1941)",
            "k": ["yale", "boxing", "law degree"],
            "n": 0
        },
        {
            "id": "warren",
            "tier": "power",
            "t": "Served on the Warren Commission, which investigated John F. Kennedy’s assassination",
            "k": ["warren commission", "kennedy"],
            "n": 0
        },
        {
            "id": "mayaguez",
            "tier": "power",
            "t": "Mayaguez incident (May 1975): sent Marines to rescue the crew of a U.S. cargo ship seized by Cambodia’s Khmer Rouge",
            "k": ["mayaguez", "khmer rouge", "cambodia"],
            "n": 0
        },
        {
            "id": "vladivostok",
            "tier": "power",
            "t": "Met Leonid Brezhnev at Vladivostok (November 1974) to set limits on nuclear weapons",
            "k": ["vladivostok", "brezhnev"],
            "n": 0
        },
        {
            "id": "greenspan",
            "tier": "power",
            "t": "Alan Greenspan, later head of the Federal Reserve, chaired his Council of Economic Advisers",
            "k": ["alan greenspan", "greenspan", "council of economic advisers"],
            "n": 0
        },
        {
            "id": "drop-dead",
            "tier": "power",
            "t": "A 1975 _Daily News_ headline claimed he told New York City to “Drop Dead”; he later approved federal loans for the city",
            "k": ["drop dead", "new york city", "daily news"],
            "n": 0
        },
        {
            "id": "eastern-europe",
            "tier": "power",
            "t": "In a 1976 debate, said “there is no Soviet domination of Eastern Europe”",
            "k": ["soviet domination", "eastern europe", "debate"],
            "n": 0
        },
        {
            "id": "halloween",
            "tier": "power",
            "t": "The 1975 “Halloween Massacre” shake-up made Donald Rumsfeld defense secretary and George H. W. Bush CIA director; Dick Cheney became chief of staff",
            "k": ["halloween massacre", "rumsfeld", "cheney"],
            "n": 0
        },
        {
            "id": "stevens-clemency",
            "tier": "power",
            "t": "His only Supreme Court pick was John Paul Stevens (1975); he offered clemency to Vietnam draft evaders who did public service (1974)",
            "k": ["john paul stevens", "stevens", "clemency"],
            "n": 0
        },
        {
            "id": "profile",
            "tier": "power",
            "t": "Won the 2001 Profile in Courage Award for the Nixon pardon; Ted Kennedy, once a critic, praised it",
            "k": ["profile in courage", "ted kennedy", "2001"],
            "n": 0
        },
        {
            "id": "chevy-chase",
            "tier": "power",
            "t": "Chevy Chase mocked him as clumsy on _Saturday Night Live_ after he stumbled on the steps of Air Force One (1975)",
            "k": ["chevy chase", "saturday night live", "air force one"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Which Ford?",
        "body": "Several famous Fords show up in quiz bowl: Gerald Ford, the 38th president; Henry Ford, the carmaker behind the Model T and the moving assembly line; and Betty Ford, Gerald’s wife. Ford’s Theatre, where Abraham Lincoln was shot, has nothing to do with any of them. In this app, “Ford” alone earns a prompt, and “Henry Ford” is wrong.",
        "fix": "Watergate, the Nixon pardon, the 25th Amendment, WIN buttons, the Helsinki Accords, and the 1976 loss to Jimmy Carter mean Gerald Ford; cars, the Model T, and the assembly line mean Henry Ford. Say “Gerald Ford” to be safe.",
        "line": "Real answer line: <b><u>Gerald Ford</u></b> (or Gerald R. Ford Jr.; prompt on <u>Ford</u> alone; do not accept “Henry Ford”)"
    },
    "tests": {
        "right": [
            "Gerald Ford",
            "Gerald R. Ford",
            "President Ford",
            "Jerry Ford",
            "Gerold Ford",
            "Gerald Rudolph Ford Jr."
        ],
        "prompt": [
            "Ford",
            "Gerald"
        ],
        "wrong": [
            "Henry Ford",
            "Harrison Ford",
            "Betty Ford",
            "Richard Nixon",
            "Jimmy Carter",
            "Nelson Rockefeller",
            "Spiro Agnew",
            "Ford's Theatre"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("wrote", data["id"])
