import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def T(p, r):
    return {"p": p, "r": r}


def C(cid, tier, t, k, rabbit=None):
    c = {"id": cid, "tier": tier, "t": t, "k": k, "n": 0}
    if rabbit:
        c["rabbit"] = rabbit
    return c


data = {
    "id": "harry-s-truman",
    "name": "Harry S. Truman",
    "mono": "HST",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "33rd U.S. President · Led the nation from World War II into the Cold War",
    "dates": "1884–1972",
    "briefing": "Harry Truman was a Missouri farmer, a World War I artillery captain, and the co-owner of a men’s clothing store that failed in 1922. He had been vice president for only 82 days when Franklin Roosevelt died in April 1945, making him president in the last months of World War II. He decided to use atomic bombs against Japan, led the country into the Cold War, and kept a sign on his desk that read “The buck stops here.”",
    "answerHtml": "Harry S. <b><u>Truman</u></b>",
    "accept": [
        "harry s truman",
        "harry truman",
        "truman",
        "president truman",
        "president harry truman"
    ],
    "prompt": [
        "harry",
        "harry s"
    ],
    "reject": [
        "truman capote",
        "capote",
        "truman doctrine",
        "the truman show",
        "truman show",
        "bess truman",
        "margaret truman",
        "harry reid",
        "harry hopkins",
        "dwight eisenhower",
        "dwight d eisenhower",
        "eisenhower",
        "franklin roosevelt",
        "franklin d roosevelt",
        "franklin delano roosevelt",
        "fdr",
        "thomas dewey",
        "dewey",
        "george marshall",
        "marshall plan",
        "douglas macarthur",
        "macarthur",
        "henry wallace",
        "alben barkley",
        "dean acheson",
        "strom thurmond",
        "lyndon johnson",
        "lucius clay"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Harry_S._Truman",
    "qb": {
        "q": "Truman",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {"n": 0, "note": "no real tossups checked yet"},
    "tossups": [
        T("Kansas City political boss Tom Pendergast helped launch this man’s career, and he won a U.S. Senate seat from Missouri in 1934. During World War II, this senator led a committee that saved billions of dollars by investigating waste in defense spending.",
          "For 10 points, name this man who became president when Franklin Roosevelt died in April 1945."),
        T("This man’s running mate in 1948 was Kentucky senator Alben Barkley, who became known as “the Veep.” That year, this man crossed the country on a “whistle-stop” train tour, giving short speeches from the back of his train.",
          "He later held up a newspaper wrongly saying Thomas Dewey had beaten him. For 10 points, name this president who won the 1948 election in an upset."),
        T("This president’s Executive Order 9981 ordered an end to segregation in the U.S. armed forces in 1948. That year, some Southern delegates walked out of his party’s convention, and the breakaway States’ Rights Democrats, or Dixiecrats, nominated Strom Thurmond.",
          "For 10 points, name this Democrat who won the 1948 election anyway, beating Thomas Dewey."),
        T("This president agreed with a reporter who called the fighting that began in June 1950 a “police action” under the United Nations. In 1951, he fired General Douglas MacArthur for publicly calling for a wider war against China.",
          "MacArthur had led UN forces in the Korean War. For 10 points, name this president who succeeded Franklin Roosevelt."),
        T("Partway through one 1945 conference, British election results replaced Winston Churchill with Clement Attlee, who then sat across the table from this president. At that Potsdam Conference, this president casually told Joseph Stalin that the United States had a powerful new weapon.",
          "Soon afterward, this president’s orders led to the atomic bombings of Hiroshima and Nagasaki. For 10 points, name this 33rd president."),
        T("This man, whose middle initial does not stand for any name, commanded an artillery unit called Battery D in France during World War I. He then opened a men’s clothing store in Kansas City with his army friend Eddie Jacobson, but it failed in 1922.",
          "He later became Franklin Roosevelt’s last vice president. For 10 points, name this Missouri politician who became the 33rd president."),
        T("This man’s 61st birthday was V-E Day, May 8, 1945, less than a month after he unexpectedly became president. He told reporters he felt “like the moon, the stars, and all the planets had fallen on me” when he took office.",
          "He had been vice president for only 82 days. For 10 points, name this man who succeeded Franklin Roosevelt."),
        T("In _Youngstown Sheet & Tube Co. v. Sawyer_, the Supreme Court ruled that this president had no power to take over the nation’s steel mills to head off a strike. Justice Robert Jackson’s concurring opinion in that 1952 case became a famous guide to presidential power.",
          "The seizure came during the Korean War. For 10 points, name this president who succeeded Franklin Roosevelt."),
        T("While the White House was being rebuilt, this president lived across the street at Blair House, where two Puerto Rican nationalists tried to kill him in 1950. White House police officer Leslie Coffelt died stopping the attack.",
          "Two years earlier, this president had beaten Thomas Dewey in a surprise victory. For 10 points, name this president."),
        T("In 1948, this president’s old army friend and business partner Eddie Jacobson persuaded him to meet a Zionist leader who later became Israel’s first president. That May, this president recognized the new state of Israel just 11 minutes after it declared independence.",
          "He also signed the Marshall Plan that year. For 10 points, name this president who took office after Franklin Roosevelt died."),
        T("During this president’s term, General Lucius Clay helped launch Operation Vittles, in which American planes flew food and coal into a city cut off by a Soviet blockade. That airlift lasted from 1948 to 1949, the same year the United States helped create NATO.",
          "That city was West Berlin. For 10 points, name this president whose namesake doctrine promised to help nations resist communism."),
        T("Congress passed the Taft–Hartley Act over this president’s veto in 1947, limiting labor unions and banning the “closed shop,” where only union members could be hired. In his 1948 campaign, he attacked that Republican-led Congress as the “Do-Nothing Congress.”",
          "His domestic program was called the Fair Deal. For 10 points, name this president who followed Franklin Roosevelt."),
        T("This president signed the National Security Act of 1947, which created the CIA and the National Security Council and made the Air Force a separate branch. That year, he chose George Marshall as his Secretary of State.",
          "Also in 1947, his namesake doctrine promised aid to Greece and Turkey to contain communism. For 10 points, name this president."),
        T("In 1965, Lyndon Johnson signed the Medicare bill at this former president’s library in Independence, Missouri, and handed him the first Medicare card. Years earlier, this man had asked Congress for national health insurance as part of his Fair Deal.",
          "He kept a sign on his desk reading “The buck stops here.” For 10 points, name this 33rd president."),
        T("This president was on stage in his home state when Winston Churchill gave his “Iron Curtain” speech at a small college in Fulton, Missouri, in 1946. Two years later, this president signed the European Recovery Program, which sent billions of dollars to rebuild Western Europe.",
          "That program is better known as the Marshall Plan. For 10 points, name this president who succeeded FDR."),
    ],
    "clues": [
        C("33rd", "giveaway", "33rd President (1945–1953); took office when Franklin Roosevelt died in April 1945", ["33rd", "franklin roosevelt", "april 1945"], "Franklin Delano Roosevelt"),
        C("atomic", "giveaway", "Ordered the atomic bombings of Hiroshima and Nagasaki (August 1945), and Japan surrendered", ["atomic", "hiroshima", "nagasaki"], "Manhattan Project"),
        C("buck", "giveaway", "Kept a sign on his desk that said “The buck stops here”", ["buck stops here", "buck", "desk"]),
        C("dewey", "giveaway", "Beat Thomas Dewey in the 1948 upset, then held up a newspaper that wrongly said Dewey had won", ["dewey", "1948", "newspaper", "upset"]),
        C("doctrine", "giveaway", "His doctrine (1947) promised aid to Greece and Turkey to contain communism", ["greece", "turkey", "contain", "doctrine"]),
        C("marshall-plan", "middle", "Signed the Marshall Plan (1948): billions of dollars to rebuild Western Europe, named for Secretary of State George Marshall", ["marshall plan", "george marshall", "europe"], "Marshall Plan"),
        C("berlin-airlift", "middle", "Berlin Airlift (1948–1949): planes flew food and coal into West Berlin during a Soviet blockade", ["berlin airlift", "west berlin", "blockade"]),
        C("korea-macarthur", "middle", "Sent U.S. troops into the Korean War (1950) and fired General Douglas MacArthur (1951)", ["korean war", "macarthur", "1951"], "Korean War"),
        C("eo-9981", "middle", "Executive Order 9981 (1948) ordered an end to segregation in the armed forces; Southern “Dixiecrats” ran Strom Thurmond against him", ["9981", "segregation", "dixiecrats", "thurmond"]),
        C("potsdam", "middle", "Met Joseph Stalin and Winston Churchill (then Clement Attlee) at the Potsdam Conference (1945)", ["potsdam", "stalin", "attlee"]),
        C("fair-deal", "middle", "Called his domestic program the Fair Deal, which included a plan for national health insurance", ["fair deal", "health insurance"]),
        C("nato", "middle", "The United States helped create NATO in 1949, while he was president", ["nato", "1949"], "NATO"),
        C("whistle-stop", "middle", "1948 “whistle-stop” train tour; his running mate, Alben Barkley, was nicknamed “the Veep”", ["whistle-stop", "barkley", "veep"]),
        C("pendergast", "power", "Kansas City boss Tom Pendergast’s political machine helped launch his career; elected senator from Missouri (1934)", ["pendergast", "kansas city", "machine", "1934"]),
        C("committee", "power", "As a senator, led a committee that investigated waste in World War II defense spending", ["committee", "waste", "defense"]),
        C("haberdashery", "power", "Ran a Kansas City men’s clothing store (a haberdashery) with Eddie Jacobson; it failed in 1922", ["haberdashery", "clothing store", "jacobson", "1922"]),
        C("battery-d", "power", "Commanded Battery D, an artillery unit, in France during World War I", ["battery d", "artillery", "france"]),
        C("s-initial", "power", "His middle initial, “S,” does not stand for any name", ["middle initial", "initial"]),
        C("82-days", "power", "Vice president for only 82 days; said he felt “like the moon, the stars, and all the planets had fallen on me”", ["82 days", "moon", "planets"]),
        C("v-e-day", "power", "V-E Day (May 8, 1945), when Germany surrendered, was his 61st birthday", ["v-e day", "birthday", "may 8"]),
        C("israel", "power", "Recognized Israel 11 minutes after it declared independence (May 1948)", ["israel", "11 minutes"]),
        C("youngstown", "power", "_Youngstown Sheet & Tube Co. v. Sawyer_ (1952): the Supreme Court said he could not seize the steel mills", ["youngstown", "steel mills", "sawyer"]),
        C("blair-house", "power", "Survived a 1950 attack by two Puerto Rican nationalists at Blair House; officer Leslie Coffelt died stopping it", ["blair house", "puerto rican", "coffelt"]),
        C("taft-hartley", "power", "Congress passed the Taft–Hartley Act (1947) over his veto; he blasted the “Do-Nothing Congress”", ["taft", "hartley", "do-nothing", "veto"]),
        C("national-security", "power", "Signed the National Security Act (1947), which created the CIA and the National Security Council", ["national security act", "national security council", "cia"]),
        C("medicare", "power", "Got the first Medicare card from Lyndon Johnson at his library in Independence, Missouri (1965)", ["medicare", "independence", "1965"]),
        C("iron-curtain", "power", "Was on stage when Winston Churchill gave his 1946 “Iron Curtain” speech in Fulton, Missouri", ["iron curtain", "fulton", "churchill"]),
        C("police-action", "power", "Agreed with a reporter who called the Korean fighting a “police action” under the United Nations", ["police action", "united nations", "reporter"]),
    ],
    "trap": {
        "title": "Truman, FDR, or Ike?",
        "body": "Truman’s presidency sits between two giants. Franklin Roosevelt led most of World War II and went to Yalta, but he died in April 1945, so the Potsdam Conference, V-E Day, and the atomic bombs belong to Truman. Dwight Eisenhower signed the Korean War armistice in 1953, but it was Truman who sent troops to Korea in 1950 and fired MacArthur.",
        "fix": "Pearl Harbor, the New Deal, and Yalta mean FDR. Potsdam, the atomic bombs, the Marshall Plan, the Berlin Airlift, and firing MacArthur mean Truman. The Korean War armistice and the interstate highways mean Eisenhower. If a question asks for a policy (“this doctrine”), answer “Truman Doctrine,” not just his name.",
        "line": "Real answer line: Harry S. <b><u>Truman</u></b>"
    },
    "tests": {
        "right": [
            "Harry S. Truman",
            "Harry Truman",
            "Truman",
            "President Truman",
            "Harry Trueman"
        ],
        "prompt": [
            "Harry"
        ],
        "wrong": [
            "Truman Capote",
            "Truman Doctrine",
            "Dwight Eisenhower",
            "Franklin Roosevelt",
            "Thomas Dewey",
            "Bess Truman"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
