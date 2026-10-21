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
    "id": "malcolm-x",
    "name": "Malcolm X",
    "mono": "MX",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "Muslim minister and Black nationalist leader · “By any means necessary”",
    "dates": "1925–1965",
    "briefing": "Malcolm X was born Malcolm Little in Omaha, Nebraska, and educated himself in prison by copying a dictionary by hand, joining the Nation of Islam there. As the group’s outspoken national spokesman, he preached Black pride, self-defense, and separation from white America, and he criticized the nonviolent civil rights movement. After leaving the group and making the hajj to Mecca in 1964, he took the name El-Hajj Malik El-Shabazz; he was killed in New York City in February 1965.",
    "answerHtml": "<b><u>Malcolm X</u></b> (accept <u>Malcolm Little</u> or <u>El-Hajj Malik El-Shabazz</u>; prompt on <u>Malcolm</u> alone; do not accept “Elijah Muhammad”)",
    "accept": [
        "malcolm x",
        "malcolm little",
        "el hajj malik el shabazz",
        "malik el shabazz",
        "el hajj malik shabazz",
        "malik shabazz",
        "minister malcolm x",
        "brother malcolm x"
    ],
    "prompt": [
        "malcolm",
        "detroit red",
        "shabazz",
        "el shabazz",
        "x"
    ],
    "reject": [
        "martin luther king jr",
        "martin luther king",
        "martin luther king junior",
        "mlk",
        "king",
        "elijah muhammad",
        "muhammad",
        "wallace fard muhammad",
        "wallace d fard",
        "w d fard",
        "fard",
        "louis farrakhan",
        "farrakhan",
        "muhammad ali",
        "cassius clay",
        "alex haley",
        "haley",
        "betty shabazz",
        "betty x",
        "betty sanders",
        "attallah shabazz",
        "qubilah shabazz",
        "ilyasah shabazz",
        "marcus garvey",
        "garvey",
        "earl little",
        "louise little",
        "ella little collins",
        "reginald little",
        "stokely carmichael",
        "kwame ture",
        "huey newton",
        "huey p newton",
        "bobby seale",
        "medgar evers",
        "john lewis",
        "nation of islam",
        "black panther party",
        "black panthers",
        "organization of afro american unity",
        "oaau",
        "autobiography of malcolm x",
        "the autobiography of malcolm x",
        "malcolm gladwell",
        "malcolm in the middle",
        "talmadge hayer",
        "thomas hagan",
        "muhammad abdul aziz",
        "muhammad aziz",
        "khalil islam",
        "w e b du bois",
        "booker t washington",
        "frederick douglass",
        "james baldwin",
        "ossie davis"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Malcolm_X",
    "qb": {
        "q": "Malcolm X",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {"n": 0, "note": "no real tossups checked yet"},
    "tossups": [
        T("This man’s mother was born on the Caribbean island of Grenada, and his father, a Baptist preacher, organized for Marcus Garvey’s movement. Born in Omaha, Nebraska, in 1925, this man grew up mostly in and around Lansing, Michigan, where his family was split up in the years after his father’s death.",
          "For 10 points, name this Nation of Islam minister who told his life story to Alex Haley."),
        T("While serving a prison sentence for burglary in Massachusetts, this man educated himself by copying an entire dictionary by hand. Letters from his brother Reginald and other relatives drew him to a religious movement, which he joined before his release in 1952.",
          "That movement was the Nation of Islam, led by Elijah Muhammad. For 10 points, name this man who became its most famous minister."),
        T("As a teenager, this man moved to Boston’s Roxbury neighborhood to live with his half-sister Ella, and later in Harlem he was nicknamed “Detroit Red” for his reddish hair and his Michigan roots. He was sent to prison in 1946 and spent more than six years there.",
          "Like other members of the Nation of Islam, he replaced his last name with a letter standing for his lost African family name. For 10 points, name this man."),
        T("Starting in 1954, this man led Temple No. 7 in Harlem, and around 1960 he founded the newspaper _Muhammad Speaks_. Before that, he helped open new temples in Boston and Philadelphia, and as a national spokesman he helped his religious group grow rapidly during the 1950s.",
          "For 10 points, name this Nation of Islam minister, who broke with Elijah Muhammad in 1964."),
        T("Mike Wallace and Louis Lomax made the 1959 TV documentary _The Hate That Hate Produced_, which introduced millions of viewers to this man and the religious group he spoke for. That group taught that Black Americans should separate from white society and build their own businesses and communities.",
          "That group, led by Elijah Muhammad, was the Nation of Islam. For 10 points, name its most famous spokesman."),
        T("After this man said that the assassination of John F. Kennedy was a case of “the chickens coming home to roost,” his religious leader ordered him to stay silent for 90 days. In March 1964, he announced that he was leaving that leader’s movement.",
          "That leader was Elijah Muhammad of the Nation of Islam. For 10 points, name this man, who later founded the Organization of Afro-American Unity."),
        T("This man became a friend of a young boxer and visited his training camp in Miami before that boxer won the heavyweight title from Sonny Liston in 1964. The two men split after this man left his religious group, and the boxer, who had taken the name Muhammad Ali, stayed with its leader.",
          "That leader was Elijah Muhammad. For 10 points, name this Muslim minister who told his life story to Alex Haley."),
        T("In his 1963 “Message to the Grass Roots” speech in Detroit, this man argued that there is no such thing as a nonviolent revolution. That same year, he mocked the March on Washington as the “Farce on Washington.”",
          "For 10 points, name this Nation of Islam minister, a critic of Martin Luther King Jr.’s nonviolent approach."),
        T("In an April 1964 speech in Cleveland, this man warned that the year would bring either “the ballot or the bullet,” urging Black Americans to use their votes and to defend themselves. He gave that speech a few weeks after leaving his old religious movement.",
          "That movement was the Nation of Islam. For 10 points, name this Black nationalist leader who was killed in 1965."),
        T("In an April 1964 letter, this man described pilgrims “of all colors” worshipping together as equals during a religious journey, an experience that changed his views on race. Afterward, he embraced Sunni Islam and moved away from the racial teachings of his former group.",
          "That journey was the hajj to Mecca, after which he took a new Muslim name. For 10 points, name this American leader."),
        T("At the June 1964 founding rally of a group modeled on the Organization of African Unity, this man promised to win freedom and equality for Black Americans. During a trip through Africa that year, he met Ghana’s president, Kwame Nkrumah.",
          "At that rally, he vowed to win those goals “by any means necessary.” For 10 points, name this founder of the Organization of Afro-American Unity."),
        T("This man met Martin Luther King Jr. only once, at the U.S. Capitol in March 1964 during the Senate debate over the Civil Rights Act. In February 1965, he spoke in Selma while King was in jail there, and told Coretta Scott King he hoped to make her husband’s work easier.",
          "Weeks later, he was killed in New York. For 10 points, name this former Nation of Islam spokesman."),
        T("In a December 1964 debate at Oxford University in England, this man defended the idea that “extremism in the defense of liberty is no vice,” a line made famous by Barry Goldwater. He also planned to charge the United States with violating human rights before the United Nations.",
          "For 10 points, name this American Muslim leader, who had founded the Organization of Afro-American Unity that June."),
        T("In 2021, a New York judge threw out the murder convictions of Muhammad Aziz and Khalil Islam, two men who had each spent about twenty years in prison for this man’s killing, after investigators found that evidence had been withheld. At this man’s funeral, the actor Ossie Davis called him “our own black shining Prince.”",
          "He had been shot as he began a speech at the Audubon Ballroom in February 1965. For 10 points, name this Muslim leader."),
        T("Spike Lee directed a 1992 film about this man, with Denzel Washington, who earned an Academy Award nomination, in the title role and Angela Bassett as his wife, Betty. That film was based on a 1965 book published months after this man’s death.",
          "That book was the autobiography he told to Alex Haley, who later wrote _Roots_. For 10 points, name this man.")
    ],
    "clues": [
        C("noi", "giveaway", "Leading minister and national spokesman of the Nation of Islam under Elijah Muhammad",
          ["nation of islam", "elijah muhammad", "spokesman"]),
        C("autobiography", "giveaway", "Told his life story to Alex Haley; the autobiography came out in 1965",
          ["alex haley", "haley", "autobiography"], "Roots"),
        C("killed", "giveaway", "Killed on February 21, 1965, at the Audubon Ballroom in New York City",
          ["audubon ballroom", "audubon", "1965"]),
        C("any-means", "giveaway", "Famous phrase: “by any means necessary”",
          ["any means necessary", "by any means"]),
        C("hajj", "giveaway", "Made the hajj to Mecca in 1964 and took a new Muslim name",
          ["hajj", "mecca", "1964"], "Hajj"),
        C("omaha", "middle", "Born in Omaha, Nebraska, in 1925; grew up mostly around Lansing, Michigan",
          ["omaha", "nebraska", "lansing"]),
        C("prison", "middle", "In prison (1946–1952), copied a dictionary by hand; his brother Reginald drew him to the Nation of Islam",
          ["prison", "dictionary", "reginald"]),
        C("letter-x", "middle", "Replaced his last name with a letter standing for his lost African family name",
          ["last name", "african family name", "letter"]),
        C("oaau", "middle", "Left the Nation of Islam in March 1964 and founded the Organization of Afro-American Unity (OAAU)",
          ["organization of afro-american unity", "oaau", "march 1964"]),
        C("ballot", "middle", "“The Ballot or the Bullet” speech (April 1964, Cleveland)",
          ["ballot", "bullet", "cleveland"]),
        C("chickens", "middle", "Called JFK’s assassination “the chickens coming home to roost”; Elijah Muhammad silenced him for 90 days",
          ["chickens", "roost", "90 days"]),
        C("mlk", "middle", "Met Martin Luther King Jr. only once, at the U.S. Capitol in March 1964",
          ["martin luther king", "capitol", "only once"], "Martin Luther King Jr."),
        C("ali", "middle", "Friend of the boxer Cassius Clay, who became Muhammad Ali",
          ["cassius clay", "muhammad ali", "boxer"]),
        C("spike-lee", "middle", "Spike Lee’s 1992 film about him starred Denzel Washington",
          ["spike lee", "denzel washington", "1992"]),
        C("grenada-garvey", "power", "His mother was born in Grenada; his father, a Baptist preacher, organized for Marcus Garvey",
          ["grenada", "marcus garvey", "garvey"]),
        C("detroit-red", "power", "Lived with half-sister Ella in Boston’s Roxbury; nicknamed “Detroit Red” in Harlem",
          ["detroit red", "roxbury", "ella"]),
        C("temple-7", "power", "Led Temple No. 7 in Harlem from 1954; founded the newspaper _Muhammad Speaks_",
          ["temple no. 7", "harlem", "muhammad speaks"]),
        C("hate-that-hate", "power", "_The Hate That Hate Produced_ (1959), by Mike Wallace and Louis Lomax, made him nationally known",
          ["hate that hate produced", "mike wallace", "lomax"]),
        C("grass-roots", "power", "“Message to the Grass Roots” (1963, Detroit); called the March on Washington the “Farce on Washington”",
          ["grass roots", "farce on washington"]),
        C("all-colors", "power", "His letter from Mecca described pilgrims “of all colors” worshipping together as equals",
          ["all colors", "letter from mecca"]),
        C("nkrumah", "power", "Met Ghana’s Kwame Nkrumah (1964); modeled the OAAU on the Organization of African Unity",
          ["nkrumah", "ghana", "organization of african unity"]),
        C("selma", "power", "Spoke in Selma (February 1965) while King was jailed; told Coretta Scott King he hoped to make King’s work easier",
          ["selma", "coretta scott king"]),
        C("oxford", "power", "Debated at Oxford (December 1964), defending “extremism in the defense of liberty is no vice”",
          ["oxford", "extremism"]),
        C("united-nations", "power", "Planned to charge the United States with human rights violations at the United Nations",
          ["human rights", "united nations"]),
        C("exoneration", "power", "In 2021, a judge threw out the convictions of Muhammad Aziz and Khalil Islam for his killing",
          ["2021", "muhammad aziz", "khalil islam"]),
        C("ossie-davis", "power", "Actor Ossie Davis’s eulogy called him “our own black shining Prince”",
          ["ossie davis", "shining prince", "eulogy"]),
        C("betty", "power", "Married Betty Sanders in 1958; they had six daughters",
          ["betty", "six daughters", "1958"])
    ],
    "trap": {
        "title": "Minister, mentor, or rival?",
        "body": "Malcolm X tossups are full of other famous names that are answer lines too: Elijah Muhammad, who led the Nation of Islam; Martin Luther King Jr., whose nonviolence he criticized; Muhammad Ali, the boxer he befriended; and Alex Haley, who wrote down his life story. Buzzing with a name you just heard in the clue loses the points. His other names, Malcolm Little and El-Hajj Malik El-Shabazz, are accepted.",
        "fix": "Ask who the clue is really about. “This man” who copied a dictionary in prison, led Temple No. 7, made the hajj in 1964, and was killed at the Audubon Ballroom is Malcolm X. The leader of the whole Nation of Islam from the 1930s to 1975, based in Chicago, is Elijah Muhammad.",
        "line": "Real answer line: <b><u>Malcolm X</u></b> (accept <u>Malcolm Little</u> or <u>El-Hajj Malik El-Shabazz</u>)"
    },
    "tests": {
        "right": [
            "Malcolm X",
            "Malcom X",
            "Malcolm Little",
            "El-Hajj Malik El-Shabazz",
            "Malik El-Shabazz"
        ],
        "prompt": [
            "Malcolm",
            "Detroit Red"
        ],
        "wrong": [
            "Elijah Muhammad",
            "Martin Luther King Jr.",
            "Muhammad Ali",
            "Nation of Islam",
            "Betty Shabazz",
            "Louis Farrakhan",
            "The Autobiography of Malcolm X"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
