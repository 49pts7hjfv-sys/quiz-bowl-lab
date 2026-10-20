import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "cabinet-of-the-united-states",
    "name": "Cabinet of the United States",
    "mono": "CAB",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "The president’s top advisers · Heads of the executive departments",
    "dates": "Since 1789",
    "briefing": "The Constitution never uses the word “cabinet.” It says only that the president may require the written opinion of the “principal Officer” in each executive department. George Washington’s first cabinet had just four members, including the bitter rivals Thomas Jefferson and Alexander Hamilton. It has since grown to include the heads of 15 departments, from State and Treasury to Homeland Security, which was created in 2002.",
    "answerHtml": "<b><u>Cabinet</u></b> of the United States (accept <u>President’s Cabinet</u> or <u>U.S. Cabinet</u>; prompt on <u>executive departments</u>; do not accept “Executive branch,” “Secretary of State,” or “Kitchen Cabinet”)",
    "accept": [
        "cabinet",
        "the cabinet",
        "cabinet of the united states",
        "us cabinet",
        "united states cabinet",
        "presidents cabinet",
        "the presidents cabinet",
        "presidential cabinet",
        "american cabinet",
        "federal cabinet"
    ],
    "prompt": [
        "executive departments",
        "heads of the executive departments",
        "heads of executive departments",
        "executive department heads",
        "department heads"
    ],
    "reject": [
        "executive branch",
        "the executive branch",
        "secretary of state",
        "kitchen cabinet",
        "jacksons kitchen cabinet",
        "shadow cabinet",
        "brain trust",
        "national security council",
        "executive office of the president",
        "white house staff",
        "joint chiefs of staff",
        "congress",
        "senate",
        "supreme court",
        "department of homeland security",
        "secretary of war",
        "secretary of the treasury",
        "attorney general",
        "vice president",
        "privy council",
        "cabinet of curiosities",
        "cabinet of dr caligari",
        "the cabinet of dr caligari"
    ],
    "mediaPending": True,
    "media": [],
    "wiki": "https://en.wikipedia.org/wiki/Cabinet_of_the_United_States",
    "qb": {
        "q": "Cabinet",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "Each year, one member of this group skips the State of the Union address and waits at a secret location as the “designated survivor.” Members of this group follow the Speaker and the president pro tempore in the line of succession, in the order their departments were created.",
            "r": "For 10 points, name this group of the president’s top advisers, whose highest-ranking member is the Secretary of State."
        },
        {
            "p": "Under Section 4 of the 25th Amendment, the vice president and a majority of this group can declare that the president is unable to do the job. In 1920, Woodrow Wilson forced out his secretary of state, Robert Lansing, for calling meetings of this group while Wilson was ill.",
            "r": "Its members include the secretaries of State, Treasury, and Defense. For 10 points, name this group of top presidential advisers."
        },
        {
            "p": "The Constitution never names this body, but Article II lets the president require the written “Opinion” of the “principal Officer” in each executive department. George Washington started the custom of meeting with those officials as a group.",
            "r": "Most of its members are called secretaries. For 10 points, name this group of the president’s top advisers, who lead departments such as State and Treasury."
        },
        {
            "p": "In 1834, the Senate rejected Roger Taney [“TAW-nee”] as Secretary of the Treasury, the first time it voted down a president’s choice for this group. In 1989, it rejected John Tower’s nomination to join this group as Secretary of Defense.",
            "r": "For 10 points, name this group of presidential advisers, whose members must be confirmed by the Senate."
        },
        {
            "p": "In 1841, every member of this group except Secretary of State Daniel Webster resigned after John Tyler vetoed bills to create a new national bank. A decade earlier, the Petticoat Affair over Peggy Eaton had broken up Andrew Jackson’s first version of this group.",
            "r": "For 10 points, name this group of top advisers, made up mostly of the heads of the executive departments."
        },
        {
            "p": "Critics complained that Andrew Jackson ignored his official advisers in favor of a “Kitchen” version of this group, which included the newspaper editors Amos Kendall and Francis Blair. Jackson also gave the Postmaster General a seat in this group, which lasted until the Post Office was reorganized in 1971.",
            "r": "For 10 points, name this group of the president’s top advisers, which includes the Secretary of State and the Attorney General."
        },
        {
            "p": "In 1953, Oveta Culp Hobby of Houston became the second woman in this group, as the first Secretary of Health, Education, and Welfare. Twenty years earlier, Frances Perkins had become the first woman in this group, serving as Franklin Roosevelt’s Secretary of Labor.",
            "r": "For 10 points, name this group of top presidential advisers who lead the executive departments."
        },
        {
            "p": "In 1966, Robert C. Weaver became the first African American in this group, as the first Secretary of Housing and Urban Development under Lyndon Johnson. In 2001, Colin Powell became the first African American to hold this group’s top-ranking post, Secretary of State.",
            "r": "For 10 points, name this group of the president’s top advisers, whose members lead the executive departments."
        },
        {
            "p": "Edmund Randolph, who presented the Virginia Plan at the Constitutional Convention, served in the first version of this group as Attorney General. Henry Knox, the namesake of Fort Knox, served alongside him as Secretary of War.",
            "r": "Thomas Jefferson and Alexander Hamilton also served in George Washington’s first version of this group. For 10 points, name this group of presidential advisers."
        },
        {
            "p": "Two rap “Battles” in the musical _Hamilton_ show Thomas Jefferson and Alexander Hamilton arguing at meetings of this group over Hamilton’s debt plan and over whether to help France. George Washington asked members of this group for written opinions on whether a national bank was constitutional.",
            "r": "Jefferson served in this group as Secretary of State, and Hamilton as Secretary of the Treasury. For 10 points, name this group of top advisers to the president."
        },
        {
            "p": "The Tenure of Office Act of 1867 required Senate approval before a president could fire certain officials, including members of this group. Andrew Johnson was impeached after he tried to remove one of them, Secretary of War Edwin Stanton, and in 1926 the Supreme Court said that law had been unconstitutional.",
            "r": "Most of its members are called secretaries. For 10 points, name this group of presidential advisers who lead the executive departments."
        },
        {
            "p": "In 2002, Congress combined 22 agencies into a new department, which became the newest department represented in this group. Tom Ridge was the first person to hold that post, Secretary of Homeland Security.",
            "r": "For 10 points, name this group of top presidential advisers, made up mainly of the heads of 15 executive departments."
        },
        {
            "p": "Doris Kearns Goodwin’s book _Team of Rivals_ describes how Abraham Lincoln filled this group with men who had run against him for the 1860 nomination, including William Seward and Salmon Chase. Lincoln later made Chase Chief Justice after he left this group.",
            "r": "For 10 points, name this group of top presidential advisers, whose members must be confirmed by the Senate."
        },
        {
            "p": "The Department of Commerce and Labor, created in 1903, was split into two separate departments in 1913, each with its own seat in this group. The old War Department lost its seat after 1947, when it became part of what was soon renamed the Department of Defense.",
            "r": "For 10 points, name this group of the president’s top advisers, which includes the heads of 15 executive departments."
        },
        {
            "p": "Among the department heads in this group, only the leader of the Justice Department, which was created in 1870, does not carry the title “Secretary.” Other members of this group include the vice president, and some presidents have added officials such as the ambassador to the United Nations.",
            "r": "For 10 points, name this body of top presidential advisers, which first met under George Washington."
        }
    ],
    "clues": [
        {
            "id": "advisers",
            "tier": "giveaway",
            "t": "The president’s group of top advisers, mostly the heads (secretaries) of the executive departments",
            "k": ["advisers", "executive departments", "secretaries"],
            "n": 0
        },
        {
            "id": "washington-four",
            "tier": "giveaway",
            "t": "George Washington’s first one had four members: Jefferson (State), Hamilton (Treasury), Knox (War), and Randolph (Attorney General)",
            "k": ["jefferson", "hamilton", "knox", "randolph"],
            "n": 0,
            "rabbit": "George Washington"
        },
        {
            "id": "senate-confirm",
            "tier": "giveaway",
            "t": "Its members are nominated by the president and confirmed by the Senate",
            "k": ["confirmed", "senate", "nominated"],
            "n": 0
        },
        {
            "id": "fifteen",
            "tier": "giveaway",
            "t": "Includes the heads of 15 executive departments, plus the vice president and other top officials",
            "k": ["departments", "15", "vice president"],
            "n": 0
        },
        {
            "id": "principal-officer",
            "tier": "middle",
            "t": "Not named in the Constitution; Article II lets the president require the written “Opinion” of the “principal Officer” of each department",
            "k": ["principal officer", "article ii", "opinion"],
            "n": 0
        },
        {
            "id": "kitchen",
            "tier": "middle",
            "t": "Andrew Jackson’s unofficial “Kitchen” advisers, such as editors Amos Kendall and Francis Blair, were nicknamed after it",
            "k": ["kitchen", "andrew jackson", "kendall", "blair"],
            "n": 0,
            "rabbit": "Andrew Jackson"
        },
        {
            "id": "perkins",
            "tier": "middle",
            "t": "First woman member: Frances Perkins, Franklin Roosevelt’s Secretary of Labor (1933–1945)",
            "k": ["frances perkins", "perkins", "labor", "first woman"],
            "n": 0
        },
        {
            "id": "weaver",
            "tier": "middle",
            "t": "First African American member: Robert C. Weaver, Secretary of Housing and Urban Development under Lyndon Johnson (1966)",
            "k": ["weaver", "housing and urban development", "hud"],
            "n": 0
        },
        {
            "id": "homeland",
            "tier": "middle",
            "t": "Newest department: Homeland Security (2002), formed from 22 agencies after the September 11 attacks; Tom Ridge led it first",
            "k": ["homeland security", "2002", "tom ridge"],
            "n": 0,
            "rabbit": "Department of Homeland Security"
        },
        {
            "id": "tenure",
            "tier": "middle",
            "t": "Tenure of Office Act (1867): Senate approval needed to fire certain officials; Andrew Johnson was impeached after removing Edwin Stanton",
            "k": ["tenure of office act", "edwin stanton", "stanton", "impeached"],
            "n": 0,
            "rabbit": "Andrew Johnson"
        },
        {
            "id": "succession",
            "tier": "middle",
            "t": "Its members follow the vice president, Speaker, and president pro tempore in the line of succession, in the order their departments were created",
            "k": ["succession", "order", "pro tempore"],
            "n": 0
        },
        {
            "id": "jefferson-hamilton",
            "tier": "middle",
            "t": "Jefferson and Hamilton clashed in Washington’s meetings over the national bank, helping start the first political parties",
            "k": ["national bank", "political parties", "clashed"],
            "n": 0
        },
        {
            "id": "team-of-rivals",
            "tier": "middle",
            "t": "Abraham Lincoln’s “Team of Rivals” included former opponents William Seward and Salmon Chase",
            "k": ["team of rivals", "seward", "chase"],
            "n": 0
        },
        {
            "id": "designated-survivor",
            "tier": "power",
            "t": "One member skips the State of the Union address as the “designated survivor”",
            "k": ["designated survivor", "state of the union"],
            "n": 0
        },
        {
            "id": "25th-amendment",
            "tier": "power",
            "t": "25th Amendment, Section 4: the vice president and a majority of its department heads can declare the president unable to serve",
            "k": ["25th amendment", "section 4", "unable"],
            "n": 0
        },
        {
            "id": "lansing",
            "tier": "power",
            "t": "Woodrow Wilson forced out Secretary of State Robert Lansing (1920) for calling its meetings while Wilson was ill",
            "k": ["robert lansing", "lansing", "wilson"],
            "n": 0
        },
        {
            "id": "taney-tower",
            "tier": "power",
            "t": "The Senate first rejected a nominee in 1834 (Roger Taney for Treasury); it also rejected John Tower for Defense (1989)",
            "k": ["roger taney", "taney", "john tower", "1834"],
            "n": 0
        },
        {
            "id": "tyler",
            "tier": "power",
            "t": "In 1841, all of John Tyler’s department heads except Daniel Webster resigned after he vetoed national bank bills",
            "k": ["john tyler", "tyler", "daniel webster", "resigned"],
            "n": 0
        },
        {
            "id": "petticoat",
            "tier": "power",
            "t": "The Petticoat Affair over Peggy Eaton broke up Andrew Jackson’s first one (1831)",
            "k": ["petticoat affair", "peggy eaton", "eaton"],
            "n": 0
        },
        {
            "id": "postmaster",
            "tier": "power",
            "t": "The Postmaster General had a seat from Andrew Jackson’s time until 1971, when the Post Office became the U.S. Postal Service",
            "k": ["postmaster general", "postal service", "1971"],
            "n": 0
        },
        {
            "id": "hobby",
            "tier": "power",
            "t": "Oveta Culp Hobby of Houston, the first Secretary of Health, Education, and Welfare (1953), was the second woman member",
            "k": ["oveta culp hobby", "hobby", "houston"],
            "n": 0
        },
        {
            "id": "albright-powell",
            "tier": "power",
            "t": "Firsts at State: Madeleine Albright, the first woman Secretary of State (1997), and Colin Powell, the first African American (2001)",
            "k": ["madeleine albright", "albright", "colin powell", "powell"],
            "n": 0,
            "rabbit": "Secretary of State"
        },
        {
            "id": "fort-knox",
            "tier": "power",
            "t": "Fort Knox, Kentucky, is named for the first Secretary of War, Henry Knox; Edmund Randolph had presented the Virginia Plan",
            "k": ["fort knox", "henry knox", "virginia plan"],
            "n": 0,
            "rabbit": "Henry Knox"
        },
        {
            "id": "hamilton-musical",
            "tier": "power",
            "t": "Two rap “Battles” in the musical _Hamilton_ show Jefferson and Hamilton arguing at its meetings (the debt plan; whether to help France)",
            "k": ["rap", "battles", "musical", "debt plan"],
            "n": 0,
            "rabbit": "Alexander Hamilton"
        },
        {
            "id": "myers",
            "tier": "power",
            "t": "The Tenure of Office Act was repealed in 1887; in 1926 the Supreme Court said it had been unconstitutional",
            "k": ["1887", "1926", "repealed", "unconstitutional"],
            "n": 0
        },
        {
            "id": "attorney-general",
            "tier": "power",
            "t": "The Attorney General, head of the Justice Department (created 1870), is the only department head not called “Secretary”",
            "k": ["attorney general", "justice department", "1870"],
            "n": 0
        },
        {
            "id": "commerce-labor",
            "tier": "power",
            "t": "Commerce and Labor (1903) split into two departments in 1913; the War Department lost its seat after 1947, when Defense took over",
            "k": ["commerce and labor", "1913", "war department", "1947"],
            "n": 0
        }
    ],
    "trap": {
        "title": "A group, not a branch",
        "body": "This answer is a group of people, so naming one member (such as the Secretary of State) or the whole executive branch is wrong. Andrew Jackson’s “Kitchen Cabinet” was an unofficial circle of friends and newspaper editors, not the official group, and Franklin Roosevelt’s “Brain Trust” was a team of professors who advised him. Because the Constitution never uses the word “cabinet,” clues about the “principal Officer” of each executive department point here.",
        "fix": "If the question says “this group” or “this body” and mentions department heads, secretaries, Senate confirmation, or the line of succession, say “Cabinet.” If it asks only for Jackson’s informal advisers, the answer is the Kitchen Cabinet; if it describes one office, name that office.",
        "line": "Real answer line: <b><u>Cabinet</u></b> of the United States (accept <u>President’s Cabinet</u>; do not accept “Executive branch” or a single cabinet post)"
    },
    "tests": {
        "right": [
            "Cabinet",
            "the Cabinet",
            "President's Cabinet",
            "U.S. Cabinet",
            "Cabinet of the United States",
            "cabinett"
        ],
        "prompt": [
            "executive departments",
            "department heads"
        ],
        "wrong": [
            "Executive branch",
            "Secretary of State",
            "Kitchen Cabinet",
            "Brain Trust",
            "National Security Council",
            "Congress",
            "Shadow Cabinet"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
