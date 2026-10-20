import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "plessy-v-ferguson",
    "name": "Plessy v. Ferguson",
    "mono": "PVF",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "1896 Supreme Court case · Upheld “separate but equal” segregation",
    "dates": "Decided May 18, 1896",
    "briefing": "In 1892, Homer Plessy bought a first-class train ticket in New Orleans and sat in a car reserved for white passengers, on purpose, so that he could be arrested and challenge Louisiana’s law segregating trains. In 1896, the Supreme Court ruled 7–1 against him, approving “separate but equal” facilities. Justice John Marshall Harlan’s lone dissent declared that “our Constitution is color-blind,” and in 1954 _Brown v. Board of Education_ overturned the ruling for public schools.",
    "answerHtml": "<b><u>Plessy</u></b> v. Ferguson (prompt on “Homer Plessy”; do not accept “Brown v. Board of Education”)",
    "accept": [
        "plessy v ferguson",
        "plessy vs ferguson",
        "plessy versus ferguson",
        "plessy ferguson",
        "plessy",
        "plessy case"
    ],
    "prompt": [
        "homer plessy",
        "homer adolph plessy"
    ],
    "reject": [
        "brown v board of education",
        "brown v board",
        "brown versus board of education",
        "brown vs board of education",
        "brown v board of education of topeka",
        "dred scott v sandford",
        "dred scott",
        "jim crow laws",
        "jim crow",
        "john marshall harlan",
        "harlan",
        "henry billings brown",
        "separate but equal",
        "separate car act",
        "civil rights cases",
        "sweatt v painter",
        "fourteenth amendment",
        "14th amendment",
        "thirteenth amendment",
        "13th amendment",
        "marbury v madison",
        "roe v wade",
        "miranda v arizona",
        "mcculloch v maryland",
        "gibbons v ogden"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Plessy_v._Ferguson",
    "qb": {
        "q": "Plessy v. Ferguson",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "A New Orleans group called the Comité des Citoyens [“koh-mee-TAY day see-twah-YEN”], or Citizens’ Committee, raised money to bring this case, and newspaper publisher Louis Martinet helped recruit the white Northern lawyer Albion Tourgée [“toor-ZHAY”] to argue it. The case challenged a Louisiana law requiring separate railroad cars for Black and white passengers.",
            "r": "For 10 points, name this 1896 Supreme Court case that upheld the doctrine of “separate but equal.”"
        },
        {
            "p": "This case began on June 7, 1892, when a passenger who had bought a first-class ticket on the East Louisiana Railroad sat in a car reserved for white riders and refused to move. He was arrested under the Separate Car Act of 1890, which required “equal but separate” train cars for white and Black passengers.",
            "r": "The Court ruled 7–1 against the passenger. For 10 points, name this 1896 Supreme Court case that upheld segregation on Louisiana trains."
        },
        {
            "p": "A lone dissent in this case predicted that the ruling would prove just as harmful as the _Dred Scott_ decision and warned that the “thin disguise” of equal train cars would fool no one. That dissent was written by a Kentucky justice from a slaveholding family.",
            "r": "That justice, John Marshall Harlan, wrote that “our Constitution is color-blind.” For 10 points, name this 1896 case that upheld “separate but equal” segregation."
        },
        {
            "p": "Writing for the majority in this case, Justice Henry Billings Brown argued that laws separating the races did not mark one race as inferior and that laws were powerless to change people’s social feelings. Brown said a state could use its “police power” to pass such reasonable rules.",
            "r": "For 10 points, name this 1896 case, later overturned in public schools by _Brown v. Board of Education_."
        },
        {
            "p": "After this case’s plaintiff was arrested, his lawyers asked a New Orleans criminal court judge to throw out the charges because the train law was unconstitutional, but the judge refused. The Louisiana Supreme Court agreed with that judge, so the plaintiff appealed to the highest court in the nation.",
            "r": "That judge was John Howard Ferguson. For 10 points, name this 1896 case that upheld “separate but equal.”"
        },
        {
            "p": "In 1954, Chief Justice Earl Warren wrote for a unanimous Court that “separate educational facilities are inherently unequal,” rejecting this earlier decision’s reasoning for public schools. Thurgood Marshall of the NAACP had argued against this earlier decision’s doctrine in that 1954 case.",
            "r": "That case was _Brown v. Board of Education_. For 10 points, name this 1896 case that had allowed segregation under the rule of “separate but equal.”"
        },
        {
            "p": "This case’s plaintiff, a shoemaker with mostly European ancestry, was classified as Black under Louisiana law, which helped his lawyers argue that sorting people by race made no sense. Many railroads disliked the law he challenged because the extra cars cost money, and his arrest was arranged in advance.",
            "r": "For 10 points, name this 1896 Supreme Court case that began with a planned arrest on a New Orleans train."
        },
        {
            "p": "Lawyers in this case argued that a segregation law brought back a mark of slavery banned by the Thirteenth Amendment and denied equal protection under the Fourteenth Amendment. The majority rejected both arguments, saying the Fourteenth Amendment protected political equality but could not force social mixing of the races.",
            "r": "The Court’s vote was 7–1. For 10 points, name this 1896 decision that upheld Louisiana’s “separate but equal” railroad law."
        },
        {
            "p": "One of this case’s lawyers, a former Union soldier, had written _A Fool’s Errand_, a best-selling novel about Reconstruction in North Carolina. That lawyer also argued that a reputation for being white was a form of property that a train conductor could not take away.",
            "r": "In his brief, that lawyer, Albion Tourgée [“toor-ZHAY”], wrote that the law should be “color-blind.” For 10 points, name this 1896 case that upheld segregated train cars in Louisiana."
        },
        {
            "p": "Descendants of this case’s plaintiff and of its trial judge formed a foundation together to teach about it, and in 2022 Louisiana’s governor granted the plaintiff a posthumous pardon. After losing his appeal, the plaintiff had pleaded guilty and paid a 25-dollar fine.",
            "r": "For 10 points, name this 1896 Supreme Court case that established the doctrine of “separate but equal.”"
        },
        {
            "p": "In the 1950 case _Sweatt v. Painter_, the Court ruled that a law school Texas had quickly set up for Black students was not equal to the University of Texas, chipping away at this earlier decision. Thurgood Marshall argued that 1950 case before winning an even bigger victory four years later.",
            "r": "That 1954 victory overturned this 1896 decision for public schools. For 10 points, name this case that allowed “separate but equal” segregation."
        },
        {
            "p": "The only justice to dissent in this case had also cast the only dissent in the Civil Rights Cases of 1883, earning the nickname “the Great Dissenter.” His grandson, who had the same name, served on the same court from 1955 to 1971.",
            "r": "That justice, John Marshall Harlan, wrote that “our Constitution is color-blind.” For 10 points, name this 1896 case that upheld segregated train cars."
        },
        {
            "p": "The majority opinion in this case pointed to an 1850 Massachusetts ruling that had allowed separate schools for Black children in Boston as proof that such laws were reasonable. Justice David Brewer did not take part in this case, which was decided 7–1.",
            "r": "For 10 points, name this May 1896 decision that upheld Louisiana’s segregated train cars under the rule of “separate but equal.”"
        },
        {
            "p": "A historical marker stands near the Press Street railroad crossing in New Orleans, where this case’s plaintiff was arrested after telling the conductor he would not move to the car for Black passengers. He had bought a first-class ticket to Covington, Louisiana.",
            "r": "For 10 points, name this 1896 Supreme Court case that upheld Louisiana’s law requiring segregated train cars."
        },
        {
            "p": "For 58 years, this decision gave legal backing to Jim Crow laws that kept Black and white Americans apart in schools, restaurants, theaters, and even at drinking fountains across the South. Facilities set aside for Black Americans under those laws were almost always worse.",
            "r": "For 10 points, name this 1896 case that said segregated facilities were legal if they were “separate but equal.”"
        }
    ],
    "clues": [
        {
            "id": "separate-but-equal",
            "tier": "giveaway",
            "t": "1896 Supreme Court case that upheld racial segregation under the doctrine of “separate but equal”",
            "k": ["separate but equal", "1896", "segregation"],
            "n": 0
        },
        {
            "id": "train-car",
            "tier": "giveaway",
            "t": "Began when a Black passenger in Louisiana sat in a train car reserved for white riders and was arrested (1892)",
            "k": ["train car", "louisiana", "arrested"],
            "n": 0
        },
        {
            "id": "brown-overturned",
            "tier": "giveaway",
            "t": "Overturned for public schools by _Brown v. Board of Education_ (1954)",
            "k": ["brown v. board", "brown v board", "1954", "overturned"],
            "n": 0,
            "rabbit": "Brown v. Board of Education"
        },
        {
            "id": "color-blind",
            "tier": "giveaway",
            "t": "John Marshall Harlan’s lone dissent: “Our Constitution is color-blind”",
            "k": ["harlan", "color-blind", "lone dissent"],
            "n": 0
        },
        {
            "id": "separate-car-act",
            "tier": "middle",
            "t": "Challenged Louisiana’s Separate Car Act (1890), which required “equal but separate” train cars",
            "k": ["separate car act", "1890", "equal but separate"],
            "n": 0
        },
        {
            "id": "seven-to-one",
            "tier": "middle",
            "t": "Decided 7–1 on May 18, 1896",
            "k": ["may 18", "7–1", "7-1"],
            "n": 0
        },
        {
            "id": "henry-brown",
            "tier": "middle",
            "t": "Justice Henry Billings Brown wrote the majority opinion: separating the races did not mean one race was inferior",
            "k": ["henry billings brown", "majority opinion", "inferior"],
            "n": 0
        },
        {
            "id": "jim-crow",
            "tier": "middle",
            "t": "Gave legal backing to Jim Crow segregation laws across the South for 58 years",
            "k": ["jim crow", "58 years"],
            "n": 0,
            "rabbit": "Jim Crow laws"
        },
        {
            "id": "trial-judge",
            "tier": "middle",
            "t": "Trial judge John Howard Ferguson of New Orleans refused to throw out the charges",
            "k": ["trial judge", "john howard", "new orleans"],
            "n": 0
        },
        {
            "id": "fourteenth",
            "tier": "middle",
            "t": "The Court said the law did not violate the 14th Amendment’s Equal Protection Clause or the 13th Amendment",
            "k": ["14th amendment", "equal protection", "13th amendment", "fourteenth"],
            "n": 0
        },
        {
            "id": "comite",
            "tier": "power",
            "t": "New Orleans’s Comité des Citoyens (Citizens’ Committee) planned the test case; Louis Martinet helped organize it",
            "k": ["comité des citoyens", "citizens’ committee", "citizens committee", "martinet"],
            "n": 0
        },
        {
            "id": "tourgee",
            "tier": "power",
            "t": "Lawyer Albion Tourgée, author of _A Fool’s Errand_, argued that the law should be “color-blind”",
            "k": ["albion tourgée", "tourgée", "tourgee", "a fool’s errand"],
            "n": 0
        },
        {
            "id": "east-louisiana",
            "tier": "power",
            "t": "Arrested June 7, 1892, on the East Louisiana Railroad near Press Street in New Orleans, with a first-class ticket to Covington",
            "k": ["east louisiana railroad", "june 7", "press street", "covington"],
            "n": 0
        },
        {
            "id": "shoemaker",
            "tier": "power",
            "t": "The plaintiff, a shoemaker with mostly European ancestry, was classified as Black; railroads disliked the law’s extra cost",
            "k": ["shoemaker", "classified", "railroads"],
            "n": 0
        },
        {
            "id": "dred-scott",
            "tier": "power",
            "t": "Harlan warned the ruling would prove as harmful as the _Dred Scott_ decision; the “thin disguise” of equal cars would fool no one",
            "k": ["dred scott", "thin disguise"],
            "n": 0,
            "rabbit": "Dred Scott v. Sandford"
        },
        {
            "id": "great-dissenter",
            "tier": "power",
            "t": "Harlan, from a Kentucky slaveholding family, also dissented alone in the Civil Rights Cases (1883): “the Great Dissenter”",
            "k": ["great dissenter", "civil rights cases", "kentucky", "1883"],
            "n": 0
        },
        {
            "id": "police-power",
            "tier": "power",
            "t": "Majority: states could use their “police power” to pass reasonable laws, and the law could not force social equality",
            "k": ["police power", "social equality"],
            "n": 0
        },
        {
            "id": "boston-schools",
            "tier": "power",
            "t": "The majority cited an 1850 Massachusetts ruling allowing separate schools in Boston; Justice David Brewer did not take part",
            "k": ["boston", "massachusetts", "david brewer", "brewer"],
            "n": 0
        },
        {
            "id": "warren",
            "tier": "power",
            "t": "In _Brown_ (1954), Earl Warren wrote that “separate educational facilities are inherently unequal”; Thurgood Marshall argued that case",
            "k": ["inherently unequal", "earl warren", "thurgood marshall"],
            "n": 0
        },
        {
            "id": "sweatt",
            "tier": "power",
            "t": "_Sweatt v. Painter_ (1950): a hastily built Texas law school for Black students was ruled not equal",
            "k": ["sweatt", "painter", "law school", "texas"],
            "n": 0
        },
        {
            "id": "pardon",
            "tier": "power",
            "t": "The plaintiff paid a $25 fine (1897); descendants of both sides formed a foundation, and Louisiana pardoned him in 2022",
            "k": ["pardoned", "foundation", "2022", "$25"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Plessy or Brown?",
        "body": "Tossups on _Brown v. Board of Education_ almost always mention Plessy v. Ferguson as the case it overturned, and Plessy tossups mention Brown, so it is easy to name the wrong one. It gets trickier: the justice who wrote the Plessy majority opinion was named Henry Billings Brown, and Plessy was about train cars, not schools. Answering “separate but equal” names the doctrine, not the case, and does not earn credit.",
        "fix": "1896, Louisiana trains, New Orleans, Albion Tourgée, John Marshall Harlan’s lone dissent, and segregation upheld mean Plessy v. Ferguson. 1954, schools in Topeka, Earl Warren, Thurgood Marshall, a unanimous Court, and segregation struck down mean _Brown v. Board of Education_.",
        "line": "Real answer line: <b><u>Plessy</u></b> v. Ferguson (prompt on “Homer Plessy”; do not accept “Brown v. Board of Education”)"
    },
    "tests": {
        "right": [
            "Plessy v. Ferguson",
            "Plessy vs. Ferguson",
            "Plessy",
            "Plesy v Ferguson",
            "plessy versus ferguson"
        ],
        "prompt": [
            "Homer Plessy"
        ],
        "wrong": [
            "Brown v. Board of Education",
            "Dred Scott v. Sandford",
            "separate but equal",
            "Jim Crow laws",
            "John Marshall Harlan",
            "Ferguson"
        ]
    }
}

out = ROOT / "topics" / f"{data['id']}.json"
with open(out, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", out)
