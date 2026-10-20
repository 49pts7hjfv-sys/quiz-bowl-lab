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
    "id": "vietnam-war",
    "name": "Vietnam War",
    "mono": "VN",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "Cold War conflict in Southeast Asia · Ended with the fall of Saigon in 1975",
    "dates": "Fought 1955–1975",
    "briefing": "From the 1950s to 1975, Communist North Vietnam and its Viet Cong allies fought to unite the country under their rule, while South Vietnam and the United States tried to stop them. More than 58,000 Americans and over a million Vietnamese died, and protests against the war spread across American college campuses. The war ended in 1975, when North Vietnamese tanks rolled into Saigon, the South’s capital.",
    "answerHtml": "<b><u>Vietnam</u></b> War (accept <u>Second Indochina War</u> or <u>American War</u>; prompt on <u>Indochina War</u>; do not accept “First Indochina War” or “Korean War”)",
    "accept": [
        "vietnam war",
        "vietnam",
        "the vietnam war",
        "viet nam war",
        "viet nam",
        "war in vietnam",
        "vietnam conflict",
        "second indochina war",
        "2nd indochina war",
        "american war",
        "american war in vietnam",
        "resistance war against america"
    ],
    "prompt": [
        "indochina war",
        "indochina wars",
        "indochina"
    ],
    "reject": [
        "first indochina war",
        "1st indochina war",
        "french indochina war",
        "third indochina war",
        "korean war",
        "korea",
        "cold war",
        "gulf war",
        "persian gulf war",
        "iraq war",
        "war in afghanistan",
        "afghanistan war",
        "mexican american war",
        "spanish american war",
        "philippine american war",
        "anglo american war",
        "american war of independence",
        "american war for independence",
        "american revolutionary war",
        "american civil war",
        "north vietnam",
        "south vietnam",
        "vietnam veterans memorial",
        "vietnam war memorial",
        "vietnam memorial",
        "vietnamization",
        "tet offensive",
        "tet",
        "gulf of tonkin",
        "tonkin",
        "viet cong",
        "viet minh",
        "ho chi minh",
        "laos",
        "cambodia",
        "my lai"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Vietnam_War",
    "qb": {
        "q": "Vietnam War",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {"n": 0, "note": "no real tossups checked yet"},
    "tossups": [
        T("Ngo Dinh Diem became the first president of the South after the Geneva Accords of 1954 divided his country at the 17th parallel. Diem was overthrown and killed in a 1963 coup as a Communist-backed guerrilla war against his government grew.",
          "American leaders feared that losing this fight would make nearby countries fall like dominoes. For 10 points, name this war that ended with the fall of Saigon in 1975."),
        T("In August 1964, the destroyer USS _Maddox_ clashed with torpedo boats, and a second attack reported two days later probably never happened. Within a week, Congress passed a resolution letting President Lyndon Johnson use military force without a declaration of war.",
          "That Gulf of Tonkin Resolution led to a huge buildup of U.S. troops. For 10 points, name this war against the Viet Cong."),
        T("Weeks after a surprise offensive, CBS anchor Walter Cronkite told TV viewers that the United States seemed “mired in stalemate” in this war. That offensive, which included an attack on the U.S. Embassy in Saigon, began during a Lunar New Year holiday in 1968.",
          "Soon afterward, President Lyndon Johnson announced he would not run again. For 10 points, name this war that included the Tet Offensive."),
        T("In May 1970, Ohio National Guard troops fired on a crowd at Kent State University, killing four students during protests against this war. Those protests had erupted after President Richard Nixon announced that U.S. troops were entering neighboring Cambodia.",
          "For 10 points, name this war that sparked huge protests on American college campuses in the 1960s and 1970s."),
        T("Le Duc Tho [“lay duck TOH”] turned down the Nobel Peace Prize he was awarded along with Henry Kissinger for negotiating a cease-fire in this war. The two men worked out the Paris Peace Accords, which were signed in January 1973 and led to the withdrawal of U.S. combat troops.",
          "Fighting went on without the Americans until 1975. For 10 points, name this war that ended when Saigon fell."),
        T("During Operation Frequent Wind, U.S. helicopters carried thousands of people out of a capital city as Communist troops closed in. On April 30, 1975, a tank crashed through the gates of that city’s presidential palace, and the city was later renamed for the North’s longtime leader.",
          "That city was Saigon, and the leader was Ho Chi Minh. For 10 points, name this war that ended with Saigon’s fall."),
        T("Daniel Ellsberg secretly copied a top-secret Defense Department history of this war and leaked it to reporters. In 1971, the Supreme Court ruled in _New York Times Co. v. United States_ that newspapers could go on printing that study, known as the Pentagon Papers.",
          "The study showed that several presidents had not told the public the whole truth about this war. For 10 points, name this war fought against the Viet Cong."),
        T("Maya Lin was still a college student when she won the contest to design a memorial to this war’s American dead and missing: a black granite wall on the National Mall carved with more than 58,000 names. It was dedicated in 1982.",
          "For 10 points, name this war in Southeast Asia that ended with the fall of Saigon in 1975."),
        T("Trucks and porters carried supplies south along a network of jungle paths through Laos and Cambodia that was named for this war’s most famous Communist leader. American planes bombed that route for years but never managed to shut it down.",
          "Those supplies helped the Viet Cong guerrillas in the South. For 10 points, name this war in which the North was led by Ho Chi Minh."),
        T("In March 1965, U.S. Marines waded ashore at Da Nang [“dah NANG”] as the first American ground combat troops sent to this war. That same month, Operation Rolling Thunder began more than three years of bombing raids on the Communist North.",
          "For 10 points, name this war that President Lyndon Johnson expanded after the Gulf of Tonkin Resolution."),
        T("In a 1969 speech, President Richard Nixon asked the “silent majority” of Americans to back his plan for this war. That plan trained the South’s army to take over the fighting so that American troops could gradually come home.",
          "Nixon had inherited this war from Lyndon Johnson. For 10 points, name this war fought against the Viet Cong."),
        T("Congress passed the War Powers Resolution over President Nixon’s veto in 1973, largely in reaction to this war. That law limits how long a president can keep troops in combat without approval from Congress.",
          "Congress never formally declared this war against the Viet Cong and the North. For 10 points, name this war that ended in 1975."),
        T("Arguments that anyone old enough to be drafted for this war was old enough to vote helped pass the 26th Amendment, which lowered the voting age to 18. Boxer Muhammad Ali lost his heavyweight title after he refused to be drafted to fight in it.",
          "A 1969 draft lottery used birthdays to decide who would be called first. For 10 points, name this war fought against the Viet Cong."),
        T("In 1968, U.S. soldiers on a “search and destroy” mission killed hundreds of unarmed villagers at My Lai [“mee LYE”], and Lieutenant William Calley was later convicted for his role. Back in 1965, the Battle of Ia Drang [“EE-ah DRANG”] had been the first major clash between U.S. troops and the North’s army.",
          "General William Westmoreland commanded U.S. forces during those years. For 10 points, name this war against the Viet Cong."),
        T("Navy pilot John McCain spent more than five years as a prisoner of war, partly in Hanoi’s Hoa Lo [“hwah LOH”] Prison, which American captives nicknamed the “Hanoi Hilton.” He and hundreds of other prisoners came home in 1973, after a peace agreement was signed in Paris.",
          "McCain had been shot down over the North in 1967. For 10 points, name this war that ended with the fall of Saigon."),
    ],
    "clues": [
        C("north-south", "giveaway", "The Communist North (capital Hanoi) and the Viet Cong fought the South (capital Saigon) and the United States", ["hanoi", "saigon", "viet cong", "communist"]),
        C("fall-of-saigon", "giveaway", "Ended when Saigon fell to the North on April 30, 1975; the city was renamed Ho Chi Minh City", ["saigon", "1975", "ho chi minh city"]),
        C("tonkin", "giveaway", "Gulf of Tonkin Resolution (1964): after clashes with U.S. destroyers, Congress let President Lyndon Johnson expand the fighting", ["gulf of tonkin", "tonkin", "lyndon johnson", "1964"], "Lyndon B. Johnson"),
        C("tet", "giveaway", "Tet Offensive (1968): surprise attacks across the South during the Lunar New Year turned many Americans against the war", ["tet offensive", "lunar new year", "1968"]),
        C("protests", "giveaway", "Sparked huge antiwar protests in the U.S.; supporters of the war were called “hawks” and opponents “doves”", ["antiwar", "protests", "hawks", "doves"]),
        C("ho-chi-minh", "middle", "Ho Chi Minh led the North until he died in 1969; the Ho Chi Minh Trail carried supplies through Laos and Cambodia", ["ho chi minh trail", "laos", "cambodia", "1969"]),
        C("geneva", "middle", "The Geneva Accords (1954) split the country at the 17th parallel after the French lost at Dien Bien Phu", ["17th parallel", "geneva", "dien bien phu", "french"]),
        C("domino", "middle", "Domino theory: U.S. leaders feared that if one country fell to communism, its neighbors would fall too", ["domino", "communism"]),
        C("paris-accords", "middle", "Paris Peace Accords (January 1973), negotiated by Henry Kissinger and Le Duc Tho, ended U.S. combat", ["paris peace accords", "kissinger", "le duc tho", "1973"]),
        C("kent-state", "middle", "Kent State (May 1970): Ohio National Guard troops killed four students during protests against the invasion of Cambodia", ["kent state", "national guard", "ohio", "cambodia"]),
        C("nixon-plan", "middle", "Richard Nixon’s plan trained the South’s army to take over the fighting as U.S. troops came home; he asked the “silent majority” for support (1969)", ["nixon", "silent majority", "south’s army"], "Richard Nixon"),
        C("westmoreland", "middle", "General William Westmoreland commanded U.S. forces (1964–1968) and sent troops on “search and destroy” missions", ["westmoreland", "search and destroy"]),
        C("rolling-thunder", "middle", "March 1965: Marines landed at Da Nang, and Operation Rolling Thunder began bombing the North (1965–1968)", ["rolling thunder", "da nang", "marines"]),
        C("diem", "power", "Ngo Dinh Diem, the South’s first president, was overthrown and killed in a 1963 coup", ["diem", "coup", "1963"]),
        C("maddox", "power", "The destroyer USS _Maddox_ clashed with torpedo boats in August 1964; a second reported attack probably never happened", ["maddox", "torpedo", "second"]),
        C("cronkite", "power", "After Tet, CBS anchor Walter Cronkite said the war seemed “mired in stalemate”; Lyndon Johnson then chose not to run again (1968)", ["cronkite", "stalemate", "cbs"]),
        C("pentagon-papers", "power", "Daniel Ellsberg leaked the Pentagon Papers, a secret history of the war; _New York Times Co. v. United States_ (1971) let papers print them", ["pentagon papers", "ellsberg", "new york times"]),
        C("war-powers", "power", "The War Powers Resolution (1973), passed over Nixon’s veto, limits how long a president can keep troops in combat without Congress", ["war powers", "veto", "1973"]),
        C("ia-drang", "power", "Battle of Ia Drang (1965): the first major clash between U.S. troops and the North’s army", ["ia drang", "1965"]),
        C("my-lai", "power", "My Lai (1968): U.S. soldiers killed hundreds of unarmed villagers; Lieutenant William Calley was convicted", ["my lai", "calley", "villagers"]),
        C("maya-lin", "power", "Maya Lin designed its memorial in Washington, D.C.: a black granite wall with more than 58,000 names (1982)", ["maya lin", "granite", "58,000", "1982"]),
        C("ali", "power", "Muhammad Ali refused to be drafted (1967) and was stripped of his boxing title; the Supreme Court overturned his conviction (1971)", ["muhammad ali", "drafted", "boxing"]),
        C("draft-lottery", "power", "A draft lottery held on December 1, 1969, used birthdays to decide who would be called up first", ["draft lottery", "lottery", "birthdays"]),
        C("26th-amendment", "power", "The 26th Amendment (1971) lowered the voting age to 18: anyone old enough to be drafted should be old enough to vote", ["26th amendment", "voting age", "drafted"]),
        C("mccain", "power", "Navy pilot John McCain was a prisoner of war for more than five years, partly in the “Hanoi Hilton”", ["mccain", "hanoi hilton", "prisoner"]),
        C("nobel", "power", "Le Duc Tho turned down the 1973 Nobel Peace Prize he was awarded along with Henry Kissinger", ["nobel", "turned down", "le duc tho"]),
        C("frequent-wind", "power", "Operation Frequent Wind (April 1975): helicopters carried thousands of people out of Saigon", ["frequent wind", "helicopters"]),
    ],
    "trap": {
        "title": "Which Indochina war?",
        "body": "Vietnam saw two big wars in a row. In the First Indochina War (1946–1954), Ho Chi Minh’s Viet Minh defeated France, ending with the French surrender at Dien Bien Phu; this war came next, which is why it is also called the Second Indochina War. Players also mix it up with the Korean War (1950–1953), another Cold War fight between a Communist north and a U.S.-backed south.",
        "fix": "French generals, Dien Bien Phu, and dates before 1955 mean the First Indochina War. The Gulf of Tonkin, Tet, the Viet Cong, Nixon’s “Vietnamization” plan, Kent State, and the fall of Saigon mean this war. The 38th parallel, Inchon, and Truman firing MacArthur mean Korea; the 17th parallel means this war.",
        "line": "Real answer line: <b><u>Vietnam</u></b> War (accept <u>Second Indochina War</u> or <u>American War</u>; prompt on <u>Indochina War</u>)"
    },
    "tests": {
        "right": [
            "Vietnam War",
            "Vietnam",
            "The Vietnam War",
            "Second Indochina War",
            "American War",
            "Veitnam War"
        ],
        "prompt": [
            "Indochina War"
        ],
        "wrong": [
            "Korean War",
            "First Indochina War",
            "Cold War",
            "Mexican-American War",
            "Tet Offensive",
            "North Vietnam",
            "Vietnam Veterans Memorial"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
