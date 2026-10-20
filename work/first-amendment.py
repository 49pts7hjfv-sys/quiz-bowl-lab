import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TIP = "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."

# Every other amendment, in the forms a kid might type, goes in "reject": the answer checker
# forgives typos, so "21st amendment" or "amendment ii" would otherwise count as right.
ORD = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth",
       "eleventh", "twelfth", "thirteenth", "fourteenth", "fifteenth", "sixteenth", "seventeenth",
       "eighteenth", "nineteenth", "twentieth", "twenty first", "twenty second", "twenty third",
       "twenty fourth", "twenty fifth", "twenty sixth", "twenty seventh"]
CARD = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven",
        "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen",
        "twenty", "twenty one", "twenty two", "twenty three", "twenty four", "twenty five",
        "twenty six", "twenty seven"]
ROMAN = ["i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x", "xi", "xii", "xiii", "xiv",
         "xv", "xvi", "xvii", "xviii", "xix", "xx", "xxi", "xxii", "xxiii", "xxiv", "xxv", "xxvi",
         "xxvii"]


def numeric(n):
    if n % 100 in (11, 12, 13):
        return f"{n}th"
    return f"{n}" + {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")


def other_amendments(keep):
    out = []
    for n in range(1, 28):
        if n == keep:
            continue
        i = n - 1
        out += [f"{ORD[i]} amendment", f"{numeric(n)} amendment", f"amendment {ROMAN[i]}",
                f"amendment {n}", f"amendment {CARD[i]}"]
    return out


data = {
    "id": "first-amendment",
    "name": "First Amendment",
    "mono": "1A",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "Five freedoms: religion, speech, press, assembly, petition · Ratified 1791",
    "dates": "Ratified December 15, 1791",
    "briefing": "The First Amendment packs five freedoms into one sentence: religion, speech, the press, peaceful assembly, and petitioning the government. James Madison wrote it as part of the Bill of Rights, ratified in 1791, and its opening words, “Congress shall make no law,” at first limited only the federal government. Supreme Court cases about flag salutes, school prayer, student armbands, and secret government papers have shaped what it means.",
    "answerHtml": "<b><u>First Amendment</u></b> (or <u>Amendment I</u>; prompt on <u>freedom of speech</u>, <u>freedom of religion</u>, or <u>freedom of the press</u>; do not accept “Bill of Rights” or “Second Amendment”)",
    "accept": [
        "first amendment",
        "the first amendment",
        "1st amendment",
        "amendment i",
        "amendment 1",
        "amendment one",
        "first amendment to the united states constitution",
        "first amendment to the us constitution",
        "first amendment to the constitution",
        "first amendment of the bill of rights",
        "first amendment in the bill of rights",
        "first amendment to the bill of rights"
    ],
    "prompt": [
        "freedom of the press",
        "freedom of press",
        "free press",
        "press freedom",
        "freedom of speech",
        "free speech",
        "freedom of expression",
        "freedom of religion",
        "religious freedom",
        "freedom of worship",
        "freedom of assembly",
        "right to assemble",
        "right of assembly",
        "right to petition",
        "freedom of petition",
        "establishment clause",
        "free exercise clause",
        "free speech clause",
        "first",
        "1st"
    ],
    "reject": other_amendments(1) + [
        "bill of rights",
        "english bill of rights",
        "equal rights amendment",
        "sedition act",
        "alien and sedition acts",
        "espionage act",
        "freedom of information act",
        "virginia statute for religious freedom",
        "virginia declaration of rights",
        "declaration of independence",
        "articles of confederation",
        "magna carta"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/First_Amendment_to_the_United_States_Constitution",
    "qb": {
        "q": "First Amendment",
        "found": 0,
        "tip": TIP
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "When Congress sent twelve proposed amendments to the states in 1789, this one was third on the list, but it took a lower number after the two proposals ahead of it failed to win ratification. One of those failed proposals was finally ratified in 1992 as the Twenty-seventh Amendment.",
            "r": "For 10 points, name this part of the Bill of Rights that protects freedom of speech, religion, and the press."
        },
        {
            "p": "In _Everson v. Board of Education_ (1947), Justice Hugo Black applied part of this amendment to the states and quoted Thomas Jefferson’s 1802 letter to the Danbury Baptists. In that letter, Jefferson said this amendment built “a wall of separation between church and state.”",
            "r": "For 10 points, name this amendment whose establishment clause bars Congress from setting up an official religion."
        },
        {
            "p": "Oliver Wendell Holmes Jr. wrote that this amendment would not protect a man “falsely shouting fire in a theatre and causing a panic.” In that 1919 case about leaflets opposing the military draft, Holmes created the “clear and present danger” test.",
            "r": "That case was _Schenck v. United States_. For 10 points, name this amendment that protects freedom of speech."
        },
        {
            "p": "In 1965, Iowa students Mary Beth Tinker, her brother John, and Christopher Eckhardt were suspended for wearing black armbands to school to protest the Vietnam War. In 1969, the Supreme Court ruled that their armbands were protected symbolic speech under this amendment.",
            "r": "For 10 points, name this amendment, which the Court said students do not lose “at the schoolhouse gate.”"
        },
        {
            "p": "A Montgomery, Alabama, city commissioner sued _The New York Times_ over an advertisement supporting Martin Luther King Jr., leading to a 1964 ruling that public officials must prove “actual malice” to win a libel case.",
            "r": "That case strengthened the freedom of the press protected by this amendment. For 10 points, name this amendment."
        },
        {
            "p": "In 1971, the Supreme Court allowed newspapers to keep printing the Pentagon Papers, a secret history of the Vietnam War leaked by Daniel Ellsberg, ruling that the government had not justified stopping them. Forty years earlier, _Near v. Minnesota_ had also struck down a “prior restraint” on the press.",
            "r": "Both cases relied on this amendment’s protection of a free press. For 10 points, name this amendment."
        },
        {
            "p": "On Flag Day in 1943, the Supreme Court ruled that public schools could not force Jehovah’s Witness students to salute the flag, overruling a decision from just three years earlier. Justice Robert Jackson wrote that no official can “prescribe what shall be orthodox in politics, nationalism, religion, or other matters of opinion.”",
            "r": "That case was _West Virginia State Board of Education v. Barnette_. For 10 points, name this amendment that protects freedom of speech and religion."
        },
        {
            "p": "In _Engel v. Vitale_ (1962), the Supreme Court ruled that public schools could not lead students in a prayer written by New York state officials. A year later, it struck down required Bible readings in public schools in _Abington School District v. Schempp_.",
            "r": "Both rulings relied on this amendment’s establishment clause. For 10 points, name this amendment."
        },
        {
            "p": "In _Texas v. Johnson_ (1989), the Supreme Court ruled 5–4 that burning an American flag as a political protest was symbolic speech protected by this amendment. Congress then passed the Flag Protection Act, which the Court struck down the next year.",
            "r": "For 10 points, name this amendment that protects freedom of speech and of the press."
        },
        {
            "p": "In _Brandenburg v. Ohio_ (1969), the Supreme Court ruled that speech can be punished only if it is meant to provoke “imminent lawless action” and is likely to do so. Decades earlier, _Gitlow v. New York_ (1925) began applying this amendment’s protection of speech to state governments.",
            "r": "For 10 points, name this amendment that protects freedom of speech, religion, the press, assembly, and petition."
        },
        {
            "p": "The 1735 trial of printer John Peter Zenger is seen as an early step toward this amendment’s protection of a free press. Less than seven years after this amendment was ratified, the Sedition Act of 1798 made it a crime to publish “false, scandalous and malicious” writing against the government.",
            "r": "Thomas Jefferson later pardoned people convicted under that law. For 10 points, name this amendment that guarantees freedom of the press."
        },
        {
            "p": "In _Wisconsin v. Yoder_ (1972), the Supreme Court ruled that Amish parents could not be forced to keep their children in school after the eighth grade. In 1993, the Court sided with a Santería congregation in Hialeah, Florida, under the same part of this amendment.",
            "r": "That part is called the free exercise clause. For 10 points, name this amendment that protects freedom of religion."
        },
        {
            "p": "In _Hazelwood School District v. Kuhlmeier_ (1988), the Supreme Court ruled that a Missouri principal could remove articles from a student newspaper written in a journalism class. That decision said schools may limit what students publish in school-sponsored papers for teaching reasons.",
            "r": "For 10 points, name this amendment that protects freedom of the press, speech, and religion."
        },
        {
            "p": "Under the 1833 case _Barron v. Baltimore_, rights like those in this amendment were held to limit only the federal government, not the states. In the 1900s, the Supreme Court applied this amendment’s protections to the states through the Fourteenth Amendment’s Due Process Clause.",
            "r": "This amendment begins “Congress shall make no law respecting an establishment of religion.” For 10 points, name it."
        },
        {
            "p": "For decades, courts used a three-part test from _Lemon v. Kurtzman_ (1971) to decide cases under this amendment’s establishment clause. In 2022, in a case about a high school football coach who prayed on the field after games, the Supreme Court said it had abandoned that test.",
            "r": "That 2022 case was _Kennedy v. Bremerton School District_. For 10 points, name this amendment that protects freedom of religion."
        }
    ],
    "clues": [
        {
            "id": "five-freedoms",
            "tier": "giveaway",
            "t": "Protects five freedoms: religion, speech, the press, peaceful assembly, and petitioning the government",
            "k": ["five freedoms", "religion", "speech", "press", "petition"],
            "n": 0
        },
        {
            "id": "bill-of-rights",
            "tier": "giveaway",
            "t": "Part of the Bill of Rights, ratified December 15, 1791",
            "k": ["bill of rights", "1791"],
            "n": 0,
            "rabbit": "Bill of Rights"
        },
        {
            "id": "opening-words",
            "tier": "giveaway",
            "t": "Begins “Congress shall make no law respecting an establishment of religion”",
            "k": ["congress shall make no law", "establishment of religion"],
            "n": 0
        },
        {
            "id": "religion-clauses",
            "tier": "middle",
            "t": "Its religion clauses are the establishment clause (no official religion) and the free exercise clause",
            "k": ["establishment clause", "free exercise"],
            "n": 0
        },
        {
            "id": "wall-of-separation",
            "tier": "middle",
            "t": "Thomas Jefferson’s 1802 letter to the Danbury Baptists said it built “a wall of separation between church and state”",
            "k": ["wall of separation", "danbury", "jefferson"],
            "n": 0,
            "rabbit": "Thomas Jefferson"
        },
        {
            "id": "tinker",
            "tier": "middle",
            "t": "_Tinker v. Des Moines_ (1969): students’ black armbands protesting the Vietnam War were protected speech",
            "k": ["tinker", "armbands", "des moines"],
            "n": 0
        },
        {
            "id": "schenck",
            "tier": "middle",
            "t": "_Schenck v. United States_ (1919): Holmes’s “clear and present danger” test and “falsely shouting fire in a theatre”",
            "k": ["schenck", "clear and present danger", "holmes"],
            "n": 0
        },
        {
            "id": "pentagon-papers",
            "tier": "middle",
            "t": "_New York Times Co. v. United States_ (1971): newspapers could keep printing the Pentagon Papers",
            "k": ["pentagon papers", "1971"],
            "n": 0
        },
        {
            "id": "engel",
            "tier": "middle",
            "t": "_Engel v. Vitale_ (1962): public schools may not lead students in an official prayer",
            "k": ["engel", "vitale", "prayer"],
            "n": 0
        },
        {
            "id": "flag-burning",
            "tier": "middle",
            "t": "_Texas v. Johnson_ (1989): burning a flag in protest is protected symbolic speech",
            "k": ["symbolic speech", "flag", "johnson"],
            "n": 0
        },
        {
            "id": "sullivan",
            "tier": "middle",
            "t": "_New York Times Co. v. Sullivan_ (1964): public officials must prove “actual malice” to win libel suits",
            "k": ["sullivan", "actual malice", "libel"],
            "n": 0
        },
        {
            "id": "madison",
            "tier": "middle",
            "t": "James Madison drafted it along with the rest of the Bill of Rights",
            "k": ["james madison", "madison"],
            "n": 0
        },
        {
            "id": "third-of-twelve",
            "tier": "power",
            "t": "Third of the twelve amendments Congress proposed in 1789; the two ahead of it failed, and one of them became the 27th Amendment in 1992",
            "k": ["twelve", "third", "27th amendment", "1992"],
            "n": 0
        },
        {
            "id": "barron-gitlow",
            "tier": "power",
            "t": "_Barron v. Baltimore_ (1833) limited the Bill of Rights to the federal government; _Gitlow v. New York_ (1925) began applying speech rights to the states (incorporation)",
            "k": ["barron", "gitlow", "incorporation", "1925"],
            "n": 0
        },
        {
            "id": "near",
            "tier": "power",
            "t": "_Near v. Minnesota_ (1931): struck down a state “gag law,” limiting “prior restraint” of the press",
            "k": ["prior restraint", "gag law", "minnesota"],
            "n": 0
        },
        {
            "id": "barnette",
            "tier": "power",
            "t": "_West Virginia v. Barnette_ (1943): schools may not force Jehovah’s Witness students to salute the flag; overruled _Gobitis_ (1940)",
            "k": ["barnette", "gobitis", "salute", "jehovah’s witness"],
            "n": 0
        },
        {
            "id": "jackson-orthodox",
            "tier": "power",
            "t": "Justice Robert Jackson in _Barnette_: no official can “prescribe what shall be orthodox”",
            "k": ["robert jackson", "orthodox"],
            "n": 0
        },
        {
            "id": "everson",
            "tier": "power",
            "t": "_Everson v. Board of Education_ (1947): Hugo Black applied the establishment clause to the states",
            "k": ["everson", "hugo black"],
            "n": 0
        },
        {
            "id": "schempp",
            "tier": "power",
            "t": "_Abington School District v. Schempp_ (1963): no required Bible readings in public schools",
            "k": ["schempp", "abington", "bible"],
            "n": 0
        },
        {
            "id": "brandenburg",
            "tier": "power",
            "t": "_Brandenburg v. Ohio_ (1969): speech can be punished only if it is meant and likely to provoke “imminent lawless action”",
            "k": ["brandenburg", "imminent lawless action"],
            "n": 0
        },
        {
            "id": "lemon",
            "tier": "power",
            "t": "_Lemon v. Kurtzman_ (1971) created a three-part test; in _Kennedy v. Bremerton_ (2022) the Court said it had abandoned that test",
            "k": ["lemon", "kurtzman", "bremerton"],
            "n": 0
        },
        {
            "id": "yoder",
            "tier": "power",
            "t": "_Wisconsin v. Yoder_ (1972): Amish parents may keep their children out of school after eighth grade",
            "k": ["yoder", "amish"],
            "n": 0
        },
        {
            "id": "hazelwood",
            "tier": "power",
            "t": "_Hazelwood v. Kuhlmeier_ (1988): schools may limit what students publish in school-sponsored newspapers",
            "k": ["hazelwood", "kuhlmeier", "newspapers"],
            "n": 0
        },
        {
            "id": "zenger-sedition",
            "tier": "power",
            "t": "Early tests of a free press: the Zenger trial (1735) and the Sedition Act of 1798",
            "k": ["zenger", "sedition act", "1735"],
            "n": 0,
            "rabbit": "Alien and Sedition Acts"
        },
        {
            "id": "citizens-united",
            "tier": "power",
            "t": "_Citizens United v. FEC_ (2010): a 5–4 ruling that independent political spending by corporations and unions is protected speech",
            "k": ["citizens united", "corporations", "2010"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Amendment or freedom?",
        "body": "This amendment is one part of the Bill of Rights, so “Bill of Rights” is wrong when a question asks for one amendment. Some real tossups ask for just one of its freedoms, such as “freedom of the press,” and want that exact answer instead. Its neighbors are easy to mix up too: the Second Amendment protects the right to keep and bear arms, and the Fifth lets people refuse to testify against themselves (“pleading the Fifth”).",
        "fix": "Listen for the noun. “This amendment” wants “First Amendment”; “this right” or “this freedom” wants the specific freedom. School prayer, the wall of separation, black armbands, flag burning, and the Pentagon Papers are all First Amendment clues.",
        "line": "Real answer line: <b><u>First Amendment</u></b> (or <u>Amendment I</u>; prompt on <u>freedom of speech</u>, <u>religion</u>, or <u>the press</u>; do not accept “Bill of Rights”)"
    },
    "tests": {
        "right": [
            "First Amendment",
            "1st Amendment",
            "Amendment I",
            "the First Amendment",
            "Frist Amendment"
        ],
        "prompt": [
            "freedom of the press",
            "free speech",
            "freedom of religion"
        ],
        "wrong": [
            "Second Amendment",
            "Bill of Rights",
            "Fifth Amendment",
            "Fourteenth Amendment",
            "Amendment II",
            "Twenty-first Amendment",
            "21st Amendment"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
