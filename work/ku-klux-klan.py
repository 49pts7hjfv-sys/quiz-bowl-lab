import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "ku-klux-klan",
    "name": "Ku Klux Klan",
    "mono": "KKK",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "Hate group founded after the Civil War · Used terror to block Black rights",
    "dates": "Founded 1865; revived 1915",
    "briefing": "The Ku Klux Klan was founded in Pulaski, Tennessee, in 1865 by six Confederate veterans. During Reconstruction, its masked members used threats and violence to stop Black Americans from voting and to drive out Republican officials, until Congress and President Ulysses S. Grant cracked down with the Ku Klux Klan Act of 1871. The group came back in 1915 and again during the civil rights movement, and each time Americans fought it in Congress, in the courts, and through peaceful protest.",
    "answerHtml": "<b><u>Ku Klux Klan</u></b> (accept <b><u>KKK</u></b> or the <u>Klan</u>)",
    "accept": [
        "ku klux klan",
        "the ku klux klan",
        "kkk",
        "the kkk",
        "k k k",
        "klan",
        "the klan",
        "ku klux",
        "knights of the ku klux klan"
    ],
    "prompt": [],
    "reject": [
        "knights of the white camellia",
        "white camellia",
        "white league",
        "red shirts",
        "white citizens councils",
        "white citizens council",
        "citizens councils",
        "know nothings",
        "know nothing party",
        "american party",
        "jim crow",
        "jim crow laws",
        "black codes",
        "redeemers",
        "knights of the golden circle",
        "nathan bedford forrest",
        "birth of a nation"
    ],
    "mediaPending": True,
    "media": [],
    "wiki": "https://en.wikipedia.org/wiki/Ku_Klux_Klan",
    "qb": {
        "q": "Ku Klux Klan",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "Part of this group’s name comes from the Greek word for “circle.” It was founded in late 1865 by six Confederate veterans in Pulaski, Tennessee, and former Confederate general Nathan Bedford Forrest became its first Grand Wizard.",
            "r": "Congress passed laws against it in 1870 and 1871. For 10 points, name this white supremacist group whose members terrorized Black Americans during Reconstruction."
        },
        {
            "p": "In 1871, Congress passed a law nicknamed for this group that let President Ulysses S. Grant suspend habeas corpus [“HAY-bee-us KOR-pus”] and use federal troops against it. Grant then suspended habeas corpus in nine South Carolina counties, and hundreds of this group’s members were arrested.",
            "r": "Its members hid their faces behind masks. For 10 points, name this secret terrorist group founded in Tennessee after the Civil War."
        },
        {
            "p": "In 1915, William J. Simmons, a former Methodist preacher who took the title Imperial Wizard, revived this group at a ceremony on Stone Mountain, near Atlanta, Georgia. He was inspired partly by a new film that glorified the group’s Reconstruction-era members.",
            "r": "That film was D. W. Griffith’s _The Birth of a Nation_. For 10 points, name this white supremacist group first founded in 1865."
        },
        {
            "p": "This group’s power in Indiana collapsed after its state leader, D. C. Stephenson, was convicted of murder in 1925, the same year tens of thousands of its members marched in Washington, D.C. In that decade, it targeted Catholics, Jews, and immigrants as well as Black Americans.",
            "r": "At its peak, it claimed millions of members. For 10 points, name this hooded white supremacist group."
        },
        {
            "p": "Bobby Frank Cherry, convicted in 2002, was the last of three members of this group found guilty of a 1963 church bombing. That bombing, at the 16th Street Baptist Church in Birmingham, Alabama, killed four Black girls on a Sunday morning.",
            "r": "In the 1960s, its members used violence against the civil rights movement. For 10 points, name this white supremacist group, first founded during Reconstruction."
        },
        {
            "p": "The FBI code-named its 1964 investigation MIBURN, short for “Mississippi Burning,” after members of this group murdered three civil rights workers, James Chaney, Andrew Goodman, and Michael Schwerner, near Philadelphia, Mississippi. In 1967, a federal jury convicted seven men of violating the workers’ civil rights.",
            "r": "The three men had been working to register Black voters during Freedom Summer. For 10 points, name this hooded white supremacist group."
        },
        {
            "p": "In _Brandenburg v. Ohio_, the Supreme Court overturned the conviction of an Ohio leader of this group, ruling that the government may punish speech only when it is meant and likely to cause “imminent lawless action.” That 1969 decision became a major free-speech precedent.",
            "r": "That group had been revived in 1915. For 10 points, name this group whose members wore white hoods and robes."
        },
        {
            "p": "Attorney General Amos Akerman led the new Department of Justice in prosecuting members of this group, while a congressional committee gathered thousands of pages of testimony about its violence in the South. Those efforts largely broke this group by 1872.",
            "r": "Ulysses S. Grant was president at the time. For 10 points, name this Reconstruction-era group that used terror to keep Black men from voting."
        },
        {
            "p": "In 1870, North Carolina governor William Holden called out the state militia against this group, in a campaign named the Kirk-Holden War after Holden and his militia commander, George Kirk. The state legislature then impeached Holden, and he became the first U.S. governor removed from office that way.",
            "r": "Its members attacked Black voters and white Republicans across the South. For 10 points, name this group founded by Confederate veterans in Pulaski, Tennessee."
        },
        {
            "p": "Thomas Dixon’s 1905 novel _The Clansman_, which praised this group, became the basis for a 1915 film that President Woodrow Wilson screened at the White House. The NAACP protested that film for its racist picture of Reconstruction.",
            "r": "That film was _The Birth of a Nation_. For 10 points, name this white supremacist group revived in 1915."
        },
        {
            "p": "In _Virginia v. Black_, the Supreme Court ruled in 2003 that a state may ban cross burning done to intimidate people, but it may not assume that every cross burning is a threat. This group took up cross burning after it was revived in 1915.",
            "r": "Its Reconstruction-era members had hidden their faces behind masks. For 10 points, name this white supremacist organization founded in Pulaski, Tennessee."
        },
        {
            "p": "With help from the Southern Poverty Law Center, Beulah Mae Donald won a seven-million-dollar lawsuit in 1987 against a large branch of this group after its members murdered her son in Mobile, Alabama. The verdict forced that branch to give up its headquarters building.",
            "r": "Its members had also fought the civil rights movement. For 10 points, name this hate group first founded in 1865 and revived in 1915."
        },
        {
            "p": "In March 1965, President Lyndon Johnson went on television to announce the arrests of four members of this group for the murder of Viola Liuzzo, a white volunteer from Detroit who had helped with the Selma to Montgomery march.",
            "r": "Johnson urged its members to quit. For 10 points, name this white supremacist organization first founded after the Civil War."
        },
        {
            "p": "Supreme Court Justice Hugo Black had briefly belonged to this group as an Alabama lawyer in the 1920s, a fact reported by a newspaper soon after he joined the Court in 1937. Black later joined the unanimous ruling in _Brown v. Board of Education_.",
            "r": "In the 1920s, it claimed millions of members. For 10 points, name this white supremacist group that was revived in 1915."
        },
        {
            "p": "In May 1961, a mob that included members of this group set fire to a Freedom Riders’ bus outside Anniston, Alabama, and members of this group attacked other riders in Birmingham while local police held back.",
            "r": "The Freedom Riders were testing a Supreme Court ruling against segregated bus stations. For 10 points, name this hooded white supremacist group."
        }
    ],
    "clues": [
        {
            "id": "founded-1865",
            "tier": "giveaway",
            "t": "White supremacist hate group founded in Pulaski, Tennessee, in 1865 by six Confederate veterans",
            "k": ["pulaski", "tennessee", "1865", "confederate veterans"],
            "n": 0
        },
        {
            "id": "reconstruction-terror",
            "tier": "giveaway",
            "t": "During Reconstruction, used threats and violence to keep Black Americans from voting and to drive out Republican officials",
            "k": ["reconstruction", "voting", "violence"],
            "n": 0,
            "rabbit": "Reconstruction"
        },
        {
            "id": "hoods",
            "tier": "giveaway",
            "t": "Its first members hid behind masks; the later group wore white robes and pointed hoods",
            "k": ["white robes", "masks", "hoods"],
            "n": 0
        },
        {
            "id": "act-1871",
            "tier": "giveaway",
            "t": "Congress passed the Civil Rights Act of 1871, nicknamed for this group, so President Grant could crack down on it",
            "k": ["civil rights act of 1871", "1871", "grant"],
            "n": 0,
            "rabbit": "Ulysses S. Grant"
        },
        {
            "id": "forrest",
            "tier": "middle",
            "t": "Former Confederate general Nathan Bedford Forrest was its first Grand Wizard",
            "k": ["nathan bedford forrest", "forrest", "grand wizard"],
            "n": 0
        },
        {
            "id": "habeas",
            "tier": "middle",
            "t": "Grant suspended habeas corpus in nine South Carolina counties (1871), and hundreds of members were arrested",
            "k": ["habeas corpus", "south carolina", "nine"],
            "n": 0
        },
        {
            "id": "revival-1915",
            "tier": "middle",
            "t": "Revived in 1915 by William J. Simmons at Stone Mountain, Georgia",
            "k": ["stone mountain", "simmons", "1915"],
            "n": 0
        },
        {
            "id": "birth-of-a-nation",
            "tier": "middle",
            "t": "D. W. Griffith’s 1915 film _The Birth of a Nation_ glorified the group; the NAACP protested it",
            "k": ["birth of a nation", "griffith", "naacp"],
            "n": 0
        },
        {
            "id": "twenties",
            "tier": "middle",
            "t": "In the 1920s it claimed millions of members and also targeted Catholics, Jews, and immigrants",
            "k": ["1920s", "catholics", "immigrants", "millions"],
            "n": 0
        },
        {
            "id": "birmingham",
            "tier": "middle",
            "t": "Members bombed the 16th Street Baptist Church in Birmingham, Alabama (1963), killing four Black girls",
            "k": ["16th street baptist church", "birmingham", "1963"],
            "n": 0,
            "rabbit": "Birmingham, Alabama"
        },
        {
            "id": "freedom-summer",
            "tier": "middle",
            "t": "During Freedom Summer (1964), members murdered civil rights workers James Chaney, Andrew Goodman, and Michael Schwerner in Mississippi",
            "k": ["freedom summer", "chaney", "goodman", "schwerner", "mississippi"],
            "n": 0
        },
        {
            "id": "enforcement-acts",
            "tier": "middle",
            "t": "The Enforcement Acts (1870–1871) made it a federal crime to use force to stop people from voting",
            "k": ["enforcement acts", "federal crime"],
            "n": 0
        },
        {
            "id": "greek-circle",
            "tier": "power",
            "t": "Part of its name comes from the Greek word for “circle”",
            "k": ["greek", "circle"],
            "n": 0
        },
        {
            "id": "akerman",
            "tier": "power",
            "t": "Attorney General Amos Akerman and the new Justice Department prosecuted members; the first group was mostly broken by 1872",
            "k": ["amos akerman", "akerman", "justice department", "1872"],
            "n": 0
        },
        {
            "id": "holden",
            "tier": "power",
            "t": "North Carolina governor William Holden fought it with militia (the Kirk-Holden War) and was impeached and removed (1871)",
            "k": ["william holden", "holden", "kirk-holden war", "impeached"],
            "n": 0
        },
        {
            "id": "dixon-wilson",
            "tier": "power",
            "t": "The 1915 film was based on Thomas Dixon’s novel _The Clansman_; Woodrow Wilson screened it at the White House",
            "k": ["thomas dixon", "the clansman", "woodrow wilson"],
            "n": 0
        },
        {
            "id": "stephenson",
            "tier": "power",
            "t": "Indiana leader D. C. Stephenson’s 1925 murder conviction helped collapse its power; members marched in Washington, D.C., that year",
            "k": ["stephenson", "indiana", "1925"],
            "n": 0
        },
        {
            "id": "cross-burning",
            "tier": "power",
            "t": "The revived group took up cross burning; _Virginia v. Black_ (2003) let states ban cross burning meant to intimidate",
            "k": ["cross burning", "virginia v. black", "2003"],
            "n": 0
        },
        {
            "id": "brandenburg",
            "tier": "power",
            "t": "_Brandenburg v. Ohio_ (1969) overturned an Ohio leader’s conviction: only speech likely to cause “imminent lawless action” can be punished",
            "k": ["brandenburg", "imminent lawless action", "ohio"],
            "n": 0
        },
        {
            "id": "miburn",
            "tier": "power",
            "t": "The FBI code-named its 1964 Mississippi investigation MIBURN (“Mississippi Burning”); a federal jury convicted seven men in 1967",
            "k": ["miburn", "mississippi burning", "fbi", "1967"],
            "n": 0
        },
        {
            "id": "liuzzo",
            "tier": "power",
            "t": "Lyndon Johnson announced on TV the arrests of members for the 1965 murder of Viola Liuzzo, a Selma march volunteer",
            "k": ["viola liuzzo", "liuzzo", "selma", "lyndon johnson"],
            "n": 0
        },
        {
            "id": "donald",
            "tier": "power",
            "t": "Beulah Mae Donald’s 1987 lawsuit, backed by the Southern Poverty Law Center, made a large branch give up its headquarters",
            "k": ["beulah mae donald", "southern poverty law center", "1987"],
            "n": 0
        },
        {
            "id": "freedom-riders",
            "tier": "power",
            "t": "Mobs that included members attacked the Freedom Riders in Anniston and Birmingham, Alabama (1961)",
            "k": ["freedom riders", "anniston", "1961"],
            "n": 0
        },
        {
            "id": "hugo-black",
            "tier": "power",
            "t": "Supreme Court Justice Hugo Black had been a member in the 1920s, which was reported in 1937",
            "k": ["hugo black", "1937"],
            "n": 0
        },
        {
            "id": "cherry",
            "tier": "power",
            "t": "Bobby Frank Cherry (2002) was the last of three men convicted for the Birmingham church bombing",
            "k": ["bobby frank cherry", "cherry", "2002"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Group, laws, or era?",
        "body": "Questions about Reconstruction and civil rights mention several related answers. The Ku Klux Klan was a secret, violent white supremacist group. Jim Crow laws were the segregation laws Southern states passed later, the Black Codes were laws passed right after the Civil War, and the White League and the Red Shirts were other armed white supremacist groups of the 1870s. Answering “Jim Crow” or “Reconstruction” when the question asks for “this group” is wrong.",
        "fix": "Listen for the noun. “This group” or “this organization,” with clues like Pulaski, Nathan Bedford Forrest, the Grand Wizard, Stone Mountain, or _The Birth of a Nation_, means the Ku Klux Klan. “These laws” means Jim Crow laws or the Black Codes, and “this era” means Reconstruction. “KKK” and “the Klan” are both fine.",
        "line": "Real answer line: <b><u>Ku Klux Klan</u></b> (accept <b><u>KKK</u></b> or the <u>Klan</u>)"
    },
    "tests": {
        "right": [
            "Ku Klux Klan",
            "KKK",
            "the Klan",
            "K.K.K.",
            "Klu Klux Klan"
        ],
        "prompt": [],
        "wrong": [
            "Jim Crow laws",
            "White League",
            "Red Shirts",
            "Know-Nothings",
            "Black Codes",
            "Knights of the White Camellia"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
