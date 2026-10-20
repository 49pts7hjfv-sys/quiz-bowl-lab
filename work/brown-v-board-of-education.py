import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TIP = "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."

data = {
    "id": "brown-v-board-of-education",
    "name": "Brown v. Board of Education",
    "mono": "BVB",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "Unanimous 1954 Supreme Court ruling · Struck down school segregation",
    "dates": "Decided May 17, 1954",
    "briefing": "Linda Brown was a third grader in Topeka, Kansas, who had to travel across town to an all-Black school even though a school for white children was much closer to her home. Her father, Oliver Brown, joined an NAACP lawsuit, and lawyer Thurgood Marshall carried the fight to the Supreme Court. On May 17, 1954, Chief Justice Earl Warren read the unanimous ruling: “separate educational facilities are inherently unequal.”",
    "answerHtml": "<b><u>Brown</u></b> v. <b><u>Board</u></b> of Education of Topeka (prompt on <u>Brown</u> alone or on <u>school desegregation</u>; do not accept “Plessy v. Ferguson”)",
    "accept": [
        "brown v board of education",
        "brown v board of education of topeka",
        "brown v board of education of topeka kansas",
        "brown v board",
        "brown vs board of education",
        "brown vs board",
        "brown versus board of education",
        "brown versus board",
        "brown v the board of education",
        "brown v topeka board of education",
        "brown v topeka"
    ],
    "prompt": [
        "brown",
        "school desegregation",
        "desegregation",
        "desegregation of schools",
        "school integration",
        "brown decision",
        "brown case",
        "the brown case"
    ],
    "reject": [
        "plessy v ferguson",
        "plessy",
        "ferguson",
        "sweatt v painter",
        "mclaurin v oklahoma state regents",
        "mclaurin",
        "bolling v sharpe",
        "bolling",
        "briggs v elliott",
        "briggs",
        "davis v county school board",
        "cooper v aaron",
        "swann v charlotte mecklenburg",
        "mendez v westminster",
        "little rock nine",
        "little rock",
        "civil rights act",
        "civil rights act of 1964",
        "dred scott v sandford",
        "marbury v madison",
        "miranda v arizona",
        "roe v wade",
        "john brown",
        "linda brown",
        "oliver brown",
        "gordon brown",
        "earl warren",
        "thurgood marshall",
        "naacp",
        "jim crow laws",
        "jim crow",
        "southern manifesto",
        "montgomery bus boycott",
        "ruby bridges"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Brown_v._Board_of_Education",
    "qb": {
        "q": "Brown v. Board",
        "found": 0,
        "tip": TIP
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "Psychologists Kenneth and Mamie Clark found that many Black children preferred white dolls to Black dolls, and this decision cited their research in its eleventh footnote. This decision declared that separating children by race “generates a feeling of inferiority” that may affect their “hearts and minds.”",
            "r": "Chief Justice Earl Warren wrote it. For 10 points, name this 1954 Supreme Court case that struck down segregation in public schools."
        },
        {
            "p": "In 1951, sixteen-year-old Barbara Johns led a student strike against crowded, run-down conditions at Robert Russa Moton High School in Farmville, Virginia. The lawsuit that grew out of that strike became one of five school cases the Supreme Court heard together under this case’s name.",
            "r": "For 10 points, name this 1954 case in which NAACP lawyer Thurgood Marshall persuaded the Court to end school segregation."
        },
        {
            "p": "John W. Davis, a former Democratic nominee for president, argued for South Carolina in _Briggs v. Elliott_, a case from Clarendon County that the Supreme Court combined with this one. Lawyers on the other side argued that segregation itself, not just unequal buildings, violated the Constitution.",
            "r": "This case was named for a father in Topeka, Kansas. For 10 points, name this 1954 case that overturned “separate but equal” in public schools."
        },
        {
            "p": "Because Washington, D.C., is not a state, the Supreme Court decided its school case, _Bolling v. Sharpe_, under the Fifth Amendment on the same day as this case. This case itself relied on the Equal Protection Clause of the Fourteenth Amendment.",
            "r": "For 10 points, name this unanimous 1954 decision that ended legal segregation in America’s public schools."
        },
        {
            "p": "After Chief Justice Fred Vinson died in 1953, this case was argued a second time before his replacement, a former governor of California. That new Chief Justice worked to get all nine justices to agree, believing a unanimous ruling would be harder to resist.",
            "r": "That man, Earl Warren, read this ruling aloud in May 1954. For 10 points, name this case that struck down school segregation."
        },
        {
            "p": "A year after this decision, a follow-up ruling ordered schools to desegregate “with all deliberate speed,” a vague phrase that many Southern districts used to delay for years. In 1956, about 100 Southern members of Congress signed the Southern Manifesto attacking this decision.",
            "r": "For 10 points, name this 1954 Supreme Court case that overturned _Plessy v. Ferguson_ in public education."
        },
        {
            "p": "Virginia senator Harry Byrd called for “massive resistance” to this decision, and Prince Edward County, Virginia, closed all of its public schools from 1959 to 1964 rather than obey it. In 1957, Arkansas governor Orval Faubus used the National Guard to keep nine Black students out of Little Rock’s Central High School.",
            "r": "For 10 points, name this 1954 Supreme Court ruling that ordered an end to segregated public schools."
        },
        {
            "p": "Earlier NAACP victories in _Sweatt v. Painter_, about a law school in Texas, and _McLaurin v. Oklahoma State Regents_ helped prepare the way for this case. The NAACP’s campaign that led to this case was planned by Charles Hamilton Houston, who trained a generation of Black lawyers at Howard University.",
            "r": "Houston’s former student Thurgood Marshall argued this case. For 10 points, name this 1954 case that struck down school segregation."
        },
        {
            "p": "A third grader was turned away from the all-white Sumner Elementary School, which was much closer to her home, and had to attend the all-Black Monroe Elementary School instead. The Monroe school building later became a national park site honoring this case.",
            "r": "Her father, Oliver Brown of Topeka, Kansas, gave his name to the lawsuit. For 10 points, name this 1954 Supreme Court case."
        },
        {
            "p": "This decision called education “perhaps the most important function of state and local governments” and concluded that separate schools are “inherently unequal.” It rejected the reasoning of an 1896 case that had upheld segregated railroad cars in Louisiana.",
            "r": "For 10 points, name this 1954 case that ended the “separate but equal” rule in public schools."
        },
        {
            "p": "In _Cooper v. Aaron_ (1958), all nine justices signed an opinion saying Arkansas officials could not ignore this earlier ruling. That case followed a 1957 crisis in which President Dwight Eisenhower sent the 101st Airborne Division to protect nine Black students in Little Rock.",
            "r": "This earlier case was argued by Thurgood Marshall. For 10 points, name this unanimous 1954 case that declared segregated public schools unconstitutional."
        },
        {
            "p": "Norman Rockwell’s painting _The Problem We All Live With_ shows six-year-old Ruby Bridges walking between federal marshals to integrate a New Orleans elementary school in 1960. Bridges had been born in 1954, the same year this ruling came down.",
            "r": "For 10 points, name this Supreme Court case in which Earl Warren’s Court declared school segregation unconstitutional."
        },
        {
            "p": "Seven years before this ruling, a federal appeals court decided _Mendez v. Westminster_, which ended the segregation of Mexican American students in parts of Orange County, California. The California governor who then signed a law ending school segregation in his state later wrote this ruling.",
            "r": "That man was Earl Warren. For 10 points, name this 1954 Supreme Court case that struck down laws requiring segregated public schools."
        },
        {
            "p": "This decision called the history of the Fourteenth Amendment “inconclusive” on whether its writers meant to ban segregated schools, so it focused on the role of education in modern life. The Court had asked lawyers to research that history before the case was argued again in 1953.",
            "r": "Chief Justice Earl Warren wrote its opinion. For 10 points, name this unanimous 1954 school desegregation case."
        },
        {
            "p": "Many people saw this decision as proof that Justice John Marshall Harlan had been right when he wrote, as the lone dissenter in an 1896 case, that “Our Constitution is color-blind.” This decision came 58 years after that case.",
            "r": "For 10 points, name this 1954 case brought for Linda Brown and other Black students that overturned “separate but equal.”"
        }
    ],
    "clues": [
        {
            "id": "school-segregation",
            "tier": "giveaway",
            "t": "1954 Supreme Court case that ruled segregated public schools unconstitutional",
            "k": ["1954", "segregated", "public schools", "unconstitutional"],
            "n": 0
        },
        {
            "id": "plessy",
            "tier": "giveaway",
            "t": "Overturned the “separate but equal” rule of _Plessy v. Ferguson_ (1896) for public schools",
            "k": ["separate but equal", "plessy", "1896"],
            "n": 0,
            "rabbit": "Plessy v. Ferguson"
        },
        {
            "id": "topeka",
            "tier": "giveaway",
            "t": "Named for Oliver Brown of Topeka, Kansas, whose daughter Linda had to attend a distant all-Black school",
            "k": ["topeka", "kansas", "linda", "oliver"],
            "n": 0
        },
        {
            "id": "warren",
            "tier": "giveaway",
            "t": "Chief Justice Earl Warren wrote the unanimous (9–0) opinion",
            "k": ["earl warren", "warren", "unanimous"],
            "n": 0,
            "rabbit": "Earl Warren"
        },
        {
            "id": "thurgood-marshall",
            "tier": "giveaway",
            "t": "Argued by NAACP lawyer Thurgood Marshall, who became the first African American Supreme Court justice in 1967",
            "k": ["thurgood marshall", "naacp", "first african american"],
            "n": 0,
            "rabbit": "Thurgood Marshall"
        },
        {
            "id": "inherently-unequal",
            "tier": "middle",
            "t": "The ruling said “separate educational facilities are inherently unequal”",
            "k": ["inherently unequal", "inherently"],
            "n": 0
        },
        {
            "id": "equal-protection",
            "tier": "middle",
            "t": "Based on the Equal Protection Clause of the 14th Amendment",
            "k": ["equal protection", "14th amendment", "fourteenth"],
            "n": 0
        },
        {
            "id": "five-cases",
            "tier": "middle",
            "t": "One of five school cases heard together, from Kansas, South Carolina, Virginia, Delaware, and Washington, D.C.",
            "k": ["five", "south carolina", "delaware"],
            "n": 0
        },
        {
            "id": "all-deliberate-speed",
            "tier": "middle",
            "t": "A 1955 follow-up ruling ordered desegregation “with all deliberate speed”",
            "k": ["all deliberate speed", "deliberate speed", "1955"],
            "n": 0
        },
        {
            "id": "little-rock",
            "tier": "middle",
            "t": "1957: Governor Orval Faubus blocked the Little Rock Nine from Central High, and Eisenhower sent the 101st Airborne to enforce the ruling",
            "k": ["little rock", "faubus", "101st airborne", "eisenhower"],
            "n": 0,
            "rabbit": "Dwight D. Eisenhower"
        },
        {
            "id": "southern-manifesto",
            "tier": "middle",
            "t": "About 100 Southern members of Congress signed the 1956 Southern Manifesto against it",
            "k": ["southern manifesto", "manifesto", "1956"],
            "n": 0
        },
        {
            "id": "ruby-bridges",
            "tier": "middle",
            "t": "In 1960, six-year-old Ruby Bridges integrated a New Orleans school, a scene Norman Rockwell painted in _The Problem We All Live With_",
            "k": ["ruby bridges", "rockwell", "new orleans"],
            "n": 0
        },
        {
            "id": "doll-tests",
            "tier": "power",
            "t": "Kenneth and Mamie Clark’s “doll tests,” cited in footnote 11, suggested segregation harmed Black children’s self-image",
            "k": ["doll tests", "doll", "mamie clark", "footnote 11"],
            "n": 0
        },
        {
            "id": "hearts-and-minds",
            "tier": "power",
            "t": "Said segregation “generates a feeling of inferiority” that may affect children’s “hearts and minds”",
            "k": ["hearts and minds", "inferiority"],
            "n": 0
        },
        {
            "id": "barbara-johns",
            "tier": "power",
            "t": "Barbara Johns, 16, led a 1951 student strike at Moton High School in Farmville, Virginia, which led to one of the combined cases",
            "k": ["barbara johns", "moton", "farmville"],
            "n": 0
        },
        {
            "id": "briggs",
            "tier": "power",
            "t": "_Briggs v. Elliott_ came from Clarendon County, South Carolina; John W. Davis argued for the state",
            "k": ["briggs", "clarendon", "john w. davis"],
            "n": 0
        },
        {
            "id": "bolling",
            "tier": "power",
            "t": "Companion case _Bolling v. Sharpe_ ended school segregation in Washington, D.C., under the Fifth Amendment",
            "k": ["bolling", "sharpe", "fifth amendment"],
            "n": 0
        },
        {
            "id": "vinson",
            "tier": "power",
            "t": "Reargued in 1953 after Chief Justice Fred Vinson died and Eisenhower named Earl Warren to replace him",
            "k": ["fred vinson", "vinson", "reargued"],
            "n": 0
        },
        {
            "id": "sweatt-mclaurin",
            "tier": "power",
            "t": "Earlier NAACP wins in 1950: _Sweatt v. Painter_ (a Texas law school) and _McLaurin v. Oklahoma State Regents_",
            "k": ["sweatt", "painter", "mclaurin"],
            "n": 0
        },
        {
            "id": "houston",
            "tier": "power",
            "t": "Charles Hamilton Houston, Thurgood Marshall’s teacher at Howard University, planned the NAACP’s legal campaign against school segregation",
            "k": ["charles hamilton houston", "houston", "howard"],
            "n": 0
        },
        {
            "id": "sumner-monroe",
            "tier": "power",
            "t": "Linda was refused at the nearby white Sumner Elementary and went to all-Black Monroe Elementary, later made a national park site",
            "k": ["sumner", "monroe elementary", "national park site"],
            "n": 0
        },
        {
            "id": "massive-resistance",
            "tier": "power",
            "t": "“Massive resistance”: Virginia senator Harry Byrd urged defiance, and Prince Edward County closed its public schools (1959–1964)",
            "k": ["massive resistance", "harry byrd", "prince edward"],
            "n": 0
        },
        {
            "id": "cooper-v-aaron",
            "tier": "power",
            "t": "_Cooper v. Aaron_ (1958): all nine justices signed an opinion saying states could not ignore the ruling",
            "k": ["cooper", "aaron", "1958"],
            "n": 0
        },
        {
            "id": "inconclusive",
            "tier": "power",
            "t": "Called the 14th Amendment’s history “inconclusive” and focused on education’s importance in modern life",
            "k": ["inconclusive"],
            "n": 0
        },
        {
            "id": "mendez",
            "tier": "power",
            "t": "_Mendez v. Westminster_ (1947) ended segregation of Mexican American students in parts of California; Governor Earl Warren then signed a law ending school segregation there",
            "k": ["mendez", "westminster", "mexican american"],
            "n": 0
        },
        {
            "id": "harlan",
            "tier": "power",
            "t": "Seen as proving right Justice John Marshall Harlan’s lone _Plessy_ dissent: “Our Constitution is color-blind”",
            "k": ["harlan", "color-blind"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Plessy or Brown?",
        "body": "Both cases are about “separate but equal,” so they show up together in many tossups. _Plessy v. Ferguson_ (1896) upheld segregated railroad cars in Louisiana and created that rule; _Brown v. Board_ (1954) struck it down for public schools. Some real tossups ask for school desegregation itself, with clues like the Little Rock Nine and Ruby Bridges, and a 1955 follow-up ruling, often called “Brown II,” ordered desegregation “with all deliberate speed.”",
        "fix": "Listen for the date and the verb: 1896, Homer Plessy, railroad cars, and “upheld” mean _Plessy_; 1954, Topeka, Earl Warren, and “struck down” or “overturned” mean Brown. If the question asks for “this process,” answer school desegregation; for “this case,” say the full name, because “Brown” alone only earns a prompt.",
        "line": "Real answer line: <b><u>Brown</u></b> v. <b><u>Board</u></b> of Education of Topeka (prompt on <u>Brown</u> alone; prompt on <u>school desegregation</u>)"
    },
    "tests": {
        "right": [
            "Brown v. Board of Education",
            "Brown v. Board",
            "Brown vs. Board of Education of Topeka",
            "Brown versus Board of Education",
            "Brown v. Bord of Education"
        ],
        "prompt": [
            "Brown",
            "school desegregation"
        ],
        "wrong": [
            "Plessy v. Ferguson",
            "Sweatt v. Painter",
            "Little Rock Nine",
            "Bolling v. Sharpe",
            "Cooper v. Aaron",
            "John Brown",
            "Earl Warren"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
