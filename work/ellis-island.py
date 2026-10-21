import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "ellis-island",
    "name": "Ellis Island",
    "mono": "ELI",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "Immigration station in New York Harbor · About 12 million arrived, 1892–1954",
    "dates": "Immigration station 1892–1954; museum since 1990",
    "briefing": "On January 1, 1892, a teenage girl from Ireland named Annie Moore became the first immigrant processed at a new federal station on a small island in New York Harbor. Over the next 62 years, about 12 million people passed through Ellis Island, waiting in long lines for medical and legal inspections in its Great Hall. Since 1990 its main building has been a museum, and millions of Americans can trace an ancestor who arrived there.",
    "answerHtml": "<b><u>Ellis Island</u></b> (accept <u>Ellis Island</u> Immigration Station; prompt on <u>Ellis</u>; do not accept “Statue of Liberty,” “Liberty Island,” or “Angel Island”)",
    "accept": [
        "ellis island",
        "ellis island immigration station",
        "ellis island immigration museum",
        "ellis island national museum of immigration"
    ],
    "prompt": [
        "ellis",
        "immigration station",
        "the immigration station",
        "island of tears",
        "isle of tears",
        "island of hope"
    ],
    "reject": [
        "statue of liberty",
        "liberty island",
        "bedloes island",
        "angel island",
        "ellis island of the west",
        "castle garden",
        "castle clinton",
        "governors island",
        "staten island",
        "long island",
        "rhode island",
        "rikers island",
        "plymouth rock"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Ellis_Island",
    "qb": {
        "q": "Ellis Island",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "In a 1998 case brought by New Jersey against New York, the Supreme Court ruled that the original part of this island belongs to New York, but the much larger area added later with landfill belongs to New Jersey. Landfill had expanded it from about three acres to more than 27.",
            "r": "About 12 million immigrants passed through it. For 10 points, name this island in New York Harbor, once the nation’s busiest immigration station."
        },
        {
            "p": "Doctors at this place used a small tool called a buttonhook to look under people’s eyelids for trachoma [“truh-KOH-muh”], a contagious eye disease. They marked people who needed a closer exam with chalk letters on their coats, such as “E” for eyes and “H” for heart.",
            "r": "For 10 points, name this immigration station near the Statue of Liberty, which opened in 1892."
        },
        {
            "p": "On June 15, 1897, a fire destroyed this place’s original wooden buildings, though no one was killed. They were replaced in 1900 by a fireproof brick and limestone building with four domed towers, designed by the architects William Boring and Edward Tilton.",
            "r": "Immigrants were inspected in that building’s Great Hall. For 10 points, name this immigration station in New York Harbor."
        },
        {
            "p": "A teenage girl from County Cork, Ireland, received a ten-dollar gold coin for being the first immigrant processed at this place, on January 1, 1892. Statues of that girl, Annie Moore, stand here and in the Irish port of Cobh [“KOHV”], where her voyage began.",
            "r": "For 10 points, name this immigration station in New York Harbor that operated until 1954."
        },
        {
            "p": "First- and second-class passengers arriving in New York were usually inspected aboard their ships, so most people sent to this place had crossed the ocean in crowded third-class quarters called steerage. Ferries carried them from the docks to this island for inspection.",
            "r": "For 10 points, name this immigration station, where about 12 million people arrived between 1892 and 1954."
        },
        {
            "p": "Immigrants at this place climbed a long staircase to the Registry Room while doctors watched them for signs of illness. At the bottom of the “Stairs of Separation,” some headed to trains going west, some to New York City, and some to be held for more questions.",
            "r": "The Registry Room was also called the Great Hall. For 10 points, name this immigration station near the Statue of Liberty."
        },
        {
            "p": "Before this place opened, New York State had processed immigrants at Castle Garden, an old fort at the southern tip of Manhattan. The national government then took over immigration and opened this station on a small island that had once held a military post called Fort Gibson.",
            "r": "For 10 points, name this federal immigration station that opened in New York Harbor in 1892."
        },
        {
            "p": "In 1916, German agents set off an explosion at the Black Tom munitions depot in nearby Jersey City that blew out windows and damaged roofs at this place. The same blast damaged the arm of the Statue of Liberty that holds the torch.",
            "r": "For 10 points, name this immigration station in New York Harbor, where about 12 million immigrants arrived."
        },
        {
            "p": "Historians say it is a myth that officials at this place changed immigrants’ last names, because inspectors worked from passenger lists written at the ports where voyages began. Interpreters helped the inspectors question newcomers in dozens of languages.",
            "r": "For 10 points, name this island immigration station, the gateway for about 12 million newcomers to the United States."
        },
        {
            "p": "After the Immigration Act of 1924 set strict quotas and moved most inspections to American offices overseas, this place was used mainly to hold people waiting to be deported. It closed in 1954, after its last detainee, a Norwegian sailor, was released.",
            "r": "For 10 points, name this former immigration station in New York Harbor, where Annie Moore had been the first immigrant processed."
        },
        {
            "p": "In 1965, Lyndon Johnson made this abandoned site part of the Statue of Liberty National Monument. In the 1980s, Chrysler chairman Lee Iacocca [“eye-uh-KOH-kuh”] led a fundraising campaign that paid to restore its main building, which reopened as a museum in 1990.",
            "r": "For 10 points, name this island in New York Harbor, a former immigration station."
        },
        {
            "p": "Photographer Lewis Hine took portraits of newcomers at this place in the early 1900s, before he became famous for photographing child workers. Women and children traveling alone were often held here until a relative arrived to meet them.",
            "r": "For 10 points, name this immigration station in New York Harbor, which opened in 1892."
        },
        {
            "p": "In 1907, this place’s busiest year, more than a million immigrants arrived here, and on one April day inspectors processed more than 11,000 people. Most of the newcomers in those years came from southern and eastern Europe, especially Italy, Russia, and Austria-Hungary.",
            "r": "For 10 points, name this island immigration station near the Statue of Liberty, where about 12 million people arrived."
        },
        {
            "p": "Only about two percent of the people who arrived at this place were turned away, often because of contagious diseases or because officials thought they were likely to need public support. It was nicknamed both the “Island of Hope” and the “Island of Tears.”",
            "r": "Doctors there checked newcomers for diseases like trachoma. For 10 points, name this immigration station in New York Harbor."
        },
        {
            "p": "Families can have an ancestor’s name engraved on the American Immigrant Wall of Honor at this site, whose museum also helps visitors search the passenger lists of ships that arrived in New York. That museum opened in the restored main building in 1990.",
            "r": "For 10 points, name this former immigration station in New York Harbor, where about 12 million people arrived."
        }
    ],
    "clues": [
        {
            "id": "immigration-station",
            "tier": "giveaway",
            "t": "The main U.S. immigration station, in New York Harbor, from 1892 to 1954",
            "k": ["immigration station", "new york harbor", "1892", "1954"],
            "n": 0
        },
        {
            "id": "twelve-million",
            "tier": "giveaway",
            "t": "About 12 million immigrants passed through it",
            "k": ["12 million", "immigrants"],
            "n": 0
        },
        {
            "id": "statue-neighbor",
            "tier": "giveaway",
            "t": "Lies near the Statue of Liberty and has been part of the Statue of Liberty National Monument since 1965",
            "k": ["statue of liberty", "1965", "national monument"],
            "n": 0,
            "rabbit": "Statue of Liberty"
        },
        {
            "id": "museum",
            "tier": "giveaway",
            "t": "Its main building reopened as an immigration museum in 1990",
            "k": ["museum", "1990"],
            "n": 0
        },
        {
            "id": "annie-moore",
            "tier": "middle",
            "t": "Annie Moore, a teenager from County Cork, Ireland, was the first immigrant processed (January 1, 1892)",
            "k": ["annie moore", "county cork", "january 1"],
            "n": 0
        },
        {
            "id": "buttonhook",
            "tier": "middle",
            "t": "Doctors checked for disease, using buttonhooks to look under eyelids for trachoma",
            "k": ["buttonhook", "trachoma", "eyelids"],
            "n": 0
        },
        {
            "id": "chalk",
            "tier": "middle",
            "t": "People needing a closer exam were marked with chalk letters, like “E” for eyes and “H” for heart",
            "k": ["chalk", "letters"],
            "n": 0
        },
        {
            "id": "great-hall",
            "tier": "middle",
            "t": "Inspections took place in the Registry Room, also called the Great Hall",
            "k": ["registry room", "great hall"],
            "n": 0
        },
        {
            "id": "two-percent",
            "tier": "middle",
            "t": "Only about 2 percent were turned away, often for disease or for seeming likely to need public support",
            "k": ["2 percent", "turned away", "public support"],
            "n": 0
        },
        {
            "id": "new-jersey",
            "tier": "middle",
            "t": "_New Jersey v. New York_ (1998): most of the island, built up with landfill, belongs to New Jersey",
            "k": ["new jersey", "landfill", "1998"],
            "n": 0
        },
        {
            "id": "steerage",
            "tier": "middle",
            "t": "First- and second-class passengers were inspected on their ships; mostly steerage (third-class) passengers came here",
            "k": ["steerage", "third-class"],
            "n": 0
        },
        {
            "id": "nicknames",
            "tier": "middle",
            "t": "Nicknamed the “Island of Hope” and the “Island of Tears”",
            "k": ["hope", "tears"],
            "n": 0
        },
        {
            "id": "fire-1897",
            "tier": "power",
            "t": "A fire destroyed the original wooden buildings in 1897; a fireproof main building opened in 1900",
            "k": ["fire", "1897", "fireproof"],
            "n": 0
        },
        {
            "id": "architects",
            "tier": "power",
            "t": "The main building, with four domed towers, was designed by William Boring and Edward Tilton",
            "k": ["boring", "tilton", "domed towers"],
            "n": 0
        },
        {
            "id": "castle-garden",
            "tier": "power",
            "t": "Replaced Castle Garden, New York State’s immigrant depot at the southern tip of Manhattan",
            "k": ["castle garden", "manhattan"],
            "n": 0
        },
        {
            "id": "fort-gibson",
            "tier": "power",
            "t": "The island once held a military post called Fort Gibson",
            "k": ["fort gibson", "military post"],
            "n": 0
        },
        {
            "id": "black-tom",
            "tier": "power",
            "t": "The 1916 Black Tom explosion in Jersey City, set off by German agents, damaged its buildings and the Statue of Liberty",
            "k": ["black tom", "1916", "jersey city"],
            "n": 0
        },
        {
            "id": "name-myth",
            "tier": "power",
            "t": "Myth: officials changed immigrants’ names here; inspectors actually used passenger lists made at the departure ports",
            "k": ["passenger lists", "myth", "names"],
            "n": 0
        },
        {
            "id": "busiest-year",
            "tier": "power",
            "t": "Busiest year: 1907, with more than a million arrivals; over 11,000 people were processed on one April day",
            "k": ["1907", "busiest", "11,000"],
            "n": 0
        },
        {
            "id": "stairs",
            "tier": "power",
            "t": "The “Stairs of Separation” sent people to trains, to New York City, or to detention",
            "k": ["stairs of separation", "detention"],
            "n": 0
        },
        {
            "id": "closed-1954",
            "tier": "power",
            "t": "After the 1924 quota law, it served mainly as a detention center; it closed in 1954 after its last detainee, a Norwegian sailor, left",
            "k": ["1924", "quota", "norwegian", "detention center"],
            "n": 0
        },
        {
            "id": "iacocca",
            "tier": "power",
            "t": "Chrysler chairman Lee Iacocca led the 1980s fundraising campaign to restore it",
            "k": ["iacocca", "chrysler", "restore"],
            "n": 0
        },
        {
            "id": "hine",
            "tier": "power",
            "t": "Lewis Hine photographed immigrants here before his famous photos of child workers",
            "k": ["lewis hine", "hine", "photographed"],
            "n": 0
        },
        {
            "id": "women-held",
            "tier": "power",
            "t": "Women and children traveling alone were often held until a relative came to meet them",
            "k": ["traveling alone", "relative", "women and children"],
            "n": 0
        },
        {
            "id": "gold-coin",
            "tier": "power",
            "t": "Annie Moore received a ten-dollar gold coin; statues of her stand on the island and in Cobh, Ireland",
            "k": ["gold coin", "cobh", "statues"],
            "n": 0
        },
        {
            "id": "wall-of-honor",
            "tier": "power",
            "t": "The American Immigrant Wall of Honor lists immigrants’ names; the museum helps visitors search ship passenger lists",
            "k": ["wall of honor", "passenger lists"],
            "n": 0
        }
    ],
    "trap": {
        "title": "The island next door",
        "body": "Ellis Island and Liberty Island, home of the Statue of Liberty, sit close together in New York Harbor and belong to the same national monument, so clues about immigrants arriving by ship can tempt you to say “Statue of Liberty.” Angel Island in San Francisco Bay, sometimes called the “Ellis Island of the West,” was a different immigration station, where many Chinese immigrants were held from 1910 to 1940.",
        "fix": "Inspections, doctors with chalk, Annie Moore, the Great Hall, and the years 1892–1954 mean Ellis Island. Emma Lazarus’s poem “The New Colossus,” the sculptor Frédéric Bartholdi, and the torch mean the Statue of Liberty. San Francisco and Chinese immigrants mean Angel Island.",
        "line": "Real answer line: <b><u>Ellis Island</u></b> (do not accept “Statue of Liberty,” “Liberty Island,” or “Angel Island”)"
    },
    "tests": {
        "right": [
            "Ellis Island",
            "Ellis Island Immigration Station",
            "Elis Island",
            "Ellis Island National Museum of Immigration",
            "ellis islnad"
        ],
        "prompt": [
            "Ellis",
            "Island of Tears"
        ],
        "wrong": [
            "Statue of Liberty",
            "Liberty Island",
            "Angel Island",
            "Castle Garden",
            "Ellis Island of the West",
            "Staten Island",
            "Governors Island"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
