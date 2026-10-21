import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "elizabeth-warren",
    "name": "Elizabeth Warren",
    "mono": "EW",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "U.S. senator from Massachusetts, first elected 2012 · Ran for president in 2020",
    "dates": "Born 1949; elected to the Senate in 2012",
    "briefing": "Elizabeth Warren grew up in Oklahoma, won a college scholarship for debate, and became a law professor who studied why families go bankrupt, eventually teaching at Harvard Law School. In 2007 she proposed a new government agency to oversee loans, credit cards, and other financial products, an idea that became the Consumer Financial Protection Bureau. In 2012 she became the first woman elected to the U.S. Senate from Massachusetts, and she ran for president in 2020.",
    "answerHtml": "Elizabeth <b><u>Warren</u></b> (accept Elizabeth Ann <b><u>Warren</u></b> or Elizabeth Ann <u>Herring</u>; prompt on <u>Elizabeth</u>; do not accept “Earl Warren”)",
    "accept": [
        "elizabeth warren",
        "warren",
        "elizabeth ann warren",
        "elizabeth a warren",
        "senator warren",
        "senator elizabeth warren",
        "liz warren",
        "elizabeth herring",
        "elizabeth ann herring"
    ],
    "prompt": [
        "elizabeth",
        "liz"
    ],
    "reject": [
        "earl warren",
        "chief justice warren",
        "justice warren",
        "warren court",
        "warren commission",
        "robert penn warren",
        "mercy otis warren",
        "mercy warren",
        "joseph warren",
        "warren harding",
        "warren g harding",
        "warren burger",
        "warren e burger",
        "warren buffett",
        "warren christopher",
        "warren hastings",
        "rick warren",
        "jim warren",
        "amelia warren tyagi",
        "elizabeth i",
        "elizabeth ii",
        "queen elizabeth",
        "elizabeth cady stanton",
        "bernie sanders",
        "scott brown",
        "ted kennedy",
        "edward kennedy",
        "richard cordray",
        "consumer financial protection bureau",
        "cfpb"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Elizabeth_Warren",
    "qb": {
        "q": "Elizabeth Warren",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "With her daughter, this law professor wrote _The Two-Income Trap_, a 2003 book about why many middle-class families with two working parents were going broke. Years earlier, she had helped write a book-length study of Americans who filed for bankruptcy.",
            "r": "She later won a U.S. Senate seat in Massachusetts in 2012. For 10 points, name this senator who ran for president in 2020."
        },
        {
            "p": "In a 2007 article titled “Unsafe at Any Rate,” this law professor argued that loans and credit cards should be checked for safety, just as toasters are, by a new government agency. That idea was written into the Dodd–Frank Act of 2010.",
            "r": "The agency became the Consumer Financial Protection Bureau. For 10 points, name this Massachusetts senator, first elected in 2012."
        },
        {
            "p": "In February 2017, the Senate voted to stop this senator from speaking during a debate over Jeff Sessions’s nomination for attorney general, after she read aloud a 1986 letter by Coretta Scott King. Majority Leader Mitch McConnell explained, “She was warned. She was given an explanation.”",
            "r": "His next words, “Nevertheless, she persisted,” became a popular slogan. For 10 points, name this senator from Massachusetts."
        },
        {
            "p": "After the 2008 financial crisis, this law professor chaired a Congressional Oversight Panel that kept watch on the Troubled Asset Relief Program, the government’s rescue of the banks. In 2010 and 2011, she worked for President Barack Obama setting up a new consumer agency.",
            "r": "For 10 points, name this woman who first proposed the Consumer Financial Protection Bureau and later became a senator from Massachusetts."
        },
        {
            "p": "Born in Oklahoma City, this future politician won a debate scholarship to George Washington University at age 16. She left college to get married and later finished a degree in speech pathology at the University of Houston.",
            "r": "She went on to teach law at Harvard. For 10 points, name this Massachusetts senator who ran for president in 2020."
        },
        {
            "p": "This expert on bankruptcy law taught at the University of Texas and the University of Pennsylvania before joining the faculty of Harvard Law School in the 1990s. She had earned her own law degree at Rutgers in 1976.",
            "r": "For 10 points, name this law professor who later became a Democratic senator from Massachusetts."
        },
        {
            "p": "In 2012, this candidate defeated Republican Scott Brown, who had won a 2010 special election for the Senate seat long held by Ted Kennedy. That win made her the first woman elected to the U.S. Senate from her state.",
            "r": "For 10 points, name this Democrat from Massachusetts who later ran for president in 2020."
        },
        {
            "p": "This candidate launched a 2019 presidential campaign at a mill in Lawrence, Massachusetts, where textile workers had gone on strike in 1912 in the “Bread and Roses” strike. Her campaign became known for the phrase “I have a plan for that.”",
            "r": "She ended that campaign in March 2020. For 10 points, name this senator from Massachusetts."
        },
        {
            "p": "This future senator was registered as a Republican until 1996 and has said she once thought that party best supported free markets. Her research on families in debt later led her to call for stronger rules on lenders.",
            "r": "For 10 points, name this Democratic senator from Massachusetts, a former Harvard law professor."
        },
        {
            "p": "This politician wrote the memoir _A Fighting Chance_ in 2014 and titled a 2021 book _Persist_, after words used about her on the Senate floor. Her other books include _This Fight Is Our Fight_.",
            "r": "For 10 points, name this Massachusetts senator who first proposed the idea for the Consumer Financial Protection Bureau."
        },
        {
            "p": "In 2011, Barack Obama picked Richard Cordray, not this official, to be the first director of a new agency she had spent a year setting up. Two months later, she announced that she would run for the U.S. Senate.",
            "r": "That agency is the Consumer Financial Protection Bureau. For 10 points, name this senator first elected in 2012."
        },
        {
            "p": "Before going to law school, this woman taught children with disabilities at a public school in New Jersey, using her training in speech pathology. She later spent decades teaching and writing about bankruptcy law.",
            "r": "For 10 points, name this Harvard law professor who became a senator from Massachusetts in 2013."
        },
        {
            "p": "This senator was reelected in 2018 over Geoff Diehl and in 2024 over John Deaton, both Republicans. Before entering politics, she had spent more than thirty years as a law professor, much of that time studying bankruptcy.",
            "r": "For 10 points, name this Democratic senator from Massachusetts who taught at Harvard Law School."
        },
        {
            "p": "While this future politician was growing up in Oklahoma, her father had a heart attack, and her mother took a minimum-wage job at Sears to help keep the family’s house. She has often told that story when talking about working families.",
            "r": "She later became a law professor at Harvard. For 10 points, name this senator from Massachusetts."
        },
        {
            "p": "During the 2020 race, this candidate proposed a yearly “two-cent” tax on each dollar of a household’s wealth above $50 million, and crowds at her rallies chanted “Two cents!” She also posed for photos with voters in long “selfie lines.”",
            "r": "For 10 points, name this Massachusetts senator who ended her presidential campaign in March 2020."
        }
    ],
    "clues": [
        {
            "id": "ma-senator",
            "tier": "giveaway",
            "t": "Democratic U.S. senator from Massachusetts, first elected in 2012; the first woman elected to the Senate from that state",
            "k": ["massachusetts", "senator", "2012", "first woman"],
            "n": 0,
            "rabbit": "Massachusetts"
        },
        {
            "id": "cfpb",
            "tier": "giveaway",
            "t": "First proposed the idea for the Consumer Financial Protection Bureau (CFPB), created by the Dodd–Frank Act of 2010",
            "k": ["consumer financial protection bureau", "cfpb", "2010"],
            "n": 0
        },
        {
            "id": "harvard",
            "tier": "giveaway",
            "t": "A Harvard Law School professor and an expert on bankruptcy law",
            "k": ["harvard", "bankruptcy", "law school"],
            "n": 0
        },
        {
            "id": "campaign-2020",
            "tier": "giveaway",
            "t": "Ran for the 2020 Democratic presidential nomination and ended her campaign in March 2020",
            "k": ["2020", "presidential nomination", "march 2020"],
            "n": 0
        },
        {
            "id": "persisted",
            "tier": "giveaway",
            "t": "“Nevertheless, she persisted”: Mitch McConnell’s words after the Senate voted to stop her from speaking in a 2017 debate",
            "k": ["nevertheless", "persisted", "mcconnell"],
            "n": 0
        },
        {
            "id": "scott-brown",
            "tier": "middle",
            "t": "Defeated Republican senator Scott Brown in 2012, winning the seat Ted Kennedy had held for decades",
            "k": ["scott brown", "ted kennedy"],
            "n": 0
        },
        {
            "id": "coretta",
            "tier": "middle",
            "t": "In 2017 she read a 1986 letter by Coretta Scott King opposing Jeff Sessions, who had been nominated for attorney general",
            "k": ["coretta scott king", "jeff sessions", "1986"],
            "n": 0
        },
        {
            "id": "unsafe",
            "tier": "middle",
            "t": "Her 2007 article “Unsafe at Any Rate” said loans and credit cards should be checked for safety, like toasters",
            "k": ["unsafe at any rate", "toasters", "2007"],
            "n": 0
        },
        {
            "id": "oklahoma",
            "tier": "middle",
            "t": "Born in Oklahoma City (1949); won a debate scholarship to George Washington University at 16",
            "k": ["oklahoma", "debate", "george washington university"],
            "n": 0
        },
        {
            "id": "two-income",
            "tier": "middle",
            "t": "Wrote _The Two-Income Trap_ (2003) with her daughter, about why middle-class families were going broke",
            "k": ["two-income trap", "daughter", "middle-class"],
            "n": 0
        },
        {
            "id": "oversight",
            "tier": "middle",
            "t": "Chaired the Congressional Oversight Panel that watched the bank rescue (TARP) after the 2008 financial crisis",
            "k": ["oversight panel", "tarp", "2008"],
            "n": 0
        },
        {
            "id": "lawrence",
            "tier": "middle",
            "t": "Launched her 2019 presidential campaign in Lawrence, Massachusetts, site of the 1912 “Bread and Roses” strike",
            "k": ["lawrence", "bread and roses", "1912"],
            "n": 0
        },
        {
            "id": "plan",
            "tier": "middle",
            "t": "Her 2020 campaign became known for the phrase “I have a plan for that”",
            "k": ["plan for that"],
            "n": 0
        },
        {
            "id": "cordray",
            "tier": "power",
            "t": "Barack Obama chose Richard Cordray, not her, as the CFPB’s first director (2011); she then ran for the Senate",
            "k": ["cordray", "first director"],
            "n": 0
        },
        {
            "id": "houston",
            "tier": "power",
            "t": "Left college to marry, then finished a speech pathology degree at the University of Houston",
            "k": ["university of houston", "speech pathology"],
            "n": 0
        },
        {
            "id": "rutgers",
            "tier": "power",
            "t": "Taught children with disabilities at a New Jersey public school, then earned a law degree at Rutgers (1976)",
            "k": ["rutgers", "disabilities", "1976"],
            "n": 0
        },
        {
            "id": "texas-penn",
            "tier": "power",
            "t": "Taught law at the University of Texas and the University of Pennsylvania before moving to Harvard",
            "k": ["university of texas", "university of pennsylvania"],
            "n": 0
        },
        {
            "id": "republican",
            "tier": "power",
            "t": "Was registered as a Republican until 1996",
            "k": ["republican", "1996"],
            "n": 0
        },
        {
            "id": "books",
            "tier": "power",
            "t": "Books: _A Fighting Chance_ (2014), _This Fight Is Our Fight_ (2017), and _Persist_ (2021)",
            "k": ["a fighting chance", "this fight is our fight", "persist"],
            "n": 0
        },
        {
            "id": "sears",
            "tier": "power",
            "t": "While she was growing up in Oklahoma, her father had a heart attack and her mother took a minimum-wage job at Sears",
            "k": ["sears", "heart attack", "minimum-wage"],
            "n": 0
        },
        {
            "id": "reelected",
            "tier": "power",
            "t": "Reelected in 2018 (over Geoff Diehl) and 2024 (over John Deaton)",
            "k": ["reelected", "geoff diehl", "john deaton"],
            "n": 0
        },
        {
            "id": "two-cents",
            "tier": "power",
            "t": "Proposed a yearly “two-cent” tax on wealth above $50 million; posed for photos with voters in long “selfie lines”",
            "k": ["two-cent", "wealth", "selfie lines"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Which Warren?",
        "body": "Several famous Warrens appear in quiz bowl. Earl Warren was the Chief Justice whose court decided _Brown v. Board of Education_, Robert Penn Warren wrote the novel _All the King’s Men_, and Mercy Otis Warren wrote plays and a history of the American Revolution. Bernie Sanders also ran for the 2020 Democratic nomination, so campaign clues can fit either senator.",
        "fix": "Massachusetts, Harvard Law, bankruptcy research, the Consumer Financial Protection Bureau, and “Nevertheless, she persisted” mean Elizabeth Warren. Vermont and Burlington mean Sanders. “Warren” alone is enough on this answer line, but if you add a first name, it must be “Elizabeth.”",
        "line": "Real answer line: Elizabeth <b><u>Warren</u></b> (accept Elizabeth Ann <b><u>Warren</u></b>; prompt on <u>Elizabeth</u>)"
    },
    "tests": {
        "right": [
            "Elizabeth Warren",
            "Warren",
            "Senator Warren",
            "Elizabeth Ann Warren",
            "Elizabeth Waren"
        ],
        "prompt": [
            "Elizabeth"
        ],
        "wrong": [
            "Earl Warren",
            "Bernie Sanders",
            "Robert Penn Warren",
            "Chief Justice Warren",
            "Elizabeth I",
            "Mercy Otis Warren",
            "Scott Brown"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
