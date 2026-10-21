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


QUOTE = "“segregation now, segregation tomorrow, segregation forever”"

data = {
    "id": "george-wallace",
    "name": "George Wallace",
    "mono": "GCW",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "Alabama governor who fought desegregation · Ran for president four times",
    "dates": "1919–1998",
    "briefing": "George Wallace became governor of Alabama in 1963 and promised “segregation now, segregation tomorrow, segregation forever,” and that June he stood in a doorway at the University of Alabama to block two Black students until federalized National Guard troops arrived. He ran for president four times, and in 1972 a gunman shot him in Maryland, leaving him paralyzed. In his later years, he said he had been wrong about segregation and asked for forgiveness.",
    "answerHtml": "George <b><u>Wallace</u></b> (accept George Corley <u>Wallace</u> Jr.; do not accept “Lurleen Wallace”)",
    "accept": [
        "george wallace",
        "george c wallace",
        "george corley wallace",
        "george corley wallace jr",
        "george c wallace jr",
        "george wallace jr",
        "wallace",
        "governor wallace",
        "governor george wallace"
    ],
    "prompt": [],
    "reject": [
        "lurleen wallace",
        "lurleen",
        "lurleen burns wallace",
        "george wallace iii",
        "henry wallace",
        "henry a wallace",
        "william wallace",
        "alfred russel wallace",
        "alfred wallace",
        "lew wallace",
        "mike wallace",
        "chris wallace",
        "david foster wallace",
        "wallace stevens",
        "orval faubus",
        "faubus",
        "ross barnett",
        "barnett",
        "lester maddox",
        "maddox",
        "strom thurmond",
        "thurmond",
        "bull connor",
        "eugene bull connor",
        "curtis lemay",
        "lemay",
        "arthur bremer",
        "bremer",
        "john patterson",
        "jim clark",
        "james hood",
        "vivian malone",
        "nicholas katzenbach",
        "katzenbach",
        "frank johnson",
        "john f kennedy",
        "robert f kennedy",
        "jimmy carter",
        "hubert humphrey",
        "richard nixon"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/George_Wallace",
    "qb": {
        "q": "George Wallace",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        T("As a teenager, this man won a state Golden Gloves boxing championship. After earning a law degree from the University of Alabama in 1942, he served as a flight engineer on B-29 bombers in the Pacific during World War II.",
          "For 10 points, name this Alabama governor who promised “segregation now, segregation tomorrow, segregation forever.”"),
        T("In June 1963, Deputy Attorney General Nicholas Katzenbach [“KATS-en-bahk”] confronted this man outside Foster Auditorium in Tuscaloosa, where he was trying to keep two Black students, Vivian Malone and James Hood, from enrolling.",
          "President John F. Kennedy then federalized the Alabama National Guard. For 10 points, name this governor known for the “Stand in the Schoolhouse Door.”"),
        T("Because Alabama’s constitution did not let him serve two terms in a row, this man’s wife, Lurleen, ran for governor in 1966 and won. She died in office in 1968, the same year this man ran for president.",
          "For 10 points, name this Alabama governor who ran as the American Independent Party candidate in 1968."),
        T("In 1968, this man won five Southern states and 46 electoral votes as a third-party candidate, with retired Air Force general Curtis LeMay as his running mate. His campaign slogan was “Stand Up for America.”",
          "For 10 points, name this Alabama governor who ran for president as the American Independent Party candidate."),
        T("Arthur Bremer was convicted of shooting this man at a shopping center in May 1972. The day after that attack, this man won the Democratic presidential primaries in Maryland and Michigan.",
          "The shooting, in Laurel, Maryland, left him paralyzed. For 10 points, name this Alabama governor who made the “Stand in the Schoolhouse Door.”"),
        T("In March 1965, this governor ordered Alabama state troopers to stop a voting rights march from Selma to Montgomery, and the troopers attacked the marchers at the Edmund Pettus Bridge on “Bloody Sunday.” Later that month, the march went ahead under federal protection.",
          "For 10 points, name this Alabama governor who had promised “segregation now, segregation tomorrow, segregation forever.”"),
        T("Federal judge Frank Johnson, who had been this man’s classmate at the University of Alabama’s law school, ruled in a 1965 case bearing this man’s name that the Selma-to-Montgomery march could go forward.",
          "The march ended at the state capitol in Montgomery. For 10 points, name this Alabama governor who had tried to stop it."),
        T("During one presidential campaign, this man claimed there was not “a dime’s worth of difference” between the Democratic and Republican parties. In that 1968 race, he carried his home state and four other Southern states.",
          "For 10 points, name this Alabama governor who ran on the American Independent Party ticket."),
        T("This former state circuit judge lost the 1958 race for governor of Alabama to John Patterson. After that defeat, he took a hard-line stand for segregation and won the governorship four years later.",
          "For 10 points, name this man who became Alabama’s governor in January 1963 and promised “segregation now, segregation tomorrow, segregation forever.”"),
        T("On the evening of June 11, 1963, hours after this man ended a standoff with federal officials, President John F. Kennedy gave a televised speech calling for a new civil rights law. That law, the Civil Rights Act, was signed the next year by Lyndon Johnson.",
          "For 10 points, name this governor who had tried to block two Black students from enrolling at the University of Alabama."),
        T("In 1964, this man made his first run for president, winning roughly a third of the vote in the Democratic primaries in Wisconsin and Indiana and even more in Maryland. Those results showed that his message had support outside the South.",
          "For 10 points, name this Alabama governor who later ran for president in 1968, 1972, and 1976."),
        T("In his later years, this man said he had been wrong about segregation and asked Black Alabamians for forgiveness. In 1982, he won his fourth and last term as governor with substantial support from Black voters.",
          "For 10 points, name this Alabama governor who had made the “Stand in the Schoolhouse Door” in 1963."),
        T("This man made his fourth and final run for president in 1976, when former Georgia governor Jimmy Carter defeated him in the Florida Democratic primary. By then, he had been using a wheelchair for four years.",
          "For 10 points, name this Alabama governor who was shot in Laurel, Maryland, in 1972."),
        T("In January 1963, this man gave his first inaugural address as governor at the state capitol in Montgomery, standing on a star that marked the spot where Jefferson Davis had been sworn in as Confederate president.",
          "In that speech, he promised “segregation now, segregation tomorrow, segregation forever.” For 10 points, name this governor."),
        T("Brigadier General Henry Graham of the Alabama National Guard asked this man to step aside after President Kennedy placed the Guard under federal control. This man then left the doorway he had been blocking at Foster Auditorium.",
          "For 10 points, name this governor who made the “Stand in the Schoolhouse Door” at the University of Alabama in 1963.")
    ],
    "clues": [
        C("segregation-forever", "giveaway", f"Governor of Alabama whose 1963 inaugural address promised {QUOTE}", ["segregation forever", "inaugural", "alabama"]),
        C("schoolhouse-door", "giveaway", "The “Stand in the Schoolhouse Door” (June 1963): tried to block two Black students from enrolling at the University of Alabama", ["schoolhouse door", "university of alabama"]),
        C("american-independent", "giveaway", "Ran for president in 1968 as the American Independent Party candidate", ["american independent party", "1968"]),
        C("laurel", "giveaway", "Shot in 1972 while campaigning in Laurel, Maryland, which left him paralyzed from the waist down", ["laurel", "paralyzed", "1972"]),
        C("national-guard", "middle", "Stepped aside after President Kennedy federalized the Alabama National Guard", ["national guard", "federalized", "kennedy"], "John F. Kennedy"),
        C("malone-hood", "middle", "The two students were Vivian Malone and James Hood", ["vivian malone", "james hood"]),
        C("katzenbach", "middle", "Deputy Attorney General Nicholas Katzenbach confronted him at Foster Auditorium in Tuscaloosa", ["katzenbach", "foster auditorium", "tuscaloosa"]),
        C("lemay", "middle", "1968 running mate: retired Air Force general Curtis LeMay; he won five Southern states", ["curtis lemay", "lemay", "five southern states"]),
        C("selma", "middle", "Ordered state troopers to stop the 1965 Selma-to-Montgomery march; troopers attacked marchers on “Bloody Sunday”", ["selma", "bloody sunday", "state troopers"]),
        C("lurleen", "middle", "His wife, Lurleen, was elected governor in 1966 when he could not run for a second straight term; she died in office in 1968", ["lurleen", "1966"]),
        C("forgiveness", "middle", "In his later years, said he had been wrong about segregation and asked for forgiveness", ["forgiveness", "wrong"]),
        C("four-terms", "middle", "Elected governor four times; served 1963–1967, 1971–1979, and 1983–1987", ["four times", "1983"]),
        C("four-runs", "middle", "Ran for president four times: 1964, 1968, 1972, and 1976", ["1964", "1976"]),
        C("golden-gloves", "power", "Won a state Golden Gloves boxing title as a teenager", ["golden gloves", "boxing"]),
        C("b-29", "power", "Flight engineer on B-29 bombers in the Pacific during World War II", ["b-29", "flight engineer"]),
        C("patterson", "power", "A former circuit judge, he lost the 1958 governor’s race to John Patterson", ["john patterson", "circuit judge", "1958"]),
        C("bremer", "power", "Arthur Bremer shot him; the next day he won the Maryland and Michigan primaries", ["arthur bremer", "bremer", "michigan"]),
        C("dime", "power", "Said there was not “a dime’s worth of difference” between the two major parties", ["dime’s worth", "difference"]),
        C("stand-up", "power", "1968 slogan: “Stand Up for America”; he won 46 electoral votes", ["stand up for america", "46 electoral votes"]),
        C("frank-johnson", "power", "Judge Frank Johnson, his law school classmate, ruled in a 1965 case bearing his name that the Selma march could go on", ["frank johnson", "classmate"]),
        C("jfk-speech", "power", "That same evening (June 11, 1963), President Kennedy gave a televised speech calling for a civil rights law", ["june 11, 1963", "televised", "civil rights"]),
        C("henry-graham", "power", "General Henry Graham of the federalized Alabama National Guard asked him to step aside", ["henry graham", "step aside"]),
        C("jefferson-davis", "power", "Gave his 1963 inaugural address standing on the star marking where Jefferson Davis took the Confederate oath", ["jefferson davis", "star"]),
        C("primaries-1964", "power", "In 1964, won roughly a third of the vote in the Wisconsin and Indiana Democratic primaries", ["wisconsin", "indiana"]),
        C("carter-1976", "power", "Lost the 1976 Florida primary to Jimmy Carter in his last run for president", ["jimmy carter", "florida"]),
        C("black-voters-1982", "power", "Won his last term as governor in 1982 with substantial support from Black voters", ["black voters", "1982"]),
        C("forrest-gump", "power", "The title character of _Forrest Gump_ (1994) appears in old news footage of his stand at the University of Alabama", ["forrest gump", "footage"])
    ],
    "trap": {
        "title": "Which segregationist governor?",
        "body": "Several Southern governors tried to block school integration, and their clues get mixed up. George Wallace stood in the doorway at the University of Alabama in 1963; Orval Faubus of Arkansas used the National Guard to keep the Little Rock Nine out of Central High School in 1957; and Ross Barnett of Mississippi tried to stop James Meredith from entering the University of Mississippi in 1962. Strom Thurmond ran as a third-party Dixiecrat in 1948, twenty years before Wallace’s third-party run.",
        "fix": "Alabama, Tuscaloosa, Vivian Malone and James Hood, Selma, the American Independent Party, and Laurel, Maryland, mean Wallace. Little Rock means Faubus, and Ole Miss means Barnett. Don’t confuse him with his wife, Lurleen Wallace, who was governor from 1967 to 1968, or with Henry Wallace, Franklin Roosevelt’s vice president.",
        "line": "Real answer line: George <b><u>Wallace</u></b> (accept George Corley <u>Wallace</u> Jr.; do not accept “Lurleen Wallace”)"
    },
    "tests": {
        "right": [
            "George Wallace",
            "Wallace",
            "George C. Wallace",
            "Governor George Wallace",
            "George Wallce"
        ],
        "prompt": [],
        "wrong": [
            "Lurleen Wallace",
            "Henry Wallace",
            "Orval Faubus",
            "Strom Thurmond",
            "Wallace Stevens",
            "Ross Barnett"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
