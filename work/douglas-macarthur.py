import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Facts kept consistent with korean-war.json (Inchon Sept 15, 1950; fired April 1951; Martin letter;
# "Old soldiers never die"), harry-s-truman.json, great-depression.json (Bonus Army, Anacostia Flats)
# and battle-of-san-juan-hill.json (one of only two father-and-son Medal of Honor pairs).
# "Arthur" alone is NOT rejected: it sits inside the accepted spelling "mac arthur".

data = {
    "id": "douglas-macarthur",
    "name": "Douglas MacArthur",
    "mono": "DM",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "Five-star general in World War II and Korea · “I shall return”",
    "dates": "1880–1964",
    "briefing": "Douglas MacArthur graduated first in his West Point class, won medals for bravery in World War I, and became famous for his corncob pipe and dark sunglasses. Forced to leave the Philippines in 1942, he promised “I shall return,” and he did, in 1944. He accepted Japan’s surrender in 1945, ran the occupation of Japan, and led UN forces in the Korean War until President Harry Truman fired him in 1951.",
    "answerHtml": "Douglas <b><u>MacArthur</u></b> (prompt on <u>Douglas</u>; do not accept “Arthur MacArthur”)",
    "accept": [
        "douglas macarthur",
        "macarthur",
        "mac arthur",
        "douglas mac arthur",
        "general macarthur",
        "general douglas macarthur"
    ],
    "prompt": [
        "douglas"
    ],
    "reject": [
        "arthur macarthur",
        "arthur macarthur jr",
        "arthur mac arthur",
        "jean macarthur",
        "harry truman",
        "harry s truman",
        "truman",
        "matthew ridgway",
        "ridgway",
        "chester nimitz",
        "nimitz",
        "dwight d eisenhower",
        "dwight eisenhower",
        "eisenhower",
        "george patton",
        "patton",
        "omar bradley",
        "jonathan wainwright",
        "wainwright",
        "joseph stilwell",
        "william halsey",
        "halsey",
        "joseph mccarthy",
        "mccarthy",
        "chester a arthur",
        "chester arthur",
        "king arthur",
        "stephen a douglas",
        "stephen douglas",
        "frederick douglass",
        "frederick douglas",
        "douglass",
        "hirohito",
        "emperor hirohito",
        "hideki tojo",
        "tojo",
        "manuel quezon",
        "syngman rhee",
        "kim il sung",
        "chiang kai shek",
        "macarthur park",
        "macarthur foundation",
        "macarthur fellowship",
        "battle of inchon",
        "inchon",
        "inchon landing",
        "korean war",
        "bonus army",
        "bataan death march",
        "corregidor",
        "uss missouri"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Douglas_MacArthur",
    "qb": {
        "q": "MacArthur",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "In World War I, this officer suggested calling the 42nd Division the “Rainbow Division” because its men came from many different states, and he won several Silver Stars while leading its soldiers in France.",
            "r": "In World War II, after leaving the Philippines, he vowed, “I shall return.” For 10 points, name this American general."
        },
        {
            "p": "This man graduated first in his West Point class in 1903 and later served as the academy’s superintendent. In 1962, he gave a farewell speech to the cadets there built around the words “Duty, Honor, Country.”",
            "r": "For 10 points, name this general whom Harry Truman removed from command during the Korean War."
        },
        {
            "p": "As Army Chief of Staff in 1932, this general, with his aide Dwight Eisenhower beside him, led troops who drove thousands of World War I veterans out of their camp at Anacostia [“an-uh-KOSS-tee-uh”] Flats in Washington, D.C.",
            "r": "Those veterans were the Bonus Army. For 10 points, name this general who later led United Nations forces in Korea."
        },
        {
            "p": "In 1936, Manuel Quezon [“KAY-zon”], president of the Philippine Commonwealth, made this American a field marshal of the Philippine Army. After Japan invaded the islands, this man left the fortress of Corregidor [“kuh-REG-ih-dor”] by PT boat in March 1942.",
            "r": "On reaching Australia, he promised, “I shall return.” For 10 points, name this general, who kept that promise in 1944."
        },
        {
            "p": "The freed prisoners of war Jonathan Wainwright and Arthur Percival stood behind this man at a 1945 ceremony where he signed as Supreme Commander for the Allied Powers, while Chester Nimitz signed separately for the United States.",
            "r": "For 10 points, name this general who accepted Japan’s surrender aboard the USS _Missouri_ on September 2, 1945."
        },
        {
            "p": "A famous 1945 photograph shows this tall American in an open-collared uniform standing beside Emperor Hirohito [“hee-roh-HEE-toh”]. This man’s staff wrote the draft of Japan’s 1947 constitution, whose Article 9 renounces war, and under his authority Japanese women gained the right to vote.",
            "r": "For 10 points, name this general who ran the occupation of Japan after World War II."
        },
        {
            "p": "At a meeting on Wake Island in October 1950, this general told President Harry Truman that China was unlikely to enter the war he was commanding. Within weeks, huge Chinese armies attacked his forces and drove them back.",
            "r": "In April 1951, Truman fired him. For 10 points, name this commander of United Nations forces in the Korean War."
        },
        {
            "p": "Answering a congressman’s question about using Chiang Kai-shek’s troops from Taiwan, this general wrote a letter, read aloud on the House floor by Republican leader Joseph Martin, that declared, “There is no substitute for victory.”",
            "r": "Days later, Harry Truman fired him. For 10 points, name this general who told Congress that “old soldiers never die.”"
        },
        {
            "p": "This general’s Operation Chromite surprised North Korea in September 1950 by landing troops at a port with some of the most extreme tides in the world, far behind enemy lines and close to Seoul.",
            "r": "That landing was at Inchon. For 10 points, name this commander of United Nations forces in the Korean War."
        },
        {
            "p": "In December 1944, this general was promoted to the new five-star rank of General of the Army. Two months earlier, he had waded ashore on the island of Leyte [“LAY-tee”], days before the naval Battle of Leyte Gulf.",
            "r": "There, he announced, “People of the Philippines, I have returned,” keeping a promise he had made in 1942. For 10 points, name this general."
        },
        {
            "p": "This man and his father, Arthur, are one of only two father-and-son pairs to both receive the Medal of Honor. His father had earned it as a teenager by carrying a Wisconsin regiment’s flag up Missionary Ridge in the Civil War.",
            "r": "For 10 points, name this American general who accepted Japan’s surrender in 1945 aboard the USS _Missouri_."
        },
        {
            "p": "Gregory Peck played this man in a 1977 film named after him, and Laurence Olivier played him in the 1981 war movie _Inchon_. Years earlier, his mother had moved into a hotel at West Point to watch over him while he was a cadet.",
            "r": "He was known for his corncob pipe and aviator sunglasses. For 10 points, name this general whom Harry Truman fired in 1951."
        },
        {
            "p": "This general was born in 1880 at an Army arsenal in Little Rock, Arkansas, the son of a Civil War hero, and he served as the Army’s Chief of Staff from 1930 to 1935.",
            "r": "In 1942, he promised the people of the Philippines, “I shall return.” For 10 points, name this general."
        },
        {
            "p": "In 1943 and 1944, commanding Allied forces in the Southwest Pacific, this general used a “leapfrogging” strategy along the coast of New Guinea, bypassing strong Japanese bases such as Rabaul [“rah-BOWL”] and leaving them cut off.",
            "r": "For 10 points, name this general who returned to the Philippines in October 1944, as he had promised."
        },
        {
            "p": "Hours after the attack on Pearl Harbor, Japanese planes caught many of this general’s bombers on the ground at Clark Field, and his American and Filipino troops were soon forced back onto the Bataan Peninsula.",
            "r": "He later accepted Japan’s surrender as Supreme Commander for the Allied Powers. For 10 points, name this general who vowed, “I shall return.”"
        }
    ],
    "clues": [
        {
            "id": "i-shall-return",
            "tier": "giveaway",
            "t": "Promised “I shall return” after leaving the Philippines (1942); kept the promise at Leyte (1944)",
            "k": ["i shall return", "philippines", "leyte"],
            "n": 0
        },
        {
            "id": "fired-by-truman",
            "tier": "giveaway",
            "t": "Led UN forces in the Korean War until Harry Truman fired him in April 1951",
            "k": ["truman", "korean war", "fired", "1951"],
            "n": 0,
            "rabbit": "Korean War"
        },
        {
            "id": "missouri",
            "tier": "giveaway",
            "t": "Accepted Japan’s surrender aboard the USS _Missouri_ in Tokyo Bay (September 2, 1945)",
            "k": ["missouri", "surrender", "tokyo bay"],
            "n": 0
        },
        {
            "id": "old-soldiers",
            "tier": "giveaway",
            "t": "Farewell speech to Congress (1951): “Old soldiers never die; they just fade away”",
            "k": ["old soldiers", "fade away", "never die"],
            "n": 0
        },
        {
            "id": "inchon",
            "tier": "middle",
            "t": "Planned the surprise landing at Inchon (September 15, 1950), which led to the recapture of Seoul",
            "k": ["inchon", "seoul", "landing"],
            "n": 0
        },
        {
            "id": "occupation",
            "tier": "middle",
            "t": "Ran the occupation of Japan (1945–1951) as Supreme Commander for the Allied Powers",
            "k": ["occupation", "supreme commander", "allied powers"],
            "n": 0
        },
        {
            "id": "bonus-army",
            "tier": "middle",
            "t": "As Army Chief of Staff, with his aide Dwight Eisenhower, led troops that drove the Bonus Army from Anacostia Flats (1932)",
            "k": ["bonus army", "anacostia", "1932", "eisenhower"],
            "n": 0,
            "rabbit": "Great Depression"
        },
        {
            "id": "corregidor",
            "tier": "middle",
            "t": "Left Corregidor by PT boat in March 1942, on Franklin Roosevelt’s orders, and went on to Australia",
            "k": ["corregidor", "pt boat", "australia"],
            "n": 0
        },
        {
            "id": "no-substitute",
            "tier": "middle",
            "t": "His letter backing the use of Chiang Kai-shek’s troops, read aloud by Joseph Martin, said “There is no substitute for victory”",
            "k": ["no substitute for victory", "joseph martin", "chiang"],
            "n": 0
        },
        {
            "id": "five-star",
            "tier": "middle",
            "t": "Promoted to the new five-star rank of General of the Army (December 1944)",
            "k": ["five-star", "general of the army"],
            "n": 0
        },
        {
            "id": "pipe",
            "tier": "middle",
            "t": "Famous for his corncob pipe and aviator sunglasses",
            "k": ["corncob pipe", "corncob", "sunglasses"],
            "n": 0
        },
        {
            "id": "medal-of-honor",
            "tier": "middle",
            "t": "He and his father, Arthur, are one of only two father-and-son pairs awarded the Medal of Honor",
            "k": ["medal of honor", "father-and-son", "arthur"],
            "n": 0
        },
        {
            "id": "rainbow",
            "tier": "power",
            "t": "Named the 42nd “Rainbow” Division in World War I and won several Silver Stars in France",
            "k": ["rainbow", "42nd", "silver stars"],
            "n": 0
        },
        {
            "id": "west-point",
            "tier": "power",
            "t": "Graduated first in his West Point class (1903); later its superintendent (1919–1922)",
            "k": ["west point", "superintendent", "1903"],
            "n": 0
        },
        {
            "id": "duty-honor-country",
            "tier": "power",
            "t": "Gave his “Duty, Honor, Country” farewell speech to West Point cadets (1962)",
            "k": ["duty, honor, country", "cadets", "1962"],
            "n": 0
        },
        {
            "id": "little-rock",
            "tier": "power",
            "t": "Born at an Army arsenal in Little Rock, Arkansas (1880); Army Chief of Staff (1930–1935)",
            "k": ["little rock", "arkansas", "chief of staff"],
            "n": 0
        },
        {
            "id": "quezon",
            "tier": "power",
            "t": "Made a field marshal of the Philippine Army (1936) by Commonwealth president Manuel Quezon",
            "k": ["field marshal", "quezon"],
            "n": 0
        },
        {
            "id": "wainwright-percival",
            "tier": "power",
            "t": "Jonathan Wainwright and Britain’s Arthur Percival stood behind him at the surrender; Chester Nimitz signed for the U.S.",
            "k": ["wainwright", "percival", "nimitz"],
            "n": 0
        },
        {
            "id": "hirohito",
            "tier": "power",
            "t": "A famous 1945 photograph shows him standing beside Emperor Hirohito",
            "k": ["hirohito", "photograph", "emperor"],
            "n": 0
        },
        {
            "id": "article-9",
            "tier": "power",
            "t": "His staff drafted Japan’s 1947 constitution, whose Article 9 renounces war; Japanese women gained the vote",
            "k": ["article 9", "constitution", "1947"],
            "n": 0
        },
        {
            "id": "wake-island",
            "tier": "power",
            "t": "Told Truman at Wake Island (October 1950) that China was unlikely to enter the Korean War",
            "k": ["wake island", "china"],
            "n": 0
        },
        {
            "id": "chromite",
            "tier": "power",
            "t": "Operation Chromite: landed at a port with some of the world’s most extreme tides",
            "k": ["chromite", "tides"],
            "n": 0
        },
        {
            "id": "leapfrogging",
            "tier": "power",
            "t": "Used “leapfrogging” along New Guinea, bypassing Japanese bases such as Rabaul",
            "k": ["leapfrogging", "new guinea", "rabaul"],
            "n": 0
        },
        {
            "id": "clark-field",
            "tier": "power",
            "t": "Hours after Pearl Harbor, Japanese planes caught many of his bombers at Clark Field; his troops fell back to Bataan",
            "k": ["clark field", "bataan"],
            "n": 0
        },
        {
            "id": "films",
            "tier": "power",
            "t": "Played by Gregory Peck (1977) and Laurence Olivier (_Inchon_, 1981); his mother lived at West Point while he was a cadet",
            "k": ["gregory peck", "laurence olivier", "mother"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Which general, which war?",
        "body": "Several World War II commanders share clues. Dwight Eisenhower led the Allies in Europe (North Africa and D-Day), this man commanded in the Southwest Pacific and the Philippines, and Admiral Chester Nimitz led the Navy across the central Pacific. His father, Arthur MacArthur, was also a general who served in the Philippines and won the Medal of Honor, so answer lines say “do not accept Arthur MacArthur.” Don’t mix up the name with Senator Joseph McCarthy, the 1950s anti-communist.",
        "fix": "The Philippines, “I shall return,” the USS _Missouri_, the occupation of Japan, Inchon, and being fired by Truman all mean Douglas MacArthur. D-Day and NATO mean Eisenhower; Midway and the Pacific Fleet mean Nimitz. In Korea, Matthew Ridgway replaced him in 1951.",
        "line": "Real answer line: Douglas <b><u>MacArthur</u></b> (do not accept “Arthur MacArthur”)"
    },
    "tests": {
        "right": [
            "Douglas MacArthur",
            "MacArthur",
            "General MacArthur",
            "Douglas McArthur",
            "General Douglas MacArthur",
            "Mac Arthur"
        ],
        "prompt": [
            "Douglas"
        ],
        "wrong": [
            "Arthur MacArthur",
            "Harry Truman",
            "Chester Nimitz",
            "Dwight Eisenhower",
            "Matthew Ridgway",
            "Joseph McCarthy",
            "Chester A. Arthur",
            "Stephen Douglas"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
