import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "j-edgar-hoover",
    "name": "J. Edgar Hoover",
    "mono": "JEH",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "Director of the FBI for 48 years · Led it from 1924 until his death in 1972",
    "dates": "1895–1972",
    "briefing": "J. Edgar Hoover took over the federal Bureau of Investigation in 1924, when he was just 29, and ran it until he died in 1972, serving under eight presidents. He built a national fingerprint file and a crime lab, and his “G-men” hunted gangsters like John Dillinger in the 1930s. Later investigations revealed that his FBI had also secretly spied on and tried to disrupt political groups and leaders, including Martin Luther King Jr.",
    "answerHtml": "<b><u>J. Edgar Hoover</u></b> (or <b><u>John Edgar Hoover</u></b>; prompt on <u>Hoover</u> alone; do not accept “Herbert Hoover”)",
    "accept": [
        "j edgar hoover",
        "john edgar hoover",
        "edgar hoover",
        "j edgar",
        "jedgar hoover",
        "fbi director hoover",
        "director j edgar hoover"
    ],
    "prompt": [
        "hoover",
        "director hoover",
        "mr hoover"
    ],
    "reject": [
        "herbert hoover",
        "herbert clark hoover",
        "president hoover",
        "hoover dam",
        "hoovervilles",
        "hooverville",
        "hoover institution",
        "hoover commission",
        "hoover moratorium",
        "lou henry hoover",
        "federal bureau of investigation",
        "fbi",
        "clyde tolson",
        "mark felt",
        "w mark felt",
        "l patrick gray",
        "clarence kelley",
        "william webster",
        "robert mueller",
        "james comey",
        "melvin purvis",
        "eliot ness",
        "a mitchell palmer",
        "mitchell palmer",
        "charles bonaparte",
        "harlan fiske stone",
        "joseph mccarthy",
        "john dillinger",
        "allen dulles"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/J._Edgar_Hoover",
    "qb": {
        "q": "J. Edgar Hoover",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "In 1919, this young Justice Department lawyer was put in charge of a new General Intelligence Division, which gathered files on suspected radicals and helped plan the Palmer Raids. He also handled the case that led to the deportation of the anarchist Emma Goldman.",
            "r": "For 10 points, name this man who led the FBI from 1924 until his death in 1972."
        },
        {
            "p": "While earning law degrees at night from George Washington University, this future official worked as a clerk at the Library of Congress, where he learned how to catalog and index information. He was born in Washington, D.C., on New Year’s Day in 1895.",
            "r": "For 10 points, name this man who became director of the Bureau of Investigation, later the FBI, in 1924."
        },
        {
            "p": "Attorney General Harlan Fiske Stone, who later became Chief Justice, chose this 29-year-old to clean up a federal agency in 1924 after scandals in the Harding administration. This man fired agents he considered unqualified and required new agents to have training in law or accounting.",
            "r": "For 10 points, name this man who ran the Bureau of Investigation and the FBI from 1924 to 1972."
        },
        {
            "p": "According to a popular story, the gangster George “Machine Gun” Kelly gave this man’s agents a famous nickname when he was arrested in Memphis in 1933. Two years later, a James Cagney film about those agents helped make them national heroes.",
            "r": "That nickname was “G-men.” For 10 points, name this director of the FBI from 1924 to 1972."
        },
        {
            "p": "This official’s agents, led in Chicago by Melvin Purvis, tracked down the bank robber John Dillinger outside the Biograph Theater in July 1934. This official reportedly resented the fame Purvis won, and Purvis soon left the bureau.",
            "r": "Dillinger had been called “Public Enemy Number One.” For 10 points, name this longtime director of the FBI, who served from 1924 to 1972."
        },
        {
            "p": "After Senator Kenneth McKellar criticized this official for never having arrested anyone himself, he flew to New Orleans in 1936 to take part in the arrest of the gangster Alvin Karpis, a leader of the Barker gang.",
            "r": "For 10 points, name this director who led the FBI for 48 years, until his death in 1972."
        },
        {
            "p": "Under this director, the bureau set up a national fingerprint collection in 1924 and a crime laboratory in 1932, its National Academy began training local police leaders in 1935, and in 1950 it began publishing its “Ten Most Wanted Fugitives” list.",
            "r": "For 10 points, name this man who led the Federal Bureau of Investigation from 1924 until 1972."
        },
        {
            "p": "In 1971, activists who broke into an office in Media, Pennsylvania, leaked files revealing COINTELPRO, a secret program run under this official. Its targets included the Communist Party, civil rights and antiwar groups, and the Ku Klux Klan.",
            "r": "A Senate committee led by Frank Church later investigated it. For 10 points, name this director of the FBI from 1924 to 1972."
        },
        {
            "p": "In 1963, Attorney General Robert Kennedy approved this official’s request to wiretap Martin Luther King Jr., and the next year this official publicly called King “the most notorious liar in the country.” King had publicly criticized the bureau’s work in the South.",
            "r": "For 10 points, name this man who ran the FBI from 1924 until his death in 1972."
        },
        {
            "p": "This official’s 1958 book _Masters of Deceit_ warned Americans about communism, and in 1947 he told the House Un-American Activities Committee that the Communist Party was a threat to the nation. His agents arrested Julius Rosenberg in 1950 on charges of spying for the Soviet Union.",
            "r": "For 10 points, name this longtime FBI director who served from 1924 to 1972."
        },
        {
            "p": "When this official died in May 1972, he became the first civil servant to lie in state in the Capitol Rotunda, and Richard Nixon gave the eulogy at his funeral. Congress later limited future holders of his job to a single ten-year term.",
            "r": "For 10 points, name this man who led the FBI and the bureau before it for 48 years."
        },
        {
            "p": "After this man’s death, one of his top officials, Mark Felt, was passed over for the top job; Felt then secretly helped two _Washington Post_ reporters uncover the Watergate scandal as “Deep Throat.” Felt revealed his secret role in 2005.",
            "r": "For 10 points, name this man who directed the FBI from 1924 until his death in 1972."
        },
        {
            "p": "Leonardo DiCaprio played this man in a 2011 film directed by Clint Eastwood. A building on Pennsylvania Avenue in Washington, D.C., completed in the 1970s, was named for this man, who had led its agency for almost half a century.",
            "r": "For 10 points, name this man who led the FBI from 1924 to 1972."
        },
        {
            "p": "After the 1932 kidnapping of Charles Lindbergh’s baby son, Congress passed a law letting this man’s agents pursue kidnappers across state lines, and in 1934 it gave those agents general power to carry guns and make arrests.",
            "r": "For 10 points, name this director who built the FBI into a powerful national agency between 1924 and 1972."
        },
        {
            "p": "After this official died in 1972, his longtime secretary, Helen Gandy, destroyed many of his private files, as he had instructed. Some of his surviving “Official and Confidential” files held information about politicians and celebrities.",
            "r": "For 10 points, name this man who served as director of the FBI for 48 years."
        }
    ],
    "clues": [
        {
            "id": "fbi-director",
            "tier": "giveaway",
            "t": "Director of the FBI (called the Bureau of Investigation until 1935) from 1924 until his death in 1972",
            "k": ["fbi", "bureau of investigation", "1924", "director"],
            "n": 0,
            "rabbit": "Federal Bureau of Investigation"
        },
        {
            "id": "48-years",
            "tier": "giveaway",
            "t": "Led the bureau for 48 years, under eight presidents from Calvin Coolidge to Richard Nixon",
            "k": ["48 years", "eight presidents"],
            "n": 0
        },
        {
            "id": "g-men",
            "tier": "giveaway",
            "t": "His agents were nicknamed “G-men,” short for “government men”",
            "k": ["g-men", "government men"],
            "n": 0
        },
        {
            "id": "palmer-raids",
            "tier": "middle",
            "t": "Headed the Justice Department’s General Intelligence Division (1919) and helped plan the Palmer Raids against suspected radicals",
            "k": ["general intelligence division", "palmer raids", "1919"],
            "n": 0
        },
        {
            "id": "dillinger",
            "tier": "middle",
            "t": "Agents led by Melvin Purvis tracked down John Dillinger, “Public Enemy Number One,” at Chicago’s Biograph Theater (1934)",
            "k": ["dillinger", "purvis", "biograph", "public enemy"],
            "n": 0
        },
        {
            "id": "cointelpro",
            "tier": "middle",
            "t": "COINTELPRO (1956–1971): secret programs that spied on and disrupted political groups, revealed by a 1971 break-in at Media, Pennsylvania",
            "k": ["cointelpro", "media, pennsylvania"],
            "n": 0
        },
        {
            "id": "king",
            "tier": "middle",
            "t": "Wiretapped Martin Luther King Jr. with Robert Kennedy’s approval (1963); called King “the most notorious liar in the country” (1964)",
            "k": ["martin luther king", "wiretapped", "robert kennedy"],
            "n": 0,
            "rabbit": "Martin Luther King Jr."
        },
        {
            "id": "crime-lab",
            "tier": "middle",
            "t": "Built a national fingerprint file (1924) and a crime laboratory (1932); the Ten Most Wanted list began in 1950",
            "k": ["fingerprint", "crime laboratory", "ten most wanted"],
            "n": 0
        },
        {
            "id": "headquarters",
            "tier": "middle",
            "t": "The FBI headquarters building on Pennsylvania Avenue in Washington, D.C., was named for him",
            "k": ["headquarters", "pennsylvania avenue"],
            "n": 0
        },
        {
            "id": "anticommunist",
            "tier": "middle",
            "t": "A fierce anticommunist: wrote _Masters of Deceit_ (1958), testified to HUAC (1947), and his agents arrested Julius Rosenberg (1950)",
            "k": ["masters of deceit", "anticommunist", "rosenberg"],
            "n": 0
        },
        {
            "id": "library",
            "tier": "power",
            "t": "Born in Washington, D.C. (1895); worked at the Library of Congress while studying law at night at George Washington University",
            "k": ["library of congress", "george washington university"],
            "n": 0
        },
        {
            "id": "goldman",
            "tier": "power",
            "t": "Handled the case that led to the deportation of the anarchist Emma Goldman (1919)",
            "k": ["emma goldman", "goldman", "deportation"],
            "n": 0
        },
        {
            "id": "stone",
            "tier": "power",
            "t": "Attorney General Harlan Fiske Stone chose him in 1924, at age 29, to clean up the bureau after Harding-era scandals",
            "k": ["harlan fiske stone", "stone", "harding"],
            "n": 0
        },
        {
            "id": "kelly",
            "tier": "power",
            "t": "Popular story: “Machine Gun” Kelly coined “G-men” at his 1933 arrest in Memphis; James Cagney starred in _G Men_ (1935)",
            "k": ["machine gun", "memphis", "cagney"],
            "n": 0
        },
        {
            "id": "karpis",
            "tier": "power",
            "t": "Joined the 1936 arrest of Alvin Karpis in New Orleans after Senator Kenneth McKellar said he had never arrested anyone",
            "k": ["karpis", "mckellar", "new orleans"],
            "n": 0
        },
        {
            "id": "lindbergh",
            "tier": "power",
            "t": "The Lindbergh kidnapping (1932) led to a federal kidnapping law; in 1934 agents got general power to carry guns and make arrests",
            "k": ["lindbergh", "kidnapping", "1934"],
            "n": 0
        },
        {
            "id": "church",
            "tier": "power",
            "t": "A Senate committee led by Frank Church investigated the bureau’s secret programs (1975–1976)",
            "k": ["frank church", "senate committee"],
            "n": 0
        },
        {
            "id": "lie-in-state",
            "tier": "power",
            "t": "First civil servant to lie in state in the Capitol Rotunda (1972); Richard Nixon gave his eulogy",
            "k": ["lie in state", "rotunda", "eulogy"],
            "n": 0
        },
        {
            "id": "ten-year-term",
            "tier": "power",
            "t": "After his death, Congress limited FBI directors to a single ten-year term (1976)",
            "k": ["ten-year term", "1976"],
            "n": 0
        },
        {
            "id": "felt",
            "tier": "power",
            "t": "Mark Felt, passed over to succeed him, became “Deep Throat,” the secret Watergate source",
            "k": ["mark felt", "deep throat", "watergate"],
            "n": 0
        },
        {
            "id": "gandy",
            "tier": "power",
            "t": "His secretary Helen Gandy destroyed many of his private files after his death; others were labeled “Official and Confidential”",
            "k": ["helen gandy", "official and confidential", "files"],
            "n": 0
        },
        {
            "id": "tolson",
            "tier": "power",
            "t": "Clyde Tolson was his closest aide and the bureau’s associate director for more than 40 years",
            "k": ["clyde tolson", "tolson", "associate director"],
            "n": 0
        },
        {
            "id": "dicaprio",
            "tier": "power",
            "t": "Leonardo DiCaprio played him in Clint Eastwood’s 2011 film",
            "k": ["dicaprio", "clint eastwood", "2011"],
            "n": 0
        }
    ],
    "trap": {
        "title": "J. Edgar, not Herbert",
        "body": "Two famous Hoovers worked in Washington at the same time, and they were not related. Herbert Hoover was the 31st president (1929–1933), remembered for the Great Depression, “Hoovervilles,” and the Hoover Dam; J. Edgar Hoover ran the FBI from 1924 to 1972. Saying only “Hoover” earns a prompt, and answering “Herbert Hoover” is wrong.",
        "fix": "G-men, gangsters, fingerprints, COINTELPRO, the Palmer Raids, and the FBI mean J. Edgar. The presidency, the 1929 stock market crash, the Bonus Army, and the Reconstruction Finance Corporation mean Herbert. When prompted, say “J. Edgar Hoover.”",
        "line": "Real answer line: <b><u>J. Edgar Hoover</u></b> (or <b><u>John Edgar Hoover</u></b>; prompt on <u>Hoover</u>; do not accept “Herbert Hoover”)"
    },
    "tests": {
        "right": [
            "J. Edgar Hoover",
            "John Edgar Hoover",
            "J Edgar Hoover",
            "Edgar Hoover",
            "J. Edgar Hover",
            "FBI Director Hoover"
        ],
        "prompt": [
            "Hoover",
            "Mr. Hoover"
        ],
        "wrong": [
            "Herbert Hoover",
            "President Hoover",
            "Hoover Dam",
            "FBI",
            "Clyde Tolson",
            "Mark Felt",
            "Eliot Ness",
            "Hoovervilles"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
