import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "john-dillinger",
    "name": "John Dillinger",
    "mono": "JHD",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "Depression-era bank robber · Called “Public Enemy Number One” in 1934",
    "dates": "1903–1934",
    "briefing": "John Dillinger’s gangs robbed banks across the Midwest in 1933 and 1934, and newspapers followed his every move during the Great Depression. In March 1934, he escaped from a jail in Crown Point, Indiana, using a fake wooden gun, and the Justice Department soon called him “Public Enemy Number One.” On July 22, 1934, federal agents led by Melvin Purvis caught up with him outside Chicago’s Biograph Theater, where he was shot and killed.",
    "answerHtml": "John <b><u>Dillinger</u></b> (accept John Herbert <u>Dillinger</u>)",
    "accept": [
        "john dillinger",
        "dillinger",
        "john herbert dillinger",
        "john h dillinger"
    ],
    "prompt": [],
    "reject": [
        "al capone",
        "capone",
        "baby face nelson",
        "lester gillis",
        "pretty boy floyd",
        "charles arthur floyd",
        "bonnie and clyde",
        "bonnie parker",
        "clyde barrow",
        "machine gun kelly",
        "george kelly",
        "ma barker",
        "alvin karpis",
        "homer van meter",
        "harry pierpont",
        "john hamilton",
        "melvin purvis",
        "purvis",
        "samuel cowley",
        "j edgar hoover",
        "hoover",
        "anna sage",
        "lady in red",
        "woman in red",
        "eliot ness",
        "jesse james",
        "billy the kid",
        "butch cassidy",
        "public enemies"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/John_Dillinger",
    "qb": {
        "q": "Dillinger",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "This man joined the U.S. Navy in 1923 and served on the battleship USS _Utah_, but he deserted a few months later when his ship docked in Boston. The next year, he was sent to prison for robbing a grocer in Mooresville, Indiana.",
            "r": "For 10 points, name this Indiana-born bank robber of the 1930s who was called “Public Enemy Number One.”"
        },
        {
            "p": "While serving nearly nine years in Indiana prisons, this man learned from experienced bank robbers like Harry Pierpont. After his parole in May 1933, he arranged for guns to be smuggled into the state prison at Michigan City to help Pierpont and others escape.",
            "r": "For 10 points, name this Depression-era bank robber who was killed by federal agents outside Chicago’s Biograph Theater in 1934."
        },
        {
            "p": "After police arrested this man in Dayton, Ohio, in September 1933, the friends he had helped escape from prison freed him from the county jail in Lima. Together they formed a gang that robbed banks across the Midwest.",
            "r": "For 10 points, name this bank robber whom the Justice Department called “Public Enemy Number One” in 1934."
        },
        {
            "p": "In January 1934, firefighters at a burning hotel in Tucson, Arizona, recognized members of this man’s gang from magazine photos, which led to the arrest of the whole group. This man was then sent back to Indiana and locked in a county jail.",
            "r": "Weeks later, he escaped from that jail at Crown Point. For 10 points, name this bank robber later killed outside Chicago’s Biograph Theater."
        },
        {
            "p": "Lake County prosecutor Robert Estill was criticized after he posed for a photograph with his arm on this prisoner’s shoulder. In March 1934, this prisoner escaped from that county’s jail, which had been called escape-proof.",
            "r": "He used a fake wooden gun. For 10 points, name this bank robber who escaped from the jail in Crown Point, Indiana."
        },
        {
            "p": "After this man escaped from a jail run by Sheriff Lillian Holley, he drove off in her own car and crossed into Illinois. Driving a stolen car across a state line broke a federal law, which let federal agents join the hunt for him.",
            "r": "For 10 points, name this bank robber who had escaped from the Crown Point jail using a fake gun."
        },
        {
            "p": "In April 1934, this man and his gang slipped away from federal agents who had surrounded the Little Bohemia Lodge in northern Wisconsin, a failed raid that embarrassed J. Edgar Hoover’s agency. Baby Face Nelson was part of his gang at the time.",
            "r": "For 10 points, name this Indiana bank robber whom the Justice Department called “Public Enemy Number One.”"
        },
        {
            "p": "In May 1934, this fugitive had plastic surgery to change his face and tried to erase his fingerprints, hoping to avoid capture. Two months later, agents were waiting for him outside a Chicago movie theater anyway.",
            "r": "For 10 points, name this Depression-era bank robber whose gangs hit banks across the Midwest."
        },
        {
            "p": "On the night he died, this man watched _Manhattan Melodrama_, a gangster film starring Clark Gable, at a movie theater on Chicago’s Lincoln Avenue. Federal agents waited outside for the film to end.",
            "r": "That theater was the Biograph. For 10 points, name this bank robber who had been called “Public Enemy Number One.”"
        },
        {
            "p": "Anna Sage, a Romanian immigrant who hoped to avoid being deported, tipped off federal agents that this man would be going to the movies with her on July 22, 1934. Newspapers called her the “Lady in Red,” though her skirt was really orange.",
            "r": "For 10 points, name this bank robber whom agents tracked down outside Chicago’s Biograph Theater."
        },
        {
            "p": "Melvin Purvis, the federal agent in charge in Chicago, lit a cigar as a signal when this man walked out of a movie theater in July 1934. Inspector Samuel Cowley had been sent by J. Edgar Hoover to help lead the hunt for this man.",
            "r": "For 10 points, name this bank robber who was shot and killed outside Chicago’s Biograph Theater that night."
        },
        {
            "p": "This man was born in Indianapolis in 1903 and is buried there in Crown Hill Cemetery, the resting place of President Benjamin Harrison. His family moved to a farm near Mooresville, Indiana, when he was a teenager.",
            "r": "For 10 points, name this Indiana bank robber of the 1930s who was called “Public Enemy Number One.”"
        },
        {
            "p": "Johnny Depp played this man, and Christian Bale played the agent chasing him, in Michael Mann’s 2009 film _Public Enemies_. That film was based on a book by Bryan Burrough about the crime wave of 1933 and 1934.",
            "r": "For 10 points, name this bank robber who escaped from the Crown Point jail and was later killed outside Chicago’s Biograph Theater."
        },
        {
            "p": "Partly in response to the crimes of this man and other outlaws, Congress passed laws in 1934 that made robbing a national bank a federal crime and allowed federal agents to carry guns and make arrests.",
            "r": "Soon after, agents caught up with him at Chicago’s Biograph Theater. For 10 points, name this bank robber called “Public Enemy Number One.”"
        },
        {
            "p": "Harry Pierpont and John “Red” Hamilton were members of this man’s gang, which raided Indiana police stations for guns and bulletproof vests in October 1933. His gangs went on to rob banks in Indiana, Wisconsin, South Dakota, and Iowa.",
            "r": "For 10 points, name this Depression-era bank robber who escaped from the Crown Point jail with a fake wooden gun."
        }
    ],
    "clues": [
        {
            "id": "bank-robber",
            "tier": "giveaway",
            "t": "Bank robber whose gangs hit banks across the Midwest in 1933 and 1934, during the Great Depression",
            "k": ["bank robber", "midwest", "great depression"],
            "n": 0,
            "rabbit": "Great Depression"
        },
        {
            "id": "public-enemy",
            "tier": "giveaway",
            "t": "Called “Public Enemy Number One” by the Justice Department in 1934",
            "k": ["public enemy number one", "public enemy", "1934"],
            "n": 0
        },
        {
            "id": "biograph",
            "tier": "giveaway",
            "t": "Killed by federal agents outside Chicago’s Biograph Theater on July 22, 1934",
            "k": ["biograph", "chicago", "july 22, 1934"],
            "n": 0
        },
        {
            "id": "crown-point",
            "tier": "giveaway",
            "t": "Escaped from the jail in Crown Point, Indiana, with a fake wooden gun (March 1934)",
            "k": ["crown point", "wooden gun"],
            "n": 0
        },
        {
            "id": "purvis",
            "tier": "middle",
            "t": "Agent Melvin Purvis led the agents who tracked him down",
            "k": ["melvin purvis", "purvis"],
            "n": 0
        },
        {
            "id": "lady-in-red",
            "tier": "middle",
            "t": "Anna Sage, the “Lady in Red,” tipped off the agents; her skirt was really orange",
            "k": ["anna sage", "lady in red", "orange"],
            "n": 0
        },
        {
            "id": "manhattan-melodrama",
            "tier": "middle",
            "t": "Watched the Clark Gable film _Manhattan Melodrama_ on the night he died",
            "k": ["manhattan melodrama", "clark gable"],
            "n": 0
        },
        {
            "id": "hoover",
            "tier": "middle",
            "t": "Hunted by J. Edgar Hoover’s agents, whose agency was renamed the FBI in 1935",
            "k": ["j. edgar hoover", "hoover", "fbi"],
            "n": 0,
            "rabbit": "Federal Bureau of Investigation"
        },
        {
            "id": "indiana",
            "tier": "middle",
            "t": "Born in Indianapolis (1903); his family moved to a farm near Mooresville, Indiana",
            "k": ["indianapolis", "mooresville", "indiana"],
            "n": 0
        },
        {
            "id": "baby-face",
            "tier": "middle",
            "t": "Baby Face Nelson was part of his gang in 1934",
            "k": ["baby face nelson", "nelson"],
            "n": 0
        },
        {
            "id": "public-enemies-film",
            "tier": "middle",
            "t": "Played by Johnny Depp in _Public Enemies_ (2009), with Christian Bale as Melvin Purvis",
            "k": ["johnny depp", "public enemies", "christian bale"],
            "n": 0
        },
        {
            "id": "navy",
            "tier": "power",
            "t": "Joined the Navy in 1923 and served on the battleship USS _Utah_, but deserted months later",
            "k": ["navy", "utah", "deserted"],
            "n": 0
        },
        {
            "id": "grocer",
            "tier": "power",
            "t": "Imprisoned for robbing a grocer in Mooresville (1924); paroled in May 1933 after nearly nine years",
            "k": ["grocer", "paroled", "1924"],
            "n": 0
        },
        {
            "id": "pierpont",
            "tier": "power",
            "t": "Learned from veteran robbers like Harry Pierpont in prison, then arranged for guns to be smuggled into Michigan City prison to free them",
            "k": ["harry pierpont", "pierpont", "michigan city"],
            "n": 0
        },
        {
            "id": "lima",
            "tier": "power",
            "t": "Arrested in Dayton, Ohio (September 1933); his gang freed him from the jail in Lima, Ohio",
            "k": ["lima", "dayton"],
            "n": 0
        },
        {
            "id": "tucson",
            "tier": "power",
            "t": "Captured in Tucson, Arizona (January 1934) after firefighters at a hotel fire recognized gang members",
            "k": ["tucson", "hotel fire", "firefighters"],
            "n": 0
        },
        {
            "id": "estill",
            "tier": "power",
            "t": "Prosecutor Robert Estill posed for a photo with his arm on his shoulder",
            "k": ["robert estill", "estill", "photo"],
            "n": 0
        },
        {
            "id": "holley",
            "tier": "power",
            "t": "Escaped in Sheriff Lillian Holley’s car; taking a stolen car across a state line broke a federal law",
            "k": ["lillian holley", "holley", "state line"],
            "n": 0
        },
        {
            "id": "little-bohemia",
            "tier": "power",
            "t": "Escaped a failed federal raid at the Little Bohemia Lodge in northern Wisconsin (April 1934)",
            "k": ["little bohemia", "wisconsin"],
            "n": 0
        },
        {
            "id": "surgery",
            "tier": "power",
            "t": "Had plastic surgery to change his face and tried to erase his fingerprints (May 1934)",
            "k": ["plastic surgery", "fingerprints"],
            "n": 0
        },
        {
            "id": "cigar",
            "tier": "power",
            "t": "Purvis lit a cigar as the signal; Inspector Samuel Cowley helped lead the hunt",
            "k": ["cigar", "samuel cowley", "cowley"],
            "n": 0
        },
        {
            "id": "crime-laws",
            "tier": "power",
            "t": "New federal laws (1934) made robbing a national bank a federal crime and let agents carry guns",
            "k": ["national bank", "federal crime", "carry guns"],
            "n": 0
        },
        {
            "id": "crown-hill",
            "tier": "power",
            "t": "Buried in Crown Hill Cemetery in Indianapolis, also the resting place of Benjamin Harrison",
            "k": ["crown hill", "cemetery", "benjamin harrison"],
            "n": 0
        },
        {
            "id": "police-raids",
            "tier": "power",
            "t": "His gang, including Harry Pierpont and John “Red” Hamilton, raided Indiana police stations for guns in October 1933",
            "k": ["police stations", "red", "october 1933"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Which public enemy?",
        "body": "Several outlaws of the early 1930s turn up in the same tossups. Al Capone was a Chicago gang boss of the Prohibition era whom the Chicago Crime Commission named “Public Enemy Number One” in 1930, and he went to prison for tax evasion; Baby Face Nelson, Pretty Boy Floyd, and Bonnie and Clyde were other robbers of the same years. Dillinger was the bank robber the Justice Department called “Public Enemy Number One” in 1934.",
        "fix": "Crown Point and the wooden gun, Melvin Purvis, the Lady in Red, _Manhattan Melodrama_, and the Biograph Theater mean Dillinger. Tax evasion, bootlegging, and Alcatraz mean Capone; Texas, Louisiana, and a couple traveling together mean Bonnie and Clyde.",
        "line": "Real answer line: John <b><u>Dillinger</u></b> (accept John Herbert <u>Dillinger</u>)"
    },
    "tests": {
        "right": [
            "John Dillinger",
            "Dillinger",
            "John Herbert Dillinger",
            "Dilinger",
            "John Dillenger"
        ],
        "prompt": [],
        "wrong": [
            "Al Capone",
            "Baby Face Nelson",
            "Bonnie and Clyde",
            "Pretty Boy Floyd",
            "Melvin Purvis",
            "J. Edgar Hoover",
            "Machine Gun Kelly",
            "Clyde Barrow"
        ]
    }
}

out = ROOT / "topics" / f"{data['id']}.json"
with open(out, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("wrote", out)
