import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "eminent-domain",
    "name": "Eminent domain",
    "mono": "EMD",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "Government power to take private property · Requires “just compensation”",
    "dates": "Limited by the Fifth Amendment (1791)",
    "briefing": "Can the government take your house? Yes, if it needs the land for a public use, like a highway, a school, or a park, and it pays you a fair price. The Fifth Amendment’s Takings Clause says private property shall not be “taken for public use, without just compensation.” In _Kelo v. City of New London_ (2005), the Supreme Court ruled 5–4 that a city could take homes for an economic development plan, and many states then passed new limits on this power.",
    "answerHtml": "<b><u>eminent domain</u></b> (prompt on <u>takings</u> or <u>condemnation</u>; do not accept “Fifth Amendment,” “Takings Clause,” or “zoning”)",
    "accept": [
        "eminent domain",
        "imminent domain",
        "power of eminent domain",
        "right of eminent domain",
        "eminent domain power"
    ],
    "prompt": [
        "takings",
        "taking",
        "government takings",
        "government taking",
        "condemnation",
        "expropriation",
        "taking private property",
        "taking property"
    ],
    "reject": [
        "fifth amendment",
        "5th amendment",
        "amendment v",
        "amendment 5",
        "amendment five",
        "takings clause",
        "just compensation",
        "just compensation clause",
        "public use",
        "public use clause",
        "zoning",
        "zoning law",
        "zoning laws",
        "police power",
        "police powers",
        "adverse possession",
        "public domain",
        "kelo",
        "kelo v city of new london",
        "kelo v new london",
        "berman v parker",
        "fourteenth amendment",
        "14th amendment",
        "due process",
        "due process clause",
        "urban renewal",
        "nationalization",
        "regulatory taking",
        "regulatory takings",
        "inverse condemnation",
        "eviction",
        "foreclosure",
        "easement",
        "property tax",
        "homestead act",
        "squatting"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Eminent_domain_in_the_United_States",
    "qb": {
        "q": "eminent domain",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "The Dutch legal scholar Hugo Grotius [“GROH-shee-us”] coined the Latin name for this power in a 1625 book on the law of war and peace. He argued that a state could take its subjects’ property for public needs, but that it should pay them for what it took.",
            "r": "For 10 points, name this government power to take private property for public use."
        },
        {
            "p": "In a dissent about this power, Sandra Day O’Connor warned that nothing would stop a government from replacing “any Motel 6 with a Ritz-Carlton” or “any home with a shopping mall.” The majority ruled that a Connecticut city’s economic development plan counted as a “public use.”",
            "r": "That 2005 case was _Kelo v. City of New London_. For 10 points, name this power to take private property."
        },
        {
            "p": "In _Berman v. Parker_, a unanimous Supreme Court let Washington, D.C., use this power on a department store that was not itself run-down, as part of a plan to rebuild a whole neighborhood. William O. Douglas wrote that a community may choose to be “beautiful as well as healthy.”",
            "r": "For 10 points, name this government power to take private property for public use."
        },
        {
            "p": "In a 1984 case, the Supreme Court let Hawaii use this power to break up huge estates by moving land from a few large landowners to the people who leased homes on it. Sandra Day O’Connor wrote that opinion, though two decades later she dissented in a famous case about the same power.",
            "r": "For 10 points, name this government power, which the Fifth Amendment limits."
        },
        {
            "p": "In 1857, New York City used this power to remove the residents of Seneca Village, a community where many African American families owned land, to make room for Central Park. The landowners were paid for their property, as the law required.",
            "r": "For 10 points, name this power of a government to take private property for public use if it pays the owner."
        },
        {
            "p": "In an 1897 case about a railroad’s land in Chicago, the Supreme Court ruled that states, not just the national government, must pay “just compensation” when they use this power. That decision is often called the first to apply part of the Bill of Rights to the states through the Fourteenth Amendment.",
            "r": "For 10 points, name this government power to take private property for public use."
        },
        {
            "p": "In 1981, Michigan’s top court let Detroit use this power to clear a neighborhood called Poletown so that General Motors could build a car factory. The same court reversed itself in 2004, ruling that taking property just to boost the economy broke the state’s constitution.",
            "r": "For 10 points, name this power of governments to take private land for public use."
        },
        {
            "p": "New York planner Robert Moses used this power to clear land for highways such as the Cross Bronx Expressway, forcing thousands of people to move. In the 1950s and 1960s, many cities also used it for “urban renewal” projects that tore down older neighborhoods.",
            "r": "For 10 points, name this government power to take private property in exchange for “just compensation.”"
        },
        {
            "p": "In _Kohl v. United States_ (1875), the Supreme Court ruled that the national government itself could use this power, in a case about land for federal offices in Cincinnati. Courts call the legal process of using this power “condemnation.”",
            "r": "For 10 points, name this power of a government to take private property for public use."
        },
        {
            "p": "After a 2005 Supreme Court decision about this power, dozens of states passed laws limiting it, and the land at the center of the case stayed empty for years. Supporters of the ruling said it let cities rebuild struggling economies, while critics said it put ordinary people’s homes at risk.",
            "r": "That case was _Kelo v. City of New London_. For 10 points, name this government power to take private property."
        },
        {
            "p": "Susette Kelo’s “little pink house,” which a Connecticut city wanted for a development plan near a Pfizer research center, became a symbol in a fight over this power. After she lost her case, the house was moved to another spot in the city.",
            "r": "The Supreme Court ruled 5–4 against her in 2005. For 10 points, name this power of governments to take private property."
        },
        {
            "p": "In the 1950s, Los Angeles used this power to clear Chavez Ravine, a mostly Mexican American neighborhood, for a public housing project that was later canceled. The land was then used to build Dodger Stadium.",
            "r": "For 10 points, name this government power to take private property for public use, as long as the owner is fairly paid."
        },
        {
            "p": "The Tennessee Valley Authority used this power in the 1930s to acquire farms that would be flooded by its new dams, and states later used it to build the Interstate Highway System. In each case, owners had to be paid for their land.",
            "r": "For 10 points, name this government power to take private property for public use."
        },
        {
            "p": "The Massachusetts Constitution of 1780 promised “a reasonable compensation” to anyone whose property was taken for public uses, an early limit on this power. A national limit followed in 1791, when the Bill of Rights was ratified.",
            "r": "For 10 points, name this government power to take private property for public use, which the Fifth Amendment says requires “just compensation.”"
        },
        {
            "p": "In the 1800s, many states let private canal and railroad companies use this power to get land for their routes, on the grounds that those projects served the public. Utility companies have also used it to build power lines.",
            "r": "For 10 points, name this power to take private property for public use, as long as the owner receives “just compensation.”"
        }
    ],
    "clues": [
        {
            "id": "definition",
            "tier": "giveaway",
            "t": "The government’s power to take private property for public use",
            "k": ["take private property", "public use", "government"],
            "n": 0
        },
        {
            "id": "takings-clause",
            "tier": "giveaway",
            "t": "Limited by the Fifth Amendment’s Takings Clause: property may not be taken “for public use, without just compensation”",
            "k": ["fifth amendment", "takings clause", "just compensation"],
            "n": 0,
            "rabbit": "Bill of Rights"
        },
        {
            "id": "uses",
            "tier": "giveaway",
            "t": "Used to get land for highways, schools, parks, dams, and railroads",
            "k": ["highways", "schools", "parks"],
            "n": 0
        },
        {
            "id": "kelo",
            "tier": "giveaway",
            "t": "_Kelo v. City of New London_ (2005): the Supreme Court ruled 5–4 that a city could take homes for an economic development plan",
            "k": ["kelo", "new london", "2005"],
            "n": 0
        },
        {
            "id": "fair-market",
            "tier": "middle",
            "t": "“Just compensation” usually means the property’s fair market value",
            "k": ["fair market value"],
            "n": 0
        },
        {
            "id": "condemnation",
            "tier": "middle",
            "t": "The legal process of using it is called condemnation",
            "k": ["condemnation"],
            "n": 0
        },
        {
            "id": "oconnor-dissent",
            "tier": "middle",
            "t": "Sandra Day O’Connor’s _Kelo_ dissent: nothing stops replacing “any Motel 6 with a Ritz-Carlton”",
            "k": ["o’connor", "oconnor", "motel 6", "ritz-carlton"],
            "n": 0
        },
        {
            "id": "berman",
            "tier": "middle",
            "t": "_Berman v. Parker_ (1954): a unanimous ruling upheld a D.C. urban renewal plan; William O. Douglas: “beautiful as well as healthy”",
            "k": ["berman", "parker", "beautiful as well as healthy"],
            "n": 0
        },
        {
            "id": "kelo-views",
            "tier": "middle",
            "t": "Supporters said _Kelo_ helped cities rebuild struggling economies; critics said it put homes at risk; dozens of states then limited such takings",
            "k": ["supporters", "critics", "dozens of states"],
            "n": 0
        },
        {
            "id": "pink-house",
            "tier": "middle",
            "t": "Susette Kelo’s “little pink house” in Connecticut became a symbol of the case",
            "k": ["susette kelo", "pink house", "connecticut"],
            "n": 0
        },
        {
            "id": "urban-renewal",
            "tier": "middle",
            "t": "Used in 1950s–1960s “urban renewal” and by Robert Moses for highways like the Cross Bronx Expressway",
            "k": ["urban renewal", "robert moses", "cross bronx"],
            "n": 0
        },
        {
            "id": "grotius",
            "tier": "power",
            "t": "Hugo Grotius coined its Latin name in a 1625 book on the law of war and peace",
            "k": ["grotius", "1625", "war and peace"],
            "n": 0
        },
        {
            "id": "midkiff",
            "tier": "power",
            "t": "_Hawaii Housing Authority v. Midkiff_ (1984): O’Connor’s opinion let Hawaii break up large estates",
            "k": ["midkiff", "hawaii", "estates"],
            "n": 0
        },
        {
            "id": "chicago-railroad",
            "tier": "power",
            "t": "An 1897 Chicago railroad case required states to pay too; often called the first case applying part of the Bill of Rights to the states",
            "k": ["1897", "railroad", "bill of rights"],
            "n": 0
        },
        {
            "id": "kohl",
            "tier": "power",
            "t": "_Kohl v. United States_ (1875): the national government may use it too",
            "k": ["kohl", "1875", "national government"],
            "n": 0
        },
        {
            "id": "seneca-village",
            "tier": "power",
            "t": "New York City used it in 1857 to remove Seneca Village, a largely African American community, for Central Park",
            "k": ["seneca village", "central park", "1857"],
            "n": 0
        },
        {
            "id": "poletown",
            "tier": "power",
            "t": "Michigan’s _Poletown_ ruling (1981) let Detroit clear a neighborhood for a General Motors plant; reversed in 2004",
            "k": ["poletown", "detroit", "general motors"],
            "n": 0
        },
        {
            "id": "chavez-ravine",
            "tier": "power",
            "t": "Los Angeles cleared Chavez Ravine in the 1950s; the land became the site of Dodger Stadium",
            "k": ["chavez ravine", "dodger stadium"],
            "n": 0
        },
        {
            "id": "tva",
            "tier": "power",
            "t": "The Tennessee Valley Authority used it for land flooded by its dams; states used it for the Interstate Highway System",
            "k": ["tennessee valley authority", "dams", "interstate"],
            "n": 0
        },
        {
            "id": "massachusetts-1780",
            "tier": "power",
            "t": "The Massachusetts Constitution of 1780 promised “a reasonable compensation”",
            "k": ["massachusetts", "1780", "reasonable compensation"],
            "n": 0
        },
        {
            "id": "railroads",
            "tier": "power",
            "t": "In the 1800s, states let private canal and railroad companies use it",
            "k": ["canal", "railroad", "1800s"],
            "n": 0
        },
        {
            "id": "pfizer",
            "tier": "power",
            "t": "The _Kelo_ plan was tied to a Pfizer research center; the land stayed empty for years",
            "k": ["pfizer", "empty"],
            "n": 0
        }
    ],
    "trap": {
        "title": "The power, not the amendment",
        "body": "Almost every tossup on this power mentions the Fifth Amendment, its Takings Clause, or “just compensation,” and those words tempt early buzzes. But the Fifth Amendment does not create this power; it limits it by requiring payment, so naming the amendment or the clause answers a different question and is ruled wrong here. Zoning, which controls how land may be used without taking it, is also wrong.",
        "fix": "If the question asks for “this power” or “this practice” of taking property for public use, say “eminent domain.” Save “Fifth Amendment” for “this amendment” and “Takings Clause” for “this clause.” Saying only “takings” or “condemnation” earns a prompt.",
        "line": "Real answer line: <b><u>eminent domain</u></b> (prompt on <u>takings</u> or <u>condemnation</u>; do not accept “Fifth Amendment” or “zoning”)"
    },
    "tests": {
        "right": [
            "eminent domain",
            "Eminent Domain",
            "imminent domain",
            "power of eminent domain",
            "eminant domain"
        ],
        "prompt": [
            "takings",
            "condemnation"
        ],
        "wrong": [
            "Fifth Amendment",
            "Takings Clause",
            "zoning",
            "just compensation",
            "police power",
            "Kelo v. City of New London",
            "public domain"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
