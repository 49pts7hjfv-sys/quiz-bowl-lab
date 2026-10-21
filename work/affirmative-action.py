import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "affirmative-action",
    "name": "Affirmative action",
    "mono": "AA",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "Programs to widen opportunity for minorities and women · Begun in the 1960s",
    "dates": "Begun 1961; race-conscious college admissions ended 2023",
    "briefing": "Affirmative action means taking active steps to widen opportunities in jobs, contracts, and college admissions for groups that have faced discrimination, such as racial minorities and women. Presidents John F. Kennedy and Lyndon Johnson started federal programs in the 1960s. Supporters argue it makes up for past and present discrimination and builds diversity; opponents argue it treats people unequally because of race or sex. In 2023, the Supreme Court ruled that colleges may not use race-conscious admissions programs.",
    "answerHtml": "<b><u>affirmative action</u></b> (prompt on descriptions like <u>race-conscious admissions</u> or <u>racial preferences</u>)",
    "accept": [
        "affirmative action",
        "affirmative action programs",
        "affirmative action policy",
        "affirmative action policies"
    ],
    "prompt": [
        "affirmative",
        "race conscious admissions",
        "race based admissions",
        "race conscious policies",
        "racial preferences",
        "preferential treatment"
    ],
    "reject": [
        "equal protection clause",
        "equal protection",
        "fourteenth amendment",
        "14th amendment",
        "civil rights act",
        "civil rights act of 1964",
        "title vii",
        "title vi",
        "title ix",
        "equal rights amendment",
        "equal employment opportunity commission",
        "eeoc",
        "brown v board of education",
        "desegregation",
        "integration",
        "busing",
        "jim crow laws",
        "plessy v ferguson",
        "separate but equal",
        "executive order 9066",
        "executive order 8802",
        "voting rights act",
        "great society",
        "war on poverty",
        "civil rights movement",
        "reverse discrimination"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Affirmative_action_in_the_United_States",
    "qb": {
        "q": "affirmative action",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "In March 1961, John F. Kennedy’s Executive Order 10925 told government contractors to make sure job applicants were treated “without regard to their race, creed, color, or national origin.” That order created a committee on equal job opportunity led by Vice President Lyndon Johnson.",
            "r": "Kennedy’s order called for this policy by name. For 10 points, name this policy of taking active steps to open jobs and schools to groups that faced discrimination."
        },
        {
            "p": "Lyndon Johnson’s Executive Order 11246, signed in September 1965, required companies with federal contracts to take active steps against job discrimination and put the Labor Department in charge of enforcing it. A 1967 order added discrimination based on sex.",
            "r": "For 10 points, name this policy, which aims to widen opportunities for women and minorities and was tested in court cases such as _Regents v. Bakke_."
        },
        {
            "p": "In a 1965 speech at Howard University, Lyndon Johnson argued that it was not enough to free a person who had been held back for years, bring him to the starting line of a race, and then say he was free to compete.",
            "r": "Opponents of this policy argue that it treats people unequally because of race. For 10 points, name this policy, ended in college admissions by a 2023 Supreme Court ruling."
        },
        {
            "p": "In 1969, Labor Secretary George Shultz announced the Philadelphia Plan, which required construction companies on federally funded projects in that city to set goals and timetables for hiring minority workers in skilled trades.",
            "r": "That plan under Richard Nixon was an early example of this policy. For 10 points, name this policy, which the Supreme Court addressed in the _Bakke_ case."
        },
        {
            "p": "Allan Bakke, a white applicant, was rejected twice by the medical school at the University of California, Davis, which set aside 16 of its 100 places for minority students. In 1978, the Supreme Court ruled 5–4 that this fixed quota was not allowed and ordered Bakke admitted.",
            "r": "But Justice Lewis Powell wrote that race could be one factor among many. For 10 points, name this policy that the _Bakke_ case limited but did not end."
        },
        {
            "p": "In _United Steelworkers v. Weber_ (1979), the Supreme Court upheld a training program at a Kaiser Aluminum plant that saved half its spots for Black workers. A year later, _Fullilove v. Klutznick_ upheld a federal law setting aside some public works money for minority-owned businesses.",
            "r": "For 10 points, name this kind of policy, which tries to widen opportunities for groups that faced discrimination."
        },
        {
            "p": "In _City of Richmond v. J.A. Croson Co._ (1989), the Supreme Court struck down a Virginia city’s rule setting aside 30 percent of construction contract money for minority-owned businesses. Six years later, _Adarand Constructors v. Peña_ [“PAYN-yuh”] said federal programs that use race must pass “strict scrutiny.”",
            "r": "For 10 points, name this kind of policy, which considers race or sex to widen opportunities."
        },
        {
            "p": "In a campaign led by the businessman Ward Connerly, California voters approved Proposition 209 in 1996, banning state agencies and public universities from giving preference to anyone based on race, sex, or ethnicity. In 2020, voters rejected a measure that would have repealed it.",
            "r": "For 10 points, name this policy that Proposition 209 ended in California’s public colleges and government jobs."
        },
        {
            "p": "After a federal court ruled in _Hopwood v. Texas_ (1996) that the University of Texas law school could not consider race, Texas guaranteed admission to its public universities for students in the top ten percent of their high school classes. Abigail Fisher later challenged the university’s use of race.",
            "r": "In 2016, the Supreme Court upheld the Texas program 4–3. For 10 points, name this policy, often called race-conscious admissions."
        },
        {
            "p": "In _Gratz v. Bollinger_ (2003), the Supreme Court struck down the University of Michigan’s undergraduate admissions system, which automatically gave 20 points out of 150 to applicants from underrepresented minority groups.",
            "r": "On the same day, a related case upheld a more flexible plan at Michigan’s law school. For 10 points, name this policy that both cases tested."
        },
        {
            "p": "Writing for a 5–4 majority in _Grutter v. Bollinger_ (2003), Justice Sandra Day O’Connor upheld the University of Michigan Law School’s use of race as one factor and wrote that she expected it to be unnecessary “25 years from now.”",
            "r": "For 10 points, name this policy that a 2023 Supreme Court ruling ended in college admissions."
        },
        {
            "p": "Edward Blum founded the group Students for Fair Admissions, which sued Harvard and the University of North Carolina. Justice Ketanji Brown Jackson sat out the Harvard case because she had served on one of Harvard’s governing boards.",
            "r": "In June 2023, the Supreme Court ruled against the schools’ race-conscious admissions. For 10 points, name this policy that the ruling ended in college admissions."
        },
        {
            "p": "In 2006, Michigan voters approved Proposal 2, which banned public colleges in that state from giving preference based on race or sex. In 2014, the Supreme Court upheld that ban in a case named for Michigan’s attorney general, Bill Schuette [“SHOO-tee”].",
            "r": "For 10 points, name this policy, which California had also banned in public colleges with Proposition 209."
        },
        {
            "p": "In January 2025, President Donald Trump signed an order revoking Executive Order 11246, which for about sixty years had required federal contractors to take active steps to hire and promote women and minorities.",
            "r": "Lyndon Johnson had signed that order in 1965. For 10 points, name this policy, which the Supreme Court had ended in college admissions in 2023."
        },
        {
            "p": "In a 2023 opinion, Chief Justice John Roberts wrote that colleges could still consider an applicant’s essay about how race had affected his or her life, and a footnote set aside the question of the military academies.",
            "r": "That ruling ended race-conscious college admissions. For 10 points, name this policy that _Grutter v. Bollinger_ had upheld in 2003."
        }
    ],
    "clues": [
        {
            "id": "definition",
            "tier": "giveaway",
            "t": "Taking active steps to widen opportunities in jobs, contracts, and college admissions for groups that faced discrimination",
            "k": ["active steps", "opportunities", "discrimination"],
            "n": 0
        },
        {
            "id": "sffa",
            "tier": "giveaway",
            "t": "_Students for Fair Admissions v. Harvard_ (2023) ended race-conscious college admissions",
            "k": ["students for fair admissions", "harvard", "2023"],
            "n": 0
        },
        {
            "id": "bakke",
            "tier": "giveaway",
            "t": "_Regents of the University of California v. Bakke_ (1978) struck down a fixed racial quota but allowed race as one factor",
            "k": ["bakke", "quota", "1978"],
            "n": 0
        },
        {
            "id": "kennedy-johnson",
            "tier": "giveaway",
            "t": "Started by executive orders under John F. Kennedy (1961) and Lyndon Johnson (1965)",
            "k": ["executive orders", "kennedy", "lyndon johnson"],
            "n": 0
        },
        {
            "id": "eo-10925",
            "tier": "middle",
            "t": "Kennedy’s Executive Order 10925 (1961) told contractors to treat applicants “without regard to their race, creed, color, or national origin”",
            "k": ["10925", "contractors", "1961"],
            "n": 0
        },
        {
            "id": "eo-11246",
            "tier": "middle",
            "t": "Johnson’s Executive Order 11246 (1965) required federal contractors to act against job discrimination; a 1967 order added sex",
            "k": ["11246", "1965", "1967"],
            "n": 0
        },
        {
            "id": "grutter",
            "tier": "middle",
            "t": "_Grutter v. Bollinger_ (2003) upheld the University of Michigan Law School’s use of race as one factor, 5–4",
            "k": ["grutter", "michigan law school", "2003"],
            "n": 0
        },
        {
            "id": "oconnor",
            "tier": "middle",
            "t": "Justice Sandra Day O’Connor’s _Grutter_ opinion said she expected such programs to be unnecessary “25 years from now”",
            "k": ["sandra day o’connor", "o’connor", "25 years"],
            "n": 0
        },
        {
            "id": "gratz",
            "tier": "middle",
            "t": "_Gratz v. Bollinger_ (2003) struck down Michigan’s undergraduate point system, which gave minority applicants 20 points",
            "k": ["gratz", "point system", "20 points"],
            "n": 0
        },
        {
            "id": "prop-209",
            "tier": "middle",
            "t": "California’s Proposition 209 (1996) banned racial and sex preferences in state government and public colleges",
            "k": ["proposition 209", "california", "1996"],
            "n": 0
        },
        {
            "id": "powell",
            "tier": "middle",
            "t": "Justice Lewis Powell’s _Bakke_ opinion said a college’s interest in diversity could justify considering race",
            "k": ["lewis powell", "powell", "diversity"],
            "n": 0
        },
        {
            "id": "roberts",
            "tier": "middle",
            "t": "Chief Justice John Roberts wrote the 2023 majority opinion, which said the programs violated the Equal Protection Clause",
            "k": ["john roberts", "equal protection clause"],
            "n": 0
        },
        {
            "id": "two-sides",
            "tier": "middle",
            "t": "Supporters say it remedies discrimination and builds diversity; opponents say it treats people unequally by race or sex",
            "k": ["supporters", "opponents", "unequally"],
            "n": 0
        },
        {
            "id": "committee",
            "tier": "power",
            "t": "Kennedy’s 1961 order created a committee on equal job opportunity led by Vice President Lyndon Johnson",
            "k": ["committee", "vice president"],
            "n": 0
        },
        {
            "id": "howard-speech",
            "tier": "power",
            "t": "Johnson’s 1965 Howard University speech compared freedom alone to bringing someone to the starting line of a race",
            "k": ["howard university", "starting line"],
            "n": 0
        },
        {
            "id": "philadelphia-plan",
            "tier": "power",
            "t": "Nixon’s Philadelphia Plan (1969) set hiring goals and timetables for minority construction workers",
            "k": ["philadelphia plan", "goals and timetables", "nixon"],
            "n": 0
        },
        {
            "id": "weber-fullilove",
            "tier": "power",
            "t": "_United Steelworkers v. Weber_ (1979) upheld a Kaiser Aluminum training program; _Fullilove v. Klutznick_ (1980) upheld federal set-asides for minority-owned businesses",
            "k": ["weber", "kaiser aluminum", "fullilove", "set-asides"],
            "n": 0
        },
        {
            "id": "croson",
            "tier": "power",
            "t": "_City of Richmond v. J.A. Croson Co._ (1989) struck down Richmond’s 30 percent contracting set-aside",
            "k": ["croson", "richmond", "30 percent"],
            "n": 0
        },
        {
            "id": "adarand",
            "tier": "power",
            "t": "_Adarand Constructors v. Peña_ (1995): federal programs that use race must pass “strict scrutiny”",
            "k": ["adarand", "strict scrutiny"],
            "n": 0
        },
        {
            "id": "connerly",
            "tier": "power",
            "t": "Ward Connerly led the Proposition 209 campaign; in 2020 California voters rejected Proposition 16, which would have repealed it",
            "k": ["ward connerly", "connerly", "proposition 16"],
            "n": 0
        },
        {
            "id": "hopwood-fisher",
            "tier": "power",
            "t": "After _Hopwood v. Texas_ (1996), Texas created its Top Ten Percent Plan; _Fisher v. University of Texas_ (2016) upheld UT’s program 4–3",
            "k": ["hopwood", "top ten percent", "fisher"],
            "n": 0
        },
        {
            "id": "schuette",
            "tier": "power",
            "t": "Michigan’s Proposal 2 (2006) banned racial and sex preferences; the Supreme Court upheld it in a 2014 case named for Bill Schuette",
            "k": ["proposal 2", "schuette", "2014"],
            "n": 0
        },
        {
            "id": "blum-jackson",
            "tier": "power",
            "t": "Edward Blum founded Students for Fair Admissions; Justice Ketanji Brown Jackson sat out the Harvard case",
            "k": ["edward blum", "blum", "ketanji brown jackson"],
            "n": 0
        },
        {
            "id": "essay",
            "tier": "power",
            "t": "The 2023 ruling still let colleges consider an applicant’s essay about how race affected his or her life; a footnote set aside the military academies",
            "k": ["essay", "military academies"],
            "n": 0
        },
        {
            "id": "eo-14173",
            "tier": "power",
            "t": "In January 2025, President Donald Trump revoked Executive Order 11246",
            "k": ["january 2025", "revoked"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Policy, not a law or clause",
        "body": "Tossups on this policy mention several related answer lines. The Civil Rights Act of 1964 banned discrimination in jobs and public places, the Equal Protection Clause of the 14th Amendment is the part of the Constitution courts used to judge these programs, and _Brown v. Board of Education_ (1954) ended legal school segregation. Naming one of them is wrong when the question asks for “this policy.”",
        "fix": "Executive Orders 10925 and 11246, _Bakke_, _Gratz_, _Grutter_, Proposition 209, and _Students for Fair Admissions_ all point to affirmative action. If the question asks for “this clause,” say Equal Protection; if it asks for “this law” from 1964, say the Civil Rights Act.",
        "line": "Real answer line: <b><u>affirmative action</u></b> (prompt on descriptions like <u>race-conscious admissions</u>)"
    },
    "tests": {
        "right": [
            "affirmative action",
            "Affirmative Action programs",
            "affirmitive action",
            "affirmative-action policy"
        ],
        "prompt": [
            "race-conscious admissions",
            "racial preferences",
            "affirmative"
        ],
        "wrong": [
            "Equal Protection Clause",
            "Civil Rights Act of 1964",
            "Title IX",
            "Equal Rights Amendment",
            "desegregation",
            "Brown v. Board of Education",
            "Executive Order 9066",
            "Jim Crow laws"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("wrote", data["id"])
