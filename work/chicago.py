import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TIP = "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."

data = {
    "id": "chicago",
    "name": "Chicago",
    "mono": "CHI",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "Illinois’s largest city, on Lake Michigan · Rebuilt after the fire of 1871",
    "dates": "Incorporated as a city in 1837",
    "briefing": "Chicago began as a trading post where a small river meets Lake Michigan, and its name comes from a Native American word for a wild onion that grew there. Railroads, stockyards, and factories made it one of the fastest-growing cities in history. After the Great Chicago Fire of 1871 destroyed much of it, the city rebuilt with some of the world’s first skyscrapers.",
    "answerHtml": "<b><u>Chicago</u></b>, Illinois",
    "accept": [
        "chicago",
        "chicago illinois",
        "chicago il",
        "chicago ill",
        "city of chicago",
        "chicago city"
    ],
    "prompt": [],
    "reject": [
        "great chicago fire",
        "great chicago fire of 1871",
        "chicago fire",
        "great fire",
        "great fire of 1871",
        "al capone",
        "capone",
        "pullman strike",
        "pullman",
        "haymarket affair",
        "haymarket riot",
        "haymarket",
        "milwaukee",
        "detroit",
        "cleveland",
        "springfield",
        "springfield illinois",
        "peoria",
        "gary",
        "st louis",
        "saint louis",
        "cincinnati",
        "minneapolis",
        "new york",
        "new york city",
        "boston",
        "philadelphia",
        "lake michigan",
        "michigan",
        "cook county"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Chicago",
    "qb": {
        "q": "Chicago",
        "found": 0,
        "tip": TIP
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "A trader of African descent, Jean Baptiste Point du Sable, is often called this city’s founder because he built a farm and trading post here in the 1780s. The U.S. Army built Fort Dearborn at this spot in 1803, but the fort was destroyed during the War of 1812.",
            "r": "This city later became the nation’s biggest railroad hub. For 10 points, name this city on Lake Michigan, the largest in Illinois."
        },
        {
            "p": "In 1900, engineers opened the Sanitary and Ship Canal, which reversed the flow of this city’s river to carry sewage away from the lake that supplies its drinking water. That river is dyed green every Saint Patrick’s Day.",
            "r": "The Illinois and Michigan Canal, finished in 1848, had earlier linked this city to the Mississippi River system. For 10 points, name this largest city in Illinois."
        },
        {
            "p": "Upton Sinclair’s novel _The Jungle_ follows Jurgis Rudkus, a Lithuanian immigrant who works in the meatpacking plants near this city’s Union Stock Yards. A Carl Sandburg poem calls this city the “Hog Butcher for the World” and the “City of the Big Shoulders.”",
            "r": "This city on Lake Michigan is nicknamed the “Windy City.” For 10 points, name this largest city in Illinois."
        },
        {
            "p": "In 1886, a bomb exploded as police moved to break up a labor rally in this city’s Haymarket Square, where workers had gathered to support an eight-hour workday. Eight anarchists were convicted after that event, which is remembered each May Day around the world.",
            "r": "For 10 points, name this city where, according to legend, Mrs. O’Leary’s cow started a great fire in 1871."
        },
        {
            "p": "At a meeting held during a world’s fair in this city, Frederick Jackson Turner presented his “frontier thesis,” arguing that the frontier had shaped American democracy. That 1893 fair, nicknamed the “White City,” introduced George Ferris’s giant wheel.",
            "r": "That fair was the World’s Columbian Exposition. For 10 points, name this Illinois city on Lake Michigan."
        },
        {
            "p": "In 1889, Jane Addams and Ellen Gates Starr opened Hull House, a settlement house that offered classes, child care, and other help to immigrant families in this city. Addams later became the first American woman to win the Nobel Peace Prize.",
            "r": "For 10 points, name this Illinois city where the gangster Al Capone made a fortune during Prohibition."
        },
        {
            "p": "William Le Baron Jenney’s Home Insurance Building, finished in this city in 1885, is often called the first skyscraper because a metal frame, not thick stone walls, held up its weight. Louis Sullivan, who wrote that “form ever follows function,” also designed tall buildings here.",
            "r": "This city’s Sears Tower was the world’s tallest building from 1973 to 1998. For 10 points, name this city."
        },
        {
            "p": "Robert Abbott’s weekly newspaper, the _Defender_, urged Black Southerners to move north to this city during the Great Migration, and many settled in its Bronzeville neighborhood. Muddy Waters and other musicians who moved here helped create an electric style of blues named for this city.",
            "r": "This city’s baseball teams are the Cubs and the White Sox. For 10 points, name this largest city in Illinois."
        },
        {
            "p": "Abraham Lincoln won the Republican nomination for president in 1860 at a convention hall in this city called the Wigwam. Thirty-six years later, William Jennings Bryan gave his “Cross of Gold” speech at a convention here.",
            "r": "Its nicknames include the “Windy City.” For 10 points, name this largest city in Illinois."
        },
        {
            "p": "Mayor Richard J. Daley led this city from 1955 until his death in 1976, and his son Richard M. Daley later served as its mayor for 22 years. In 1968, police clashed with antiwar protesters outside the Democratic National Convention in this city.",
            "r": "For 10 points, name this Illinois city whose O’Hare Airport is named for a World War II pilot."
        },
        {
            "p": "On December 2, 1942, Enrico Fermi’s team achieved the first self-sustaining nuclear chain reaction under the stands of Stagg Field, at a university in this city. In 1983, Harold Washington became this city’s first African American mayor.",
            "r": "For 10 points, name this city where the Sears Tower, later renamed the Willis Tower, was built."
        },
        {
            "p": "Eight players on this city’s American League baseball team were banned from the sport for life after being accused of losing the 1919 World Series on purpose. Those players, including “Shoeless” Joe Jackson, were nicknamed the “Black Sox.”",
            "r": "This city’s National League team, the Cubs, plays at Wrigley Field. For 10 points, name this city."
        },
        {
            "p": "Cyrus McCormick moved his factory for mechanical reapers to this city in 1847, and Aaron Montgomery Ward started one of the first mail-order catalog businesses here in 1872. Sears, Roebuck and Company later moved its catalog business here as well.",
            "r": "For 10 points, name this railroad hub on Lake Michigan, the largest city in Illinois."
        },
        {
            "p": "This city was incorporated as a town in 1833 and as a city in 1837, and its name comes from a Native American word for a wild onion or garlic plant that grew along its river. Its downtown business district is called the Loop.",
            "r": "Much of this city burned in a great fire in 1871. For 10 points, name this city on the southwestern shore of Lake Michigan."
        },
        {
            "p": "Daniel Burnham, who led the building of the 1893 world’s fair, later co-wrote a 1909 plan for this city calling for a chain of public parks along its lakefront. This city’s Art Institute owns Grant Wood’s _American Gothic_ and Edward Hopper’s _Nighthawks_.",
            "r": "For 10 points, name this city in Illinois, the third-largest city in the United States by population."
        }
    ],
    "clues": [
        {
            "id": "illinois-lake-michigan",
            "tier": "giveaway",
            "t": "Largest city in Illinois, on the southwestern shore of Lake Michigan",
            "k": ["illinois", "lake michigan", "largest city"],
            "n": 0
        },
        {
            "id": "great-fire",
            "tier": "giveaway",
            "t": "A great fire in 1871, blamed in legend on Mrs. O’Leary’s cow, destroyed much of it",
            "k": ["1871", "o’leary", "cow", "great fire"],
            "n": 0,
            "rabbit": "Great Chicago Fire"
        },
        {
            "id": "windy-city",
            "tier": "giveaway",
            "t": "Nicknamed the “Windy City” and the “Second City”",
            "k": ["windy city", "windy", "second city"],
            "n": 0
        },
        {
            "id": "capone",
            "tier": "giveaway",
            "t": "Prohibition gangster Al Capone’s bootlegging gang was based here; he was convicted of tax evasion in 1931",
            "k": ["al capone", "capone", "tax evasion"],
            "n": 0,
            "rabbit": "Al Capone"
        },
        {
            "id": "sears-tower",
            "tier": "giveaway",
            "t": "Its Sears Tower (renamed the Willis Tower in 2009) was the world’s tallest building from 1973 to 1998",
            "k": ["sears tower", "willis tower", "tallest"],
            "n": 0
        },
        {
            "id": "teams",
            "tier": "giveaway",
            "t": "Home of baseball’s Cubs, who play at Wrigley Field, and White Sox",
            "k": ["cubs", "wrigley field", "white sox"],
            "n": 0
        },
        {
            "id": "wild-onion",
            "tier": "middle",
            "t": "Its name comes from a Native American word for a wild onion or garlic plant",
            "k": ["wild onion", "onion", "garlic"],
            "n": 0
        },
        {
            "id": "columbian-exposition",
            "tier": "middle",
            "t": "Hosted the World’s Columbian Exposition (1893), the “White City,” which introduced the Ferris wheel",
            "k": ["columbian exposition", "white city", "ferris wheel", "1893"],
            "n": 0
        },
        {
            "id": "haymarket",
            "tier": "middle",
            "t": "Haymarket Affair (1886): a bomb exploded at a labor rally for the eight-hour workday",
            "k": ["haymarket", "1886", "eight-hour"],
            "n": 0,
            "rabbit": "Haymarket Affair"
        },
        {
            "id": "pullman",
            "tier": "middle",
            "t": "The Pullman Strike (1894) began in George Pullman’s company town, now part of the city",
            "k": ["pullman", "1894", "company town"],
            "n": 0,
            "rabbit": "Pullman Strike"
        },
        {
            "id": "the-jungle",
            "tier": "middle",
            "t": "Upton Sinclair’s _The Jungle_ (1906) exposed its meatpacking plants near the Union Stock Yards",
            "k": ["the jungle", "sinclair", "stock yards", "meatpacking"],
            "n": 0
        },
        {
            "id": "hull-house",
            "tier": "middle",
            "t": "Jane Addams and Ellen Gates Starr founded Hull House, a settlement house for immigrants, in 1889",
            "k": ["hull house", "jane addams", "addams", "settlement house"],
            "n": 0
        },
        {
            "id": "sandburg",
            "tier": "middle",
            "t": "Carl Sandburg’s poem calls it “Hog Butcher for the World” and “City of the Big Shoulders”",
            "k": ["sandburg", "hog butcher", "big shoulders"],
            "n": 0
        },
        {
            "id": "conventions",
            "tier": "middle",
            "t": "Lincoln was nominated at the Wigwam (1860); William Jennings Bryan gave the “Cross of Gold” speech here (1896)",
            "k": ["wigwam", "cross of gold", "1860"],
            "n": 0,
            "rabbit": "William Jennings Bryan"
        },
        {
            "id": "ohare",
            "tier": "middle",
            "t": "O’Hare International Airport is named for World War II Navy pilot Butch O’Hare",
            "k": ["o’hare", "butch", "airport"],
            "n": 0
        },
        {
            "id": "du-sable",
            "tier": "power",
            "t": "Jean Baptiste Point du Sable, a trader of African descent, was its first permanent non-Native settler (1780s)",
            "k": ["du sable", "point du sable", "1780s"],
            "n": 0
        },
        {
            "id": "fort-dearborn",
            "tier": "power",
            "t": "Fort Dearborn (1803) was destroyed in the War of 1812; incorporated as a town in 1833 and a city in 1837",
            "k": ["fort dearborn", "dearborn", "1837"],
            "n": 0
        },
        {
            "id": "canal-river",
            "tier": "power",
            "t": "The Illinois and Michigan Canal (1848) linked it to the Mississippi; in 1900 the Sanitary and Ship Canal reversed its river’s flow",
            "k": ["illinois and michigan canal", "sanitary and ship canal", "reversed", "1900"],
            "n": 0
        },
        {
            "id": "skyscraper",
            "tier": "power",
            "t": "William Le Baron Jenney’s Home Insurance Building (1885), often called the first skyscraper; Louis Sullivan: “form ever follows function”",
            "k": ["home insurance", "jenney", "louis sullivan", "sullivan"],
            "n": 0
        },
        {
            "id": "turner",
            "tier": "power",
            "t": "At a meeting during the 1893 fair, Frederick Jackson Turner presented his “frontier thesis”; Daniel Burnham led the fair’s building",
            "k": ["frederick jackson turner", "turner", "frontier thesis", "burnham"],
            "n": 0
        },
        {
            "id": "great-migration",
            "tier": "power",
            "t": "Robert Abbott’s _Defender_ newspaper drew Black Southerners here in the Great Migration; many settled in Bronzeville, and Muddy Waters helped create its electric blues",
            "k": ["defender", "great migration", "bronzeville", "muddy waters"],
            "n": 0
        },
        {
            "id": "fermi",
            "tier": "power",
            "t": "Enrico Fermi’s team made the first self-sustaining nuclear chain reaction under the stands of Stagg Field (December 2, 1942)",
            "k": ["fermi", "chain reaction", "stagg field", "1942"],
            "n": 0,
            "rabbit": "Enrico Fermi"
        },
        {
            "id": "daley",
            "tier": "power",
            "t": "Mayors Richard J. Daley (1955–1976) and his son Richard M. Daley (1989–2011); protests outside the 1968 Democratic convention",
            "k": ["daley", "1968", "democratic convention"],
            "n": 0
        },
        {
            "id": "harold-washington",
            "tier": "power",
            "t": "Harold Washington became its first African American mayor in 1983",
            "k": ["harold washington", "1983", "mayor"],
            "n": 0
        },
        {
            "id": "black-sox",
            "tier": "power",
            "t": "Black Sox Scandal: eight White Sox players were banned after being accused of losing the 1919 World Series on purpose",
            "k": ["black sox", "1919", "shoeless joe"],
            "n": 0
        },
        {
            "id": "mail-order",
            "tier": "power",
            "t": "Cyrus McCormick’s reaper factory (1847); Montgomery Ward (1872) and Sears, Roebuck mail-order catalogs",
            "k": ["mccormick", "reaper", "montgomery ward", "mail-order"],
            "n": 0
        },
        {
            "id": "burnham-plan",
            "tier": "power",
            "t": "Daniel Burnham’s 1909 plan called for public parks along its lakefront; its Art Institute owns _American Gothic_ and _Nighthawks_",
            "k": ["burnham", "lakefront", "art institute"],
            "n": 0
        }
    ],
    "trap": {
        "title": "City or event?",
        "body": "Several separate answer lines are packed with clues about this city: the Great Chicago Fire (1871), the Haymarket Affair (1886), the Pullman Strike (1894), and the gangster Al Capone. A tossup that asks for “this fire,” “this strike,” or “this gangster” wants one of those, not the city. Also, Chicago is not the capital of Illinois; Springfield is.",
        "fix": "Listen for the noun: “this city” wants Chicago. Mrs. O’Leary’s cow, Haymarket Square, George Pullman, and Al Capone can all show up inside a Chicago tossup, so if you are unsure what is being asked, wait for the last line.",
        "line": "Real answer line: <b><u>Chicago</u></b>, Illinois"
    },
    "tests": {
        "right": [
            "Chicago",
            "Chicago, Illinois",
            "Chicgo",
            "City of Chicago",
            "Chicago IL"
        ],
        "prompt": [],
        "wrong": [
            "Great Chicago Fire",
            "Al Capone",
            "Milwaukee",
            "Springfield",
            "Illinois",
            "Haymarket Affair",
            "Pullman Strike",
            "Detroit"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
