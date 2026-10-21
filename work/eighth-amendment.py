import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Reject every other amendment number in five forms (the pattern of first-amendment / 27th-amendment).
# None of these forms sits inside one of this topic's accept phrases, so nothing is skipped.
# "bill of rights" is deliberately NOT rejected: it sits inside accepted forms such as
# "eighth amendment of the bill of rights" (a reject phrase would turn "the Eighth Amendment of the
# Bill of Rights" wrong). "Bill of Rights" alone is still judged wrong (see tests).
ORD = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth",
       "eleventh", "twelfth", "thirteenth", "fourteenth", "fifteenth", "sixteenth", "seventeenth",
       "eighteenth", "nineteenth", "twentieth", "twenty first", "twenty second", "twenty third",
       "twenty fourth", "twenty fifth", "twenty sixth", "twenty seventh"]
NUMW = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven",
        "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen",
        "twenty", "twenty one", "twenty two", "twenty three", "twenty four", "twenty five", "twenty six",
        "twenty seven"]
ROMAN = ["i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x", "xi", "xii", "xiii", "xiv", "xv",
         "xvi", "xvii", "xviii", "xix", "xx", "xxi", "xxii", "xxiii", "xxiv", "xxv", "xxvi", "xxvii"]
SUF = {1: "st", 2: "nd", 3: "rd", 21: "st", 22: "nd", 23: "rd"}
other_amendments = []
for i in range(1, 28):
    if i == 8:
        continue
    for form in (f"{ORD[i - 1]} amendment", f"{i}{SUF.get(i, 'th')} amendment",
                 f"amendment {ROMAN[i - 1]}", f"amendment {i}", f"amendment {NUMW[i - 1]}"):
        other_amendments.append(form)

data = {
    "id": "eighth-amendment",
    "name": "Eighth Amendment",
    "mono": "8A",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "No excessive bail or fines, no cruel and unusual punishments · Ratified 1791",
    "dates": "Ratified December 15, 1791",
    "briefing": "The Eighth Amendment is one of the shortest parts of the Bill of Rights, just sixteen words long: “Excessive bail shall not be required, nor excessive fines imposed, nor cruel and unusual punishments inflicted.” Its wording comes almost straight from England’s Bill of Rights of 1689. Supreme Court cases about the death penalty, prison conditions, and sentences for teenagers have all turned on what “cruel and unusual” means.",
    "answerHtml": "<b><u>Eighth Amendment</u></b> (or <u>Amendment VIII</u>; prompt on <u>cruel and unusual punishment</u>, <u>excessive bail</u>, or <u>excessive fines</u>; do not accept “Bill of Rights” or other amendment numbers)",
    "accept": [
        "eighth amendment",
        "the eighth amendment",
        "8th amendment",
        "the 8th amendment",
        "amendment viii",
        "viii amendment",
        "amendment 8",
        "amendment eight",
        "8 amendment",
        "eighth amendment to the united states constitution",
        "eighth amendment to the us constitution",
        "eighth amendment to the constitution",
        "eighth amendment of the bill of rights",
        "eighth amendment in the bill of rights",
        "eighth amendment to the bill of rights"
    ],
    "prompt": [
        "cruel and unusual punishment",
        "cruel and unusual punishments",
        "cruel and unusual",
        "no cruel and unusual punishment",
        "excessive bail",
        "excessive fines",
        "excessive bail clause",
        "excessive fines clause",
        "cruel and unusual punishment clause",
        "cruel and unusual punishments clause",
        "eighth",
        "8th",
        "viii"
    ],
    "reject": other_amendments + [
        "twenty eighth amendment",
        "28th amendment",
        "amendment xxviii",
        "english bill of rights",
        "bill of rights 1689",
        "1689 bill of rights",
        "magna carta",
        "virginia declaration of rights",
        "equal rights amendment",
        "death penalty",
        "capital punishment",
        "due process",
        "double jeopardy",
        "habeas corpus",
        "furman v georgia",
        "gregg v georgia",
        "roper v simmons",
        "timbs v indiana",
        "trop v dulles",
        "atkins v virginia"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Eighth_Amendment_to_the_United_States_Constitution",
    "qb": {
        "q": "Eighth Amendment",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "In _Trop v. Dulles_, Earl Warren wrote that this amendment “must draw its meaning from the evolving standards of decency that mark the progress of a maturing society.” That 1958 case held that a wartime deserter could not be stripped of his citizenship as punishment.",
            "r": "For 10 points, name this part of the Bill of Rights that bans excessive bail, excessive fines, and “cruel and unusual punishments.”"
        },
        {
            "p": "In _Stack v. Boyle_, a 1951 case involving Communist Party members charged under the Smith Act, the Supreme Court ruled under this amendment that bail set higher than needed to make sure a defendant returns for trial is too high.",
            "r": "For 10 points, name this amendment, part of the Bill of Rights, that bans excessive bail and cruel and unusual punishments."
        },
        {
            "p": "In a 2019 case, Ruth Bader Ginsburg wrote for a unanimous Supreme Court that one clause of this amendment applies to the states, after Indiana tried to take away Tyson Timbs’s $42,000 Land Rover, worth more than four times the largest fine allowed for his crime.",
            "r": "That clause bans excessive fines. For 10 points, name this amendment that also outlaws cruel and unusual punishments."
        },
        {
            "p": "In one 1972 case decided under this amendment, all nine justices wrote separate opinions, and Thurgood Marshall and William Brennan argued that the death penalty is always unconstitutional. The 5–4 decision itself was a short unsigned opinion.",
            "r": "That case, _Furman v. Georgia_, struck down the death penalty laws then in use. For 10 points, name this amendment banning cruel and unusual punishments."
        },
        {
            "p": "In _Weems v. United States_, a 1910 case from the Philippines, the Supreme Court read the words also found in this amendment to mean that punishments must be in proportion to the crime. The case involved a harsh sentence for an official who had falsified government records.",
            "r": "For 10 points, name this amendment, ratified in 1791 as part of the Bill of Rights, that bans cruel and unusual punishments."
        },
        {
            "p": "In _Robinson v. California_ (1962), the Supreme Court first used the Fourteenth Amendment to apply part of this amendment to the states, striking down a state law that punished a person for having an illness rather than for any act.",
            "r": "For 10 points, name this amendment that forbids excessive bail, excessive fines, and cruel and unusual punishments."
        },
        {
            "p": "George Mason put almost the same words as this amendment into the Virginia Declaration of Rights in 1776. At Virginia’s ratifying convention, Patrick Henry complained that the proposed Constitution had no such protection.",
            "r": "Its wording came from England’s Bill of Rights of 1689. For 10 points, name this amendment that bans cruel and unusual punishments."
        },
        {
            "p": "In a 2005 opinion, Anthony Kennedy pointed to “the overwhelming weight of international opinion” while ruling that this amendment bars the death penalty for crimes committed before age 18. That 5–4 decision overruled _Stanford v. Kentucky_, a 1989 case.",
            "r": "That case was _Roper v. Simmons_. For 10 points, name this amendment that bans cruel and unusual punishments."
        },
        {
            "p": "In _Atkins v. Virginia_ (2002), the Supreme Court ruled that this amendment bars the death penalty for people with intellectual disabilities, noting that a growing number of states had already banned the practice.",
            "r": "For 10 points, name this amendment, part of the Bill of Rights, that outlaws cruel and unusual punishments."
        },
        {
            "p": "In _Graham v. Florida_ and _Miller v. Alabama_, the Supreme Court used this amendment to limit sentences of life in prison without parole for people who committed crimes as teenagers, pointing out that young people have a greater ability to change.",
            "r": "Those 2010 and 2012 cases built on _Roper v. Simmons_. For 10 points, name this amendment banning cruel and unusual punishments."
        },
        {
            "p": "In _Estelle v. Gamble_ (1976), the Supreme Court ruled that prison officials who show “deliberate indifference” to an inmate’s serious medical needs violate this amendment. The case was brought by a Texas prisoner who hurt his back while doing prison work.",
            "r": "That same year, _Gregg v. Georgia_ allowed states to use new death penalty laws. For 10 points, name this amendment banning cruel and unusual punishments."
        },
        {
            "p": "In _Brown v. Plata_ (2011), Anthony Kennedy wrote for a 5–4 majority that crowding in California’s prisons had made medical care so poor that it violated this amendment, and he upheld an order to reduce the prison population.",
            "r": "For 10 points, name this amendment, part of the Bill of Rights, that bans cruel and unusual punishments."
        },
        {
            "p": "In _Ewing v. California_ (2003), the Supreme Court ruled that a “three strikes” sentence of 25 years to life for a man with earlier serious convictions who had stolen three golf clubs did not violate this amendment.",
            "r": "For 10 points, name this amendment that bans excessive bail, excessive fines, and cruel and unusual punishments."
        },
        {
            "p": "This amendment is only sixteen words long, and its wording comes almost exactly from England’s Bill of Rights of 1689, passed after the Glorious Revolution put William and Mary on the throne.",
            "r": "Its first clause forbids excessive bail. For 10 points, name this amendment that also bans cruel and unusual punishments."
        },
        {
            "p": "In _United States v. Salerno_ (1987), the Supreme Court ruled that the Bail Reform Act of 1984, which lets judges hold some dangerous defendants in jail before trial without bail, did not violate this amendment.",
            "r": "For 10 points, name this amendment whose first clause bans excessive bail and whose last clause bans cruel and unusual punishments."
        }
    ],
    "clues": [
        {
            "id": "three-bans",
            "tier": "giveaway",
            "t": "Bans excessive bail, excessive fines, and cruel and unusual punishments",
            "k": ["cruel and unusual", "excessive bail", "excessive fines"],
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
            "id": "death-penalty",
            "tier": "giveaway",
            "t": "The basis for Supreme Court cases about the death penalty",
            "k": ["death penalty", "supreme court"],
            "n": 0
        },
        {
            "id": "english-bill",
            "tier": "middle",
            "t": "Its words come almost exactly from the English Bill of Rights of 1689",
            "k": ["english bill of rights", "1689"],
            "n": 0
        },
        {
            "id": "furman",
            "tier": "middle",
            "t": "_Furman v. Georgia_ (1972): a 5–4 ruling struck down the death penalty laws then in use",
            "k": ["furman", "1972"],
            "n": 0
        },
        {
            "id": "gregg",
            "tier": "middle",
            "t": "_Gregg v. Georgia_ (1976): allowed states to use new death penalty laws",
            "k": ["gregg", "1976"],
            "n": 0
        },
        {
            "id": "roper",
            "tier": "middle",
            "t": "_Roper v. Simmons_ (2005): no death penalty for crimes committed before age 18",
            "k": ["roper", "simmons", "age 18"],
            "n": 0
        },
        {
            "id": "timbs",
            "tier": "middle",
            "t": "_Timbs v. Indiana_ (2019): the ban on excessive fines applies to the states (a $42,000 Land Rover)",
            "k": ["timbs", "land rover", "2019"],
            "n": 0
        },
        {
            "id": "atkins",
            "tier": "middle",
            "t": "_Atkins v. Virginia_ (2002): no death penalty for people with intellectual disabilities",
            "k": ["atkins", "intellectual disabilities", "2002"],
            "n": 0
        },
        {
            "id": "mason",
            "tier": "middle",
            "t": "George Mason’s Virginia Declaration of Rights (1776) used almost the same words",
            "k": ["george mason", "virginia declaration", "1776"],
            "n": 0
        },
        {
            "id": "sixteen-words",
            "tier": "middle",
            "t": "Only sixteen words long: “Excessive bail shall not be required, nor excessive fines imposed, nor cruel and unusual punishments inflicted”",
            "k": ["sixteen words", "sixteen", "inflicted"],
            "n": 0
        },
        {
            "id": "trop",
            "tier": "power",
            "t": "_Trop v. Dulles_ (1958): Earl Warren said it draws its meaning from “evolving standards of decency”",
            "k": ["trop", "evolving standards of decency", "earl warren"],
            "n": 0,
            "rabbit": "Earl Warren"
        },
        {
            "id": "stack",
            "tier": "power",
            "t": "_Stack v. Boyle_ (1951): bail set higher than needed to make sure a defendant returns for trial is excessive",
            "k": ["stack", "boyle", "1951"],
            "n": 0
        },
        {
            "id": "weems",
            "tier": "power",
            "t": "_Weems v. United States_ (1910): punishments must be in proportion to the crime",
            "k": ["weems", "proportion", "1910"],
            "n": 0
        },
        {
            "id": "robinson",
            "tier": "power",
            "t": "_Robinson v. California_ (1962): first applied its ban on cruel and unusual punishments to the states",
            "k": ["robinson", "1962", "states"],
            "n": 0
        },
        {
            "id": "furman-opinions",
            "tier": "power",
            "t": "In _Furman_, all nine justices wrote separate opinions; Thurgood Marshall and William Brennan said the death penalty is always unconstitutional",
            "k": ["separate opinions", "thurgood marshall", "william brennan"],
            "n": 0,
            "rabbit": "Thurgood Marshall"
        },
        {
            "id": "kennedy-roper",
            "tier": "power",
            "t": "In _Roper_, Anthony Kennedy cited “the overwhelming weight of international opinion”; it overruled _Stanford v. Kentucky_ (1989)",
            "k": ["international opinion", "stanford v. kentucky", "anthony kennedy"],
            "n": 0
        },
        {
            "id": "graham-miller",
            "tier": "power",
            "t": "_Graham v. Florida_ (2010) and _Miller v. Alabama_ (2012) limited life without parole for crimes committed as teenagers",
            "k": ["graham", "miller", "life without parole"],
            "n": 0
        },
        {
            "id": "estelle",
            "tier": "power",
            "t": "_Estelle v. Gamble_ (1976): “deliberate indifference” to a prisoner’s serious medical needs violates it",
            "k": ["estelle", "deliberate indifference", "medical needs"],
            "n": 0
        },
        {
            "id": "plata",
            "tier": "power",
            "t": "_Brown v. Plata_ (2011): crowding in California’s prisons made medical care so poor that the state had to reduce the prison population",
            "k": ["plata", "crowding", "california"],
            "n": 0
        },
        {
            "id": "ewing",
            "tier": "power",
            "t": "_Ewing v. California_ (2003): upheld a “three strikes” sentence of 25 years to life for stealing golf clubs",
            "k": ["ewing", "three strikes", "golf clubs"],
            "n": 0
        },
        {
            "id": "salerno",
            "tier": "power",
            "t": "_United States v. Salerno_ (1987): upheld the Bail Reform Act of 1984, which lets judges hold some dangerous defendants without bail",
            "k": ["salerno", "bail reform act", "1987"],
            "n": 0
        },
        {
            "id": "patrick-henry",
            "tier": "power",
            "t": "At Virginia’s ratifying convention, Patrick Henry complained that the Constitution had no such protection",
            "k": ["patrick henry", "ratifying convention"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Amendment, clause, or case?",
        "body": "This amendment is one part of the Bill of Rights, so “Bill of Rights” is wrong when a question asks for one amendment. Its neighbors are easy to mix up: the Fifth protects against self-incrimination and double jeopardy, and the Sixth guarantees a speedy trial and a lawyer. Saying only “cruel and unusual punishment” or “excessive bail” earns a prompt, and the Eighteenth Amendment (Prohibition) is a different number entirely.",
        "fix": "Bail, fines, “cruel and unusual,” “evolving standards of decency,” the death penalty, and cases like _Furman_, _Gregg_, _Roper_, and _Timbs_ all mean the Eighth Amendment. If the question asks for “this clause,” name the specific clause; if it asks for “this amendment,” say “Eighth Amendment.”",
        "line": "Real answer line: <b><u>Eighth Amendment</u></b> (or <u>Amendment VIII</u>; prompt on <u>cruel and unusual punishment</u> or <u>excessive bail</u>; do not accept other amendment numbers)"
    },
    "tests": {
        "right": [
            "Eighth Amendment",
            "8th Amendment",
            "Amendment VIII",
            "the Eighth Amendment",
            "Eigth Amendment",
            "Eighth Amendment to the Constitution",
            "the Eighth Amendment of the Bill of Rights"
        ],
        "prompt": [
            "cruel and unusual punishment",
            "excessive bail",
            "excessive fines"
        ],
        "wrong": [
            "Fifth Amendment",
            "Bill of Rights",
            "Fourteenth Amendment",
            "Sixth Amendment",
            "18th Amendment",
            "Amendment VII",
            "Eighteenth Amendment",
            "English Bill of Rights",
            "death penalty"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"], "with", len(data["reject"]), "reject entries")
