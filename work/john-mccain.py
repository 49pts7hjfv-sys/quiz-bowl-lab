import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TIP = "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."

data = {
    "id": "john-mccain",
    "name": "John McCain",
    "mono": "JMC",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "Vietnam POW and Arizona senator · 2008 Republican nominee",
    "dates": "1936–2018",
    "briefing": "Navy pilot John McCain was shot down over North Vietnam in 1967 and spent more than five years as a prisoner of war, turning down an early release because other Americans had been held longer. Back home, he represented Arizona in the U.S. Senate from 1987 to 2018 and was nicknamed “the Maverick” for sometimes breaking with his own party. In 2008, he was the Republican nominee for president but lost to Barack Obama.",
    "answerHtml": "John <b><u>McCain</u></b> (or John Sidney <u>McCain</u> III; do not accept “Cindy McCain”)",
    "accept": [
        "john mccain",
        "mccain",
        "john sidney mccain",
        "john sidney mccain iii",
        "john s mccain iii",
        "john mccain iii",
        "senator mccain",
        "senator john mccain"
    ],
    "prompt": [
        "maverick",
        "the maverick"
    ],
    "reject": [
        "cindy mccain",
        "meghan mccain",
        "john s mccain jr",
        "john s mccain sr",
        "john mccain jr",
        "john mccain sr",
        "mccain feingold",
        "mccain feingold act",
        "mitt romney",
        "romney",
        "john kerry",
        "kerry",
        "barry goldwater",
        "goldwater",
        "sarah palin",
        "palin",
        "barack obama",
        "obama",
        "george w bush",
        "russ feingold",
        "feingold",
        "bob dole",
        "mike huckabee",
        "lindsey graham",
        "joe lieberman",
        "jeff flake",
        "john glenn"
    ],
    "tests": {
        "right": [
            "John McCain",
            "McCain",
            "Senator John McCain",
            "John Sidney McCain III",
            "Jon McCain",
            "John McCane"
        ],
        "prompt": [
            "the Maverick"
        ],
        "wrong": [
            "Mitt Romney",
            "John Kerry",
            "Barry Goldwater",
            "Sarah Palin",
            "Cindy McCain",
            "McCain-Feingold Act",
            "Barack Obama"
        ]
    },
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/John_McCain",
    "qb": {
        "q": "McCain",
        "found": 0,
        "tip": TIP
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "In July 1967, this pilot escaped from his burning jet during a fire aboard the aircraft carrier USS _Forrestal_ that killed 134 sailors. Three months later, he was shot down over Hanoi on his 23rd bombing mission and was captured.",
            "r": "He spent more than five years as a prisoner of war. For 10 points, name this Arizona senator who was the 2008 Republican presidential nominee."
        },
        {
            "p": "A stone monument beside Truc Bach [“trook BAHK”] Lake in Hanoi marks the spot where this American pilot landed after his A-4 Skyhawk was shot down in October 1967. His captors later offered to free him early because his father was a top admiral, but he refused.",
            "r": "For 10 points, name this Navy pilot who spent more than five years as a prisoner of war before becoming a senator from Arizona."
        },
        {
            "p": "This man was born in 1936 at a naval air station in the Panama Canal Zone, so in 2008 the Senate passed a resolution stating that he was a “natural-born citizen” eligible to be president. He had graduated near the bottom of his class at the U.S. Naval Academy in 1958.",
            "r": "For 10 points, name this Arizona senator who lost the 2008 presidential election to Barack Obama."
        },
        {
            "p": "The Senate Ethics Committee said this man showed “poor judgment” as one of the “Keating Five,” a group of senators who met with federal regulators on behalf of a savings-and-loan owner. This man had won Barry Goldwater’s Senate seat in 1986.",
            "r": "For 10 points, name this Arizona Republican, a former prisoner of war, who was his party’s presidential nominee in 2008."
        },
        {
            "p": "This senator and Wisconsin Democrat Russ Feingold wrote the Bipartisan Campaign Reform Act of 2002, which banned unlimited “soft money” donations to national political parties. Parts of that law were later struck down in the Supreme Court case _Citizens United v. FEC_.",
            "r": "That law is usually called by both senators’ last names. For 10 points, name this Arizona senator nicknamed “the Maverick.”"
        },
        {
            "p": "In 2000, this man rode a campaign bus called the “Straight Talk Express” across New Hampshire, where he beat George W. Bush in the Republican primary by a wide margin. He lost the nomination after losing the South Carolina primary weeks later.",
            "r": "Eight years later, he won that nomination and chose Sarah Palin as his running mate. For 10 points, name this Arizona senator."
        },
        {
            "p": "Days after announcing that he had brain cancer, this senator returned to Washington and in July 2017 cast one of three Republican votes that defeated a bill to partly repeal the Affordable Care Act. He signaled that vote with a thumbs-down gesture on the Senate floor.",
            "r": "For 10 points, name this Arizona senator, a former prisoner of war in Vietnam, who died in 2018."
        },
        {
            "p": "In 2005, this senator wrote an amendment banning “cruel, inhuman, or degrading” treatment of prisoners in American custody. Decades earlier, he had spent years in Hoa Lo [“hwah LOH”] Prison, which its American captives nicknamed the “Hanoi Hilton.”",
            "r": "For 10 points, name this Navy pilot who was a prisoner of war in Vietnam before representing Arizona in the Senate."
        },
        {
            "p": "In the 1990s, this senator joined fellow Vietnam veteran John Kerry in urging President Bill Clinton to restore diplomatic relations with Vietnam, which Clinton did in 1995. Earlier, both men served on a Senate committee that investigated whether any American prisoners were still being held in Southeast Asia.",
            "r": "This man had been a prisoner of war in Hanoi himself. For 10 points, name this Arizona senator."
        },
        {
            "p": "This senator chaired the Senate Armed Services Committee from 2015 until his death, and the defense bill that Congress passed in 2018 was named in his honor. His father, an admiral with the same name, commanded American forces in the Pacific during the Vietnam War.",
            "r": "For 10 points, name this Arizona senator who lost the 2008 presidential election to Barack Obama."
        },
        {
            "p": "This man wrote about his grandfather, his father, and his own years in captivity in the 1999 memoir _Faith of My Fathers_, written with his longtime aide Mark Salter. His final book, _The Restless Wave_, came out in 2018.",
            "r": "For 10 points, name this senator from Arizona who was a prisoner of war in North Vietnam for more than five years."
        },
        {
            "p": "This man was buried at the U.S. Naval Academy Cemetery in Annapolis, Maryland, after a funeral at Washington National Cathedral where two men who had beaten him in presidential campaigns both gave eulogies.",
            "r": "Those men were George W. Bush and Barack Obama. For 10 points, name this Arizona senator who died in 2018."
        },
        {
            "p": "This candidate’s 2008 campaign used the slogan “Country First,” and he defeated Mitt Romney and Mike Huckabee in the Republican primaries. That August, he chose a first-term governor as his running mate.",
            "r": "That governor was Alaska’s Sarah Palin. For 10 points, name this Republican who lost the 2008 presidential election to Barack Obama."
        },
        {
            "p": "In 2018, a Navy destroyer that had been named for this man’s father and grandfather, both four-star admirals, was rededicated to honor him as well. He had retired from the Navy as a captain in 1981 and moved to Arizona.",
            "r": "For 10 points, name this former prisoner of war who represented Arizona in the Senate and ran for president in 2008."
        },
        {
            "p": "After retiring from the Navy, this man won two terms in the U.S. House from Arizona. In 1986, he was elected to replace the retiring Barry Goldwater in the Senate, where he served until his death more than thirty years later.",
            "r": "For 10 points, name this Republican senator nicknamed “the Maverick,” his party’s nominee for president in 2008."
        }
    ],
    "clues": [
        {
            "id": "pow",
            "tier": "giveaway",
            "t": "Navy pilot shot down over North Vietnam in 1967; a prisoner of war for more than five years",
            "k": ["prisoner of war", "north vietnam", "navy pilot", "1967"],
            "n": 0,
            "rabbit": "Vietnam War"
        },
        {
            "id": "nominee-2008",
            "tier": "giveaway",
            "t": "Republican presidential nominee in 2008; lost to Barack Obama",
            "k": ["2008", "republican", "nominee", "barack obama"],
            "n": 0,
            "rabbit": "Barack Obama"
        },
        {
            "id": "arizona",
            "tier": "giveaway",
            "t": "U.S. senator from Arizona from 1987 until his death in 2018",
            "k": ["arizona", "senator", "1987"],
            "n": 0
        },
        {
            "id": "palin",
            "tier": "giveaway",
            "t": "His 2008 running mate was Alaska governor Sarah Palin, the first woman on a Republican presidential ticket",
            "k": ["sarah palin", "palin", "running mate", "alaska"],
            "n": 0
        },
        {
            "id": "maverick",
            "tier": "giveaway",
            "t": "Nicknamed “the Maverick” for sometimes breaking with his own party",
            "k": ["maverick"],
            "n": 0
        },
        {
            "id": "hanoi-hilton",
            "tier": "middle",
            "t": "Held partly in Hanoi’s Hoa Lo Prison, the “Hanoi Hilton”; came home in 1973",
            "k": ["hanoi hilton", "hoa lo", "1973"],
            "n": 0
        },
        {
            "id": "campaign-finance",
            "tier": "middle",
            "t": "Co-wrote a 2002 campaign-finance law with Democrat Russ Feingold that banned “soft money” gifts to national parties",
            "k": ["feingold", "campaign-finance", "soft money"],
            "n": 0
        },
        {
            "id": "aca-vote",
            "tier": "middle",
            "t": "In July 2017, cast one of three Republican votes that defeated a bill to partly repeal the Affordable Care Act, with a thumbs-down",
            "k": ["affordable care act", "thumbs-down", "2017", "repeal"],
            "n": 0,
            "rabbit": "Affordable Care Act"
        },
        {
            "id": "straight-talk",
            "tier": "middle",
            "t": "Ran for the 2000 Republican nomination on the “Straight Talk Express”; won New Hampshire but lost to George W. Bush",
            "k": ["straight talk express", "new hampshire", "george w. bush", "2000"],
            "n": 0
        },
        {
            "id": "admirals",
            "tier": "middle",
            "t": "Son and grandson of four-star Navy admirals with the same name",
            "k": ["admirals", "four-star", "grandson"],
            "n": 0
        },
        {
            "id": "goldwater",
            "tier": "middle",
            "t": "Won Barry Goldwater’s Senate seat in 1986, after two terms in the U.S. House",
            "k": ["goldwater", "1986"],
            "n": 0
        },
        {
            "id": "died-2018",
            "tier": "middle",
            "t": "Died of brain cancer in August 2018; his old rivals George W. Bush and Barack Obama gave eulogies at his funeral",
            "k": ["brain cancer", "eulogies", "2018"],
            "n": 0
        },
        {
            "id": "faith-of-my-fathers",
            "tier": "middle",
            "t": "Memoir _Faith of My Fathers_ (1999), about his family and his years as a captive",
            "k": ["faith of my fathers"],
            "n": 0
        },
        {
            "id": "forrestal",
            "tier": "power",
            "t": "Escaped his burning jet in the 1967 fire aboard the aircraft carrier USS _Forrestal_, which killed 134 sailors",
            "k": ["forrestal", "fire", "134"],
            "n": 0
        },
        {
            "id": "truc-bach",
            "tier": "power",
            "t": "Shot down over Hanoi in October 1967 on his 23rd mission; landed in Truc Bach Lake, where a monument marks the spot",
            "k": ["truc bach", "23rd mission", "skyhawk"],
            "n": 0
        },
        {
            "id": "early-release",
            "tier": "power",
            "t": "Refused an early release offered because his father was a top admiral; prisoners were supposed to go home in the order they were captured",
            "k": ["early release", "order they were captured"],
            "n": 0
        },
        {
            "id": "canal-zone",
            "tier": "power",
            "t": "Born in 1936 at a naval air station in the Panama Canal Zone; a 2008 Senate resolution called him a “natural-born citizen”",
            "k": ["canal zone", "panama", "natural-born"],
            "n": 0
        },
        {
            "id": "naval-academy",
            "tier": "power",
            "t": "Graduated near the bottom of his U.S. Naval Academy class (1958); retired from the Navy as a captain in 1981",
            "k": ["naval academy", "1958", "bottom"],
            "n": 0
        },
        {
            "id": "keating-five",
            "tier": "power",
            "t": "One of the “Keating Five” senators; the Ethics Committee said he showed “poor judgment” in helping a savings-and-loan owner",
            "k": ["keating five", "keating", "poor judgment", "savings-and-loan"],
            "n": 0
        },
        {
            "id": "detainee-amendment",
            "tier": "power",
            "t": "His 2005 amendment banned “cruel, inhuman, or degrading” treatment of prisoners in American custody",
            "k": ["cruel", "degrading", "2005"],
            "n": 0
        },
        {
            "id": "vietnam-relations",
            "tier": "power",
            "t": "Worked with fellow Vietnam veteran John Kerry to restore U.S. relations with Vietnam (1995)",
            "k": ["john kerry", "kerry", "relations"],
            "n": 0
        },
        {
            "id": "armed-services",
            "tier": "power",
            "t": "Chaired the Senate Armed Services Committee (2015–2018); the defense bill passed in 2018 was named for him",
            "k": ["armed services", "defense bill"],
            "n": 0
        },
        {
            "id": "pacific-father",
            "tier": "power",
            "t": "His father commanded U.S. forces in the Pacific during the Vietnam War; a destroyer named for his father and grandfather was rededicated to him too (2018)",
            "k": ["pacific", "destroyer", "rededicated"],
            "n": 0
        },
        {
            "id": "country-first",
            "tier": "power",
            "t": "2008 slogan: “Country First”; beat Mitt Romney and Mike Huckabee in the Republican primaries",
            "k": ["country first", "romney", "huckabee"],
            "n": 0
        },
        {
            "id": "restless-wave",
            "tier": "power",
            "t": "Wrote his books with aide Mark Salter; his last was _The Restless Wave_ (2018)",
            "k": ["restless wave", "mark salter"],
            "n": 0
        },
        {
            "id": "annapolis",
            "tier": "power",
            "t": "Funeral at Washington National Cathedral; buried at the U.S. Naval Academy Cemetery in Annapolis, Maryland",
            "k": ["annapolis", "national cathedral", "cemetery"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Which Republican nominee?",
        "body": "Several politicians get mixed up with this man. Barry Goldwater, whose Senate seat he took in 1986, was also a senator from Arizona and the Republican nominee in 1964. Mitt Romney was the Republican nominee in 2012, the next nominee to lose to Barack Obama, and John Kerry, another Vietnam veteran senator, was the Democratic nominee in 2004. Clues about the 2008 race can also be asking for Sarah Palin or Obama.",
        "fix": "The “Hanoi Hilton,” the _Forrestal_ fire, Russ Feingold, the “Straight Talk Express,” and the 2008 ticket with Palin mean this man. Goldwater means 1964; Romney means 2012, Massachusetts, and Utah; Kerry means the 2004 Democratic ticket.",
        "line": "Real answer line: John <b><u>McCain</u></b> (or John Sidney <u>McCain</u> III)"
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
