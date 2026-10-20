import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "great-depression",
    "name": "Great Depression",
    "mono": "GD",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "The economic collapse of the 1930s · Began with the 1929 stock market crash",
    "dates": "Began 1929; lasted through the 1930s",
    "briefing": "The Great Depression began when the New York stock market crashed in October 1929. Over the next few years, thousands of banks failed, and by 1933 about one in four American workers had no job. Families who lost their homes built shantytowns nicknamed “Hoovervilles,” after President Herbert Hoover, while dust storms drove farmers off the Great Plains, and the hard times lasted through the 1930s.",
    "answerHtml": "<b><u>Great Depression</u></b> (prompt on <u>Depression</u>; do not accept “Great Recession” or “New Deal”)",
    "accept": [
        "great depression",
        "the great depression",
        "depression of the 1930s",
        "1930s depression",
        "depression of 1929",
        "1929 depression"
    ],
    "prompt": [
        "depression",
        "the depression",
        "economic depression"
    ],
    "reject": [
        "great recession",
        "recession",
        "new deal",
        "dust bowl",
        "long depression",
        "panic of 1929",
        "panic of 1893",
        "panic of 1873",
        "panic of 1837",
        "panic of 1907",
        "stock market crash",
        "stock market crash of 1929",
        "wall street crash",
        "crash of 1929",
        "black tuesday",
        "black thursday",
        "hoovervilles",
        "hooverville",
        "herbert hoover",
        "roaring twenties",
        "great society",
        "great migration",
        "bonus army",
        "smoot hawley tariff",
        "smoot hawley"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Great_Depression",
    "qb": {
        "q": "Great Depression",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "Milton Friedman and Anna Schwartz blamed this crisis on the Federal Reserve, arguing in _A Monetary History of the United States_ that the Fed let the money supply shrink by about a third. In 2002, Ben Bernanke admitted the Fed’s role in this crisis, telling Friedman, “We did it. We’re very sorry.”",
            "r": "For 10 points, name this economic disaster of the 1930s that followed the stock market crash of 1929."
        },
        {
            "p": "More than a thousand economists signed a petition asking the president to veto a 1930 law that raised taxes on imported goods, but he signed it anyway. Other countries struck back with their own tariffs, and world trade shrank during this crisis.",
            "r": "That law was the Smoot–Hawley Tariff. For 10 points, name this economic crisis that began while Herbert Hoover was president."
        },
        {
            "p": "Troops led by Douglas MacArthur drove thousands of World War I veterans out of their camp at Anacostia [“an-uh-KOSS-tee-uh”] Flats during this crisis. Those veterans, called the Bonus Army, had marched to Washington in 1932 to demand early payment of bonuses that were not due until 1945.",
            "r": "For 10 points, name this economic crisis of the 1930s, when millions of Americans lost their jobs."
        },
        {
            "p": "During this period, people called old newspapers used as bedding “Hoover blankets” and turned their empty pockets inside out as “Hoover flags.” Cars pulled by mules because their owners could not afford gasoline were mocked as “Hoover wagons.”",
            "r": "Shantytowns of the homeless were called Hoovervilles. For 10 points, name this economic crisis that followed the 1929 stock market crash."
        },
        {
            "p": "Florence Owens Thompson was the subject of a 1936 photograph taken at a camp for pea pickers in Nipomo [“nih-POH-moh”], California, during this crisis. That photograph, Dorothea Lange’s _Migrant Mother_, shows a worried woman with her children.",
            "r": "For 10 points, name this economic crisis of the 1930s that Franklin Roosevelt fought with the New Deal."
        },
        {
            "p": "On April 14, 1935, a day remembered as “Black Sunday,” a giant dust storm rolled across the southern Great Plains during this period. Years of drought and over-plowing had turned parts of Oklahoma, Kansas, and Texas into the Dust Bowl.",
            "r": "For 10 points, name this economic crisis of the 1930s that began with a stock market crash."
        },
        {
            "p": "Karen Hesse’s Newbery Medal–winning novel _Out of the Dust_, written in free verse, follows an Oklahoma girl named Billie Jo during this period. An earlier novel set during this period follows the Joad family as they drive west on Route 66 to California.",
            "r": "That novel is John Steinbeck’s _The Grapes of Wrath_. For 10 points, name this economic crisis of the 1930s."
        },
        {
            "p": "In Christopher Paul Curtis’s novel _Bud, Not Buddy_, a ten-year-old orphan in Michigan searches for the man he believes is his father during this period. The musical _Annie_ is also set during this period, and in one song, people living in a shantytown sing “We’d Like to Thank You, Herbert Hoover.”",
            "r": "For 10 points, name this time of mass unemployment that followed the stock market crash of 1929."
        },
        {
            "p": "The failure of Austria’s largest bank, the Creditanstalt [“kreh-DEET-ahn-shtahlt”], in 1931 helped spread this crisis across Europe. Later that year, Britain abandoned the gold standard, and in Germany the hard times of this crisis helped the Nazi Party win votes.",
            "r": "In the United States, Franklin Roosevelt’s New Deal tried to end it. For 10 points, name this worldwide economic collapse of the 1930s."
        },
        {
            "p": "Yip Harburg wrote the words to “Brother, Can You Spare a Dime?,” a 1932 song in which a man who had built a railroad and fought in a war ends up standing in line, waiting for bread, during this period.",
            "r": "Soup kitchens and breadlines fed hungry people across the country during this crisis. For 10 points, name this economic disaster of the 1930s."
        },
        {
            "p": "In 1932, the president created the Reconstruction Finance Corporation to lend money to banks and railroads during this crisis. That president, who had praised “rugged individualism” in his 1928 campaign, lost the 1932 election in a landslide.",
            "r": "That president was Herbert Hoover. For 10 points, name this economic crisis that began during his term."
        },
        {
            "p": "Many investors had bought stocks “on margin,” using borrowed money, in the years before this crisis. Between 1929 and 1932, the Dow Jones Industrial Average lost almost 90 percent of its value, and it did not climb back to its 1929 peak until 1954.",
            "r": "At its worst, about one in four American workers had no job. For 10 points, name this economic disaster that Franklin Roosevelt’s New Deal fought."
        },
        {
            "p": "John Maynard Keynes [“KAYNZ”] argued in his 1936 book _The General Theory of Employment, Interest and Money_ that governments should spend more to fight slumps like this one. Thousands of American banks failed during this crisis, wiping out many families’ savings before federal deposit insurance existed.",
            "r": "For 10 points, name this economic disaster of the 1930s, which began with the stock market crash of 1929."
        },
        {
            "p": "Writer James Agee [“AY-jee”] and photographer Walker Evans spent the summer of 1936 with poor sharecropping families in Alabama, a project that became the book _Let Us Now Praise Famous Men_. Government photographers such as Dorothea Lange also recorded the hardships of this period.",
            "r": "For 10 points, name this time of economic hardship in the 1930s, when about a quarter of American workers had no job."
        },
        {
            "p": "During this period, Midwestern farmers organized “penny auctions,” bidding only pennies for farms being sold to pay debts and then handing the land back to its owners. Milo Reno’s Farmers’ Holiday Association urged farmers to stop sending crops to market until prices rose.",
            "r": "For 10 points, name this economic crisis of the 1930s, which began with the 1929 stock market crash."
        }
    ],
    "clues": [
        {
            "id": "worst-crisis",
            "tier": "giveaway",
            "t": "The worst economic crisis in U.S. history, lasting through the 1930s",
            "k": ["economic crisis", "1930s", "worst"],
            "n": 0
        },
        {
            "id": "crash-1929",
            "tier": "giveaway",
            "t": "Began with the stock market crash of October 1929",
            "k": ["stock market crash", "1929", "crash"],
            "n": 0
        },
        {
            "id": "hoover-fdr",
            "tier": "giveaway",
            "t": "Began under President Herbert Hoover; Franklin Roosevelt fought it with the New Deal",
            "k": ["herbert hoover", "hoover", "new deal", "roosevelt"],
            "n": 0,
            "rabbit": "New Deal"
        },
        {
            "id": "one-in-four",
            "tier": "giveaway",
            "t": "Unemployment reached about 25 percent, or one in four workers, in 1933",
            "k": ["unemployment", "25 percent", "one in four"],
            "n": 0
        },
        {
            "id": "black-tuesday",
            "tier": "middle",
            "t": "Black Tuesday (October 29, 1929) was the worst day of the crash",
            "k": ["black tuesday", "october 29"],
            "n": 0
        },
        {
            "id": "hoovervilles",
            "tier": "middle",
            "t": "Hoovervilles: shantytowns of homeless people, named for Herbert Hoover",
            "k": ["hoovervilles", "shantytowns"],
            "n": 0
        },
        {
            "id": "dust-bowl",
            "tier": "middle",
            "t": "The Dust Bowl: drought and dust storms drove farm families off the southern Great Plains",
            "k": ["dust bowl", "drought", "great plains", "dust storms"],
            "n": 0,
            "rabbit": "Dust Bowl"
        },
        {
            "id": "grapes-of-wrath",
            "tier": "middle",
            "t": "_The Grapes of Wrath_ (1939): John Steinbeck’s novel about the Joad family’s trip to California",
            "k": ["grapes of wrath", "steinbeck", "joad"],
            "n": 0,
            "rabbit": "The Grapes of Wrath"
        },
        {
            "id": "migrant-mother",
            "tier": "middle",
            "t": "_Migrant Mother_ (1936): Dorothea Lange’s photograph of a worried mother and her children",
            "k": ["migrant mother", "dorothea lange", "lange"],
            "n": 0
        },
        {
            "id": "bonus-army",
            "tier": "middle",
            "t": "Bonus Army (1932): World War I veterans marched on Washington for early payment of their bonuses",
            "k": ["bonus army", "veterans", "bonuses"],
            "n": 0
        },
        {
            "id": "smoot-hawley",
            "tier": "middle",
            "t": "Smoot–Hawley Tariff (1930) raised taxes on imports; other nations struck back and world trade shrank",
            "k": ["smoot", "hawley", "tariff"],
            "n": 0
        },
        {
            "id": "bank-failures",
            "tier": "middle",
            "t": "Thousands of banks failed; FDR declared a “bank holiday” in 1933, and the new FDIC began insuring deposits",
            "k": ["banks", "bank holiday", "fdic"],
            "n": 0
        },
        {
            "id": "breadlines",
            "tier": "middle",
            "t": "Breadlines and soup kitchens fed the hungry",
            "k": ["breadlines", "soup kitchens"],
            "n": 0
        },
        {
            "id": "anacostia",
            "tier": "power",
            "t": "Troops under Douglas MacArthur drove the Bonus Army from its camp at Anacostia Flats",
            "k": ["anacostia", "douglas macarthur", "macarthur"],
            "n": 0
        },
        {
            "id": "hoover-blankets",
            "tier": "power",
            "t": "“Hoover blankets” (old newspapers), “Hoover flags” (empty pockets), and “Hoover wagons” (cars pulled by mules)",
            "k": ["hoover blankets", "hoover flags", "hoover wagons", "newspapers"],
            "n": 0
        },
        {
            "id": "rfc",
            "tier": "power",
            "t": "Hoover, who praised “rugged individualism,” created the Reconstruction Finance Corporation (1932) to lend to banks and railroads",
            "k": ["reconstruction finance", "rugged individualism", "rfc"],
            "n": 0
        },
        {
            "id": "black-sunday",
            "tier": "power",
            "t": "“Black Sunday” (April 14, 1935): a giant dust storm swept the Great Plains",
            "k": ["black sunday", "1935"],
            "n": 0
        },
        {
            "id": "nipomo",
            "tier": "power",
            "t": "Florence Owens Thompson was photographed for _Migrant Mother_ at a pea pickers’ camp in Nipomo, California",
            "k": ["florence owens thompson", "nipomo", "pea pickers"],
            "n": 0
        },
        {
            "id": "friedman",
            "tier": "power",
            "t": "Milton Friedman and Anna Schwartz blamed the Federal Reserve for letting the money supply shrink by about a third",
            "k": ["friedman", "schwartz", "federal reserve", "money supply"],
            "n": 0
        },
        {
            "id": "bernanke",
            "tier": "power",
            "t": "Ben Bernanke (2002), on the Fed’s role: “We did it. We’re very sorry.”",
            "k": ["bernanke", "very sorry"],
            "n": 0,
            "rabbit": "Ben Bernanke"
        },
        {
            "id": "keynes",
            "tier": "power",
            "t": "Keynes’s _General Theory_ (1936) argued that governments should spend more to fight slumps",
            "k": ["keynes", "general theory", "spend"],
            "n": 0,
            "rabbit": "John Maynard Keynes"
        },
        {
            "id": "creditanstalt",
            "tier": "power",
            "t": "Austria’s Creditanstalt bank failed in 1931; Britain left the gold standard the same year",
            "k": ["creditanstalt", "gold standard", "austria"],
            "n": 0
        },
        {
            "id": "spare-a-dime",
            "tier": "power",
            "t": "“Brother, Can You Spare a Dime?” (1932), Yip Harburg’s song about a jobless veteran",
            "k": ["spare a dime", "harburg", "brother"],
            "n": 0
        },
        {
            "id": "dow",
            "tier": "power",
            "t": "Many had bought stocks “on margin”; the Dow lost almost 90 percent by 1932 and did not regain its 1929 peak until 1954",
            "k": ["margin", "dow", "1954", "90 percent"],
            "n": 0
        },
        {
            "id": "kids-books",
            "tier": "power",
            "t": "Set during it: _Bud, Not Buddy_ (Michigan), _Out of the Dust_ (Oklahoma, in free verse), and the musical _Annie_",
            "k": ["out of the dust", "bud not buddy", "annie", "free verse"],
            "n": 0
        },
        {
            "id": "agee-evans",
            "tier": "power",
            "t": "James Agee and Walker Evans’s _Let Us Now Praise Famous Men_ documented Alabama sharecroppers",
            "k": ["agee", "walker evans", "sharecroppers"],
            "n": 0
        },
        {
            "id": "penny-auctions",
            "tier": "power",
            "t": "Farmers held “penny auctions” to save neighbors’ farms; Milo Reno’s Farmers’ Holiday Association held back crops",
            "k": ["penny auctions", "milo reno", "farmers holiday"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Depression, Recession, or Deal?",
        "body": "Several answer lines sit right next to this one. The New Deal was Franklin Roosevelt’s set of programs to fight this crisis, the Dust Bowl was the drought and dust storms that hit the Great Plains at the same time, and the Great Recession was a different downturn that began in 2007. “Hoovervilles,” the shantytowns, can also be an answer of their own. Saying only “Depression” usually earns a prompt, so be ready to add “Great.”",
        "fix": "Listen for the noun. “This crisis” or “this period” wants the Great Depression; “this program” or “these agencies” wants the New Deal; “this environmental disaster” or “these dust storms” wants the Dust Bowl; “these shantytowns” wants Hoovervilles. Clues about 2008, home mortgages, or TARP point to the Great Recession.",
        "line": "Real answer line: <b><u>Great Depression</u></b> (prompt on <u>Depression</u>; do not accept “Great Recession”)"
    },
    "tests": {
        "right": [
            "Great Depression",
            "the Great Depression",
            "Grate Depression",
            "Depression of the 1930s",
            "great depresion"
        ],
        "prompt": [
            "Depression",
            "the Depression"
        ],
        "wrong": [
            "Great Recession",
            "New Deal",
            "Dust Bowl",
            "Stock Market Crash of 1929",
            "Hoovervilles",
            "Panic of 1893",
            "Black Tuesday"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
