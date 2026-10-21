import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "john-roberts",
    "name": "John Roberts",
    "mono": "JGR",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "17th Chief Justice, confirmed in 2005 · Appointed by George W. Bush",
    "dates": "Born 1955",
    "briefing": "As a young lawyer, John Roberts clerked for Justice William Rehnquist, and in 2005 he succeeded his old boss as Chief Justice of the United States. At his confirmation hearing, he compared judges to umpires, saying his job was “to call balls and strikes, and not to pitch or bat.” He wrote the 2012 decision that upheld the Affordable Care Act’s insurance requirement as a tax, and he presided over Donald Trump’s first Senate impeachment trial in 2020.",
    "answerHtml": "John <b><u>Roberts</u></b> (accept John Glover <u>Roberts</u> Jr.; do not accept “Owen Roberts”)",
    "accept": [
        "john roberts",
        "roberts",
        "john glover roberts",
        "john glover roberts jr",
        "john g roberts",
        "john roberts jr",
        "chief justice roberts",
        "chief justice john roberts",
        "justice roberts"
    ],
    "prompt": [],
    "reject": [
        "owen roberts",
        "owen j roberts",
        "william rehnquist",
        "rehnquist",
        "john marshall",
        "john jay",
        "john rutledge",
        "earl warren",
        "warren burger",
        "samuel alito",
        "alito",
        "antonin scalia",
        "scalia",
        "clarence thomas",
        "anthony kennedy",
        "sandra day oconnor",
        "brett kavanaugh",
        "neil gorsuch",
        "amy coney barrett",
        "sonia sotomayor",
        "elena kagan",
        "ketanji brown jackson",
        "ruth bader ginsburg",
        "john paul stevens",
        "harriet miers",
        "henry friendly",
        "julia roberts",
        "oral roberts",
        "nora roberts",
        "pat roberts",
        "robin roberts",
        "cokie roberts",
        "bartholomew roberts",
        "roberts rules of order",
        "roberts rules",
        "george w bush"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/John_Roberts",
    "qb": {
        "q": "John Roberts",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "After serving as managing editor of the _Harvard Law Review_, this lawyer clerked for Judge Henry Friendly of the Second Circuit Court of Appeals and then for Justice William Rehnquist [“REN-kwist”]. He then joined Ronald Reagan’s Justice Department.",
            "r": "In 2005, he succeeded Rehnquist as Chief Justice. For 10 points, name this man appointed by George W. Bush."
        },
        {
            "p": "In Ronald Reagan’s administration, this young lawyer worked as a special assistant to Attorney General William French Smith and then in the White House counsel’s office. Later, as principal deputy solicitor general under George H. W. Bush, he argued cases for the government before the Supreme Court.",
            "r": "For 10 points, name this man who was confirmed as Chief Justice of the United States in 2005."
        },
        {
            "p": "Before becoming a judge, this lawyer argued 39 cases before the Supreme Court, many of them while working at the Washington law firm Hogan & Hartson. In 1992, George H. W. Bush nominated him to a federal appeals court, but the Senate never voted on the nomination.",
            "r": "For 10 points, name this man whom George W. Bush later made Chief Justice of the United States."
        },
        {
            "p": "As an appeals court judge in Washington, D.C., this man joined a 2005 ruling in _Hamdan v. Rumsfeld_ allowing military trials for prisoners at Guantanamo Bay, so he sat out the case when the Supreme Court reversed that ruling the next year.",
            "r": "By then, he had become Chief Justice. For 10 points, name this successor of William Rehnquist."
        },
        {
            "p": "In July 2005, George W. Bush nominated this appeals court judge to replace the retiring Sandra Day O’Connor. After William Rehnquist died that September, Bush withdrew that nomination and named this judge for a different seat on the same court.",
            "r": "For 10 points, name this man who was confirmed as Chief Justice of the United States in September 2005."
        },
        {
            "p": "The Senate confirmed this man by a vote of 78 to 22, and at age 50 he became the youngest person to lead his court in more than 200 years. He was the 17th person to hold his job.",
            "r": "For 10 points, name this man who succeeded William Rehnquist as Chief Justice of the United States in 2005."
        },
        {
            "p": "In his opening statement to the Senate Judiciary Committee in September 2005, this nominee said that “judges and justices are servants of the law, not the other way around.” He was then a judge on the D.C. Circuit.",
            "r": "In the same speech, he compared judges to umpires who “call balls and strikes.” For 10 points, name this man who became Chief Justice."
        },
        {
            "p": "In January 2009, this man and Barack Obama got the words of the presidential oath out of order, so the next day this man gave Obama the oath again at the White House, just to be safe.",
            "r": "For 10 points, name this Chief Justice of the United States, appointed by George W. Bush."
        },
        {
            "p": "In _National Federation of Independent Business v. Sebelius_ [“suh-BEE-lee-us”], this judge wrote that Congress could not require people to buy health insurance under its power to regulate commerce, but that the requirement was allowed as a tax.",
            "r": "That 2012 decision upheld most of the Affordable Care Act. For 10 points, name this Chief Justice."
        },
        {
            "p": "In _Shelby County v. Holder_ (2013), this judge wrote for a 5–4 majority that struck down the formula deciding which states and counties needed federal approval before changing their voting laws under the Voting Rights Act of 1965.",
            "r": "For 10 points, name this Chief Justice, who joined the Supreme Court in 2005 after George W. Bush nominated him."
        },
        {
            "p": "In 2015, this judge wrote the majority opinion in _King v. Burwell_, which allowed health insurance subsidies to continue in every state, and the main dissent in _Obergefell v. Hodges_, the case that legalized same-sex marriage nationwide.",
            "r": "For 10 points, name this Chief Justice appointed by George W. Bush, who had clerked for William Rehnquist."
        },
        {
            "p": "This judge gave Donald Trump the presidential oath in 2017 and again in January 2025, when cold weather moved the ceremony indoors to the Capitol Rotunda. He had given the oath to Joe Biden in 2021.",
            "r": "In 2020, he presided over Trump’s first Senate impeachment trial. For 10 points, name this Chief Justice."
        },
        {
            "p": "In 2023, this judge wrote the majority opinion in _Students for Fair Admissions v. Harvard_, which ruled that colleges’ race-conscious admissions programs violated the Equal Protection Clause. The next day, he wrote the decision that blocked a federal plan to forgive student loans.",
            "r": "For 10 points, name this Chief Justice, who presided over Donald Trump’s first impeachment trial in 2020."
        },
        {
            "p": "This man was born in Buffalo, New York, in 1955, grew up in Long Beach, Indiana, and captained the football team at La Lumiere, a Catholic boarding school in La Porte, Indiana. He then graduated from Harvard College in just three years.",
            "r": "For 10 points, name this man who became Chief Justice of the United States in 2005, succeeding William Rehnquist."
        },
        {
            "p": "In November 2018, this judge responded to a president’s criticism of another federal judge by declaring, “We do not have Obama judges or Trump judges, Bush judges or Clinton judges.” He said the country should be thankful for an independent judiciary.",
            "r": "For 10 points, name this Chief Justice, who was appointed by George W. Bush in 2005."
        }
    ],
    "clues": [
        {
            "id": "chief-justice",
            "tier": "giveaway",
            "t": "Confirmed as Chief Justice of the United States in 2005, the 17th person in that job",
            "k": ["chief justice", "2005", "17th"],
            "n": 0,
            "rabbit": "U.S. Supreme Court"
        },
        {
            "id": "bush",
            "tier": "giveaway",
            "t": "Nominated by President George W. Bush",
            "k": ["george w. bush", "bush"],
            "n": 0,
            "rabbit": "George W. Bush"
        },
        {
            "id": "rehnquist",
            "tier": "giveaway",
            "t": "Succeeded William Rehnquist, for whom he had once clerked",
            "k": ["william rehnquist", "rehnquist", "clerked"],
            "n": 0
        },
        {
            "id": "umpire",
            "tier": "giveaway",
            "t": "At his confirmation hearing, compared judges to umpires who “call balls and strikes, and not to pitch or bat”",
            "k": ["umpires", "balls and strikes"],
            "n": 0
        },
        {
            "id": "nfib",
            "tier": "middle",
            "t": "_NFIB v. Sebelius_ (2012): upheld the Affordable Care Act’s insurance requirement as a tax",
            "k": ["nfib", "sebelius", "affordable care act", "tax"],
            "n": 0,
            "rabbit": "Affordable Care Act"
        },
        {
            "id": "impeachment",
            "tier": "middle",
            "t": "Presided over Donald Trump’s first Senate impeachment trial (2020)",
            "k": ["impeachment", "donald trump", "2020"],
            "n": 0,
            "rabbit": "Impeachment"
        },
        {
            "id": "oconnor",
            "tier": "middle",
            "t": "First nominated (July 2005) to replace Sandra Day O’Connor; renominated for Chief Justice after Rehnquist died",
            "k": ["sandra day o’connor", "o’connor", "renominated"],
            "n": 0
        },
        {
            "id": "dc-circuit",
            "tier": "middle",
            "t": "Judge on the U.S. Court of Appeals for the D.C. Circuit (2003–2005)",
            "k": ["d.c. circuit", "court of appeals"],
            "n": 0
        },
        {
            "id": "youngest",
            "tier": "middle",
            "t": "At 50, the youngest Chief Justice in more than 200 years (only John Jay and John Marshall started younger); confirmed 78–22",
            "k": ["john marshall", "youngest", "78–22"],
            "n": 0,
            "rabbit": "John Marshall"
        },
        {
            "id": "oath",
            "tier": "middle",
            "t": "Gave the presidential oath to Barack Obama (2009, 2013), Donald Trump (2017, 2025), and Joe Biden (2021)",
            "k": ["presidential oath", "oath"],
            "n": 0
        },
        {
            "id": "friendly",
            "tier": "power",
            "t": "Managing editor of the _Harvard Law Review_; clerked for Judge Henry Friendly of the Second Circuit before clerking for Rehnquist",
            "k": ["henry friendly", "harvard law review", "second circuit"],
            "n": 0
        },
        {
            "id": "reagan",
            "tier": "power",
            "t": "In the Reagan administration, worked for Attorney General William French Smith and in the White House counsel’s office",
            "k": ["reagan", "william french smith", "white house counsel"],
            "n": 0
        },
        {
            "id": "solicitor",
            "tier": "power",
            "t": "Principal deputy solicitor general under George H. W. Bush (1989–1993)",
            "k": ["deputy solicitor general", "solicitor general"],
            "n": 0
        },
        {
            "id": "thirty-nine-cases",
            "tier": "power",
            "t": "Argued 39 cases before the Supreme Court, many while at the law firm Hogan & Hartson",
            "k": ["39 cases", "hogan & hartson"],
            "n": 0
        },
        {
            "id": "nomination-1992",
            "tier": "power",
            "t": "George H. W. Bush’s 1992 nomination of him to an appeals court never got a Senate vote",
            "k": ["1992", "senate vote"],
            "n": 0
        },
        {
            "id": "hamdan",
            "tier": "power",
            "t": "Joined the D.C. Circuit’s 2005 ruling in _Hamdan v. Rumsfeld_, so he sat out the case at the Supreme Court",
            "k": ["hamdan", "rumsfeld", "sat out"],
            "n": 0
        },
        {
            "id": "servants",
            "tier": "power",
            "t": "Told senators in 2005 that “judges and justices are servants of the law, not the other way around”",
            "k": ["servants of the law", "servants"],
            "n": 0
        },
        {
            "id": "obama-oath",
            "tier": "power",
            "t": "He and Barack Obama got the oath’s words out of order in 2009, so he gave it again the next day",
            "k": ["barack obama", "out of order", "next day"],
            "n": 0
        },
        {
            "id": "shelby",
            "tier": "power",
            "t": "_Shelby County v. Holder_ (2013): struck down the Voting Rights Act’s formula for which places needed federal approval",
            "k": ["shelby county", "voting rights act", "holder"],
            "n": 0
        },
        {
            "id": "king-burwell",
            "tier": "power",
            "t": "_King v. Burwell_ (2015): allowed health insurance subsidies to continue in every state",
            "k": ["king v. burwell", "burwell", "subsidies"],
            "n": 0
        },
        {
            "id": "obergefell",
            "tier": "power",
            "t": "Wrote the main dissent in _Obergefell v. Hodges_ (2015), the same-sex marriage case",
            "k": ["obergefell", "dissent", "same-sex marriage"],
            "n": 0,
            "rabbit": "Same-sex marriage"
        },
        {
            "id": "sffa",
            "tier": "power",
            "t": "Wrote the 2023 majority opinions in _Students for Fair Admissions v. Harvard_ and in the student-loan forgiveness case",
            "k": ["students for fair admissions", "student-loan", "2023"],
            "n": 0,
            "rabbit": "Affirmative action"
        },
        {
            "id": "indiana",
            "tier": "power",
            "t": "Born in Buffalo, New York (1955); grew up in Long Beach, Indiana; football captain at La Lumiere School; finished Harvard College in three years",
            "k": ["buffalo", "long beach", "la lumiere", "three years"],
            "n": 0
        },
        {
            "id": "obama-judges",
            "tier": "power",
            "t": "2018: “We do not have Obama judges or Trump judges, Bush judges or Clinton judges”",
            "k": ["obama judges", "trump judges"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Which Chief Justice?",
        "body": "Several chief justices show up in the same kinds of clues. William Rehnquist was Chief Justice from 1986 to 2005 and presided over Bill Clinton’s impeachment trial; John Roberts, who once clerked for him, replaced him in 2005 and presided over Donald Trump’s first trial in 2020. John Marshall, the fourth Chief Justice, is famous for _Marbury v. Madison_, and Owen Roberts was a different justice whose 1937 vote was called “the switch in time that saved nine.”",
        "fix": "George W. Bush, the umpire comparison, _NFIB v. Sebelius_, and the 2020 trial mean John Roberts. Bill Clinton’s 1999 trial and Richard Nixon’s 1971 appointment mean Rehnquist. Saying “Roberts” alone is fine, but never say “Owen Roberts.”",
        "line": "Real answer line: John <b><u>Roberts</u></b> (accept John Glover <u>Roberts</u> Jr.)"
    },
    "tests": {
        "right": [
            "John Roberts",
            "Roberts",
            "Chief Justice John Roberts",
            "John Glover Roberts Jr.",
            "John Robertz",
            "Jon Roberts"
        ],
        "prompt": [],
        "wrong": [
            "William Rehnquist",
            "Owen Roberts",
            "John Marshall",
            "John Jay",
            "Samuel Alito",
            "Antonin Scalia",
            "Earl Warren",
            "Julia Roberts"
        ]
    }
}

out = ROOT / "topics" / f"{data['id']}.json"
with open(out, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("wrote", out)
