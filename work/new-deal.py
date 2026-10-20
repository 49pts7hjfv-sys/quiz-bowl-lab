import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "new-deal",
    "name": "New Deal",
    "mono": "NDL",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "FDR’s answer to the Great Depression · Relief, recovery, and reform",
    "dates": "1933–1939",
    "briefing": "When Franklin Roosevelt became president in 1933, about one in four American workers had no job, and thousands of banks had failed. His New Deal answered with a flood of new laws and “alphabet agencies,” such as the CCC, the TVA, and the WPA, that put millions of people to work building roads, dams, schools, and parks. It also created Social Security, which pays pensions to retired workers, and it sparked heated debates, including fights with the Supreme Court.",
    "answerHtml": "<b><u>New Deal</u></b> (do not accept “Square Deal,” “Fair Deal,” or “Great Society”)",
    "accept": [
        "new deal",
        "the new deal",
        "first new deal",
        "second new deal"
    ],
    "prompt": [
        "deal",
        "alphabet agencies",
        "alphabet soup",
        "three rs",
        "relief recovery and reform",
        "relief recovery reform"
    ],
    "reject": [
        "square deal",
        "fair deal",
        "great society",
        "new frontier",
        "new freedom",
        "new nationalism",
        "great depression",
        "green new deal",
        "hundred days",
        "first hundred days",
        "marshall plan",
        "national industrial recovery act",
        "national recovery administration",
        "nira",
        "nra",
        "glass steagall act",
        "social security act",
        "social security",
        "works progress administration",
        "wpa",
        "civilian conservation corps",
        "ccc",
        "tennessee valley authority",
        "tva",
        "franklin roosevelt",
        "franklin delano roosevelt",
        "fdr",
        "court packing plan",
        "dust bowl",
        "reconstruction"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/New_Deal",
    "qb": {
        "q": "New Deal",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "In the “sick chicken” case, _Schechter_ [“SHEK-ter”] _Poultry Corp. v. United States_, the Supreme Court unanimously struck down this program’s National Industrial Recovery Act. Businesses that followed that law’s rules had displayed a blue eagle with the motto “We Do Our Part.”",
            "r": "For 10 points, name this group of programs that Franklin Roosevelt created to fight the Great Depression."
        },
        {
            "p": "After the Supreme Court struck down several laws from this program, its creator proposed adding up to six new justices in 1937. Justice Owen Roberts’s vote in a 1937 case upholding a minimum-wage law was nicknamed “the switch in time that saved nine.”",
            "r": "For 10 points, name this set of programs, including the WPA and Social Security, that Franklin Roosevelt used to fight the Great Depression."
        },
        {
            "p": "Ida May Fuller of Vermont received the first monthly check from a 1935 law that was part of this program. Frances Perkins, the first woman to serve in a presidential cabinet, led the committee that designed that law, the Social Security Act.",
            "r": "For 10 points, name this program of Franklin Roosevelt’s, which also created the CCC and the WPA."
        },
        {
            "p": "Hallie Flanagan led a theater project paid for by this program, and its Federal Writers’ Project hired authors such as Zora Neale Hurston and Richard Wright. Both projects belonged to the Works Progress Administration, which Harry Hopkins ran.",
            "r": "For 10 points, name this collection of Franklin Roosevelt’s programs that fought the Great Depression."
        },
        {
            "p": "Utility company president Wendell Willkie fought a public power agency created by this program, then ran for president against its creator in 1940. That agency, the Tennessee Valley Authority, built dams such as Norris Dam to control floods and make electricity.",
            "r": "For 10 points, name this group of 1930s programs that Franklin Roosevelt promised the American people."
        },
        {
            "p": "Francis Townsend proposed a pension for every American aged 60 or older, and Huey Long called for a “Share Our Wealth” plan, because both men thought this program did not go far enough. From the other side, the American Liberty League argued that this program gave the government too much power.",
            "r": "For 10 points, name this set of programs, including Social Security, that Franklin Roosevelt created during the Great Depression."
        },
        {
            "p": "Dorothea Lange took the photograph _Migrant Mother_ while working for the Resettlement Administration, one of many agencies created by this program. Another of its agencies, the Rural Electrification Administration, brought electric power lines to farms across the country.",
            "r": "For 10 points, name this set of 1930s programs that included the Social Security Act."
        },
        {
            "p": "Advisers such as Raymond Moley and Rexford Tugwell, a group nicknamed the “Brain Trust,” helped plan this program. Its name came from a promise made in 1932 by a candidate who flew to Chicago to accept the Democratic nomination in person.",
            "r": "That candidate was Franklin Roosevelt. Its goals were summed up as “relief, recovery, and reform.” For 10 points, name this program that fought the Great Depression."
        },
        {
            "p": "In _United States v. Butler_, the Supreme Court struck down a law from this program that paid farmers to grow fewer crops so that prices would rise. Under that law, the Agricultural Adjustment Act, some farmers were even paid to plow under cotton that they had already planted.",
            "r": "It also created the Civilian Conservation Corps. For 10 points, name this group of programs from Franklin Roosevelt’s presidency."
        },
        {
            "p": "Workers in one agency of this program earned 30 dollars a month and had to send most of that pay home to their families. Those young men planted billions of trees and built trails and cabins in parks for the Civilian Conservation Corps.",
            "r": "For 10 points, name this group of programs Franklin Roosevelt used to fight the Great Depression."
        },
        {
            "p": "The Fair Labor Standards Act, which set the first national minimum wage in 1938, was one of the last major laws of this program. Three years earlier, its Wagner Act had protected workers’ right to form unions and created the National Labor Relations Board.",
            "r": "For 10 points, name this set of programs that Franklin Roosevelt created during the Great Depression."
        },
        {
            "p": "Interior Secretary Harold Ickes [“ICK-eez”] ran this program’s Public Works Administration, which paid private companies to build bridges, dams, and schools. Harry Hopkins ran several of its relief agencies, including the Civil Works Administration, which hired millions of people during the winter of 1933 to 1934.",
            "r": "For 10 points, name this group of programs, including the WPA, that Franklin Roosevelt began in 1933."
        },
        {
            "p": "Before he was elected to Congress, a young Lyndon Johnson ran this program’s National Youth Administration in Texas, which gave part-time jobs to students and other young people. Laws for this program were passed in two big waves, in 1933 and 1935.",
            "r": "For 10 points, name this program whose “alphabet agencies” included the NYA, the CCC, and the TVA."
        },
        {
            "p": "Joseph Kennedy became the first chairman of the Securities and Exchange Commission, which this program created to police the stock market. The Glass-Steagall Act, another part of this program, created the FDIC to insure people’s bank deposits.",
            "r": "For 10 points, name this program that Franklin Roosevelt promised the American people in 1932."
        },
        {
            "p": "This program began with a national “bank holiday” and the Emergency Banking Act, which Congress passed in a single day in March 1933. Congress passed so many of this program’s laws over the next few months that the period became known as the Hundred Days.",
            "r": "For 10 points, name this group of programs Franklin Roosevelt created to fight the Great Depression."
        }
    ],
    "clues": [
        {
            "id": "fdr",
            "tier": "giveaway",
            "t": "Franklin D. Roosevelt’s programs to fight the Great Depression (1933–1939)",
            "k": ["great depression", "roosevelt", "fdr"],
            "n": 0,
            "rabbit": "Franklin Delano Roosevelt"
        },
        {
            "id": "three-rs",
            "tier": "giveaway",
            "t": "Its goals are summed up as the “three R’s”: relief, recovery, and reform",
            "k": ["three r’s", "relief", "recovery", "reform"],
            "n": 0
        },
        {
            "id": "alphabet",
            "tier": "giveaway",
            "t": "Created “alphabet agencies” known by their initials, like the CCC, the TVA, and the WPA",
            "k": ["alphabet agencies", "alphabet", "initials"],
            "n": 0
        },
        {
            "id": "social-security",
            "tier": "giveaway",
            "t": "Included the Social Security Act (1935), which created pensions for retired workers and unemployment insurance",
            "k": ["social security", "pensions", "unemployment insurance", "1935"],
            "n": 0
        },
        {
            "id": "promise-1932",
            "tier": "middle",
            "t": "FDR first promised it in 1932, when he flew to Chicago to accept the Democratic nomination in person",
            "k": ["1932", "chicago", "nomination"],
            "n": 0
        },
        {
            "id": "hundred-days",
            "tier": "middle",
            "t": "Began in the “Hundred Days” of 1933 with a “bank holiday” and the Emergency Banking Act",
            "k": ["hundred days", "bank holiday", "emergency banking act"],
            "n": 0
        },
        {
            "id": "ccc",
            "tier": "middle",
            "t": "Civilian Conservation Corps (CCC): young men planted billions of trees and built trails and cabins in parks",
            "k": ["civilian conservation corps", "trees", "parks"],
            "n": 0
        },
        {
            "id": "tva",
            "tier": "middle",
            "t": "Tennessee Valley Authority (TVA, 1933): built dams to control floods and bring electricity to the region",
            "k": ["tennessee valley authority", "dams", "electricity"],
            "n": 0
        },
        {
            "id": "wpa",
            "tier": "middle",
            "t": "Works Progress Administration (WPA, 1935), led by Harry Hopkins, hired millions of people to build roads, bridges, and schools",
            "k": ["works progress administration", "harry hopkins", "hopkins"],
            "n": 0
        },
        {
            "id": "perkins",
            "tier": "middle",
            "t": "Labor Secretary Frances Perkins, the first woman in a presidential cabinet, led the committee that designed Social Security",
            "k": ["frances perkins", "perkins", "first woman"],
            "n": 0
        },
        {
            "id": "court-packing",
            "tier": "middle",
            "t": "After the Supreme Court struck down some of its laws, FDR proposed adding up to six justices (the 1937 “court-packing” plan)",
            "k": ["court-packing", "six justices", "1937"],
            "n": 0
        },
        {
            "id": "wagner-act",
            "tier": "middle",
            "t": "The Wagner Act (1935) protected workers’ right to form unions and created the National Labor Relations Board",
            "k": ["wagner act", "wagner", "unions", "national labor relations board"],
            "n": 0,
            "rabbit": "Labor unions"
        },
        {
            "id": "fdic-sec",
            "tier": "middle",
            "t": "The FDIC (1933) insures bank deposits, and the SEC (1934) polices the stock market",
            "k": ["fdic", "deposits", "stock market"],
            "n": 0,
            "rabbit": "Glass-Steagall Act"
        },
        {
            "id": "schechter",
            "tier": "power",
            "t": "_Schechter Poultry Corp. v. United States_ (1935), the “sick chicken” case, struck down the National Industrial Recovery Act; the NRA’s symbol was a blue eagle",
            "k": ["schechter", "sick chicken", "blue eagle", "national industrial recovery act"],
            "n": 0,
            "rabbit": "National Industrial Recovery Act"
        },
        {
            "id": "butler",
            "tier": "power",
            "t": "_United States v. Butler_ (1936) struck down the Agricultural Adjustment Act, which paid farmers to grow less",
            "k": ["butler", "agricultural adjustment act", "grow less"],
            "n": 0
        },
        {
            "id": "switch-in-time",
            "tier": "power",
            "t": "Owen Roberts’s vote in _West Coast Hotel Co. v. Parrish_ (1937), upholding a minimum-wage law, was called “the switch in time that saved nine”",
            "k": ["switch in time", "owen roberts", "west coast hotel", "parrish"],
            "n": 0
        },
        {
            "id": "critics",
            "tier": "power",
            "t": "Huey Long (“Share Our Wealth”) and Francis Townsend said it did too little; the American Liberty League said it gave the government too much power",
            "k": ["huey long", "share our wealth", "townsend", "liberty league"],
            "n": 0
        },
        {
            "id": "fair-labor",
            "tier": "power",
            "t": "The Fair Labor Standards Act (1938), one of its last major laws, set the first national minimum wage and limited child labor",
            "k": ["fair labor standards act", "minimum wage", "child labor", "1938"],
            "n": 0
        },
        {
            "id": "ida-may-fuller",
            "tier": "power",
            "t": "Ida May Fuller of Vermont received the first monthly Social Security check (1940)",
            "k": ["ida may fuller", "fuller", "vermont"],
            "n": 0
        },
        {
            "id": "federal-one",
            "tier": "power",
            "t": "WPA arts projects hired writers like Zora Neale Hurston and Richard Wright; Hallie Flanagan led the Federal Theatre Project",
            "k": ["federal theatre project", "hallie flanagan", "hurston", "richard wright"],
            "n": 0
        },
        {
            "id": "migrant-mother",
            "tier": "power",
            "t": "Dorothea Lange took the photograph _Migrant Mother_ (1936) for its Resettlement Administration",
            "k": ["dorothea lange", "migrant mother", "resettlement"],
            "n": 0
        },
        {
            "id": "rea",
            "tier": "power",
            "t": "The Rural Electrification Administration (1935) brought electric power lines to farms",
            "k": ["rural electrification", "power lines", "farms"],
            "n": 0
        },
        {
            "id": "brain-trust",
            "tier": "power",
            "t": "Advisers called the “Brain Trust,” including Raymond Moley and Rexford Tugwell, helped plan it",
            "k": ["brain trust", "moley", "tugwell"],
            "n": 0
        },
        {
            "id": "nya",
            "tier": "power",
            "t": "A young Lyndon Johnson ran the National Youth Administration in Texas, which gave part-time jobs to students",
            "k": ["national youth administration", "lyndon johnson", "part-time jobs"],
            "n": 0,
            "rabbit": "Lyndon B. Johnson"
        },
        {
            "id": "willkie",
            "tier": "power",
            "t": "Utility executive Wendell Willkie fought the TVA, then ran against FDR as the Republican nominee in 1940",
            "k": ["wendell willkie", "willkie", "1940"],
            "n": 0
        },
        {
            "id": "ickes-hopkins",
            "tier": "power",
            "t": "Harold Ickes ran the Public Works Administration; Harry Hopkins’s Civil Works Administration hired millions in the winter of 1933–1934",
            "k": ["harold ickes", "ickes", "public works administration", "civil works administration"],
            "n": 0
        },
        {
            "id": "kennedy-sec",
            "tier": "power",
            "t": "Joseph Kennedy, father of a future president, was the first chairman of the Securities and Exchange Commission",
            "k": ["joseph kennedy", "kennedy", "securities and exchange commission"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Which deal is it?",
        "body": "Presidents love catchy names for their programs, and quiz bowl loves to mix them up: Theodore Roosevelt’s Square Deal, Franklin Roosevelt’s New Deal, Harry Truman’s Fair Deal, and Lyndon Johnson’s Great Society. Another trap is answering “Great Depression,” which was the crisis, not the programs created to fight it.",
        "fix": "Match the president and the decade. The 1930s, FDR, alphabet agencies, Social Security, and fights with the Supreme Court mean the New Deal. The “three Cs” of conservation, control of corporations, and consumer protection mean the Square Deal; Truman’s plan for national health insurance means the Fair Deal; Medicare and the War on Poverty mean the Great Society.",
        "line": "Real answer line: <b><u>New Deal</u></b> (do not accept “Square Deal,” “Fair Deal,” or “Great Society”)"
    },
    "tests": {
        "right": [
            "New Deal",
            "the New Deal",
            "new deel",
            "FDR's New Deal",
            "Second New Deal"
        ],
        "prompt": [
            "Alphabet agencies",
            "deal"
        ],
        "wrong": [
            "Square Deal",
            "Fair Deal",
            "Great Society",
            "Great Depression",
            "Green New Deal",
            "New Frontier",
            "Social Security Act"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
