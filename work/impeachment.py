import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TIP = "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."

data = {
    "id": "impeachment",
    "name": "Impeachment",
    "mono": "IMP",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "How Congress charges and tries officials · Can remove a president",
    "dates": "First federal case 1797",
    "briefing": "The Constitution gives Congress a way to remove a president, a judge, or another federal official for “Treason, Bribery, or other high Crimes and Misdemeanors.” First the House of Representatives votes, by a simple majority, to impeach, which is like bringing formal charges. Then the Senate holds a trial, and it takes a two-thirds vote to convict and remove the official. Three presidents have been impeached, and the Senate acquitted all three.",
    "answerHtml": "<b><u>impeachment</u></b> (accept word forms like <u>impeach</u> or <u>impeached</u>; prompt on <u>removal</u> from office)",
    "accept": [
        "impeachment",
        "impeachments",
        "impeach",
        "impeached",
        "impeaching",
        "impeachment process",
        "impeachment trial",
        "presidential impeachment"
    ],
    "prompt": [
        "removal",
        "removal from office",
        "senate trial",
        "trial",
        "conviction"
    ],
    "reject": [
        "censure",
        "recall",
        "recall election",
        "expulsion",
        "expel",
        "resignation",
        "veto",
        "veto override",
        "pardon",
        "25th amendment",
        "twenty fifth amendment",
        "watergate",
        "watergate scandal",
        "vote of no confidence",
        "no confidence",
        "filibuster",
        "cloture",
        "contempt of congress",
        "indictment",
        "habeas corpus"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Impeachment_in_the_United_States",
    "qb": {
        "q": "impeachment",
        "found": 0,
        "tip": TIP
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "At the Constitutional Convention, George Mason proposed “maladministration” as a reason for this process, but James Madison objected that so vague a term would let the Senate remove a president whenever it pleased. Mason then substituted a different phrase.",
            "r": "The Constitution allows this process for “Treason, Bribery, or other high Crimes and Misdemeanors.” For 10 points, name this process in which the House brings charges against a federal official."
        },
        {
            "p": "The first federal official to face this process was Senator William Blount of Tennessee, who was accused in 1797 of plotting to help Britain seize Spanish Florida and Louisiana. The Senate expelled Blount and later dismissed the case, ruling that it lacked jurisdiction.",
            "r": "For 10 points, name this process in which the House of Representatives brings formal charges against an official."
        },
        {
            "p": "In 1804, John Pickering, a federal judge from New Hampshire, became the first official removed from office through this process. Every official removed this way has been a federal judge, including Alcee Hastings, who was later elected to the House of Representatives.",
            "r": "For 10 points, name this process in which the House brings charges and the Senate holds a trial."
        },
        {
            "p": "Vice President Aaron Burr presided over the Senate trial of Samuel Chase in 1805, only months after killing Alexander Hamilton in a duel. Chase is the only Supreme Court justice ever to go through this process, and the Senate acquitted him.",
            "r": "For 10 points, name this process, in which the House of Representatives can charge federal officials with “high crimes and misdemeanors.”"
        },
        {
            "p": "Secretary of War William Belknap rushed to resign in 1876 after he was caught taking money from a trading-post operator, but the House went ahead with this process against him anyway. The Senate acquitted Belknap, partly because some senators believed it could not try a former official.",
            "r": "For 10 points, name this process that begins with a vote in the House of Representatives."
        },
        {
            "p": "In 1868, the House used this process against a president who had tried to fire Secretary of War Edwin Stanton in violation of the Tenure of Office Act. Chief Justice Salmon Chase presided over the Senate trial, where Edmund Ross cast a key vote to acquit.",
            "r": "That president, Andrew Johnson, kept his job by a single vote. For 10 points, name this process in which the House brings charges and the Senate holds a trial."
        },
        {
            "p": "In July 1974, the House Judiciary Committee, chaired by Peter Rodino, approved three articles accusing a president of obstruction of justice, abuse of power, and contempt of Congress. That president resigned on August 9, before the full House could vote on those articles.",
            "r": "That president was Richard Nixon. For 10 points, name this process, which the House of Representatives can start against a federal official."
        },
        {
            "p": "Chief Justice William Rehnquist presided over a 1999 Senate trial that followed the House’s approval of charges of perjury and obstruction of justice in December 1998. Henry Hyde led the House managers who argued the case.",
            "r": "The Senate acquitted President Bill Clinton. For 10 points, name this process in which the House brings formal charges against an official."
        },
        {
            "p": "Chief Justice John Roberts presided over a Senate trial in early 2020, but Senator Patrick Leahy presided over a second trial of the same man in 2021, because he was no longer president by then. The House had approved those charges in December 2019 and January 2021.",
            "r": "The Senate acquitted Donald Trump both times. For 10 points, name this process, which the House has used against three presidents."
        },
        {
            "p": "In Britain, Edmund Burke led this kind of case against Warren Hastings, the former governor-general of Bengal, in a trial that dragged on for seven years before Hastings was acquitted in 1795. George Mason mentioned Hastings’s case while the U.S. Constitution was being written.",
            "r": "For 10 points, name this process that the U.S. House of Representatives uses to bring charges against officials."
        },
        {
            "p": "In _Nixon v. United States_, the Supreme Court ruled in 1993 that the Senate may decide for itself how to run trials in this process, after a judge named Walter Nixon complained that a Senate committee, not the full Senate, had heard the evidence against him.",
            "r": "That judge’s removal stood. For 10 points, name this process in which the House brings charges and a two-thirds vote of the Senate can remove an official."
        },
        {
            "p": "In Federalist No. 65, Alexander Hamilton explained why the Senate, rather than the Supreme Court, should hold trials in this process. The Constitution says that the president’s pardon power does not apply to cases of this kind, and that such cases are not tried by a jury.",
            "r": "For 10 points, name this process that begins when the House of Representatives approves charges called articles."
        },
        {
            "p": "In 1843, Whig congressman John Botts introduced the first resolution aimed at starting this process against a president, John Tyler, but the House voted it down. In 1970, Gerald Ford led an effort to use this process against Justice William O. Douglas.",
            "r": "For 10 points, name this process in which the House brings charges that the Senate then tries."
        },
        {
            "p": "The Constitution limits the punishment in this process to removal from office and a ban on holding federal office again, though the official can still face a criminal trial in court. In 2010, the Senate removed Judge Thomas Porteous and also barred him from future office.",
            "r": "A two-thirds vote of the Senate is needed to convict. For 10 points, name this process that starts in the House of Representatives."
        },
        {
            "p": "Members of the House known as “managers” act as prosecutors when the Senate holds a trial in this process, and senators take a special oath before hearing the evidence. The House Judiciary Committee usually drafts the charges, which are called articles.",
            "r": "A simple majority of the House can approve those articles. For 10 points, name this process, which can lead to an official’s removal from office."
        }
    ],
    "clues": [
        {
            "id": "house-charges",
            "tier": "giveaway",
            "t": "The House of Representatives approves the charges by a simple majority vote",
            "k": ["house of representatives", "simple majority", "charges"],
            "n": 0
        },
        {
            "id": "senate-trial",
            "tier": "giveaway",
            "t": "The Senate holds the trial, and a two-thirds vote is needed to convict and remove the official",
            "k": ["senate", "two-thirds", "convict"],
            "n": 0
        },
        {
            "id": "high-crimes",
            "tier": "giveaway",
            "t": "Grounds in the Constitution: “Treason, Bribery, or other high Crimes and Misdemeanors”",
            "k": ["high crimes", "misdemeanors", "treason", "bribery"],
            "n": 0
        },
        {
            "id": "chief-justice",
            "tier": "giveaway",
            "t": "The Chief Justice presides when a sitting president is on trial in the Senate",
            "k": ["chief justice", "presides"],
            "n": 0
        },
        {
            "id": "three-presidents",
            "tier": "giveaway",
            "t": "Three presidents have been charged this way: Andrew Johnson (1868), Bill Clinton (1998), and Donald Trump (2019 and 2021); all were acquitted",
            "k": ["andrew johnson", "bill clinton", "donald trump", "acquitted"],
            "n": 0
        },
        {
            "id": "johnson-1868",
            "tier": "middle",
            "t": "Andrew Johnson was charged with breaking the Tenure of Office Act by trying to fire Edwin Stanton; the Senate fell one vote short of removing him",
            "k": ["tenure of office", "stanton", "one vote"],
            "n": 0,
            "rabbit": "Andrew Johnson"
        },
        {
            "id": "nixon",
            "tier": "middle",
            "t": "Richard Nixon resigned on August 9, 1974, after Peter Rodino’s House Judiciary Committee approved three articles but before the full House voted",
            "k": ["nixon", "resigned", "rodino", "1974"],
            "n": 0,
            "rabbit": "Watergate scandal"
        },
        {
            "id": "clinton",
            "tier": "middle",
            "t": "Bill Clinton was charged with perjury and obstruction of justice in December 1998 and acquitted in February 1999",
            "k": ["perjury", "obstruction of justice", "1999"],
            "n": 0,
            "rabbit": "Bill Clinton"
        },
        {
            "id": "trump-2019",
            "tier": "middle",
            "t": "The House charged Donald Trump with abuse of power and obstruction of Congress in December 2019; the Senate acquitted him in February 2020",
            "k": ["abuse of power", "obstruction of congress", "2019"],
            "n": 0
        },
        {
            "id": "trump-2021",
            "tier": "middle",
            "t": "The House charged Trump with incitement of insurrection after the January 6, 2021, attack on the U.S. Capitol; the Senate acquitted him after he left office",
            "k": ["incitement of insurrection", "january 6", "capitol"],
            "n": 0
        },
        {
            "id": "judges",
            "tier": "middle",
            "t": "Every official removed this way has been a federal judge; John Pickering of New Hampshire (1804) was the first",
            "k": ["federal judge", "pickering", "1804"],
            "n": 0
        },
        {
            "id": "samuel-chase",
            "tier": "middle",
            "t": "Samuel Chase is the only Supreme Court justice ever charged this way (1804); the Senate acquitted him in 1805",
            "k": ["samuel chase", "supreme court justice"],
            "n": 0
        },
        {
            "id": "articles-managers",
            "tier": "middle",
            "t": "The charges are called “articles,” usually drafted by the House Judiciary Committee; House “managers” act as prosecutors in the Senate",
            "k": ["articles", "managers", "judiciary committee"],
            "n": 0
        },
        {
            "id": "pardon-jury",
            "tier": "middle",
            "t": "The president’s pardon power does not cover these cases, and they are not tried by a jury",
            "k": ["pardon", "jury"],
            "n": 0
        },
        {
            "id": "mason",
            "tier": "power",
            "t": "George Mason first proposed “maladministration”; James Madison said it was too vague, so Mason chose “high crimes and misdemeanors”",
            "k": ["maladministration", "george mason", "madison"],
            "n": 0
        },
        {
            "id": "federalist-65",
            "tier": "power",
            "t": "Alexander Hamilton explained why the Senate should hold these trials in Federalist No. 65",
            "k": ["federalist no. 65", "federalist", "hamilton"],
            "n": 0
        },
        {
            "id": "blount",
            "tier": "power",
            "t": "Senator William Blount of Tennessee (1797) was the first federal official charged; the Senate expelled him instead",
            "k": ["blount", "1797", "expelled"],
            "n": 0
        },
        {
            "id": "burr",
            "tier": "power",
            "t": "Vice President Aaron Burr presided over Samuel Chase’s Senate trial (1805)",
            "k": ["aaron burr", "burr", "1805"],
            "n": 0
        },
        {
            "id": "belknap",
            "tier": "power",
            "t": "Secretary of War William Belknap (1876) was charged even though he had just resigned; the Senate acquitted him",
            "k": ["belknap", "secretary of war", "1876"],
            "n": 0
        },
        {
            "id": "chase-ross",
            "tier": "power",
            "t": "Chief Justice Salmon Chase presided over Andrew Johnson’s trial; Edmund Ross cast a key vote to acquit",
            "k": ["salmon chase", "edmund ross"],
            "n": 0
        },
        {
            "id": "hyde-rehnquist",
            "tier": "power",
            "t": "Chief Justice William Rehnquist presided over Clinton’s Senate trial; Henry Hyde led the House managers",
            "k": ["rehnquist", "henry hyde", "hyde"],
            "n": 0
        },
        {
            "id": "roberts-leahy",
            "tier": "power",
            "t": "John Roberts presided over Trump’s first trial (2020); Senator Patrick Leahy presided over the second (2021), held after Trump left office",
            "k": ["john roberts", "leahy", "2020"],
            "n": 0
        },
        {
            "id": "warren-hastings",
            "tier": "power",
            "t": "In Britain, Edmund Burke led the case against Warren Hastings, who was acquitted in 1795 after a seven-year trial",
            "k": ["warren hastings", "edmund burke", "1795"],
            "n": 0
        },
        {
            "id": "walter-nixon",
            "tier": "power",
            "t": "_Nixon v. United States_ (1993), about Judge Walter Nixon, let the Senate decide for itself how to run these trials",
            "k": ["walter nixon", "1993"],
            "n": 0
        },
        {
            "id": "alcee-hastings",
            "tier": "power",
            "t": "Judge Alcee Hastings was removed in 1989 and later won election to the U.S. House",
            "k": ["alcee hastings", "1989"],
            "n": 0
        },
        {
            "id": "tyler-ford",
            "tier": "power",
            "t": "John Botts’s 1843 resolution against John Tyler failed; in 1970, Gerald Ford tried to target Justice William O. Douglas",
            "k": ["john tyler", "botts", "gerald ford", "douglas"],
            "n": 0
        },
        {
            "id": "porteous",
            "tier": "power",
            "t": "Judge Thomas Porteous (2010) was removed and barred from future office; convicted officials can still face criminal trials",
            "k": ["porteous", "2010", "barred"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Charged is not removed",
        "body": "Being impeached means the House has approved charges; it does not mean the official was removed. Andrew Johnson, Bill Clinton, and Donald Trump were all impeached, and the Senate acquitted every one of them. Richard Nixon was never impeached: he resigned in 1974 before the full House voted. Players also confuse impeachment with censure (a vote that formally scolds someone), recall (an election that removes a state or local official), and the 25th Amendment (replacing a president who cannot do the job).",
        "fix": "If the question describes the House bringing charges and the Senate holding a trial, say “impeachment.” If it asks which president resigned, the answer is Nixon; if it asks for the first president impeached, the answer is Andrew Johnson.",
        "line": "Real answer line: <b><u>impeachment</u></b> (accept word forms like <u>impeach</u> or <u>impeached</u>)"
    },
    "tests": {
        "right": [
            "impeachment",
            "Impeach",
            "impeached",
            "impeachmnet",
            "impeachment process"
        ],
        "prompt": [
            "removal from office",
            "Senate trial"
        ],
        "wrong": [
            "censure",
            "recall election",
            "25th Amendment",
            "veto",
            "resignation",
            "Watergate"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
