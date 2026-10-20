import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "al-capone",
    "name": "Al Capone",
    "mono": "AGC",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "Chicago gang boss of the Prohibition era · Jailed for tax evasion in 1931",
    "dates": "1899–1947",
    "briefing": "Al Capone led a Chicago gang that made millions of dollars selling illegal alcohol during Prohibition, and he was linked to many violent crimes. Prohibition agents, including Eliot Ness and his “Untouchables,” raided his breweries, but tax investigators finally brought him down: in 1931 he was convicted of income tax evasion and sentenced to 11 years in prison. He served part of that sentence at Alcatraz, left prison in poor health, and died in 1947.",
    "answerHtml": "Al <b><u>Capone</u></b> (or Alphonse Gabriel <b><u>Capone</u></b>; prompt on <u>Scarface</u>)",
    "accept": [
        "al capone",
        "capone",
        "alphonse capone",
        "alphonse gabriel capone",
        "alphonse g capone",
        "al scarface capone"
    ],
    "prompt": [
        "scarface"
    ],
    "reject": [
        "eliot ness",
        "elliot ness",
        "ness",
        "untouchables",
        "the untouchables",
        "johnny torrio",
        "torrio",
        "bugs moran",
        "george moran",
        "frank nitti",
        "nitti",
        "lucky luciano",
        "luciano",
        "john dillinger",
        "dillinger",
        "baby face nelson",
        "pretty boy floyd",
        "dutch schultz",
        "meyer lansky",
        "bugsy siegel",
        "john gotti",
        "ralph capone",
        "frank capone",
        "sonny capone",
        "mae capone",
        "dean obanion",
        "hymie weiss",
        "jack mcgurn",
        "frankie yale",
        "tony camonte",
        "elmer irey",
        "frank wilson",
        "prohibition",
        "chicago outfit",
        "the outfit"
    ],
    "mediaPending": True,
    "media": [],
    "wiki": "https://en.wikipedia.org/wiki/Al_Capone",
    "qb": {
        "q": "Capone",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "In 1986, Geraldo Rivera hosted a live TV special in which workers broke into a secret vault beneath this man’s old headquarters at Chicago’s Lexington Hotel, but they found only dirt and a few empty bottles.",
            "r": "For 10 points, name this Prohibition-era Chicago gang boss who was convicted of tax evasion in 1931."
        },
        {
            "p": "In 1927, the Supreme Court ruled in _United States v. Sullivan_ that money earned from illegal businesses could be taxed, a decision that later let prosecutors go after this man, who had not filed tax returns for years.",
            "r": "For 10 points, name this Chicago gangster who was sent to prison for income tax evasion in 1931."
        },
        {
            "p": "Treasury agent Frank Wilson found an old ledger that tied this man to the profits of a gambling house, helping to prove how much income he had never reported. Wilson worked for Elmer Irey’s special intelligence unit.",
            "r": "For 10 points, name this gangster nicknamed “Scarface,” who was convicted of tax evasion in 1931."
        },
        {
            "p": "On the first day of this man’s trial, Judge James Wilkerson swapped the entire jury with the jury from another trial, after reports that this man’s gang was trying to bribe or threaten jurors.",
            "r": "Wilkerson sentenced him to 11 years in prison. For 10 points, name this Chicago gang boss convicted of income tax evasion in 1931."
        },
        {
            "p": "This man’s older brother Ralph, nicknamed “Bottles,” was convicted of tax evasion in 1930, a year before this man was convicted of the same crime. This man’s gang had moved its headquarters to Cicero, just outside Chicago, in the 1920s.",
            "r": "For 10 points, name this gangster who made a fortune selling illegal alcohol during Prohibition."
        },
        {
            "p": "In 1930, Frank Loesch’s Chicago Crime Commission named this man “Public Enemy Number One” on its list of gangsters. Five years earlier, he had taken over Johnny Torrio’s criminal organization when Torrio retired.",
            "r": "For 10 points, name this Chicago gang boss of the Prohibition era who was later sent to Alcatraz."
        },
        {
            "p": "This man’s business card claimed he was a “Second Hand Furniture Dealer,” and during the Great Depression he paid for a Chicago soup kitchen to improve his public image. That soup kitchen handed out free meals to thousands of jobless people.",
            "r": "For 10 points, name this Prohibition-era gangster who was pursued by Eliot Ness and the “Untouchables.”"
        },
        {
            "p": "While working as a bouncer at a Coney Island club owned by Frankie Yale, this man was left with scars on his face after a fight, giving him a nickname he hated. He had been born in Brooklyn in 1899 to Italian immigrant parents.",
            "r": "That nickname was “Scarface.” For 10 points, name this gangster who led a Chicago gang during Prohibition."
        },
        {
            "p": "While in federal prison, this man played the banjo in a band of inmates, and he was released in 1939 in poor health. He died in 1947 at his estate in Miami Beach, Florida.",
            "r": "He had served part of his sentence at Alcatraz. For 10 points, name this Chicago gangster convicted of tax evasion in 1931."
        },
        {
            "p": "A Prohibition agent led a small squad that raided this man’s breweries and got its nickname because its members refused to take bribes. That agent’s memoir about this man’s downfall became a TV series starring Robert Stack.",
            "r": "That agent was Eliot Ness, leader of the Untouchables. For 10 points, name this Chicago gangster whom Ness pursued."
        },
        {
            "p": "Robert De Niro played this man in a 1987 film directed by Brian De Palma, in which Sean Connery won an Oscar for playing a tough Chicago police officer who helps take this man down.",
            "r": "Kevin Costner played Eliot Ness in that film, _The Untouchables_. For 10 points, name this Prohibition-era Chicago gangster."
        },
        {
            "p": "Paul Muni played a gangster loosely based on this man in Howard Hawks’s 1932 film _Scarface_, whose title echoed this man’s own hated nickname. This man’s real-life gang became known as the Chicago Outfit.",
            "r": "For 10 points, name this gangster who got rich bootlegging during Prohibition and went to prison for tax evasion."
        },
        {
            "p": "U.S. Attorney George E. Q. Johnson prosecuted this man, who at first agreed to plead guilty in exchange for a short sentence but withdrew his plea when the judge said he would not be bound by the deal.",
            "r": "This man was also linked to the 1929 St. Valentine’s Day Massacre. For 10 points, name this Chicago gangster convicted of tax evasion."
        },
        {
            "p": "In August 1934, this man was moved from the federal prison in Atlanta to a new maximum-security prison on an island in San Francisco Bay, where he became one of its earliest and most famous inmates.",
            "r": "He had been sentenced to 11 years for tax evasion. For 10 points, name this Chicago gang boss of the Prohibition era."
        },
        {
            "p": "In May 1929, this man was arrested in Philadelphia for carrying a concealed gun and spent several months in Eastern State Penitentiary, where a re-creation of his furnished cell is shown to visitors.",
            "r": "For 10 points, name this Chicago gangster whose biggest conviction came two years later, in 1931, for income tax evasion."
        }
    ],
    "clues": [
        {
            "id": "chicago-gang",
            "tier": "giveaway",
            "t": "Chicago gang boss during Prohibition (the 1920s)",
            "k": ["chicago", "gang boss", "prohibition"],
            "n": 0
        },
        {
            "id": "bootlegging",
            "tier": "giveaway",
            "t": "Made millions bootlegging (selling illegal alcohol) to speakeasies",
            "k": ["bootlegging", "speakeasies", "illegal alcohol"],
            "n": 0,
            "rabbit": "Prohibition"
        },
        {
            "id": "tax-evasion",
            "tier": "giveaway",
            "t": "Convicted of income tax evasion in 1931 and sentenced to 11 years",
            "k": ["tax evasion", "income tax", "1931", "11 years"],
            "n": 0
        },
        {
            "id": "scarface",
            "tier": "giveaway",
            "t": "Nicknamed “Scarface” for scars on his face, a name he hated",
            "k": ["scarface", "scars"],
            "n": 0
        },
        {
            "id": "ness",
            "tier": "giveaway",
            "t": "Pursued by Eliot Ness and the “Untouchables,” Prohibition agents who refused bribes",
            "k": ["eliot ness", "untouchables", "bribes"],
            "n": 0
        },
        {
            "id": "alcatraz",
            "tier": "middle",
            "t": "Served time in the federal prison in Atlanta and then at Alcatraz (from 1934)",
            "k": ["alcatraz", "atlanta", "1934"],
            "n": 0
        },
        {
            "id": "valentines",
            "tier": "middle",
            "t": "Linked to the 1929 St. Valentine’s Day Massacre",
            "k": ["valentine", "1929"],
            "n": 0
        },
        {
            "id": "torrio",
            "tier": "middle",
            "t": "Took over Johnny Torrio’s Chicago gang in 1925, at age 26",
            "k": ["johnny torrio", "torrio", "1925"],
            "n": 0
        },
        {
            "id": "brooklyn",
            "tier": "middle",
            "t": "Born in Brooklyn, New York (1899), to Italian immigrant parents",
            "k": ["brooklyn", "italian", "1899"],
            "n": 0
        },
        {
            "id": "public-enemy",
            "tier": "middle",
            "t": "Named “Public Enemy Number One” by the Chicago Crime Commission (1930)",
            "k": ["public enemy", "crime commission"],
            "n": 0
        },
        {
            "id": "untouchables-film",
            "tier": "middle",
            "t": "Played by Robert De Niro in _The Untouchables_ (1987), with Kevin Costner as Ness",
            "k": ["de niro", "costner", "1987"],
            "n": 0
        },
        {
            "id": "released",
            "tier": "middle",
            "t": "Released in 1939 in poor health; died in 1947 at his Miami Beach estate",
            "k": ["1939", "1947", "miami beach"],
            "n": 0
        },
        {
            "id": "cicero",
            "tier": "middle",
            "t": "His gang moved its headquarters to Cicero, just outside Chicago",
            "k": ["cicero"],
            "n": 0
        },
        {
            "id": "sullivan",
            "tier": "power",
            "t": "_United States v. Sullivan_ (1927): illegal income can be taxed, which opened the door to his tax case",
            "k": ["sullivan", "1927"],
            "n": 0
        },
        {
            "id": "wilson-ledger",
            "tier": "power",
            "t": "Treasury agent Frank Wilson found a gambling-house ledger; Elmer Irey led the special intelligence unit",
            "k": ["frank wilson", "ledger", "elmer irey", "irey"],
            "n": 0
        },
        {
            "id": "wilkerson",
            "tier": "power",
            "t": "Judge James Wilkerson swapped his jury with another trial’s after reports of bribes and threats",
            "k": ["wilkerson", "jury"],
            "n": 0
        },
        {
            "id": "plea",
            "tier": "power",
            "t": "He first agreed to plead guilty, then withdrew the plea when the judge would not honor the deal; U.S. Attorney George E. Q. Johnson prosecuted",
            "k": ["plead guilty", "plea", "george e. q. johnson"],
            "n": 0
        },
        {
            "id": "ralph",
            "tier": "power",
            "t": "His older brother Ralph (“Bottles”) was convicted of tax evasion in 1930",
            "k": ["ralph", "bottles"],
            "n": 0
        },
        {
            "id": "geraldo",
            "tier": "power",
            "t": "Geraldo Rivera’s 1986 TV special opened his secret vault at the Lexington Hotel; it held only dirt and empty bottles",
            "k": ["geraldo rivera", "geraldo", "vault", "lexington hotel"],
            "n": 0
        },
        {
            "id": "soup-kitchen",
            "tier": "power",
            "t": "Paid for a Chicago soup kitchen during the Great Depression to improve his image",
            "k": ["soup kitchen", "great depression"],
            "n": 0
        },
        {
            "id": "furniture",
            "tier": "power",
            "t": "His business card said “Second Hand Furniture Dealer”",
            "k": ["furniture", "business card"],
            "n": 0
        },
        {
            "id": "coney-island",
            "tier": "power",
            "t": "Got his facial scars in a fight while working as a bouncer at Frankie Yale’s club on Coney Island",
            "k": ["frankie yale", "coney island", "bouncer"],
            "n": 0
        },
        {
            "id": "banjo",
            "tier": "power",
            "t": "Played the banjo in a band of prison inmates",
            "k": ["banjo"],
            "n": 0
        },
        {
            "id": "muni",
            "tier": "power",
            "t": "Paul Muni played a gangster based on him in Howard Hawks’s _Scarface_ (1932); his gang became known as the Chicago Outfit",
            "k": ["paul muni", "muni", "chicago outfit"],
            "n": 0
        },
        {
            "id": "robert-stack",
            "tier": "power",
            "t": "Ness’s memoir _The Untouchables_ became a TV series starring Robert Stack",
            "k": ["robert stack", "memoir"],
            "n": 0
        },
        {
            "id": "eastern-state",
            "tier": "power",
            "t": "Arrested in Philadelphia in 1929 for carrying a concealed gun; spent months in Eastern State Penitentiary",
            "k": ["eastern state", "philadelphia", "concealed"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Gangster, not G-man",
        "body": "Capone questions are packed with names that are answer lines of their own: Eliot Ness (the agent who chased him), Johnny Torrio (the boss who brought him to Chicago), and John Dillinger (a 1930s bank robber who was also called “Public Enemy Number One”). Capone’s big conviction was not for bootlegging or violence but for income tax evasion, which surprises many players.",
        "fix": "The agent who led the Untouchables is Ness; the gang boss they chased is Capone. If you hear “tax evasion,” “Alcatraz,” “Scarface,” or the Lexington Hotel, say Capone.",
        "line": "Real answer line: Al <b><u>Capone</u></b> (or Alphonse Gabriel <b><u>Capone</u></b>; prompt on “Scarface”)"
    },
    "tests": {
        "right": [
            "Al Capone",
            "Capone",
            "Alphonse Capone",
            "Alphonse Gabriel Capone",
            "Al Capon"
        ],
        "prompt": [
            "Scarface"
        ],
        "wrong": [
            "Eliot Ness",
            "John Dillinger",
            "Johnny Torrio",
            "Bugs Moran",
            "Lucky Luciano",
            "Ralph Capone",
            "Frank Nitti"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("wrote", data["id"])
