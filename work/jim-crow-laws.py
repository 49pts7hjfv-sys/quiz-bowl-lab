import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "jim-crow-laws",
    "name": "Jim Crow laws",
    "mono": "JCL",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "Segregation laws of the South · Ended by civil rights laws of the 1960s",
    "dates": "Late 1800s–1960s",
    "briefing": "Jim Crow laws kept Black and white Southerners apart in schools, trains, restaurants, theaters, and even at drinking fountains, from the late 1800s until the 1960s. Other laws used poll taxes, literacy tests, and grandfather clauses to keep Black citizens from voting. The name came from a character in 1830s minstrel shows. The Supreme Court allowed segregation in _Plessy v. Ferguson_ (1896), but court rulings and the Civil Rights Act of 1964 and Voting Rights Act of 1965 finally brought the system down.",
    "answerHtml": "<b><u>Jim Crow</u></b> laws (accept <u>Jim Crow</u> era or system; prompt on <u>segregation</u> laws; do not accept “Black Codes”)",
    "accept": [
        "jim crow laws",
        "jim crow",
        "jim crow law",
        "the jim crow laws",
        "jim crow era",
        "jim crow system",
        "jim crow segregation",
        "jim crow south"
    ],
    "prompt": [
        "segregation",
        "segregation laws",
        "racial segregation",
        "racial segregation laws",
        "southern segregation",
        "segregation in the south"
    ],
    "reject": [
        "black codes",
        "black code",
        "plessy v ferguson",
        "plessy",
        "separate but equal",
        "separate car act",
        "brown v board of education",
        "civil rights act",
        "civil rights act of 1964",
        "voting rights act",
        "voting rights act of 1965",
        "ku klux klan",
        "kkk",
        "reconstruction",
        "poll tax",
        "poll taxes",
        "literacy test",
        "literacy tests",
        "grandfather clause",
        "grandfather clauses",
        "white primary",
        "green book",
        "apartheid",
        "nuremberg laws",
        "desegregation",
        "integration",
        "sharecropping",
        "redlining"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Jim_Crow_laws",
    "qb": {
        "q": "Jim Crow",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "The nickname for these laws came from a character that the white performer Thomas D. Rice made famous in minstrel shows of the 1830s, which mocked Black Americans. By the late 1800s, that character’s name had become a label for segregation.",
            "r": "For 10 points, name these laws that segregated Black and white Americans in the South until the 1960s."
        },
        {
            "p": "In his 1895 Atlanta Compromise speech, Booker T. Washington seemed to accept these laws, saying that in social matters the races could be “as separate as the fingers, yet one as the hand.” W. E. B. Du Bois criticized that approach.",
            "r": "The Supreme Court upheld one of these laws the next year in _Plessy v. Ferguson_. For 10 points, name these segregation laws of the American South."
        },
        {
            "p": "Mississippi’s 1890 constitution added a poll tax and a literacy test that kept most Black citizens from voting, and other Southern states soon copied it. In _Williams v. Mississippi_ (1898), the Supreme Court let those rules stand.",
            "r": "For 10 points, name this system of laws that blocked Black voting and enforced segregation in the South from the late 1800s until the 1960s."
        },
        {
            "p": "Louisiana added a “grandfather clause” to its constitution in 1898, letting men skip new voting tests if their fathers or grandfathers had been able to vote before 1867. The Supreme Court struck down Oklahoma’s version of that rule in _Guinn v. United States_ in 1915.",
            "r": "For 10 points, name this system of Southern laws that kept Black citizens from voting and segregated public places."
        },
        {
            "p": "In _Smith v. Allwright_ (1944), the Supreme Court struck down the “white primary,” which Texas Democrats used to keep Black voters out of the elections that really decided who held office in the one-party South. Thurgood Marshall argued that case for the NAACP.",
            "r": "For 10 points, name these laws and rules that kept Black Southerners from voting and enforced segregation until the 1960s."
        },
        {
            "p": "The Twenty-fourth Amendment, ratified in 1964, banned one voting tool of these laws in federal elections, and the Supreme Court banned it in state elections two years later in _Harper v. Virginia Board of Elections_.",
            "r": "That tool was the poll tax. For 10 points, name these Southern laws that also used literacy tests to keep Black citizens from voting."
        },
        {
            "p": "Starting in 1936, the Harlem mail carrier Victor Hugo Green published a guide listing hotels, restaurants, and gas stations that would serve Black travelers, who faced these laws in the South and discrimination elsewhere. A 2018 film named for his guide won the Academy Award for Best Picture.",
            "r": "For 10 points, name these laws that segregated the South from the late 1800s until the 1960s."
        },
        {
            "p": "In the Civil Rights Cases of 1883, the Supreme Court struck down the Civil Rights Act of 1875, ruling that Congress could not ban discrimination by private businesses such as inns and theaters. That decision, along with the end of Reconstruction, opened the way for these laws.",
            "r": "For 10 points, name these segregation laws later approved under the doctrine of “separate but equal.”"
        },
        {
            "p": "Louisiana’s Separate Car Act of 1890, one of these laws, required railroads to provide “equal but separate” cars for white and Black passengers. A New Orleans citizens’ committee planned a test case in which a passenger broke that law on purpose in 1892.",
            "r": "In 1896, the Supreme Court upheld it in _Plessy v. Ferguson_. For 10 points, name these segregation laws of the South."
        },
        {
            "p": "In _Browder v. Gayle_ (1956), federal judges struck down Alabama’s and Montgomery’s bus segregation rules, which were part of these laws, and the Supreme Court agreed. That ruling ended a boycott that had begun when Rosa Parks refused to give up her bus seat.",
            "r": "For 10 points, name these laws that kept Black and white Southerners apart on buses and in schools and restaurants."
        },
        {
            "p": "On February 1, 1960, four Black college students sat down at a whites-only Woolworth’s lunch counter in Greensboro, North Carolina, starting a wave of sit-ins against the segregation that these laws and local customs enforced.",
            "r": "For 10 points, name these Southern segregation laws, which the Civil Rights Act of 1964 helped bring to an end."
        },
        {
            "p": "In 1961, the Freedom Riders rode buses through the South to test whether states would obey _Boynton v. Virginia_, a ruling that banned segregation in bus terminals serving travelers between states. Mobs attacked some of the riders in Alabama.",
            "r": "For 10 points, name these segregation laws that the Freedom Riders and other civil rights activists challenged."
        },
        {
            "p": "Millions of Black Southerners moved to cities in the North and West during the Great Migration, partly to escape these laws and the violence used to enforce them. Many rode the Illinois Central Railroad north to Chicago.",
            "r": "For 10 points, name these Southern laws, named for a minstrel-show character, that kept the races apart."
        },
        {
            "p": "In _Loving v. Virginia_ (1967), the Supreme Court struck down state laws that banned marriages between people of different races, some of the last of these laws still in force. Three years earlier, Congress had banned segregation in hotels, restaurants, and theaters.",
            "r": "That 1964 law was the Civil Rights Act. For 10 points, name these Southern segregation laws."
        },
        {
            "p": "Writing for a unanimous Supreme Court in 1954, Earl Warren declared that “separate educational facilities are inherently unequal,” striking at the legal basis of these laws in public schools. Thurgood Marshall of the NAACP had argued that case.",
            "r": "For 10 points, name these segregation laws of the South, which had been upheld in _Plessy v. Ferguson_."
        }
    ],
    "clues": [
        {
            "id": "segregation",
            "tier": "giveaway",
            "t": "State and local laws that segregated Black and white people in the South from the late 1800s to the 1960s",
            "k": ["segregated", "south", "1960s"],
            "n": 0
        },
        {
            "id": "separate-but-equal",
            "tier": "giveaway",
            "t": "Upheld by the Supreme Court in _Plessy v. Ferguson_ (1896) under the doctrine of “separate but equal”",
            "k": ["plessy", "separate but equal", "1896"],
            "n": 0,
            "rabbit": "Plessy v. Ferguson"
        },
        {
            "id": "civil-rights-act",
            "tier": "giveaway",
            "t": "Brought down by court rulings and by the Civil Rights Act of 1964 and the Voting Rights Act of 1965",
            "k": ["civil rights act", "voting rights act", "1964", "1965"],
            "n": 0
        },
        {
            "id": "voting-tools",
            "tier": "giveaway",
            "t": "Kept Black citizens from voting with poll taxes, literacy tests, and grandfather clauses",
            "k": ["poll taxes", "literacy tests", "grandfather clauses"],
            "n": 0
        },
        {
            "id": "name-origin",
            "tier": "middle",
            "t": "Named for a character in 1830s minstrel shows, made famous by the white performer Thomas D. Rice",
            "k": ["minstrel", "thomas d. rice", "rice"],
            "n": 0
        },
        {
            "id": "brown",
            "tier": "middle",
            "t": "_Brown v. Board of Education_ (1954) ruled segregated public schools unconstitutional",
            "k": ["brown v. board of education", "brown", "1954"],
            "n": 0,
            "rabbit": "Brown v. Board of Education"
        },
        {
            "id": "24th-amendment",
            "tier": "middle",
            "t": "The 24th Amendment (1964) banned poll taxes in federal elections",
            "k": ["24th amendment", "federal elections"],
            "n": 0
        },
        {
            "id": "green-book",
            "tier": "middle",
            "t": "Victor Hugo Green’s _Green Book_ (from 1936) listed places that would serve Black travelers; a 2018 film named for it won Best Picture",
            "k": ["green book", "victor hugo green", "1936"],
            "n": 0
        },
        {
            "id": "montgomery",
            "tier": "middle",
            "t": "The Montgomery Bus Boycott (1955–1956), begun after Rosa Parks’s arrest, challenged bus segregation",
            "k": ["montgomery", "rosa parks", "boycott"],
            "n": 0,
            "rabbit": "Rosa Parks"
        },
        {
            "id": "separate-car-act",
            "tier": "middle",
            "t": "Louisiana’s Separate Car Act (1890) required “equal but separate” train cars",
            "k": ["separate car act", "equal but separate"],
            "n": 0
        },
        {
            "id": "end-of-reconstruction",
            "tier": "middle",
            "t": "Spread after Reconstruction ended in 1877 and federal troops left the South",
            "k": ["reconstruction", "1877"],
            "n": 0,
            "rabbit": "Reconstruction"
        },
        {
            "id": "atlanta-compromise",
            "tier": "power",
            "t": "Booker T. Washington’s Atlanta Compromise speech (1895): “as separate as the fingers, yet one as the hand”",
            "k": ["atlanta compromise", "booker t. washington", "fingers"],
            "n": 0
        },
        {
            "id": "mississippi-plan",
            "tier": "power",
            "t": "Mississippi’s 1890 constitution used a poll tax and a literacy test to block Black voters; other states copied it",
            "k": ["mississippi", "1890 constitution"],
            "n": 0
        },
        {
            "id": "williams",
            "tier": "power",
            "t": "_Williams v. Mississippi_ (1898) let Mississippi’s voting rules stand",
            "k": ["williams v. mississippi", "1898"],
            "n": 0
        },
        {
            "id": "guinn",
            "tier": "power",
            "t": "Louisiana’s grandfather clause (1898); _Guinn v. United States_ (1915) struck down Oklahoma’s",
            "k": ["guinn", "grandfather clause", "oklahoma", "louisiana"],
            "n": 0,
            "rabbit": "NAACP"
        },
        {
            "id": "white-primary",
            "tier": "power",
            "t": "_Smith v. Allwright_ (1944) struck down the Texas “white primary”; Thurgood Marshall argued the case",
            "k": ["white primary", "smith v. allwright", "allwright"],
            "n": 0,
            "rabbit": "Thurgood Marshall"
        },
        {
            "id": "harper",
            "tier": "power",
            "t": "_Harper v. Virginia Board of Elections_ (1966) banned poll taxes in state elections",
            "k": ["harper", "virginia board of elections"],
            "n": 0
        },
        {
            "id": "civil-rights-cases",
            "tier": "power",
            "t": "The Civil Rights Cases (1883) struck down the Civil Rights Act of 1875, allowing private businesses to discriminate",
            "k": ["civil rights cases", "1883", "1875"],
            "n": 0
        },
        {
            "id": "browder",
            "tier": "power",
            "t": "_Browder v. Gayle_ (1956) ended bus segregation in Montgomery",
            "k": ["browder v. gayle", "browder"],
            "n": 0
        },
        {
            "id": "greensboro",
            "tier": "power",
            "t": "Greensboro sit-ins (1960): four Black college students at a Woolworth’s lunch counter",
            "k": ["greensboro", "woolworth", "sit-ins", "lunch counter"],
            "n": 0
        },
        {
            "id": "freedom-rides",
            "tier": "power",
            "t": "The Freedom Riders (1961) tested _Boynton v. Virginia_, which banned segregated bus terminals for travel between states",
            "k": ["freedom riders", "boynton"],
            "n": 0
        },
        {
            "id": "great-migration",
            "tier": "power",
            "t": "Millions of Black Southerners moved north and west in the Great Migration, partly to escape segregation",
            "k": ["great migration", "north"],
            "n": 0
        },
        {
            "id": "loving",
            "tier": "power",
            "t": "_Loving v. Virginia_ (1967) struck down state bans on interracial marriage",
            "k": ["loving v. virginia", "interracial marriage", "loving"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Laws, codes, or case?",
        "body": "Several answer lines travel together in these tossups. The Black Codes were laws Southern states passed in 1865 and 1866, right after the Civil War, to control newly freed people; Jim Crow laws came later, after Reconstruction ended, and lasted until the 1960s. _Plessy v. Ferguson_ is the 1896 court case that upheld them, and “separate but equal” is the doctrine from that case, so neither earns credit when the question asks for “these laws.”",
        "fix": "Listen for dates and nouns. 1865–1866 and freed people right after the war mean the Black Codes; “this case” or “this decision” means _Plessy v. Ferguson_; “these laws” with clues from the 1880s to the 1960s means Jim Crow laws. Saying only “segregation” earns a prompt, so add “Jim Crow.”",
        "line": "Real answer line: <b><u>Jim Crow</u></b> laws (accept <u>Jim Crow</u>; prompt on <u>segregation</u>; do not accept “Black Codes”)"
    },
    "tests": {
        "right": [
            "Jim Crow laws",
            "Jim Crow",
            "Jim Crow era",
            "jim crowe laws",
            "Jim Crow segregation",
            "the Jim Crow laws"
        ],
        "prompt": [
            "segregation",
            "segregation laws"
        ],
        "wrong": [
            "Black Codes",
            "Plessy v. Ferguson",
            "separate but equal",
            "Ku Klux Klan",
            "poll tax",
            "Reconstruction",
            "apartheid",
            "Brown v. Board of Education"
        ]
    }
}

out = ROOT / "topics" / f"{data['id']}.json"
with open(out, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("wrote", out)
