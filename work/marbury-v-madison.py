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
    "id": "marbury-v-madison",
    "name": "Marbury v. Madison",
    "mono": "MVM",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "1803 Supreme Court case · Established judicial review",
    "dates": "Decided 1803",
    "briefing": "In his last days as president, John Adams rushed to appoint dozens of new officials, but some of their commissions were never delivered. When one of them, William Marbury, sued, Chief Justice John Marshall used the case to declare that the Supreme Court can strike down laws that break the Constitution. That power, called judicial review, helped make the Court one of the most important parts of the U.S. government.",
    "answerHtml": "<b><u>Marbury</u></b> v. Madison",
    "accept": [
        "marbury v madison",
        "marbury versus madison",
        "marbury vs madison",
        "marbury v james madison",
        "william marbury v james madison",
        "marbury"
    ],
    "prompt": [],
    "reject": [
        "mcculloch v maryland",
        "mcculloch",
        "gibbons v ogden",
        "fletcher v peck",
        "dred scott v sandford",
        "dred scott",
        "plessy v ferguson",
        "brown v board of education",
        "martin v hunters lessee",
        "cohens v virginia",
        "dartmouth college v woodward",
        "stuart v laird",
        "worcester v georgia",
        "cherokee nation v georgia",
        "judicial review",
        "judiciary act of 1789",
        "judiciary act of 1801",
        "judiciary act",
        "midnight judges",
        "writ of mandamus",
        "mandamus",
        "john marshall",
        "thomas jefferson",
        "john adams"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Marbury_v._Madison",
    "qb": {
        "q": "Marbury",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {"n": 0, "note": "no real tossups checked yet"},
    "tossups": [
        T("This case struck down Section 13 of the Judiciary Act of 1789 because that law tried to give the Supreme Court more original jurisdiction than Article III of the Constitution allows. It was the first time the Court overturned an act of Congress.",
          "For 10 points, name this 1803 Supreme Court case in which Chief Justice John Marshall established judicial review."),
        T("In this case, the Chief Justice declared, “It is emphatically the province and duty of the judicial department to say what the law is.” He reasoned that when a law conflicts with the Constitution, judges must follow the Constitution.",
          "That Chief Justice was John Marshall. For 10 points, name this 1803 Supreme Court case that established judicial review."),
        T("The plaintiff in this case asked the Supreme Court to issue a writ of mandamus, Latin for “we command,” ordering a cabinet officer to hand over a document. That document was a signed commission naming the plaintiff a justice of the peace in the District of Columbia.",
          "For 10 points, name this 1803 case in which the Court claimed the power of judicial review."),
        T("After Congress repealed the Judiciary Act of 1801, it also canceled the Supreme Court’s 1802 term, so the justices did not hear this case until February 1803. Many Federalist judges lost their new jobs when that 1801 law was repealed.",
          "The case grew out of John Adams’s last-minute “midnight judges.” For 10 points, name this case in which John Marshall’s Court established judicial review."),
        T("The Chief Justice who decided this case had, as John Adams’s Secretary of State, sealed the very commission at the center of the dispute but failed to get it delivered before Adams left office. That Chief Justice nevertheless ruled that the commission was valid.",
          "That Chief Justice was John Marshall. For 10 points, name this 1803 case that established judicial review."),
        T("Former Attorney General Charles Lee argued this case for a plaintiff whom John Adams had named a justice of the peace. The defendant, the new Secretary of State, did not even send a lawyer to argue his side.",
          "For 10 points, name this case in which John Marshall declared that courts can strike down unconstitutional laws."),
        T("The opinion in this case asked three questions: whether the plaintiff had a right to his commission, whether the law gave him a remedy, and whether this Court could order the remedy he wanted. The answers were yes, yes, and no.",
          "For 10 points, name this 1803 case in which John Marshall established the power of judicial review."),
        T("After this case, the Supreme Court did not strike down another act of Congress until it ruled the Missouri Compromise unconstitutional in _Dred Scott v. Sandford_ in 1857. Both decisions found that Congress had gone beyond the powers the Constitution gave it.",
          "For 10 points, name this 1803 case, John Marshall’s most famous decision, which established judicial review."),
        T("This decision argued that “a law repugnant to the constitution is void,” since the Constitution is the supreme law that every judge swears to uphold. It overturned part of a 1789 law that had organized the federal courts.",
          "For 10 points, name this case in which Chief Justice John Marshall established judicial review."),
        T("This case ruled that Congress could not add to Article III’s short list of cases that go straight to the Supreme Court, such as those involving ambassadors or a state. So the Court could not give the plaintiff what he asked for.",
          "Chief Justice John Marshall wrote the opinion. For 10 points, name this 1803 case that established judicial review."),
        T("When Thomas Jefferson took office, his administration refused to deliver several commissions that John Adams had signed in his final days as president. One man who never received his commission sued the new Secretary of State in this case.",
          "For 10 points, name this 1803 case in which Chief Justice John Marshall established judicial review."),
        T("Alexander Hamilton had argued in _Federalist_ No. 78 that judges should treat the Constitution as a higher law than ordinary laws, an idea this case put into practice. This case’s opinion warned that a written constitution would mean nothing if Congress could ignore it.",
          "John Marshall wrote that opinion. For 10 points, name this 1803 case that established judicial review."),
        T("Justice Samuel Chase, a member of the Supreme Court that decided this case, was impeached by the House the next year, though the Senate acquitted him. Thomas Jefferson’s allies distrusted the Court’s Federalist Chief Justice, whom John Adams had appointed.",
          "That Chief Justice was John Marshall. For 10 points, name this 1803 case that established judicial review."),
        T("By ruling that his Court could not order the delivery of a commission, the Chief Justice avoided giving an order that President Jefferson would likely have ignored, while claiming a powerful new role for the courts. The plaintiff in this case never got his job.",
          "That role was judicial review. For 10 points, name this 1803 case decided by John Marshall’s Court."),
        T("Seven years after this case, the same Chief Justice used _Fletcher v. Peck_ to strike down a Georgia law, one of the first times the Court overturned a state law. That Chief Justice, John Marshall, served longer than any other Chief Justice in American history.",
          "For 10 points, name this 1803 case, which established that federal courts can strike down acts of Congress."),
    ],
    "clues": [
        C("judicial-review", "giveaway", "Established judicial review: courts can strike down laws that go against the Constitution", ["judicial review", "strike down", "constitution"]),
        C("decided-1803", "giveaway", "Decided by the Supreme Court in 1803", ["1803", "supreme court"], "U.S. Supreme Court"),
        C("marshall", "giveaway", "Chief Justice John Marshall wrote the Court’s unanimous opinion", ["john marshall", "chief justice", "unanimous"], "John Marshall"),
        C("midnight", "giveaway", "Grew out of John Adams’s last-minute “midnight judges” appointments (1801)", ["midnight judges", "midnight", "john adams"], "John Adams"),
        C("commission", "middle", "The plaintiff, named a justice of the peace for the District of Columbia, never received his signed commission", ["commission", "justice of the peace", "district of columbia"]),
        C("jefferson", "middle", "President Thomas Jefferson’s administration refused to deliver the commission", ["thomas jefferson", "jefferson", "refused"], "Thomas Jefferson"),
        C("mandamus", "middle", "The plaintiff asked for a writ of mandamus (Latin for “we command”) to force the Secretary of State to deliver it", ["writ of mandamus", "mandamus", "we command"]),
        C("first-struck", "middle", "The first time the Supreme Court struck down an act of Congress", ["first time", "act of congress"]),
        C("province", "middle", "Marshall: “It is emphatically the province and duty of the judicial department to say what the law is”", ["province and duty", "say what the law is", "emphatically"]),
        C("never-got-job", "middle", "The Court said the plaintiff deserved his commission but could not order it delivered, so he never got the job", ["never got", "deserved"]),
        C("section-13", "power", "Struck down Section 13 of the Judiciary Act of 1789, which gave the Court more original jurisdiction than Article III allows", ["section 13", "judiciary act of 1789", "original jurisdiction", "article iii"]),
        C("article-iii", "power", "Article III lists the few kinds of cases that go straight to the Supreme Court, such as those involving ambassadors or states", ["article iii", "ambassadors", "straight"]),
        C("dred-scott", "power", "The Court did not strike down another act of Congress until _Dred Scott v. Sandford_ (1857)", ["dred scott", "1857"], "Dred Scott v. Sandford"),
        C("repugnant", "power", "Marshall wrote that “a law repugnant to the constitution is void”", ["repugnant", "void"]),
        C("three-questions", "power", "Marshall’s three questions: a right to the commission? (yes) A legal remedy? (yes) Could this Court order it? (no)", ["three questions", "remedy"]),
        C("marshall-secretary", "power", "As Adams’s Secretary of State, John Marshall himself had sealed the commission but failed to get it delivered", ["sealed", "failed", "secretary of state"]),
        C("term-1802", "power", "Congress repealed the Judiciary Act of 1801 and canceled the Court’s 1802 term, delaying the case until 1803", ["judiciary act of 1801", "1802", "repealed", "canceled"]),
        C("charles-lee", "power", "Former Attorney General Charles Lee argued the plaintiff’s side; the government sent no lawyer", ["charles lee", "attorney general"]),
        C("federalist-78", "power", "Alexander Hamilton had argued for judicial review in _Federalist_ No. 78", ["federalist", "no. 78", "hamilton"], "The Federalist Papers"),
        C("chase", "power", "Justice Samuel Chase, on the Court that decided it, was impeached in 1804 but acquitted by the Senate", ["samuel chase", "impeached", "acquitted"]),
        C("won-by-losing", "power", "Marshall avoided an order that Jefferson would likely have ignored, while claiming a powerful new role for the courts", ["powerful", "ignored", "new role"]),
        C("fletcher", "power", "_Fletcher v. Peck_ (1810) struck down a Georgia law, one of the first times the Court overturned a state law", ["fletcher", "georgia", "state law", "1810"]),
        C("longest", "power", "Marshall, the fourth Chief Justice, served from 1801 to 1835, longer than any other Chief Justice", ["fourth chief justice", "1835", "longer"]),
    ],
    "trap": {
        "title": "Which Marshall Court case?",
        "body": "John Marshall’s Supreme Court decided several famous cases, and players mix them up. This case (1803) created judicial review; _McCulloch v. Maryland_ (1819) upheld the national bank and said “the power to tax involves the power to destroy”; and _Gibbons v. Ogden_ (1824) gave Congress power over steamboats crossing state lines. Some players also answer “judicial review,” which is the idea this case created, not the case itself.",
        "fix": "Midnight judges, an undelivered commission, a writ of mandamus, and Section 13 of the Judiciary Act of 1789 mean this case. A bank and a state tax mean _McCulloch_; steamboats and interstate commerce mean _Gibbons_. If the question says “this case,” name the case; “this power” or “this principle” wants judicial review.",
        "line": "Real answer line: <b><u>Marbury</u></b> v. Madison"
    },
    "tests": {
        "right": [
            "Marbury v. Madison",
            "Marbury versus Madison",
            "Marbury",
            "Marbery v. Madison",
            "Marbury vs Madison"
        ],
        "prompt": [],
        "wrong": [
            "McCulloch v. Maryland",
            "Gibbons v. Ogden",
            "James Madison",
            "John Marshall",
            "Judicial review",
            "Dred Scott v. Sandford",
            "Fletcher v. Peck"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
