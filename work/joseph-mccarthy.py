import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TIP = "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."

data = {
    "id": "joseph-mccarthy",
    "name": "Joseph McCarthy",
    "mono": "JM",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "Wisconsin senator of the Red Scare · Gave his name to McCarthyism",
    "dates": "1908–1957",
    "briefing": "In 1950, a little-known Wisconsin senator named Joseph McCarthy announced that he had a list of communists working in the State Department. For four years he made headlines with accusations he often could not prove, and his name became a word: McCarthyism. In 1954, televised hearings about the Army and a broadcast by journalist Edward R. Murrow hurt his popularity, and the Senate voted to condemn him.",
    "answerHtml": "Joseph <b><u>McCarthy</u></b> (accept Joe <u>McCarthy</u>; do not accept “Eugene McCarthy”)",
    "accept": [
        "joseph mccarthy",
        "joe mccarthy",
        "mccarthy",
        "senator mccarthy",
        "senator joseph mccarthy",
        "joseph r mccarthy",
        "joseph raymond mccarthy"
    ],
    "prompt": [],
    "reject": [
        "eugene mccarthy",
        "gene mccarthy",
        "john mccarthy",
        "cormac mccarthy",
        "kevin mccarthy",
        "melissa mccarthy",
        "mccartney",
        "paul mccartney",
        "mccarthyism",
        "douglas macarthur",
        "macarthur",
        "richard nixon",
        "nixon",
        "roy cohn",
        "cohn",
        "g david schine",
        "schine",
        "joseph welch",
        "welch",
        "edward r murrow",
        "murrow",
        "huac",
        "house un american activities committee",
        "house committee on un american activities",
        "j edgar hoover",
        "hoover",
        "robert la follette",
        "la follette",
        "margaret chase smith",
        "millard tydings",
        "alger hiss",
        "whittaker chambers",
        "julius rosenberg",
        "ethel rosenberg",
        "rosenberg",
        "joseph stalin",
        "stalin",
        "red scare",
        "second red scare",
        "robert f kennedy",
        "dwight d eisenhower",
        "eisenhower",
        "arthur miller"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Joseph_McCarthy",
    "qb": {
        "q": "McCarthy",
        "found": 0,
        "tip": TIP
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "Senator Margaret Chase Smith of Maine and six other Republican senators issued a “Declaration of Conscience” in 1950 criticizing this man’s tactics, though Smith never mentioned him by name. Months earlier, this man had claimed in Wheeling, West Virginia, to have a list of communists working in the State Department.",
            "r": "For 10 points, name this Wisconsin senator whose name became a word for reckless accusations of disloyalty."
        },
        {
            "p": "A Senate subcommittee led by Millard Tydings of Maryland called this man’s charges against the State Department “a fraud and a hoax,” and this man then campaigned against Tydings, who lost his reelection race in 1950.",
            "r": "For 10 points, name this Wisconsin Republican who led a hunt for communists in the federal government in the early 1950s."
        },
        {
            "p": "In 1946, this former Wisconsin circuit judge upset Senator Robert La Follette Jr. in a Republican primary, campaigning as “Tail Gunner Joe” based on his service in the Marine Corps during World War II.",
            "r": "He later chaired a Senate subcommittee that investigated suspected communists. For 10 points, name this senator from Wisconsin."
        },
        {
            "p": "In a long 1951 Senate speech, this man accused former Secretary of State George Marshall of taking part in a vast conspiracy, and Dwight Eisenhower later dropped a passage praising Marshall from a 1952 campaign speech in this man’s home state.",
            "r": "For 10 points, name this senator from Wisconsin who led an anticommunist crusade in the early 1950s."
        },
        {
            "p": "This man’s chief counsel, Roy Cohn, was accused of seeking special treatment for G. David Schine, a former consultant to this man’s subcommittee who had been drafted into the Army. Those charges led to weeks of nationally televised hearings in 1954.",
            "r": "For 10 points, name this Wisconsin senator, a leading figure of the Second Red Scare in the early 1950s."
        },
        {
            "p": "During a 1954 hearing, this man revealed that Fred Fisher, a young lawyer at Joseph Welch’s Boston law firm, had once belonged to the National Lawyers Guild. Welch then asked him, “Have you no sense of decency, sir, at long last?”",
            "r": "For 10 points, name this Wisconsin senator who was censured by the Senate later that year."
        },
        {
            "p": "Edward R. Murrow devoted a 1954 episode of his CBS program _See It Now_ to criticizing this man, mostly by showing clips of this man’s own speeches. A 2005 film about that broadcast took its title from Murrow’s sign-off, “Good night, and good luck.”",
            "r": "For 10 points, name this Wisconsin senator who made sweeping charges of communist influence in the government."
        },
        {
            "p": "Senator Ralph Flanders of Vermont introduced a resolution against this man, and a special committee led by Arthur Watkins of Utah recommended that the Senate condemn him. In December 1954, the Senate voted 67 to 22 to condemn his conduct.",
            "r": "For 10 points, name this Wisconsin Republican who led a crusade against suspected communists."
        },
        {
            "p": "_Washington Post_ cartoonist Herbert Block, known as Herblock, coined a word from this man’s name in a 1950 cartoon that showed a stack of tar barrels. That word came to mean attacking people’s loyalty without solid evidence.",
            "r": "For 10 points, name this senator who claimed in 1950 that communists were working in the State Department."
        },
        {
            "p": "A young Robert F. Kennedy briefly worked as an assistant counsel for a Senate subcommittee chaired by this man, whose chief counsel was Roy Cohn. This man had become chairman of that Permanent Subcommittee on Investigations in 1953, after Republicans won control of the Senate.",
            "r": "For 10 points, name this senator from Wisconsin who led a hunt for suspected communists in the early 1950s."
        },
        {
            "p": "This man demanded to know “Who promoted Peress?” after Irving Peress, an Army dentist accused of communist ties, received a routine promotion and an honorable discharge. This man also investigated the Army Signal Corps laboratories at Fort Monmouth, New Jersey.",
            "r": "Those clashes led to televised hearings about the Army in 1954. For 10 points, name this Wisconsin senator."
        },
        {
            "p": "In 1953, this man’s aides Roy Cohn and G. David Schine toured Europe looking for “subversive” books in American government libraries overseas. That same year, this man held hearings attacking the Voice of America radio service.",
            "r": "For 10 points, name this Wisconsin senator who gave his name to an era of anticommunist accusations."
        },
        {
            "p": "When this man died in 1957 at age 48, Democrat William Proxmire won a special election to fill his Senate seat. Three years earlier, his fellow senators had voted to condemn his conduct.",
            "r": "For 10 points, name this Wisconsin Republican who led the Second Red Scare’s hunt for communists in government."
        },
        {
            "p": "In a Lincoln Day speech to a Republican women’s club in February 1950, this man claimed to have a list of 205 people in the State Department who were members of the Communist Party. He later gave smaller numbers, such as 57.",
            "r": "That speech was given in Wheeling, West Virginia. For 10 points, name this Republican senator from Wisconsin."
        },
        {
            "p": "Arthur Miller’s play _The Crucible_, set during the Salem witch trials, is often read as an allegory for the anticommunist investigations of this man’s era. Miller himself was later questioned by a House committee, not by this senator.",
            "r": "For 10 points, name this Wisconsin senator whose name became a term for making accusations of disloyalty without proof."
        }
    ],
    "clues": [
        {
            "id": "wisconsin-senator",
            "tier": "giveaway",
            "t": "Republican senator from Wisconsin (1947–1957) who led a hunt for communists in the government",
            "k": ["wisconsin", "senator", "communists", "republican"],
            "n": 0
        },
        {
            "id": "red-scare",
            "tier": "giveaway",
            "t": "Leading figure of the Second Red Scare in the early 1950s",
            "k": ["second red scare", "red scare"],
            "n": 0
        },
        {
            "id": "ism",
            "tier": "giveaway",
            "t": "His name became a word for accusing people of disloyalty without good evidence",
            "k": ["disloyalty", "evidence", "accusing"],
            "n": 0
        },
        {
            "id": "wheeling",
            "tier": "middle",
            "t": "Wheeling, West Virginia (February 1950): claimed to have a list of 205 communists in the State Department",
            "k": ["wheeling", "205", "state department"],
            "n": 0
        },
        {
            "id": "army-hearings",
            "tier": "middle",
            "t": "The nationally televised Army hearings of 1954 badly damaged his reputation",
            "k": ["army", "televised", "1954"],
            "n": 0
        },
        {
            "id": "welch",
            "tier": "middle",
            "t": "Army lawyer Joseph Welch asked him, “Have you no sense of decency, sir, at long last?”",
            "k": ["joseph welch", "welch", "sense of decency"],
            "n": 0
        },
        {
            "id": "murrow",
            "tier": "middle",
            "t": "Edward R. Murrow criticized him on CBS’s _See It Now_ (March 1954), signing off “Good night, and good luck”",
            "k": ["murrow", "see it now", "good night"],
            "n": 0
        },
        {
            "id": "censure",
            "tier": "middle",
            "t": "The Senate condemned (censured) him in December 1954 by a vote of 67 to 22",
            "k": ["censured", "condemned", "67 to 22"],
            "n": 0
        },
        {
            "id": "cohn-schine",
            "tier": "middle",
            "t": "His chief counsel was Roy Cohn; charges of special treatment for drafted aide G. David Schine set off the Army hearings",
            "k": ["roy cohn", "cohn", "schine"],
            "n": 0
        },
        {
            "id": "subcommittee",
            "tier": "middle",
            "t": "Chaired the Senate Permanent Subcommittee on Investigations (1953–1954)",
            "k": ["permanent subcommittee", "subcommittee", "investigations"],
            "n": 0
        },
        {
            "id": "crucible",
            "tier": "middle",
            "t": "Arthur Miller’s _The Crucible_ (1953) is often read as an allegory of his era",
            "k": ["crucible", "arthur miller", "salem"],
            "n": 0
        },
        {
            "id": "chase-smith",
            "tier": "power",
            "t": "Margaret Chase Smith of Maine gave the “Declaration of Conscience” speech (1950), criticizing his tactics without naming him",
            "k": ["margaret chase smith", "declaration of conscience", "maine"],
            "n": 0
        },
        {
            "id": "tydings",
            "tier": "power",
            "t": "Millard Tydings’s subcommittee called his charges “a fraud and a hoax”; Tydings lost reelection in 1950",
            "k": ["tydings", "fraud and a hoax", "hoax"],
            "n": 0
        },
        {
            "id": "la-follette",
            "tier": "power",
            "t": "Beat Robert La Follette Jr. in the 1946 Republican primary, campaigning as “Tail Gunner Joe”",
            "k": ["la follette", "tail gunner joe", "1946"],
            "n": 0
        },
        {
            "id": "judge-marine",
            "tier": "power",
            "t": "A former Wisconsin circuit judge who served in the Marine Corps in World War II",
            "k": ["circuit judge", "marine corps", "world war ii"],
            "n": 0
        },
        {
            "id": "marshall",
            "tier": "power",
            "t": "In 1951 he accused George Marshall of taking part in a vast conspiracy; Eisenhower dropped a pro-Marshall passage from a 1952 speech in Wisconsin",
            "k": ["george marshall", "marshall", "1951"],
            "n": 0
        },
        {
            "id": "herblock",
            "tier": "power",
            "t": "Cartoonist Herblock (Herbert Block) coined the word for his tactics in a 1950 _Washington Post_ cartoon",
            "k": ["herblock", "herbert block", "washington post", "cartoon"],
            "n": 0
        },
        {
            "id": "rfk",
            "tier": "power",
            "t": "Robert F. Kennedy briefly worked as an assistant counsel on his subcommittee (1953)",
            "k": ["robert f. kennedy", "kennedy", "assistant counsel"],
            "n": 0,
            "rabbit": "Robert F. Kennedy"
        },
        {
            "id": "fred-fisher",
            "tier": "power",
            "t": "He brought up young lawyer Fred Fisher’s past membership in the National Lawyers Guild just before Welch’s famous rebuke",
            "k": ["fred fisher", "fisher", "national lawyers guild"],
            "n": 0
        },
        {
            "id": "peress",
            "tier": "power",
            "t": "“Who promoted Peress?”: attacked the Army over dentist Irving Peress; investigated Fort Monmouth",
            "k": ["peress", "fort monmouth", "dentist"],
            "n": 0
        },
        {
            "id": "flanders-watkins",
            "tier": "power",
            "t": "Ralph Flanders of Vermont introduced the censure resolution; Arthur Watkins’s committee recommended it",
            "k": ["ralph flanders", "flanders", "watkins"],
            "n": 0
        },
        {
            "id": "voa-libraries",
            "tier": "power",
            "t": "Cohn and Schine toured Europe in 1953 hunting “subversive” books in U.S. libraries; he also attacked the Voice of America",
            "k": ["voice of america", "libraries", "subversive"],
            "n": 0
        },
        {
            "id": "death",
            "tier": "power",
            "t": "Died in 1957 at age 48; Democrat William Proxmire won his Senate seat",
            "k": ["proxmire", "1957", "48"],
            "n": 0
        },
        {
            "id": "wheeling-details",
            "tier": "power",
            "t": "Gave the Wheeling speech to a Republican women’s club on a Lincoln Day tour; he later gave smaller numbers, such as 57",
            "k": ["lincoln day", "women’s club", "57"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Senator, not HUAC",
        "body": "Joseph McCarthy was a senator, so he never served on the House Un-American Activities Committee (HUAC), which held the 1947 Hollywood hearings (the “Hollywood Ten”) and the Alger Hiss case that made Richard Nixon famous. Some tossups about the whole era want “McCarthyism” or the “Red Scare,” not the man. Eugene McCarthy, a Minnesota senator who ran for president in 1968, is a different person.",
        "fix": "Hollywood blacklists, the Hollywood Ten, and Alger Hiss point to HUAC. Wheeling, the 1954 Army hearings, Joseph Welch, Edward R. Murrow, and the 1954 censure point to Joseph McCarthy. Listen for “this senator” versus “this committee,” “this era,” or “this term.”",
        "line": "Real answer line: Joseph <b><u>McCarthy</u></b> (accept Joe <u>McCarthy</u>; do not accept “Eugene McCarthy”)"
    },
    "tests": {
        "right": [
            "Joseph McCarthy",
            "McCarthy",
            "Joe McCarthy",
            "Senator McCarthy",
            "McCarty",
            "Joseph McCarthey"
        ],
        "prompt": [],
        "wrong": [
            "Eugene McCarthy",
            "McCarthyism",
            "Richard Nixon",
            "Roy Cohn",
            "Douglas MacArthur",
            "HUAC",
            "Joseph Welch"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
