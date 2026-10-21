import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TIP = "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."

data = {
    "id": "dont-ask-dont-tell",
    "name": "Don’t Ask, Don’t Tell",
    "mono": "DT",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "Military policy on gay service members · In force from 1994 to 2011",
    "dates": "Adopted 1993; ended September 20, 2011",
    "briefing": "For decades, the U.S. military did not allow gay people to serve. In 1993, President Bill Clinton and Congress settled on a compromise called Don’t Ask, Don’t Tell: officials were not to ask service members about their sexual orientation, and gay, lesbian, and bisexual troops could serve only if they kept it private. Barack Obama signed a law repealing the policy in 2010, and it officially ended on September 20, 2011.",
    "answerHtml": "<b><u>Don’t Ask, Don’t Tell</u></b> (or <u>DADT</u>; prompt on <u>Don’t Ask</u>; do not accept “Don’t Ask, Don’t Tell Repeal Act”)",
    "accept": [
        "dont ask dont tell",
        "dont ask dont tell policy",
        "the dont ask dont tell policy",
        "do not ask do not tell",
        "dont ask and dont tell",
        "dadt",
        "d a d t"
    ],
    "prompt": [
        "dont ask",
        "dont tell"
    ],
    "reject": [
        "dont ask dont tell repeal act",
        "dont ask dont tell repeal act of 2010",
        "repeal of dont ask dont tell",
        "defense of marriage act",
        "doma",
        "same sex marriage",
        "obergefell v hodges",
        "lawrence v texas",
        "stonewall riots",
        "stonewall",
        "military draft",
        "selective service",
        "uniform code of military justice",
        "ucmj",
        "national defense authorization act",
        "military readiness enhancement act",
        "equal rights amendment",
        "title ix",
        "affirmative action"
    ],
    "tests": {
        "right": [
            "Don't Ask, Don't Tell",
            "Don’t Ask Don’t Tell",
            "DADT",
            "dont ask dont tell policy",
            "Do not ask, do not tell",
            "Dont Ask Dont Tel"
        ],
        "prompt": [
            "Don't Ask"
        ],
        "wrong": [
            "Don't Ask, Don't Tell Repeal Act",
            "Defense of Marriage Act",
            "DOMA",
            "same-sex marriage",
            "military draft",
            "Obergefell v. Hodges",
            "Stonewall riots"
        ]
    },
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Don%27t_ask,_don%27t_tell",
    "qb": {
        "q": "Don't Ask, Don't Tell",
        "found": 0,
        "tip": TIP
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "The Northwestern University sociologist Charles Moskos is often credited with designing this policy, which took effect in 1994. It replaced a 1982 Defense Department rule that barred gay people from serving in the armed forces at all.",
            "r": "Under this policy, gay, lesbian, and bisexual troops could serve only if they kept their sexual orientation private. For 10 points, name this policy adopted under Bill Clinton."
        },
        {
            "p": "Senator Sam Nunn of Georgia, who chaired the Senate Armed Services Committee, and General Colin Powell, the chairman of the Joint Chiefs of Staff, opposed a new president’s plan to let gay Americans serve openly in the military. This policy was the compromise that followed.",
            "r": "For 10 points, name this 1993 policy, under which gay service members could serve if they did not reveal their sexual orientation."
        },
        {
            "p": "In 2010, federal judge Virginia Phillips ruled in a lawsuit brought by the Log Cabin Republicans that this policy was unconstitutional, and she ordered the military to stop enforcing it. An appeals court soon put her order on hold.",
            "r": "Congress repealed this policy later that year. For 10 points, name this policy on gay, lesbian, and bisexual service members, adopted in 1993."
        },
        {
            "p": "In November 2010, a Pentagon study led by Jeh Johnson and General Carter Ham reported on surveys of service members and their families about this policy. The study concluded that ending this policy posed a low risk to the military’s effectiveness.",
            "r": "Weeks later, Barack Obama signed a law repealing it. For 10 points, name this 1993 policy on gay service members."
        },
        {
            "p": "In July 2011, the president, Defense Secretary Leon Panetta, and Admiral Mike Mullen certified that the armed forces were ready for this policy to end. Sixty days later, on September 20, 2011, it officially ended.",
            "r": "For 10 points, name this policy, adopted under Bill Clinton, that let gay service members serve only if they kept their sexual orientation private."
        },
        {
            "p": "Senators Joe Lieberman of Connecticut and Susan Collins of Maine led a December 2010 push to end this policy, and the Senate approved its repeal by a vote of 65 to 31. Four days later, the repeal was signed into law.",
            "r": "Barack Obama signed that repeal. For 10 points, name this policy on gay service members that began under Bill Clinton."
        },
        {
            "p": "By most estimates, more than 13,000 service members were discharged under this policy during the roughly 17 years it was in force. Those discharged included some who worked as Arabic translators.",
            "r": "For 10 points, name this policy, adopted in 1993, that barred gay, lesbian, and bisexual troops from serving openly."
        },
        {
            "p": "In February 2010, Admiral Mike Mullen, the chairman of the Joint Chiefs of Staff, told Congress that he personally supported ending this policy, while some other military leaders urged Congress to wait for a Pentagon study first.",
            "r": "Congress repealed this policy that December. For 10 points, name this 1993 policy on gay, lesbian, and bisexual service members."
        },
        {
            "p": "During his 1992 campaign, a future president promised to end the military’s ban on gay service members, but after months of fierce debate in 1993, he accepted this policy as a compromise instead.",
            "r": "That president was Bill Clinton. For 10 points, name this policy, under which gay troops could serve only if they did not reveal their sexual orientation."
        },
        {
            "p": "Because this policy was written into a federal law in 1993, ending it took a new act of Congress rather than just an order from the president. That 1993 law also authorized the Defense Department’s spending for the coming year.",
            "r": "For 10 points, name this policy, which kept gay service members from serving openly until 2011."
        },
        {
            "p": "In his January 2010 State of the Union address, the president promised to work with Congress that year to end this policy. Soon afterward, Defense Secretary Robert Gates ordered a study of how the military could carry out that change.",
            "r": "That president, Barack Obama, signed the repeal in December 2010. For 10 points, name this policy adopted under Bill Clinton."
        },
        {
            "p": "Pennsylvania congressman Patrick Murphy, an Iraq War veteran, led the effort in the House of Representatives to end this policy. In December 2010, the House passed a repeal bill by a vote of 250 to 175.",
            "r": "For 10 points, name this policy on gay, lesbian, and bisexual service members that took effect in 1994."
        },
        {
            "p": "Senate Majority Leader Harry Reid helped pass the 2010 law ending this policy. That same year, Reid also helped pass the Dodd–Frank law, which set new rules for banks after the 2008 financial crisis.",
            "r": "For 10 points, name this policy, adopted in 1993, that let gay service members serve only if they kept their sexual orientation private."
        },
        {
            "p": "Defense Secretary Les Aspin, a former congressman from Wisconsin, issued the first guidelines for this policy in July 1993, after months of hearings in Congress about who could serve in the military.",
            "r": "Bill Clinton had announced the policy that month. For 10 points, name this policy, under which gay service members could serve only if they did not reveal their sexual orientation."
        },
        {
            "p": "Massachusetts congressman Marty Meehan introduced the Military Readiness Enhancement Act in 2005 to end this policy, but that bill did not pass. Five years later, a different repeal effort succeeded.",
            "r": "Congress ended this policy in 2010. For 10 points, name this 1993 policy on gay, lesbian, and bisexual service members."
        }
    ],
    "clues": [
        {
            "id": "what-it-required",
            "tier": "giveaway",
            "t": "Military policy: officials were not to question service members about their sexual orientation, and gay, lesbian, and bisexual troops could serve only if they did not reveal it",
            "k": ["sexual orientation", "military", "reveal"],
            "n": 0
        },
        {
            "id": "clinton-1993",
            "tier": "giveaway",
            "t": "Adopted under President Bill Clinton in 1993; took effect in 1994",
            "k": ["bill clinton", "clinton", "1993"],
            "n": 0,
            "rabbit": "Bill Clinton"
        },
        {
            "id": "obama-repeal",
            "tier": "giveaway",
            "t": "Repealed by a law Barack Obama signed on December 22, 2010",
            "k": ["barack obama", "obama", "december 22, 2010"],
            "n": 0,
            "rabbit": "Barack Obama"
        },
        {
            "id": "ended-2011",
            "tier": "middle",
            "t": "Officially ended on September 20, 2011; after that, gay, lesbian, and bisexual Americans could serve openly",
            "k": ["september 20, 2011", "serve openly", "2011"],
            "n": 0
        },
        {
            "id": "nunn-powell",
            "tier": "middle",
            "t": "Senator Sam Nunn and General Colin Powell opposed letting gay Americans serve openly in 1993; this policy was the compromise",
            "k": ["sam nunn", "colin powell", "compromise"],
            "n": 0
        },
        {
            "id": "campaign-1992",
            "tier": "middle",
            "t": "Clinton had promised in his 1992 campaign to end the military’s ban on gay service members",
            "k": ["1992", "campaign", "ban"],
            "n": 0
        },
        {
            "id": "discharges",
            "tier": "middle",
            "t": "By most estimates, more than 13,000 service members were discharged under it",
            "k": ["13,000", "discharged"],
            "n": 0
        },
        {
            "id": "federal-law",
            "tier": "middle",
            "t": "It was written into federal law in 1993, so ending it took an act of Congress, not just a presidential order",
            "k": ["federal law", "act of congress"],
            "n": 0
        },
        {
            "id": "mullen",
            "tier": "middle",
            "t": "Admiral Mike Mullen, chairman of the Joint Chiefs, told Congress in 2010 that he supported ending it; other leaders urged waiting for a study",
            "k": ["mike mullen", "mullen", "joint chiefs"],
            "n": 0
        },
        {
            "id": "certification",
            "tier": "middle",
            "t": "The repeal took effect only after the president, the defense secretary, and the Joint Chiefs chairman certified readiness, plus 60 days",
            "k": ["certified", "60 days", "readiness"],
            "n": 0
        },
        {
            "id": "moskos",
            "tier": "power",
            "t": "Sociologist Charles Moskos of Northwestern University is often credited with designing it",
            "k": ["charles moskos", "moskos", "northwestern"],
            "n": 0
        },
        {
            "id": "rule-1982",
            "tier": "power",
            "t": "It replaced a 1982 Defense Department rule that barred gay people from serving at all",
            "k": ["1982", "defense department"],
            "n": 0
        },
        {
            "id": "log-cabin",
            "tier": "power",
            "t": "In 2010, Judge Virginia Phillips ruled it unconstitutional in a suit by the Log Cabin Republicans; an appeals court put her order on hold",
            "k": ["log cabin republicans", "virginia phillips", "unconstitutional"],
            "n": 0
        },
        {
            "id": "pentagon-study",
            "tier": "power",
            "t": "A November 2010 Pentagon study led by Jeh Johnson and General Carter Ham found that ending it posed a low risk to the military",
            "k": ["jeh johnson", "carter ham", "low risk"],
            "n": 0
        },
        {
            "id": "panetta",
            "tier": "power",
            "t": "In July 2011, Obama, Defense Secretary Leon Panetta, and Admiral Mike Mullen certified that the military was ready",
            "k": ["leon panetta", "panetta", "july 2011"],
            "n": 0
        },
        {
            "id": "senate-vote",
            "tier": "power",
            "t": "Senators Joe Lieberman and Susan Collins led the repeal push; the Senate voted 65 to 31 in December 2010",
            "k": ["lieberman", "susan collins", "65 to 31"],
            "n": 0
        },
        {
            "id": "house-vote",
            "tier": "power",
            "t": "Congressman Patrick Murphy, an Iraq War veteran, led the House effort; the House voted 250 to 175",
            "k": ["patrick murphy", "250 to 175", "iraq war"],
            "n": 0
        },
        {
            "id": "state-of-union",
            "tier": "power",
            "t": "Obama promised to work to end it in his January 2010 State of the Union address; Robert Gates then ordered a study",
            "k": ["state of the union", "robert gates", "january 2010"],
            "n": 0
        },
        {
            "id": "translators",
            "tier": "power",
            "t": "Those discharged under it included some Arabic translators",
            "k": ["arabic", "translators"],
            "n": 0
        },
        {
            "id": "reid",
            "tier": "power",
            "t": "Senate Majority Leader Harry Reid helped pass its repeal, the same year he helped pass the Dodd–Frank law",
            "k": ["harry reid", "reid", "dodd–frank"],
            "n": 0,
            "rabbit": "Harry Reid"
        },
        {
            "id": "aspin",
            "tier": "power",
            "t": "Defense Secretary Les Aspin issued its first guidelines in July 1993",
            "k": ["les aspin", "aspin", "july 1993"],
            "n": 0
        },
        {
            "id": "meehan",
            "tier": "power",
            "t": "Congressman Marty Meehan introduced the Military Readiness Enhancement Act to end it in 2005; it did not pass",
            "k": ["marty meehan", "military readiness enhancement act", "2005"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Policy, not the repeal",
        "body": "This answer line is the 1993 policy itself. The Don’t Ask, Don’t Tell Repeal Act is the 2010 law that ended it, so a question asking for “this law” signed by Barack Obama may want the repeal instead. Players also mix it up with the Defense of Marriage Act, a 1996 law about marriage that Bill Clinton also signed, and with the Supreme Court’s 2015 same-sex marriage case, _Obergefell v. Hodges_.",
        "fix": "If the question asks for “this policy” about who could serve openly in the military, say “Don’t Ask, Don’t Tell.” If it asks for the 2010 law that ended that policy, name the repeal act. Clues about marriage point to the Defense of Marriage Act or _Obergefell_, not this policy.",
        "line": "Real answer line: <b><u>Don’t Ask, Don’t Tell</u></b> (or <u>DADT</u>; do not accept “Don’t Ask, Don’t Tell Repeal Act”)"
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("wrote", data["id"])
