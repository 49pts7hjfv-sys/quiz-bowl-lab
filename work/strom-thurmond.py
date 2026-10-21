import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "strom-thurmond",
    "name": "Strom Thurmond",
    "mono": "ST",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "South Carolina senator (1954–2003) · 1948 Dixiecrat presidential nominee",
    "dates": "1902–2003",
    "briefing": "Strom Thurmond served in the U.S. Senate for more than 47 years and did not retire until he was 100 years old. In 1948, as governor of South Carolina, he ran for president for the States’ Rights “Dixiecrats,” who supported racial segregation, and in 1957 he spoke for more than 24 hours straight against a civil rights bill. In 1964 he switched from the Democratic Party to the Republican Party, and he left the Senate in 2003.",
    "answerHtml": "Strom <b><u>Thurmond</u></b> (accept James Strom <u>Thurmond</u>; prompt on <u>Strom</u>)",
    "accept": [
        "strom thurmond",
        "thurmond",
        "james strom thurmond",
        "j strom thurmond",
        "senator thurmond",
        "senator strom thurmond",
        "governor thurmond"
    ],
    "prompt": [
        "strom"
    ],
    "reject": [
        "jesse helms",
        "helms",
        "george wallace",
        "wallace",
        "fielding wright",
        "fielding l wright",
        "harry truman",
        "harry s truman",
        "truman",
        "lindsey graham",
        "trent lott",
        "robert byrd",
        "richard russell",
        "harry byrd",
        "james eastland",
        "john c calhoun",
        "calhoun",
        "ben tillman",
        "fritz hollings",
        "ernest hollings",
        "orval faubus",
        "barry goldwater",
        "hubert humphrey",
        "ralph yarborough",
        "dixiecrats",
        "dixiecrat",
        "dixiecrat party",
        "states rights democratic party",
        "states rights party",
        "southern manifesto",
        "filibuster"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Strom_Thurmond",
    "qb": {
        "q": "Thurmond",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "In 1954, this politician became the first person elected to the U.S. Senate as a write-in candidate. He had promised to resign in 1956 so that voters could choose him in a primary, and he kept that promise before winning the seat again.",
            "r": "For 10 points, name this South Carolina senator who had run for president as a “Dixiecrat” in 1948."
        },
        {
            "p": "At age 41, this future senator landed in a glider with the 82nd Airborne Division during the D-Day invasion of Normandy. He had volunteered for the Army while serving as a South Carolina circuit judge.",
            "r": "In 1957, he spoke for more than 24 hours against a civil rights bill. For 10 points, name this longtime senator."
        },
        {
            "p": "In 1948, this candidate and his running mate, Mississippi governor Fielding Wright, carried South Carolina, Alabama, Mississippi, and Louisiana and won 39 electoral votes. Their party was formed by Southern Democrats who opposed the civil rights plank adopted at the Democratic convention.",
            "r": "That party was nicknamed the “Dixiecrats.” For 10 points, name this South Carolina governor who later served in the Senate until age 100."
        },
        {
            "p": "This senator wrote the first draft of the 1956 “Declaration of Constitutional Principles,” better known as the Southern Manifesto, which attacked the Supreme Court’s ruling in _Brown v. Board of Education_. About one hundred Southern members of Congress signed it.",
            "r": "The next year, he spoke for over 24 hours against the Civil Rights Act of 1957. For 10 points, name this senator from South Carolina."
        },
        {
            "p": "In September 1964, this senator left the Democratic Party to support Barry Goldwater’s presidential campaign. Four years later, he helped Richard Nixon keep Southern delegates from switching to Ronald Reagan at the Republican convention.",
            "r": "He had run for president himself in 1948 as the nominee of the States’ Rights Democratic Party. For 10 points, name this longtime South Carolina senator."
        },
        {
            "p": "In December 2002, Senate Republican leader Trent Lott praised this man’s 1948 presidential campaign at his 100th birthday party, and the uproar that followed led Lott to give up his leadership post. Weeks later, this man retired from the Senate.",
            "r": "For 10 points, name this South Carolina senator who once spoke for more than 24 hours against a civil rights bill."
        },
        {
            "p": "As chairman of the Senate Judiciary Committee from 1981 to 1987, this senator led the confirmation hearings for Sandra Day O’Connor, the first woman on the Supreme Court. In the late 1990s, he chaired the Senate Armed Services Committee.",
            "r": "He had been the States’ Rights candidate for president in 1948. For 10 points, name this senator who served until he was 100."
        },
        {
            "p": "In 2001, the Senate created the honorary title of “president pro tempore emeritus” for this senator, who had held the office of president pro tempore for much of the 1980s and 1990s. That office made him third in line for the presidency.",
            "r": "He became the first sitting senator to reach age 100. For 10 points, name this South Carolinian who ran for president as a Dixiecrat in 1948."
        },
        {
            "p": "This politician grew up in Edgefield, South Carolina, earned a degree in horticulture from Clemson, and worked as a teacher, an athletic coach, and a county superintendent of education. He served in the South Carolina Senate in the 1930s.",
            "r": "In 1948, he ran for president as the nominee of the States’ Rights Democratic Party. For 10 points, name this man who later served in the U.S. Senate until 2003."
        },
        {
            "p": "When this senator retired in January 2003, his more than 47 years of service were the longest in Senate history, a record that Robert Byrd of West Virginia broke in 2006. His time in office was interrupted only by a short break in 1956.",
            "r": "He was the oldest senator in history. For 10 points, name this South Carolinian who held the floor for more than 24 hours in 1957."
        },
        {
            "p": "In 1983, this senator voted for the bill that made Martin Luther King Jr.’s birthday a federal holiday, decades after he had become one of the best-known defenders of segregation. He chaired the Senate Judiciary Committee at the time.",
            "r": "He had run for president as a “Dixiecrat” in 1948. For 10 points, name this South Carolina senator."
        },
        {
            "p": "Lindsey Graham won this man’s Senate seat in 2002, after this man decided not to seek another term. This man died in his hometown of Edgefield in June 2003, about six months after leaving office.",
            "r": "He had served in the Senate until age 100. For 10 points, name this South Carolinian who ran for president as a Dixiecrat in 1948."
        },
        {
            "p": "In July 1948, delegates meeting in Birmingham, Alabama, nominated this governor for president, days after some Southerners walked out of the Democratic National Convention in Philadelphia. His platform called for keeping the races segregated.",
            "r": "His party was officially the States’ Rights Democratic Party. For 10 points, name this South Carolina governor, the “Dixiecrat” candidate."
        },
        {
            "p": "In August 1957, this senator tried to block the first civil rights bill to pass Congress after Reconstruction, which created the federal Commission on Civil Rights. Majority Leader Lyndon Johnson got the bill passed anyway after this senator finally gave up the floor.",
            "r": "He had spoken for 24 hours and 18 minutes, a Senate record that stood until 2025. For 10 points, name this South Carolina senator."
        },
        {
            "p": "In 1964, this senator got into a wrestling match with Texas senator Ralph Yarborough outside a committee room while trying to delay a vote on LeRoy Collins, the first director of the Community Relations Service. Two months later, this senator joined the Republican Party.",
            "r": "For 10 points, name this South Carolinian who had run for president as a Dixiecrat in 1948."
        }
    ],
    "clues": [
        {
            "id": "dixiecrat",
            "tier": "giveaway",
            "t": "1948 presidential nominee of the States’ Rights Democratic Party, the “Dixiecrats,” who supported segregation",
            "k": ["dixiecrats", "states’ rights", "1948", "segregation"],
            "n": 0
        },
        {
            "id": "south-carolina",
            "tier": "giveaway",
            "t": "U.S. senator from South Carolina (1954–2003) and, before that, its governor (1947–1951)",
            "k": ["south carolina", "governor", "senator"],
            "n": 0
        },
        {
            "id": "record-speech",
            "tier": "giveaway",
            "t": "Spoke for 24 hours and 18 minutes against the Civil Rights Act of 1957, a Senate record until 2025",
            "k": ["24 hours", "civil rights act of 1957", "1957"],
            "n": 0,
            "rabbit": "Filibuster"
        },
        {
            "id": "age-100",
            "tier": "giveaway",
            "t": "Served in the Senate until January 2003, when he was 100 years old",
            "k": ["100 years old", "2003"],
            "n": 0
        },
        {
            "id": "party-switch",
            "tier": "giveaway",
            "t": "Switched from the Democratic Party to the Republican Party in 1964",
            "k": ["republican party", "switched", "1964"],
            "n": 0
        },
        {
            "id": "fielding-wright",
            "tier": "middle",
            "t": "1948 running mate: Fielding Wright of Mississippi; they won four Southern states and 39 electoral votes",
            "k": ["fielding wright", "39 electoral votes"],
            "n": 0
        },
        {
            "id": "walkout",
            "tier": "middle",
            "t": "The Dixiecrats formed after Southern delegates walked out of the 1948 Democratic convention over a civil rights plank",
            "k": ["walked out", "civil rights plank"],
            "n": 0,
            "rabbit": "Democratic Party"
        },
        {
            "id": "truman",
            "tier": "middle",
            "t": "Ran against Democrat Harry Truman, who won the 1948 election anyway",
            "k": ["harry truman", "truman"],
            "n": 0,
            "rabbit": "Harry S. Truman"
        },
        {
            "id": "write-in",
            "tier": "middle",
            "t": "In 1954, became the first person elected to the Senate as a write-in candidate",
            "k": ["write-in", "1954"],
            "n": 0
        },
        {
            "id": "southern-manifesto",
            "tier": "middle",
            "t": "Wrote the first draft of the Southern Manifesto (1956), which attacked _Brown v. Board of Education_",
            "k": ["southern manifesto", "manifesto", "brown v. board of education"],
            "n": 0,
            "rabbit": "Brown v. Board of Education"
        },
        {
            "id": "goldwater",
            "tier": "middle",
            "t": "Left the Democrats in September 1964 to support Republican Barry Goldwater for president",
            "k": ["barry goldwater", "goldwater"],
            "n": 0
        },
        {
            "id": "pro-tem",
            "tier": "middle",
            "t": "President pro tempore of the Senate for much of the 1980s and 1990s; named “president pro tempore emeritus” in 2001",
            "k": ["president pro tempore", "emeritus"],
            "n": 0,
            "rabbit": "President pro tempore of the Senate"
        },
        {
            "id": "longest-serving",
            "tier": "middle",
            "t": "Retired as the longest-serving senator up to that time (over 47 years) and the oldest ever; Robert Byrd broke his service record in 2006",
            "k": ["robert byrd", "longest-serving", "oldest"],
            "n": 0
        },
        {
            "id": "d-day",
            "tier": "power",
            "t": "At age 41, landed in a glider with the 82nd Airborne Division on D-Day (1944)",
            "k": ["d-day", "glider", "82nd airborne"],
            "n": 0
        },
        {
            "id": "clemson",
            "tier": "power",
            "t": "From Edgefield, South Carolina; horticulture degree from Clemson; teacher, coach, and county school superintendent",
            "k": ["clemson", "horticulture", "edgefield"],
            "n": 0
        },
        {
            "id": "judge",
            "tier": "power",
            "t": "Served in the South Carolina Senate (1933–1938), then became a circuit judge; volunteered for the Army in World War II",
            "k": ["circuit judge", "army"],
            "n": 0
        },
        {
            "id": "birmingham",
            "tier": "power",
            "t": "Nominated at a States’ Rights convention in Birmingham, Alabama (July 1948), days after the walkout in Philadelphia",
            "k": ["birmingham", "philadelphia"],
            "n": 0
        },
        {
            "id": "resign-1956",
            "tier": "power",
            "t": "Kept a promise to resign in 1956 and face voters in a primary, then won the seat back",
            "k": ["resign", "primary"],
            "n": 0
        },
        {
            "id": "civil-rights-commission",
            "tier": "power",
            "t": "The 1957 act he fought created the Commission on Civil Rights; Majority Leader Lyndon Johnson pushed it through",
            "k": ["commission on civil rights", "lyndon johnson"],
            "n": 0,
            "rabbit": "Lyndon B. Johnson"
        },
        {
            "id": "nixon-1968",
            "tier": "power",
            "t": "At the 1968 Republican convention, helped Richard Nixon keep Southern delegates from switching to Ronald Reagan",
            "k": ["richard nixon", "nixon", "1968"],
            "n": 0,
            "rabbit": "Richard Nixon"
        },
        {
            "id": "judiciary",
            "tier": "power",
            "t": "Chaired the Judiciary Committee (1981–1987), including Sandra Day O’Connor’s hearings, and later the Armed Services Committee",
            "k": ["judiciary committee", "sandra day o’connor", "armed services"],
            "n": 0
        },
        {
            "id": "mlk-holiday",
            "tier": "power",
            "t": "Voted for the 1983 law making Martin Luther King Jr.’s birthday a federal holiday",
            "k": ["martin luther king", "holiday", "1983"],
            "n": 0
        },
        {
            "id": "trent-lott",
            "tier": "power",
            "t": "Trent Lott’s praise of his 1948 campaign at his 100th birthday party (2002) cost Lott his job as Republican leader",
            "k": ["trent lott", "lott", "birthday party"],
            "n": 0
        },
        {
            "id": "lindsey-graham",
            "tier": "power",
            "t": "Lindsey Graham won his seat in 2002; he died in Edgefield in June 2003",
            "k": ["lindsey graham", "graham", "edgefield"],
            "n": 0
        },
        {
            "id": "yarborough",
            "tier": "power",
            "t": "In 1964, got into a wrestling match with Texas senator Ralph Yarborough while trying to delay a vote on a civil rights official",
            "k": ["ralph yarborough", "yarborough", "wrestling"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Thurmond, Wallace, or Helms?",
        "body": "Several Southern politicians who opposed civil rights laws show up in the same kinds of clues. Strom Thurmond of South Carolina was the Dixiecrat candidate in 1948; George Wallace of Alabama stood in a doorway at the University of Alabama in 1963 and ran a third-party campaign in 1968; and Jesse Helms of North Carolina was a senator from 1973 to 2003 who led opposition to the Martin Luther King Jr. holiday. Answering “Dixiecrats” names the party, not the man.",
        "fix": "1948, the States’ Rights ticket, the 24-hour speech of 1957, switching parties in 1964, and serving until age 100 mean Thurmond. Alabama and the schoolhouse door mean Wallace, and North Carolina means Helms.",
        "line": "Real answer line: Strom <b><u>Thurmond</u></b> (accept James Strom <u>Thurmond</u>)"
    },
    "tests": {
        "right": [
            "Strom Thurmond",
            "Thurmond",
            "James Strom Thurmond",
            "Senator Thurmond",
            "Strom Thurmund",
            "Thurmon"
        ],
        "prompt": [
            "Strom"
        ],
        "wrong": [
            "Jesse Helms",
            "George Wallace",
            "Dixiecrats",
            "Harry Truman",
            "Fielding Wright",
            "Lindsey Graham",
            "John C. Calhoun",
            "Robert Byrd"
        ]
    }
}

out = ROOT / "topics" / f"{data['id']}.json"
with open(out, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("wrote", out)
