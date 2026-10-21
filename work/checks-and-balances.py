import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TIP = "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."

data = {
    "id": "checks-and-balances",
    "name": "Checks and balances",
    "mono": "CB",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "Each branch can limit the other two · Built into the U.S. Constitution",
    "dates": "Written into the Constitution, 1787",
    "briefing": "What keeps a president from acting like a king? The Constitution splits power among three branches and then gives each one ways to rein in the other two. The president can veto bills, Congress can override vetoes and impeach officials, and the courts can strike down laws. James Madison explained this system of checks and balances in _Federalist_ No. 51: “Ambition must be made to counteract ambition.”",
    "answerHtml": "<b><u>checks and balances</u></b> (accept <u>system of checks and balances</u>; prompt on <u>separation of powers</u>; do not accept “federalism”)",
    "accept": [
        "checks and balances",
        "the checks and balances",
        "check and balances",
        "checks and balance",
        "check and balance",
        "checks balances",
        "system of checks and balances",
        "a system of checks and balances",
        "the system of checks and balances",
        "checks and balances system",
        "principle of checks and balances",
        "checks and balances principle"
    ],
    "prompt": [
        "separation of powers",
        "the separation of powers",
        "separation of power",
        "separated powers"
    ],
    "reject": [
        "federalism",
        "federal system",
        "dual federalism",
        "balance of power",
        "balance of powers",
        "separation of church and state",
        "judicial review",
        "veto",
        "veto override",
        "impeachment",
        "advice and consent",
        "executive privilege",
        "power of the purse",
        "popular sovereignty",
        "limited government",
        "rule of law",
        "republicanism",
        "bill of rights",
        "the federalist papers",
        "federalist papers",
        "the spirit of the laws",
        "spirit of the laws",
        "montesquieu",
        "marbury v madison",
        "executive branch",
        "legislative branch",
        "judicial branch"
    ],
    "tests": {
        "right": [
            "checks and balances",
            "Checks & Balances",
            "system of checks and balances",
            "checks and balences",
            "check and balance"
        ],
        "prompt": [
            "separation of powers",
            "Separation of Power"
        ],
        "wrong": [
            "federalism",
            "judicial review",
            "veto",
            "balance of power",
            "impeachment",
            "Bill of Rights",
            "executive branch"
        ]
    },
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Checks_and_balances",
    "qb": {
        "q": "checks and balances",
        "found": 0,
        "tip": TIP
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "In a 1748 book, the French writer Montesquieu [“MON-tes-kyoo”] warned that liberty is lost when one person or group holds the powers to make the laws, to carry them out, and to judge. He praised the government of Great Britain for dividing power so that each part could restrain the others.",
            "r": "That book was _The Spirit of the Laws_. For 10 points, name this system, built into the U.S. Constitution, that lets each branch of government limit the other two."
        },
        {
            "p": "One essay argued that “ambition must be made to counteract ambition” and that each branch of government needs the “personal motives to resist” the others. The same essay, _Federalist_ No. 51, famously says that “if men were angels, no government would be necessary.”",
            "r": "Its author, James Madison, was explaining this idea. For 10 points, name this system in which each branch of government can limit the powers of the others."
        },
        {
            "p": "In 1845, John Tyler became the first president to have Congress overturn one of his rejections of a bill, on a bill about ships called revenue cutters. Two decades later, Congress overturned Andrew Johnson’s rejection of the Civil Rights Act of 1866, the first major law ever passed that way.",
            "r": "Overriding a veto takes two-thirds of each house. For 10 points, name this system that lets each branch of government limit the other two."
        },
        {
            "p": "In an 1803 case brought by William Marbury against James Madison, Chief Justice John Marshall declared that it is “emphatically the province and duty of the judicial department to say what the law is.” That decision gave the courts a powerful new tool under this principle.",
            "r": "That tool, judicial review, lets courts strike down laws that break the Constitution. For 10 points, name this system in which each branch of government can limit the others."
        },
        {
            "p": "In 1987, the Senate voted 58 to 42 against Robert Bork, Ronald Reagan’s nominee for the Supreme Court. That vote showed this principle at work, because the Constitution requires the Senate’s “advice and consent” before judges and other top officials can take office.",
            "r": "For 10 points, name this system that keeps any one branch of government from becoming too powerful."
        },
        {
            "p": "Senator Henry Cabot Lodge led the opposition that kept the Senate from approving the Treaty of Versailles, which Woodrow Wilson had helped write after World War I. That defeat showed this principle at work, since a treaty needs the votes of two-thirds of the senators present.",
            "r": "For 10 points, name this system that lets each branch of the U.S. government limit the powers of the others."
        },
        {
            "p": "Chief Justice Salmon Chase presided in 1868 when the Senate fell one vote short of the two-thirds it needed to remove President Andrew Johnson from office. Johnson had angered Congress by trying to fire his Secretary of War, Edwin Stanton.",
            "r": "The power to impeach and remove officials is one tool of this principle. For 10 points, name this system in which each branch of government can limit the others."
        },
        {
            "p": "After the Supreme Court struck down several New Deal laws, Franklin Roosevelt proposed in 1937 to add up to six new justices, but Congress refused to pass his plan. Critics said that “court-packing” scheme threatened the independence of the courts and this principle.",
            "r": "The president’s veto is another part of this idea. For 10 points, name this system that lets each branch of government limit the other two."
        },
        {
            "p": "In 1974, the Supreme Court ruled 8–0 that Richard Nixon had to hand over his secret Watergate tapes, rejecting his claim of executive privilege. That decision in _United States v. Nixon_ showed the courts using this principle to limit the president.",
            "r": "Nixon resigned about two weeks later. For 10 points, name this system in which each branch of government can limit the powers of the others."
        },
        {
            "p": "The Greek historian Polybius [“puh-LIB-ee-us”] praised the government of the Roman Republic because its consuls, its Senate, and its popular assemblies could each hold back the others. Many centuries later, the framers of the U.S. Constitution built a version of that idea into their plan.",
            "r": "For 10 points, name this system, which includes the president’s veto and the courts’ power to strike down laws."
        },
        {
            "p": "The Eleventh Amendment, ratified in 1795, reversed the Supreme Court’s ruling in _Chisholm v. Georgia_ [“CHIZ-um”], and the Sixteenth Amendment allowed a federal income tax after the Court had struck one down in 1895. Those amendments show how Congress and the states can overrule the courts under this principle.",
            "r": "For 10 points, name this system in which the branches of government can limit one another."
        },
        {
            "p": "Passed over Richard Nixon’s veto in 1973, the War Powers Resolution requires the president to notify Congress within 48 hours of sending troops into combat. Congress’s powers to declare war and to control spending, often called the “power of the purse,” are also tools of this principle.",
            "r": "For 10 points, name this system that keeps any one branch of government from growing too strong."
        },
        {
            "p": "In _Youngstown Sheet & Tube Co. v. Sawyer_, the Supreme Court ruled in 1952 that Harry Truman could not take over the nation’s steel mills during the Korean War without approval from Congress. That decision is a famous example of this principle limiting a president.",
            "r": "For 10 points, name this system in which each branch of government can limit the powers of the other two."
        },
        {
            "p": "John Adams’s 1776 pamphlet _Thoughts on Government_ urged Americans writing new state constitutions to create a two-house legislature, a separate executive, and independent judges, so that each part could restrain the others. About a decade later, the framers of the Constitution built that design into the national government.",
            "r": "For 10 points, name this system, under which the president can veto bills and Congress can override vetoes."
        },
        {
            "p": "In 1989, the Senate voted 53 to 47 to reject John Tower, George H. W. Bush’s choice to be Secretary of Defense. The Constitution requires the Senate to approve Cabinet members, ambassadors, and federal judges, which is one way this principle limits a president.",
            "r": "For 10 points, name this system that lets each branch of government limit the others."
        }
    ],
    "clues": [
        {
            "id": "definition",
            "tier": "giveaway",
            "t": "The system that lets each branch of government limit the powers of the other two, so that no branch grows too strong",
            "k": ["each branch", "limit", "too strong", "other two"],
            "n": 0
        },
        {
            "id": "veto-override",
            "tier": "giveaway",
            "t": "The president can veto bills; Congress can override a veto with a two-thirds vote in both houses",
            "k": ["veto", "override", "two-thirds"],
            "n": 0,
            "rabbit": "Veto"
        },
        {
            "id": "judicial-review",
            "tier": "giveaway",
            "t": "Judicial review: courts can strike down laws that break the Constitution",
            "k": ["judicial review", "strike down", "courts"],
            "n": 0
        },
        {
            "id": "impeachment",
            "tier": "giveaway",
            "t": "The House can impeach officials, and the Senate can remove them with a two-thirds vote",
            "k": ["impeach", "remove", "senate"],
            "n": 0,
            "rabbit": "Impeachment"
        },
        {
            "id": "three-branches",
            "tier": "giveaway",
            "t": "Works together with the separation of powers among the legislative, executive, and judicial branches (Articles I, II, and III)",
            "k": ["separation of powers", "legislative", "executive", "judicial"],
            "n": 0,
            "rabbit": "Executive branch"
        },
        {
            "id": "federalist-51",
            "tier": "middle",
            "t": "_Federalist_ No. 51 (James Madison): “Ambition must be made to counteract ambition”; “If men were angels, no government would be necessary”",
            "k": ["federalist", "ambition", "angels", "madison"],
            "n": 0,
            "rabbit": "The Federalist Papers"
        },
        {
            "id": "montesquieu",
            "tier": "middle",
            "t": "Montesquieu’s _The Spirit of the Laws_ (1748) warned against letting one person or group make, enforce, and judge the laws",
            "k": ["montesquieu", "spirit of the laws", "1748"],
            "n": 0
        },
        {
            "id": "marbury",
            "tier": "middle",
            "t": "_Marbury v. Madison_ (1803): John Marshall said it is the courts’ duty “to say what the law is”",
            "k": ["marbury", "marshall", "1803", "say what the law is"],
            "n": 0,
            "rabbit": "Marbury v. Madison"
        },
        {
            "id": "advice-consent",
            "tier": "middle",
            "t": "“Advice and consent”: the Senate must approve federal judges, Cabinet members, and ambassadors",
            "k": ["advice and consent", "approve", "cabinet"],
            "n": 0
        },
        {
            "id": "treaties",
            "tier": "middle",
            "t": "Treaties need the votes of two-thirds of the senators present; the Senate refused to approve the Treaty of Versailles (1919–1920)",
            "k": ["treaties", "versailles", "senators present"],
            "n": 0,
            "rabbit": "Treaty of Versailles"
        },
        {
            "id": "nixon-tapes",
            "tier": "middle",
            "t": "_United States v. Nixon_ (1974): the Supreme Court ruled 8–0 that Nixon had to hand over the Watergate tapes, rejecting executive privilege",
            "k": ["watergate", "tapes", "executive privilege"],
            "n": 0
        },
        {
            "id": "court-packing",
            "tier": "middle",
            "t": "Franklin Roosevelt’s 1937 “court-packing” plan to add up to six justices failed in Congress",
            "k": ["court-packing", "roosevelt", "six justices"],
            "n": 0
        },
        {
            "id": "purse",
            "tier": "middle",
            "t": "Congress controls spending (the “power of the purse”) and has the power to declare war",
            "k": ["power of the purse", "spending", "declare war"],
            "n": 0
        },
        {
            "id": "johnson-trial",
            "tier": "middle",
            "t": "In 1868, the Senate fell one vote short of removing Andrew Johnson; the Chief Justice presides when a president is tried",
            "k": ["andrew johnson", "one vote", "chief justice"],
            "n": 0
        },
        {
            "id": "polybius",
            "tier": "power",
            "t": "The Greek historian Polybius praised the Roman Republic, whose consuls, Senate, and assemblies could each hold back the others",
            "k": ["polybius", "roman republic", "consuls"],
            "n": 0
        },
        {
            "id": "britain",
            "tier": "power",
            "t": "Montesquieu admired Great Britain’s government for dividing power so each part could restrain the others; _Federalist_ No. 47 calls him “the oracle”",
            "k": ["britain", "oracle", "restrain"],
            "n": 0
        },
        {
            "id": "first-override",
            "tier": "power",
            "t": "Congress first overrode a veto in 1845, against John Tyler, on a bill about revenue cutters",
            "k": ["1845", "tyler", "revenue cutters"],
            "n": 0
        },
        {
            "id": "civil-rights-1866",
            "tier": "power",
            "t": "The Civil Rights Act of 1866 was the first major law passed over a veto; Congress overrode Andrew Johnson a record 15 times",
            "k": ["civil rights act", "1866", "15 times"],
            "n": 0
        },
        {
            "id": "bork",
            "tier": "power",
            "t": "In 1987, the Senate rejected Robert Bork, Ronald Reagan’s Supreme Court nominee, by a vote of 58 to 42",
            "k": ["bork", "58 to 42", "reagan"],
            "n": 0
        },
        {
            "id": "tower",
            "tier": "power",
            "t": "In 1989, the Senate rejected John Tower, George H. W. Bush’s choice for Secretary of Defense, by 53 to 47",
            "k": ["tower", "secretary of defense", "1989"],
            "n": 0
        },
        {
            "id": "lodge",
            "tier": "power",
            "t": "Senator Henry Cabot Lodge led the opposition to Woodrow Wilson’s Treaty of Versailles",
            "k": ["lodge", "henry cabot lodge", "wilson"],
            "n": 0
        },
        {
            "id": "youngstown",
            "tier": "power",
            "t": "_Youngstown Sheet & Tube Co. v. Sawyer_ (1952): Truman could not seize the steel mills during the Korean War without Congress’s approval",
            "k": ["youngstown", "steel mills", "truman"],
            "n": 0
        },
        {
            "id": "war-powers",
            "tier": "power",
            "t": "War Powers Resolution (1973), passed over Nixon’s veto: Congress must be told within 48 hours when troops go into combat",
            "k": ["war powers", "48 hours", "1973"],
            "n": 0
        },
        {
            "id": "amendments",
            "tier": "power",
            "t": "Amendments can reverse court rulings: the 11th Amendment (1795) reversed _Chisholm v. Georgia_; the 16th allowed an income tax after an 1895 ruling",
            "k": ["11th amendment", "chisholm", "income tax"],
            "n": 0
        },
        {
            "id": "thoughts-on-government",
            "tier": "power",
            "t": "John Adams’s _Thoughts on Government_ (1776) called for a two-house legislature, a separate executive, and independent judges",
            "k": ["thoughts on government", "john adams", "1776"],
            "n": 0,
            "rabbit": "John Adams"
        },
        {
            "id": "stanton",
            "tier": "power",
            "t": "Andrew Johnson was impeached after trying to fire Secretary of War Edwin Stanton; Chief Justice Salmon Chase presided at his trial",
            "k": ["stanton", "salmon chase", "secretary of war"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Checks or separation?",
        "body": "Two answer lines share almost every clue. The separation of powers means dividing the government into three branches with different jobs; checks and balances means giving each branch tools to limit the others, like the veto, the override, impeachment, and judicial review. Saying “separation of powers” may earn only a prompt, and “federalism,” which divides power between the national and state governments, is wrong.",
        "fix": "If the clue shows one branch blocking, overruling, or approving another, say “checks and balances.” If it is only about splitting jobs among branches, think separation of powers; if it is about the states versus the national government, think federalism.",
        "line": "Real answer line: <b><u>checks and balances</u></b> (prompt on <u>separation of powers</u>; do not accept “federalism”)"
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("wrote", data["id"])
