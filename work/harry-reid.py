import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def T(p, r):
    return {"p": p, "r": r}


def C(cid, tier, t, k, rabbit=None):
    c = {"id": cid, "tier": tier, "t": t, "k": k, "n": 0}
    if rabbit:
        c["rabbit"] = rabbit
    return c


data = {
    "id": "harry-reid",
    "name": "Harry Reid",
    "mono": "HMR",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "Senate Majority Leader (2007–2015) · Nevada Democrat from Searchlight",
    "dates": "1939–2021",
    "briefing": "Harry Reid grew up in Searchlight, a tiny Nevada mining town, boxed as an amateur, and worked as a U.S. Capitol Police officer to help pay for law school. He represented Nevada in the U.S. Senate from 1987 to 2017 and was Senate Majority Leader from 2007 to 2015. In 2013 he led the “nuclear option” rules change for nominations, and in 2021, shortly before his death, Las Vegas renamed its airport Harry Reid International Airport.",
    "answerHtml": "Harry <b><u>Reid</u></b> (accept Harry Mason <u>Reid</u>; prompt on “Harry” alone)",
    "accept": [
        "harry reid",
        "harry mason reid",
        "harry m reid",
        "reid",
        "senator reid",
        "senator harry reid"
    ],
    "prompt": [
        "harry"
    ],
    "reject": [
        "harry s truman",
        "harry truman",
        "truman",
        "harry byrd",
        "harry f byrd",
        "harry hopkins",
        "jack reed",
        "thomas reed",
        "thomas brackett reed",
        "walter reed",
        "mitch mcconnell",
        "mcconnell",
        "chuck schumer",
        "schumer",
        "tom daschle",
        "daschle",
        "nancy pelosi",
        "pelosi",
        "john boehner",
        "bill frist",
        "bob dole",
        "lyndon johnson",
        "lyndon b johnson",
        "paul laxalt",
        "laxalt",
        "pat mccarran",
        "mccarran",
        "john ensign",
        "sharron angle",
        "mike ocallaghan",
        "catherine cortez masto",
        "dick durbin",
        "nevada"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Harry_Reid",
    "qb": {
        "q": "Harry Reid",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        T("While studying law at George Washington University, this future senator paid his way partly by working as a U.S. Capitol Police officer. He later chaired the Nevada Gaming Commission, which regulates the state’s casinos.",
          "For 10 points, name this Nevada Democrat who served as Senate Majority Leader from 2007 to 2015."),
        T("This man grew up in the tiny mining town of Searchlight and attended high school in Henderson, where his teacher and mentor was future Nevada governor Mike O’Callaghan. This man later served as lieutenant governor while O’Callaghan was governor.",
          "For 10 points, name this Nevada senator who was the Senate Majority Leader from 2007 to 2015."),
        T("In November 2013, this Senate leader led a rules change that let most presidential nominees be confirmed by a simple majority instead of the 60 votes needed to end a filibuster. That change was nicknamed the “nuclear option.”",
          "For 10 points, name this Nevada Democrat who was Senate Majority Leader from 2007 to 2015."),
        T("This senator spent decades fighting a federal plan to store the nation’s nuclear waste at Yucca Mountain, northwest of Las Vegas. Congress had chosen that site in 1987, the year this man joined the Senate.",
          "For 10 points, name this Nevada Democrat, the Senate Majority Leader from 2007 to 2015."),
        T("On December 24, 2009, this Senate leader brought the Affordable Care Act to a 60–39 vote that passed the bill in the Senate, with no Republican votes. Months earlier, he had helped pass an economic stimulus law, the American Recovery and Reinvestment Act.",
          "For 10 points, name this Nevada senator who was Majority Leader from 2007 to 2015."),
        T("In January 2022, this former senator lay in state in the Rotunda of the U.S. Capitol, the building where he had once worked as a police officer. He had died in December 2021 in Henderson, Nevada.",
          "Weeks earlier, Las Vegas had renamed its main airport for him. For 10 points, name this Senate Majority Leader from 2007 to 2015."),
        T("This man served as Nevada’s lieutenant governor from 1971 to 1975, and in 1974 he narrowly lost a U.S. Senate race to Republican Paul Laxalt. He won that same Senate seat in 1986, after Laxalt retired.",
          "For 10 points, name this Democrat who served as Senate Majority Leader from 2007 to 2015."),
        T("A former amateur boxer, this man titled his 2008 memoir _The Good Fight_. Ten years earlier, he had written a history of his hometown, a mining camp in the desert of southern Nevada called Searchlight.",
          "For 10 points, name this Nevada senator who led Senate Democrats from 2005 to 2017."),
        T("This man became the Senate’s top Democrat after Tom Daschle of South Dakota lost his seat in the 2004 election. Chuck Schumer of New York took over that role when this man retired in 2017.",
          "For 10 points, name this Nevada senator who was Majority Leader from 2007 to 2015."),
        T("Before joining the Senate in 1987, this man spent two terms in the U.S. House, representing a district that included Las Vegas. In the Senate, he served as his party’s whip, its second-ranking leader, before becoming its leader.",
          "For 10 points, name this Nevada Democrat who was Senate Majority Leader from 2007 to 2015."),
        T("This man and his wife, Landra, joined The Church of Jesus Christ of Latter-day Saints while he was a student at Utah State University. He later earned his law degree at George Washington University in Washington, D.C.",
          "For 10 points, name this Nevada senator who led Senate Democrats during Barack Obama’s presidency."),
        T("In 2010, this senator won a fifth term by defeating Republican Sharron Angle, a candidate backed by the Tea Party movement. Twelve years earlier, he had won reelection over John Ensign by only a few hundred votes.",
          "For 10 points, name this Nevada Democrat, the Senate Majority Leader from 2007 to 2015."),
        T("This man served 30 years in the Senate, from 1987 to 2017, longer than anyone else from his state. His Republican counterpart for most of his time as party leader was Mitch McConnell of Kentucky.",
          "For 10 points, name this Nevada Democrat for whom the main Las Vegas airport was renamed in 2021."),
        T("This man helped pass the 2010 repeal of “Don’t Ask, Don’t Tell,” which let gay, lesbian, and bisexual Americans serve openly in the military. That same year, he helped pass the Dodd–Frank law, which set new rules for banks.",
          "For 10 points, name this Nevada Democrat who was Senate Majority Leader from 2007 to 2015."),
        T("After Republicans won control of the Senate in the 2014 elections, this man became Minority Leader again. In 2015, he announced that he would not seek a sixth term, and he retired in January 2017.",
          "For 10 points, name this Nevada Democrat who had been Senate Majority Leader from 2007 until that change.")
    ],
    "clues": [
        C("majority-leader", "giveaway", "Senate Majority Leader from 2007 to 2015, a Democrat", ["majority leader", "2007", "2015"]),
        C("democratic-leader", "giveaway", "Led Senate Democrats from 2005 to 2017, including during Barack Obama’s presidency", ["senate democrats", "barack obama", "2005"], "Barack Obama"),
        C("airport", "giveaway", "Las Vegas’s main airport was renamed for him in December 2021, shortly before his death", ["airport", "las vegas"]),
        C("nevada", "middle", "Represented Nevada in the U.S. Senate (1987–2017) after two terms in the House (1983–1987)", ["nevada", "1987", "house"], "Nevada"),
        C("searchlight", "middle", "Grew up in the small mining town of Searchlight, Nevada", ["searchlight", "mining town"]),
        C("nuclear-option", "middle", "Led the 2013 “nuclear option”: most nominees could be confirmed by a simple majority, ending filibusters of them", ["nuclear option", "simple majority", "filibusters"], "Filibuster"),
        C("boxer", "middle", "Former amateur boxer; his 2008 memoir is _The Good Fight_", ["boxer", "the good fight"]),
        C("yucca", "middle", "Fought plans to store the nation’s nuclear waste at Yucca Mountain, Nevada", ["yucca mountain", "nuclear waste"]),
        C("aca", "middle", "Led Senate passage of the Affordable Care Act on December 24, 2009", ["affordable care act", "december 24, 2009"], "Affordable Care Act"),
        C("mcconnell", "middle", "His Republican counterpart was Mitch McConnell, who became Majority Leader in 2015", ["mitch mcconnell", "mcconnell"]),
        C("minority-leader", "middle", "Minority Leader before (2005–2007) and after (2015–2017) his years as Majority Leader", ["minority leader"]),
        C("lay-in-state", "middle", "Died in December 2021; lay in state in the Capitol Rotunda (January 2022)", ["lay in state", "rotunda", "2021"]),
        C("capitol-police", "power", "Worked as a U.S. Capitol Police officer while in law school at George Washington University", ["capitol police", "george washington university"]),
        C("gaming", "power", "Chaired the Nevada Gaming Commission, which regulates casinos (1977–1981)", ["gaming commission", "casinos"]),
        C("ocallaghan", "power", "His high school teacher and mentor, Mike O’Callaghan, became governor; he served as lieutenant governor (1971–1975)", ["mike o’callaghan", "o’callaghan", "lieutenant governor"]),
        C("laxalt", "power", "Narrowly lost the 1974 Senate race to Republican Paul Laxalt; won the seat in 1986 after Laxalt retired", ["paul laxalt", "laxalt", "1974"]),
        C("searchlight-book", "power", "Wrote a history of his hometown, _Searchlight: The Camp That Didn’t Fail_ (1998)", ["the camp that didn’t fail", "history"]),
        C("daschle-schumer", "power", "Followed Tom Daschle as Democratic leader (2005); Chuck Schumer followed him (2017)", ["tom daschle", "daschle", "chuck schumer", "schumer"]),
        C("mccarran", "power", "The Las Vegas airport had been named for Senator Pat McCarran", ["pat mccarran", "mccarran"]),
        C("whip", "power", "Served as the Senate Democrats’ whip (1999–2005) before becoming their leader", ["whip", "1999"]),
        C("lds", "power", "Joined The Church of Jesus Christ of Latter-day Saints while at Utah State University", ["latter-day saints", "utah state"]),
        C("angle-ensign", "power", "Beat Sharron Angle in 2010; had beaten John Ensign in 1998 by only a few hundred votes", ["sharron angle", "john ensign", "ensign"]),
        C("thirty-years", "power", "Served 30 years in the Senate, the longest of any senator from Nevada", ["30 years", "longest"]),
        C("laws", "power", "Helped pass the stimulus law (2009), Dodd–Frank (2010), and the repeal of “Don’t Ask, Don’t Tell” (2010)", ["stimulus", "dodd–frank", "don’t ask, don’t tell"]),
        C("retired", "power", "Announced in 2015 that he would not run for a sixth term; retired in January 2017", ["sixth term", "retired"])
    ],
    "trap": {
        "title": "Which Senate leader?",
        "body": "Several modern Senate leaders show up in quiz bowl, and their clues blur together. Harry Reid of Nevada led Senate Democrats from 2005 to 2017; Mitch McConnell of Kentucky, his Republican counterpart, took over as Majority Leader in 2015; and Chuck Schumer of New York followed Reid as Democratic leader in 2017. Nancy Pelosi, who was Speaker of the House while Reid was Majority Leader, led the other chamber of Congress.",
        "fix": "Nevada, Searchlight, boxing, Yucca Mountain, the Capitol Police, and the Las Vegas airport mean Reid. If a question asks for the 2013 rules change, the answer is the “nuclear option,” and if it asks for the delaying tactic that change limited, the answer is the filibuster. Don’t confuse him with Harry Truman or with Senator Jack Reed of Rhode Island.",
        "line": "Real answer line: Harry <b><u>Reid</u></b> (accept Harry Mason <u>Reid</u>)"
    },
    "tests": {
        "right": [
            "Harry Reid",
            "Reid",
            "Senator Harry Reid",
            "Harry Mason Reid",
            "Harry Reed"
        ],
        "prompt": [
            "Harry"
        ],
        "wrong": [
            "Harry Truman",
            "Mitch McConnell",
            "Chuck Schumer",
            "Jack Reed",
            "Nancy Pelosi",
            "Tom Daschle"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
