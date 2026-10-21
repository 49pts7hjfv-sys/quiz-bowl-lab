import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "great-chicago-fire",
    "name": "Great Chicago Fire",
    "mono": "GCF",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "Burned the heart of Chicago in October 1871 · Blamed in legend on a cow",
    "dates": "October 8–10, 1871",
    "briefing": "On the night of October 8, 1871, a fire started in or near the O’Leary family’s barn on Chicago’s West Side. Pushed by strong winds through a city built mostly of wood, it burned for more than a day, killing about 300 people and leaving about 100,000 homeless. Legend blamed Mrs. O’Leary’s cow for kicking over a lantern, but that story was never proven, and Chicago rebuilt with some of the world’s first skyscrapers.",
    "answerHtml": "Great <b><u>Chicago Fire</u></b> (accept <u>Great Fire of 1871</u>; prompt on <u>Chicago</u> or <u>Great Fire</u>; do not accept “Peshtigo Fire”)",
    "accept": [
        "great chicago fire",
        "the great chicago fire",
        "chicago fire",
        "the chicago fire",
        "great chicago fire of 1871",
        "chicago fire of 1871",
        "1871 chicago fire",
        "chicago fire 1871",
        "great fire of chicago",
        "the great fire of chicago",
        "chicago great fire",
        "great fire of 1871",
        "the great fire of 1871"
    ],
    "prompt": [
        "chicago",
        "great fire",
        "the great fire",
        "fire",
        "fire of 1871",
        "1871 fire",
        "the 1871 fire"
    ],
    "reject": [
        "peshtigo fire",
        "peshtigo",
        "great peshtigo fire",
        "great michigan fire",
        "great boston fire",
        "great baltimore fire",
        "great fire of london",
        "san francisco earthquake",
        "1906 san francisco earthquake",
        "great san francisco earthquake",
        "iroquois theater fire",
        "iroquois theatre fire",
        "our lady of the angels school fire",
        "triangle shirtwaist fire",
        "triangle shirtwaist factory fire",
        "great hinckley fire",
        "johnstown flood",
        "galveston hurricane",
        "haymarket affair",
        "haymarket riot",
        "pullman strike",
        "worlds columbian exposition",
        "columbian exposition",
        "chicago illinois",
        "chicago river",
        "mrs oleary",
        "mrs olearys cow",
        "olearys cow",
        "catherine oleary",
        "oleary"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Great_Chicago_Fire",
    "qb": {
        "q": "Chicago Fire",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "The roof of a waterworks pumping station caught fire during this disaster, and its pumps stopped working, leaving firefighters without water. Flaming debris carried by strong winds from the southwest helped this disaster jump the main branch of a river and spread into the North Side.",
            "r": "Legend blamed a cow for starting it. For 10 points, name this 1871 disaster that destroyed much of Chicago."
        },
        {
            "p": "A neighbor nicknamed “Peg Leg,” Daniel Sullivan, told investigators that he was the first person to see this fire and that he hurried into a burning barn to try to save the animals inside. One later historian argued that Sullivan himself may have started it.",
            "r": "The barn belonged to Patrick and Catherine O’Leary. For 10 points, name this 1871 fire that destroyed much of Chicago."
        },
        {
            "p": "Days after this disaster, Mayor Roswell Mason put General Philip Sheridan, a Civil War cavalry commander, in charge of keeping order in the city. Relief money and supplies poured in from across the country and from Europe.",
            "r": "This disaster left about 100,000 people homeless. For 10 points, name this fire of October 1871 that burned much of Chicago."
        },
        {
            "p": "Weeks after this disaster, newspaper publisher Joseph Medill [“meh-DILL”] was elected mayor on a “Fireproof” ticket and pushed for stricter fire codes. Medill’s newspaper, the _Tribune_, had lost its own building in this disaster but soon printed an editorial headlined “Cheer Up.”",
            "r": "Legend says this fire began when Mrs. O’Leary’s cow kicked over a lantern. For 10 points, name this 1871 fire."
        },
        {
            "p": "After this disaster, British donors, including Queen Victoria, sent thousands of books across the Atlantic to help the stricken city found its first free public library. That library opened its doors on New Year’s Day, 1873, inside an old iron water tank.",
            "r": "Much of the city’s downtown burned. For 10 points, name this 1871 fire blamed in legend on Mrs. O’Leary’s cow."
        },
        {
            "p": "One of the four red six-pointed stars on a city’s flag stands for this event, while two others honor world’s fairs held in 1893 and 1933. That city’s firefighter training academy was later built on the spot where this event began.",
            "r": "This event began in or near a barn owned by the O’Leary family. For 10 points, name this 1871 fire."
        },
        {
            "p": "The house of the family blamed for this disaster survived it, because strong winds from the southwest pushed the flames northeast, away from the home and toward the business district. The fire jumped the South Branch of the river within a few hours.",
            "r": "In 1997, the city council cleared Catherine O’Leary and her cow of blame. For 10 points, name this 1871 fire."
        },
        {
            "p": "Potter Palmer’s grand new hotel, the Palmer House, burned in this disaster just 13 days after it opened. Palmer quickly built a larger replacement, one of many new buildings made of brick, stone, and iron instead of wood.",
            "r": "Rebuilding after this fire led to some of the world’s first skyscrapers. For 10 points, name this 1871 disaster in Chicago."
        },
        {
            "p": "On the same night that this fire began, a far deadlier forest fire destroyed the Wisconsin town of Peshtigo [“PESH-tih-goh”], killing more than 1,000 people. Fires also burned the Michigan town of Holland that night, after a long, dry summer across the Midwest.",
            "r": "It killed about 300 people in a big Midwestern city. For 10 points, name this October 1871 fire, legendarily started by Mrs. O’Leary’s cow."
        },
        {
            "p": "Architects Daniel Burnham and John Root formed their partnership two years after this disaster, as builders rushed to replace thousands of lost buildings. William Le Baron Jenney’s Home Insurance Building, finished in 1885 in the rebuilt downtown, is often called the first skyscraper.",
            "r": "For 10 points, name this 1871 disaster that destroyed much of Chicago, blamed in legend on a cow."
        },
        {
            "p": "Fire Prevention Week is held each year during the week that includes October 9, in memory of this disaster. Late on that date, rain began to fall and helped put out this disaster, which had burned for more than a day across about three square miles.",
            "r": "It destroyed more than 17,000 buildings. For 10 points, name this 1871 fire that destroyed much of Chicago."
        },
        {
            "p": "One of the few buildings in this disaster’s path to survive was a castle-like limestone water tower designed by William W. Boyington and finished in 1869. That tower became a symbol of the city’s recovery.",
            "r": "Legend blamed this disaster on Mrs. O’Leary’s cow. For 10 points, name this 1871 fire that destroyed much of Chicago."
        },
        {
            "p": "After a summer of drought, wooden sidewalks, wooden houses, and piles of lumber helped fuel this disaster, and blowing embers let it leap across a river. Firefighters were already worn out from battling a large fire in the same part of the city the night before.",
            "r": "It killed about 300 people and left about 100,000 homeless. For 10 points, name this 1871 fire that destroyed much of Chicago."
        },
        {
            "p": "During this disaster, the courthouse that also served as City Hall burned, and the great bell that had been ringing the alarm crashed down through its tower. Even so, the city grew so quickly afterward that its population passed one million by 1890.",
            "r": "For 10 points, name this fire of October 1871, which legend blames on Mrs. O’Leary’s cow."
        },
        {
            "p": "A private charity called the Relief and Aid Society handed out donated food, clothing, and building supplies to families left homeless by this disaster. Twenty-two years later, the rebuilt city hosted the World’s Columbian Exposition, a world’s fair nicknamed the “White City.”",
            "r": "About 300 people died in this disaster. For 10 points, name this October 1871 fire that destroyed much of Chicago."
        }
    ],
    "clues": [
        {
            "id": "october-1871",
            "tier": "giveaway",
            "t": "Burned much of Chicago from October 8 to 10, 1871",
            "k": ["october 8", "1871", "burned"],
            "n": 0,
            "rabbit": "Chicago"
        },
        {
            "id": "cow-legend",
            "tier": "giveaway",
            "t": "Legend blamed Mrs. Catherine O’Leary’s cow for kicking over a lantern in her barn",
            "k": ["o’leary", "oleary", "cow", "lantern"],
            "n": 0
        },
        {
            "id": "toll",
            "tier": "giveaway",
            "t": "Killed about 300 people and left about 100,000 homeless, about a third of the city",
            "k": ["300 people", "100,000", "homeless"],
            "n": 0
        },
        {
            "id": "rebuilt",
            "tier": "giveaway",
            "t": "The city rebuilt with stricter building codes and some of the world’s first skyscrapers",
            "k": ["skyscrapers", "rebuilt", "building codes"],
            "n": 0
        },
        {
            "id": "barn",
            "tier": "middle",
            "t": "Started on the night of October 8 in or near the O’Leary barn on DeKoven Street, southwest of downtown",
            "k": ["dekoven street", "dekoven", "barn"],
            "n": 0
        },
        {
            "id": "water-tower",
            "tier": "middle",
            "t": "The limestone Water Tower (1869) was one of the few buildings in its path to survive",
            "k": ["water tower", "limestone", "1869"],
            "n": 0
        },
        {
            "id": "peshtigo",
            "tier": "middle",
            "t": "The same night, the far deadlier Peshtigo Fire in Wisconsin killed more than 1,000 people, and fires also burned Holland, Michigan",
            "k": ["peshtigo", "holland"],
            "n": 0
        },
        {
            "id": "cleared-1997",
            "tier": "middle",
            "t": "In 1997, the city council passed a resolution clearing Catherine O’Leary and her cow",
            "k": ["1997", "resolution", "clearing"],
            "n": 0
        },
        {
            "id": "wind-wood",
            "tier": "middle",
            "t": "Drought, strong southwest winds, and a city built mostly of wood helped it spread; blowing embers carried it across the river",
            "k": ["drought", "southwest winds", "wood", "embers"],
            "n": 0
        },
        {
            "id": "home-insurance",
            "tier": "middle",
            "t": "The rebuilt downtown got William Le Baron Jenney’s Home Insurance Building (1885), often called the first skyscraper",
            "k": ["home insurance", "jenney", "1885"],
            "n": 0
        },
        {
            "id": "prevention-week",
            "tier": "middle",
            "t": "Fire Prevention Week is held every year during the week that includes October 9, in its memory",
            "k": ["prevention week", "october 9", "prevention"],
            "n": 0
        },
        {
            "id": "rain",
            "tier": "middle",
            "t": "Rain late on October 9 helped end it after it had burned about three square miles and more than 17,000 buildings",
            "k": ["rain", "17,000", "three square miles"],
            "n": 0
        },
        {
            "id": "waterworks",
            "tier": "power",
            "t": "The waterworks pumping station’s roof caught fire and its pumps stopped, cutting off the city’s water",
            "k": ["waterworks", "pumping station", "pumps"],
            "n": 0
        },
        {
            "id": "sullivan",
            "tier": "power",
            "t": "Neighbor Daniel “Peg Leg” Sullivan told investigators he saw it first and tried to save the animals in the barn",
            "k": ["peg leg", "sullivan", "daniel"],
            "n": 0
        },
        {
            "id": "sheridan",
            "tier": "power",
            "t": "Mayor Roswell Mason put General Philip Sheridan in charge of keeping order",
            "k": ["sheridan", "mason"],
            "n": 0
        },
        {
            "id": "medill",
            "tier": "power",
            "t": "_Tribune_ publisher Joseph Medill, whose paper printed a “Cheer Up” editorial, was elected mayor weeks later on a “Fireproof” ticket",
            "k": ["medill", "mayor"],
            "n": 0
        },
        {
            "id": "library",
            "tier": "power",
            "t": "British donors, including Queen Victoria, sent thousands of books that started the city’s free public library (opened 1873 in an old water tank)",
            "k": ["queen victoria", "public library", "water tank", "books"],
            "n": 0
        },
        {
            "id": "flag-star",
            "tier": "power",
            "t": "One of the four red stars on the city’s flag stands for it",
            "k": ["four red stars", "flag", "stars"],
            "n": 0
        },
        {
            "id": "academy",
            "tier": "power",
            "t": "The city’s firefighter training academy was later built where the O’Leary barn stood",
            "k": ["training academy", "academy", "firefighter"],
            "n": 0
        },
        {
            "id": "house-survived",
            "tier": "power",
            "t": "The O’Learys’ house survived because the wind pushed the flames northeast, away from it",
            "k": ["northeast", "house survived", "wind"],
            "n": 0
        },
        {
            "id": "palmer-house",
            "tier": "power",
            "t": "Potter Palmer’s new hotel, the Palmer House, burned just 13 days after it opened",
            "k": ["palmer house", "potter palmer", "13 days"],
            "n": 0
        },
        {
            "id": "night-before",
            "tier": "power",
            "t": "Firefighters were worn out from battling a large blaze in the same area the night before, October 7",
            "k": ["night before", "worn out", "october 7"],
            "n": 0
        },
        {
            "id": "burnham-root",
            "tier": "power",
            "t": "Daniel Burnham and John Root formed their architecture firm in 1873 as the city rebuilt",
            "k": ["burnham", "john root", "1873"],
            "n": 0
        },
        {
            "id": "courthouse-bell",
            "tier": "power",
            "t": "The courthouse, which also served as City Hall, burned, and its alarm bell crashed down through the tower",
            "k": ["courthouse", "city hall", "bell"],
            "n": 0
        },
        {
            "id": "relief-aid",
            "tier": "power",
            "t": "The Relief and Aid Society gave out donated food, clothing, and building supplies to the homeless",
            "k": ["relief and aid", "donated", "society"],
            "n": 0
        },
        {
            "id": "columbian",
            "tier": "power",
            "t": "Twenty-two years later, the rebuilt city hosted the World’s Columbian Exposition (1893), the “White City”",
            "k": ["columbian exposition", "white city", "1893"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Fire, city, or Peshtigo?",
        "body": "Questions about Chicago itself often use this fire as a clue, so a tossup that asks for “this city” wants Chicago, not the fire. The Peshtigo Fire in Wisconsin started the same night and killed far more people, and it is a different answer. Saying only “Chicago” on a fire question earns just a prompt, so be ready to say the whole name.",
        "fix": "Listen for the noun: “this fire” or “this disaster” with Mrs. O’Leary’s cow, the Water Tower, or 1871 means the Great Chicago Fire; “this city” means Chicago; a fire in the Wisconsin woods means Peshtigo. Don’t mix it up with the 1906 San Francisco earthquake, which also set off huge fires.",
        "line": "Real answer line: Great <b><u>Chicago Fire</u></b> (accept <u>Great Fire of 1871</u>; prompt on <u>Chicago</u>; do not accept “Peshtigo Fire”)"
    },
    "tests": {
        "right": [
            "Great Chicago Fire",
            "Chicago Fire",
            "the Great Chicago Fire of 1871",
            "Great Chicago Fier",
            "Great Fire of 1871"
        ],
        "prompt": [
            "Chicago",
            "Great Fire"
        ],
        "wrong": [
            "Peshtigo Fire",
            "San Francisco earthquake",
            "Great Fire of London",
            "Haymarket Affair",
            "Chicago, Illinois",
            "Mrs. O'Leary's cow",
            "Great Boston Fire"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("wrote", data["id"])
