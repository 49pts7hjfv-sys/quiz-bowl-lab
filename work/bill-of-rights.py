import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "bill-of-rights",
    "name": "Bill of Rights",
    "mono": "BOR",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "First ten amendments to the U.S. Constitution · Ratified in 1791",
    "dates": "Proposed 1789; ratified 1791",
    "briefing": "When the Constitution went to the states in 1787, many Americans worried that it did not protect their basic freedoms, and some states would ratify it only if changes were promised. James Madison answered by writing amendments for the First Congress, and in 1791 ten of them were ratified as the Bill of Rights. They protect freedom of speech, religion, and the press, the right to a fair trial, and much more.",
    "answerHtml": "<b><u>Bill of Rights</u></b> (accept the <u>first ten amendments</u> to the U.S. Constitution; prompt on <u>amendments</u>; do not accept “English Bill of Rights”)",
    "accept": [
        "bill of rights",
        "us bill of rights",
        "united states bill of rights",
        "american bill of rights",
        "first ten amendments",
        "first 10 amendments"
    ],
    "prompt": [
        "amendments",
        "constitutional amendments",
        "amendments to the constitution",
        "ten amendments"
    ],
    "reject": [
        "english bill of rights",
        "bill of rights 1689",
        "bill of rights of 1689",
        "1689 bill of rights",
        "second bill of rights",
        "virginia bill of rights",
        "canadian bill of rights",
        "virginia declaration of rights",
        "declaration of rights",
        "declaration of independence",
        "articles of confederation",
        "magna carta",
        "petition of right",
        "first amendment",
        "second amendment",
        "third amendment",
        "fourth amendment",
        "fifth amendment",
        "eighth amendment",
        "ninth amendment",
        "tenth amendment",
        "10th amendment",
        "fourteenth amendment",
        "14th amendment",
        "27th amendment",
        "civil rights act",
        "equal rights amendment",
        "federalist papers",
        "the federalist papers",
        "declaration of the rights of man"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/United_States_Bill_of_Rights",
    "qb": {
        "q": "Bill of Rights",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "George Mason’s list of objections to the new Constitution began with the complaint, “There is no Declaration of Rights,” and he refused to sign the document in 1787. Mason’s own Virginia Declaration of Rights, written in 1776, later served as a model for this set of amendments.",
            "r": "James Madison drew on Mason’s work when he drafted them. For 10 points, name these ten amendments to the U.S. Constitution, ratified in 1791."
        },
        {
            "p": "During a 1789 race for the House of Representatives against James Monroe, one candidate promised Virginia voters that he would support this set of changes, even though he had once doubted that written “parchment barriers” could protect liberty. That candidate won and introduced these amendments in Congress.",
            "r": "That man was James Madison. For 10 points, name these ten amendments to the Constitution, ratified in 1791."
        },
        {
            "p": "In _Federalist_ No. 84, Alexander Hamilton argued that this addition to the Constitution was unnecessary and might even be dangerous, because listing some rights might suggest that the government could take away others. Anti-Federalists such as Patrick Henry insisted that it was needed to protect people from a powerful national government.",
            "r": "James Madison later wrote it to calm those fears. For 10 points, name this group of ten amendments, ratified in 1791."
        },
        {
            "p": "Congress originally sent twelve amendments to the states in 1789, but only ten were ratified at first. One of the other two, which delays any change in congressional pay until after the next election, finally became the 27th Amendment in 1992.",
            "r": "For 10 points, name the ten amendments that were ratified in 1791 and that protect rights like freedom of speech."
        },
        {
            "p": "In _Barron v. Baltimore_, John Marshall’s Supreme Court ruled in 1833 that this group of amendments limited only the federal government, not the states. In the twentieth century, the Supreme Court used the Fourteenth Amendment to apply most of its protections to state governments as well, a process called incorporation.",
            "r": "For 10 points, name this part of the Constitution made up of the First through Tenth Amendments."
        },
        {
            "p": "Roger Sherman got these changes added as a separate list at the end of the Constitution, instead of being woven into its text as their main author had planned. That author’s favorite proposal, which would have kept the states from violating freedom of the press, was rejected by the Senate.",
            "r": "That author, James Madison, introduced them in the House in 1789. For 10 points, name these ten amendments, ratified in 1791."
        },
        {
            "p": "While serving as the U.S. minister to France, Thomas Jefferson wrote to a friend that this kind of protection “is what the people are entitled to against every government on earth.” That friend, who had helped write the Constitution, later drafted these amendments.",
            "r": "That friend was James Madison. For 10 points, name the first set of amendments to the Constitution, ratified in 1791."
        },
        {
            "p": "One part of this document guarantees a jury trial in lawsuits over more than twenty dollars, and another forbids the government from forcing people to house soldiers in peacetime. Another part says that powers not given to the national government are reserved to the states or to the people.",
            "r": "For 10 points, name this collection of amendments that also protects freedom of speech and religion."
        },
        {
            "p": "Virginia’s approval on December 15, 1791, made these amendments part of the Constitution, and Franklin Roosevelt set aside December 15 to honor them on their 150th anniversary. Massachusetts, Connecticut, and Georgia did not approve them until 1939.",
            "r": "For 10 points, name these ten amendments to the U.S. Constitution, written mostly by James Madison."
        },
        {
            "p": "The words “cruel and unusual punishments” in this document were borrowed from an English law passed in 1689, after the Glorious Revolution placed William and Mary on the throne. The same part of this document also bans excessive bail and fines.",
            "r": "This set of ten amendments was ratified in 1791. For 10 points, name this part of the U.S. Constitution that protects freedom of speech and religion."
        },
        {
            "p": "North Carolina’s original copy of this document was taken by a Union soldier during the Civil War and recovered by the FBI in 2003. The federal government’s copy is displayed in the National Archives in Washington, D.C., alongside the Declaration of Independence and the Constitution.",
            "r": "James Madison wrote most of this document. For 10 points, name this set of ten amendments ratified in 1791."
        },
        {
            "p": "One amendment in this group bans double jeopardy, lets people refuse to testify against themselves, and requires “just compensation” when the government takes private property for public use. Another guarantees a speedy and public trial and the right to a lawyer.",
            "r": "For 10 points, name this set of ten amendments, including the Fifth and Sixth, which were ratified in 1791."
        },
        {
            "p": "In the Massachusetts Compromise, that state ratified the Constitution while recommending changes, and several other states followed its example; those suggestions led to this set of amendments. Anti-Federalists had argued that without such protections, the new national government could threaten people’s freedoms.",
            "r": "For 10 points, name these ten amendments, which James Madison guided through the First Congress."
        },
        {
            "p": "One amendment in this group requires that warrants be based on “probable cause” and forbids “unreasonable searches and seizures.” Another begins by saying that a “well regulated Militia” is necessary to the security of a free state.",
            "r": "For 10 points, name the collection of ten amendments that also protects the freedoms of speech, press, and religion."
        },
        {
            "p": "The House of Representatives approved seventeen amendments in August 1789, but the Senate combined and trimmed them to twelve. The Ninth Amendment, one of the ten that were ratified, says that listing certain rights does not deny others kept by the people.",
            "r": "Those ten were largely written by James Madison. For 10 points, name these amendments ratified in 1791."
        }
    ],
    "clues": [
        {
            "id": "ten-amendments",
            "tier": "giveaway",
            "t": "The ten amendments added to the U.S. Constitution in 1791",
            "k": ["ten amendments", "1791", "constitution"],
            "n": 0
        },
        {
            "id": "madison",
            "tier": "giveaway",
            "t": "Written mainly by James Madison, who introduced them in the First Congress in 1789",
            "k": ["james madison", "madison", "1789"],
            "n": 0,
            "rabbit": "James Madison"
        },
        {
            "id": "freedoms",
            "tier": "giveaway",
            "t": "Protects freedom of speech, religion, and the press (the First Amendment) and the right to a fair trial",
            "k": ["freedom of speech", "religion", "press", "fair trial"],
            "n": 0,
            "rabbit": "First Amendment"
        },
        {
            "id": "anti-federalists",
            "tier": "giveaway",
            "t": "Demanded by the Anti-Federalists, who feared that a strong national government would threaten liberty",
            "k": ["anti-federalists", "anti-federalist"],
            "n": 0
        },
        {
            "id": "mason",
            "tier": "middle",
            "t": "George Mason refused to sign the Constitution partly because it lacked a declaration of rights; his Virginia Declaration of Rights (1776) was a model",
            "k": ["george mason", "mason", "virginia declaration"],
            "n": 0
        },
        {
            "id": "twelve",
            "tier": "middle",
            "t": "Congress proposed twelve amendments in 1789; ten were ratified",
            "k": ["twelve", "proposed"],
            "n": 0
        },
        {
            "id": "december-15",
            "tier": "middle",
            "t": "Ratified on December 15, 1791, when Virginia approved",
            "k": ["december 15", "virginia"],
            "n": 0
        },
        {
            "id": "federalist-84",
            "tier": "middle",
            "t": "Alexander Hamilton argued in _Federalist_ No. 84 that it was unnecessary and even dangerous",
            "k": ["unnecessary", "dangerous", "hamilton"],
            "n": 0,
            "rabbit": "The Federalist Papers"
        },
        {
            "id": "contents",
            "tier": "middle",
            "t": "Includes the right to bear arms (Second), no unreasonable searches (Fourth), and no cruel and unusual punishments (Eighth)",
            "k": ["bear arms", "unreasonable searches", "cruel and unusual"],
            "n": 0,
            "rabbit": "Second Amendment"
        },
        {
            "id": "tenth",
            "tier": "middle",
            "t": "The Tenth Amendment reserves powers not given to the national government to the states or the people",
            "k": ["tenth amendment", "reserves", "states"],
            "n": 0
        },
        {
            "id": "henry-monroe",
            "tier": "middle",
            "t": "Anti-Federalist Patrick Henry demanded amendments; Madison promised them to beat James Monroe in a 1789 House race",
            "k": ["patrick henry", "james monroe", "monroe"],
            "n": 0,
            "rabbit": "Patrick Henry"
        },
        {
            "id": "mason-objections",
            "tier": "power",
            "t": "Mason’s list of objections to the Constitution began, “There is no Declaration of Rights”",
            "k": ["objections", "there is no declaration"],
            "n": 0
        },
        {
            "id": "parchment",
            "tier": "power",
            "t": "Madison at first doubted that “parchment barriers” could protect rights",
            "k": ["parchment barriers", "parchment"],
            "n": 0
        },
        {
            "id": "jefferson-letter",
            "tier": "power",
            "t": "Jefferson, in France, wrote that such protection “is what the people are entitled to against every government on earth”",
            "k": ["every government on earth", "jefferson", "france"],
            "n": 0
        },
        {
            "id": "twenty-seventh",
            "tier": "power",
            "t": "The proposed amendment on congressional pay was finally ratified in 1992 as the 27th Amendment",
            "k": ["27th amendment", "congressional pay", "1992"],
            "n": 0,
            "rabbit": "27th Amendment"
        },
        {
            "id": "barron",
            "tier": "power",
            "t": "_Barron v. Baltimore_ (1833): its protections limited only the federal government, not the states",
            "k": ["barron", "baltimore", "1833"],
            "n": 0
        },
        {
            "id": "incorporation",
            "tier": "power",
            "t": "Incorporation: in the 1900s, the Supreme Court used the Fourteenth Amendment to apply most of its protections to the states",
            "k": ["incorporation", "fourteenth amendment"],
            "n": 0
        },
        {
            "id": "sherman",
            "tier": "power",
            "t": "Roger Sherman got the amendments added as a list at the end of the Constitution instead of woven into the text",
            "k": ["roger sherman", "sherman"],
            "n": 0
        },
        {
            "id": "most-valuable",
            "tier": "power",
            "t": "Madison’s favorite proposal, protecting the press and conscience from the states, was rejected by the Senate",
            "k": ["favorite proposal", "conscience", "senate"],
            "n": 0
        },
        {
            "id": "anniversaries",
            "tier": "power",
            "t": "FDR set aside December 15 to honor it on its 150th anniversary (1941); Massachusetts, Connecticut, and Georgia ratified only in 1939",
            "k": ["150th anniversary", "1939", "connecticut", "georgia"],
            "n": 0
        },
        {
            "id": "english-1689",
            "tier": "power",
            "t": "“Cruel and unusual punishments” came from an English law of 1689, passed after the Glorious Revolution",
            "k": ["1689", "glorious revolution", "english"],
            "n": 0,
            "rabbit": "Glorious Revolution"
        },
        {
            "id": "archives",
            "tier": "power",
            "t": "North Carolina’s copy was stolen in the Civil War and recovered by the FBI (2003); the federal copy is at the National Archives",
            "k": ["national archives", "north carolina", "fbi"],
            "n": 0
        },
        {
            "id": "massachusetts-compromise",
            "tier": "power",
            "t": "Massachusetts Compromise: states ratified the Constitution while recommending amendments",
            "k": ["massachusetts compromise", "recommending"],
            "n": 0
        },
        {
            "id": "seventeen",
            "tier": "power",
            "t": "The House passed seventeen amendments (1789); the Senate cut them to twelve; the Ninth Amendment protects rights not listed",
            "k": ["seventeen", "ninth amendment"],
            "n": 0
        },
        {
            "id": "third-seventh",
            "tier": "power",
            "t": "The Third Amendment bans quartering soldiers in homes in peacetime; the Seventh promises juries in lawsuits over twenty dollars",
            "k": ["quartering", "twenty dollars", "seventh"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Which bill of rights?",
        "body": "England’s Bill of Rights of 1689, passed after the Glorious Revolution, shows up in European history tossups, and it gave the American version the phrase “cruel and unusual punishments.” George Mason’s Virginia Declaration of Rights (1776) was a model too. Some tossups ask for one amendment, like the First or the Fifth, instead of the whole set, and others want James Madison himself.",
        "fix": "1689, Parliament, or William and Mary means the English one; Madison, 1791, the Anti-Federalists, or “the first ten amendments” means the American one. Listen for “this amendment” (just one) versus “these amendments” or “this document” (all ten), and “this man” for Madison.",
        "line": "Real answer line: <b><u>Bill of Rights</u></b> (accept the <u>first ten amendments</u> to the U.S. Constitution; do not accept “English Bill of Rights”)"
    },
    "tests": {
        "right": [
            "Bill of Rights",
            "the Bill of Rights",
            "US Bill of Rights",
            "Bill of Right",
            "first ten amendments"
        ],
        "prompt": [
            "amendments"
        ],
        "wrong": [
            "English Bill of Rights",
            "Constitution",
            "First Amendment",
            "Virginia Declaration of Rights",
            "Second Bill of Rights",
            "Magna Carta",
            "Tenth Amendment"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
