import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TIP = "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."

data = {
    "id": "department-of-education",
    "name": "Department of Education",
    "mono": "ED",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "Cabinet department for schools and student aid · Created under Carter, 1979",
    "dates": "Created 1979; opened 1980",
    "briefing": "Most American public schools are run by states and local school boards, but the U.S. Department of Education oversees federal money for schools and colleges. Jimmy Carter signed the law creating it in 1979, splitting it off from a bigger department, and it opened in 1980 with Shirley Hufstedler, a federal judge, as its first secretary. It runs Pell Grants and the FAFSA, the form students fill out to get help paying for college.",
    "answerHtml": "<b><u>Department of Education</u></b> (accept <u>Education Department</u>; prompt on <u>education</u>; do not accept “Department of Energy” or “Department of Health, Education, and Welfare”)",
    "accept": [
        "department of education",
        "the department of education",
        "us department of education",
        "u s department of education",
        "the us department of education",
        "united states department of education",
        "federal department of education",
        "dept of education",
        "education department",
        "the education department",
        "us education department"
    ],
    "prompt": [
        "education",
        "the education"
    ],
    "reject": [
        "department of energy",
        "the department of energy",
        "energy department",
        "doe",
        "department of health education and welfare",
        "health education and welfare",
        "hew",
        "department of health and human services",
        "health and human services",
        "hhs",
        "department of labor",
        "department of the interior",
        "department of housing and urban development",
        "department of homeland security",
        "department of veterans affairs",
        "office of education",
        "us office of education",
        "bureau of education",
        "secretary of education",
        "board of education",
        "state board of education",
        "brown v board of education",
        "national education association",
        "american federation of teachers",
        "no child left behind",
        "every student succeeds act",
        "elementary and secondary education act",
        "individuals with disabilities education act",
        "title ix",
        "pell grant",
        "pell grants",
        "fafsa",
        "head start"
    ],
    "tests": {
        "right": [
            "Department of Education",
            "Education Department",
            "U.S. Department of Education",
            "Dept. of Education",
            "Departmnt of Education"
        ],
        "prompt": [
            "education"
        ],
        "wrong": [
            "Department of Energy",
            "Department of Health, Education, and Welfare",
            "Health and Human Services",
            "Office of Education",
            "Secretary of Education",
            "Brown v. Board of Education",
            "Department of Labor"
        ]
    },
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/United_States_Department_of_Education",
    "qb": {
        "q": "Department of Education",
        "found": 0,
        "tip": TIP
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "A federal appeals court judge, Shirley Hufstedler [“HUFF-sted-ler”], became the first person to lead this executive department in December 1979. She served until early 1981, when Terrel Bell, Ronald Reagan’s choice for the job, took over.",
            "r": "For 10 points, name this Cabinet department, created under Jimmy Carter, that oversees federal school programs and student aid."
        },
        {
            "p": "Henry Barnard, a school reformer from Connecticut, was the first commissioner of an 1867 federal agency that was this department’s forerunner. Congressman James Garfield had sponsored the law creating that agency, which was demoted to an office just a year later.",
            "r": "For 10 points, name this Cabinet department, created in 1979 under Jimmy Carter."
        },
        {
            "p": "This department runs grants named for Senator Claiborne Pell of Rhode Island, which help students from low-income families pay for college. To apply for that aid, students fill out a form called the FAFSA, short for Free Application for Federal Student Aid.",
            "r": "For 10 points, name this Cabinet department created under Jimmy Carter."
        },
        {
            "p": "This department was carved out of a larger department created in 1953, whose first secretary, Oveta Culp Hobby, was only the second woman ever to serve in a president’s Cabinet. The rest of that older department was renamed Health and Human Services.",
            "r": "For 10 points, name this department that opened in 1980, a year after Jimmy Carter signed the law creating it."
        },
        {
            "p": "This department carries out IDEA, a law guaranteeing children with disabilities a free public school program suited to their needs. Gerald Ford signed the first version of that law in 1975, and Congress gave it the name IDEA in 1990.",
            "r": "For 10 points, name this Cabinet department, created in 1979, which also runs federal student aid."
        },
        {
            "p": "In 1983, a commission formed by this department’s second leader, Terrel Bell, warned of “a rising tide of mediocrity” in American schools. That commission’s report, _A Nation at Risk_, set off decades of efforts to raise school standards.",
            "r": "For 10 points, name this Cabinet department, first led by Shirley Hufstedler."
        },
        {
            "p": "Lauro Cavazos [“kuh-VAH-sohs”], who took charge of this department in 1988, was the first Hispanic American to serve in a president’s Cabinet. In 2001, Rod Paige, a former Houston schools superintendent, became the first African American to lead this department.",
            "r": "For 10 points, name this Cabinet department, created by Jimmy Carter."
        },
        {
            "p": "In 2002, George W. Bush signed No Child Left Behind, which required states to test students every year in reading and math, and this department enforced it. In 2015, Barack Obama replaced that law with the Every Student Succeeds Act, which gave states more control.",
            "r": "For 10 points, name this Cabinet department, created in 1979, that oversees federal school programs."
        },
        {
            "p": "This department’s Office for Civil Rights enforces Title IX, a 1972 law that bans discrimination based on sex in school programs that receive federal money. That law helped bring about a huge increase in girls’ and women’s sports.",
            "r": "For 10 points, name this Cabinet department, first led by Shirley Hufstedler in 1979."
        },
        {
            "p": "This department runs Title I, which sends money to schools serving many children from low-income families. That program began with a 1965 law that Lyndon Johnson signed outside the one-room schoolhouse in Texas where he had started school as a boy.",
            "r": "For 10 points, name this Cabinet department created under Jimmy Carter."
        },
        {
            "p": "In 2017, Vice President Mike Pence cast the first tie-breaking vote ever needed to confirm a Cabinet secretary, making Betsy DeVos the head of this department. DeVos held that job until January 2021.",
            "r": "For 10 points, name this Cabinet department, created in 1979, whose first leader was Shirley Hufstedler."
        },
        {
            "p": "The nation’s largest teachers’ union endorsed a presidential candidate for the first time in 1976, partly because he promised to create this department. Congress approved the law creating it in 1979 after close votes in the House of Representatives.",
            "r": "That candidate was Jimmy Carter. For 10 points, name this department, which opened in 1980."
        },
        {
            "p": "Arne Duncan, who had run Chicago’s public schools, led this department under Barack Obama. Duncan ran Race to the Top, a contest in which states competed for billions of dollars in grants by promising to change their schools.",
            "r": "For 10 points, name this Cabinet department, first led by Shirley Hufstedler."
        },
        {
            "p": "In his 1980 campaign, Ronald Reagan promised to abolish this new department, and calls to close it have returned in later decades. Instead, Reagan appointed three men to lead it in turn: Terrel Bell, William Bennett, and Lauro Cavazos.",
            "r": "For 10 points, name this Cabinet department, created under Jimmy Carter in 1979."
        },
        {
            "p": "William Bennett, who led this department in the late 1980s, later became the first director of the White House office that coordinates national drug-control policy. Bennett also edited _The Book of Virtues_, a 1993 collection of stories meant to teach good character.",
            "r": "For 10 points, name this Cabinet department, created in 1979 under Jimmy Carter, that runs federal student aid."
        }
    ],
    "clues": [
        {
            "id": "carter",
            "tier": "giveaway",
            "t": "Created by a law Jimmy Carter signed in October 1979",
            "k": ["jimmy carter", "carter", "1979"],
            "n": 0,
            "rabbit": "Jimmy Carter"
        },
        {
            "id": "opened-1980",
            "tier": "giveaway",
            "t": "Began operating in May 1980",
            "k": ["may 1980", "1980"],
            "n": 0
        },
        {
            "id": "job",
            "tier": "giveaway",
            "t": "Cabinet department that oversees federal programs for schools and federal student aid for college",
            "k": ["student aid", "schools", "cabinet"],
            "n": 0
        },
        {
            "id": "hufstedler",
            "tier": "middle",
            "t": "First secretary: Shirley Hufstedler, a federal appeals court judge (1979–1981)",
            "k": ["shirley hufstedler", "hufstedler", "judge"],
            "n": 0
        },
        {
            "id": "hew",
            "tier": "middle",
            "t": "Split off from the Department of Health, Education, and Welfare (created 1953); the rest became Health and Human Services",
            "k": ["health and human services", "welfare", "1953"],
            "n": 0
        },
        {
            "id": "pell-fafsa",
            "tier": "middle",
            "t": "Runs Pell Grants (named for Senator Claiborne Pell) and the FAFSA, the Free Application for Federal Student Aid",
            "k": ["pell", "fafsa", "claiborne pell"],
            "n": 0
        },
        {
            "id": "idea",
            "tier": "middle",
            "t": "Carries out IDEA, the law guaranteeing children with disabilities a free public school program suited to their needs",
            "k": ["idea", "disabilities"],
            "n": 0
        },
        {
            "id": "title-ix",
            "tier": "middle",
            "t": "Its Office for Civil Rights enforces Title IX (1972), which bans sex discrimination in school programs that get federal money",
            "k": ["title ix", "office for civil rights", "1972"],
            "n": 0
        },
        {
            "id": "nclb",
            "tier": "middle",
            "t": "Enforced No Child Left Behind (2002, George W. Bush), which was replaced by the Every Student Succeeds Act (2015, Barack Obama)",
            "k": ["no child left behind", "every student succeeds", "2002"],
            "n": 0
        },
        {
            "id": "barnard",
            "tier": "middle",
            "t": "Its forerunner, an 1867 federal agency, was first led by Commissioner Henry Barnard and was demoted to an office a year later",
            "k": ["henry barnard", "barnard", "1867"],
            "n": 0
        },
        {
            "id": "nation-at-risk",
            "tier": "middle",
            "t": "_A Nation at Risk_ (1983), from a commission formed by Secretary Terrel Bell, warned of “a rising tide of mediocrity”",
            "k": ["nation at risk", "terrel bell", "mediocrity"],
            "n": 0
        },
        {
            "id": "garfield",
            "tier": "power",
            "t": "Congressman James Garfield sponsored the 1867 law that created its forerunner",
            "k": ["garfield", "congressman"],
            "n": 0
        },
        {
            "id": "hobby",
            "tier": "power",
            "t": "Oveta Culp Hobby, the first secretary of Health, Education, and Welfare (1953), was the second woman in a president’s Cabinet",
            "k": ["oveta culp hobby", "hobby", "second woman"],
            "n": 0
        },
        {
            "id": "ford-1975",
            "tier": "power",
            "t": "Gerald Ford signed the 1975 law that was renamed IDEA in 1990",
            "k": ["gerald ford", "ford", "1975"],
            "n": 0
        },
        {
            "id": "cavazos",
            "tier": "power",
            "t": "Lauro Cavazos (from 1988) was the first Hispanic American in a president’s Cabinet",
            "k": ["lauro cavazos", "cavazos", "hispanic"],
            "n": 0
        },
        {
            "id": "paige",
            "tier": "power",
            "t": "Rod Paige, a former Houston schools superintendent, became its first African American secretary (2001)",
            "k": ["rod paige", "paige", "houston"],
            "n": 0
        },
        {
            "id": "title-i",
            "tier": "power",
            "t": "Runs Title I, money for schools serving many low-income children, which began with a 1965 law Lyndon Johnson signed at his boyhood one-room schoolhouse",
            "k": ["title i", "lyndon johnson", "schoolhouse", "1965"],
            "n": 0,
            "rabbit": "Lyndon B. Johnson"
        },
        {
            "id": "devos",
            "tier": "power",
            "t": "In 2017, Vice President Mike Pence cast the first tie-breaking vote ever needed to confirm a Cabinet secretary, Betsy DeVos",
            "k": ["betsy devos", "devos", "mike pence", "tie-breaking"],
            "n": 0
        },
        {
            "id": "teachers-union",
            "tier": "power",
            "t": "The nation’s largest teachers’ union made its first presidential endorsement, for Carter, in 1976, partly over his promise to create it",
            "k": ["teachers’ union", "endorsement", "1976"],
            "n": 0
        },
        {
            "id": "duncan",
            "tier": "power",
            "t": "Arne Duncan, Barack Obama’s secretary, ran Race to the Top, a contest for billions of dollars in state grants",
            "k": ["arne duncan", "race to the top", "duncan"],
            "n": 0
        },
        {
            "id": "reagan-secretaries",
            "tier": "power",
            "t": "Ronald Reagan’s three secretaries: Terrel Bell, William Bennett, and Lauro Cavazos",
            "k": ["ronald reagan", "william bennett", "three secretaries"],
            "n": 0
        },
        {
            "id": "bennett",
            "tier": "power",
            "t": "William Bennett later became the first director of national drug-control policy and edited _The Book of Virtues_ (1993)",
            "k": ["book of virtues", "bennett", "drug-control"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Education or Energy?",
        "body": "Jimmy Carter created two Cabinet departments: the Department of Energy in 1977 and this one in 1979, so the president clue alone won’t tell you which. This department also grew out of an older one, Health, Education, and Welfare (1953), whose leftover parts became Health and Human Services. Some questions instead want the 1867 agency led by Henry Barnard, or a famous case like _Brown v. Board of Education_.",
        "fix": "Oil, nuclear power, and the 1970s energy crisis mean Energy, which is usually called “DOE.” Schools, Pell Grants, the FAFSA, Title IX, and Shirley Hufstedler mean this department, whose official abbreviation is “ED.” Say the whole name, because “education” alone may only earn a prompt.",
        "line": "Real answer line: <b><u>Department of Education</u></b> (accept <u>Education Department</u>; prompt on <u>education</u>; do not accept “Department of Energy” or “Department of Health, Education, and Welfare”)"
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("wrote", data["id"])
