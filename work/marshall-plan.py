import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TIP = "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."

data = {
    "id": "marshall-plan",
    "name": "Marshall Plan",
    "mono": "MP",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "U.S. aid that helped rebuild Western Europe after World War II · 1948–1952",
    "dates": "Proposed 1947; aid sent 1948–1952",
    "briefing": "In 1947, much of Europe still lay in ruins from World War II, and millions of people were hungry and cold. That June, in a speech at Harvard, Secretary of State George Marshall proposed that the United States help Europe rebuild, and from 1948 to 1952 America sent about $13 billion in food, fuel, machinery, and other aid to Western European countries. The Soviet Union refused to take part and kept the countries it controlled out too, deepening the Cold War split.",
    "answerHtml": "<b><u>Marshall Plan</u></b> (or <b><u>European Recovery Program</u></b> or <b><u>ERP</u></b>; prompt on <u>Marshall</u>; do not accept “Truman Doctrine”)",
    "accept": [
        "marshall plan",
        "the marshall plan",
        "european recovery program",
        "european recovery programme",
        "the european recovery program",
        "erp",
        "e r p",
        "marshall aid",
        "marshalls plan"
    ],
    "prompt": [
        "marshall",
        "george marshall",
        "george c marshall",
        "general marshall",
        "european recovery",
        "economic cooperation act",
        "economic cooperation act of 1948",
        "economic cooperation administration"
    ],
    "reject": [
        "truman doctrine",
        "berlin airlift",
        "berlin blockade",
        "nato",
        "north atlantic treaty organization",
        "north atlantic treaty",
        "molotov plan",
        "comecon",
        "dawes plan",
        "young plan",
        "morgenthau plan",
        "schuman plan",
        "lend lease",
        "lend lease act",
        "point four",
        "point four program",
        "containment",
        "john marshall",
        "thurgood marshall",
        "marshall islands",
        "marshall scholarship",
        "german marshall fund",
        "oeec",
        "oecd",
        "harry truman",
        "harry s truman",
        "new deal",
        "fair deal",
        "anaconda plan",
        "european union",
        "united nations"
    ],
    "tests": {
        "right": [
            "Marshall Plan",
            "the Marshall Plan",
            "European Recovery Program",
            "ERP",
            "Marshal Plan",
            "George Marshall Plan",
            "Marshall Aid"
        ],
        "prompt": [
            "Marshall",
            "George Marshall",
            "Economic Cooperation Act"
        ],
        "wrong": [
            "Truman Doctrine",
            "Berlin Airlift",
            "NATO",
            "Molotov Plan",
            "Thurgood Marshall",
            "Dawes Plan",
            "Containment",
            "Lend-Lease"
        ]
    },
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Marshall_Plan",
    "qb": {
        "q": "Marshall Plan",
        "found": 0,
        "tip": TIP
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "Under Secretary of State Will Clayton returned from Europe in 1947 and wrote memos warning of economic collapse there, and George Kennan’s Policy Planning Staff drafted ideas that shaped this program. Its supporters hoped a healthy Europe would be less likely to turn to communism.",
            "r": "For 10 points, name this American program to rebuild Western Europe after World War II, named for Truman’s Secretary of State."
        },
        {
            "p": "A month before this program was proposed, Dean Acheson previewed its ideas in a speech to the Delta Council in Cleveland, Mississippi. The European response to this program was organized by Britain’s foreign secretary, Ernest Bevin, and France’s foreign minister, Georges Bidault [“bee-DOH”].",
            "r": "For 10 points, name this program of U.S. aid to Western Europe that was first proposed in a June 1947 speech at Harvard."
        },
        {
            "p": "Vyacheslav Molotov walked out of a 1947 meeting in Paris about this program, and Czechoslovakia withdrew its acceptance of an invitation to join it after pressure from Joseph Stalin. The Soviet Union then set up its own rival programs for Eastern Europe.",
            "r": "For 10 points, name this U.S. program that sent about $13 billion to rebuild Western Europe after World War II."
        },
        {
            "p": "Republican senator Arthur Vandenberg of Michigan led the fight in Congress to approve this program, which passed quickly after communists seized power in Czechoslovakia in February 1948. President Harry Truman signed the law creating it that April.",
            "r": "For 10 points, name this aid program proposed by Secretary of State George Marshall to rebuild Europe."
        },
        {
            "p": "Former Studebaker car company president Paul Hoffman led the Economic Cooperation Administration, which ran this program, while W. Averell Harriman served as its special representative in Europe. Countries receiving this program’s aid set aside matching amounts of their own money in “counterpart funds.”",
            "r": "For 10 points, name this program that sent about $13 billion to Western Europe from 1948 to 1952."
        },
        {
            "p": "Sixteen European countries met in Paris in July 1947 to write a joint request for this program, and in 1948 they formed the Organisation for European Economic Co-operation to divide its aid. That organization later became the OECD.",
            "r": "For 10 points, name this American program to rebuild Europe after World War II, named for George Marshall."
        },
        {
            "p": "A speech proposing this program declared that American policy was directed “not against any country or doctrine but against hunger, poverty, desperation, and chaos.” That speech also said that “the initiative” must come from Europe.",
            "r": "That speech was given at Harvard in June 1947. For 10 points, name this program named for Truman’s Secretary of State."
        },
        {
            "p": "Harry Truman called this program and a doctrine he had announced three months before it “two halves of the same walnut.” That doctrine promised aid to Greece and Turkey, while this program offered economic help to all of Europe as part of Truman’s policy of containment.",
            "r": "For 10 points, name this program that sent billions of dollars to rebuild Western Europe after World War II."
        },
        {
            "p": "The man who proposed this program had been the U.S. Army’s chief of staff during World War II, and he later served as Secretary of Defense during the Korean War. In 1953, he won the Nobel Peace Prize.",
            "r": "For 10 points, name this program, named for that man, which sent aid to rebuild Western Europe."
        },
        {
            "p": "To thank the United States for this program, Britain created a scholarship for American students to study in the United Kingdom in 1953, and West German chancellor Willy Brandt announced the creation of a foundation in 1972, twenty-five years after it was proposed.",
            "r": "For 10 points, name this program proposed by Secretary of State George Marshall to rebuild Europe."
        },
        {
            "p": "Spain, under the dictator Francisco Franco, was left out of this program, while the United Kingdom, France, and West Germany received the largest shares of its aid. This program’s aid included food, fuel, and machinery.",
            "r": "For 10 points, name this American program that helped rebuild Western Europe from 1948 to 1952."
        },
        {
            "p": "The Soviet Union answered this program with the Molotov Plan, a set of trade deals with its Eastern European allies, and in 1949 it founded COMECON [“KOM-ih-kon”]. Countries such as Poland were pressured to turn down this program’s aid.",
            "r": "For 10 points, name this U.S. program that offered aid to rebuild Europe after a June 1947 speech at Harvard."
        },
        {
            "p": "The Economic Cooperation Act of 1948 created this program, and most of its money was given as grants that did not have to be repaid. European nations receiving its aid were expected to cooperate with one another and lower trade barriers.",
            "r": "For 10 points, name this American program, proposed by George Marshall, that sent billions of dollars to rebuild Western Europe."
        },
        {
            "p": "_Time_ magazine named the man who proposed this program its Man of the Year for 1947, the second time he had received that honor. That man had served as President Truman’s envoy to China before becoming Secretary of State in January 1947.",
            "r": "For 10 points, name this program of aid to rebuild Western Europe, named for that Secretary of State."
        },
        {
            "p": "The speech proposing this program never named the Soviet Union, but it warned that any government that tried to block the recovery of other countries could not expect American help. That speech was delivered at a university commencement in Cambridge, Massachusetts.",
            "r": "For 10 points, name this program proposed by George Marshall to rebuild Europe after World War II."
        }
    ],
    "clues": [
        {
            "id": "rebuild-europe",
            "tier": "giveaway",
            "t": "U.S. program that sent aid to help Western Europe rebuild after World War II (1948–1952)",
            "k": ["rebuild", "western europe", "world war ii"],
            "n": 0
        },
        {
            "id": "george-marshall",
            "tier": "giveaway",
            "t": "Named for Secretary of State George C. Marshall",
            "k": ["george c. marshall", "secretary of state"],
            "n": 0,
            "rabbit": "Secretary of State"
        },
        {
            "id": "harvard-speech",
            "tier": "giveaway",
            "t": "Proposed in a speech at Harvard University on June 5, 1947",
            "k": ["harvard", "june 5", "1947", "speech"],
            "n": 0
        },
        {
            "id": "truman",
            "tier": "giveaway",
            "t": "President Harry Truman signed the law creating it, the Economic Cooperation Act, in April 1948",
            "k": ["harry truman", "truman", "economic cooperation act", "april 1948"],
            "n": 0,
            "rabbit": "Harry S. Truman"
        },
        {
            "id": "thirteen-billion",
            "tier": "middle",
            "t": "Sent about $13 billion to Western European countries from 1948 to 1952, mostly as grants that did not have to be repaid",
            "k": ["$13 billion", "13 billion", "grants"],
            "n": 0
        },
        {
            "id": "soviet-refusal",
            "tier": "middle",
            "t": "The Soviet Union refused to take part and pressured the Eastern European countries it controlled, such as Poland, to refuse too",
            "k": ["soviet union", "refused", "eastern european", "poland"],
            "n": 0,
            "rabbit": "Soviet Union"
        },
        {
            "id": "molotov",
            "tier": "middle",
            "t": "Soviet foreign minister Vyacheslav Molotov walked out of the 1947 Paris talks about it",
            "k": ["vyacheslav molotov", "molotov", "walked out"],
            "n": 0
        },
        {
            "id": "czechoslovakia",
            "tier": "middle",
            "t": "Czechoslovakia accepted an invitation to join but withdrew under pressure from Joseph Stalin (1947)",
            "k": ["czechoslovakia", "joseph stalin", "stalin", "withdrew"],
            "n": 0,
            "rabbit": "Joseph Stalin"
        },
        {
            "id": "containment",
            "tier": "middle",
            "t": "Part of Truman’s Cold War policy of containment; Truman called it and the Truman Doctrine “two halves of the same walnut”",
            "k": ["containment", "truman doctrine", "walnut", "cold war"],
            "n": 0
        },
        {
            "id": "hunger-quote",
            "tier": "middle",
            "t": "Marshall: American policy was directed “not against any country or doctrine but against hunger, poverty, desperation, and chaos”",
            "k": ["hunger", "poverty", "desperation", "chaos"],
            "n": 0
        },
        {
            "id": "nobel",
            "tier": "middle",
            "t": "George Marshall won the 1953 Nobel Peace Prize, largely for this aid program",
            "k": ["nobel peace prize", "nobel", "1953"],
            "n": 0
        },
        {
            "id": "recipients",
            "tier": "middle",
            "t": "The biggest shares of aid went to the United Kingdom, France, and West Germany",
            "k": ["united kingdom", "france", "west germany"],
            "n": 0
        },
        {
            "id": "oeec",
            "tier": "middle",
            "t": "European countries formed the Organisation for European Economic Co-operation (OEEC, 1948) to divide the aid; it later became the OECD",
            "k": ["oeec", "oecd", "organisation for european economic co-operation"],
            "n": 0
        },
        {
            "id": "hoffman",
            "tier": "power",
            "t": "Run by the Economic Cooperation Administration under former Studebaker president Paul Hoffman; W. Averell Harriman was its special representative in Europe",
            "k": ["paul hoffman", "studebaker", "averell harriman", "harriman"],
            "n": 0
        },
        {
            "id": "vandenberg",
            "tier": "power",
            "t": "Republican senator Arthur Vandenberg of Michigan led the fight to pass it in Congress",
            "k": ["arthur vandenberg", "vandenberg", "michigan"],
            "n": 0
        },
        {
            "id": "clayton-kennan",
            "tier": "power",
            "t": "Shaped by Will Clayton’s 1947 memos on Europe’s economic crisis and by George Kennan’s Policy Planning Staff",
            "k": ["will clayton", "clayton", "george kennan", "policy planning staff"],
            "n": 0
        },
        {
            "id": "acheson",
            "tier": "power",
            "t": "Dean Acheson previewed the idea in a May 1947 speech to the Delta Council in Cleveland, Mississippi",
            "k": ["dean acheson", "acheson", "delta council", "cleveland, mississippi"],
            "n": 0
        },
        {
            "id": "bevin",
            "tier": "power",
            "t": "Britain’s Ernest Bevin and France’s Georges Bidault organized Europe’s response",
            "k": ["ernest bevin", "bevin", "georges bidault", "bidault"],
            "n": 0
        },
        {
            "id": "sixteen",
            "tier": "power",
            "t": "Sixteen European countries met in Paris in July 1947 to write a joint request for aid",
            "k": ["sixteen", "paris", "july 1947"],
            "n": 0
        },
        {
            "id": "speech-details",
            "tier": "power",
            "t": "The Harvard speech said “the initiative” must come from Europe and warned that governments blocking other countries’ recovery could not expect U.S. help; it never named the Soviet Union",
            "k": ["initiative", "blocking", "never named"],
            "n": 0
        },
        {
            "id": "counterpart",
            "tier": "power",
            "t": "Receiving countries set aside matching amounts of their own money in “counterpart funds”",
            "k": ["counterpart funds", "counterpart", "matching"],
            "n": 0
        },
        {
            "id": "czech-coup",
            "tier": "power",
            "t": "A communist takeover in Czechoslovakia (February 1948) pushed Congress to pass it quickly",
            "k": ["communist takeover", "february 1948", "takeover"],
            "n": 0
        },
        {
            "id": "molotov-plan",
            "tier": "power",
            "t": "The Soviet answers: the Molotov Plan (1947) trade deals and COMECON (1949)",
            "k": ["molotov plan", "comecon", "1949"],
            "n": 0
        },
        {
            "id": "spain",
            "tier": "power",
            "t": "Spain, ruled by the dictator Francisco Franco, was left out",
            "k": ["spain", "francisco franco", "franco"],
            "n": 0
        },
        {
            "id": "thanks",
            "tier": "power",
            "t": "Thank-yous: Britain’s Marshall Scholarships (1953) and a foundation announced by West German chancellor Willy Brandt (1972)",
            "k": ["scholarships", "willy brandt", "brandt"],
            "n": 0
        },
        {
            "id": "marshall-career",
            "tier": "power",
            "t": "George Marshall had been Army chief of staff in World War II and Truman’s envoy to China, and later became Secretary of Defense; _Time_ named him Man of the Year for 1947",
            "k": ["chief of staff", "china", "secretary of defense", "man of the year"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Plan, doctrine, or airlift?",
        "body": "Four early Cold War answers get mixed up. The Truman Doctrine (March 1947) promised aid to Greece and Turkey to resist communism; the Marshall Plan (proposed June 1947) sent economic aid to rebuild Western Europe; the Berlin Airlift (1948–1949) flew supplies into West Berlin during a Soviet blockade; and NATO (1949) is a military alliance. Also, George Marshall the man is a different answer from the plan named after him.",
        "fix": "A Harvard speech, about $13 billion, Paul Hoffman, the OEEC, and “European Recovery Program” mean the Marshall Plan. Greece and Turkey mean the Truman Doctrine; cargo planes and West Berlin mean the Berlin Airlift; a military alliance means NATO. If the question says “this program” or “this plan,” say “Marshall Plan,” not just “Marshall.”",
        "line": "Real answer line: <b><u>Marshall Plan</u></b> (or <b><u>European Recovery Program</u></b> or <b><u>ERP</u></b>; prompt on <u>Marshall</u>; do not accept “Truman Doctrine”)"
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
