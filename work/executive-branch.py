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
    "id": "executive-branch",
    "name": "Executive branch",
    "mono": "EB",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "Branch that carries out the laws · Led by the president under Article II",
    "dates": "Since 1789",
    "briefing": "Congress writes the nation’s laws, but the executive branch carries them out. Article II of the Constitution puts the president in charge of it as commander in chief, with power to veto bills, make treaties with the Senate’s approval, grant pardons, and issue executive orders. The vice president, the 15 departments whose heads make up the Cabinet, and agencies from NASA to the FBI all belong to it.",
    "answerHtml": "<b><u>Executive</u></b> branch (accept the <u>executive</u>; prompt on the <u>president</u> or <u>presidency</u>; do not accept “legislative branch,” “judicial branch,” or “Cabinet”)",
    "accept": [
        "executive branch",
        "the executive branch",
        "executive",
        "the executive",
        "executive branch of government",
        "executive branch of the government",
        "executive branch of the united states",
        "executive branch of the federal government",
        "federal executive branch",
        "us executive branch"
    ],
    "prompt": [
        "president",
        "the president",
        "presidency",
        "the presidency",
        "office of the president",
        "executive departments",
        "executive department"
    ],
    "reject": [
        "legislative branch",
        "the legislative branch",
        "legislative",
        "legislature",
        "judicial branch",
        "the judicial branch",
        "judicial",
        "judiciary",
        "cabinet",
        "the cabinet",
        "presidents cabinet",
        "cabinet of the united states",
        "us cabinet",
        "executive order",
        "executive orders",
        "executive privilege",
        "executive agreement",
        "executive agreements",
        "executive office of the president",
        "eop",
        "executive mansion",
        "congress",
        "senate",
        "house of representatives",
        "supreme court",
        "vice president",
        "article ii",
        "article 2",
        "article two",
        "checks and balances",
        "separation of powers",
        "veto"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Federal_government_of_the_United_States#Executive_branch",
    "qb": {
        "q": "executive branch",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        T("In _Federalist_ No. 70, Alexander Hamilton argued that “energy” in this branch is “a leading character in the definition of good government.” He added that this branch works best when one person leads it, a quality he called “unity.”",
          "Article II of the Constitution created this branch. For 10 points, name this branch of government headed by the president."),
        T("A 1937 report by the Brownlow Committee declared that “the President needs help.” Two years later, Franklin Roosevelt created a new office of advisers for the leader of this branch, including the Bureau of the Budget.",
          "That bureau later became the Office of Management and Budget. For 10 points, name this branch of government that carries out the laws."),
        T("In _United States v. Nixon_, the Supreme Court ruled that a special privilege claimed by this branch could not be used to withhold the Watergate tapes from a criminal trial. That privilege lets officials of this branch keep some of their private advice secret.",
          "Richard Nixon resigned as its leader soon after that 1974 ruling. For 10 points, name this branch of government headed by the president."),
        T("In _Youngstown Sheet & Tube Co. v. Sawyer_, the Supreme Court ruled that the head of this branch could not seize the nation’s steel mills without approval from Congress. Justice Robert Jackson’s opinion in that 1952 case explained when the powers of this branch are strongest and weakest.",
          "The steel seizure was ordered by Harry Truman. For 10 points, name this branch of government led by the president."),
        T("In 1948, Harry Truman ended segregation in the armed forces with a numbered order, the kind of directive the head of this branch can issue without a vote of Congress. Franklin Roosevelt’s 1942 order of that kind led to the forced removal of Japanese Americans to incarceration camps.",
          "This branch carries out the laws that Congress passes. For 10 points, name this branch led by the president."),
        T("After a disappointed office seeker assassinated President James Garfield, the Pendleton Act of 1883 required that many jobs in this branch be filled through merit exams instead of being handed out as political rewards. That law weakened the “spoils system” associated with Andrew Jackson.",
          "For 10 points, name this branch of the U.S. government, which includes the president and the federal departments."),
        T("Passed over Richard Nixon’s veto in 1973, the War Powers Resolution requires the head of this branch to notify Congress within 48 hours of sending troops into combat, and it limits how long those troops can stay without Congress’s approval.",
          "The head of this branch is commander in chief of the armed forces. For 10 points, name this branch of government."),
        T("In _Clinton v. City of New York_, the Supreme Court struck down a 1996 law that let the head of this branch cancel individual spending items in a bill after signing it. The Court ruled that this line-item veto broke the Constitution’s rules for how bills become laws.",
          "For 10 points, name this branch of government whose leader can veto bills passed by Congress."),
        T("The Constitution gives the head of this branch the power to grant “Reprieves and Pardons” for federal crimes, except in cases of impeachment. In 1974, Gerald Ford used that power to pardon Richard Nixon for any federal crimes he might have committed as president.",
          "Ford had taken over this branch’s top job when Nixon resigned. For 10 points, name this branch of government that carries out the laws."),
        T("The Articles of Confederation created no separate branch of this kind, so the national government had no one to carry out its laws. At the Constitutional Convention, delegates argued over whether this branch should be led by one person or by a council of several people.",
          "They chose one person, the president. For 10 points, name this branch created by Article II."),
        T("In _The Spirit of the Laws_, Montesquieu [“MON-tes-kyoo”] warned that liberty is lost if the power of this branch is joined with the power to make laws or the power to judge. The framers of the Constitution borrowed that idea, the separation of powers.",
          "For 10 points, name this branch of government, which enforces the laws and is led by the president."),
        T("Historian Arthur Schlesinger Jr. warned in a 1973 book that the leader of this branch had gained so much power, especially over war, that the office had become an “imperial presidency.” Schlesinger had earlier worked as a special assistant in John F. Kennedy’s White House.",
          "For 10 points, name this branch of government created by Article II of the Constitution."),
        T("If the head of this branch holds a bill unsigned for ten days while Congress has adjourned, the bill dies in a “pocket veto.” Congress can override a regular veto from the head of this branch by a two-thirds vote in both houses.",
          "For 10 points, name this branch of government, which shares power with the legislative and judicial branches."),
        T("The Constitution says that the leader of this branch must be a natural-born citizen, at least 35 years old, and a resident of the United States for at least 14 years. That leader swears to “preserve, protect and defend the Constitution of the United States.”",
          "The vice president also belongs to this branch. For 10 points, name this branch of government led by the president."),
        T("The newest of the 15 departments in this branch, the Department of Homeland Security, was created in 2002 after the September 11 attacks. Its oldest departments, including State and Treasury, date from 1789.",
          "The heads of those departments make up most of the Cabinet. For 10 points, name this branch of the U.S. government, whose leader is the president.")
    ],
    "clues": [
        C("carries-out-laws", "giveaway", "The branch of government that carries out (enforces) the laws; Congress makes them and the courts interpret them", ["carries out", "enforces", "laws"]),
        C("article-ii", "giveaway", "Created by Article II of the Constitution", ["article ii", "article 2"]),
        C("president", "giveaway", "Headed by the president; also includes the vice president, the Cabinet, and federal agencies", ["president", "vice president", "cabinet"], "Cabinet of the United States"),
        C("commander-veto", "giveaway", "Its leader is commander in chief of the armed forces and can veto bills passed by Congress", ["commander in chief", "veto"], "Veto"),
        C("orders", "middle", "Its leader can issue numbered orders with the force of law, like Truman’s 1948 order ending segregation in the armed forces", ["orders", "force of law", "segregation"]),
        C("departments", "middle", "Has 15 departments, from State and Treasury to Homeland Security (2002); their heads make up most of the Cabinet", ["15 departments", "homeland security", "departments"], "Department of Homeland Security"),
        C("treaties-appointments", "middle", "Treaties need approval by two-thirds of the Senate; top appointments, like Supreme Court justices, need Senate approval too", ["treaties", "two-thirds", "appointments"]),
        C("pardons", "middle", "Pardon power: Gerald Ford pardoned Richard Nixon in 1974", ["pardon", "pardoned", "gerald ford"]),
        C("qualifications", "middle", "Its leader must be a natural-born citizen, at least 35 years old, and a U.S. resident for 14 years", ["natural-born", "35 years", "14 years"]),
        C("checks", "middle", "Checks and balances: Congress can override a veto with a two-thirds vote in both houses and can impeach officials", ["override", "impeach", "checks and balances"], "Checks and balances"),
        C("pocket-veto", "middle", "Pocket veto: a bill dies if it goes unsigned for ten days while Congress has adjourned", ["pocket veto", "ten days"]),
        C("agencies", "middle", "Independent agencies such as NASA (1958) and the EPA (1970) belong to it", ["agencies", "nasa", "epa"]),
        C("advisers-1939", "middle", "In 1939, Franklin Roosevelt created a new office of advisers for the president, which holds the White House staff and the budget office", ["1939", "advisers", "white house"]),
        C("federalist-70", "power", "_Federalist_ No. 70: Alexander Hamilton praised “energy” and “unity” (one leader, not a council)", ["federalist", "energy", "unity", "hamilton"], "The Federalist Papers"),
        C("brownlow", "power", "Brownlow Committee (1937): “the President needs help”; its Bureau of the Budget later became the Office of Management and Budget", ["brownlow", "needs help", "bureau of the budget"]),
        C("us-v-nixon", "power", "_United States v. Nixon_ (1974): its claimed privilege could not keep the Watergate tapes from a criminal trial", ["united states v. nixon", "privilege", "watergate"], "Watergate scandal"),
        C("youngstown", "power", "_Youngstown Sheet & Tube Co. v. Sawyer_ (1952): Truman could not seize the steel mills; Justice Robert Jackson wrote a famous opinion", ["youngstown", "steel mills", "robert jackson"]),
        C("war-powers", "power", "War Powers Resolution (1973), passed over Nixon’s veto: Congress must be told within 48 hours when troops go into combat", ["war powers", "48 hours"]),
        C("line-item", "power", "_Clinton v. City of New York_ (1998) struck down the Line Item Veto Act of 1996", ["line item veto", "clinton v. city of new york"]),
        C("pendleton", "power", "Pendleton Act (1883): many of its jobs must be filled through merit exams, after Garfield was killed by a disappointed office seeker", ["pendleton", "merit", "garfield"]),
        C("hatch", "power", "Hatch Act (1939), named for Senator Carl Hatch of New Mexico: limits political campaigning by most of its employees", ["hatch act", "carl hatch", "campaigning"]),
        C("imperial", "power", "Historian Arthur Schlesinger Jr. warned of an “imperial presidency” (1973)", ["imperial presidency", "schlesinger"]),
        C("montesquieu", "power", "Montesquieu’s _The Spirit of the Laws_ (1748) warned against joining the powers to make laws, to enforce them, and to judge", ["montesquieu", "spirit of the laws"]),
        C("articles", "power", "The Articles of Confederation had no separate branch like it; Convention delegates debated one leader versus a council", ["articles of confederation", "council"], "Articles of Confederation"),
        C("oath", "power", "Its leader’s oath promises to “preserve, protect and defend the Constitution of the United States”", ["preserve, protect and defend", "oath"]),
        C("order-1942", "power", "Franklin Roosevelt’s 1942 order led to the forced removal of Japanese Americans to incarceration camps", ["japanese americans", "1942", "incarceration"])
    ],
    "trap": {
        "title": "Branch, group, or office?",
        "body": "Several answer lines live inside this branch: the president, the vice president, the Cabinet, the Executive Office of the President (created in 1939), and single departments such as State or Defense. If a question asks for “this branch,” say “executive branch,” but if it asks for “this group of advisers,” the answer is the Cabinet. Executive orders, vetoes, and executive privilege are powers of this branch, not the branch itself.",
        "fix": "Count the articles: Article I is the legislative branch (Congress makes the laws), Article II is the executive branch (the president carries them out), and Article III is the judicial branch (the courts interpret them). Saying only “the president” may earn a prompt, so add “executive branch.”",
        "line": "Real answer line: <b><u>Executive</u></b> branch (accept the <u>executive</u>; prompt on the <u>president</u> or <u>presidency</u>; do not accept “legislative branch,” “judicial branch,” or “Cabinet”)"
    },
    "tests": {
        "right": [
            "Executive branch",
            "executive",
            "the executive branch",
            "Excecutive branch",
            "executive branch of government"
        ],
        "prompt": [
            "President",
            "the presidency"
        ],
        "wrong": [
            "Legislative branch",
            "Judicial branch",
            "Cabinet",
            "Executive order",
            "Congress",
            "Executive Office of the President"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
